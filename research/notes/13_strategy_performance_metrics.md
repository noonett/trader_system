# 策略表现指标：哪些值得追踪、何时可信、如何避免自欺

> ⚠️ **状态标注**：本笔记为 Phase 3b/3c 策略指标设计的调研基础。最终系统约束以 `design_phase3bc_notifications_webui.md` §七 为准。
>
> 调研日期：2026-05-06
> 调研方法：Web 检索（SSRN / Cambridge / arXiv / 行业专业站点）+ 已有 foundation_2026.md 样本量约束复用
> 上下文：本笔记是第 13 份调研。前 12 份覆盖行为/系统设计维度；本份回答的是用户提出的"策略指标是否应该追踪"。
> 证据等级：S（同行评审）/ M（监管 / 大型行业数据 / 工作论文）/ W（行业博客 / 营销）/ U（基于已知文献的逻辑推演）

---

## 摘要

**1. 应该追踪策略表现指标——但与行为合规指标的逻辑完全不同。** 行为指标（决策链完成率、EMA 填写率）在 n=1 就有意义（"我今天做了吗"）；策略指标（胜率、期望值、Sharpe）在 n<30 时**几乎没有统计学意义**。这不是"不追踪"的理由——而是"追踪但诚实标注置信度"的理由。

**2. 最有价值的指标不是 Sharpe Ratio，而是 Expectancy（以 R 倍数计）。** Sharpe 需要大量数据且对自相关敏感（Ledoit & Wolf 2008）。Expectancy 直觉清晰（"每笔平均赚/亏多少 R"），且能按 setup 分组——这才是"我的哪个策略有 edge"的直接答案。

**3. 散户系统性误评自身表现。** Linnainmaa et al. (2024, SSRN 4636623) 发现处置效应人为膨胀胜率：真实盈利日 47% 被膨胀为 52%——如果你用胜率作为唯一指标，会系统性高估自己。这是追踪 R 倍数（不可被处置效应扭曲）的强理由。

**4. 按 Setup 分组是核心价值。** 行业实践（ACY 2025 综合）一致表明：账户级 profit factor 无法诊断问题；按 setup_tag 拆分后才能发现"主策略 PF=2.2 而副策略 PF=0.7 在拖后腿"。

**5. 样本量是不可回避的硬约束。** foundation_2026.md §三.5 已要求"样本量 < 50 时拒绝下统计结论"。本调研进一步量化：55% 真实胜率在 30 笔交易中有 40% 的概率看起来不赚钱（M1NDTR8DE 统计模拟）。

---

## Q1：哪些策略指标有学术/行业证据支持？

### 1.1 R 倍数（R-Multiple）

**定义**：(平仓价 - 入场价) / (入场价 - 止损价)。以初始风险为单位衡量收益。

**来源**：Van Tharp (1998), *Trade Your Way to Financial Freedom*, McGraw-Hill。【M 级——行业经典，非同行评审但被专业交易教育广泛采用】

**为什么比绝对金额更好**：
- 标准化了不同仓位大小的交易（一笔 10 手和一笔 1 手可以直接比较）
- 直接与止损挂钩——强化"先定义风险再计算收益"的纪律
- 不受处置效应扭曲（处置效应扭曲的是"何时卖出"决策，不是 R 计算本身）

**σ 系统适用性**：trades/TEMPLATE.md 已有 entry_price / exit_price / stop_loss_price 三个字段 → R 倍数可自动计算，无需用户额外填写。

### 1.2 期望值 / Expectancy

**定义**：(win_rate × avg_win_R) - (loss_rate × avg_loss_R)。以 R 为单位的每笔平均期望收益。

**学术基础**：这是概率论的基本应用（非特定论文）。在交易领域，Tharp (1998) 和 Larry Williams (1979) 是最早系统化使用者。

**关键洞察**（trading-journals.com 综合，M/W 级）：
- 一个 45% 胜率 + 2.5R 平均赢 + 1R 平均亏的交易者：Expectancy = 0.45×2.5 - 0.55×1 = 0.58R/笔
- **Expectancy > 0 是"你有 edge"的唯一直接证据**
- 没有 initial risk（止损位）就无法计算 R → 无法计算 Expectancy → 无法验证 edge

### 1.3 Profit Factor

**定义**：gross_profit / |gross_loss|。大于 1 = 总体赚钱。

**行业基准**（CrossTrade 综合，W 级但与 S 级回测文献一致）：
- PF < 1.0 = 无 edge
- PF 1.2-2.0 = 现实区间（多数可行策略在此）
- PF > 3.0 = 很可能过拟合 / 极小样本
- PF 在 20 笔交易时提供的信息极少，需要 100+ 笔才稳定

**为什么优于单看胜率或单看盈亏比**：PF 同时编码了频率和幅度——60% 胜率但每次只赚 0.5R 亏 1R 的策略 PF = (0.6×0.5)/(0.4×1) = 0.75 < 1，实际在亏。

### 1.4 Sharpe Ratio

**定义**：(mean_return - risk_free_rate) / std_return × sqrt(annualization_factor)

**学术证据**：

**Ledoit, O. & Wolf, M. (2008). "Robust Performance Hypothesis Testing with the Sharpe Ratio." *Journal of Empirical Finance*.**【S 级】
- Sharpe Ratio 的标准误差在小样本下极大
- 自相关结构（交易序列天然有自相关）进一步恶化估计
- 需要参考表来判断是否显著

**Bailey & López de Prado (2014). "The Deflated Sharpe Ratio." *Journal of Portfolio Management*.**【S 级】
- 多次回测后的 Sharpe 必须做 multiple testing 校正
- 未校正的 Sharpe > 2 可能实际 ≈ 0（经 deflation 后）

**Lo, A. (2002). "The Statistics of Sharpe Ratios." *Financial Analysts Journal*.**【S 级】
- 给出了 Sharpe Ratio 置信区间的解析公式
- 月度 Sharpe 2.0 的 95% CI 在 1 年数据下约为 [0.4, 3.6]——极宽

**对 σ 系统的含义**：Sharpe 在 n < 50 笔交易时**几乎没有判断力**。但作为长期趋势观察（n > 100 笔、跨 regime）仍有参考价值。

### 1.5 最大回撤（Maximum Drawdown）

**定义**：从权益曲线峰值到后续谷值的最大跌幅。

**学术基础**：回撤分析在资产管理文献中是标准做法。Magdon-Ismail & Atiya (2004, *J. Applied Prob.*) 给出了最大回撤的分布理论。

**实践价值**：
- 直觉清晰："我最多会亏到什么程度"
- 不需要大样本——即使 20 笔也能计算历史 max drawdown
- **但不能外推**——过去的 max drawdown ≠ 未来的上限

### 1.6 最大连续亏损

**定义**：最长的连续亏损笔数。

**心理价值**（U 级推演）：提前知道"我的策略正常运行时可能连亏 N 笔"能防止连续亏损时误判"策略失效了"。

**统计参考**：胜率 55% 的策略连续亏损 7 笔的概率 ≈ 0.55^7 ≈ 0.015 ≈ 1.5%——每 67 组 7 笔中会出现 1 次。

---

## Q2：样本量需要多少才可信？

### 2.1 统计框架

**核心公式**（BacktestBase 综合 + 标准统计学）：

n = (Z² × p × (1-p)) / E²

| 置信度 | Z 值 |
|--------|------|
| 90% | 1.645 |
| 95% | 1.96 |
| 99% | 2.576 |

### 2.2 具体数字

| 真实胜率 | 95% 置信 / 5% 误差需要的 n | 含义 |
|---------|---------------------------|------|
| 50% | ~385 笔 | 接近随机，几乎不可能在小样本中判断 |
| 52% | ~2,400 笔 | 微弱 edge 需要极大样本 |
| 55% | ~380 笔 | 中等 edge 约大半年到一年 |
| 60% | ~95 笔 | 较强 edge 约 3-6 个月 |
| 70% | ~33 笔 | 很强 edge 可较快判断 |

**来源**：BacktestBase (2025) 综合 + Central Limit Theorem 标准应用。【M 级——统计学教科书级计算，专业站点应用】

### 2.3 关键发现：小样本的欺骗性

**M1NDTR8DE 统计模拟（W/M 级）**：
- 55% 真实胜率在 30 笔中有 **40% 概率表现为 ≤50%**（看起来不赚钱）
- 同一策略在不同 30 笔窗口中，胜率可在 35%-75% 之间波动

**CrossTrade 分析（W 级）**：
- Profit Factor 在 20 笔时"几乎没有信息量"
- 100 笔开始稳定
- 500+ 笔才接近"真实"值

### 2.4 超越笔数：Regime 多样性

**López de Prado (2018). *Advances in Financial Machine Learning*. Wiley.**【S 级】
- 500 笔交易在 6 个月内（单一市场环境）的可靠性 < 100 笔跨 5 年（多 regime）
- 必须覆盖牛市、熊市、震荡市
- 样本必须跨至少 3-5 个 regime 才有"策略有效"的基本判断力

**对 σ 系统的含义**：即使积累了 100 笔交易，如果全部来自同一个市场环境（如 2026 年上半年的 A 股震荡市），也不能结论"策略有效"——只能说"在这个 regime 下表现为正"。

---

## Q3：散户评估自身表现的系统性偏误

### 3.1 处置效应膨胀胜率

**Linnainmaa, J., Kalda, A., Egan, M. (2024). "Counting pennies, losing pounds: Biased learning about own trading ability." SSRN 4636623.**【S 级 working paper】

- 散户用"今天赚了吗"作为自评指标
- 处置效应（过早卖盈、过晚卖亏）人为提高了"盈利天数比例"
- 真实盈利日 47% 被膨胀到 52%
- 这产生系统性过度自信——交易者认为自己在进步但实际在亏

**对 σ 系统的含义**：
- 单看胜率 **不够**——必须看 R 倍数分布
- R 倍数不受处置效应扭曲（因为它是基于止损位计算的，不是基于"今天赚了吗"）
- 这是 σ 系统追踪 R 倍数而非只追踪胜率的核心理由

### 3.2 Profit Factor 的过拟合风险

**Harvey, C., Liu, Y., Zhu, H. (2016). "...and the Cross-Section of Expected Returns." *Review of Financial Studies*.**【S 级】

- 多次回测后选出的最优策略 Profit Factor 会被系统性高估
- 如果你测试了 10 个 setup 然后选了最好的一个——那个"最好的"很可能是噪音

**对 σ 系统的含义**：如果用户有多个 setup，不要只看"哪个 PF 最高"——要看哪个 PF 在 multiple testing 校正后仍然 > 1。在小样本下这几乎不可能做到——所以**不要过早淘汰 setup**。

### 3.3 Backtested vs Live 的差距

**Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." *Journal of Portfolio Management*.**【S 级】

- 回测 Sharpe 2.0 经 deflation 后可能 ≈ 0
- 真实交易面对：滑点 + 市场冲击 + 情绪偏差 + 参数衰减

**对 σ 系统的含义**：trades/ 里记录的是**真实交易数据**——这比回测更可信，但样本量更小。两个约束方向相反，需要诚实标注。

---

## Q4：按 Setup 分组追踪 — 行业实践与学术基础

### 4.1 行业实践

**ACY (2025). "Trading Journal System Metrics: How to Measure Setup Quality & System Edge."**【W 级但行业共识】

- 专业交易台普遍使用 **Setup Quality Scoring**（A+ / B / C 分级）
- 发现模式：A+ 级交易贡献大部分利润，C 级交易贡献大部分回撤
- **入场时标注 setup 质量**（不是事后）是关键——事后标注有后见之明偏差

**trading-journals.com 综合（W/M 级）**：
- "账户级 profit factor 无法诊断问题"
- 按 setup 拆分后发现："主策略 PF=2.2，副策略 PF=0.7，副策略在拖后腿"
- **这是 setup-specific 追踪的核心价值：不是为了"证明策略有效"，是为了"发现谁在拖后腿"**

### 4.2 市场环境条件化

**ACY (2025) + 行业共识**：
- Setup 往往只在特定 regime 下有效
- "breakout-retest 在趋势市有效但在震荡市亏钱"是常见模式
- 需要按 market_condition 维度追踪

**对 σ 系统的含义**：trades/ frontmatter 需要 `market_condition` 字段（trending / ranging / volatile / low-vol），在入场时标注——这样后续可以分析"我的策略在哪种环境下有 edge"。

### 4.3 止损/止盈方式对比

**行业实践（W 级）**：
- 不同止损方式（structure / ATR / percent / time）对同一 setup 的 R 分布有显著影响
- 追踪 `stop_type` 和 `target_type` 可以回答"我应该用什么方式止损最优"
- 但注意：小样本下这个对比几乎没有统计力——需要同一 setup × 同一市场环境下 30+ 笔才有初步参考

---

## Q5：行为合规 × 策略表现 — 最有价值的交叉分析

### 5.1 为什么交叉分析比单独看任一维度更有价值

**U 级推演**（基于 σ 系统已有架构 + 行为金融基本原理）：

| 问题 | 需要的数据 |
|------|-----------|
| "我的系统有 edge 吗？" | 全局 Expectancy |
| "我有没有在执行这个 edge？" | 合规笔 Expectancy vs 违规笔 Expectancy |
| "我是因为策略问题还是执行问题在亏钱？" | 两者分别算 |
| "纪律给我带来多少 R 的差异？" | 合规 avg_R - 违规 avg_R |

**假设示例**：
- 合规笔（遵守决策链 + 止损）：Expectancy = 0.6R，PF = 1.8
- 违规笔（跳过决策链 / 穿越止损）：Expectancy = -0.3R，PF = 0.6
- 差异 = 0.9R/笔 → **"每次违反纪律平均多亏 0.9R"**

这个数字是极强的行为锚点——比抽象的"遵守纪律很重要"有说服力 10 倍。

### 5.2 实现前提

σ 系统已有的基础设施使这成为可能：
- `has_decision_chain`：trades/ 文件 If 1-5 是否完整
- `has_ema`：盘后 EMA 是否填写
- 止损遵守率：`stop_loss_price` vs `exit_price` 比对（violations_scan.py 已实现）

只需要一个 `compliant` 布尔标记（上述三项全满足 = true），然后对 compliant=true / compliant=false 两组分别算 Expectancy 和 PF。

---

## 综合判断

### 应追踪的指标体系

| 层级 | 指标 | 最低有效 n | σ 系统实现方式 |
|------|------|-----------|---------------|
| **每笔** | R 倍数 | 1 | 自动计算（entry/exit/stop） |
| **累计 Layer 2** | 胜率、Expectancy、Profit Factor、平均 R、最大连续亏损、最大回撤 | ≥10 初看趋势；≥30 初步参考 | strategy_metrics.py 周/月自动跑 |
| **累计 Layer 3** | Sharpe、Sortino、Calmar | ≥50 且跨 regime | 长期才启用 |
| **分组** | 以上所有按 setup_tag / stop_type / market_condition 分组 | 每组 ≥10 | WebUI 筛选 + 周报按组摘要 |
| **交叉** | 合规 vs 违规的 Expectancy/PF 对比 | 各组 ≥10 | 最有价值的分析维度 |

### 诚实约束

| 约束 | 阈值 | 动作 |
|------|------|------|
| n < 30 | 所有指标标 "U 级 / 可能是噪音" | 呈现但加警告 |
| n < 100 | 标 "初步参考" | 不做策略淘汰决策 |
| 单一 regime | 标 "单环境数据" | 不推广结论 |
| PF > 3.0 或 Sharpe > 3.0 | 标 "可能过拟合" | 怀疑而非庆祝 |
| 多 setup 比较 | 标 "未校正 multiple testing" | 不选"最好的"然后假装其他不存在 |

### 与 foundation_2026.md 的一致性

| foundation 约束 | 本调研响应 |
|-----------------|-----------|
| §三.5 样本量诚实 | 所有指标带 n 和置信等级标注 |
| §三.8 复盘必须有客观证据 | R 倍数 = 客观可计算的证据（无需主观判断） |
| §四.2 隐含假设盲区 #6 动态预警 | 滚动 Expectancy 折线图可充当策略退化的动态预警 |

---

## 引用清单

### S 级（同行评审）

- Ledoit, O. & Wolf, M. (2008). "Robust Performance Hypothesis Testing with the Sharpe Ratio." *Journal of Empirical Finance*, 15(5), 850-859.
- Bailey, D. & López de Prado, M. (2014). "The Deflated Sharpe Ratio." *Journal of Portfolio Management*, 40(5), 94-107.
- Lo, A. (2002). "The Statistics of Sharpe Ratios." *Financial Analysts Journal*, 58(4), 36-52.
- Harvey, C., Liu, Y., Zhu, H. (2016). "...and the Cross-Section of Expected Returns." *Review of Financial Studies*, 29(1), 5-68.
- López de Prado, M. (2018). *Advances in Financial Machine Learning*. Wiley.
- Magdon-Ismail, M. & Atiya, A. (2004). "Maximum Drawdown." *Risk Magazine*.
- Linnainmaa, J., Kalda, A., Egan, M. (2024). "Counting pennies, losing pounds: Biased learning about own trading ability." SSRN 4636623.

### M 级（行业标准 / 工作论文）

- Van Tharp (1998). *Trade Your Way to Financial Freedom*. McGraw-Hill.
- BacktestBase (2025). "Minimum Trades for a Valid Backtest? Calculator + Research."
- M1NDTR8DE (2025). "How many trades do you need? A sample size guide for traders."
- TradeProb (2025). "What a Sample Size Means in a Live Trading System."

### W 级（行业博客 / 专业站点）

- CrossTrade (2025). "Profit Factor | Performance Metrics."
- ACY (2025). "Trading Journal Strategy Metrics: How to Measure Setup Quality & System Edge."
- trading-journals.com (2025). "5 Metrics Every Trader Needs to Track." + "What to Actually Include in a Trading Journal Template."

---

*笔记版本：v0 | 上游 Plan：foundation_2026.md §三.5 样本量诚实 + design_phase3bc_notifications_webui.md §七 策略指标体系*
