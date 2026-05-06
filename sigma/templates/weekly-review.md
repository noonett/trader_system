# σ 周复盘模板

> **每周末 30-60 分钟**——复制本模板到 reviews/weekly/YYYY-WW.md 后填写。
> 复盘前先跑 `make weekly-report`（AI 自动生成 reviews/weekly/YYYY-WW-auto.md）
> 再跑 `make violations-scan`（自动生成 reviews/violations/YYYY-WW.md）。
> 填完后 git add + commit "weekly YYYY-WW"。

---

## 日期：____ 年第 ____ 周（____ 至 ____）

## 一、AI 自动报告已读确认

- 我已读 reviews/weekly/YYYY-WW-auto.md
- 我已读 reviews/violations/YYYY-WW.md

## 二、三段式复盘（v5 §三.8 AAR 框架）

### 2.1 事前预设

> 本周开始时的盘前规则 if-then 主要内容摘要（从 sigma/daily/ 本周文件中提取关键 3 条）：

1. [___]
2. [___]
3. [___]

### 2.2 实际发生

> 本周实际交易的客观事实（从 trades/ 本周文件中提取）：


| 日期  | 标的  | 方向  | 结果  | 盈亏  | 决策链完整？ | 止损遵守？ |
| --- | --- | --- | --- | --- | ------ | ----- |
|     |     |     |     |     |        |       |


### 2.3 偏差

> 事前预设 vs 实际发生的差异——用 What 主导描述（禁 Why）：


| 偏差  | 对应的 if-then | 偏差方向 | 影响  |
| --- | ----------- | ---- | --- |
|     |             |      |     |


## 三、违规回应（必须逐条 acknowledge）

> 从 reviews/violations/YYYY-WW.md 逐条列出 + 写明 acknowledge / 解释 / 修正承诺：


| 违规项 | 我的回应 |
| --- | ---- |
|     |      |


## 四、周批量对账（从券商 App 导出 CSV → 与 trades/ 对账）

- 本周券商实际成交笔数：[___]
- 本周 trades/ 记录笔数：[___]
- 差异说明（如有漏记的"冲动交易"）：[___]

## 五、下周调整

> 基于本周偏差，下周的盘前规则 if-then 需要调整什么？（限 3 条以内）

1. [___]
2. [___]
3. [___]

## 六、本周 Honesty oath（v5 §三.8 + Capraro 2024 honesty oath）

> "这周我作为系统化交易者，以上记录是否足够可检验？如果有人读到这份复盘，他能用券商交割单 + git log 对账验证吗？"

- 是
- 否——不可验证的部分是：[___]

---

*模板版本：v0 | 来源：design_proposal_2026.md §三.2.1 + foundation §三.8*