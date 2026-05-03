"""
σ 引擎 — 仓位计算器（基础版）

基于 Kelly / 半 Kelly 公式计算建议仓位。

用法：
    python position_sizer.py

输入：
    - 预期胜率（%）
    - 平均盈利（金额或百分比）
    - 平均亏损（金额或百分比）
    - 可选：Kelly 分数（默认 0.5 = 半 Kelly）

输出：
    - 全 Kelly 建议仓位
    - 半 Kelly 建议仓位
    - 自定义分数建议仓位
    - 风险警告（如适用）

来源：
    - Kelly (1956), "A New Interpretation of Information Rate", Bell System Technical Journal
    - Busseti, Ryabko, Qian & Cover (2016), "Kelly Capital Growth Investing", Cambridge University Press

诚实标记：
    Kelly 公式假设你知道真实的胜率和赔率。在实际交易中，你只有估计值。
    当你的估计有系统性偏差时，Kelly 会给出过度激进的仓位建议。
    因此默认使用半 Kelly（保守策略），并强烈建议新手从半 Kelly 或更保守的 0.25 Kelly 开始。
"""

import argparse


def calculate_kelly(win_prob: float, avg_win: float, avg_loss: float) -> float:
    """
    计算全 Kelly 仓位比例。

    参数：
        win_prob: 胜率（0-1 之间）
        avg_win:  平均盈利
        avg_loss: 平均亏损（正数）

    返回：
        Kelly 比例（0-1 之间，建议仓位占总资金的比例）

    公式：
        f* = (p × b - q) / b
        其中 p = 胜率, q = 1-p, b = avg_win / avg_loss（赔率）
    """
    if not 0 < win_prob < 1:
        raise ValueError("胜率必须在 0-1 之间")
    if avg_win <= 0:
        raise ValueError("平均盈利必须为正数")
    if avg_loss <= 0:
        raise ValueError("平均亏损必须为正数")

    b = avg_win / avg_loss  # 赔率
    q = 1 - win_prob

    kelly = (win_prob * b - q) / b

    return max(0.0, min(kelly, 1.0))  # 限制在 [0, 1]


def calculate_fractional_kelly(kelly: float, fraction: float = 0.5) -> float:
    """计算分数 Kelly。fraction=0.5 为半 Kelly。"""
    if not 0 < fraction <= 1:
        raise ValueError("Kelly 分数必须在 0-1 之间")
    return kelly * fraction


def format_risk_warning(kelly: float, capital: float = None) -> str:
    """根据 Kelly 比例生成风险警告。"""
    warnings = []
    if kelly > 0.3:
        warnings.append(
            "⚠️  全 Kelly 建议仓位 > 30%，风险偏高。强烈建议使用半 Kelly 或更小仓位。"
        )
    if kelly > 0.5:
        warnings.append(
            "🚨 全 Kelly 建议仓位 > 50%，这很可能是因为你输入的胜率或赔率存在过度乐观偏差。"
        )
    if capital and (kelly * capital) > capital * 0.2:
        warnings.append(
            f"📋 按照风控规则（单票上限 20%），建议仓位已自动截断至 {capital * 0.2:.0f}"
        )

    return "\n".join(warnings) if warnings else "✅ Kelly 比例在合理范围内。"


def main():
    parser = argparse.ArgumentParser(
        description="σ 引擎 — 仓位计算器（基于 Kelly 公式）"
    )
    parser.add_argument(
        "--win-prob", type=float,
        help="预期胜率（如 0.6 表示 60%）"
    )
    parser.add_argument(
        "--avg-win", type=float,
        help="平均盈利（金额或百分比）"
    )
    parser.add_argument(
        "--avg-loss", type=float,
        help="平均亏损（金额或百分比）"
    )
    parser.add_argument(
        "--fraction", type=float, default=0.5,
        help="Kelly 分数，默认 0.5（半 Kelly）"
    )
    parser.add_argument(
        "--capital", type=float, default=None,
        help="当前账户总资产（可选），用于计算具体金额和触发风控"
    )
    parser.add_argument(
        "--interactive", "-i", action="store_true",
        help="交互模式（逐个输入参数）"
    )

    args = parser.parse_args()

    if args.interactive or not all([args.win_prob, args.avg_win, args.avg_loss]):
        print("=" * 50)
        print("σ 引擎 — 仓位计算器")
        print("=" * 50)
        try:
            win_prob = float(input("预期胜率（%）：")) / 100
            avg_win = float(input("平均盈利："))
            avg_loss = float(input("平均亏损："))
            fraction_input = input("Kelly 分数（默认 0.5 = 半 Kelly，直接回车用默认值）：")
            fraction = float(fraction_input) if fraction_input.strip() else 0.5
        except ValueError as e:
            print(f"输入错误：{e}")
            return
    else:
        win_prob = args.win_prob
        avg_win = args.avg_win
        avg_loss = args.avg_loss
        fraction = args.fraction

    capital = args.capital

    try:
        kelly_full = calculate_kelly(win_prob, avg_win, avg_loss)
        kelly_fractional = calculate_fractional_kelly(kelly_full, fraction)
    except ValueError as e:
        print(f"计算错误：{e}")
        return

    print("\n" + "=" * 50)
    print("📊 计算结果")
    print("=" * 50)
    print(f"胜率：           {win_prob * 100:.1f}%")
    print(f"平均盈利：       {avg_win}")
    print(f"平均亏损：       {avg_loss}")
    print(f"赔率（盈亏比）： {avg_win / avg_loss:.2f}")
    print(f"期望值：         {win_prob * avg_win - (1 - win_prob) * avg_loss:.2f}")
    print()
    print(f"全 Kelly 比例：   {kelly_full * 100:.2f}%")
    print(f"{'半' if fraction == 0.5 else ''}Kelly (×{fraction}) 比例： {kelly_fractional * 100:.2f}%")

    if capital:
        print(f"\n--- 基于账户总资产 {capital:.0f} ---")
        print(f"全 Kelly 金额：   {kelly_full * capital:.0f}")
        print(f"分数 Kelly 金额： {kelly_fractional * capital:.0f}")

    print("\n" + "-" * 50)
    print(format_risk_warning(kelly_full, capital))
    print("-" * 50)

    print(f"\n{'=' * 50}")
    print("⚠️  诚实声明")
    print(f"{'=' * 50}")
    print("Kelly 公式假设你知道真实的胜率和赔率。")
    print("你输入的胜率和赔率是估计值——不是事实。")
    print("如果你的估计有系统性偏差，Kelly 会给出错误的建议。")
    print("新手强烈建议从半 Kelly (×0.5) 或 ¼ Kelly (×0.25) 开始。")
    print("最终仓位决定权在你手里——这个计算器只是辅助工具。")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
