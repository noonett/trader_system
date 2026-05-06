---
description: 当前进化阶段与进展跟踪
last_updated: 2026-05-06
---

# 当前阶段：Phase 2 Design 完成 — 等用户拍板进入 Phase 3 Action

## 重大转折（2026-05-06）

**用户明确"老 Stage 0 工具不需要兼容，全新项目"**——这改变了整个轨道结构：

- 旧"Stage -1 / Stage 0 / Stage 1+"渐进路径在 Phase 2 Design 中被重新定义
- v0 σ 系统是**全新设计**（详见 [research/design_proposal_2026.md](../research/design_proposal_2026.md)），不沿用旧 Stage 0 的 [decision-chain.md](../decision-chain.md) / [trade-journal-template.md](../trade-journal-template.md) / [tools/position_sizer.py](../tools/position_sizer.py)
- v0 启动后这些旧文件移到 archive/deprecated_stage0/（Phase 3 Action PR-1 范围）
- 用户已记录的真实交易 [trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md) 保留（不强制按新格式回填）

## 双轨进度（v3 整合）

```
轨道 A — Stage 进度（旧定义已被 Phase 2 Design 取代）
   ⚠️ 旧 Stage -1 / Stage 0 / Stage 1+ 框架在 v0 σ 系统启动后失效
   📦 旧 Stage 0 工具按 design_proposal_2026.md §七 处置（Phase 3 Action PR-1）

轨道 B — Plan / Design 调研 / 全新 v0 设计
   ✅ Phase 1 · Plan       (foundation_2026.md v5, master 286b2bd)
   ✅ Phase 2 · 调研 v1    (entry_form_research v1, master 3906c41)
   ✅ Phase 2 · 调研 v3 cleanup  (entry_form_research v3, branch c1c77f5)
   ✅ Phase 2 · Design     (design_proposal_2026.md v0, branch 17d186f)
   🟡 Phase 3 · Action     (待用户拍板 — 8 个独立小 PR 骨架已列出)

旧 Stage 进度（保留为历史档案）：
   ✅ Stage -1: 预备阶段（术语词典 + 风控规则）— 知识库已建
   🟡→📦 Stage 0:  σ 引擎基础 — 工具就绪并记录 1 笔实战，但 v0 全新设计已取代
   ⏸️→📦 Stage 1/2/3:  在 v0 σ 系统中重新对应（详见 design_proposal §四 KPI + §五 退出协议）
```

## 阶段产出物（旧轨道 A · Stage 0 — 已被 Phase 2 Design 取代）

| 产出 | 旧状态 | v0 处置 |
|---|---|---|
| 决策链问题卡 | ✅ 旧版 | 📦 移到 archive/deprecated_stage0/（v0 在 sigma/decision-chain.md 重写为 if-then + identity 形式）|
| 交易日志模板 | ✅ 旧版 | 📦 移到 archive/deprecated_stage0/（v0 在 trades/YYYY/MM/<single>.md 一文聚合）|
| 仓位计算器（基础版）| ✅ 旧版 | 📦 移到 archive/deprecated_stage0/tools/（v0 仓位嵌入决策链 If 5 + Q5a 来源校验）|
| AI 作为守门人 | ✅ 运作中 | 重新定义为"D2 受限 AI（B 后台静默 + C 前台对话仅在用户主动调用且独立思考后）"|
| 第 1 笔实战 | ✅ 已记录 | [trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md) 保留——v0 KPI 计算从 v0 启动日开始，不回溯 |

## 阶段产出物（轨道 B · Phase 1 + Phase 2 全部完成）

| 产出 | 状态 | 备注 |
|---|---|---|
| **Phase 1 · Plan 宪法** | ✅ master 286b2bd | foundation_2026.md v5（758 行；4 层目标结构 + 13 节 Plan 约束 + §四.2 隐含假设盲区）|
| **Phase 2 · 入口形态调研 v2** | ✅ master 3906c41 | entry_form_research_2026.md v2 + notes/07-12（4175 行）+ 5 份 first-pass review |
| **Phase 2 · 调研 v3 cleanup** | ✅ branch c1c77f5 | entry_form_research v3 补齐 §四.3-4.10 v2 内部不一致 |
| **Phase 2 · Design v0** | ✅ branch 17d186f | [design_proposal_2026.md v0](../research/design_proposal_2026.md)（659 行）+ [clinical_self_check.md](../knowledge/clinical_self_check.md)（伴生交付，265 行）|
| **Cursor rules 基础设施** | ✅ master 60adc3d | .cursor/rules/ 含 graphify + karpathy + σ × karpathy precedence 仲裁 |
| **知识库 sync Level A** | ✅ 完成 | INDEX.md / stage.md / trader-profile.md（多次更新）|
| **知识库 sync Level B** | ⏸️ 推到 Phase 3 Action PR-5/6 | meta-rule N=1 vs productization 分层 / risk_rules 加产品过滤+临床+黑天鹅 / glossary 加 v3+v5 新术语 |
| **知识库 Level C claims/** | ⏸️ 推到 Phase 3 Action 后 | 12 项候选纲要已在 INDEX.md 列出 |

## 阶段指标（v0 σ 系统 KPI — Phase 3 Action 启动后才能开始测量）

> **指标定义已迁移**：v0 σ 系统的可证伪性 KPI 在 [research/design_proposal_2026.md §四](../research/design_proposal_2026.md) 完整定义。本表是简化跟踪，启动 v0 后填写。

**P0 KPI（4 周节点必须达标）**：

| KPI | 4 周阈值 | 当前值 |
|---|---|---|
| 盘前规则书写完成率 | ≥ 80% 交易日 | v0 未启动 |
| 盘后 EMA 完成率 | ≥ 70% 已平仓交易 | v0 未启动 |
| 决策链 5 问完整率 | ≥ 90% 开仓 | v0 未启动 |

**P1 KPI（监测但不强制）**：

| KPI | 4 周阈值 | 当前值 |
|---|---|---|
| 周复盘完成率 | ≥ 50% 周次 | v0 未启动 |
| 月校准完成率 | ≥ 1 次/月 | v0 未启动 |
| 9:20 集合竞价 binding 利用率 | ≥ 70% A 股交易日 | v0 未启动 |

**校准 KPI（每月 1 次）**：

| KPI | 4 周阈值 | 当前值 |
|---|---|---|
| 决策链预估准确率 | 偏差 < 10 个百分点 | v0 未启动 |
| 仓位偏差（实际 vs 凯利建议）| 缩小中 | v0 未启动 |
| 止损遵守率 | ≥ 95% | v0 未启动 |

**整体退化触发**（design_proposal §四.4）：4 周 P0 < 50% → L2；8 周 P0 < 50% → L1；12 周仍 < 50% → 退出协议。

## 阶段指标（轨道 B · Phase 3 Action 转入条件）

| 指标 | 当前值 | 目标 |
|---|---|---|
| Phase 1 + Phase 2 全部产出 | ✅ Plan 宪法 + 调研 v3 + Design v0 + clinical_self_check | Done |
| 用户拍板 Phase 3 启动 | ⏸️ 等用户 | Done 后开始 PR-1（archive/deprecated_stage0/ 移动）|
| 真外部多模型 review | ❌ 未做（用户接受同模型偏见 caveat）| 可选 / 推迟 |
| 用户确认 N=1 自评 | ✅（"不是极端高风险人群"，2026-05-05）+（"老项目不兼容 / 全新项目"，2026-05-06）| Done — 已落到 entry_form_research v3 §6.1 + design_proposal §一.1 |

## 当前阻塞项

**轨道 B**：
- Phase 3 Action 启动等用户拍板（建议从 PR-1 开始：archive/deprecated_stage0/ 移动 + DEPRECATION_NOTES.md）
- 8 个独立小 PR 骨架已在 [design_proposal_2026.md §八.2](../research/design_proposal_2026.md) 列出

**v0 σ 实战阻塞**（Phase 3 Action 完成后开始）：
- v0 启动条件 = PR-1 + PR-2（sigma/ 5 模板）+ PR-3（trades/ 新格式 README）+ PR-4（reviews/ 目录初始化）— 最小可用集
- 启动后 4 周节点判定 KPI

## 阶段进度

- [x] **Phase 1 · Plan 宪法**（foundation v5，13 节 Plan 级证据驱动约束）
- [x] **Phase 2 · 调研 v1/v2**（entry_form_research + 12 篇 notes + 5 份 first-pass review）
- [x] **Phase 2 · 调研 v3 cleanup**（补齐 §四.3-4.10 v2 内部不一致）
- [x] **Phase 2 · Design v0**（design_proposal_2026.md + clinical_self_check.md）
- [ ] **Phase 3 · Action**（8 个独立小 PR，待启动）
  - [ ] PR-1: archive/deprecated_stage0/ 文件移动 + DEPRECATION_NOTES.md
  - [ ] PR-2: sigma/ 5 个模板（pre-market / post-trade-ema / decision-chain / weekly / monthly）
  - [ ] PR-3: trades/ 新格式 README + 1 个示例文件
  - [ ] PR-4: reviews/ 目录初始化 + README
  - [ ] PR-5: knowledge/risk_rules.md 加产品过滤器 + 临床触发 + 黑天鹅章节（Level B sync）
  - [ ] PR-6: knowledge/glossary.md 加 v3 + foundation v5 新术语（Level B sync）
  - [ ] PR-7: AI 后台读 git log 的 prompt 模板
  - [ ] PR-8: KPI 计算工具（最简版）
- [ ] **v0 σ 启动**（PR-1+2+3+4 完成后；最小可用集）
- [ ] **v0 4 周节点判定**（P0 KPI 达标 / 退化 / 退出协议）
- [ ] **α 引擎调研启动**（v0 σ 稳定后，远未启动）

## 更新记录

| 日期 | 更新内容 |
|---|---|
| 2026-05-03 | Stage 0 创建，Stage -1 标记完成 |
| 2026-05-05 | **Level A sync 更新**：(1) 引入"双轨进度"模型——区分轨道 A（Stage 实战进度）与轨道 B（Plan/Design 调研工作流），互不阻塞；(2) 加入 Phase 1 v5 + Phase 2 v2 + cursor rules 三个 master 提交的产出；(3) 更新阶段指标（实战 n=1，未达 Stage 1 转入）+ 阻塞项；(4) 加入 Stage 0 → 1 转入门槛的诚实标记；(5) 当前阻塞项分轨道列出。 |
| **2026-05-06** | **Phase 2 收口 + 旧 Stage 0 deprecation**：(1) 用户明确"老项目不需要兼容，全新项目"——Stage -1 / 0 / 1+ 旧框架在 v0 σ 系统中失效，旧工具按 design_proposal §七 处置（移到 archive/deprecated_stage0/）；(2) 完成 Phase 2 调研 v3 cleanup（branch c1c77f5）补齐 §四.3-4.10 v2 内部不一致；(3) 完成 Phase 2 Design v0（branch 17d186f）+ 伴生交付 clinical_self_check.md；(4) 阶段指标从"Stage 0 → 1 实战样本"重新定义为"v0 σ KPI"（P0 / P1 / 校准三组）；(5) 阶段进度重写为 Phase 1+2 全完成 → Phase 3 Action 8 个独立小 PR 待启动；(6) 真实交易记录 trades/2026/05/2026-05-04-mgc-202606-long.md 保留——v0 KPI 不回溯。**未触发 foundation v6 修订**（v5 仍是 Plan 宪法）。 |
