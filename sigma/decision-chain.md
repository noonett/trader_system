# σ 决策链 — 下单前 5 项 if-then 承诺

> **设计来源**：foundation v5 §三.3 binding pre-commitment + §三.4 if-then 形式（Gollwitzer & Sheeran 2006, d=.27-.66 跨域元分析）+ entry_form_research v3 §四.4.1 BCT identity change（Michie 2013 BCTTv1 13.x）
>
> **禁开放式 Why 问题**（Watkins & Teasdale 2004, S 级：Why 触发反刍）。仅在事后复盘（reviews/weekly/）中允许 Why。
>
> **每笔交易前必须完成且不可跳过**——跳过会被后台违规扫描（scripts/violations_scan.py）自动检测并记入 reviews/violations/。

---

## 使用方法

每次开仓前，在 trades/YYYY/MM/YYYY-MM-DD-\<symbol\>-\<dir\>.md 的决策链章节填写以下 5 项 if-then。全部填完 → git add + commit "open \<symbol\>" → 然后才实际下单。

---

## 5 项 if-then 承诺

```
作为系统化交易者，本笔交易的 5 项 if-then 承诺：

If 1（论据）:
  我做这笔交易的论据是 [___]。
  证据等级：[S / M / W / U]
  置信度：[1-5]
  → 如果论据等级 < W 且置信度 < 3，则取消本笔交易。

If 2（止损）:
  我的入场理由被推翻的条件是 [___]，对应价格 [P_stop = ___]。
  → 如果到达 P_stop，则平仓——不重新评估、不延长止损。
  → 如果无法定义 P_stop（如无法设置止损的产品），则不开仓。

If 3（仓位）:
  这笔钱全亏损对我的影响是 [___]。
  本笔最大损失金额：[___]
  训练资金账户总额：[___]
  本笔占比：[___%]
  → 如果占比超过训练资金的 [___]%（由 risk_rules.md 单笔上限决定），
     则缩小仓位至上限以下。
  → 如果影响到日常生活 / 心理状态，说明仓位偏大。

If 4（情绪）:
  我现在的情绪状态是 [___]，强度 [1-5]。
  → 如果情绪 ∈ {兴奋, 愤怒, 报复, 翻本, 恐惧}，则不开仓。
     替代行为（BCT 8.2）：[写一段补充规则 / 起身离开屏幕 5 分钟 / 再读一遍当日 if-then]
  → 如果情绪强度 ≥ 4，建议暂停 30 分钟后重新评估。

If 5（期望值）:
  这类交易 10 笔我预期 [n] 笔赚钱。
  平均每笔赚 [G = ___]
  平均每笔亏 [L = ___]
  期望值 EV = n × G − (10−n) × L = [___]
  → 如果 EV ≤ 0，则不开仓。
  → 如果我答不出来（无法估算 n / G / L），则不开仓。

  Q5a 估计来源：
  - [ ] 过去类似交易的实际数据
  - [ ] 回测结果
  - [ ] 我的直觉 / 感觉
  - [ ] 别人的建议
  - [ ] 其他：[___]
  → 如果来源是"直觉"或"别人"，则把仓位减半。
```

---

## 决策前检查清单

- [ ] 我已经诚实地完成了 If 1-5 的每一项（这条记录是否足够可检验？）
- [ ] 我的止损已经明确（If 2 的 P_stop 已定义）
- [ ] 我的仓位不超过 risk_rules.md 允许的单笔上限（If 3 已验证）
- [ ] 我没有处于高风险情绪状态（If 4 已排除 {兴奋, 愤怒, 报复, 翻本, 恐惧}）
- [ ] reviews/alerts/ 没有未 acknowledge 的 alert

---

## 来源

- Gollwitzer & Sheeran (2006), implementation intentions 跨域元分析 d=.27-.66（S 级）
- Sheeran, Listrom, Gollwitzer (2024) *European Review of Social Psychology*, 642 项研究 meta（S 级）
- Michie et al. (2013) *Annals of Behavioral Medicine*, BCT Taxonomy v1 13.x identity change（M 级）
- Watkins & Teasdale (2004), Why 类提问触发反刍（S 级）
- Odean (1998) *Journal of Finance*, 处置效应（S 级）
- Fischbacher autocommitment 实验（S 级）

**诚实标记**：if-then 形式的效应量 d=.27-.66 来自跨领域元分析；在交易场景的迁移效应量预计被打折扣，需 N-of-1 验证（foundation §一调研 1 caveat）。
