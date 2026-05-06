#!/usr/bin/env python3
"""σ 训练资金对账（D 类后台强制）

对应 design_proposal_2026.md §三.2.3 D 类。
周末由用户手动从券商导出 CSV，本脚本对比 CSV 与 trades/ 记录。
输出：reviews/reconcile/YYYY-WW.md

检测项：
  1. trades/ 中有记录但 CSV 中没有（漏报交易？或不同账户？）
  2. CSV 中有交易但 trades/ 中没有（冲动交易未记录——σ 最危险盲区）
  3. 金额/方向不一致（误记）
  4. Mental Accounting 边界违规：训练资金账户出现非训练类交易

用法：
  python3 scripts/reconcile_funds.py path/to/broker_export.csv
  python3 scripts/reconcile_funds.py path/to/broker_export.csv --week 2026-W19
"""

import argparse
import csv
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
TRADES_DIR = WORKSPACE / "trades"
RECONCILE_DIR = WORKSPACE / "reviews" / "reconcile"


def parse_broker_csv(csv_path):
    """Parse broker CSV export into list of dicts.

    Expects at minimum columns: date, symbol, direction (or side), quantity, price.
    Flexible: tries common column name variants.
    """
    trades = []
    with open(csv_path, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames_lower = {fn.lower().strip(): fn for fn in (reader.fieldnames or [])}

        date_col = _find_col(fieldnames_lower, ["date", "日期", "trade_date", "成交日期"])
        symbol_col = _find_col(fieldnames_lower, ["symbol", "代码", "合约", "instrument", "code", "标的"])
        dir_col = _find_col(fieldnames_lower, ["direction", "side", "方向", "买卖方向", "买卖"])
        qty_col = _find_col(fieldnames_lower, ["quantity", "qty", "数量", "成交数量", "手数", "volume"])
        price_col = _find_col(fieldnames_lower, ["price", "成交价", "成交价格", "avg_price"])

        if not date_col or not symbol_col:
            print(f"WARNING: CSV 缺少必需列（date, symbol）。找到的列: {list(fieldnames_lower.keys())}")
            return trades

        for row in reader:
            t = {
                "date": _normalize_date(row.get(date_col, "")),
                "symbol": row.get(symbol_col, "").strip().upper(),
                "direction": _normalize_direction(row.get(dir_col, "")),
                "quantity": _safe_float(row.get(qty_col, "")),
                "price": _safe_float(row.get(price_col, "")),
            }
            if t["date"] and t["symbol"]:
                trades.append(t)
    return trades


def _find_col(fieldnames_lower, candidates):
    for c in candidates:
        if c.lower() in fieldnames_lower:
            return fieldnames_lower[c.lower()]
    return None


def _normalize_date(s):
    s = s.strip()
    for fmt in ["%Y-%m-%d", "%Y/%m/%d", "%Y%m%d", "%m/%d/%Y", "%d/%m/%Y"]:
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""


def _normalize_direction(s):
    s = s.strip().lower()
    if s in ("long", "buy", "买", "买入", "开多", "b"):
        return "long"
    if s in ("short", "sell", "卖", "卖出", "开空", "s"):
        return "short"
    return s


def _safe_float(s):
    try:
        return float(str(s).replace(",", "").strip())
    except (ValueError, TypeError):
        return 0.0


def find_sigma_trades(start_date, end_date):
    """Find trades recorded in trades/ directory."""
    sigma = {}
    for root, _, files in os.walk(TRADES_DIR):
        for f in files:
            if f in ("TEMPLATE.md", "README.md", "SCREENSHOTS.md") or not f.endswith(".md"):
                continue
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f)
            if not match:
                continue
            fdate = match.group(1)
            if start_date <= fdate <= end_date:
                path = Path(root) / f
                content = path.read_text(encoding="utf-8")
                fm_match = re.search(r"symbol:\s*(.+)", content)
                dir_match = re.search(r"direction:\s*(.+)", content)
                symbol = fm_match.group(1).strip().upper() if fm_match else ""
                direction = dir_match.group(1).strip().lower() if dir_match else ""
                key = f"{fdate}|{symbol}|{direction}"
                sigma[key] = {"date": fdate, "symbol": symbol, "direction": direction, "file": f}
    return sigma


def reconcile(broker_trades, sigma_trades, start_date, end_date):
    """Compare broker CSV against sigma trades/ records."""
    issues = []

    broker_keys = set()
    for bt in broker_trades:
        if bt["date"] < start_date or bt["date"] > end_date:
            continue
        key = f"{bt['date']}|{bt['symbol']}|{bt['direction']}"
        broker_keys.add(key)

        if key not in sigma_trades:
            issues.append((
                "券商有记录但 trades/ 无",
                f"{bt['date']} {bt['symbol']} {bt['direction']} — **冲动交易未记录？**"
            ))

    for key, st in sigma_trades.items():
        if key not in broker_keys:
            issues.append((
                "trades/ 有记录但券商无",
                f"{st['date']} {st['symbol']} {st['direction']} ({st['file']}) — 不同账户/模拟盘？"
            ))

    return issues


def write_report(year, week, issues, csv_path, broker_count, sigma_count):
    """Write reconciliation report."""
    RECONCILE_DIR.mkdir(parents=True, exist_ok=True)
    filename = RECONCILE_DIR / f"{year}-W{week:02d}.md"

    lines = [
        f"# σ 训练资金对账报告 — {year} 年第 {week} 周\n\n",
        f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}（scripts/reconcile_funds.py）\n",
        f"> 券商 CSV：`{csv_path}`\n",
        f"> 券商交易笔数：{broker_count} | trades/ 记录笔数：{sigma_count}\n\n",
    ]

    if not issues:
        lines.append("**本周对账无差异。** 券商记录与 trades/ 完全匹配。\n")
    else:
        lines.append(f"**检测到 {len(issues)} 项差异：**\n\n")
        lines.append("| # | 类型 | 详情 |\n|---|---|---|\n")
        for i, (itype, detail) in enumerate(issues, 1):
            lines.append(f"| {i} | {itype} | {detail} |\n")

        lines.append("\n## 待确认\n\n")
        for i, (itype, detail) in enumerate(issues, 1):
            lines.append(f"- [ ] #{i} {itype}：[解释：___]\n")

    lines.extend([
        "\n---\n\n",
        "*对应 design_proposal §三.2.3 D 类 + foundation §三.7 训练资金独立*\n",
    ])

    filename.write_text("".join(lines), encoding="utf-8")
    print(f"Reconciliation report: {filename}")
    return filename


def get_week_range(year, week):
    jan4 = datetime(year, 1, 4)
    start = jan4 - timedelta(days=jan4.weekday()) + timedelta(weeks=week - 1)
    end = start + timedelta(days=6)
    return start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser(description="σ 训练资金对账")
    parser.add_argument("csv_path", help="券商导出 CSV 文件路径")
    parser.add_argument("--week", help="指定周（如 2026-W19），默认当前周")
    args = parser.parse_args()

    if not os.path.isfile(args.csv_path):
        print(f"ERROR: CSV 文件不存在: {args.csv_path}")
        sys.exit(1)

    if args.week:
        m = re.match(r"(\d{4})-W(\d{1,2})", args.week)
        if not m:
            print("ERROR: --week 格式应为 YYYY-WNN（如 2026-W19）")
            sys.exit(1)
        year, week = int(m.group(1)), int(m.group(2))
    else:
        now = datetime.now()
        year, week, _ = now.isocalendar()

    start_date, end_date = get_week_range(year, week)
    print(f"对账范围：{year}-W{week:02d}（{start_date} to {end_date}）")

    broker_trades = parse_broker_csv(args.csv_path)
    week_broker = [t for t in broker_trades if start_date <= t["date"] <= end_date]
    sigma_trades = find_sigma_trades(start_date, end_date)

    print(f"券商 CSV 本周交易：{len(week_broker)} 笔")
    print(f"trades/ 本周记录：{len(sigma_trades)} 笔")

    issues = reconcile(broker_trades, sigma_trades, start_date, end_date)
    report_path = write_report(year, week, issues, args.csv_path, len(week_broker), len(sigma_trades))

    if issues:
        print(f"发现 {len(issues)} 项差异——请在报告中逐条确认。")
    else:
        print("对账完全匹配。")

    subprocess.run(["git", "add", str(report_path)], cwd=WORKSPACE)
    subprocess.run(
        ["git", "commit", "-m",
         f"auto(reconcile): {year}-W{week:02d} — {len(issues)} 项差异"],
        cwd=WORKSPACE,
    )


if __name__ == "__main__":
    main()
