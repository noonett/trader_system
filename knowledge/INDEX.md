# 知识库索引

> 最后更新：2026-05-08（`CLAUDE.md` → `AGENTS.md` 根说明改名）

## 元规则

- [meta-rule.md](meta-rule.md) — 论据来源与诚实标记（S 级约束，不可被任何知识条目覆盖）
- [AGENTS.md](../AGENTS.md) — 仓库根上的 **Cursor / Agent 项目说明**（用户画像、目录地图、权威文档指针；原 `CLAUDE.md`）

## 基础参考

- [glossary.md](glossary.md) — 术语词典（50+ 术语已入库，含学术来源和诚实标记）
- [risk_rules.md](risk_rules.md) — 风控规则（仓位、止损、危险信号、不做清单）
- [clinical_self_check.md](clinical_self_check.md) — **Phase 2 Design 伴生交付（v0，2026-05-06）**：N=1 临床安全自检模板（PHQ-9 + GAD-7 + 5 项投机交易行为自查 + DSM-5 9 项 + 5 项简化禁忌症 + 中国大陆心理援助资源最小指针）；不 lockout、用户自决重测；状态性风险防御保留。

## 调研档案（research/）

> Phase 1 + Phase 2 完整证据链。这一层是**调研历史档案**——做实战决策时不需要每次翻；要查具体证据、要追溯结论由来时来这里。

### 顶层综合文档（按 Plan/Design/Action 分层）

- [research/foundation_2026.md](../research/foundation_2026.md) — **σ 系统证据基础（v5）**，758 行，13 节 Plan 级约束 + 4 层目标结构 + 12 个 S 级证据组件 + 4.2 隐含假设盲区 6 条。**当前 Plan 宪法**。
- [research/entry_form_research_2026.md](../research/entry_form_research_2026.md) — Phase 2 入口形态调研整合（**v3 cleanup**，2026-05-06），~750 行。Plan→Design 桥梁；6+1 收敛信号 + §四.3-4.10 12 项 Phase 2 Design 必决事项（v3 补齐 v2 内部不一致）+ §六 N=1 vs productization 临床安全分级。
- [research/design_proposal_2026.md](../research/design_proposal_2026.md) — **Phase 2 Design v0.1（2026-05-06，A+ 按优先级分阶段修订）**，~1000 行。在 N=1 用户语境下对 12 项 D1–D12 给出推荐选择 + 主证据 + 反向证据 + 退化路径；§零 优先级矩阵（P0/P1/P2/P3）+ Phase 3a/b/c/d 阶段拆分 + 11 个独立小 PR；定义 v0 sigma/ 目录结构（含 scripts/ + ai-roles.md + reviews/violations/ + reviews/alerts/ + webui/ 占位）+ 5 层工作流（用户手动 + AI 后台批处理 + 后台强制风控 4 类 A/B/C/D + Mobile 提醒 + WebUI 渲染）+ 4 周可证伪 KPI + 4→3→2→1→0 退化 + 退出协议；§六 相容性核查双栏（Phase 3a 后 vs 前）；§七 处置旧 Stage 0 工具。**当前 Design 主交付**。

### 原始调研笔记（research/notes/）


| 笔记                                                                                                   | 主题                           | 行数    | Phase |
| ---------------------------------------------------------------------------------------------------- | ---------------------------- | ----- | ----- |
| [01_journaling_evidence.md](../research/notes/01_journaling_evidence.md)                             | 交易日志范式实证基础                   | ~470  | 1     |
| [02_retail_failure_2020_2026.md](../research/notes/02_retail_failure_2020_2026.md)                   | 散户失败根因 2020-2026             | ~500  | 1     |
| [03_ai_coaching_evidence.md](../research/notes/03_ai_coaching_evidence.md)                           | AI 教练实证证据（含 §D v4+ 推翻标注）     | ~660  | 1     |
| [04_deliberate_practice_metacognition.md](../research/notes/04_deliberate_practice_metacognition.md) | 刻意练习与元认知在交易的适用性              | ~950  | 1     |
| [05_alternative_paradigms.md](../research/notes/05_alternative_paradigms.md)                         | 替代范式审视 + 退出协议                | ~995  | 1     |
| [06_tool_design_retention.md](../research/notes/06_tool_design_retention.md)                         | 工具可用性 / 习惯形成 / 留存            | ~1248 | 1     |
| [07_entry_form_comparison.md](../research/notes/07_entry_form_comparison.md)                         | 6 类入口对比                      | 866   | 2     |
| [08_recording_medium.md](../research/notes/08_recording_medium.md)                                   | 记录介质对比（含 v2 工程现实 caveat 4 项） | 661   | 2     |
| [09_foreground_vs_background_ai.md](../research/notes/09_foreground_vs_background_ai.md)             | 前台 vs 后台 vs 无 AI             | 623   | 2     |
| [10_multi_vs_single_end.md](../research/notes/10_multi_vs_single_end.md)                             | 单端 vs 多端部署                   | 510   | 2     |
| [11_context_switching_cost.md](../research/notes/11_context_switching_cost.md)                       | 上下文切换成本 + 物理可达性矩阵            | 922   | 2     |
| [12_no_ai_option.md](../research/notes/12_no_ai_option.md)                                           | "完全不用 AI 前台"作为合法选项           | 893   | 2     |


### Review 档案

- Phase 1 multi-model review 模板：[research/review_prompts/](../research/review_prompts/) — 5 视角 prompt
- Phase 1 review 结果：`pr_1_review_comments*.md`（4 份：Gemini 4 inline / GPT-5.5 10 inline / Gemini 3.1 Pro 5 视角 / GPT-5.5 5 视角）
- Phase 2 multi-model review 模板：[research/review_prompts_phase2/](../research/review_prompts_phase2/) — 5 视角 HCI/UX 侧重 prompt
- Phase 2 same-model first-pass review：`pr_3_review_*_claude_first_pass.md`（5 份；含 honesty_caveat frontmatter 声明同模型偏见无法侦测）

## 主张库 (claims/)

> ⚠️ **暂未建库（Level C 未启动）。** Phase 1 v5 + Phase 2 v3 + Phase 2 Design v0.1 已列出多项候选；**Phase 3a 工程已就位**，建库仍可安排在 Phase 3b（Level B sync）或你主动开 `claims/` 首条时。

候选条目（仅列纲要，未真正建库；详见 [research/foundation_2026.md](../research/foundation_2026.md) / [entry_form_research_2026.md](../research/entry_form_research_2026.md) / [design_proposal_2026.md](../research/design_proposal_2026.md) 原文）：


| 候选编号         | 主题                                                                                           | 来源                                                                  | 状态  |
| ------------ | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | --- |
| `behav-001`  | Implementation intention 跨领域 d=0.65；交易场景迁移效应量预计被打折                                           | foundation §一调研 1 + Sheeran/Listrom/Gollwitzer 2024                 | 候选  |
| `behav-002`  | AAR 复盘在复杂模糊任务 d=0.79；σ 证据最强训练方法                                                              | foundation §一调研 1 + Keiser & Arthur 2021                            | 候选  |
| `behav-003`  | 高反刍用户写日志情绪恢复变差且持续 9 月                                                                        | foundation §一调研 1 + Sbarra 2013                                     | 候选  |
| `behav-004`  | 痛苦驱动型交易（DSM-5 #5）= σ 系统最危险的过渡机制                                                              | entry_form_research §6.3 + clinical_self_check §1.4                 | 候选  |
| `behav-005`  | 用户预先承诺 + 必经之路 > 单方施加的 reminder                                                               | entry_form_research 收敛信号 6 + Patterson 2020                         | 候选  |
| `system-001` | 产品过滤器分级（红/黄/绿）— σ 系统硬约束                                                                      | foundation §三.10                                                    | 候选  |
| `system-002` | 早晨规则书写 ROI 数量级最高（0-5 工时 vs 盘中浮窗 80-160 工时）                                                   | entry_form_research §四.5 + design_proposal §二 D10                   | 候选  |
| `system-003` | 完全不用 AI 前台是合法选项（对临床高风险用户必需）                                                                  | entry_form_research §6.1 + notes/12 + design_proposal §二 D2         | 候选  |
| `system-004` | 6 信号实际由 5-10 篇核心论文反复使用——收敛强度被结构性夸大                                                           | entry_form_research §二（v2 元方法学诚实标记）                                 | 候选  |
| `system-005` | Implementation intention 与 Habit formation 是两套范式                                             | entry_form_research 收敛信号 7（v2 新增）                                   | 候选  |
| `system-006` | v0 退化路径 4→1 时唯一保留早晨规则书写                                                                      | entry_form_research §四.9 + design_proposal §二 D11                   | 候选  |
| `system-007` | BCT 三组（identity 13.x / behavioral substitution 8.2 / environmental restructuring 12.x）必须显式落地 | entry_form_research §四.4 + design_proposal §二 D9                    | 候选  |
| `tech-001`   | A 股 9:20-9:25 集合竞价不可撤单 = 市场制度免费提供的 commitment device                                         | entry_form_research §四.7 + design_proposal §二 D7                    | 候选  |
| `me-001`     | 用户自评不在极端高风险 → 临床安全自检不作 lockout gate                                                          | entry_form_research §6.1 + 用户输入 2026-05-05 + clinical_self_check 整体 | 候选  |
| `me-002`     | 用户明确"老 Stage 0 工具不需要兼容，全新项目" → v0 是全新设计                                                      | 用户输入 2026-05-06 + design_proposal §一.1 + §七                         | 候选  |
| `system-008` | 后台 AI 周读 + 自动违规扫描是 σ 物理边界内激活中等被审视感的核心机制                                                      | design_proposal v0.1 §三.2.2 + §收敛信号 5 + Lelkes 2012                 | 候选  |
| `system-009` | σ 物理边界内 4 类后台强制风控（A 违规扫描 + B KPI alert + C 红区 schema 拒绝 + D 训练资金对账）                          | design_proposal v0.1 §三.2.3 + foundation §三.3 / §三.10 / §三.12       | 候选  |
| `system-010` | Mobile 仅作时点提醒辅助层 + 不承担主入口（与 §收敛信号 2 原文严格相容）                                                  | design_proposal v0.1 §二 D4 + §三.2.4 + entry_form_research §收敛信号 2   | 候选  |
| `system-011` | D3 介质（markdown + git）是 N=1 起点偏好胜出的 satisficing，不是"最优解"                                       | design_proposal v0.1 §九.2 #7 + 用户 2026-05-06 当面抓出                   | 候选  |


## 待验证队列 (testing/queue.md)

⏸️ **暂未建立**（Phase 3 Action PR-8 范围 — KPI 计算工具上线后联动建立）。v0 σ 系统 6 个 P0/P1 KPI + 3 个校准 KPI 已在 [design_proposal §四](../research/design_proposal_2026.md) 完整定义；4 周节点判定后真实数据进入此队列。

## 已归档

- **旧 Stage 0 工具**（不参与 v0 工作流）：[archive/deprecated_stage0/](../archive/deprecated_stage0/) + [DEPRECATION_NOTES.md](../archive/deprecated_stage0/DEPRECATION_NOTES.md)
- **其它历史文档**：见 [archive/README.md](../archive/README.md)

## 学习源 (sources/)

> 已在 research/notes/01-12 + entry_form_research_2026.md 中累计引用 80+ 篇同行评审论文 + 15+ 部书籍 + 多份监管报告。**未建立独立 sources/ 目录索引**——目前需要时直接在 research/ 中 grep。

主要 S 级来源类别（按调研笔记归类，不重复）：

- **行为金融**：Barber/Odean 系列、Cipriano/Gruca/Jiao 2020、Schwager Market Wizards、Annie Duke、Mauboussin
- **行为改变 / mHealth**：Gollwitzer & Sheeran 2006、Wood/Lally habit formation、Sheeran/Listrom 2024 642-meta、Wen 2017 JMIR、Pratap 2020 npj Digital Medicine、Linardon 2024
- **AI 教练 / 反向证据**：Bastani 2024 PNAS、METR 2025、MIT Kosmyna 2025、Microsoft × CMU 2025、Hodge 2023、Liu et al. 2026 arXiv 2604.04721
- **AAR / 复盘**：Tannenbaum 2013、Keiser & Arthur 2021
- **临床心理学**：Sbarra 2013、Watkins & Teasdale 2004、Karyotaki 2017 + Cuijpers 2021 + Andersson 2014/Carlbring 2018、PHQ-9 / GAD-7 / PGSI 量表原始文献
- **工程 / HCI**：Scarr et al. 2014 CHI、Cockburn 2014（senior author 视角）、Perez De Rosso & Jackson OOPSLA 2016、Patterson 2020 Cornell RCT、Masicampo & Baumeister 2011 JPSP

---

## 条目编号规则

```
[领域]-[序号]
领域代号：
  macro    = 宏观
  flow     = 资金流向
  funda    = 基本面
  tech     = 技术面/价格行为
  behav    = 行为金融/心理学
  system   = 系统设计
  me       = 关于用户（你自己的认知）
```

## 每个主张条目必须包含

1. 主张陈述（一句话）
2. 来源（按 S/M/W/U 分级）
3. 置信度（1-5，含义见 meta-rule.md）
4. 诚实标记（如果需要）
5. 系统影响（如果为真，改变 α/σ 的什么？）
6. 可测试假设（我们怎么验证？）
7. 状态（待验证 / 已验证 / 已反驳 / 部分成立 / 已归档）
8. 适用范围（哪个市场？哪个周期？）

---

## 更新记录


| 日期                 | 更新内容                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-05-03         | 初版索引创建（Stage -1 完成时）                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2026-05-05         | **Level A sync 更新**：加入 research/ 章节链接；claims/ 候选 12 项；学习源类别按调研笔记归类。                                                                                                                                                                                                                                                                                                                                                             |
| **2026-05-06**     | **Phase 2 Design 收口 sync**：(1) 顶层综合文档加入 [design_proposal_2026.md](../research/design_proposal_2026.md) v0；entry_form_research 标记 v3 cleanup（补齐 v2 内部不一致）；(2) 基础参考加入 [clinical_self_check.md](clinical_self_check.md)（Phase 2 Design D12 伴生交付）；(3) claims/ 候选从 12 项扩到 15 项（新增 system-006 退化路径 / system-007 BCT 三组 / me-002 全新项目）；(4) 待验证队列说明改为"Phase 3 Action PR-8 KPI 工具上线后建立"。**未建实际 claims 库（Level C 仍推到 Phase 3 Action 后）**。 |
| **2026-05-06 (晚)** | **Phase 2 Design v0.1 修订 sync**：(1) design_proposal 标 v0.1（A+ 按优先级分阶段修订）—— 加后台强制风控 + WebUI 渲染层 + Mobile 提醒；P0/P1/P2/P3 + Phase 3a/b/c/d 阶段；总 PR 从 8 扩到 11；(2) **新增 4 项候选 claims**：system-008 后台 AI 周读 + 自动违规扫描激活中等被审视感 / system-009 σ 物理边界内 4 类后台强制风控（A/B/C/D） / system-010 Mobile 提醒辅助层（不主入口）/ system-011 D3 介质 satisficing 性质显式声明（v0 错标"最优"，v0.1 修正）。                                                                         |
| **2026-05-07**      | **Phase 3a 落地后索引清理**：`deprecated/` 占位改为指向 `archive/deprecated_stage0/`；claims 说明改为「3a 已就位、建库时间可协商」；顶栏 `last_updated` 更新。                                                                                                                                                                                                                                                                                                                                    |
| **2026-05-08**      | **根说明改名**：元规则节增加 [AGENTS.md](../AGENTS.md) 链接（原 `CLAUDE.md` → Cursor 惯例文件名）。                                                                                                                                                                                                                                                                                                                                                                                              |


