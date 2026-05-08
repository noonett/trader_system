"""Tests for sigma-relay core logic."""

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import MagicMock

import pytest


class TestPositionAggregation:
    """Test that partial fills aggregate correctly."""

    def test_single_fill(self):
        from draft_generator import generate_draft_markdown

        pos = {
            "symbol": "MGCM6",
            "direction": "short",
            "fills": [{"price": 4722.0, "qty": 1, "time": "2026-05-06T22:23:03Z"}],
            "first_fill_time": "2026-05-06T22:23:03Z",
            "account": "S50K",
            "stop_prices": [],
            "screenshots": [],
        }
        close_event = MagicMock()
        close_event.realized_pnl = -38.0
        close_event.avg_entry_price = 4722.0
        close_event.timestamp = "2026-05-06T22:43:13Z"
        close_event.account = "S50K"

        with tempfile.TemporaryDirectory() as td:
            config = {"workspace_root": td, "trader_id": "default"}
            # Create the expected directory
            trades_dir = Path(td) / "traders" / "default" / "trades" / "2026/05"
            trades_dir.mkdir(parents=True)

            path = generate_draft_markdown(pos, close_event, config)
            assert path.exists()
            content = path.read_text()
            assert "date: 2026-05-06" in content
            assert "symbol: MGCM6" in content
            assert "direction: short" in content
            assert "entry_price: 4722.0" in content
            assert "pnl_gross: -38.0" in content
            assert "status: draft" in content

    def test_multi_fill_weighted_average(self):
        from draft_generator import generate_draft_markdown

        pos = {
            "symbol": "MGCM6",
            "direction": "short",
            "fills": [
                {"price": 4722.0, "qty": 1, "time": "2026-05-06T22:23:03Z"},
                {"price": 4717.7, "qty": 1, "time": "2026-05-06T22:30:06Z"},
            ],
            "first_fill_time": "2026-05-06T22:23:03Z",
            "account": "S50K",
            "stop_prices": [{"price": 4725.8, "time": "2026-05-06T22:25:00Z", "type": "Stop"}],
            "screenshots": [],
        }
        close_event = MagicMock()
        close_event.realized_pnl = -119.0
        close_event.avg_entry_price = 4719.85
        close_event.timestamp = "2026-05-06T22:43:13Z"
        close_event.account = "S50K"

        with tempfile.TemporaryDirectory() as td:
            config = {"workspace_root": td, "trader_id": "default"}
            trades_dir = Path(td) / "traders" / "default" / "trades" / "2026/05"
            trades_dir.mkdir(parents=True)

            path = generate_draft_markdown(pos, close_event, config)
            content = path.read_text()
            assert "entry_price: 4719.85" in content
            assert "position_size: 2" in content
            assert "stop_loss_price: 4725.8" in content

    def test_frontmatter_is_valid_yaml(self):
        """Verify the frontmatter can be parsed as YAML."""
        import yaml
        from draft_generator import generate_draft_markdown

        pos = {
            "symbol": "MESM6",
            "direction": "long",
            "fills": [{"price": 5500.0, "qty": 1, "time": "2026-05-08T10:00:00Z"}],
            "first_fill_time": "2026-05-08T10:00:00Z",
            "account": "test",
            "stop_prices": [],
            "screenshots": [],
        }
        close_event = MagicMock()
        close_event.realized_pnl = 50.0
        close_event.avg_entry_price = 5500.0
        close_event.timestamp = "2026-05-08T11:00:00Z"
        close_event.account = "test"

        with tempfile.TemporaryDirectory() as td:
            config = {"workspace_root": td, "trader_id": "default"}
            trades_dir = Path(td) / "traders" / "default" / "trades" / "2026/05"
            trades_dir.mkdir(parents=True)

            path = generate_draft_markdown(pos, close_event, config)
            content = path.read_text()

            # Extract frontmatter between --- delimiters
            parts = content.split("---")
            assert len(parts) >= 3, "Should have --- delimiters"
            fm_text = parts[1]
            fm = yaml.safe_load(fm_text)
            assert fm["date"] == datetime(2026, 5, 8).date()
            assert fm["symbol"] == "MESM6"
            assert fm["direction"] == "long"
            assert fm["status"] == "draft"


class TestPersistence:
    """Test EventStore persistence and recovery."""

    def test_append_and_load(self):
        from persistence import EventStore

        with tempfile.TemporaryDirectory() as td:
            store = EventStore(data_dir=Path(td))
            event = {
                "event_type": "new_trade",
                "symbol": "MGCM6",
                "price": 4722.0,
                "quantity": 1,
                "side": "Sell",
                "account": "S50K",
            }
            store.append(event)

            today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            loaded = store.load_date(today)
            assert len(loaded) == 1
            assert loaded[0]["symbol"] == "MGCM6"
            assert "received_at" in loaded[0]

    def test_rebuild_open_positions(self):
        from persistence import EventStore

        with tempfile.TemporaryDirectory() as td:
            store = EventStore(data_dir=Path(td))

            # Simulate: open position (2 fills) + stop update, no close
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4700, "quantity": 1, "side": "Sell", "account": "A1"})
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4695, "quantity": 1, "side": "Sell", "account": "A1"})
            store.append({"event_type": "stop_order_update", "symbol": "MGC", "stop_price": 4710, "account": "A1", "order_type": "Stop"})

            positions = store.rebuild_open_positions()
            assert ("MGC", "A1") in positions
            pos = positions[("MGC", "A1")]
            assert len(pos["fills"]) == 2
            assert pos["direction"] == "short"
            assert pos["remaining_qty"] == 2
            assert len(pos["stop_prices"]) == 1
            assert pos["stop_prices"][0]["price"] == 4710

    def test_rebuild_ignores_reducing_fills_in_entry_metrics(self):
        from persistence import EventStore

        with tempfile.TemporaryDirectory() as td:
            store = EventStore(data_dir=Path(td))

            # Open long 1, then reduce 1 (without explicit position_closed event).
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4700, "quantity": 1, "side": "Buy", "account": "A1"})
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4710, "quantity": 1, "side": "Sell", "account": "A1"})

            positions = store.rebuild_open_positions()
            assert ("MGC", "A1") in positions
            pos = positions[("MGC", "A1")]
            assert len(pos["fills"]) == 1
            assert pos["fills"][0]["price"] == 4700
            assert pos["remaining_qty"] == 0

    def test_rebuild_excludes_closed(self):
        from persistence import EventStore

        with tempfile.TemporaryDirectory() as td:
            store = EventStore(data_dir=Path(td))

            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4700, "quantity": 1, "side": "Sell", "account": "A1"})
            store.append({"event_type": "position_closed", "symbol": "MGC", "account": "A1", "realized_pnl": 50})

            positions = store.rebuild_open_positions()
            assert ("MGC", "A1") not in positions

    def test_rebuild_handles_reopen_after_close(self):
        from persistence import EventStore

        with tempfile.TemporaryDirectory() as td:
            store = EventStore(data_dir=Path(td))

            # First position: open then close
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4700, "quantity": 1, "side": "Sell", "account": "A1"})
            store.append({"event_type": "position_closed", "symbol": "MGC", "account": "A1", "realized_pnl": 50})
            # Second position: reopen
            store.append({"event_type": "new_trade", "symbol": "MGC", "price": 4720, "quantity": 2, "side": "Buy", "account": "A1"})

            positions = store.rebuild_open_positions()
            assert ("MGC", "A1") in positions
            pos = positions[("MGC", "A1")]
            assert len(pos["fills"]) == 1
            assert pos["fills"][0]["price"] == 4720
            assert pos["direction"] == "long"


class TestOrderKeyConsistency:
    """Verify order-update uses the same key as trade/position events."""

    def test_order_update_model_has_account(self):
        """OrderUpdate must accept account field."""
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent))
        from server import OrderUpdate

        ou = OrderUpdate(
            event_type="stop_order_update",
            timestamp="2026-05-08T10:00:00Z",
            symbol="MGC",
            order_state="Active",
            stop_price=4725.0,
            order_type="Stop",
            side="Buy",
            account="S50K",
        )
        assert ou.account == "S50K"


class TestServerSafetyHelpers:
    """Test key safety helpers in server.py."""

    def test_apply_trade_to_position_excludes_reducing_fill_from_entry(self):
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent))
        import server

        pos = server._new_position(
            symbol="MGC",
            account="A1",
            direction="long",
            first_fill_time="2026-05-08T10:00:00Z",
        )

        assert server._apply_trade_to_position(
            pos,
            price=4700,
            quantity=1,
            trade_time="2026-05-08T10:00:00Z",
            trade_id="t1",
            side="Buy",
        )
        assert not server._apply_trade_to_position(
            pos,
            price=4710,
            quantity=1,
            trade_time="2026-05-08T10:05:00Z",
            trade_id="t2",
            side="Sell",
        )

        assert len(pos["fills"]) == 1
        assert sum(f["qty"] for f in pos["fills"]) == 1
        assert pos["remaining_qty"] == 0

    def test_symbol_only_fallback_requires_unique_match(self):
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent))
        import server

        server.open_positions.clear()
        try:
            server.open_positions[("MGC", "A1")] = server._new_position(
                symbol="MGC",
                account="A1",
                direction="long",
                first_fill_time="2026-05-08T10:00:00Z",
            )
            server.open_positions[("MGC", "A2")] = server._new_position(
                symbol="MGC",
                account="A2",
                direction="short",
                first_fill_time="2026-05-08T10:01:00Z",
            )

            assert server._resolve_position_key("MGC", "A1", context="test") == ("MGC", "A1")
            assert server._resolve_position_key("MGC", "", context="test") is None

            server.open_positions.pop(("MGC", "A2"))
            assert server._resolve_position_key("MGC", "", context="test") == ("MGC", "A1")
        finally:
            server.open_positions.clear()
