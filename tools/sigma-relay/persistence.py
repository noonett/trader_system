"""事件持久化 — 所有收到的原始交易事件写入 JSONL 日志。

目的：
1. 即使 sigma-relay 崩溃/重启，事件不丢失
2. 可回溯所有成交记录（独立于 ATAS 本身的导出）
3. 作为 reconcile_funds.py 的数据源（替代手动导出 CSV）
4. 调试用：可以 replay 事件流

存储格式：每日一个 JSONL 文件
  data/events/2026-05-08.jsonl
  每行一个 JSON 对象，含 received_at 时间戳
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

logger = logging.getLogger("sigma-relay.persistence")


def _side_to_direction(side: str) -> str:
    return "long" if str(side).lower() in ("buy", "long") else "short"


def _is_opening_fill(direction: str, side: str) -> bool:
    normalized_side = str(side).lower()
    if direction == "long":
        return normalized_side in ("buy", "long")
    if direction == "short":
        return normalized_side in ("sell", "short")
    return True


def _new_position(symbol: str, account: str, direction: str, first_fill_time: str) -> dict:
    return {
        "symbol": symbol,
        "direction": direction,
        "fills": [],
        "first_fill_time": first_fill_time,
        "account": account,
        "stop_prices": [],
        "screenshots": [],
        "remaining_qty": 0.0,
    }


def _apply_trade_to_position(position: dict, event: dict) -> None:
    qty = float(event.get("quantity", 0) or 0)
    if qty <= 0:
        return

    if _is_opening_fill(position["direction"], event.get("side", "")):
        position["fills"].append({
            "price": event.get("price", 0),
            "qty": qty,
            "time": event.get("local_time") or event.get("timestamp", ""),
            "trade_id": event.get("trade_id"),
        })
        position["remaining_qty"] = float(position.get("remaining_qty", 0.0)) + qty
        return

    remaining_qty = float(position.get("remaining_qty", 0.0))
    position["remaining_qty"] = max(0.0, remaining_qty - qty)


class EventStore:
    """Append-only event log with daily rotation."""

    def __init__(self, data_dir: Optional[Path] = None):
        if data_dir is None:
            data_dir = Path(__file__).parent / "data" / "events"
        self.data_dir = data_dir
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._current_date: Optional[str] = None
        self._current_file = None

    def append(self, event: dict) -> None:
        """Append an event to today's log file."""
        now = datetime.now(timezone.utc)
        today = now.strftime("%Y-%m-%d")

        record = {
            "received_at": now.isoformat(),
            **event,
        }

        filepath = self.data_dir / f"{today}.jsonl"
        try:
            with open(filepath, "a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
        except Exception as e:
            logger.error(f"Failed to persist event: {e}")

    def load_today(self) -> list[dict]:
        """Load all events from today's log."""
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        return self.load_date(today)

    def load_date(self, date_str: str) -> list[dict]:
        """Load all events from a specific date."""
        filepath = self.data_dir / f"{date_str}.jsonl"
        if not filepath.exists():
            return []

        events = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        events.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
        return events

    def rebuild_open_positions(self, lookback_days: int = 3) -> dict[tuple[str, str], dict]:
        """Rebuild in-memory open_positions from recent event logs.

        Replays the last `lookback_days` of events to handle:
        - Cross-day positions (opened yesterday, still held today)
        - UTC/local timezone day boundary differences
        - Relay restart after multi-day downtime

        Logic: replay all trade events across recent files, remove those
        that had position_closed.
        """
        from datetime import timedelta

        all_events = []
        today = datetime.now(timezone.utc)
        for offset in range(lookback_days, -1, -1):
            day = (today - timedelta(days=offset)).strftime("%Y-%m-%d")
            all_events.extend(self.load_date(day))

        positions: dict[tuple[str, str], dict] = {}
        closed_keys: set[tuple[str, str]] = set()

        for ev in all_events:
            event_type = ev.get("event_type", "")
            symbol = ev.get("symbol", "")
            account = ev.get("account", "")
            key = (symbol, account)

            if event_type == "new_trade":
                if key in closed_keys:
                    # This trade was for a position that already closed;
                    # could be a new position opened after the close.
                    # Reset if we see new trades after a close.
                    closed_keys.discard(key)

                if key not in positions:
                    positions[key] = _new_position(
                        symbol=symbol,
                        account=account,
                        direction=_side_to_direction(ev.get("side", "")),
                        first_fill_time=ev.get("local_time") or ev.get("timestamp", ""),
                    )
                _apply_trade_to_position(positions[key], ev)

            elif event_type == "position_closed":
                closed_keys.add(key)
                positions.pop(key, None)

            elif event_type == "stop_order_update":
                if key in positions and ev.get("stop_price", 0) > 0:
                    positions[key]["stop_prices"].append({
                        "price": ev["stop_price"],
                        "time": ev.get("timestamp", ""),
                        "type": ev.get("order_type", ""),
                    })

        return positions
