"""σ 路径解析 — 多交易员目录结构支持

所有脚本 import 此模块获取路径。支持 --trader 参数（默认 "default"）。
对应 research/design_webui_multitrader_2026.md §五。
"""

import os
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent


def get_trader_root(trader_id=None):
    if trader_id is None:
        trader_id = os.environ.get("SIGMA_TRADER", "default")
    root = WORKSPACE / "traders" / trader_id
    if not root.exists():
        raise FileNotFoundError(f"交易员目录不存在: {root}")
    return root


def get_paths(trader_id=None):
    root = get_trader_root(trader_id)
    return {
        "root": root,
        "daily": root / "daily",
        "trades": root / "trades",
        "reviews": root / "reviews",
        "weekly": root / "reviews" / "weekly",
        "monthly": root / "reviews" / "monthly",
        "violations": root / "reviews" / "violations",
        "alerts": root / "reviews" / "alerts",
        "reconcile": root / "reviews" / "reconcile",
        "profile": root / "profile",
        "config": root / "config.yaml",
    }


def get_shared_paths():
    return {
        "templates": WORKSPACE / "sigma" / "templates",
        "knowledge": WORKSPACE / "knowledge",
        "scripts": WORKSPACE / "scripts",
    }
