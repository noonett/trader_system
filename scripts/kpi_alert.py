#!/usr/bin/env python3
"""σ KPI 退化检测 + alert 生成（B 类后台强制）

对应 design_proposal_2026.md §三.2.3 B 类 + §四.4。
由 Makefile 的 `make monthly-calibration` 调用。
输出：reviews/alerts/YYYY-MM-DD-alert.md（含 acknowledge 字段）。

退化触发条件（design_proposal §四.4）：
  - 4 周 P0 < 50% → 4→2 退化建议
  - 8 周 P0 < 50% → 4→1 退化建议
  - 12 周 P0 < 50% → 触发退出协议
"""

import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

# Resolved per-trader at runtime (see main())
TRADES_DIR = None
DAILY_DIR = None
ALERTS_DIR = None


def count_trading_days(start_date, end_date):
    """Count weekdays (Mon-Fri) in range as proxy for trading days."""
    count = 0
    d = start_date
    while d <= end_date:
        if d.weekday() < 5:
            count += 1
        d += timedelta(days=1)
    return count


def count_daily_pre_files(start_date, end_date):
    """Count sigma/daily/ pre-market files in the date range."""
    count = 0
    for root, _, files in os.walk(DAILY_DIR):
        for f in files:
            if f == ".gitkeep" or not f.endswith(".md"):
                continue
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f)
            if match:
                file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if start_date <= file_date <= end_date:
                    count += 1
    return count


def count_trade_files(start_date, end_date):
    """Count trades/ files + those with complete decision chain."""
    total = 0
    complete_chain = 0
    with_ema = 0

    for root, _, files in os.walk(TRADES_DIR):
        for f in files:
            if f in ("TEMPLATE.md", "README.md") or not f.endswith(".md"):
                continue
            match = re.match(r"(\d{4}-\d{2}-\d{2})", f)
            if match:
                file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
                if start_date <= file_date <= end_date:
                    total += 1
                    content = (Path(root) / f).read_text(encoding="utf-8")
                    if "If 5" in content and "EV =" in content:
                        complete_chain += 1
                    if "结果：" in content and "是否按计划执行" in content:
                        with_ema += 1

    return total, complete_chain, with_ema


def compute_kpis(weeks_back=4):
    """Compute P0 KPIs for the last N weeks."""
    end_date = datetime.now()
    start_date = end_date - timedelta(weeks=weeks_back)

    trading_days = count_trading_days(start_date, end_date)
    pre_files = count_daily_pre_files(start_date, end_date)
    total_trades, complete_chains, with_ema = count_trade_files(start_date, end_date)

    pre_rate = (pre_files / trading_days * 100) if trading_days > 0 else 0
    chain_rate = (complete_chains / total_trades * 100) if total_trades > 0 else 100
    ema_rate = (with_ema / total_trades * 100) if total_trades > 0 else 100

    return {
        "weeks": weeks_back,
        "trading_days": trading_days,
        "pre_files": pre_files,
        "pre_rate": pre_rate,
        "total_trades": total_trades,
        "complete_chains": complete_chains,
        "chain_rate": chain_rate,
        "with_ema": with_ema,
        "ema_rate": ema_rate,
    }


def _any_p0_below(kpis, threshold):
    """Check if any P0 KPI (pre_rate, chain_rate, ema_rate) < threshold.

    Design §4.4: "P0 任一 < 50% → 退化"
    Only triggers when there is actual activity (trading_days > 0) and at
    least one trade exists (so chain_rate/ema_rate are meaningful).
    """
    if kpis["trading_days"] <= 0:
        return False
    below = kpis["pre_rate"] < threshold
    if kpis["total_trades"] > 0:
        below = below or kpis["chain_rate"] < threshold or kpis["ema_rate"] < threshold
    return below


def determine_level(kpis_4w, kpis_8w, kpis_12w):
    """Determine current degradation level based on KPI data.

    Design §4.4 triggers:
      12w any P0 < 50% → L0 (exit protocol)
       8w any P0 < 50% → L1 (pre-market only)
       4w any P0 < 50% → L2 (pre-market + monthly calibration)
    """
    if _any_p0_below(kpis_12w, 50):
        dims = _format_dims(kpis_12w)
        return "L0", f"触发退出协议（v5 §三.6）——12 周 P0 任一 < 50%（{dims}）"
    if _any_p0_below(kpis_8w, 50):
        dims = _format_dims(kpis_8w)
        return "L1", f"4→1 退化——仅保留盘前规则书写（8 周 P0 任一 < 50%: {dims}）"
    if _any_p0_below(kpis_4w, 50):
        dims = _format_dims(kpis_4w)
        return "L2", f"4→2 退化——盘前 + 月校准（4 周 P0 任一 < 50%: {dims}）"

    any_below_threshold = (
        kpis_4w["pre_rate"] < 80 or
        kpis_4w["chain_rate"] < 90 or
        kpis_4w["ema_rate"] < 70
    )
    if any_below_threshold and kpis_4w["trading_days"] > 0:
        return "L4-warning", f"L4 维持但有 KPI 低于阈值——盘前 {kpis_4w['pre_rate']:.0f}% / 决策链 {kpis_4w['chain_rate']:.0f}% / EMA {kpis_4w['ema_rate']:.0f}%"

    return "L4", "L4 完整版维持——所有 P0 KPI 达标"


def _format_dims(kpis):
    return f"盘前 {kpis['pre_rate']:.0f}% / 决策链 {kpis['chain_rate']:.0f}% / EMA {kpis['ema_rate']:.0f}%"


def generate_alert(level, reason, kpis_4w):
    """Generate alert file if level is not L4."""
    if level == "L4":
        print(f"KPI status: {level} — {reason}. No alert needed.")
        return None

    ALERTS_DIR.mkdir(parents=True, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = ALERTS_DIR / f"{today}-alert.md"

    lines = [
        f"# σ KPI Alert — {today}\n\n",
        f"> 自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}（scripts/kpi_alert.py）\n\n",
        f"## 当前级别：{level}\n\n",
        f"**判定**：{reason}\n\n",
        "## KPI 数据（最近 4 周）\n\n",
        "| KPI | 值 | 阈值 |\n|---|---|---|\n",
        f"| 盘前规则书写完成率 | {kpis_4w['pre_rate']:.0f}% ({kpis_4w['pre_files']}/{kpis_4w['trading_days']}) | ≥ 80% |\n",
        f"| 决策链 5 问完整率 | {kpis_4w['chain_rate']:.0f}% ({kpis_4w['complete_chains']}/{kpis_4w['total_trades']}) | ≥ 90% |\n",
        f"| 盘后 EMA 完成率 | {kpis_4w['ema_rate']:.0f}% ({kpis_4w['with_ema']}/{kpis_4w['total_trades']}) | ≥ 70% |\n",
        "\n## 建议行动\n\n",
    ]

    if level == "L0":
        lines.append("**触发退出协议**（design_proposal §五）——请认真评估是否继续 σ 训练。\n")
    elif level == "L1":
        lines.append("**退化到 L1**——仅保留盘前规则书写，砍掉其他层。\n")
    elif level == "L2":
        lines.append("**退化到 L2**——保留盘前 + 月校准，砍掉盘后 EMA + 周复盘。\n")
    else:
        lines.append("**维持 L4 但关注低 KPI**——下周集中改善上表中低于阈值的项。\n")

    lines.extend([
        "\n## Acknowledge（必填——未填前 sigma/daily/ 顶部会有 banner 提醒）\n\n",
        f"- [ ] 我已于 [日期] 阅读本 alert\n",
        f"- [ ] 我的决定是：[维持 / 退化到 L___ / 触发退出协议 / 其他：___]\n",
        f"- [ ] 理由：[___]\n",
    ])

    filename.write_text("".join(lines), encoding="utf-8")
    print(f"Alert written to {filename}")
    return filename


def _init_paths(trader_id=None):
    global TRADES_DIR, DAILY_DIR, ALERTS_DIR
    from paths import get_paths
    p = get_paths(trader_id)
    TRADES_DIR = p["trades"]
    DAILY_DIR = p["daily"]
    ALERTS_DIR = p["alerts"]


def main():
    import sys
    trader_id = None
    if "--trader" in sys.argv:
        idx = sys.argv.index("--trader")
        trader_id = sys.argv[idx + 1]

    _init_paths(trader_id)
    print(f"=== σ KPI 退化检测 (trader: {trader_id or 'default'}) ===")

    kpis_4w = compute_kpis(4)
    kpis_8w = compute_kpis(8)
    kpis_12w = compute_kpis(12)

    for label, k in [("4w", kpis_4w), ("8w", kpis_8w), ("12w", kpis_12w)]:
        print(f"{label}: pre={k['pre_rate']:.0f}% chain={k['chain_rate']:.0f}% ema={k['ema_rate']:.0f}%")

    level, reason = determine_level(kpis_4w, kpis_8w, kpis_12w)
    alert_path = generate_alert(level, reason, kpis_4w)

    if alert_path:
        subprocess.run(["git", "add", str(alert_path)], cwd=WORKSPACE)
        subprocess.run(
            ["git", "commit", "-m", f"auto(kpi-alert): {level} — {datetime.now().strftime('%Y-%m-%d')}"],
            cwd=WORKSPACE,
        )


if __name__ == "__main__":
    main()
