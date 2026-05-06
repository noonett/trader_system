---

## date: YYYY-MM-DD

symbol: 
direction: # long / short
product_class: # green-passive-etf / green-cash-stock / yellow-small-future / red
market: # a-share / hk-stock / futures-cme / futures-cn
setup_tag: # 策略标签（如 breakout-retest / mean-reversion / trend-follow）
stop_type: # 止损类型（structure / atr / percent / time）
target_type: # 止盈类型（fixed-rr / trailing / structure / time）
target_rr: # 目标盈亏比（如 2.0）
market_condition: # 市场状态（trending / ranging / volatile / low-vol）
entry_price: 
exit_price: 
position_size: 
stop_loss_price: 
pnl_gross: 
pnl_net: # 毛盈亏 - 手续费 - 滑点 - 融资/隔夜成本
fees: 

# YYYY-MM-DD  <long/short>

## 一、盘前 if-then 参考

> 从 sigma/daily/YYYY-MM/YYYY-MM-DD-pre.md 复制今日 §一 的关键规则摘要：

- 今日 setup：
- 今日最大风险预算：
- 今日止损纪律：

## 二、决策链 5 项 if-then（开仓前填写）

> 复制 sigma/decision-chain.md 的模板填写：

### If 1（论据）

我做这笔交易的论据是：
证据等级：[S / M / W / U]
置信度：[1-5]

### If 2（止损）

入场理由被推翻的条件是：
对应价格 P_stop =

### If 3（仓位）

全亏对我的影响：
本笔最大损失金额：
训练资金账户总额：
本笔占比：___%

### If 4（情绪）

当前情绪状态：
强度：[1-5]

### If 5（期望值）

10 笔同类预期 [n] 笔赚钱
平均每笔赚 G =
平均每笔亏 L =
EV = n × G − (10−n) × L =

Q5a 估计来源：

- 过去类似交易的实际数据
- 回测结果
- 我的直觉 / 感觉
- 别人的建议

## 三、决策前检查清单

- If 1-5 全部填完且足够可检验
- P_stop 已定义
- 仓位不超过 risk_rules.md 单笔上限
- 情绪不属于 {兴奋, 愤怒, 报复, 翻本, 恐惧}
- reviews/alerts/ 无未 acknowledge 的 alert
- 入场时截了图（贴给 AI 即可，AI 代为归档）

## 四、盘后 EMA（平仓后 30 分钟内填写，≤4 字段）

1. 结果：[盈 / 亏 / 平]，金额
2. 是否按计划执行：[是 / 否]——偏离了哪一条？
3. 平仓时情绪：，强度 [1-5]
4. 一句话信号：

## 五、截图证据

> 截图由 AI 代为整理（你贴图 + 说一句话，AI 处理命名和归档）。
> 下方由 AI 填写——周复盘时引用这些做对照分析。

**入场截图**：
- <!-- AI 填写：screenshots/{trade-id}-entry-N.png -->

**平仓截图**：
- <!-- AI 填写：screenshots/{trade-id}-exit-N.png -->

**过程截图**（可选）：
- <!-- AI 填写：screenshots/{trade-id}-context-N.png -->

## 六、事后复盘（可选——周复盘时写更详细的在 reviews/weekly/）

事前预设 vs 实际发生 vs 偏差：

---

*模板版本：v0.1 | 来源：design_proposal_2026.md §三.2.1 + §三.3 + foundation §五 AAR 客观证据约束*