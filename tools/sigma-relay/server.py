"""σ sigma-relay — 本地中继服务

接收 ATAS SigmaBridge 推送的交易事件，聚合 partial fills，
在完全平仓时生成交易记录草稿（draft）。

启动：
    cd tools/sigma-relay
    pip install -r requirements.txt
    python server.py

或使用 uvicorn：
    uvicorn server:app --host 127.0.0.1 --port 9733
"""

import json
import logging
import subprocess
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

app = FastAPI(title="σ sigma-relay", version="0.1.0")

event_store = EventStore()

open_positions: dict[tuple[str, str], dict] = {}


@app.on_event("startup")
async def startup():
    """Recover open positions from today's event log (handles restart)."""
    global open_positions
    recovered = event_store.rebuild_open_positions()
    if recovered:
        open_positions.update(recovered)
        logger.info(
            f"Recovered {len(recovered)} open position(s) from event log"
        )


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


class ScreenshotNotification(BaseModel):
    timestamp: str
    symbol: str
    file_path: str
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
        open_positions[key] = {
            "symbol": event.symbol,
            "direction": "long" if event.side.lower() in ("buy", "long") else "short",
            "fills": [],
            "first_fill_time": event.local_time or event.timestamp,
            "account": event.account or "",
            "stop_prices": [],
            "screenshots": [],
        }

    open_positions[key]["fills"].append(
        {
            "price": event.price,
            "qty": event.quantity,
            "time": event.local_time or event.timestamp,
            "trade_id": event.trade_id,
        }
    )

    fill_count = len(open_positions[key]["fills"])
    total_qty = sum(f["qty"] for f in open_positions[key]["fills"])
    logger.info(f"  Aggregated: {fill_count} fills, total qty={total_qty}")

    config = get_config()
    if config.get("auto_screenshot", True):
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

    return {"status": "aggregating", "fills": fill_count, "total_qty": total_qty}


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

    git_commit_draft(draft_path, event.symbol, pos["direction"])

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
    key = (event.symbol, "")
    logger.info(
        f"Order update: {event.symbol} {event.order_type} "
        f"stop={event.stop_price} state={event.order_state}"
    )

    event_store.append(event.model_dump())

    if key in open_positions and event.stop_price > 0:
        open_positions[key]["stop_prices"].append(
            {
                "price": event.stop_price,
                "time": event.timestamp,
                "type": event.order_type,
            }
        )

    return {"status": "recorded"}


@app.post("/screenshot")
async def handle_screenshot(notif: ScreenshotNotification):
    logger.info(f"Screenshot: {notif.symbol} type={notif.capture_type} path={notif.file_path}")
    # TODO: move/copy screenshot to trades/YYYY/MM/screenshots/ and link to draft
    return {"status": "noted", "file_path": notif.file_path}


def git_commit_draft(draft_path: Path, symbol: str, direction: str):
    """Stage and commit the draft file."""
    config = get_config()
    workspace = Path(config["workspace_root"])

    try:
        subprocess.run(
            ["git", "add", str(draft_path)],
            cwd=workspace,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            [
                "git",
                "commit",
                "-m",
                f"draft({symbol}): auto-captured {direction} position closed",
            ],
            cwd=workspace,
            check=True,
            capture_output=True,
        )
        logger.info(f"Git committed: {draft_path.name}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Git commit failed: {e.stderr.decode()}")


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    port = config.get("port", 9733)
    logger.info(f"Starting sigma-relay on 127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)
