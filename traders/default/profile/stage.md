---

## description: 当前进化阶段与进展跟踪
last_updated: 2026-05-07

# 当前阶段：v0 σ 已可运行（Phase 3a 在 `master`）

## 快照

- **Plan / Design**：`research/foundation_2026.md` v5 + `research/entry_form_research_2026.md` v3 + `research/design_proposal_2026.md` v0.1 — 已定稿为工程依据。
- **Action**：**Phase 3a（v0 启动硬集）已合并 `master`** — `sigma/`、`trades/TEMPLATE.md`、`reviews/`、`scripts/`、`Makefile`、红区 pre-commit 安装脚本等已就位。
- **下一里程碑**：**Phase 3b（P1）** — 见 `design_proposal_2026.md` §零 / §八.2（Mobile 提醒模板、训练资金对账、`risk_rules`/`glossary` Level B sync 等）；触发条件：**v0 运行满 4 周且 P0 KPI 达标**（或你主动提前开做文档同步 PR）。

## 旧 Stage 0 处置（历史）

用户 2026-05-06 确认 **不兼容老项目**。旧工具仅在归档中保留：

- [archive/deprecated_stage0/decision-chain.md](../archive/deprecated_stage0/decision-chain.md)
- [archive/deprecated_stage0/trade-journal-template.md](../archive/deprecated_stage0/trade-journal-template.md)
- [archive/deprecated_stage0/tools/position_sizer.py](../archive/deprecated_stage0/tools/position_sizer.py)
- 说明：[archive/deprecated_stage0/DEPRECATION_NOTES.md](../archive/deprecated_stage0/DEPRECATION_NOTES.md)

**v0 正本**：决策链 → `sigma/decision-chain.md`；交易流水 → `trades/` + `sigma/daily/` 盘前文件。

真实历史单 [trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md) 保留；**v0 KPI 不回溯**（见 `trades/README.md`）。

## Phase 进度总览


| Phase          | 状态    | 备注                                                                  |
| -------------- | ----- | ------------------------------------------------------------------- |
| 1 · Plan       | ✅     | `foundation_2026.md` v5                                             |
| 2 · 调研         | ✅     | `entry_form_research_2026.md` v3                                    |
| 2 · Design     | ✅     | `design_proposal_2026.md` v0.1 + `knowledge/clinical_self_check.md` |
| **3a · v0 硬集** | **✅** | 6 PR 已在 `master`；遗留缺陷修复（kpi_alert 三维 + violations #3 + sigma/daily/）  |
| **3b · v0.1**  | **🔧** | PR-6 glossary sync ✅ / PR-7c reminders+reconcile ✅ / PR-5 risk_rules 已在 v2 无需再改 |
| 3c / 3d        | ⏸️    | P2 / P3，见设计稿                                                        |


## v0 KPI 跟踪（简表）

完整定义见 [design_proposal_2026.md §四](../research/design_proposal_2026.md)。**计数自你开始按 v0 流程提交 `sigma/daily/` + `trades/` 之日起**（未启动前可填「—」）。


| KPI        | 4 周阈值       | 当前值 |
| ---------- | ----------- | --- |
| 盘前规则书写完成率  | ≥ 80% 交易日   | —   |
| 盘后 EMA 完成率 | ≥ 70% 已平仓交易 | —   |
| 决策链 5 问完整率 | ≥ 90% 开仓    | —   |


**整体退化**（design_proposal §四.4）：4 周 P0 < 50% → L2；8 周 → L1；12 周仍差 / 心理痛苦自评 ≥ 7 → 退出协议。

## 当前阻塞项

- **实战侧**：需你本人按 v0 写盘前、走 `trades/TEMPLATE.md`、周末 `make weekly-report`（Bash 环境）——无自动化替你下单。
- **工程侧**：Phase 3b 工程交付已完成（reminders + reconcile + glossary sync）；**Level C `claims/`** 仍未建库；Phase 3c WebUI 待 KPI 数据积累后启动。

## 更新记录


| 日期             | 更新内容                                                                     |
| -------------- | ------------------------------------------------------------------------ |
| 2026-05-03     | Stage 0 创建，Stage -1 标记完成                                                 |
| 2026-05-05     | Level A sync：双轨进度、Phase 1+2 产出、Stage 门槛诚实标记                              |
| 2026-05-06     | Phase 2 收口 + v0.1 设计修订 + 旧 Stage 0 迁 archive 计划                          |
| **2026-05-07** | **文档与进度对齐**：Phase 3a 标为已完成；修复失效链接与错误 frontmatter；KPI 改为「自 v0 实操起算」；阻塞项更新 |
| **2026-05-06** | **Phase 3b 工程推进**：(1) Phase 3a 遗留修复——kpi_alert.py §4.4 三维退化检测 + violations_scan.py check #3 仓位超阈值 + sigma/daily/ 目录 + Makefile 消息修正；(2) Phase 3b PR-7c——sigma/reminders/（Calendar 5 模板 + 邮件 cron 配置）+ scripts/reconcile_funds.py（D 类对账）；(3) Phase 3b PR-6——glossary Level B sync 12 术语入库 |
