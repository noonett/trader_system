"""Configuration for sigma-relay."""

import os
from pathlib import Path

import yaml

DEFAULT_CONFIG = {
    "port": 9733,
    "workspace_root": str(Path(__file__).resolve().parent.parent.parent),
    "trader_id": "default",
    "notify_channels": ["toast"],  # list: toast / wechat_work / pushplus / serverchan
    "wechat_work_webhook_url": "",
    "pushplus_token": "",
    "serverchan_key": "",
    "auto_screenshot": True,
    "screenshot_monitor": 1,
    # TODO: not yet implemented — positions are finalized only by position_closed events.
    # Future: background task to auto-close stale positions after this timeout.
    "partial_fill_timeout_seconds": 60,
}


def get_config() -> dict:
    """Load config from environment and/or config file."""
    config = DEFAULT_CONFIG.copy()

    config_path = Path(__file__).parent / "relay-config.yaml"
    file_config: dict = {}
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            file_config = yaml.safe_load(f) or {}
        config.update(file_config)

    env_overrides = {
        "SIGMA_RELAY_PORT": ("port", int),
        "SIGMA_WORKSPACE_ROOT": ("workspace_root", str),
        "SIGMA_TRADER_ID": ("trader_id", str),
        "SIGMA_WECHAT_WORK_WEBHOOK_URL": ("wechat_work_webhook_url", str),
        "SIGMA_PUSHPLUS_TOKEN": ("pushplus_token", str),
        "SIGMA_SERVERCHAN_KEY": ("serverchan_key", str),
    }

    for env_var, (key, cast) in env_overrides.items():
        val = os.environ.get(env_var)
        if val is not None:
            config[key] = cast(val)

    # Normalize: accept legacy singular key from file config
    if "notify_channel" in file_config and "notify_channels" not in file_config:
        config["notify_channels"] = [file_config["notify_channel"]]

    return config
