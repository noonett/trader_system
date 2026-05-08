"""σ sigma-relay — 本地中继服务

接收 ATAS SigmaBridge 推送的交易事件，聚合 partial fills，
在完全平仓时生成交易记录草稿（draft）。

启动：
    cd tools/sigma-relay
    pip install -r requirements.txt
    python server.py

或使用 uvicorn：
    uvicorn server:app --host 127.0.0.1 --port 9733

安全模型：
    - 仅绑定 127.0.0.1（不接受外部连接）
    - 无鉴权（威胁模型：信任本机所有进程）
    - 如果需要暴露到网络（如内网穿透），必须添加 API Key 鉴权
    - 事件日志存储在本地磁盘，不包含账户密码类敏感信息
"""

import json
import logging
import subprocess
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from draft_generator import generate_draft_markdown
from config import get_config
from screenshot import capture_screen, move_to_trade_screenshots
from notify import send_notification
from persistence import EventStore

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("sigma-relay.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("sigma-relay")

event_store = EventStore()

open_positions: dict[tuple[str, str], dict] = {}


def _side_to_direction(side: str) -> str:
    return "long" if side.lower() in ("buy", "long") else "short"


def _is_opening_fill(direction: str, side: str) -> bool:
    normalized_side = side.lower()
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
        # Remaining quantity in the original direction.
        "remaining_qty": 0.0,
    }


def _apply_trade_to_position(
    position: dict,
    *,
    price: float,
    quantity: float,
    trade_time: str,
    trade_id: Optional[str],
    side: str,
) -> bool:
    """Apply one fill to a position.

    Returns True if this is an opening fill in position direction, False otherwise.
    Closing/reducing fills update remaining_qty but are excluded from entry fills,
    so draft entry metrics stay accurate.
    """
    qty = float(quantity)
    if qty <= 0:
        logger.warning(f"Ignoring non-positive quantity fill: qty={quantity}")
        return False

    if _is_opening_fill(position["direction"], side):
        position["fills"].append(
            {
                "price": price,
                "qty": qty,
                "time": trade_time,
                "trade_id": trade_id,
            }
        )
        position["remaining_qty"] = float(position.get("remaining_qty", 0.0)) + qty
        return True

    remaining_qty = float(position.get("remaining_qty", 0.0))
    if remaining_qty <= 0:
        logger.warning(
            f"Received reducing fill with no open qty for {position['symbol']} "
            f"{position.get('account', '')}: {side} {qty}@{price}"
        )
        return False

    new_remaining = remaining_qty - qty
    position["remaining_qty"] = max(0.0, new_remaining)
    if new_remaining < 0:
        logger.warning(
            f"Reducing fill exceeded tracked qty for {position['symbol']} "
            f"{position.get('account', '')}: reduce={qty}, tracked={remaining_qty}"
        )
    return False


def _resolve_position_key(symbol: str, account: str, *, context: str) -> Optional[tuple[str, str]]:
    """Resolve position key safely.

    Exact (symbol, account) match first. Symbol-only fallback is allowed only when
    there is exactly one candidate; otherwise skip to avoid wrong attribution.
    """
    exact_key = (symbol, account or "")
    if exact_key in open_positions:
        return exact_key

    candidates = [k for k in open_positions if k[0] == symbol]
    if not candidates:
        return None
    if len(candidates) == 1:
        return candidates[0]

    candidate_accounts = [acc for _, acc in candidates]
    logger.warning(
        f"Ambiguous {context} position match for symbol={symbol} account={account or '<empty>'} "
        f"candidates={candidate_accounts}; skipping fallback."
    )
    return None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup: recover open positions from recent event logs.
    Optionally start file watcher for ATAS sandbox fallback mode.
    """
    global open_positions
    recovered = event_store.rebuild_open_positions()
    if recovered:
        open_positions.update(recovered)
        logger.info(
            f"Recovered {len(recovered)} open position(s) from event log "
            f"(lookback: 3 days)"
        )

    # Start file watcher if configured (fallback for ATAS sandbox blocking HTTP)
    config = get_config()
    watcher_thread = None
    watch_dir = config.get("file_watcher_dir", "")
    if watch_dir:
        from file_watcher import start_file_watcher
        watcher_thread = start_file_watcher(
            watch_dir=watch_dir,
            callback=_handle_file_event,
        )
        if watcher_thread:
            logger.info(f"File watcher active: {watch_dir}")

    yield


app = FastAPI(title="σ sigma-relay", version="0.1.0", lifespan=lifespan)


class TradeEvent(BaseModel):
    event_type: str
    timestamp: str
    local_time: Optional[str] = None
    symbol: str
    price: float
    quantity: float
    side: str
    account: Optional[str] = ""
    trade_id: Optional[str] = None


class PositionClosed(BaseModel):
    event_type: str
    timestamp: str
    symbol: str
    realized_pnl: float
    avg_entry_price: float
    account: Optional[str] = ""


class OrderUpdate(BaseModel):
    event_type: str
    timestamp: str
    symbol: str
    order_state: str
    stop_price: float
    order_type: str
    side: str
    account: Optional[str] = ""


class ScreenshotNotification(BaseModel):
    timestamp: str
    symbol: str
    file_path: str
    account: Optional[str] = ""
    capture_type: str = "entry"  # entry / exit / context


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "open_positions": len(open_positions),
        "uptime": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/events")
async def get_events(date: Optional[str] = None):
    """Query stored events. Defaults to today."""
    if date is None:
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    events = event_store.load_date(date)
    return {"date": date, "count": len(events), "events": events}


@app.get("/positions")
async def get_positions():
    """Query current open positions being tracked."""
    result = {}
    for (symbol, account), pos in open_positions.items():
        fills = pos.get("fills", [])
        total_qty = sum(f["qty"] for f in fills)
        result[f"{symbol}|{account}"] = {
            "symbol": symbol,
            "direction": pos["direction"],
            "fills": len(fills),
            "total_qty": total_qty,
            "first_fill": pos.get("first_fill_time", ""),
        }
    return {"open_positions": result}


@app.post("/trade-event")
async def handle_trade(event: TradeEvent):
    key = (event.symbol, event.account or "")
    logger.info(
        f"Trade event: {event.symbol} {event.side} {event.quantity}@{event.price}"
    )

    event_store.append(event.model_dump())

    if key not in open_positions:
        open_positions[key] = _new_position(
            symbol=event.symbol,
            account=event.account or "",
            direction=_side_to_direction(event.side),
            first_fill_time=event.local_time or event.timestamp,
        )

    is_opening_fill = _apply_trade_to_position(
        open_positions[key],
        price=event.price,
        quantity=event.quantity,
        trade_time=event.local_time or event.timestamp,
        trade_id=event.trade_id,
        side=event.side,
    )

    fill_count = len(open_positions[key]["fills"])
    total_qty = sum(f["qty"] for f in open_positions[key]["fills"])
    remaining_qty = float(open_positions[key].get("remaining_qty", 0.0))
    logger.info(
        f"  Aggregated entry fills: {fill_count}, entry qty={total_qty}, "
        f"open qty={remaining_qty}"
    )

    config = get_config()
    if config.get("auto_screenshot", True) and is_opening_fill:
        capture_type = "entry" if fill_count == 1 else "context"
        screenshot_path = capture_screen(
            symbol=event.symbol,
            capture_type=capture_type,
            monitor_index=config.get("screenshot_monitor", 0),
        )
        if screenshot_path:
            open_positions[key]["screenshots"].append(
                {"path": str(screenshot_path), "type": capture_type}
            )

    return {
        "status": "aggregating",
        "fills": fill_count,
        "total_qty": total_qty,
        "open_qty": remaining_qty,
        "opening_fill": is_opening_fill,
    }


@app.post("/position-closed")
async def handle_close(event: PositionClosed):
    key = (event.symbol, event.account or "")
    logger.info(
        f"Position closed: {event.symbol} PnL={event.realized_pnl} "
        f"avg_entry={event.avg_entry_price}"
    )

    event_store.append(event.model_dump())

    pos = open_positions.pop(key, None)
    if pos is None:
        logger.warning(
            f"No open position found for {key}. "
            "Relay may have restarted. Creating minimal draft."
        )
        pos = {
            "symbol": event.symbol,
            "direction": "unknown",
            "fills": [],
            "first_fill_time": event.timestamp,
            "account": event.account or "",
            "stop_prices": [],
            "screenshots": [],
            "remaining_qty": 0.0,
        }

    config = get_config()

    if config.get("auto_screenshot", True):
        exit_screenshot = capture_screen(
            symbol=event.symbol,
            capture_type="exit",
            monitor_index=config.get("screenshot_monitor", 0),
        )
        if exit_screenshot:
            pos["screenshots"].append({"path": str(exit_screenshot), "type": "exit"})

    draft_path = generate_draft_markdown(pos, event, config)

    # Move screenshots to trade's screenshots/ dir and collect final paths
    committed_screenshots = []
    trades_dir = draft_path.parent
    for ss in pos.get("screenshots", []):
        ss_path = Path(ss["path"])
        if ss_path.exists():
            final_path = move_to_trade_screenshots(
                screenshot_path=ss_path,
                trades_dir=trades_dir,
                trade_date=datetime.now().strftime("%Y-%m-%d"),
                symbol=event.symbol.lower().replace("/", "").replace(" ", ""),
                direction=pos["direction"],
                capture_type=ss["type"],
            )
            if final_path:
                committed_screenshots.append(final_path)

    git_commit_draft(draft_path, event.symbol, pos["direction"], committed_screenshots)

    pnl_str = f"+{event.realized_pnl}" if event.realized_pnl >= 0 else str(event.realized_pnl)
    send_notification(
        title=f"σ Draft: {event.symbol} {pos['direction']}",
        message=(
            f"PnL: {pnl_str} | Entry: {event.avg_entry_price}\n"
            f"Draft: {draft_path.name}\n"
            f"待补填：决策链 5 问 + 盘后 EMA"
        ),
        config=config,
        urgency="high" if event.realized_pnl < 0 else "normal",
    )

    return {"status": "draft_created", "path": str(draft_path)}


@app.post("/order-update")
async def handle_order(event: OrderUpdate):
    logger.info(
        f"Order update: {event.symbol} {event.order_type} "
        f"stop={event.stop_price} state={event.order_state}"
    )

    event_store.append(event.model_dump())

    if event.stop_price > 0:
        resolved_key = _resolve_position_key(
            event.symbol,
            event.account or "",
            context="order-update",
        )
        if resolved_key is None:
            logger.warning(
                f"Skipping stop update without unique position: "
                f"symbol={event.symbol} account={event.account or '<empty>'}"
            )
            return {"status": "ignored_no_match"}

        open_positions[resolved_key]["stop_prices"].append(
            {
                "price": event.stop_price,
                "time": event.timestamp,
                "type": event.order_type,
            }
        )

    return {"status": "recorded"}


@app.post("/screenshot")
async def handle_screenshot(notif: ScreenshotNotification):
    """Receive screenshot notification and associate with current open position."""
    logger.info(
        f"Screenshot: {notif.symbol} account={notif.account or '<empty>'} "
        f"type={notif.capture_type} path={notif.file_path}"
    )

    matched_key = _resolve_position_key(
        notif.symbol,
        notif.account or "",
        context="screenshot",
    )

    if matched_key and Path(notif.file_path).exists():
        open_positions[matched_key]["screenshots"].append(
            {"path": notif.file_path, "type": notif.capture_type}
        )
        return {"status": "associated", "position": matched_key[0]}

    return {"status": "noted_no_position", "file_path": notif.file_path}


def git_commit_draft(draft_path: Path, symbol: str, direction: str, screenshot_paths: list[Path] = None):
    """Stage and commit only the draft file (+ screenshots), nothing else.

    Uses a temporary index to avoid committing unrelated staged changes.
    """
    config = get_config()
    workspace = Path(config["workspace_root"])
    paths_to_commit = [str(draft_path)]
    if screenshot_paths:
        paths_to_commit.extend(str(p) for p in screenshot_paths)

    try:
        # Reset index for target files only, then commit with -- pathspec
        # This ensures only our files go in, even if other things are staged.
        subprocess.run(
            ["git", "add", "--"] + paths_to_commit,
            cwd=workspace,
            check=True,
            capture_output=True,
        )

        # Verify only our files are being committed
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            cwd=workspace,
            capture_output=True,
            text=True,
        )
        staged = set(result.stdout.strip().splitlines()) if result.stdout.strip() else set()
        our_files = set(
            str(Path(p).relative_to(workspace)) for p in paths_to_commit
            if Path(p).is_relative_to(workspace)
        )
        extra_staged = staged - our_files
        if extra_staged:
            logger.warning(
                f"Extra staged files detected (won't be committed): {extra_staged}"
            )
            # Use pathspec to commit only our files
            subprocess.run(
                ["git", "commit", "-m",
                 f"draft({symbol}): auto-captured {direction} position closed",
                 "--"] + paths_to_commit,
                cwd=workspace,
                check=True,
                capture_output=True,
            )
        else:
            subprocess.run(
                ["git", "commit", "-m",
                 f"draft({symbol}): auto-captured {direction} position closed"],
                cwd=workspace,
                check=True,
                capture_output=True,
            )

        logger.info(f"Git committed: {draft_path.name}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Git commit failed: {e.stderr.decode() if e.stderr else str(e)}")


def _handle_file_event(event_data: dict):
    """Callback for file_watcher: injects events into the same pipeline as HTTP."""
    import asyncio

    event_type = event_data.get("event_type", "")
    logger.info(f"File watcher event: {event_type} {event_data.get('symbol', '?')}")

    event_store.append(event_data)

    if event_type == "new_trade":
        key = (event_data.get("symbol", ""), event_data.get("account", ""))
        if key not in open_positions:
            side = event_data.get("side", "")
            open_positions[key] = _new_position(
                symbol=event_data.get("symbol", ""),
                account=event_data.get("account", ""),
                direction=_side_to_direction(side),
                first_fill_time=event_data.get("local_time") or event_data.get("timestamp", ""),
            )
        _apply_trade_to_position(
            open_positions[key],
            price=event_data.get("price", 0),
            quantity=event_data.get("quantity", 0),
            trade_time=event_data.get("local_time") or event_data.get("timestamp", ""),
            trade_id=event_data.get("trade_id"),
            side=event_data.get("side", ""),
        )

    elif event_type == "position_closed":
        key = (event_data.get("symbol", ""), event_data.get("account", ""))
        pos = open_positions.pop(key, None)
        if pos is None:
            pos = {
                "symbol": event_data.get("symbol", ""),
                "direction": "unknown",
                "fills": [],
                "first_fill_time": event_data.get("timestamp", ""),
                "account": event_data.get("account", ""),
                "stop_prices": [],
                "screenshots": [],
                "remaining_qty": 0.0,
            }
        config = get_config()

        class _CloseMock:
            realized_pnl = event_data.get("realized_pnl", 0)
            avg_entry_price = event_data.get("avg_entry_price", 0)
            timestamp = event_data.get("timestamp", "")
            account = event_data.get("account", "")

        draft_path = generate_draft_markdown(pos, _CloseMock(), config)
        git_commit_draft(draft_path, event_data.get("symbol", ""), pos["direction"])
        pnl = event_data.get("realized_pnl", 0)
        pnl_str = f"+{pnl}" if pnl >= 0 else str(pnl)
        send_notification(
            title=f"σ Draft: {event_data.get('symbol', '?')} {pos['direction']}",
            message=f"PnL: {pnl_str}\nDraft: {draft_path.name}\n待补填：决策链 5 问 + 盘后 EMA",
            config=config,
        )

    elif event_type == "stop_order_update":
        resolved_key = _resolve_position_key(
            event_data.get("symbol", ""),
            event_data.get("account", ""),
            context="file-watcher-stop-update",
        )
        if resolved_key and event_data.get("stop_price", 0) > 0:
            open_positions[resolved_key]["stop_prices"].append({
                "price": event_data["stop_price"],
                "time": event_data.get("timestamp", ""),
                "type": event_data.get("order_type", ""),
            })


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    port = config.get("port", 9733)
    logger.info(f"Starting sigma-relay on 127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)
