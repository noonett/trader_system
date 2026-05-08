"""通知模块 — Windows Toast + 企业微信/个人微信推送。

通道：
1. Windows Toast Notification（系统弹窗，仅 Windows）
2. 企业微信 Webhook（群机器人，最简单）
3. PushPlus / Server酱（个人微信推送备选）
"""

import logging
from typing import Optional

logger = logging.getLogger("sigma-relay.notify")


def send_notification(
    title: str,
    message: str,
    config: dict,
    urgency: str = "normal",
) -> None:
    """Send notification through configured channels.

    Args:
        title: Notification title.
        message: Notification body.
        config: App config with notification settings.
        urgency: "normal" / "high" (high = trade closed with loss).
    """
    channels = config.get("notify_channels", ["toast"])
    if isinstance(channels, str):
        channels = [channels]

    for channel in channels:
        try:
            if channel == "toast":
                _send_toast(title, message)
            elif channel == "wechat_work":
                _send_wechat_work(title, message, config)
            elif channel == "pushplus":
                _send_pushplus(title, message, config)
            elif channel == "serverchan":
                _send_serverchan(title, message, config)
            else:
                logger.warning(f"Unknown notify channel: {channel}")
        except Exception as e:
            logger.error(f"Notification via {channel} failed: {e}")


# ─── Windows Toast ─────────────────────────────────────────────────────────────


def _send_toast(title: str, message: str) -> None:
    """Windows 10/11 Toast Notification."""
    try:
        from win10toast_click import ToastNotifier

        toaster = ToastNotifier()
        toaster.show_toast(
            title=title,
            msg=message,
            duration=10,
            threaded=True,
            icon_path=None,
        )
        logger.info(f"Toast sent: {title}")
    except ImportError:
        try:
            from plyer import notification

            notification.notify(
                title=title,
                message=message,
                timeout=10,
                app_name="σ sigma-relay",
            )
            logger.info(f"Toast (plyer) sent: {title}")
        except ImportError:
            logger.error(
                "Toast notification unavailable. "
                "Install: pip install win10toast-click  OR  pip install plyer"
            )


# ─── 企业微信 Webhook ──────────────────────────────────────────────────────────


def _send_wechat_work(title: str, message: str, config: dict) -> None:
    """企业微信群机器人 Webhook。

    配置方式：
    1. 在企业微信群中添加"群机器人"
    2. 获取 Webhook URL（形如 https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx）
    3. 填入 relay-config.yaml 的 wechat_work_webhook_url
    """
    import httpx

    webhook_url = config.get("wechat_work_webhook_url", "")
    if not webhook_url:
        logger.warning("企业微信 Webhook URL 未配置 (wechat_work_webhook_url)")
        return

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": f"## {title}\n\n{message}",
        },
    }

    resp = httpx.post(webhook_url, json=payload, timeout=5)
    if resp.status_code == 200:
        result = resp.json()
        if result.get("errcode") == 0:
            logger.info("企业微信通知已发送")
        else:
            logger.error(f"企业微信 API 错误: {result}")
    else:
        logger.error(f"企业微信 HTTP {resp.status_code}: {resp.text}")


# ─── PushPlus（个人微信推送） ──────────────────────────────────────────────────


def _send_pushplus(title: str, message: str, config: dict) -> None:
    """PushPlus — 通过公众号推送到个人微信。

    配置方式：
    1. 访问 https://www.pushplus.plus/ 注册并获取 token
    2. 填入 relay-config.yaml 的 pushplus_token
    """
    import httpx

    token = config.get("pushplus_token", "")
    if not token:
        logger.warning("PushPlus token 未配置 (pushplus_token)")
        return

    payload = {
        "token": token,
        "title": title,
        "content": message,
        "template": "markdown",
    }

    resp = httpx.post("http://www.pushplus.plus/send", json=payload, timeout=10)
    if resp.status_code == 200:
        result = resp.json()
        if result.get("code") == 200:
            logger.info("PushPlus 通知已发送")
        else:
            logger.error(f"PushPlus 错误: {result}")
    else:
        logger.error(f"PushPlus HTTP {resp.status_code}")


# ─── Server酱（个人微信推送备选） ─────────────────────────────────────────────


def _send_serverchan(title: str, message: str, config: dict) -> None:
    """Server酱 — 另一种个人微信推送方式。

    配置方式：
    1. 访问 https://sct.ftqq.com/ 注册并获取 SendKey
    2. 填入 relay-config.yaml 的 serverchan_key
    """
    import httpx

    key = config.get("serverchan_key", "")
    if not key:
        logger.warning("Server酱 key 未配置 (serverchan_key)")
        return

    resp = httpx.post(
        f"https://sctapi.ftqq.com/{key}.send",
        data={"title": title, "desp": message},
        timeout=10,
    )
    if resp.status_code == 200:
        logger.info("Server酱通知已发送")
    else:
        logger.error(f"Server酱 HTTP {resp.status_code}")
