#!/usr/bin/env python3
"""σ 后台违规扫描（A 类）— 7 类模式检测

对应 design_proposal_2026.md §三.2.3 A 类。
由 Makefile 的 `make violations-scan` 或 `make weekly-report` 调用。
输出：reviews/violations/YYYY-WW.md（自动 git commit）。

7 类违规：
  1. 未写规则有交易（当日有 trades/ 但没 daily/ 中的盘前文件）
  2. 决策链跳过（trades/ 文件 If 1-5 任一为空但已 commit）
  3. 仓位超阈值（实际仓位 > config.yaml overrides.max_single_position_pct）
  4. 止损穿越未平仓（If 2 设了 P_stop，但平仓价显示穿越后继续持有）
  5. 红区产品出现（trades/ frontmatter product_class: red 已 commit）
  6. 日损超限（当日累计亏损 > config.yaml overrides.max_daily_loss_pct）
  7. 黄色产品周上限（本周 yellow-* 交易笔数 > config.yaml overrides.yellow_weekly_limit）
"""

import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

TRADES_DIR = None
DAILY_DIR = None
VIOLATIONS_DIR = None
TRADER_OVERRIDES = None


def get_current_week():
    now = datetime.now()
    year, week, _ = now.isocalendar()
    return year, week


def get_week_range(year, week):
    """Return (monday, sunday) for the given ISO week."""
    jan4 = datetime(year, 1, 4)
    start = jan4 - timedelta(days=jan4.weekday()) + timedelta(weeks=week - 1)
    end = start + timedelta(days=6)
    return start, end


def find_trade_files(start_date, end_date):
    """Find all trade .md files with dates in the range."""
    trades = []
    for root, _, files in os.walk(TRADES_DIR):
        for f in files:
            if f == "TEMPLATE.md" or f == "README.md" or not f.endswith(".md"):
                continue
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f)
            if match:
                file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if start_date <= file_date <= end_date:
                    trades.append(Path(root) / f)
    return sorted(trades)


def find_daily_files(start_date, end_date):
    """Find all daily pre-market .md files with dates in the range."""
    dailies = {}
    for root, _, files in os.walk(DAILY_DIR):
        for f in files:
            if f == ".gitkeep" or not f.endswith(".md"):
                continue
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f)
            if match:
                file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if start_date <= file_date <= end_date:
                    dailies[match.group(1)] = Path(root) / f
    return dailies


def read_frontmatter(filepath):
    """Extract YAML frontmatter as dict (simple parser)."""
    content = filepath.read_text(encoding="utf-8")
    fm = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    fm[key.strip()] = val.strip()
    return fm, content


def _load_trader_config(trader_id):
    """Load overrides from traders/{id}/config.yaml.

    Falls back to hardcoded defaults if config is missing or unreadable.
    """
    defaults = {
        "max_single_position_pct": 20,
        "max_daily_loss_pct": 3,
        "yellow_weekly_limit": 3,
        "black_swan_window_minutes": 30,
    }
    config_path = WORKSPACE / "traders" / (trader_id or "default") / "config.yaml"
    if not config_path.exists():
        return defaults
    try:
        import yaml
        with open(config_path, encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        overrides = config.get("overrides", {})
        for k, v in defaults.items():
            if k not in overrides:
                overrides[k] = v
        return overrides
    except Exception:
        return defaults


def _check_overposition(trade_path, fm, content, violations):
    """Check #3: position size exceeds config.yaml max_single_position_pct."""
    limit = TRADER_OVERRIDES["max_single_position_pct"]

    pct_match = re.search(r"本笔占比[：:]\s*([\d.]+)\s*%", content)
    if pct_match:
        try:
            pct = float(pct_match.group(1))
            if pct > limit:
                violations.append((
                    "仓位超阈值",
                    f"{trade_path.name}: 本笔占比 {pct}% > 单票上限 {limit}%（config.yaml）"
                ))
                return
        except ValueError:
            pass

    pos = fm.get("position_size", "").strip()
    if not pos:
        return
    acct_match = re.search(r"训练资金账户总额[：:]\s*([\d,.]+)", content)
    if not acct_match:
        return
    try:
        position = float(pos.replace(",", ""))
        account = float(acct_match.group(1).replace(",", ""))
        if account > 0:
            ratio = position / account * 100
            if ratio > limit:
                violations.append((
                    "仓位超阈值",
                    f"{trade_path.name}: position_size/账户 ≈ {ratio:.0f}% > 单票上限 {limit}%（config.yaml）"
                ))
    except ValueError:
        pass


def check_violations(start_date, end_date):
    """Run all 7 violation checks and return list of (type, detail) tuples."""
    violations = []
    trade_files = find_trade_files(start_date, end_date)
    daily_files = find_daily_files(start_date, end_date)

    # Pre-compute per-day aggregates for checks #6 and #7
    daily_pnl = defaultdict(float)       # date_str -> cumulative pnl_net
    daily_acct = {}                       # date_str -> account total (from If 3)
    yellow_count = 0

    for tf in trade_files:
        fm, content = read_frontmatter(tf)
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", tf.name)
        if not date_match:
            continue
        trade_date = date_match.group(1)

        # Accumulate daily PnL
        pnl_str = fm.get("pnl_net", "").strip()
        if pnl_str:
            try:
                daily_pnl[trade_date] += float(pnl_str.replace(",", ""))
            except ValueError:
                pass

        # Grab account total for daily-loss-% calculation
        if trade_date not in daily_acct:
            acct_match = re.search(r"训练资金账户总额[：:]\s*([\d,.]+)", content)
            if acct_match:
                try:
                    daily_acct[trade_date] = float(acct_match.group(1).replace(",", ""))
                except ValueError:
                    pass

        # Count yellow products for check #7
        pc = fm.get("product_class", "").strip()
        if pc.startswith("yellow"):
            yellow_count += 1

        # --- Per-trade checks ---

        # 1. 未写规则有交易
        if trade_date not in daily_files:
            violations.append((
                "未写规则有交易",
                f"{tf.name}: {trade_date} 有交易记录但 daily/ 中没有 {trade_date}-pre.md"
            ))

        # 2. 决策链跳过（检查 If 1-5 是否有内容）
        empty_ifs = []
        for i in range(1, 6):
            section = re.search(rf"### If {i}.*?(?=### If {i+1}|## 三|## 四|$)", content, re.DOTALL)
            if section:
                section_text = section.group()
                filled_lines = [l for l in section_text.split("\n")
                                if l.strip() and not l.startswith("#") and not l.startswith(">")
                                and "___" not in l and "[1-5]" not in l
                                and "S / M / W / U" not in l]
                if len(filled_lines) < 2:
                    empty_ifs.append(f"If {i}")
        if empty_ifs:
            violations.append((
                "决策链跳过",
                f"{tf.name}: {', '.join(empty_ifs)} 未填写或内容不足"
            ))

        # 3. 仓位超阈值（从 If 3 "本笔占比" + frontmatter position_size）
        _check_overposition(tf, fm, content, violations)

        # 4. 止损穿越未平仓
        stop = fm.get("stop_loss_price", "").strip()
        exit_p = fm.get("exit_price", "").strip()
        direction = fm.get("direction", "").strip()
        if stop and exit_p and direction:
            try:
                stop_f = float(stop)
                exit_f = float(exit_p)
                if direction == "long" and exit_f < stop_f * 0.95:
                    violations.append((
                        "止损穿越未平仓（处置效应）",
                        f"{tf.name}: long 止损 {stop}，实际平仓 {exit_p}（穿越 >5%）"
                    ))
                elif direction == "short" and exit_f > stop_f * 1.05:
                    violations.append((
                        "止损穿越未平仓（处置效应）",
                        f"{tf.name}: short 止损 {stop}，实际平仓 {exit_p}（穿越 >5%）"
                    ))
            except ValueError:
                pass

        # 5. 红区产品出现
        if fm.get("product_class", "").strip() == "red":
            violations.append((
                "红区产品违规",
                f"{tf.name}: product_class = red（绕过了 pre-commit hook？）"
            ))

    # --- Aggregate checks (after iterating all trades) ---

    # 6. 日损超限
    max_daily_loss_pct = TRADER_OVERRIDES["max_daily_loss_pct"]
    for date_str, pnl in daily_pnl.items():
        if pnl >= 0:
            continue
        acct = daily_acct.get(date_str)
        if acct and acct > 0:
            loss_pct = abs(pnl) / acct * 100
            if loss_pct > max_daily_loss_pct:
                violations.append((
                    "日损超限",
                    f"{date_str}: 当日净亏损 {pnl:+.1f}（占账户 {loss_pct:.1f}%）> 日损上限 {max_daily_loss_pct}%（config.yaml）"
                ))

    # 7. 黄色产品周上限
    yellow_limit = TRADER_OVERRIDES["yellow_weekly_limit"]
    if yellow_count > yellow_limit:
        violations.append((
            "黄色产品周上限",
            f"本周 yellow-* 交易 {yellow_count} 笔 > 周上限 {yellow_limit} 笔（config.yaml）"
        ))

    return violations


def write_report(year, week, violations):
    """Write violations report to reviews/violations/YYYY-WW.md."""
    VIOLATIONS_DIR.mkdir(parents=True, exist_ok=True)
    filename = VIOLATIONS_DIR / f"{year}-W{week:02d}.md"

    lines = [
        f"# σ 违规扫描报告 — {year} 年第 {week} 周\n",
        f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}（scripts/violations_scan.py）\n",
        f"> 用户必须在 reviews/weekly/{year}-W{week:02d}.md 中逐条 acknowledge 每条违规。\n\n",
    ]

    if not violations:
        lines.append("**本周无违规检测到。**\n")
    else:
        lines.append(f"**本周检测到 {len(violations)} 条违规：**\n\n")
        lines.append("| # | 类型 | 详情 |\n|---|---|---|\n")
        for i, (vtype, detail) in enumerate(violations, 1):
            lines.append(f"| {i} | {vtype} | {detail} |\n")

        lines.append("\n## 待 acknowledge\n\n")
        for i, (vtype, detail) in enumerate(violations, 1):
            lines.append(f"- [ ] #{i} {vtype}：[用户回应：___]\n")

    filename.write_text("".join(lines), encoding="utf-8")
    print(f"Violations report written to {filename}")
    return filename


def _init_paths(trader_id=None):
    global TRADES_DIR, DAILY_DIR, VIOLATIONS_DIR, TRADER_OVERRIDES
    from paths import get_paths
    p = get_paths(trader_id)
    TRADES_DIR = p["trades"]
    DAILY_DIR = p["daily"]
    VIOLATIONS_DIR = p["violations"]
    TRADER_OVERRIDES = _load_trader_config(trader_id)


def main():
    trader_id = None
    args = sys.argv[1:]
    if "--trader" in args:
        idx = args.index("--trader")
        trader_id = args[idx + 1]
        args = args[:idx] + args[idx + 2:]

    _init_paths(trader_id)

    year, week = get_current_week()
    if len(args) >= 2:
        year, week = int(args[0]), int(args[1])

    start, end = get_week_range(year, week)
    print(f"Scanning violations for {year}-W{week:02d} ({start.date()} to {end.date()})...")

    violations = check_violations(start, end)
    report_path = write_report(year, week, violations)

    if violations:
        print(f"Found {len(violations)} violation(s).")
    else:
        print("No violations found.")

    # Auto git add + commit
    subprocess.run(["git", "add", str(report_path)], cwd=WORKSPACE)
    subprocess.run(
        ["git", "commit", "-m", f"auto(violations-scan): {year}-W{week:02d} — {len(violations)} violation(s)"],
        cwd=WORKSPACE,
    )


if __name__ == "__main__":
    main()
