"""文件监控退化方案 — 当 ATAS 沙箱阻止 HTTP 时使用。

SigmaBridge 改为写本地 JSONL 文件，本模块监控该文件的变化并注入到主事件流。

启动方式：
    python file_watcher.py --watch-dir "C:\\sigma-events"
    
或在 server.py 中作为后台线程启动。
"""

import json
import logging
import time
from pathlib import Path
from threading import Thread
from typing import Callable, Optional

logger = logging.getLogger("sigma-relay.file_watcher")

try:
    from watchdog.events import FileSystemEventHandler, FileModifiedEvent
    from watchdog.observers import Observer

    WATCHDOG_AVAILABLE = True
except ImportError:
    WATCHDOG_AVAILABLE = False


class EventFileHandler(FileSystemEventHandler):
    """Watch a JSONL file for new trade events."""

    def __init__(self, filepath: Path, callback: Callable[[dict], None]):
        self.filepath = filepath
        self.callback = callback
        self._last_position = 0
        self._init_position()

    def _init_position(self):
        if self.filepath.exists():
            self._last_position = self.filepath.stat().st_size

    def on_modified(self, event):
        if not isinstance(event, FileModifiedEvent):
            return
        if Path(event.src_path).resolve() != self.filepath.resolve():
            return
        self._read_new_lines()

    def _read_new_lines(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                f.seek(self._last_position)
                new_content = f.read()
                self._last_position = f.tell()

            for line in new_content.strip().splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    event_data = json.loads(line)
                    self.callback(event_data)
                except json.JSONDecodeError as e:
                    logger.warning(f"Invalid JSON line: {e}")
        except Exception as e:
            logger.error(f"Error reading event file: {e}")


def start_file_watcher(
    watch_dir: str,
    callback: Callable[[dict], None],
    filename: str = "events.jsonl",
) -> Optional[Thread]:
    """Start watching a JSONL file for new trade events.

    Args:
        watch_dir: Directory containing the events file.
        callback: Function to call with each parsed event dict.
        filename: Name of the JSONL file to watch.

    Returns:
        The watcher thread, or None if watchdog is unavailable.
    """
    if not WATCHDOG_AVAILABLE:
        logger.error(
            "watchdog not installed. Run: pip install watchdog\n"
            "File watcher mode unavailable."
        )
        return None

    watch_path = Path(watch_dir)
    watch_path.mkdir(parents=True, exist_ok=True)
    event_file = watch_path / filename

    if not event_file.exists():
        event_file.touch()

    handler = EventFileHandler(event_file, callback)
    observer = Observer()
    observer.schedule(handler, str(watch_path), recursive=False)

    def run():
        observer.start()
        logger.info(f"File watcher started: {event_file}")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    thread = Thread(target=run, daemon=True, name="sigma-file-watcher")
    thread.start()
    return thread


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="σ file watcher (standalone)")
    parser.add_argument(
        "--watch-dir",
        default=r"C:\sigma-events",
        help="Directory to watch for events.jsonl",
    )
    args = parser.parse_args()

    def print_event(event: dict):
        print(f"[EVENT] {json.dumps(event, ensure_ascii=False)}")

    logging.basicConfig(level=logging.INFO)
    logger.info(f"Watching: {args.watch_dir}")

    start_file_watcher(args.watch_dir, print_event)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")
