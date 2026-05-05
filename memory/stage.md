---
description: 当前进化阶段与进展跟踪
last_updated: 2026-05-05
---

# 当前阶段：Stage 0（σ 引擎搭建）+ Plan/Design 调研工作流并行

## 双轨进度（v2 整合）

σ 系统目前同时在两个独立工作流上推进，互不阻塞：

```
轨道 A — Stage 进度（用户认知 + σ 引擎实战）
   ✅ Stage -1: 预备阶段（术语词典 + 风控规则）
   🟡 Stage 0:  σ 引擎基础（决策链 + 交易日志 + 仓位计算器）
       — 工具就绪，已记录第 1 笔实战（MGC 期货 2026-05-04）
       — 阻塞：未推到 Stage 1 阈值（需要 ≥10 笔有完整决策链的实战）
   ⏸️ Stage 1:  σ 引擎运行（开始记录 + 行为偏误积累）
   ⏸️ Stage 2:  σ 引擎进化（每周复盘 + 偏误检测启用）
   ⏸️ Stage 3:  α 引擎启动

轨道 B — Plan / Design 调研
   ✅ Phase 1 · Plan      (foundation_2026.md v5, master 286b2bd)
   ✅ Phase 2 · 调研       (entry_form_research v2, master 3906c41)
   🟡 Phase 2 · Design    (待启动)
   ⏸️ Phase 3 · Action    (拆 6 个独立小 PR，远未启动)
```

## 阶段产出物（轨道 A · Stage 0）

| 产出 | 状态 | 备注 |
|---|---|---|
| 决策链问题卡 | ✅ 已完成 | [decision-chain.md](../decision-chain.md) |
| 交易日志模板 | ✅ 已完成 | [trade-journal-template.md](../trade-journal-template.md) |
| 仓位计算器（基础版） | ✅ 已完成 | [tools/position_sizer.py](../tools/position_sizer.py) |
| AI 作为守门人 | ✅ 运作中 | 每次下单前走决策链 5 问 |
| 第 1 笔实战 | ✅ 已记录 | [trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md) |

## 阶段产出物（轨道 B · Phase 1 + Phase 2）

| 产出 | 状态 | 备注 |
|---|---|---|
| **Phase 1 · Plan 宪法** | ✅ master 286b2bd | foundation_2026.md v5（758 行；4 层目标结构 + 13 节 Plan 约束 + §四.2 隐含假设盲区）|
| **Phase 2 · 入口形态调研** | ✅ master 3906c41 | entry_form_research_2026.md v2（458 行）+ notes/07-12（4175 行）+ 5 份 same-model first-pass review（2982 行）+ 5 份 HCI/UX review prompts |
| **Cursor rules 基础设施** | ✅ master 60adc3d | .cursor/rules/ 含 graphify + karpathy + σ × karpathy precedence 仲裁（共 184 行 alwaysApply）|
| **知识库 sync Level A** | 🟡 进行中 | 本次提交（INDEX.md / stage.md / trader-profile.md / last_updated 头）|
| **知识库 sync Level B** | ⏸️ 推迟 | meta-rule N=1 vs productization 分层 / risk_rules 加产品过滤+临床+黑天鹅 / glossary 加 v5+v2 新术语 — 推到 Phase 2 Design 启动前 |
| **知识库 Level C claims/** | ⏸️ 推迟 | 12 项候选纲要已在 INDEX.md 列出；推到 Phase 2 Design 前后启动 |

## 阶段指标（轨道 A · Stage 0 → Stage 1 转入条件）

| 指标 | 当前值 | 目标 |
|---|---|---|
| 已记录实战交易笔数 | **1**（MGC 2026-05-04） | → ≥ 10 笔进入 Stage 1 |
| 决策链遵守率 | 暂无统计（n=1） | → 100% |
| 止损遵守率 | 暂无统计（n=1） | → 100% |
| 决策链准确率（预估胜率 vs 实际胜率） | 暂无统计 | 偏差 < 10 个百分点 |
| 仓位偏差（实际 vs 凯利建议） | 暂无统计 | 缩小中 |

> **注**：v5 §三.5 + entry_form_research §一调研 7 已显式声明：50 笔阈值在统计上是噪音；55% 胜率达 95% 置信需 ~380 笔（基于二项独立 IID 假设）。Stage 0 → 1 的"≥10 笔"门槛是**操作惯性**，不是统计意义上的"足够样本"。

## 阶段指标（轨道 B · Phase 2 → Phase 2 Design 转入条件）

| 指标 | 当前值 | 目标 |
|---|---|---|
| Phase 2 调研整合完成 | ✅（v2 master 3906c41）| Done |
| Phase 2 必决事项 12 项 | 全部已识别 | 进入 Design 时逐项决策 |
| 真外部多模型 review | ❌ 未做（用户明确选择跳过，接受同模型偏见 caveat）| 可选 / 推迟 |
| 用户确认 N=1 自评 | ✅（"我不是极端高风险人群"，2026-05-05）| Done — 已落到 entry_form_research §6.1 |

## 当前阻塞项

**轨道 A**：
- 主要阻塞：积累实战样本量（n=1 → ≥10 + 最终 ≥50）。**等用户实际交易**。
- 次要阻塞：第 1 笔 MGC 交易记录的事后复盘（v5 §三.8 复盘工具约束指出复盘必须含三段式：事前预设 → 实际发生 → 偏差）

**轨道 B**：
- Phase 2 Design 启动等用户拍板（选项：立刻启动 / 暂停 / 先做 Level B 知识库 sync）

## 阶段进度

- [x] **Stage -1**：预备阶段（术语词典 + 风控规则）
- [ ] **Stage 0**：σ 引擎基础（决策链 + 交易日志 + 仓位计算器 ✅，但实战样本仅 n=1，未达 Stage 1 转入条件）
- [ ] **Stage 1**：σ 引擎运行（开始记录 + 行为偏误积累，需要 ≥10 笔实战）
- [ ] **Stage 2**：σ 引擎进化（每周复盘 + 偏误检测启用）
- [ ] **Stage 3**：α 引擎启动

并行：

- [x] **Phase 1 · Plan**（foundation v5）
- [x] **Phase 2 · 调研**（entry_form_research v2）
- [ ] **Phase 2 · Design**（待启动）
- [ ] **Phase 3 · Action**（远未启动，拆 6 个独立小 PR）

## 更新记录

| 日期 | 更新内容 |
|---|---|
| 2026-05-03 | Stage 0 创建，Stage -1 标记完成 |
| **2026-05-05** | **Level A sync 更新**：(1) 引入"双轨进度"模型——区分轨道 A（Stage 实战进度）与轨道 B（Plan/Design 调研工作流），互不阻塞；(2) 加入 Phase 1 v5 + Phase 2 v2 + cursor rules 三个 master 提交的产出；(3) 更新阶段指标（实战 n=1，未达 Stage 1 转入）+ 阻塞项；(4) 加入 Stage 0 → 1 转入门槛的诚实标记（10 笔是操作惯性，50/380 笔的统计阈值在 v5 §三.5 / entry_form_research §一调研 7 显式说明）；(5) 当前阻塞项分轨道列出。**未改 Stage 系统本身的定义**（这是 Level B/Phase 2 Design 范围）。 |
