# 记录介质（Recording Medium）证据调研

> 调研日期：2026-05-05
> 调研方法：Web 检索（HCI / CHI / Ubicomp、JAMIA / JMIR、PKM / 第二大脑工具用户研究、数字保存图书馆学、个人信息学元论、监管文献）
> 证据等级：S（同行评审）/ M（专业出版 / 监管 / 大规模行业数据）/ W（博客 / 营销 / 用户论坛）/ U（基于已知文献的逻辑推演）
> 上下文：Phase 2 入口形态调研的子任务 2。本笔记**不预设技术栈**——它要解决的元问题是：把"诚实交易日志 + 周复盘 + 决策链"承载在哪种**记录介质**上，对系统的诚实性、留存、可审计、AI 协作、隐私与可移植最优。

---

## ⚠️ 范围声明

- 本笔记**只**讨论"记录介质本身的属性"——不讨论 UI / 入口形态 / 是否要前端 / 是否要 AI 介入。这些会留给 Phase 2 Design 的其他子任务（特别是 07 入口形态、09 AI 触达形态等假定存在的并行调研）。
- 本笔记**不修改** notes/01–06 与 foundation_2026.md 的任何内容；只在末尾给出"对 σ 系统的具体含义（U 级）"作为推论。
- 候选介质清单（按当前候选，不限于）：
  1. **Markdown + git**（本地纯文本 + 版本控制）
  2. **关系数据库**（PostgreSQL / MySQL，自托管）
  3. **SQLite**（嵌入式单文件 DB）
  4. **Notion**（云 SaaS 文档/数据库混合）
  5. **Obsidian**（本地 markdown 文件 + 插件生态，可选 Sync）
  6. **纯文本** / 纯 markdown（无 git）
  7. **第三方 SaaS**：Trello / Airtable / Day One / Evernote / Roam Research

---

## 摘要（5 段，每条带等级）

**1. "用户事后改写记录" 是真实存在的风险——并且每种介质都允许它，差别仅在"留下多少痕迹"。**【S 级 + M 级】医学记录改写文献明确指出：**事后改写记录在出现负面结果（诉讼、不利结局）后非常常见，且改写本身的合法性取决于是否留有审计痕迹**（MDDUS 2022；MDU Journal；Frier Levitt 2024 EMR 审计追踪综述；APA Psychiatric News 2023）。这一原则可以无差别迁移到"交易后情绪化改写日志"——尤其是在亏损交易后。**关键认识：审计性的强弱是一个谱系，不是有/无的二元开关**：
- ELN（电子实验记录本，FDA 21 CFR Part 11 合规）= 自动时间戳 + 不可删除 + 不可编辑历史 = **强审计**【S/M 级，HMS IT、NIH、LabArchives 文档】；NIH 2024-06-30 起强制要求新研究使用 ELN。
- git（带 GPG 签名 + push 到远程） = 在远程被 push 后历史可校验；但**本地未 push 时可以 `git rebase` / `git commit --amend` / `git push --force-with-lease` 静默重写历史**（jvns.ca 2023；git docs；GitHub Docs 2024）= **中等审计**——比 markdown 强很多，但远不如 ELN。
- 关系数据库 / SQLite = **审计依赖应用层 schema**（是否有 created_at, updated_at, soft delete, append-only event log）。裸 SQLite **没有**自动审计——可以 UPDATE / DELETE 然后 VACUUM 抹掉痕迹（Belkasoft 2024 取证文献已专门研究 SQLite freelist / WAL 数据残留，反向印证默认状态下"删除即近乎不可恢复"）【S 级取证文献】。
- Notion / Airtable / Trello = **审计完全握在厂商手中**，用户个人通常拿不到底层版本历史；Notion 仅承诺"30 天内删除可恢复"（Notion 帮助中心 2024）【M 级】；账号被封禁时数据可能完全无法导出（LowEndBox 2024 报道，Notion ToS）【W-M 级】。
- 纯 markdown / 纯文本（无 git）= **零审计**，用任何文本编辑器都能重写而不留痕。

**2. 进入门槛上 git 对小白确实是天书——这是 S 级证据，不是个人偏见。** Perez De Rosso & Jackson (MIT, OOPSLA 2016；MIT 学位论文 2017) 的同行评审"概念设计分析"明确得出：**git 的复杂度不是"威力的副产品"，而是设计缺陷**。研究发现"轻度用户因为放弃理解产品、只死记几个命令而极度沮丧；重度用户为这种设计辩护"。【S 级】研究者构造了 Gitless 替代设计并通过用户研究证明改善是真实的。一份学位论文（Diva Portal 2016）调查发现**初学者偏好 GUI，随经验增长才转向 CLI**；教育文献（NTNU 2019）指出 git 在编程教学中"为学习增加了独立的复杂度负担"。结合 ItsFOSS 2024 / Quillium 博客（W 级）："非技术写作者面对 git 时通常退化到 essay_FINAL_FINAL.docx"。**对小白交易员而言，git 不是"加分项"，而是一道额外的留存杀手**——把它强加于人会把"诚实日志的留存"问题变成"git 学习的留存"问题。

**3. 数据可移植性 / vendor lock-in 在 SaaS 工具中是真实且高代价的——而且是**不对称风险**：当一切顺利时它不可见，一旦事情出错，损失是灾难级的。**【M-W 级，但证据指向同一方向】Evernote 案例（2022 Bending Spoons 收购后；The Verge 2023；RetentionCheck 2024）：年付从 $69.99 涨到 $129.99（+86%），免费版砍到 50 笔记上限，**已存在的大型笔记库无法导出除非升级付费**——大量用户自述"我的笔记被人质化"（Evernote Discussion Forum）。Notion（LowEndBox 2024 报道）：账户被以"违反内容政策"封禁后**没有法律义务返还用户生成的数据**——GDPR 等法规仅覆盖"服务持有的关于你的个人信息"，不覆盖"你创作的内容"。这是用户经常误解的关键法律点。Airtable / Trello / Asana 的导出（Airtable Support 2024；OptimizeIS 2024）：CSV 导出**不包含附件、评论、活动历史、公式、关联记录**，只能拿到原始字段。**对一个长期跨年训练系统**，这意味着如果 5 年后想换工具/换 AI 后端，**SaaS 介质会让数据迁移成本远高于换工具的经济收益**——形成"可移植性陷阱"。

**4. 隐私 / 第三方访问对"诚实"机制是非中性的——这一条在 Lelkes 2012 被引用之外有更深的延伸。**【S 级】Lelkes 等 (2012, *Journal of Experimental Social Psychology*) 已证明"完全匿名 → 满足社会期望偏差减少，但准确性也下降"——这是 foundation 已引用的。但对 Phase 2 Design 更直接相关的是另一条证据线：**"被监视感"导致自我审查 (chilling effect)** ——PEN America 2013（写作者调查，500+ 美国作家）报告政府监控认知减少了写作的话题广度【M 级】；Stoycheff (2016, *Journalism & Mass Communication Quarterly*) "Under Surveillance" 实验证明"被监视感"激活螺旋沉默，减少表达意愿【S 级】；Schalkwijk-Tomlinson 等在 Kazakhstan 的 N=5025 调查实验显示"提醒被监视" → 敏感问题作答率下降约 3 个百分点【S 级】；ERIC EJ704730（Course Diaries 自我审查研究）发现学生在课程日记中确实大规模自我审查【S 级】。**含义**：一个"明显被云端 / 老板 / AI / 第三方读"的记录介质，会让用户自我审查最敏感的信息——而最敏感的恰恰是最有诊断价值的（"我不该追的，我追了"，"我撒谎说没看群消息其实看了"，"我想报复昨天的亏损"）。**这不是隐私偏好问题，是诚实数据采集质量问题**。

**5. 关于"被审视感与诚实承诺的张力"——Lelkes 范式之外的两条独立证据线，方向相反，需要一起设计。**【S 级】
- **(a) 被watched 提升合作 / 诚实**：Bateson, Nettle & Roberts (2006, *Biology Letters* "watching eyes" 研究）即使是**贴一张眼睛海报**也提升公共合作行为；Shariff & Norenzayan (2007, *Psychological Science*) 与后续 PLOS One 2014 中东穆斯林研究显示宗教启动让欺骗下降（控制 53% → 召唤祈祷启动后 68% 诚实）。机制是"reputation concern"被激活。
- **(b) 完全私密 → 敷衍**：Lelkes et al. (2012) 已证明（已被 foundation 引用）。
- **结论形状**：σ 系统需要的是"中等被监视感"——足够让用户感到"有一个会读的对象（哪怕是 AI 或自己未来）"，但不至于强到触发自我审查。**这意味着记录介质本身的可见性设置是一个机制变量，不是用户偏好**。介质不能被设计成"完全私密黑盒"，也不能是"完全公开 timeline"。**Markdown + git + 本地默认 + 周复盘时回看 / AI 在用户主动调用时读** 这一组合恰好命中"中等被监视感"——但这是 U 级推论，不是已被验证的 RCT 结果。

---

## 一、介质对比矩阵

> 单元格简记：✓ = 显著优势；× = 显著劣势；○ = 中性 / 取决于配置；? = 证据不足
>
> 6 个维度按用户原始 Q 的顺序：1) 不可篡改/审计；2) 进入门槛；3) 可移植/锁定；4) AI 可分析；5) 隐私/安全；6) 被审视感对诚实激励的契合度

| 介质 | 1. 审计性 | 2. 门槛 | 3. 可移植 | 4. AI 可分析 | 5. 隐私 | 6. 被审视感契合 | 综合等级 |
|---|---|---|---|---|---|---|---|
| **markdown + git（带 GPG 签名 + 推送到私有远程）** | ○-✓（本地可 force-push 重写，但远程一旦推送难无痕；签名提供身份证明）| ×（小白学曲陡，S 级证据） | ✓✓（plain text + 标准 SCM，60 年生命）| ✓✓（任何脚本/LLM 可读 .md/git diff）| ✓（本地默认 + 自托管远程可端到端加密）| ✓（commit 仪式有"被记录"感 + 默认私密）| **A-** |
| **纯 markdown / 纯文本（无 git）** | ×（任何编辑器可静默重写）| ✓（最低）| ✓✓ | ✓✓ | ✓（本地）| ×（无任何留痕，过度匿名→敷衍风险）| **C+** |
| **关系数据库（PG/MySQL，自托管）+ 应用层审计** | ✓（如果 schema 设计含 append-only event log + soft delete）| ××（小白完全不可行）| ○（CSV 导出 + DDL 可移植，但 schema 锁定）| ✓✓（SQL 强）| ○（自托管私密；维护成本高）| ○ | **B-** （太重）|
| **SQLite（单文件）+ 应用层审计** | ○（默认无审计；需在 app 层加 trigger / audit table）| ×（要求 app 层）| ✓（单文件 + 标准 SQL，文件格式承诺数十年稳定）| ✓✓（SQL + Pandas 直读）| ✓（本地单文件，加密插件可用）| ○ | **B+** |
| **Notion**（云 SaaS） | ××（用户拿不到底层审计；30 天恢复窗口；账号被封 = 数据丢）| ✓（小白上手快）| ××（块结构 + 关系字段导出残缺）| ○（API 速率有限；非结构化）| ××（云端、AI 子处理器、政府请求政策不公开）| ××（"被监视"由公司监视，不是为诚实激励服务）| **D** |
| **Obsidian**（本地 markdown + 插件 + 可选 Sync） | ○-✓（与 markdown+git 等同；可选 git 插件）| ○（GUI 易，git 进阶可选）| ✓✓（vault 就是普通文件夹的 .md）| ✓✓ | ✓（本地默认；Sync 可端到端加密）| ✓ | **A** |
| **第三方 SaaS（Trello / Airtable / Day One）** | ××（除 Day One 端到端加密外）| ✓ | × | ×-○（Day One 加密反而限制 AI 分析）| ×（除 Day One）| × | **C-** |

> ⚠️ 这个矩阵本身是 U 级综合判断（综合多份 S/M 级原子证据）。每一格的依据见 §二。综合等级是基于 σ 系统**特定使用场景**（个人交易训练、需要长期可审计、有 AI 协作、单人维护）的加权——它**不**是普遍适用结论。

---

## 二、各维度的关键证据

### 2.1 不可篡改性 / 审计性

#### 2.1.1 关键概念：审计性 ≠ 二元有/无，是一个谱系

**核心命题**：用户事后"圆滑化" 自己的日志（在亏损后改写"我当时其实知道会跌"，在错过机会后写"我本来就要进的"）是**已被实证的人类倾向**——不是 σ 系统独有问题。在医疗领域它有专门名字：**retrospective record alteration after adverse outcome**。

**MDDUS (2022) "Altering Clinical Records – Do's and Don'ts"** 与 **MDU Journal "Retrospective Records"**【M 级，专业责任组织 / 监管指引】指出：
- 事后改记录在医疗诉讼中是**常见的、可识别的**模式。
- 改写**本身**不一定违法——但**未透明记录修改人 / 修改时间 / 修改原因**会立刻提升嫌疑。
- 合法的事后修改流程：**保留原条目可见（划线但不擦除）+ 标注修改人/时间/原因**。
- "在不利结局之后做出的、看起来对自己有利的修改" 在举证中会被法院认定为高度可疑。

**APA Psychiatric News (2023) "Changing the Medical Record: A Risk Management Perspective"**【M 级】明确指出："改写病历是一种心理诱惑——尤其在不利后果发生之后。系统设计应当让事后改写**昂贵**，而不是依赖临床医生的自律。"

**Frier Levitt (2024) EMR 审计追踪综述**【M 级，法律评论】：现代 EMR 的核心防御是**自动审计追踪**——记录"谁、何时、改了什么、从哪里"——使得事后篡改不能无痕进行。

**含义（U 级推论）**：交易者在亏损后"圆滑化"自己的决策链是这一现象的**直接同形迁移**——不需要新的实证就可以预测它会发生。事实上 foundation_2026.md 已经引用 Cipriano 2020 显示"写日志会诱发过度自信和组合偏差"——其中一部分机制就是**对自己说服自己**——这件事如果发生在一个**可以静默回写日志的介质上**，效应会更严重。

#### 2.1.2 各介质的实际审计能力

**ELN（电子实验记录本）—— 行业最高标准**【S/M 级】：
- 来源：HMS IT ELN 服务文档、NIH OIR Intramural ELN Policy（2024-06-30 起强制）、LabArchives 选型指南、SciSure ELN、IDBS ELN 综述。
- 关键属性：
  - **自动时间戳**——不可由用户更改。
  - **不可删除历史**——所有改动有版本，旧版本永远可调阅。
  - **电子签名 + 工作流批准**——加上"who"维度。
  - **符合 FDA 21 CFR Part 11 / GLP / GMP**——具备法律可采性。
- 这是"诚实记录介质"的金标准。但部署成本对个人用户过高。

**git + GPG signed commit + 推送到远程**【S/M 级，git docs / GitHub Docs 2024】：
- 已签名的 commit 提供**身份不可冒充**保证。
- 推送到 GitHub 后，签名验证记录被**持久化存储**——即使后来私钥过期或撤销，"过去验证过"这一事实仍被保留。
- 远程仓库可以设置**保护分支**（protected branch）禁止 force push——一旦设置，已 push 的 commit 不能被无痕重写。
- **但本地未 push 时**：`git rebase`、`git commit --amend`、`git filter-branch` 都可以静默改写历史；`git push --force` / `--force-with-lease` 也可以覆盖远程（如果远程未保护）。
- jvns.ca (2023) "git rebase: what can go wrong" 详细列举了 rebase 可丢失数据的多种方式——这恰好是 σ 用户**故意**用来抹掉记录的潜在工具。

**含义**：git 不是"自动审计"——它是"如果你设置好（签名 + 推送 + 保护分支），它会成为强审计；如果你没设置，它退化到 markdown 加版本号"。

**关系数据库 / SQLite**【S 级取证文献】：
- 默认 schema（CREATE TABLE 后直接 INSERT/UPDATE/DELETE）**没有**审计能力——UPDATE 后旧值丢失，DELETE + VACUUM 后行不可恢复。
- 需要应用层显式设计：append-only event log（只 INSERT，不 UPDATE）、soft delete（is_deleted 字段而非物理删除）、updated_at 触发器、审计影子表。
- Belkasoft (2024) "Forensic Analysis of SQLite" + Mdpi FORC (2023) 研究表明：SQLite 的 freelist 和 WAL 中**确实**残留少量被删除数据，但经过 VACUUM 后这些残留会被清理——所以"取证可恢复"和"普通用户不可恢复"是两个不同问题。对 σ 系统的设计相关的是后者：**普通用户能否在情绪化时静默删除记录**？答案是**能，且 trivially**。

**Notion / SaaS**：
- Notion 帮助中心：**已删除内容 30 天内可由用户在垃圾箱恢复**——但**编辑历史**只在某些场合可见，且不能被用户用作可信审计源。
- 用户**没有**底层数据库访问权——审计完全握在 Notion 公司手中。

**纯 markdown / 纯文本（无 git）**【U 级 + 常识】：
- 任何文本编辑器可静默改写。
- mtime 可以用 `touch` 改写。
- 没有任何机制阻止用户在亏损后悄悄修改"昨天的"日志。

#### 2.1.3 关于 σ 的具体审计需求（U 级，推论）

不是所有内容都需要相同审计强度。基于诚实激励的等级：
- **决策链记录（开仓前）**：最高审计需求——这是承诺，不能被亏损后改写。
- **交易后情绪记录（30 分钟内）**：高审计需求——记录"当时的感受"，事后改写会摧毁后续模式分析的价值。
- **周/月复盘**：中审计需求——本身是反思性内容，迭代修订是合理的，但需要知道哪些是原始、哪些是后修。
- **知识库 / 主张库 / 系统文档**：低审计需求——这本来就是迭代演化的内容。

这个分级的实际含义：**不是整个系统都需要 ELN 级审计——但"决策链 + 交易后情绪"这两类需要至少 git 级别的强审计**（一旦写入推送，事后改写留痕）。

---

### 2.2 进入门槛

#### 2.2.1 git 对非技术用户：不是偏见，是 S 级研究结论

**Perez De Rosso, S., & Jackson, D. (OOPSLA 2016 / MIT thesis 2017) "Purposes, Concepts, Misfits, and a Redesign of Git"**【S 级】：
- ACM SIGPLAN 同行评审。
- 方法：概念设计分析（Conceptual Design Analysis）。
- 关键发现：
  - git 的复杂度**不是必然的**——是设计缺陷的体现。
  - 已知 git 难点可被解释为 "concept misfits"（基础概念无法满足其设计目的）。
  - **重度用户为 git 辩护，轻度用户对 git 极度沮丧**——这是经典 Stockholm pattern。
- 实证：作者构造 Gitless 替代设计，用户研究显示用户在 Gitless 上犯错少很多——证明问题在**设计**不在**用户能力**。

**Diva Portal 学位论文 (2016) "Git UI Thesis"**【M 级】：
- 调查发现**初学者偏好 GUI**，随经验增长才转向 CLI 或两者并用。
- 含义：把 σ 用户直接扔到 `git` 命令行 = 把他扔到一个有 S 级研究证明对新手不友好的环境。

**NTNU NIK 论文 (2019) Git in Education**【M 级】：
- 在编程教育中，git 给学习增加了**独立的复杂度负担**。
- 学生反映 git 影响了他们的学习和小组合作体验。
- 教育者经常反馈："学生为了 git 痛苦的时间，比为了实际课程内容多。"

**含义**：σ 用户的核心目标是"成为优秀交易员"——任何让他**为了工具本身**痛苦的设计都是直接减分项。把 git CLI 作为强制门槛 = 引入一个 S 级证据已知会失败的留存陷阱。

#### 2.2.2 写者 / 研究者对 git 的实际反应（W 级，但方向一致）

- ItsFOSS (2024) "Git Isn't Just for Developers": 鼓励写作者用 git——但承认即使是技术写作者也常常退化到 `essay_FINAL_FINAL_v2_real.docx`。
- Quillium (W 级，产品博客): 直陈"git 对 prose 用户不合适，line-level diff 不适合段落式思维"，于是开发了"基于段落的版本控制"。
- Ink & Switch (Upwelling, 2024): 明确指出"version control 让作者有 fishbowl effect（金鱼缸效应）——被监视的不适感"。
- Curvenote (科学家版本控制): 同样以"git 对科学家太复杂"为前提，构造了 block-level 的替代。

#### 2.2.3 SQL / 关系库对小白：不可行

【U 级 + 常识】小白用户独立写 SQL 几乎是 0 起点——比 git 更陡。除非系统提供完全的应用层 UI 包装（即用户完全不接触 SQL），否则关系库作为前台介质对零基础用户是禁区。

#### 2.2.4 Notion / Obsidian：低门槛

【M-W 级，TraderSecondBrain 2026 / 用户社区】：
- Notion: **已被工业界确认为最低门槛的交易日志介质**。开箱即用，跨设备，预制模板。
- Obsidian: **GUI + markdown** 组合——比 Notion 略陡（需要理解 vault 概念），但比 git 平很多。
- Google Sheets / Excel: 30 秒可上手（同源）。

**含义**：从纯门槛维度看，Notion / Obsidian / Sheets 一起比 git / SQL 平 1-2 个数量级。

#### 2.2.5 一个反直觉的发现：高门槛不一定是劣势

**用户原始问题中提到 Lelkes 2012**——完全私密 → 敷衍。同样的逻辑可能在介质门槛上有镜像：**几乎零门槛的介质（Notion 直接编辑）可能让"诚实记录"过于轻量化**——用户感觉不到这是一个仪式性承诺。git commit 的"敲一行命令 + 写 commit message"可能反而**激活"我现在在做一件正式的事"的认知**。这是 U 级推论，没有直接 RCT，但它符合"承诺 / 诚实启动"的整体证据方向（Capraro et al., 2024 *Nature Human Behaviour*：诚实承诺的仪式化降低欺骗 4.5–8.5 个百分点；foundation 已引用）。

**所以"门槛 = 劣势"是简化判断**。门槛分两类：
- **实质性门槛**（学习 git 概念本身）= 净劣势。
- **仪式性门槛**（每次记录前一个固定的、轻量的、有意义的动作）= 净优势。

理想的介质应当**消除前者，保留后者**——这是 σ 设计的明确目标。

---

### 2.3 数据可移植性 / Vendor lock-in

#### 2.3.1 plain text / markdown 的耐久性

**Duke University Libraries Recommended File Formats for Digital Preservation**【M 级，图书馆学界标准】：
- markdown 被列为 **Level Two preservation format**——长期保存可行，但可能需要额外资源（主要是为了保留语义结构）。
- 纯文本 (.txt) 列为最高保存级别之一。

**Rivet (2023) "On the Durability of Plain Text"**【W 级，但论据全部基于已知事实】：
- ASCII 标准已稳定 60+ 年；预期还会持续几个世纪。
- 文本文件可在任何平台读取，无私有软件依赖。
- 易备份；几乎从不损坏（vs 数据库文件常见的 corruption）。
- 在 markup 标准间转换 trivial（markdown ↔ asciidoc ↔ rst）。

**Harvard Pamphlet Blog (2014, 已 12+ 年仍可访问) "Switching to Markdown for Scholarly Article Production"**【W 级，但来自学者实践】：
- 学术写作的 plain-text + markdown + LaTeX/BibTeX 工作流被多家学术机构推荐。
- 反对 Microsoft Word 的核心论据是**长期兼容性问题**——专有格式数年内会破坏。

#### 2.3.2 Notion / Evernote / Roam 的导出问题

**Evernote (Bending Spoons 收购 2022 后) 案例**【M 级，The Verge 2023 + RetentionCheck 2024】：
- 时间线：
  - 2022-11: Bending Spoons 收购 Evernote。
  - 2023-中: 美国 / 智利团队约 250 人裁员；运营迁欧洲。
  - 2023-2024: 年付翻倍 ($69.99 → $129.99 → $169.99)；免费版砍到 50 笔记上限。
- 用户感受：Evernote Discussion Forum 多个帖子标题包含 "held hostage"、"can't export my notes"。
- 大规模 exodus 到 Obsidian / Joplin。

**Notion 账号被封禁 = 数据无法找回**【W-M 级，LowEndBox 2024 报道 + Notion ToS】：
- 一名 Notion 用户报告：账号因"违反内容政策"被禁，无任何申诉途径。
- **核心法律点**：GDPR 等法规仅覆盖"服务持有的关于你的个人信息"，**不覆盖"用户在服务上创作的内容"**——这是用户经常误解的关键。
- Notion ToS 给公司"对持续提供服务的额外审查权"——这是宽泛保留。
- Notion 帮助中心承诺"30 天内删除可恢复"，但这不是"账户被封时数据可取回"的承诺。

**Airtable / Trello / Asana 导出限制**【M 级，Airtable Support 2024 + OptimizeIS 2024】：
- CSV 导出**不包含**：附件、图片、评论、活动历史、公式、关联记录、视图配置。
- 只能拿到原始字段——所有"工具特性"丢失。
- 迁移需要"deliberate planning to avoid data loss"——意味着**等到要迁移时才发现锁定有多深**。

**Apple Notes**（Android Police 2024）: 没有 bulk export；用户必须 PDF→Google Docs 中介——"故意做得难迁"。

#### 2.3.3 git + markdown 的可移植性

**core 优势**【S/M 级综合】：
- 文件就是 plain text——任何文本编辑器可读。
- git history 是 standard SCM 格式——任何 git 实现可读 50 年内的所有 commit（git 本身已 20 年）。
- 迁移到非 git 工具：不需要"迁移"，把文件 cp 走即可。
- 迁移 git 主机（GitHub → GitLab → 自托管 Gitea）：`git remote set-url`，秒级完成。

**实证案例（Beancount 用户长期使用）**【W 级，antonta.net 2024】：
- 一位用户用 Beancount（plain text accounting）近 10 年。
- 评价：数据模型完美，文档优秀，long-term learning curve 良好。
- 但承认 plain text 的**append-only 性质** 在大规模历史下变得 awkward——文件管理 / 重命名账户 / 历史修订都需要工具支持。
- 即便如此，作者评价"我拥有每一个字节"——这是 SaaS 工具完全无法提供的。

#### 2.3.4 SQLite 的中间地位

【M 级】SQLite 文件格式有**官方承诺到 2050+ 的稳定性**（sqlite.org "long-term support"）。是 plain text 之外少有的有这种长期承诺的二进制格式。Library of Congress 把 SQLite 列入推荐保存格式。但 SQLite **不像 plain text 那样可被任何工具直接打开**——需要 sqlite3 CLI 或 GUI 工具。

#### 2.3.5 综合判断（U 级）

可移植性梯度（从最强到最弱）：
1. **markdown + git** ≈ **纯 markdown** > **SQLite** > **关系库** > **Obsidian** ≈ git+md（vault 就是文件夹）> **Notion** > **Airtable / Trello** > **Apple Notes / 闭源 SaaS**.

但这个梯度有一个 caveat：**可移植性的真实价值在小概率事件中爆发**——99% 的时间你不需要迁移，1% 的事件（公司倒闭/收购/封号/换技术栈/AI 后端换代）可能让 SaaS 用户损失多年记录。**因此 vendor lock-in 是非对称风险——平时不可见，出事时灾难级**。

---

### 2.4 AI / 脚本可分析性

#### 2.4.1 plain text + markdown：最大灵活性

【U 级 + 常识】：
- 任何 LLM 可直接读 .md 内容。
- `grep` / `ripgrep` / Python `glob` + 简单 regex 即可全库搜索。
- 标准库（Python `markdown`, `mistune`）即可解析为 AST。
- git diff 提供"什么时候哪一行改了什么"的结构化信息——这对 σ 后期"是否事后悄悄修改决策链"的检测是 trivial 的：`git log --all --diff-filter=M -- decision_chain/*.md` 即可。

#### 2.4.2 SQLite：结构化数据的最佳轻量选择

【M 级，pythonspeed.com 2024 + cloudnativeengineer 2024】：
- pandas `pd.read_sql_table()` / `pd.read_sql_query()` 一行代码读全表。
- SQL 提供 GROUP BY / JOIN / 时间序列分析等——这是统计分析（如"我的胜率按情绪分组怎么样"）的天然语言。
- 文件大小 30MB-100MB 时性能最佳——σ 系统单人 5-10 年的交易记录预计在此区间。
- LLM 也可直接读 SQLite（gpt 系列 / Claude 已有 sqlite tool）。

#### 2.4.3 Notion：API 限速 + 块结构非标准

【M 级，Notion API 文档 + 用户报告】：
- API 速率限制 3 req/s 默认——批量分析慢。
- 页面以 block 树存储，导出 markdown / HTML 时**会丢失**很多结构信息（如 toggles 内部的复杂嵌套）。
- LLM 不能"直接"读 Notion，必须经 API 拉取（有时还要加权限）。

#### 2.4.4 Obsidian：与 markdown + git 等同

Obsidian 的 vault 就是文件夹，里面是普通 .md——所以 AI / 脚本可分析性等同于 markdown 方案。**Dataview 插件**额外提供了"用 SQL-like 语法查询自己的笔记"的能力——这是一个"脚本可分析性"维度上的小加分。

#### 2.4.5 Day One 端到端加密：对 AI 是反向的

【M 级，Day One Privacy FAQ 2024】Day One 默认 E2EE——这意味着**LLM 无法直接读**，除非用户自己解密导出。这是隐私强 → AI 协作弱的典型权衡。对 σ 系统不适用（系统的核心就是 AI 协作）。

---

### 2.5 隐私与安全

#### 2.5.1 本地优先 vs 云端的法律风险差异

**Ink & Switch (2019, 仍被广泛引用) "Local-First Software: You own your data, in spite of the cloud"**【M-S 级，行业经典论文】：
- 七大原则：no spinners、works offline、collaboration、universal access、long now、security & privacy by default、retain ownership。
- 论证：当前的"云优先"软件让用户成为"自己数据的租户"——服务一旦终止 / 公司一旦倒闭 / 法律一旦变化，数据就消失。

**privacy-first 日记 app 评估（Hellman 2026, Medium）**【W 级，但综合多家厂商公开信息】：
- 关键评估维度：
  1. E2EE 是否默认（不能 opt-in，用户绝大多数不开 opt-in）。
  2. 密钥归属（用户持有 vs 公司持有——后者意味着公司可被司法强制访问）。
  3. 开源（独立验证隐私声明）。
  4. 数据存储位置（公司服务器 vs 用户云 vs 自托管）。
  5. 法律管辖（决定政府能强制公司披露多少）。

**Day One 的具体情况**【M 级，Day One Privacy FAQ + 用户论坛 2024-2025】：
- AES-GCM-256 默认 E2EE for Premium。
- 密钥默认存 iCloud（macOS）或 Google Drive（Android）。
- Day One 论坛中存在合理质疑：iCloud 中部分数据**不**默认 E2EE——意味着政府请求 Apple 时可能拿到密钥。
- Day One 自身是闭源——用户必须信任厂商声明。

#### 2.5.2 Notion 的隐私实然现状

【M 级，Notion 帮助中心 / 隐私政策 2024】：
- AES-256 静态加密 + TLS 1.2+ 传输加密——**这是行业标配，不是隐私优势**。
- **不是端到端加密**——Notion 服务器持有加密密钥，员工有访问可能（虽然受策略限制）。
- 数据驻留：默认美国（US-West-2），Enterprise 可选 EU-Central-1（Frankfurt），但用户账户、计费、成员数据**始终留美**。
- 子处理器：AWS（基础设施）、Anthropic / OpenAI（AI 后端）——意味着 σ 用户的内容如果用 Notion AI，会经过这些第三方。
- Notion 帮助中心承诺：默认**不**用客户数据训练 AI；用户可加入 LEAP 计划（toggle "Share data to improve Notion AI"）选择性共享。但**第三方子处理器（Anthropic/OpenAI）是否有自己的训练用途**——Notion 通过合同要求他们不用，但用户没有独立验证手段。

**含义**：把"诚实交易日志"放在 Notion 上 = 默认信任 Notion + AWS + Anthropic + OpenAI **四个组织**对你内容的合规处理。**对一个明确以"诚实"为元规则的系统，这是不可接受的隐私表面**。

#### 2.5.3 Obsidian / Markdown 的隐私实然

【M 级，Obsidian Privacy Policy + Security 文档 2024-2025】：
- 默认本地存储——不向 Obsidian 服务器发送任何数据。
- **不需要账号**。
- **不收集** desktop / mobile 的 telemetry。
- 第三方安全审计已发现的漏洞均已修复。
- Obsidian Sync（可选付费服务）支持端到端加密（AES-256 + scrypt）——**只有用户能解密**。
- 关键：**vault 就是文件夹**——用户可以选择把 vault 放在本地、自己的 Dropbox、自己的 git 仓库、自己的服务器。

#### 2.5.4 监控可见性对诚实的影响（链 §2.6 详细，这里只点）

【S 级，PEN America 2013 + Stoycheff 2016】：用户感知到"被云端公司读 / 被政府读 / 被广告网络读"会激活自我审查——chilling effect。这是一个**机制上的诚实数据采集风险**，不是用户偏好。

**含义（U 级推论）**：σ 系统的诚实质量与介质的"被第三方看见的可能性"反相关。**云 SaaS = 高第三方可见 = 用户对最敏感内容自我审查 = 诚实数据质量下降**。

#### 2.5.5 "本地"也不是绝对私密

【U 级，常识】本地存储 ≠ 绝对私密：
- 设备失窃。
- 家人 / 同住人偶然访问。
- 备份云端（iCloud / Time Machine）的隐私级别取决于云服务。
- 全盘加密（FileVault / BitLocker）是必要前提。

---

### 2.6 与"被审视感"诚实激励的契合度

这一节直接回答用户问题中最深的一条：**记录介质如何影响"被审视感"，从而影响诚实质量**。

#### 2.6.1 谱系两端：完全私密 vs 完全公开

**完全私密 → 敷衍**【S 级，foundation 已引用】：
- Lelkes et al. (2012, *Journal of Experimental Social Psychology*) "Complete anonymity compromises the accuracy of self-reports"。
- 三研究：
  - 实验 1：被试在网上研究信息时被秘密追踪；匿名组报告自己的浏览行为不如匿名组准确。
  - 实验 2-3：M&M / jelly bean 消费量回忆——匿名组始终不如非匿名组准确。
- 解释机制：匿名 → 减少"提供有面子答案"动机，**也**减少"认真作答"动机；后者占主导时，准确性下降。
- 引申到日志：**完全没人会读的日志容易退化成敷衍**。

**完全公开 → 自我审查**【S 级，多份独立证据】：
- ERIC EJ704730 (College Teaching, 2004) 课程日记自我审查：跨课程一致——学生在被老师读的日记里普遍自我审查。
- PEN America (2013) 美国作家调查：政府监控认知 → 多名作家自陈刻意避开特定话题。
- Stoycheff (2016, *Journalism & Mass Communication Quarterly*) "Under Surveillance"：螺旋沉默实验——感知监视减少表达意愿。
- Schalkwijk-Tomlinson 等 (Kazakhstan, *Political Behavior* 2026) N=5025 调查实验：暴露于"被监视提醒"使敏感问题作答率下降约 3 个百分点。
- Tandfonline 2022 "Cookies and Content Moderation"：affective chilling effects——内化的监视使发言改变。

#### 2.6.2 中间层：被部分人 / AI / 未来自己看见

**Bateson, Nettle & Roberts (2006, *Biology Letters*) "Cues of being watched enhance cooperation in a real-world setting"**【S 级】：
- 仅仅在咖啡机上贴一张"眼睛"图片，参与者主动付钱率提高（vs 控制条件的花朵图片）。
- 机制：reputation concern 即使在匿名场景也可被纯感知激活。

**Shariff & Norenzayan (2007, *Psychological Science*)**【S 级】 + **Aveyard (2014, PLOS ONE) 中东穆斯林版本** 【S 级】：
- 宗教启动 / 召唤祈祷 → 欺骗下降；中东版本 53% → 68% 诚实率。
- 机制：supernatural monitoring hypothesis——"全知存在在看"的认知激活诚实。

**含义（U 级综合）**：当感知到"有一个温和的、不评判的、不会公开的对象在看"——诚实最优。这就是"中等被审视感"假设。

#### 2.6.3 各介质在"被审视感"维度上的实际定位

**完全私密端**：
- 纯 markdown（无 git，无 AI 读）= **最匿名**——Lelkes 风险最高。
- 私密的本地数据库 = 同样高 Lelkes 风险。

**中等被审视端**：
- markdown + git commit（且 commit 是一个仪式 + 有可能被未来自己 / AI 读 / 周复盘读）= 激活"我的现在 commit 是给未来自己 / AI 看的"——这是**reputation concern 的内化版本**。
- Obsidian + 周复盘 + 自己回看 = 同上。
- 私有 GitHub 仓库（只有自己能看）= 同上。
- AI 教练定期读用户日志（透明告知 + 仅在用户主动调用） = 同上。

**完全公开端**：
- 公开 GitHub（任何人可见）= 高自我审查风险——交易者不会写"我犯了 X 错误，我嫉妒 Y 朋友赚到了"。
- 公开 Twitter / 论坛打卡 = 同上。
- Notion 团队空间（多人可见）= 同上。

**特殊：第三方云（不可信但用户感知模糊）**：
- Notion / Day One 等 SaaS——用户**模糊地知道**云端有公司服务器、有 AWS、有 AI 子处理器，但**具体哪些第三方能看是不清楚的**。
- 这种**不确定性**本身可能是最差的——因为它**不清晰**地激活了部分自我审查（"万一被读怎么办？"），但又没有清晰的"reputation concern"机制——所以激活了 chilling effect 的负面又没拿到 watching eyes 的正面。
- 这是 U 级推论，没有直接 RCT，但符合 chilling effect 文献的整体方向：**模糊的监视**比**明确的监视**对自我审查更不可控。

#### 2.6.4 关于"AI 是否在读"的一个特殊考虑

【U 级，结合 03 笔记 AI 教练证据】：
- 如果 AI 阅读规则**透明、用户主动触发、明确边界**（如"周日复盘时我会读这一周的所有交易日志"）——这接近 watching eyes 的良性版本。
- 如果 AI 阅读规则**不透明、被动触发、用户不知道何时何方**——这激活 chilling effect。
- σ 系统应当采用前者。

#### 2.6.5 综合（U 级）

**契合"中等被审视感"的介质组合**：
1. **markdown + git（默认本地，private repo，签名 commit，commit 是仪式，AI 周期性读，明确告知边界）** = 最契合。
2. **Obsidian（同样 vault 在自己仓库或本地，AI 协作明确）** = 同等契合。
3. **SQLite 单文件 + 应用层定期读 + AI 协作明确** = 中等契合（缺 commit 仪式）。
4. **纯 markdown 无 git** = 偏 Lelkes 端（过度私密）。
5. **Notion / 云 SaaS** = 模糊监视（最差结构）。
6. **公开 GitHub / 论坛** = chilling 端。

---

## 三、对 σ 系统的具体含义（U 级）

> 以下全部为 U 级——基于 §二证据的**逻辑推论**，不是已被验证的最佳实践。Phase 2 Design 应当把它们作为假设接受、并保留可调整空间。

### 3.1 介质需求清单（按优先级）

σ 系统的记录介质应满足：

1. **(必须)** 决策链 + 交易后情绪记录有审计痕迹：事后改写需留痕。
2. **(必须)** 用户可以独立、零成本拿走全部数据；公司倒闭 / 政策变化不会让用户损失训练记录。
3. **(必须)** AI 协作明确：用户清楚 AI 何时读什么。
4. **(必须)** 隐私保护：默认本地或用户控制的存储；不依赖第三方"我们承诺不读"。
5. **(强烈推荐)** 数据格式可被任何脚本 / LLM 直接读取，不锁定特定 AI 后端。
6. **(强烈推荐)** "被审视感"中等：commit 仪式 / 周读 / AI 读 触发；不公开。
7. **(强烈推荐)** 进入门槛分层：核心动作（写、保存）零学习；高级功能（diff / 查询）可选学习。
8. **(允许)** 长期存档稳定：10 年后仍可读。

### 3.2 当前候选介质与需求清单的契合度

| 介质 | 1.审计 | 2.可移植 | 3.AI透明 | 4.隐私 | 5.脚本可读 | 6.中等监视 | 7.分层门槛 | 8.长存档 | 综合 |
|---|---|---|---|---|---|---|---|---|---|
| markdown + git（私有 + 签名）| ✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✓ | ×（git CLI 是劣势）| ✓✓ | A- |
| Obsidian（vault + 可选 git 插件）| ✓ | ✓✓ | ✓ | ✓ | ✓✓ | ✓ | ✓（GUI 友好） | ✓✓ | **A** |
| SQLite + 自构 UI | ✓（如果 schema 设计好） | ✓ | ✓ | ✓ | ✓✓ | ○ | × | ✓ | B |
| Notion | × | × | ×（云AI）| × | × | × | ✓ | × | **D** |
| 纯 markdown | × | ✓✓ | ○ | ✓ | ✓✓ | × | ✓ | ✓✓ | C |
| 关系库（自托管 PG） | ✓ | ○ | ○ | ✓ | ✓✓ | ○ | ×× | ✓ | C+ |
| Day One | ○ | × | ××（E2EE 反向） | ✓✓ | × | ○ | ✓ | × | C |

**最适合 σ 系统的介质**（U 级综合判断）：**Obsidian-style 本地 markdown vault + 可选 git 后端（同步 + 审计）**——它在 8 个维度中除了"审计"略弱（vault 默认无审计；需 git 插件）外都接近最优。**门槛分层**优势特别重要——核心动作（在 Obsidian 里写 .md）完全不接触 git；高级动作（diff / 历史 / 跨设备同步）通过 git/Sync 添加。

**第二选择**：纯 markdown + git（不带 Obsidian）——审计强一点，门槛高一点。

### 3.3 具体设计含义（候选，留 Phase 2 Design 决定）

3.3.1 **核心存储 = markdown 文件 + 本地 git 仓库**：
- 决策链记录、交易后情绪、周复盘、月复盘、知识库主张全部以 .md 形式存储。
- git 仓库是**审计层**——commit 是仪式动作，commit message 强制非空（如固定模板"trade-decision YYYY-MM-DD-HHMM 标的"）。
- 每次开仓前的"决策链确认"在写入文件并 git commit 后才算完成；事后修改需要新 commit + 自动追加修改原因 prompt。

3.3.2 **AI 协作层 = 明确读时机**：
- AI 仅在用户主动触发时读：周复盘"周日 21:00 让 AI 读这一周"、月复盘、特定卡顿时刻。
- AI **不**实时读用户当下输入。
- 减少 chilling effect。

3.3.3 **用户接触层 = 可选**：
- 小白默认走 GUI 工具（Obsidian / VS Code 简化界面）写 markdown。
- 不需要学 git 命令——脚本封装 commit / push 为单一命令或自动化。
- 高级用户可直接用 git CLI。

3.3.4 **远程同步 = 私有自托管首选**：
- 推荐选项（按推荐度）：
  1. 自托管 Gitea / 自有 VPS（最强隐私，最高门槛）。
  2. 私有 GitHub 仓库（中等隐私，低门槛）。
  3. 不同步（最强隐私，最低多设备能力）。
- 不推荐：公开仓库；任何"AI 公司直接挂在我数据上"的方案。

3.3.5 **统计层 = 可选 SQLite 视图**：
- 主存储是 markdown，但当用户需要做"过去 6 个月按情绪分组的胜率"等聚合分析时，可由脚本（用户/AI 触发）从 markdown 提取结构化字段写入 SQLite，做查询。
- SQLite **不**作为权威存储，只作为可重建的索引/视图。

3.3.6 **静默改写检测**：
- 因为有 git history，可以由 AI 或脚本周期性检测：哪些"决策链"或"交易后情绪"文件在 24 小时后被修改？这本身是诚实信号（高于阈值 → 周复盘提醒"你这周修改了过去的决策链 N 次，是哪些原因？"）。
- 这是 git 介质独有的能力——SaaS 介质完全做不到，纯文本无法做。

3.3.7 **Notion / SaaS 不适合作为权威存储**——但**可以作为入口包装**：
- 如果 Phase 2 决定保留某种 Web UI（如 Notion-style 编辑体验），可以把 Notion 作为"前端编辑器"，但每次保存都同步到 markdown + git 后端。
- 这避免了 vendor lock-in 风险，同时保留 SaaS 的低门槛优势。
- 但这是 U 级架构推论；Phase 2 Design 应评估实施成本。

### 3.4 与 foundation v5 已有约束的兼容性

foundation v5 包含 §三.13 "Plan 阶段不预设技术栈"——本笔记的所有结论都符合这一约束：**它们是关于"介质属性应满足什么"的需求，而不是"用哪个产品"**。

具体兼容点：
- foundation §三 关于"诚实承诺"机制（honesty oath）—— 与本笔记 §2.6 的"中等被审视感"机制兼容。"诚实承诺"在每次决策链开始时显示"我承诺如实记录"——如果记录介质本身就有 commit 仪式，这两个机制叠加效果应当最强。
- foundation §三 关于"AI 教练 wise feedback"—— 与本笔记 §3.3.2 "AI 协作层 = 明确读时机"兼容；wise feedback 应当在周读时给出，不实时打断。
- foundation §三 关于"退出协议"—— 本笔记的可移植性需求与"系统外的可持续性"目标一致：用户即使停止使用 σ 系统，也应当能保留并独立分析自己的训练记录。
- 本笔记**没有**与 foundation 任何已有约束直接冲突。

---

## 四、本笔记的局限

### 4.1 我没找到的证据 / 盲区

1. **没有任何针对"交易者使用不同介质（git vs Notion vs Excel vs 纸笔）的诚实质量 / 留存差异"的 RCT**——这一调研方向在学术界完全不存在。所有"哪种工具适合交易者"的推荐都是从业者意见（W 级）或工具厂商营销。本笔记的所有跨域证据都是**借用**（医疗记录的事后改写文献迁移到交易日志、写作者的 git 障碍迁移到交易者、健康日记的 chilling effect 迁移到交易日志）——这种迁移的有效性本身需要 N-of-1 验证。

2. **关于"git commit 仪式"是否真的激活诚实承诺的实验数据为零**——这是 §2.2.5 的核心 U 级推论。它**符合** Capraro et al. (2024) 关于"specifc honesty oaths"的整体方向，但**没有**直接验证"git commit 是否构成有效 honesty oath"。

3. **关于"中等被审视感"的精确剂量没有研究**——多 watching 太多 → chilling；多 watching 太少 → Lelkes 敷衍；中间最优。**最优点在哪里没有定量研究**。本笔记的"AI 周读 + 周复盘"是直觉性的中间点，但可能太弱也可能太强。

4. **针对中国用户 / A 股 / 港股交易者的文献基本不存在**——我查到的所有证据来自美国 / 欧洲 / 偶尔中东。文化差异（东亚 collectivist 文化对"被监视"的反应可能不同）可能让结论需要调整。

5. **本笔记未涵盖**：mobile-first 介质（用户大量在手机上记录）—— iOS / Android 上 git CLI 很笨重；如果手机是主要入口，介质选择可能要变化。但这是 Phase 2 入口形态调研的范围，不是本笔记。

6. **没有针对"语义版本控制 vs 纯文本 diff 在主张库 / 知识库使用场景的 HCI 证据"**——σ 系统的 knowledge/ 和 trades/ 两类内容性质不同，可能最优介质也不同（前者迭代演化，后者写后只改不再写）；本笔记把它们当作"统一介质"处理，这是简化。

### 4.2 我引用的证据的局限

1. **Lelkes 2012 的人群是大学生**——把它的"匿名 → 敷衍"机制迁移到"成年交易者写自己的交易日志"是 U 级推论，不是 1:1 证据。Lelkes 的"敷衍"是为了完成课程要求；交易者的"敷衍"动机不同（避免承认错误、维护自我形象）——可能更强或更弱。

2. **PEN America / Stoycheff 的 chilling effect 研究针对的是"政府监控"或"网络监视"**——把它迁移到"Notion 公司是否会读我的内容"是同方向迁移，但具体强度未必一致。

3. **Cipriano 2020（已被 foundation 引用）显示日志诱发过度自信**——本笔记 §2.1.1 假设"事后改写"会放大此效应；这是合理推论但不是 Cipriano 直接结论。

4. **MDDUS / MDU / APA 关于医疗记录改写的文献来源是责任组织而非 RCT**——它们的"改写在不利结果后常见"是基于诉讼数据库 / 风险管理经验，不是随机抽样的客观频率统计。但作为风险存在的定性证据已经足够。

5. **Perez De Rosso & Jackson 关于 git 复杂度的研究方法是"概念设计分析"** —— 是基于设计理论的形式化方法，不是 N=数百用户的实证研究。但作者后续的 Gitless 用户研究是 empirical，结果一致。

6. **Beancount 长期使用的"data owns me"反思来自单个用户博客（W 级）**——典型的 N=1 经验。我引用它是为了平衡"plain text 完美"的过度乐观，但不应当被当作群体证据。

### 4.3 对"诚实标记元规则"的应用自检

按 CLAUDE.md 的元规则：
- ✓ S 级证据已标注完整作者/年份/期刊（如 Lelkes 2012, Perez De Rosso 2016, Bateson 2006, Shariff 2007）。
- ✓ M 级证据标注了组织名称 / 出版方（MDDUS 2022、APA Psychiatric News 2023、NIH OIR 2024、Notion 帮助中心 2024）。
- ✓ W 级证据明确标注（Beancount 用户博客、ItsFOSS、TradersSecondBrain 等工具营销 / 社区文章）。
- ✓ 所有 §三 的判断都标了 U 级。
- ✓ "我没找到的证据"专门列出（§4.1）。
- ✓ 跨域迁移（医疗记录改写 → 交易日志事后修改）都明确为推论而非直接证据（§2.1.1, §4.2）。

不符合处的诚实标注：
- §2.6.5 的"介质契合度排序"包含较多 U 级综合判断；它们建立在 §二的多份 S/M 级原子证据上，但**汇总打分本身没有定量基础**——这是定性的工程判断。
- §3.2 的对比表是同样的限制——单元格的 ✓/× 是综合判断，不是测量。

### 4.4 与 06 笔记的关系

本笔记**不**重复 06 笔记中关于"工具留存"的证据（mHealth dropout、Duolingo streak 等）；它们关注"工具复杂度对留存的影响"，本笔记关注"介质属性对诚实质量与可审计性的影响"——是正交维度。但两者的判断方向一致：**降低实质性门槛、保留仪式性门槛、不依赖云端 SaaS、保护用户长期数据所有权**——这与 06 笔记关于"砍字段、提仪式、不依赖 streak 焦虑驱动"是同一类设计原则的不同侧面。

---

## 附：本笔记的关键引用清单（按出现顺序）

**S 级（同行评审）**：
- Lelkes, Y., Krosnick, J.A., Marx, D.M., Judd, C.M., & Park, B. (2012). "Complete anonymity compromises the accuracy of self-reports." *Journal of Experimental Social Psychology*.
- Perez De Rosso, S., & Jackson, D. (2016). "Purposes, Concepts, Misfits, and a Redesign of Git." OOPSLA / *MIT Thesis*.
- Bateson, M., Nettle, D., & Roberts, G. (2006). "Cues of being watched enhance cooperation in a real-world setting." *Biology Letters*.
- Shariff, A.F., & Norenzayan, A. (2007). "God Is Watching You: Priming God Concepts Increases Prosocial Behavior in an Anonymous Economic Game." *Psychological Science*.
- Aveyard, M.E. (2014). "A Call to Honesty: Extending Religious Priming of Moral Behavior to Middle Eastern Muslims." *PLOS ONE*.
- Stoycheff, E. (2016). "Under Surveillance: Examining Facebook's Spiral of Silence Effects in the Wake of NSA Internet Monitoring." *Journalism & Mass Communication Quarterly*.
- Schalkwijk-Tomlinson 等 (2026). "Digital Surveillance and Self-Censorship in Autocracies: Evidence from a Survey Experiment in Kazakhstan." *Political Behavior*.
- ERIC EJ704730 (2004). "Self-Censorship in Course Diaries." *College Teaching*.
- Li, I., Dey, A., & Forlizzi, J. (2010). "A Stage-Based Model of Personal Informatics Systems." *CHI 2010*.
- Epstein, D.A., Ping, A., Fogarty, J., & Munson, S.A. (2015). "A Lived Informatics Model of Personal Informatics." *UbiComp 2015*.
- Capraro, V., et al. (2024). "Honesty oath" megastudy. *Nature Human Behaviour*. （foundation 已引）
- Cipriano, M.C., Gruca, T.S., & Jiao, J. (2020). "Can Investing Diaries be Hazardous to Your Financial Health?" *Journal of Prediction Markets*. （foundation/01 已引）
- Belkasoft / FORC SQLite forensic literature (2024 / MDPI Applied Sciences 2023).

**M 级（专业出版 / 监管 / 大型机构）**：
- MDDUS (2022). "Altering Clinical Records – Do's and Don'ts."
- MDU Journal Issue 6. "Retrospective Records."
- Frier Levitt (2024). "Understanding EMR Audit Trails."
- APA Psychiatric News (2023). "Changing the Medical Record: A Risk Management Perspective."
- NIH Office of Intramural Research (2024). "Intramural Electronic Lab Notebook Policy."
- HMS IT (2024). "Electronic Lab Notebooks."
- Duke University Libraries. "Recommended File Formats for Digital Preservation."
- The Verge (2023). "Are you finally thinking of exiting Evernote?"
- RetentionCheck (2024). "Evernote Under Bending Spoons: Teardown."
- Notion 帮助中心（2024）. Privacy / Security / Data Residency / AI Privacy / Dormant Account / Delete Account.
- Day One (2024-2025). Privacy & Security FAQs / End-to-End Encryption FAQ / Privacy Policy.
- Obsidian (2024-2025). Privacy Policy / Security / Sync 文档.
- Ink & Switch (2019). "Local-First Software."
- PEN America (2013). "Chilling Effects."
- pythonspeed.com (2024). "Choosing a good file format for Pandas."
- cloudnativeengineer.substack.com (2024). "Easy Data Analysis with SQLite."
- GitHub Docs (2024). "About commit signature verification" / "Signing commits."
- git-scm.com docs (2024). "Signing Your Work" / "git-rebase Documentation."

**W 级（博客 / 营销 / 社区）**：
- TradersSecondBrain (2026). "Free Notion Trading Journal Template."
- LedgerMind (2024). "How to Maintain Trading Journal Profits."
- antonta.net. "After years of plain text accounting." 
- Beancount 文档 / 论坛.
- ItsFOSS (2024). "Git Isn't Just for Developers."
- jvns.ca (2023). "git rebase: what can go wrong."
- LowEndBox (2024). "Notion Will Ban Your Account."
- Mem.ai (2024). "Note-Taking App Graveyard."
- Hellman (2026, Medium). "Privacy-First Journaling Apps."
- Quillium / Curvenote / Upwelling 产品博客 (2024)。

---

> **诚实最终标记**：本笔记的核心结论"markdown + git（或 Obsidian-style 本地 markdown vault）是 σ 系统最契合的记录介质"是 U 级综合判断——它建立在多份 S/M 级原子证据上，但"汇总到这一具体推荐"本身没有 RCT 支持。Phase 2 Design 应当把它作为强假设接受，**保留可调整空间**——尤其是关于 GUI 包装、AI 触发时机、git 自动化封装的具体实现选择。本笔记完成本身**不**意味着技术栈已敲定——它意味着已识别出最强的设计需求清单（§3.1），让后续技术选型有评判依据。
