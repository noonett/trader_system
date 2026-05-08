"""Configuration for sigma-relay."""

import os
from pathlib import Path

import yaml

DEFAULT_CONFIG = {
    "port": 9733,
    "workspace_root": str(Path(__file__).resolve().parent.parent.parent),
    "trader_id": "default",
    "notify_channel": "log",  # log / telegram / webhook
    "telegram_bot_token": "",
    "telegram_chat_id": "",
    "webhook_url": "",
    "screenshot_watch_dir": "",  # 如果启用文件监控截图
    "partial_fill_timeout_seconds": 60,  # 多久没有新 fill 视为开仓完成
}


def get_config() -> dict:
    """Load config from environment and/or config file."""
    config = DEFAULT_CONFIG.copy()

    config_path = Path(__file__).parent / "relay-config.yaml"
    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            file_config = yaml.safe_load(f) or {}
        config.update(file_config)

    env_overrides = {
        "SIGMA_RELAY_PORT": ("port", int),
        "SIGMA_WORKSPACE_ROOT": ("workspace_root", str),
        "SIGMA_TRADER_ID": ("trader_id", str),
        "SIGMA_NOTIFY_CHANNEL": ("notify_channel", str),
        "SIGMA_TELEGRAM_BOT_TOKEN": ("telegram_bot_token", str),
        "SIGMA_TELEGRAM_CHAT_ID": ("telegram_chat_id", str),
        "SIGMA_WEBHOOK_URL": ("webhook_url", str),
    }

    for env_var, (key, cast) in env_overrides.items():
        val = os.environ.get(env_var)
        if val is not None:
            config[key] = cast(val)

    return config
