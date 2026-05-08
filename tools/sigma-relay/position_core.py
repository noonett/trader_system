"""Shared position logic used by both server.py (live) and persistence.py (replay).

Single source of truth for how fills are classified and positions are tracked.
"""

import logging
from typing import Optional

logger = logging.getLogger("sigma-relay.position_core")


def side_to_direction(side: str) -> str:
    return "long" if str(side).lower() in ("buy", "long") else "short"


def is_opening_fill(direction: str, side: str) -> bool:
    normalized_side = str(side).lower()
    if direction == "long":
        return normalized_side in ("buy", "long")
    if direction == "short":
        return normalized_side in ("sell", "short")
    return True


def new_position(symbol: str, account: str, direction: str, first_fill_time: str) -> dict:
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


def apply_trade_to_position(
    position: dict,
    *,
    price: float,
    quantity: float,
    trade_time: str,
    trade_id: Optional[str] = None,
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

    if is_opening_fill(position["direction"], side):
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


def apply_trade_event_dict(position: dict, event: dict) -> bool:
    """Convenience wrapper for apply_trade_to_position using a raw event dict."""
    return apply_trade_to_position(
        position,
        price=event.get("price", 0),
        quantity=float(event.get("quantity", 0) or 0),
        trade_time=event.get("local_time") or event.get("timestamp", ""),
        trade_id=event.get("trade_id"),
        side=event.get("side", ""),
    )
