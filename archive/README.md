# archive/ — 历史档案

> 这些文档**历史上有效**，但已被 master 上更新的文档**取代**。保留是为了追溯系统演进路径，**不是当前操作宪法**。

## 当前状态（随 `master` 更新）

如果你想看 σ 系统**当前**的设计，请查：

| 你想看 | 当前权威文档 |
|---|---|
| 系统目标 / Plan 级约束 | [`research/foundation_2026.md`](../research/foundation_2026.md)（v5）|
| 入口形态 / Plan→Design 桥梁 | [`research/entry_form_research_2026.md`](../research/entry_form_research_2026.md)（v3）|
| v0 操作规范（Design） | [`research/design_proposal_2026.md`](../research/design_proposal_2026.md)（v0.1）|
| 日盘前 / 交易流水模板 | [`sigma/`](../sigma/)、[`trades/TEMPLATE.md`](../trades/TEMPLATE.md) |
| 操作层风控规则 | [`knowledge/risk_rules.md`](../knowledge/risk_rules.md) |
| 元规则（诚实标记体系） | [`knowledge/meta-rule.md`](../knowledge/meta-rule.md) |
| 知识库索引 | [`knowledge/INDEX.md`](../knowledge/INDEX.md) |

## archive/ 内容（按时间顺序）

### `system_design.md` — 早期概念设计
- **作用**：σ 系统最初的设计稿（Stage 0 之前）
- **被取代**：历史上曾以同目录 [`system_spec_v2.md`](system_spec_v2.md) 为「规范 V2」→ 二者均已归档；**当前**以 `research/foundation_2026.md` v5 等为权威（见上表）
- **历史价值**：可看到原始的 α/σ 双引擎构想；Phase 1 调研之前的隐含假设
- **诚实标记**：当时假设的"AI 必为核心交互入口" 已在 v4 撤销；当时的"承诺训练能让你赚钱"叙事已在 v2 修正为 4 层目标结构。**任何与 foundation v5 冲突的措辞，以 v5 为准**

### `system_spec_v2.md` — 规范文档 V2（早期）
- **作用**：Stage -1 前后的长文规范（双引擎、核心论题、进化指标、失败模式等）
- **状态（2026-05-07）**：从仓库**根目录移入** `archive/`；文首有指向 `foundation` / `entry_form` / `design_proposal` 的归档说明
- **被取代**：Plan → `research/foundation_2026.md` v5；调研 → `entry_form_research` v3；v0 结构 → `design_proposal` v0.1

### `audit_report.md` — 第一轮审计
- **作用**：2026-05-03 第一轮审计——识别 7 个 P0/P1 缺口
- **被取代**：审计触发的修复曾合入 Stage -1 的 glossary.md / risk_rules.md / `system_spec_v2.md`（现于本目录），并最终演进为 foundation v5
- **历史价值**：看 Phase 1 何时从"假设充分"转向"承认证据不足"

### `audit_report_v2.md` — 第二轮审计
- **作用**：第一轮审计后再做的 review，识别 4 个战略层问题
- **被取代**：触发了 Phase 1 v1（"不骗自己"二元目标）的最初定位；之后在 v2-v5 期间多次被修正
- **历史价值**：查 v1 的目标定位最初为何偏激进

### `MR_20260503_audit_fixes.md` — 两轮审计后的 MR 描述
- **作用**：把审计修复整合的 merge request 描述
- **被取代**：单一 squash commit `286b2bd` (Phase 1 v5) 和后续 commit 已涵盖全部修复 + 远超
- **历史价值**：Phase 1 之前最后一份"系统状态报告"

## 为什么不直接删？

按 `.cursor/rules/sigma-meta-rule-precedence.mdc` 的 σ × karpathy 仲裁规则——
- **karpathy §3** 说"Don't remove pre-existing dead code unless asked"
- **σ 元规则** 说"诚实标记体系违例必须显式修正"

这些文档**不是 dead code**——它们是真实的历史轨迹，删了等于擦除证据链。但保留在仓库根目录会与当前权威文档**产生表面冲突**（用户访问根目录会看到"哪个是真的"的歧义）。

**两规则共同的解 = archive/**：保留历史完整性 + 物理分离当前与历史 + README 显式说明优先级。

## 不要做的事

- 不要在 archive/ 下添加新文档（这里是单向归档，不是工作区）
- 不要修改 archive/ 下的旧文档（保持原样作历史快照；如发现引用错误等元规则违例，加 caveat 而非改原文）
- 不要把 archive/ 下的链接作为 σ 系统当前规则引用——查 master 上的当前权威文档
