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

open_positions: dict[tuple[str, str], dict] = {}


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


@app.post("/trade-event")
async def handle_trade(event: TradeEvent):
    key = (event.symbol, event.account or "")
    logger.info(
        f"Trade event: {event.symbol} {event.side} {event.quantity}@{event.price}"
    )

    if key not in open_positions:
        open_positions[key] = {
            "symbol": event.symbol,
            "direction": "long" if event.side.lower() in ("buy", "long") else "short",
            "fills": [],
            "first_fill_time": event.local_time or event.timestamp,
            "account": event.account or "",
            "stop_prices": [],
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

    return {"status": "aggregating", "fills": fill_count, "total_qty": total_qty}


@app.post("/position-closed")
async def handle_close(event: PositionClosed):
    key = (event.symbol, event.account or "")
    logger.info(
        f"Position closed: {event.symbol} PnL={event.realized_pnl} "
        f"avg_entry={event.avg_entry_price}"
    )

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
        }

    config = get_config()
    draft_path = generate_draft_markdown(pos, event, config)

    git_commit_draft(draft_path, event.symbol, pos["direction"])
    notify_user(draft_path, event.symbol, event.realized_pnl)

    return {"status": "draft_created", "path": str(draft_path)}


@app.post("/order-update")
async def handle_order(event: OrderUpdate):
    key = (event.symbol, "")
    logger.info(
        f"Order update: {event.symbol} {event.order_type} "
        f"stop={event.stop_price} state={event.order_state}"
    )

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


def notify_user(draft_path: Path, symbol: str, pnl: float):
    """Send notification that a draft is ready for review."""
    config = get_config()
    channel = config.get("notify_channel", "log")
    pnl_str = f"+{pnl}" if pnl >= 0 else str(pnl)
    message = f"📝 Draft ready: {symbol} (PnL: {pnl_str}) → {draft_path.name}"

    if channel == "log":
        logger.info(f"NOTIFY: {message}")
    elif channel == "telegram":
        _send_telegram(message, config)
    elif channel == "webhook":
        _send_webhook(message, config)


def _send_telegram(message: str, config: dict):
    """Send via Telegram Bot API."""
    import httpx

    bot_token = config.get("telegram_bot_token", "")
    chat_id = config.get("telegram_chat_id", "")
    if not bot_token or not chat_id:
        logger.warning("Telegram not configured")
        return
    try:
        httpx.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={"chat_id": chat_id, "text": message},
            timeout=5,
        )
    except Exception as e:
        logger.error(f"Telegram send failed: {e}")


def _send_webhook(message: str, config: dict):
    """Send to arbitrary webhook URL."""
    import httpx

    url = config.get("webhook_url", "")
    if not url:
        logger.warning("Webhook URL not configured")
        return
    try:
        httpx.post(url, json={"text": message}, timeout=5)
    except Exception as e:
        logger.error(f"Webhook send failed: {e}")


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    port = config.get("port", 9733)
    logger.info(f"Starting sigma-relay on 127.0.0.1:{port}")
    uvicorn.run(app, host="127.0.0.1", port=port)
