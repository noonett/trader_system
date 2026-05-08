"""Draft markdown generator — 从交易事件数据生成 σ 交易记录草稿。

遵循 traders/default/trades/TEMPLATE.md 格式。
"""

from datetime import datetime
from pathlib import Path
from typing import Optional


def generate_draft_markdown(
    position: dict, close_event, config: dict
) -> Path:
    """Generate a draft trade record markdown file.

    Args:
        position: Aggregated position data with fills list
        close_event: PositionClosed event with final PnL
        config: Application config (workspace root, trader id, etc.)

    Returns:
        Path to the created draft file.
    """
    fills = position.get("fills", [])
    direction = position.get("direction", "unknown")
    symbol = position["symbol"]

    total_qty = sum(f["qty"] for f in fills) if fills else 0
    avg_entry = (
        sum(f["price"] * f["qty"] for f in fills) / total_qty
        if total_qty > 0
        else close_event.avg_entry_price
    )

    first_time = position.get("first_fill_time", close_event.timestamp)
    try:
        trade_date = datetime.fromisoformat(first_time.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        trade_date = datetime.now()

    date_str = trade_date.strftime("%Y-%m-%d")
    symbol_clean = symbol.lower().replace("/", "").replace(" ", "")

    stop_prices = position.get("stop_prices", [])
    last_stop = stop_prices[-1]["price"] if stop_prices else None

    frontmatter = _build_frontmatter(
        date_str=date_str,
        symbol=symbol,
        direction=direction,
        avg_entry=avg_entry,
        position_size=int(total_qty) if total_qty else None,
        stop_loss=last_stop,
        pnl_gross=close_event.realized_pnl,
        account=close_event.account or position.get("account", ""),
    )

    body = _build_body(
        date_str=date_str,
        direction=direction,
        fills=fills,
        total_qty=total_qty,
        avg_entry=avg_entry,
    )

    content = f"<!-- DRAFT: auto-captured by sigma-relay, pending user confirmation -->\n{frontmatter}\n{body}"

    trades_dir = _get_trades_dir(config, date_str)
    trades_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{date_str}-{symbol_clean}-{direction}.md"
    filepath = trades_dir / filename

    counter = 1
    while filepath.exists():
        counter += 1
        filename = f"{date_str}-{symbol_clean}-{direction}-{counter}.md"
        filepath = trades_dir / filename

    filepath.write_text(content, encoding="utf-8")
    return filepath


def _build_frontmatter(
    date_str: str,
    symbol: str,
    direction: str,
    avg_entry: float,
    position_size: Optional[int],
    stop_loss: Optional[float],
    pnl_gross: float,
    account: str,
) -> str:
    product_class = _infer_product_class(symbol)
    market = _infer_market(symbol)

    lines = [
        "---",
        "",
        f"## date: {date_str}",
        "",
        f"symbol: {symbol}",
        f"direction: {direction}",
        f"product_class: {product_class}",
        f"market: {market}",
        f"account: {account}",
        "fund_type: training",
        "setup_tag: # [待填写]",
        "stop_type: # [待填写]",
        "target_type: # [待填写]",
        "target_rr: # [待填写]",
        "market_condition: # [待填写]",
        f"entry_price: {round(avg_entry, 2)}",
        "exit_price: # [待确认 — relay 未直接获取平仓价]",
        f"position_size: {position_size or '# [待确认]'}",
        f"stop_loss_price: {round(stop_loss, 2) if stop_loss else '# [待填写]'}",
        f"pnl_gross: {pnl_gross}",
        "pnl_net: # [待扣费计算]",
        "fees: # [待确认]",
        "",
    ]
    return "\n".join(lines)


def _build_body(
    date_str: str,
    direction: str,
    fills: list,
    total_qty: float,
    avg_entry: float,
) -> str:
    fills_table = ""
    if fills:
        fills_table = "\n| # | 时间 | 价格 | 数量 |\n|---|------|------|------|\n"
        for i, f in enumerate(fills, 1):
            fills_table += f"| {i} | {f.get('time', 'N/A')} | {f['price']} | {f['qty']} |\n"
        fills_table += f"\n**加权均价**: {round(avg_entry, 2)} | **总量**: {int(total_qty)}\n"

    return f"""# {date_str}  {direction}

> ⚠️ **这是自动生成的草稿** — 由 sigma-relay 捕获 ATAS 成交事件后创建。
> 请补填以下必需信息后移除本 banner。

## 成交明细（自动捕获）
{fills_table}
---

## 一、盘前 if-then 参考

> [待填写 — 参考当日 sigma/daily/ 盘前文件]

---

## 二、决策链 5 项 if-then（开仓前填写）

### If 1（论据）

我做这笔交易的论据是：**[待填写]**

证据等级：**[S/M/W/U]**

置信度：**[ ] / 5**

### If 2（止损）

入场理由被推翻的条件是：**[待填写]**

对应价格 P_stop = **[待确认]**

### If 3（仓位）

全亏对我的影响：**[待计算]**

本笔最大损失金额：**[待计算]**

训练资金账户总额：**[待填写]**

本笔占比：**[待计算]**

### If 4（情绪）

当前情绪状态：**[待填写]**

强度：**[ ] / 5**

### If 5（期望值）

10 笔同类预期 **[ ]** 笔赚钱

平均每笔赚 G = **[待估]**

平均每笔亏 L = **[待估]**

EV = **[待算]**

---

## 三、决策前检查清单

- [ ] 是否在盘前 if-then 预设范围内？
- [ ] 仓位是否符合风险预算？
- [ ] 是否有明确的止损？
- [ ] 是否在情绪平稳时入场？

---

## 四、盘后 EMA（平仓后 30 分钟内填写，≤4 字段）

| 字段 | 内容 |
|------|------|
| 做对了什么 | [待填写] |
| 做错了什么 | [待填写] |
| 学到了什么 | [待填写] |
| 下次改进 | [待填写] |

---

## 五、截图证据

> [待补充 — 入场截图 + 出场截图]

---

## 六、事后复盘（可选）

[如需深入复盘可在此展开]

---
*草稿由 sigma-relay v0.1 自动生成 | 模板基于 TEMPLATE.md v0.1*
"""


def _infer_product_class(symbol: str) -> str:
    """Infer product_class from symbol naming convention."""
    sym = symbol.upper()
    if any(sym.startswith(prefix) for prefix in ("MGC", "MES", "MNQ", "M2K", "MYM")):
        return "yellow-small-future"
    if any(sym.startswith(prefix) for prefix in ("ES", "NQ", "YM", "GC", "CL", "SI")):
        return "yellow-small-future"  # 根据实际账户可调整
    return "# [待确认]"


def _infer_market(symbol: str) -> str:
    """Infer market from symbol."""
    sym = symbol.upper()
    if any(
        sym.startswith(p)
        for p in ("MGC", "MES", "MNQ", "ES", "NQ", "GC", "CL", "SI", "M2K", "MYM")
    ):
        return "futures-cme"
    return "# [待确认]"


def _get_trades_dir(config: dict, date_str: str) -> Path:
    """Determine the trades directory path for a given date."""
    workspace = Path(config["workspace_root"])
    trader_id = config.get("trader_id", "default")
    year_month = date_str[:7].replace("-", "/")  # "2026-05" -> "2026/05"

    return workspace / "traders" / trader_id / "trades" / year_month
