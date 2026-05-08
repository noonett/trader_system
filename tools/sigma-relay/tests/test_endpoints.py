"""Integration tests for sigma-relay HTTP endpoints using FastAPI TestClient."""

import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture(autouse=True)
def _clean_state():
    """Reset open_positions and event_store between tests."""
    import server
    from persistence import EventStore

    server.open_positions.clear()
    _orig_store = server.event_store
    with tempfile.TemporaryDirectory() as td:
        server.event_store = EventStore(data_dir=Path(td))
        yield
    server.event_store = _orig_store
    server.open_positions.clear()


@pytest.fixture()
def client():
    from fastapi.testclient import TestClient
    from server import app
    with TestClient(app) as c:
        yield c


class TestHealthEndpoint:
    def test_health_returns_ok(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert "open_positions" in data

    def test_health_reflects_position_count(self, client):
        import server
        from position_core import new_position

        with server._positions_lock:
            server.open_positions[("MGC", "A1")] = new_position(
                "MGC", "A1", "long", "2026-05-08T10:00:00Z"
            )
        resp = client.get("/health")
        assert resp.json()["open_positions"] == 1


class TestTradeEventEndpoint:
    def test_first_trade_creates_position(self, client):
        resp = client.post("/trade-event", json={
            "event_type": "new_trade",
            "timestamp": "2026-05-08T10:00:00Z",
            "symbol": "MGC",
            "price": 4700.0,
            "quantity": 1.0,
            "side": "Buy",
            "account": "A1",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "aggregating"
        assert data["fills"] == 1
        assert data["opening_fill"] is True

    def test_partial_fills_aggregate(self, client):
        payload = {
            "event_type": "new_trade",
            "timestamp": "2026-05-08T10:00:00Z",
            "symbol": "MGC",
            "price": 4700.0,
            "quantity": 1.0,
            "side": "Sell",
            "account": "A1",
        }
        client.post("/trade-event", json=payload)

        payload["price"] = 4695.0
        payload["timestamp"] = "2026-05-08T10:01:00Z"
        resp = client.post("/trade-event", json=payload)
        data = resp.json()
        assert data["fills"] == 2
        assert data["total_qty"] == 2.0

    def test_reducing_fill_not_counted_as_entry(self, client):
        client.post("/trade-event", json={
            "event_type": "new_trade",
            "timestamp": "2026-05-08T10:00:00Z",
            "symbol": "MGC",
            "price": 4700.0,
            "quantity": 1.0,
            "side": "Buy",
            "account": "A1",
        })
        resp = client.post("/trade-event", json={
            "event_type": "new_trade",
            "timestamp": "2026-05-08T10:05:00Z",
            "symbol": "MGC",
            "price": 4710.0,
            "quantity": 1.0,
            "side": "Sell",
            "account": "A1",
        })
        data = resp.json()
        assert data["fills"] == 1
        assert data["opening_fill"] is False


class TestPositionClosedEndpoint:
    @patch("server.capture_screen", return_value=None)
    @patch("server.send_notification")
    def test_position_closed_creates_draft(self, mock_notify, mock_screenshot, client):
        with tempfile.TemporaryDirectory() as td:
            with patch("server.get_config", return_value={
                "workspace_root": td,
                "trader_id": "default",
                "auto_screenshot": False,
                "notify_channels": [],
            }):
                client.post("/trade-event", json={
                    "event_type": "new_trade",
                    "timestamp": "2026-05-08T10:00:00Z",
                    "symbol": "MGC",
                    "price": 4700.0,
                    "quantity": 1.0,
                    "side": "Sell",
                    "account": "A1",
                })

                with patch("server.git_commit_draft"):
                    resp = client.post("/position-closed", json={
                        "event_type": "position_closed",
                        "timestamp": "2026-05-08T11:00:00Z",
                        "symbol": "MGC",
                        "realized_pnl": 50.0,
                        "avg_entry_price": 4700.0,
                        "account": "A1",
                    })

                assert resp.status_code == 200
                assert resp.json()["status"] == "draft_created"

    @patch("server.capture_screen", return_value=None)
    @patch("server.send_notification")
    def test_position_closed_without_prior_trade(self, mock_notify, mock_screenshot, client):
        with tempfile.TemporaryDirectory() as td:
            with patch("server.get_config", return_value={
                "workspace_root": td,
                "trader_id": "default",
                "auto_screenshot": False,
                "notify_channels": [],
            }):
                with patch("server.git_commit_draft"):
                    resp = client.post("/position-closed", json={
                        "event_type": "position_closed",
                        "timestamp": "2026-05-08T11:00:00Z",
                        "symbol": "MGC",
                        "realized_pnl": -20.0,
                        "avg_entry_price": 4700.0,
                        "account": "A1",
                    })
                assert resp.status_code == 200
                assert resp.json()["status"] == "draft_created"


class TestOrderUpdateEndpoint:
    def test_stop_order_recorded(self, client):
        from position_core import new_position
        import server

        with server._positions_lock:
            server.open_positions[("MGC", "A1")] = new_position(
                "MGC", "A1", "short", "2026-05-08T10:00:00Z"
            )

        resp = client.post("/order-update", json={
            "event_type": "stop_order_update",
            "timestamp": "2026-05-08T10:05:00Z",
            "symbol": "MGC",
            "order_state": "Active",
            "stop_price": 4725.0,
            "order_type": "Stop",
            "side": "Buy",
            "account": "A1",
        })
        assert resp.status_code == 200
        assert resp.json()["status"] == "recorded"

        with server._positions_lock:
            stops = server.open_positions[("MGC", "A1")]["stop_prices"]
        assert len(stops) == 1
        assert stops[0]["price"] == 4725.0

    def test_stop_order_no_match_returns_ignored(self, client):
        resp = client.post("/order-update", json={
            "event_type": "stop_order_update",
            "timestamp": "2026-05-08T10:05:00Z",
            "symbol": "UNKNOWN",
            "order_state": "Active",
            "stop_price": 100.0,
            "order_type": "Stop",
            "side": "Buy",
            "account": "X",
        })
        assert resp.status_code == 200
        assert resp.json()["status"] == "ignored_no_match"


class TestPositionsEndpoint:
    def test_positions_empty(self, client):
        resp = client.get("/positions")
        assert resp.status_code == 200
        assert resp.json()["open_positions"] == {}

    def test_positions_reflects_trades(self, client):
        client.post("/trade-event", json={
            "event_type": "new_trade",
            "timestamp": "2026-05-08T10:00:00Z",
            "symbol": "MGC",
            "price": 4700.0,
            "quantity": 2.0,
            "side": "Buy",
            "account": "A1",
        })
        resp = client.get("/positions")
        positions = resp.json()["open_positions"]
        assert "MGC|A1" in positions
        assert positions["MGC|A1"]["total_qty"] == 2.0
