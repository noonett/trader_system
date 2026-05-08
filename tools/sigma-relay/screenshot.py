"""Windows 屏幕截图模块 — 成交时自动捕获交易画面。

使用 mss（纯 Python，跨平台，无需外部工具）。
在 Windows 上通过 sigma-relay 调用，ATAS 成交事件触发后立刻截图。
"""

import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

try:
    import mss
    import mss.tools

    MSS_AVAILABLE = True
except ImportError:
    MSS_AVAILABLE = False

logger = logging.getLogger("sigma-relay.screenshot")


def capture_screen(
    symbol: str,
    capture_type: str = "entry",
    output_dir: Optional[Path] = None,
    monitor_index: int = 0,
) -> Optional[Path]:
    """Capture the full screen (or primary monitor) and save as PNG.

    Args:
        symbol: Trading symbol (for filename).
        capture_type: "entry" / "exit" / "context".
        output_dir: Where to save. Defaults to ~/Documents/sigma-screenshots/
        monitor_index: 0 = all monitors combined, 1 = primary, 2 = secondary...

    Returns:
        Path to saved screenshot, or None if capture failed.
    """
    if not MSS_AVAILABLE:
        logger.error(
            "mss not installed. Run: pip install mss"
        )
        return None

    if output_dir is None:
        output_dir = Path.home() / "Documents" / "sigma-screenshots"
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    symbol_clean = symbol.lower().replace("/", "").replace(" ", "")
    filename = f"{timestamp}_{symbol_clean}_{capture_type}.png"
    filepath = output_dir / filename

    try:
        with mss.mss() as sct:
            monitor = sct.monitors[monitor_index]
            img = sct.grab(monitor)
            mss.tools.to_png(img.rgb, img.size, output=str(filepath))

        logger.info(f"Screenshot saved: {filepath} ({filepath.stat().st_size // 1024}KB)")
        return filepath

    except Exception as e:
        logger.error(f"Screenshot capture failed: {e}")
        return None


def move_to_trade_screenshots(
    screenshot_path: Path,
    trades_dir: Path,
    trade_date: str,
    symbol: str,
    direction: str,
    capture_type: str = "entry",
) -> Optional[Path]:
    """Move screenshot to the trade's screenshots/ directory with proper naming.

    Follows SCREENSHOTS.md convention:
        trades/YYYY/MM/screenshots/YYYY-MM-DD-<symbol>-<dir>-<type>-<seq>.png

    Returns:
        New path after move, or None if failed.
    """
    screenshots_dir = trades_dir / "screenshots"
    screenshots_dir.mkdir(parents=True, exist_ok=True)

    symbol_clean = symbol.lower().replace("/", "").replace(" ", "")
    base_name = f"{trade_date}-{symbol_clean}-{direction}-{capture_type}"

    seq = 1
    while True:
        target = screenshots_dir / f"{base_name}-{seq}.png"
        if not target.exists():
            break
        seq += 1

    try:
        import shutil

        shutil.move(str(screenshot_path), str(target))
        logger.info(f"Screenshot moved: {target.name}")
        return target
    except Exception as e:
        logger.error(f"Failed to move screenshot: {e}")
        return None
