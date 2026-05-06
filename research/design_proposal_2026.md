# Phase 2 Design — σ 系统 v0 设计提案（N=1 用户语境，全新设计）

> **位置**：本文件是 Phase 2 Design 的输出，对应 [foundation_2026.md](foundation_2026.md) §五 + [entry_form_research_2026.md](entry_form_research_2026.md) §七 的下一步。
>
> **输入**：foundation v5（13 节 Plan 级证据驱动约束）+ entry_form_research v3（§4.10 12 项必决事项 + §四.3-4.9 各项约束）。
>
> **输出**：在上述 Plan + 调研约束内，给出 N=1 用户语境下的具体 v0 方案——12 项 D1–D12 选择 + 目录结构 + 4 层工作流 + 可证伪性 KPI + 退化路径。
>
> **不输出**（推到 Phase 3 Action）：实施代码 / hooks / 自动化脚本 / GUI 封装实现。

---

## 普通话版 TL;DR

**1 段话**：σ v0 是一个"完全跑在 Cursor + git + markdown 里的 N=1 个人训练系统"——没有浮窗、没有 broker API、没有强制 lockout、没有外部服务依赖。每个交易日早上写一份 if-then 规则（这是唯一硬必经的 P0），平仓后 30 秒填 4 个字段，周末做结构化复盘。AI 只在你打开 Cursor、主动提问时回应；不前台推送、不主动归因、不当朋友。临床自检（PHQ-9 + GAD-7 + 5 项投机交易行为自查 + DSM-5 9 项 + 5 项禁忌症）在入门时跑一次作基线，之后由你自己决定何时重测；任何时候自检触发，系统提示"考虑暂停"，但不强制 lockout（v2 §6.1 N=1 原则）。4 周判定窗后按 KPI 数据决定 σ 是退化（4→2→1）、维持，还是触发退出协议。

**这是一个全新项目**：老的 [decision-chain.md](../decision-chain.md) / [trade-journal-template.md](../trade-journal-template.md) / [tools/position_sizer.py](../tools/position_sizer.py) / [trades/2026/05/](../trades/2026/05/) 都不再被沿用——v0 用调研证据重新设计这一整套，老文件按 §七处置（保留 1 份在 archive/ 作为历史，不再纳入工作流）。

---

## 一、设计语境锁定

### 1.1 N=1 用户语境（已在 entry_form_research v3 §6.1 显式化）

| 维度 | 当前状态 |
|---|---|
| 系统语境 | **N=1 个人训练系统**，**不是** productization 路径 |
| 用户基线 | 临床高风险自评：用户已声明不属极端高风险（v2 §6.1） → 临床自检不作 lockout gate；状态性风险防御保留 |
| 已就位工具栈 | Cursor IDE（用户日常工作环境）+ git + markdown + GitHub 私有 repo |
| 交易市场 | A 股 / 港股 / 期货 |
| 已有交易经验 | 用户已交易期货（MGC 2026-05-04 记录在 [trades/2026/05/](../trades/2026/05/)）|
| 兼容老 Stage 0 工具 | **不需要兼容**（用户 2026-05-06 明确确认）→ v0 是全新设计，老工具按 §七处置 |

### 1.2 Plan/Design 分层（v3 维持）

- **Plan**（foundation v5 + entry_form_research v3）：证据告诉我们"什么必须满足、什么必须禁止"
- **Design**（本文件）：在 Plan 约束内做具体方案选择 + 候选对比
- **Action**（Phase 3，不在本范围）：拆若干独立小 PR 真实施

### 1.3 本设计的方法学定位

本设计是**N=1 工程组合假设**——12 项决策每个组件单独有 S/M 级证据（详见 §二），但**整体组合在 N=1 交易场景**没 RCT 验证。这与 [foundation_2026.md §四.2](foundation_2026.md) 隐含假设盲区 #4 "12 组件拼盘 1+1>1 在交易领域无 RCT" 一致——本系统应作为**个人级 N-of-1 实验**对待，而非"已验证产品"。

---

## 二、12 项必决事项 — 推荐选择 + 证据 + 退化路径

> 对应 [entry_form_research §4.10](entry_form_research_2026.md) D1–D12。每项给：(a) 推荐选择 + (b) 主证据 + (c) 关键反向证据 + (d) 退化候选。

### D1 入口形态主形式

**推荐 = D（markdown + git）+ B（Cursor 编辑）混合**——入口物理位置在用户已有的 Cursor IDE 工作空间内，介质是仓库内 markdown 文件。

**主证据**：
- §收敛信号 5（中等被审视感）：markdown + git commit 仪式 + 私有 = 接近诚实最优区（Lelkes 2012 + Bateson 2006，S 级综合）
- §四.5 ROI：早晨规则书写工程成本 0–5 工时（vs 浮窗 80–160 工时）
- 用户已在 Cursor 工作 → 零迁移成本（避开 §收敛信号 6"必经之路"的反向激励）

**关键反向证据**：
- Perez De Rosso & Jackson 2016 OOPSLA（S 级）：git CLI 对小白是天书 → **必须 GUI 封装**
- 缓解：用户当前已是 git/Cursor 用户 → 该反向证据对本 N=1 不适用（productization 时仍适用）

**退化候选**：若 4 周内 Cursor 内编辑摩擦过大，退化到 D 单独（任意编辑器 + 手动 git commit）。

### D2 AI 角色

**推荐 = B（后台静默分析）+ C（前台对话仅在用户主动调用且独立思考后）混合**——禁前台主动推送，禁拟人化"朋友/伙伴"措辞。

**主证据**：
- foundation §三.2（v5 反馈组件角色约束 9 条）+ §收敛信号 3（高风险用户必须 default No-AI）
- §一调研 9 矩阵：前台 AI 在 4/6 维度反向（认知卸载 / 用户主动思考 / 临床安全 / 实施成本）
- Liu 2026 N=1222 三组 RCT（S 级）：**取 hint 不取答案的人与对照组无显著差异**——支持"AI 仅当 hint 给出"的受限前台
- Bastani 2024 PNAS（S 级）：撤掉 AI 后 GPT Base 学生比从未用过的差 17%——支持"不让 AI 主动归因"

**关键反向证据**：
- Hodge 2023（S 级）：拟人化 robo-advisor 恶化处置效应 → **AI 措辞必须形式化，禁"朋友/伙伴"**
- Sharma 2023 + Cheng 2025 ELEPHANT（S 级）：默认 LLM 谄媚直接伤害决策质量 → **AI prompt 必须显式禁 sycophancy**

**退化候选**：若 4 周内发现 AI 即使受限调用也产生认知卸载（用户停止独立思考），退化到 A（完全无 AI）—— v2 §6.1 N=1 用户路径明确支持这一退化。

**N=1 用户当前判定**：用户已声明不属临床高风险 + 偏好"按推荐来"且重视证据来源 → 保留 B+C 受限 AI 是合理初始；不强制 default No-AI（productization 时强制）。

### D3 数据介质

**推荐 = A（markdown + git）**——本仓库已有结构（trades/YYYY/MM/，knowledge/，research/，memory/），v0 沿用并扩展。

**主证据**：
- notes/08 §3.3 综合（U 级）：markdown + git GUI 封装 = 中等被审视感的可行结构（前提：GUI 封装到位）
- §收敛信号 5：完全私密（敷衍）/ 完全公开（chilling effect）/ 中间（reputation concern 激活诚实）—— git commit 仪式 + 私有 + AI 周期性透明读 ≈ 中间
- 用户当前已在用 git → 零迁移成本

**关键反向证据**：
- notes/08 v2 caveat 4 项（S/M/W）：(a) git 力推/篡改仍可能；(b) GUI 封装是被低估 1 个数量级的工程承诺；(c) AI 周读 vs 本地优先矛盾；(d) 任何中间格式必须可被独立工具读懂——所有这些对 productization 路径都成立，但**对 N=1 用户当前已是 git 使用者的情况，前 3 项已被既有工作流吸收**；(d) markdown 本身满足"独立工具可读"

**退化候选**：若 4 周内仓库结构变得过于复杂（>20 个 markdown 文件 N=1 用户难以维护），退化到 SQLite 本地（B）—— 但 v0 不预先做这个工程投入。

### D4 端策略

**推荐 = B（单端 Cursor 桌面）**——不上 Web、不上 Mobile、不上多端。

**主证据**：
- §收敛信号 2（S 级跨多源）：Mobile 不作主入口（NBER w28363 + SSRN 4852148 + FCA 66）
- notes/10（S 级）：Heron 2017 元分析多端不优于单端依从（p=.36）；Jiang 2025 4 臂 RCT 决定因素是"该端的设计"而非"端的数量"
- notes/10 §3.3（S/M/W 三层一致）：多端同步是工程已知的数据完整性故障模式（Last-write-wins 76% vs CRDT 99.7%）

**关键反向证据**：
- 用户在出差 / 旅行场景 Cursor 不可用时无替代——但这属于 missed-day 范围（详见 §四.5）

**退化候选**：若 4 周内出差场景频繁（>30% 交易日不在桌面），退化路径是用手机原生 Notes / 微信文件传输 → 桌面 Cursor 同步 markdown。**不引入 Mobile App**（§收敛信号 2 反向证据）。

### D5 物理位置组合

**推荐 = A（三位置 + 异步深度，但优先级递降）**：

| 层 | 优先级 | A 股语境调整 |
|---|---|---|
| 盘前规则书写 | **P0**（必经路径，唯一不可砍）| 9:00–9:15 完成 → 9:15-9:25 集合竞价（§四.7.1 binding）|
| 盘后即时记录 | **P0**（4 字段 EMA）| 平仓后 30 分钟内（A 股 T+1 紧迫性低于美股，但仍保留即时性）|
| 盘中拦截 binding | **P1**（A 股市场制度天然提供）| 9:20 集合竞价 + T+1 + 涨跌停板，三选一即可（§四.7）|
| 周/月异步深度 | **P1** | 周末 30 分钟 + 月末 1 小时 |
| 盘中浮窗 | **P2 不做** | §四.5 ROI 数量级最低 + 工程成本 80–160 工时 |

**主证据**：
- §收敛信号 1（U 级，由 4 个独立调研收敛）：σ 入口是按时刻分层组合
- §四.5 工程 ROI：早晨规则书写比浮窗高 1–2 个数量级
- §四.7 A 股市场制度：9:20 集合竞价 + T+1 + 涨跌停 = 美股没有的天然 binding device

**关键反向证据**：
- R01-HCI 问题 4 + R02-mHealth §8.2：4 层组合不可证伪 → **必须有 §四.3 可证伪性 KPI + §四.9 退化路径**
- 缓解：详见 §四（KPI）+ §三.5（退化路径具体化）

**退化候选**：详见 §四.5 退化路径表（4→3→2→1，L1 仅保留盘前规则书写）。

### D6 成交记录获取方式

**推荐 = C（手动复盘）+ D（周批量对账）混合**——A 股零售无 broker API（§四.6），不投入 OCR / API 工程预算。

**主证据**：
- §四.6 4 候选评估：A 股零售券商基本不开放 broker API（M 级，多源一致）；OCR 极脆弱
- §收敛信号 4（S 级）：事后回忆系统性漏掉最危险的冲动交易 —— **D 周批量对账正是为缓解此问题**

**关键反向证据**：
- D 路径"对账发现 C 漏掉的冲动交易"是 U 级假设——若用户连 D 都不做，σ 实际仍只看到"愿意被记录的交易"
- 缓解：D 周批量纳入 P1 周复盘工作流（§三.4），与异步深度复盘合并

**退化候选**：若用户 4 周内周批量对账完成率 < 30%，退化到仅 C（接受"σ 是当日复盘系统 + 已知盲区"的形态定位）。

### D7 A 股市场制度 binding 利用

**推荐 = (i) 9:20 集合竞价 + (ii) T+1 + (iii) 涨跌停板 三项全用**——这是 A 股版 σ 优于美股版的结构性优势（§四.7）。

**具体落地**：

1. **9:20 不可撤单作为 implementation intention 的执行式具象化**（§四.7.1）：
   - 9:00–9:15：用户在 σ 系统写当日 if-then（盘前规则 P0）
   - 9:15–9:20：在 σ 系统打开盘前规则文件 → 强制复述"我今天能且仅能在 X 价位下 Y 大小的单"
   - 9:20–9:25：已下集合竞价单**法律意义上不可撤**——制度硬承诺
2. **T+1 放大早晨规则的影响半径**（§四.7.2）：盘前规则书写时显式用第一人称 identity 表述（BCT 13.x，§四.4.1），强化"今早的我"对一整天 + 一整夜的承诺
3. **涨跌停板作为 hot state 触发器**（§四.7.3）：盘前规则书写必含"今日如果碰到涨跌停板，我的预设动作是 X"——把 hot state 决策提前到 cold state；v0 不实现自动触发（属盘中浮窗 P2）

**主证据**：
- Patterson 2020 Cornell RCT（S 级）：commitment device +24% 学习时间——σ 直接利用市场制度而非自建 device
- §四.7 三个市场制度的强度对比 + 行为含义

**关键反向证据**：
- 9:20 强制复述的具体形态需 N=1 实测——是显示 prompt？是手动 checkbox？是自动 git diff？
- 缓解：v0 选最简——9:20 前用户在 σ 系统打开盘前规则文件即视为复述完成（信任 + 中等被审视感）

### D8 可证伪性 KPI（§四.3 落地）

**推荐 = §四.3 KPI 候选清单全采纳，4 周节点判定**：

| 层 | KPI | 4 周阈值 |
|---|---|---|
| P0 盘前规则书写 | 当日是否写下 if-then | ≥ 80% 交易日完成 |
| P0 盘后 30 秒 EMA | 平仓后 30 分钟内 ≤4 字段 | ≥ 70% 交易完成 |
| P0 决策链 5 问完整率 | 开仓前 5 问全部诚实回答 | ≥ 90% 交易 |
| P1 周复盘 | 周末 30 分钟内完成模板 | ≥ 50% 周次 |
| P1 月校准 | 月末完成"事前预设 vs 实际"对照 | ≥ 1 次/月 |
| P1 盘中 binding（A 股 9:20）| 9:20 前提交集合竞价单 / 守住涨跌停规则 | 当日有效 ≥ 70% |

**整体退化触发**（§四.3）：
- 4 周 P0 完成率均 < 50% → 4→2 退化
- 8 周 P0 < 50% → 4→1 退化
- 12 周仍 < 50% → 触发 v5 §三.6 退出协议

**主证据**：
- §四.3（U 级整体 + 各组件 S/M）：mHealth 30 日留存基线 + Pratap 2020 + AppsFlyer 2024
- v5 §四.2 隐含假设盲区 #6：动态预警（贝叶斯 / SPC）+ 硬性统计门槛双机制

**诚实标记**：80%/70%/90%/50% 是 U 级初始假设，无 RCT 校准。**4 周后必须根据 N=1 实测调整**——这是 v3 §四.3 的硬约束。

### D9 BCT 维度（§四.4 落地）

**推荐 = 三项全采纳**：

1. **Identity change（BCT 13.x）—— §四.4.1**：
   - 盘前规则用第一人称 identity 表述："我作为系统化交易者，今天的执行约束是 X"——而非"我应该 X"
   - 周复盘 honesty oath 含 identity 维度："这周我作为系统化交易者，是否符合自己的标准"
2. **Behavioral substitution（BCT 8.2）—— §四.4.2**：
   - 盘中冲动想下单时的替代行为清单（盘前规则书写时预设）：
     - 写一段补充规则到当日 if-then
     - 起身离开屏幕 5 分钟
     - 再读一遍当日 if-then
3. **Environmental restructuring（BCT 12.x）—— §四.4.3**：
   - onboarding 必含"top 3 cue 源"对话（用户列出冲动种子位置）
   - 盘前规则书写显式列出"今日不接受的 cue 源"——R05-China "微信群拍单"作为 if-then 排除项

**主证据**：
- Michie 2013 BCTTv1 三组（M 级）+ Steenbarger / Kiev / Oyserman identity-based motivation（S/M）
- R02-mHealth §3.2 三组缺席的 audit + §收敛信号 6 用户预先承诺 + 必经之路

### D10 v0 工程优先级

**推荐 = §四.5 ROI + §四.8 R03-Engineer 路径，但用 Cursor 替代 Obsidian**：

| 层 | 工程实现 | 工时估算（业余）|
|---|---|---|
| 盘前规则书写（P0）| markdown 模板 + 系统通知 + Cursor 内编辑 | 0–5 工时（已有 Cursor，零迁移）|
| 盘后 30 秒 EMA（P0）| markdown daily note 模板 + ≤4 字段 | 2–4 工时 |
| 周月异步深度（P1）| markdown 模板 + git commit | 2–4 工时（已有 git）|
| 盘中 binding（P1）| 不实现自动触发；纳入盘前规则书写 | 0 工时（市场制度天然提供）|
| **v0 总开发** | | **~5–15 工时** |
| **v0 总占用（含 4 周自测）**| | **~30–60 工时** |

**与 R03-Engineer 推荐的差异**：
- R03 推 Obsidian + 4 模板，估 ~25–50 工时开发——是因为他假设全新引入 Obsidian + Git plugin
- 本设计推 Cursor + git（已就位），估 ~5–15 工时——节省 ~20 工时的"工具搭建"成本
- 4 模板设计 + 自测占用估算与 R03 一致

**v0 故意不做**（§四.8 同款）：
- 盘中浮窗 / 自动 broker 集成 / 多端同步 / 精细审计 / GPG 签名

### D11 退化路径

**推荐 = §四.9 落地（4 → 3 → 2 → 1 → 0）**：

| 级别 | 保留的层 | 触发条件 |
|---|---|---|
| L4 完整版 | 盘前 + 盘中 binding + 盘后 EMA + 周月 | 默认起点 |
| L3 缩减版 | 盘前 + 盘后 EMA + 周月（砍盘中 binding 的"自动触发"——手动保留）| 9:20 binding 4 周完成率 < 50% / 用户出差比例高 |
| L2 简化版 | 盘前 + 月校准（砍盘中 + 盘后 EMA + 周复盘）| 盘后 EMA 4 周 < 50% |
| **L1 最简版** | **仅盘前规则书写** | P0 整体 4 周 < 50% |
| L0 退出协议 | 触发 v5 §三.6 退出协议（4 类分叉输出）| 12 周仍 < 50% / 心理痛苦自评 ≥ 7 / 临床自检触发 |

**Missed-day recovery**（§四.9）：
- 早晨没写规则的当日 → **当日不交易**（binding pre-commitment 逻辑直接推论）
- 周末 / 出差 → 提前一天用"模板规则"占位（"周末仅做被动持仓 review，不开新仓"）
- 连续 3 天未写规则 → 系统提示"考虑暂停 1 周复盘"——不强制 lockout

**主证据**：见 §四.9 五条理由（工程成本最低 + 效应最强 + 覆盖最危险失败模式 + A 股市场制度配合 + identity 兼容）。

### D12 临床安全 N=1 自检模板

**推荐 = 完整 §六.2/6.3/6.4/6.5/6.6 落地为单文件 [knowledge/clinical_self_check.md](../knowledge/clinical_self_check.md)**：

包含：
- PHQ-9（含自杀题第 9）
- GAD-7
- 5 项投机交易行为自查（v3 §6.6 A 股本地化措辞——避免"赌博"用语）
- DSM-5 problem gambling 9 项（v3 §6.3 完整版，含 #5 痛苦驱动型交易 = σ 系统最危险的过渡机制）
- 5 项简化绝对禁忌症（v3 §6.5）
- 中国大陆心理援助资源最小指针（v3 §6.4）
- 使用说明：基线一次 + 用户决定何时重测；**不 lockout**；任一触发 → 系统提示"考虑暂停"

**主证据**：详见 v3 §六.1–6.6 N=1 vs productization 临床安全分级。

**N=1 关键约束**（v2 §6.1）：
1. 自检不作 lockout gate
2. 用户自决何时重测
3. **状态性风险防御保留**：连续亏损 + 睡眠剥夺 + 重大生活事件不依赖特质风险等级
4. 诚实措辞调整对所有语境适用："这条记录是否足够可检验"——审查记录质量不审判人格

---

## 三、v0 σ 系统具体方案（基于二的合并）

### 3.1 目录结构（彻底重构，不兼容旧 Stage 0）

```
/workspace/
├── CLAUDE.md                           ← 项目上下文（保留）
├── system_spec_v2.md                    ← 系统规范文档（保留为历史档案，不再权威）
├── README.md                            ← v0 σ 操作手册（v0 新建）
│
├── sigma/                               ← v0 σ 系统主目录（v0 新建）
│   ├── pre-market.md                   ← 盘前规则模板（每日复制为 daily 文件）
│   ├── post-trade-ema.md               ← 盘后 30 秒 EMA 模板（≤4 字段）
│   ├── decision-chain.md                ← 决策链（v0 重写——if-then 形式 + identity）
│   ├── weekly-review.md                ← 周复盘模板
│   ├── monthly-calibration.md          ← 月校准模板
│   └── daily/                           ← 每日 if-then 实例（YYYY-MM-DD-pre.md）
│       └── 2026-MM/
│
├── trades/                              ← 交易记录（v0 重构格式）
│   └── YYYY/MM/                         ← 每月归档
│       └── YYYY-MM-DD-<symbol>-<dir>.md ← 每笔交易（盘前 if-then + 决策链 + 盘后 EMA + 异步复盘 一文聚合）
│
├── reviews/                             ← 周月复盘归档（v0 新建）
│   ├── weekly/YYYY-WW.md
│   └── monthly/YYYY-MM.md
│
├── knowledge/                           ← 知识库（保留 + 增强）
│   ├── meta-rule.md                    ← 保留
│   ├── glossary.md                      ← 保留（v0 后再扩）
│   ├── risk_rules.md                    ← 保留（Level B sync 推到 Phase 3）
│   ├── INDEX.md                         ← 保留 + sync
│   └── clinical_self_check.md          ← v0 新建（D12）
│
├── memory/                              ← 项目专属记忆（保留）
│   ├── trader-profile.md
│   ├── bias-patterns.md
│   └── stage.md                         ← v0 重新对齐
│
├── research/                            ← 调研档案（保留为历史）
│   ├── foundation_2026.md              ← Plan 宪法
│   ├── entry_form_research_2026.md      ← Plan→Design 桥梁
│   ├── design_proposal_2026.md         ← 本文件
│   ├── notes/                           ← 12 篇调研
│   ├── review_prompts/                  ← Phase 1 review prompts
│   ├── review_prompts_phase2/           ← Phase 2 review prompts
│   └── pr_*_review_*.md                 ← 已合 first-pass review
│
├── archive/                             ← 历史档案（保留 + 增加旧 Stage 0 工具）
│   ├── audit_report.md
│   ├── audit_report_v2.md
│   ├── system_design.md
│   ├── README.md
│   ├── MR_20260503_audit_fixes.md
│   └── deprecated_stage0/              ← v0 新建：deprecated 旧 Stage 0 工具
│       ├── decision-chain.md            ← 旧版（移自根目录）
│       ├── trade-journal-template.md    ← 旧版（移自根目录）
│       ├── tools/position_sizer.py      ← 旧版（移自 tools/）
│       └── DEPRECATION_NOTES.md         ← 说明为什么 deprecate + 新版位置
│
└── .cursor/rules/                       ← Cursor 规则（保留）
```

### 3.2 工作流（4 层 + AI 角色）

```
每个交易日：
  ┌─ 盘前 (8:30-9:15) ───────────────────────────────────────┐
  │ 1. 在 sigma/daily/YYYY-MM/YYYY-MM-DD-pre.md 写 if-then 规则
  │    - 第一人称 identity 表述（BCT 13.x）
  │    - 列今日不接受的 cue 源（BCT 12.3）
  │    - 列今日冲动替代行为（BCT 8.2）
  │    - 列今日如果碰涨跌停板的预设动作
  │ 2. git add + commit "pre YYYY-MM-DD"
  │ 3. 9:15-9:20 在 Cursor 打开当日 pre 文件 → 强制复述（§四.7.1）
  └─ 9:20 集合竞价不可撤单 = 制度硬承诺 ──────────────────────┘

  ┌─ 开仓时 ────────────────────────────────────────────────┐
  │ 1. 在 trades/YYYY/MM/ 新建 YYYY-MM-DD-<symbol>-<dir>.md
  │ 2. 走决策链 5 问（sigma/decision-chain.md if-then 形式）
  │ 3. git add + commit "open <symbol>"
  │ 4. 实际下单
  └────────────────────────────────────────────────────────┘

  ┌─ 平仓后 30 分钟内 ──────────────────────────────────────┐
  │ 1. 在同一交易文件填盘后 EMA（≤4 字段）
  │ 2. git add + commit "close <symbol>"
  └────────────────────────────────────────────────────────┘

每周末（30 分钟）：
  ┌─ 周复盘 ────────────────────────────────────────────────┐
  │ 1. 复制 sigma/weekly-review.md 到 reviews/weekly/YYYY-WW.md
  │ 2. 三段式：事前预设 → 实际发生 → 偏差（v5 §三.8）
  │ 3. 周批量对账：从券商 App 导出 CSV → 与 trades/ 对账
  │ 4. git add + commit "weekly YYYY-WW"
  └────────────────────────────────────────────────────────┘

每月末（1 小时）：
  ┌─ 月校准 ────────────────────────────────────────────────┐
  │ 1. 复制 sigma/monthly-calibration.md
  │ 2. KPI 跑 §四 6 个 KPI 表
  │ 3. 决策链准确率（预估胜率 vs 实际胜率，4 周累计）
  │ 4. 是否触发 §四.5 退化路径？
  │ 5. 是否触发 v5 §三.6 退出协议？
  │ 6. git add + commit "monthly YYYY-MM"
  └────────────────────────────────────────────────────────┘

AI 角色（D2 落地）：
  - 后台静默：用户主动提"读一下我这周的复盘" / "看一下决策链遵守率" → AI 读 git log + 文件回应
  - 前台对话：用户主动提问 + 已独立写下答案后 → AI 给 hint 不给答案
  - 禁前台主动推送 / 禁拟人化 / 禁主动归因 / 禁 sycophancy
```

### 3.3 决策链（v0 重写为 if-then 形式 + identity）

> **v0 改动**：旧 [decision-chain.md](../decision-chain.md) Q1–Q5 是开放式问题（What/Why 主导）；v0 改为 if-then 形式（implementation intention，d=.27-.66 跨域元分析，foundation §三.6 调研 6）+ identity 第一人称（BCT 13.x）。

新决策链（写入 [sigma/decision-chain.md](../sigma/decision-chain.md)）骨架：

```
作为系统化交易者，本笔交易的 5 项 if-then 承诺：

If 1（论据）: 我做这笔交易的论据是 [X]，证据等级 [S/M/W/U]，置信度 [1-5]。
              如果论据等级 < W，则取消。

If 2（止损）: 我的入场理由被推翻的条件是 [Y]，对应价格 [P_stop]。
              如果到达 [P_stop]，则平仓——不重新评估、不延长止损。

If 3（仓位）: 这笔钱全亏损对我的影响是 [Z]。
              如果 Z 超过"我能完全输掉的学费"，则缩小仓位至 ≤ 学费阈值。

If 4（情绪）: 我现在的情绪状态是 [E]，强度 [1-5]。
              如果 E ∈ {兴奋, 愤怒, 报复, 翻本}，则不开仓——盘前规则已经
              预设这种情况下不交易（BCT 8.2 替代行为）。

If 5（期望值）: 这类交易 10 笔我预期 [n] 笔赚钱、平均赚 [G]、平均亏 [L]。
                EV = n×G − (10−n)×L
                如果 EV ≤ 0 或我答不出来，则不开仓。
                Q5a 估计来源：[过去类似数据 / 回测 / 直觉 / 别人]——
                如果是"直觉/别人"，则把仓位减半。
```

**禁开放式 Why 问题**（v5 §三.4 + Watkins & Teasdale 2004）；**仅在事后复盘允许 Why**。

### 3.4 临床自检（D12）

详见 [knowledge/clinical_self_check.md](../knowledge/clinical_self_check.md) 落地（本设计的伴生文件）。

入门基线：用户 v0 启动时跑一次（约 5-10 分钟）+ 把结果存到 `memory/clinical_baseline.md`（不公开 commit；放在 `.gitignore` 边界——**v0 默认 commit**，因为是 N=1 个人系统 + 已经是私有 repo；productization 时改）。

---

## 四、可证伪性 KPI（每层 N=1 + 4 周）

### 4.1 P0 KPI 表（必须达标）

| KPI | 4 周阈值 | 计算方法 |
|---|---|---|
| 盘前规则书写完成率 | ≥ 80% 交易日 | count(daily/YYYY-MM/) / 交易日数 |
| 盘后 EMA 完成率 | ≥ 70% 已平仓交易 | count(已填 EMA 字段) / count(已平仓交易) |
| 决策链 5 问完整率 | ≥ 90% 开仓 | count(5 问全填) / count(已开仓) |

### 4.2 P1 KPI 表（监测但不强制）

| KPI | 4 周阈值 | 计算方法 |
|---|---|---|
| 周复盘完成率 | ≥ 50% 周次 | count(reviews/weekly/) / 周次数 |
| 月校准完成率 | ≥ 1 次/月 | count(reviews/monthly/) ≥ 1 |
| 9:20 集合竞价 binding 利用率 | ≥ 70% A 股交易日 | count(9:20 前完成复述) / A 股交易日数 |

### 4.3 校准 KPI（每月 1 次）

| KPI | 4 周阈值 | 计算方法 |
|---|---|---|
| 决策链预估准确率 | 偏差 < 10 个百分点 | abs(平均预估胜率 − 实际胜率) |
| 仓位偏差（实际 vs 凯利建议）| 缩小中 | trend(abs(实际仓位 − 凯利建议) / 凯利建议) |
| 止损遵守率 | ≥ 95% | count(止损触发后已平仓) / count(止损触发) |

### 4.4 整体退化触发（§四.3 + §四.9）

```
4 周节点判定：
  P0 完成率均 ≥ 80%/70%/90% → 维持 L4
  P0 任一 < 50%               → 4→2 (L2)
  
8 周节点判定：
  P0 完成率仍均 < 50%         → 4→1 (L1，仅盘前规则书写)

12 周节点判定：
  仍 < 50% / 心理痛苦自评 ≥ 7  → 触发 v5 §三.6 退出协议
```

### 4.5 退化路径（§四.9 落地）

详见 §二 D11 表 + §四.4 触发条件。

**关键 invariant**：L1 最简版**保留早晨规则书写**——这是 §四.5 ROI 推论 + §收敛信号 4+6 + Patterson 2020 的合成结论。

---

## 五、退出协议（v5 §三.6 落地到 N=1）

### 5.1 数据触发的退出（v5 §三.6 4 类分叉）

| 触发情境 | v0 输出 |
|---|---|
| 决策链遵守率连续 3 月 < 50%（执行问题）| **降低频率 / 降低杠杆 / 缩小训练资金**——重新建立硬约束 |
| 单一 setup 失效（连续 20 笔 EV < 0）| **暂停当前 setup / 换一个证据更强的 setup** |
| 整体 edge 持续未显现（跑输被动基准 6 月+ 净值） | **转入被动基线 + 训练资金归零或极小化** |
| 心理安全触发 | **完全暂停训练系统使用**——优先恢复健康 |
| Level 2 红灯连续 2 次 | **暂停 4 周 + 全面复盘 + 与外部审查者讨论** |

### 5.2 临床触发的退出（v3 §6.1/6.3/6.5）

任一触发 → 系统提示"考虑暂停"——**不强制 lockout（v2 §6.1 N=1 原则）**：
- PHQ-9 任一题阳性 / 总分骤升 ≥ 5
- GAD-7 总分 ≥ 15（severe）
- DSM-5 9 项任 4 项触发（临床诊断阈值）
- DSM-5 #5（痛苦驱动型交易）单独触发 = σ 系统最危险过渡机制
- 5 项简化禁忌症任一触发

### 5.3 状态性风险触发（v3 §6.1 #3）

不依赖特质风险等级 —— 即便用户自评不在极端高风险，以下状态性条件仍触发"考虑暂停"提示：
- 连续亏损 + 睡眠剥夺
- 重大生活事件（搬家 / 失业 / 关系危机 / 健康事件）
- 心理痛苦自评 ≥ 7/10

### 5.4 退出后的 6 月重启评估

**核心原则**（v5 §三.6）：退出 ≠ 永久放弃。

- 6 个月后可在被动基线安全基础上**重启训练评估**
- 重启前置条件：心理安全条件满足 + 重启时承诺重新进入完整决策链 + 至少 1 次月校准 + 1 次外部 review（可以是 AI 也可以是 peer）

---

## 六、与 foundation v5 + entry_form_research v3 的相容性核查

| Plan 约束 | v0 设计落地 | 相容性 |
|---|---|---|
| foundation §三.1 4 层目标结构 | 训练资金独立 + 长期财富走被动（§五）| ✅ |
| foundation §三.2 反馈组件角色约束（9 条）| §二 D2 AI 角色边界（B+C 受限 + 禁拟人化 / 谄媚 / 主动归因）| ✅ |
| foundation §三.3 binding pre-commitment | §三.2 工作流 + §二 D7 A 股市场制度三项 binding | ✅ 强化 |
| foundation §三.4 三个动作（记录/监测/复盘）| §三.1 目录结构（sigma/ 决策链记录 + 4 KPI 监测 + reviews/ 复盘）| ✅ |
| foundation §三.5 样本量诚实 | §四 KPI 表 + 月校准（< 50 笔标 U 级）| ✅ |
| foundation §三.6 退出协议（4 类分叉）| §五.1–5.4 完整落地 | ✅ |
| foundation §三.7 训练资金 vs 长期财富分离 | §五.1 转入被动基线选项（明确） | ✅ |
| foundation §三.8 复盘工具约束（含打破私密通道）| §三.2 weekly + monthly 模板 + git commit + AI 周读| ✅ |
| foundation §三.9 渐进披露 + 通知限制 | §二 D2 禁前台主动推送 + onboarding 仅必经层 | ✅ |
| foundation §三.10 产品过滤器 | 由 [knowledge/risk_rules.md](../knowledge/risk_rules.md) 承载（保留）| ✅ 沿用 |
| foundation §三.11 临床安全（productization 路径）| §二 D12 + clinical_self_check.md（v3 §6 N=1 分级，自检不 lockout）| ✅ N=1 分层 |
| foundation §三.12 黑天鹅锁仓 | 由 risk_rules.md 承载（保留）| ✅ 沿用 |
| foundation §三.13 字段数上限 / 不预设技术栈 | §三.3 决策链 5 问 + 盘后 EMA ≤4 字段 + 周月模板字段 ≤ 8 | ✅ |
| Mental Accounting caveat | 训练资金独立账户（用户已实践——MGC 期货是学费账户）| ✅ |
| **entry_form_research v3 §四.3 可证伪性** | §四 KPI 表 + 退化触发 + 12 周退出 | ✅ 强化 |
| v3 §四.4 BCT 三组 | §二 D9 三项落地 | ✅ |
| v3 §四.5 早晨规则 ROI | §二 D10 工程优先级（盘前 P0 / 浮窗 P2 不做）| ✅ |
| v3 §四.6 成交记录 4 候选 | §二 D6 C+D 混合 | ✅ |
| v3 §四.7 A 股市场制度 binding | §二 D7 三项全用 | ✅ |
| v3 §四.8 v0 工程参考方案 | §二 D10 + §三.1 目录结构（Cursor 替代 Obsidian）| ✅ 调整 |
| v3 §四.9 退化路径 | §二 D11 + §四.4-4.5 | ✅ |
| v3 §4.10 12 项必决事项 | §二 D1–D12 全部给出推荐 | ✅ |
| v3 §六 临床安全分级 N=1 | §二 D12 + clinical_self_check.md | ✅ |

**结论**：v0 设计与 foundation v5 + entry_form_research v3 全部约束相容；6+ 项形成强化（不冲突）。

---

## 七、老 Stage 0 工具的处置（用户 2026-05-06 明确不需兼容）

> **触发动因**：用户 2026-05-06 明确"stage0 这些都可以动，都可以扔了，老的项目完全不要考虑，不用考虑兼容，这一个彻彻底底的全新的项目"。
>
> **处置原则**：
> - **保留为历史档案**（移到 [archive/deprecated_stage0/](../archive/deprecated_stage0/)）：保证可回溯，但不再纳入工作流
> - **不在 v0 主路径上**：根目录 / tools/ / trades/ 都不再使用旧版
> - **重写而非扩展**：v0 决策链 / 交易日志 / 仓位计算器全部按 §三.3 的 if-then + identity 范式重写

### 7.1 处置清单

| 旧文件 | 处置 | 理由 |
|---|---|---|
| [decision-chain.md](../decision-chain.md)（根目录）| **移到 archive/deprecated_stage0/** | 旧版是开放式 Q1-Q5（What/Why 主导），与 v3 §四.4 BCT identity + foundation §三.4 if-then 范式不一致。v0 在 sigma/decision-chain.md 重写。|
| [trade-journal-template.md](../trade-journal-template.md)（根目录）| **移到 archive/deprecated_stage0/** | 旧版是单文件模板；v0 在 trades/YYYY/MM/<single>.md 一文聚合（盘前 if-then + 决策链 + 盘后 EMA + 异步复盘）+ sigma/post-trade-ema.md 提供 EMA 模板。|
| [tools/position_sizer.py](../tools/position_sizer.py)| **移到 archive/deprecated_stage0/tools/** | 工具本身实现没问题（半 Kelly），但作为独立 Python 脚本不在 v0 工作流中——v0 把仓位计算嵌入决策链 If 5（期望值 + Q5a 来源校验）。Phase 3 Action 时可重新引入或封装到 git hook。|
| [trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md)| **保留在 trades/2026/05/**（用户已记录的真实交易）| 这是真实交易记录，不是模板/工具——保留。但格式与 v0 新模板不完全一致——v0 启动后用户自行决定是否回填新格式（不强制）。|
| [system_spec_v2.md](../system_spec_v2.md)（根目录）| **保留为历史档案**（不移动）| 是项目最早的规范文档；v0 后已被 foundation v5（Plan 宪法）+ entry_form_research v3（调研）+ 本文件（Design）三层取代。在文件顶部加一句说明指向新文档。|
| [archive/](../archive/) 现有内容（audit_report v1/v2 / system_design.md 等）| 不动 | 历史档案，已分类。|

### 7.2 archive/deprecated_stage0/DEPRECATION_NOTES.md（v0 新建）

内容骨架：

```
# Stage 0 工具 deprecation 说明（2026-05-06）

## 背景
- 项目原计划经历 Stage -1 → Stage 0 → Stage 1+ 渐进搭建
- Phase 1 + Phase 2 调研（2026-05-05）发现：
  - 旧 Stage 0 决策链是开放式 Q1-Q5，与 implementation intention 文献的 if-then 范式不一致
  - 旧 trade-journal-template 与 v3 §四.4 BCT identity 维度不兼容
  - 旧 position_sizer.py 是独立脚本，未嵌入决策链工作流
- 用户 2026-05-06 明确"老项目完全不要考虑，不用考虑兼容"

## 处置
本目录下的文件都已被 v0 σ 系统（详见 research/design_proposal_2026.md）取代。
保留这些文件仅作历史回溯；任何新交易请使用 v0 工作流（sigma/ + trades/）。

## 新版本位置
- 决策链：sigma/decision-chain.md
- 交易日志：trades/YYYY/MM/<single>.md（一文聚合）+ sigma/post-trade-ema.md
- 仓位计算：嵌入决策链 If 5（不再独立脚本）
```

### 7.3 关于已记录交易的处置

[trades/2026/05/2026-05-04-mgc-202606-long.md](../trades/2026/05/2026-05-04-mgc-202606-long.md) 是用户已记录的真实交易——**保留不动**。v0 启动后：
- 用户可选择把这笔交易按 v0 新格式回填（不强制）
- 或者就当作 v0 之前的"历史交易"——v0 KPI 计算从 v0 启动日开始，不回溯

---

## 八、Phase 3 Action 不承诺的事项

> Phase 2 Design 仅给"设计"——具体实施由 Phase 3 Action 独立 PR 负责。

### 8.1 不在 Phase 2 Design 范围

- v0 sigma/ 目录的实际模板内容（pre-market.md / post-trade-ema.md / decision-chain.md / weekly-review.md / monthly-calibration.md 5 个模板的逐字段写作）
- archive/deprecated_stage0/ 的实际文件移动操作
- knowledge/clinical_self_check.md 的具体内容（**例外**：本 PR 同时新建该文件，因为它是 D12 的伴生交付）
- KPI 计算的实际工具（Python / shell 脚本 / Cursor 内 prompt）
- AI 后台读 git log 的具体 prompt 模板
- 周批量对账的具体 CSV 格式
- system_spec_v2.md 顶部的"已被取代"说明

### 8.2 Phase 3 拆 PR 计划（建议骨架）

```
Phase 3 Action（独立小 PR，每个 ≤ 200 行）:
  PR-1: archive/deprecated_stage0/ 文件移动 + DEPRECATION_NOTES.md
  PR-2: sigma/ 5 个模板（pre-market / post-trade-ema / decision-chain / weekly / monthly）
  PR-3: trades/ 新格式 README + 1 个示例文件
  PR-4: reviews/ 目录初始化 + README
  PR-5: knowledge/risk_rules.md 加产品过滤器 + 临床触发 + 黑天鹅章节（Level B sync）
  PR-6: knowledge/glossary.md 加 v3 + foundation v5 新术语（Level B sync）
  PR-7: AI 后台读 git log 的 prompt 模板（在 .cursor/rules/ 或 sigma/ai-roles.md）
  PR-8: KPI 计算工具（最简版：单 shell / Python 脚本统计 git log + 文件存在性）
```

每个 PR 独立可 merge / 可回滚；用户接受 v0 启动条件 = PR-1 + PR-2 + PR-3 + PR-4（最小可用集）。

---

## 九、本设计的局限与未覆盖

### 9.1 整体诚实标记（U 级）

本 Design 是 N=1 工程组合假设——12 项决策每个组件单独有 S/M 级证据，但**整体组合在 N=1 交易场景**没 RCT 验证。**应作为个人级 N-of-1 实验对待**，4 周节点必须按数据调整。

### 9.2 已识别但未解决的盲区

1. **AI 后台读 git log 的实施细节** —— D2 推荐 B+C 受限 AI，但"后台静默读 git log → 周回应"的具体 prompt 工程量在 R03-Engineer 估 ~20-40 工时（[pr_3_review_03_engineer_claude_first_pass.md](pr_3_review_03_engineer_claude_first_pass.md) §意见 23）；v0 不投入这个预算 → 实际等于"用户主动调用 + 手动复制最近 commit list 给 AI"。这与 D2 设计意图（"被他人观察"= 中等被审视感）有 gap，但属 §收敛信号 5 GUI 封装局限的延续，不可消除。
2. **Mental Accounting 实施** —— v5 §四.2 隐含假设盲区 #3 + foundation §三.1 4 层结构 caveat：v0 通过"trades/ 命名 + 训练资金独立 broker（用户已实践）"做了符号层标识，但**没有阻止用户把训练资金心智账户重建构为"赌资"**——这条只能靠用户自己每次盘前规则书写中的 identity 表述（§四.4.1）软性维系。
3. **冲动种子在交易工作台之外** —— §收敛信号 6 + R05-China §1.1：σ 在微信生态拦截能力 ≈ 0。v0 通过"盘前规则书写显式列出 cue 排除项"做软性补救，但这是 BCT 12.3 的弱实现——σ 物理上无法拦截微信群拍单。
4. **σ 是"防守"系统，"如何在浮盈时合理加仓"未覆盖** —— foundation §四.2 隐含假设盲区 #5。v0 不在范围内——待 σ 引擎稳定后调研（Phase 4+）。
5. **跨平台一致性** —— v0 锁单端 Cursor 桌面，跨设备 / 出差 / Mobile 场景由 missed-day recovery 协议软性补救（§二 D4 退化候选 + §二 D11 missed-day），但**用户出差比例高时**会显著降低 KPI 完成率——是已识别的退化触发条件。
6. **不可证伪触发的 false positive** —— v5 §四.2 #2：金融数据高噪音，4 周 / 50 笔节点的退化触发可能反映市场 regime 变化而非系统问题。v0 未引入贝叶斯 / SPC 校正（属 Phase 3+ 的 KPI 工具范围）。

### 9.3 未做（按用户当前轮跳过）

- 外部多模型 review（review_prompts_phase2/ 已就位但 Cloud Agent 工具仅 Claude；用户在 v3 已接受同模型偏见 caveat）—— 该限制在 v3 §五.3 + Phase 1 multi-model review 框架中已显式标注

---

## 附：修订记录

| 日期 | 版本 | 修订内容 | 触发动因 |
|---|---|---|---|
| 2026-05-06 | v0 | 初版 Phase 2 Design 收口提案：12 项 D1–D12 推荐选择 + N=1 用户语境 v0 全新设计 + 目录结构（sigma/ + trades/ + reviews/）+ 4 层工作流（盘前 P0 / 盘后 EMA P0 / 周月 P1 / 盘中 binding P1 由 A 股市场制度提供）+ 可证伪 KPI（4 周节点）+ 4→3→2→1 退化路径 + 退出协议落地 + §七 老 Stage 0 工具 deprecation（用户 2026-05-06 明确不兼容）+ §六 与 foundation v5 + entry_form_research v3 全约束相容性核查 | 用户 2026-05-05 "你去完成 phase2，按推荐来"+ 2026-05-06 "stage0 都可以动 / 不用考虑兼容 / 全新项目" → Phase 2 Design 收口提案；伴生交付 [knowledge/clinical_self_check.md](../knowledge/clinical_self_check.md)（D12）|

---

*完成日期：2026-05-06 | 当前版本：v0 | 调研代号：sigma-phase2-design-239d | 上游 Plan：[foundation_2026.md v5](foundation_2026.md) + [entry_form_research_2026.md v3](entry_form_research_2026.md) | 伴生交付：[knowledge/clinical_self_check.md](../knowledge/clinical_self_check.md)*
