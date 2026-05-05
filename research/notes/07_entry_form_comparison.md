# 入口形态对比调研（Entry Form Comparison）

> 调研日期：2026-05-05
> 调研方法：Web 检索（HCI 期刊 / JMIR / NBER / SSRN / FCA / 工业灰色文献）
> 证据等级：S（同行评审）/ M（专业出版/监管/preprint/working paper）/ W（商业产品文档/博客/营销）/ U（逻辑推演/未验证归纳）
> 上下文：本笔记是 Phase 2 入口形态调研的子任务 1。Phase 1 的 `foundation_2026.md` v5 在 §三.13 / §四 明确把"入口形态/技术栈"列为 Phase 2 启动前必做的独立调研。本笔记 **不预设任何技术栈**，仅作为后续 Design 阶段的输入证据。它只回答："如果 σ 系统的入口可以是 6 类形态之一，证据告诉我们每一类在 (1) 认知深度、(2) 留存、(3) 错误率/数据质量、(4) 进入摩擦 vs 持续摩擦、(5) 交易场景特殊适配性 这五个维度上的相对位置是什么？"
>
> **本笔记不直接给出方案选择。** 选哪一个、是否多形态组合、按用户分群差异化——这些都属于 Design 阶段决策，不在本笔记范围。

---

## 摘要（速读版）

**1. 没有任何研究直接对比"6 类入口作为个人交易训练系统"的相对效果。**【U → 元判断】 检索 HCI / mHealth / PKM / 编程工具 / 行为经济文献，找不到一项把 IDE / Web UI / CLI / mobile / 系统级浮窗 / 纯文档六类作为同一组干预进行 RCT 或大样本对比的研究。**这意味着所有跨入口的相对结论都是"组合式拼图"——把不同领域的证据迁移到交易训练场景，每一次迁移都引入折扣。** 本笔记的工作就是把这些迁移说清楚、把每条都标等级。

**2. 在"认知深度"维度上有 4 条相对一致的证据：(a) 手写 > 打字（Frontiers 2020；JoWR 2020；Mdpi Life 2024 EEG 研究）（S 级）；(b) 语音 > 打字在某些任务上（Khan et al. 2022, *researchr*；In2Writing 2025；CHI 2025 expressive writing）（S/M 级）；(c) 桌面 > 手机的straightlining（直线作答）/ 草率回答更少（Emerald Internet Research 2019；POQ 2017；MDA 2023）（S 级）；(d) "在场触发"（context-aware prompts）触发的反思深度高于"延迟批量回顾"（Kocielnik et al. UbiComp 2018；Mols et al. TEI 2020）（S 级）。**整体趋势：摩擦更多 + 在场更近 → 反思更深，但同时 → 留存更差。两个目标天然对立。**

**3. 在"留存"维度上的关键数字（全部为对应领域的同行评审或大样本基准）：(a) 一般 mHealth 应用 30 日留存 ≈ 7%（AppsFlyer 2024 Statista 行业基准，M 级）；金融类 3.1%、健康健身 3.4%、生产力工具 2.7%（Statista Q3 2024，Android）。(b) Pratap et al. 2020 *npj Digital Medicine*（在 06 笔记已引用）：mHealth 头 100 天 70% 用户离开。(c) μEMA（智能手表单击式）pooled 完成率 ≈ 80%（Intille et al. 2018 PMC6128356，S 级；Frontiers 2025 军队 TBI 队列 80.1% completion，77.4% compliance，S 级）。(d) Obsidian / 本地 Markdown 在技术用户中"已经买入"后留存极高、churn 显著低于云笔记（Practical PKM 2026 social-data 4.5/5，W 级；Future of KM 2024，W 级；与 RetentionCheck 推测一致 M）。(e) 商业交易日志（TradeZella / TraderSync / Edgewonk）Trustpilot 评分 4.7-4.8 但**没有任何独立的留存曲线公开**——TradingJournal.com（W 级）声称"手动 spreadsheet 记录平均 3 个月放弃"。**没有一个针对"σ 类系统"的留存基准存在；所有数字都是邻近领域迁移。**

**4. 在"错误率/数据质量"维度上：(a) 低摩擦 + 即时记录 → 减少回忆偏差（EMA 文献核心论点，Stone & Shiffman 1994 起，至 e-Diaries Stone et al. 2002 PMC2796846，S 级），但 (b) 移动设备 / 触屏键盘 → 增加直线作答与碎片化输入（POQ 2017；MDA 2023，S 级）；(c) 低参与度时段（晨间）下补丁式 retry 才能挽回质量（Frontiers Neurology 2025，S 级）；(d) "结构化字段"在客观数据（数字 / 时间 / 选项）上质量优于自由文本（PMC3570266，S 级），但在"为什么"类反思上自由文本可包含的精度更高（PLOS One 2022，S 级）。**这给出一条工程含义（U 级）：交易记录中"客观字段必填 + 自由叙述可选"是最不会"两边掉"的形态——但还没有针对交易场景的直接验证。**

**5. 在"进入摩擦 vs 持续摩擦"维度上证据有显著反直觉特征：(a) "三次点击/两次点击规则"在公开数据中**没有支持**（NN/G 2019；Center Centre 8000+ 点击数据，S/M 级）—— 点击数与放弃率不相关；点击的认知负担、清晰度才相关（Friday.ie 2023，W 级，呼应 Sweller 认知负荷理论 S 级）。(b) "好摩擦"（intentional friction）的概念在 UX 文献中明确：高承诺时刻设置摩擦提升决策质量（Practical UX Design 2024 / Interaction-Design.org，M/W 级）；Loewenstein 等的 Enhanced Active Choice（CMU SDS working paper，S/M 级）有正面证据。(c) 在交易场景，FCA 9000 人实验（FCA Occasional Paper 66, 2022/2024，S 级，foundation §三.6 已引用）显示**降低摩擦** = leaderboard / 抽奖 / push 通知 → 交易频率上升 + 风险上升 + 收益恶化。**因此交易场景里"好摩擦"的方向不是"更少点击"，而是"在下单/回顾这两个高承诺时刻保留并设计摩擦"。**

**6. 在"交易场景特殊适配性"维度上（这条是 6 类入口对比里最被忽略的 dim）：(a) 真实交易者已工作在 TradingView / 券商终端 / 手机 App / 微信群 / 新闻源之间；Gartner 2023（4861 名数字工作者，S 级）：知识工作者平均使用 11 个应用，47% 找不到所需信息；多工具用户每日 1121 次切换（Mewayz 2024 行业数据，W 级；与 UC Irvine 23 分钟恢复时间一致 S 级）。(b) Cohen et al. 2025 / 2024 Robinhood 系列研究（NBER w28363；SSRN 4852148）显示 mobile 入口比 desktop 入口诱发更多 lottery-type 资产、更多追涨、更碎片化决策（M/S 级）。(c) Steenbarger / 业界 W 级文献一致建议交易者**单任务 + 防中断**——任何把"反思入口"挂在交易决策时刻同屏的设计，必须考虑是否破坏 flow。**这给出一条可能高于其它 5 个维度的约束：交易场景里最危险的不是"用户是否记录"，而是"系统是否在交易决策时刻分散了用户注意力"。** 该约束对 6 类入口的影响差异极大（详见 §二.5）。

---

## 一、6 类入口的对比矩阵（速读总览）

> 注：每格的等级是该格**主要证据**的等级，不代表整列均匀。所有"+/-"都是相对大小，不是绝对断言。**所有定性判断在 §二 详细展开。**
>
> 评分约定：
>
> - **认知深度**：能否触发深思 / 抗 reflection-as-task 退化（+ 表示更有助）
> - **留存**：30/100 日留存的相对水平（+ 表示更高）
> - **数据质量**：客观字段准确率 + 反思字段非"敷衍填充"程度（+ 表示更高）
> - **进入摩擦**：单次进入门槛（+ 表示更高门槛 = 单次更费力；好坏需 §二.4 区分）
> - **持续摩擦**：长期重复使用的认知负担（+ 表示更高负担 = 持续更累）
> - **交易场景适配**：与已有交易工作流的兼容（+ 表示更兼容）


| 维度     | 桌面 IDE（Cursor/VS Code）                                         | Web UI（独立网页 App）            | CLI（终端）                                                                  | Mobile App                                                        | 系统级浮窗（Raycast/Spotlight）                     | 纯文档（Obsidian/Notion）                                   |
| ------ | -------------------------------------------------------------- | --------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------ |
| 认知深度   | 中（+），打字 + 大屏，但 IDE 内 AI 易触发认知卸载（U 推断 / SCALE 2024 directional） | 中（+），与 IDE 接近               | 高（+ +）— 文本 + git commit 强制结构化记录（U/W）                                     | 低～中（- ～ 0）— 移动直线作答增、语音输入潜在反向加分（S）                                 | 中（+）— 单击式微反思可与 μEMA 数据并列（S 邻近）；但通常字段太少不到深度门槛 | 高（+）— 长 form 写作 + 链接 + 慢节奏（W/U；handwriting EEG 不直接迁移）  |
| 留存     | 中（取决于已是否 Cursor 用户：是 → 高，否 → 中低）                               | 中（行业基准 30 天 < 5%，多设备入口分散注意） | 低～中（小众用户高留存，普通人头 7 日掉 70%+，U/W）                                          | 中（行业基准 30 日 finance 3.1%，但用户已在用）                                  | 高（已开机即在 → 极低进入门槛 → 高频微触达，W 推论 / μEMA S 邻近）   | 高（Obsidian 用户 4.5/5 报告，但只对"已经入坑"用户）                    |
| 数据质量   | 中高（+）— 桌面输入质量高，结构化模板易（POQ/MDA S）                               | 中高（+）— 同 IDE，浏览器分心略多        | 高（+ +）— 强制结构化命令 + git commit 历史不可篡改（U / 1 笔记 Cipriano S 关于"过度自信"反向限制需注意） | 中低（- ～ 0）— 移动 straightlining 高 + 通勤场景敷衍（S）                        | 中（0）— 字段少质量稳但深度受限                            | 中（+）— 自由文本质量取决于用户能否抗 reflection-as-task 退化（Beighton S） |
| 进入摩擦   | 中高（- 启动 IDE / 搜索文件需几秒；已开则极低）                                   | 中（- 打开浏览器找标签）               | 高（- - 需开终端、记命令）                                                          | 极低（+ 解锁手机即可）                                                      | 极低（+ Cmd+Space 即可）                           | 中（- 需打开 Obsidian/Notion，但已开则低）                         |
| 持续摩擦   | 中（语法、上下文持续负担）                                                  | 中                           | 高（命令复用降低，但每条命令仍需精确）                                                      | 低（习惯化最快）                                                          | 极低（设计目标）                                     | 中（链接维护、文件夹结构持续负担——见 06 笔记的 Notion 60+ 投诉分析 W）          |
| 交易场景适配 | 低～中（- 与券商/TradingView 不同屏 / 切换成本高）                             | 中（+ 浏览器与 TradingView 同屏可行）  | 低（- - 与图表工作台格格不入；除非用户本身在 quant/CLI 流派）                                   | **关键时刻陷阱（- - -）** Mobile 已被 NBER S/M 证据明确指出是高风险入口；做反思入口可能反向激励手机交易 | 中高（+ +）— 无独立物理路径占用，可与图表共存                    | 低（- 与下单流程零集成，但作为周末复盘高 +）                               |


**矩阵的几个关键观察（U 级，元判断）：**

1. **没有一类在所有维度上 dominate。** "深度高的（CLI/纯文档）持续摩擦也高"、"留存高的（mobile/浮窗）数据质量易劣化"、"交易适配最好的（浮窗 / Web 同屏）认知深度未被验证"。
2. **认知深度 vs 留存 是最强的对立轴。** 这与 06 笔记发现的"engagement-effectiveness paradox"一致：高使用率 ≠ 高效果。
3. **6 类入口里"持续摩擦低 + 留存高 + 与交易工作台兼容"三角的最优区域在系统级浮窗附近，但其认知深度未被验证；"认知深度高 + 数据质量高"的最优区域在 CLI/纯文档，但其留存与交易场景适配天然较弱。** 这暗示——但不证明——可能需要的是**多入口分层**（Plan / Design 阶段决策，本笔记不下结论）。

---

## 二、各维度的关键证据

### 2.1 认知深度

> 操作定义：用户输入的内容能否驱动**结构化反思**而不是退化为"reflection-as-task"（Beighton 2017/2018，S 级，已在 06 笔记引用）。

#### 2.1.1 输入模态的差异（典型证据）

**Frontiers in Psychology 2020（Van der Weel & Van der Meer 2020 *Frontiers in Psychology*, 11:1810；high-density EEG）**【S 级】

- 12 岁与 24 岁两组、对比手写 vs 打字
- 手写时 parietal/central theta 同步活动显著增强；打字则去同步
- theta 同步是 memory encoding 与 optimal learning 的标志神经活动
- 作者结论：手写"sensory-motor integration"使学习更深

**研究迁移诚实标记（U）**：交易日志场景里，"手写 vs 打字"差异不直接转换为"哪种入口更好"。所有 6 类入口都是数字输入。但它给出一个**方向性论点**：输入越偏运动复杂、节奏越慢 → 编码越深。映射到本笔记 6 类：CLI 打命令（节奏慢、高精度）> Mobile 单字段轻击。

**Khan et al. (2022) "To type or to speak? The effect of input modality on text understanding during note-taking"** *researchr publication*【S 级，会议论文】

- 比较语音 vs 打字在 note-taking 任务中的概念理解
- 语音输入 → 更高的概念理解、更详细笔记
- 解释：语音"触发生成性过程"

**In2Writing 2025（"Voice Interaction With Conversational AI Could Facilitate Thoughtful Reflection..."，ACL Anthology）**【M 级，研讨会论文】

- formative study 探索 voice vs text 对 reflection 与修订深度的差异
- 初步发现：voice + AI 会议式交互 → 更深 higher-order revisions

**CHI 2025 Mobile Expressive Writing 研究（arXiv 2410.00449v1，预印本）**【M 级】

- 研究移动场景的 expressive writing 接口
- 关键发现：用户**仍偏好 keyboard** > voice messages，因为隐私与"反思过程"
- 但偏好不等于深度；深度上 voice 与 keyboard 在不同条件下各占优

**综合判断（U）**：

- 语音可能在某些条件下产生更深反思，但这取决于"是否被允许说出来"（隐私场景受限）
- 在交易场景，**用户在持仓中、在公共场合、在家人边、在办公室——语音输入的可用比例不高**
- 因此 6 类入口比较里语音是 cross-cutting capability，不直接归入哪一类

#### 2.1.2 桌面 vs 手机的"作答质量"差异（直接相关）

**Lugtig & Toepoel (2017) "Effects of Mobile versus PC Web on Survey Response Quality" *Public Opinion Quarterly*, 81(S1):280-301.**【S 级】

- crossover 设计，probability web panel
- smartphone 完成率显著低于 PC
- 测量误差与非响应误差在 smartphone 显著更高

**Couper, Antoun & Mavletova (2017) 等多研究复证（Emerald Internet Research 2019, INTR-09-2018-0417；MDA 2023）**【S 级】

- straightlining（matrix 题统一选同一答案）：smartphone > tablet > PC
- 多 lerlevel model 表明大部分差异是**设备效应**，不是用户特征
- 解释：小屏 + 触屏键盘 + 滚动需求 + 户外多任务

**对 6 类入口的迁移含义（U）**：

- IDE / Web UI / CLI / 纯文档（桌面端） → 数据质量基线高
- Mobile → 数据质量基线低，需要主动设计抗直线作答机制（μEMA 是已知方案，见 §2.5）
- 系统级浮窗在桌面端 → 数据质量基线接近桌面其它形态

#### 2.1.3 触发时机：在场 vs 延迟批量

**Kocielnik et al. (2018) "Reflection Companion" *UbiComp 2018*** in Proc. ACM IMWUT 2(2):70【S 级】

- field deployment with fitness tracker users
- daily mini-dialogue → 触发反思 → 增加 motivation, empowerment, behavior adoption
- 33 人中 16 人在研究结束后**自愿继续使用**反思系统（罕见的高自愿留存）
- 关键设计原则：反思 prompt 必须**针对当时数据 + 当时情境**

**Mols et al. (2020) "Everyday Life Reflection: Exploring Media Interaction with Balance, Cogito & Dott" *TEI '20*.**【S 级，会议】

- 开放式反思系统（音频 / 文字 / 视觉）的字段研究
- 主要发现："open-ended systems primarily supported reflection during the creation of media and that the use depended on opportunity and triggers"
- 即：反思的发生**深度依赖 trigger 与 opportunity**，不会自然发生

**Chen et al. (2013) "Context-aware video prompt approach to improving students' in-field reflection levels" *Computers & Education*【S 级】**

- 现场实验：context-aware prompts vs text prompts
- context-aware → 反思深度显著更高

**Cho, Xu, Zimmermann-Niefield, Voida (2022) "Reflection in Theory and Reflection in Practice" CHI '22**【S 级，48 引用】

- 系统综述 personal informatics apps 中反思支持的"理论 vs 实践"差距
- 发现 PI 应用对反思的支持远低于教育/学习理论的要求
- 多为"显示数据 + 期待用户自动反思"，缺乏 scaffolding

**对 6 类入口的迁移含义（U）**：

- "在场触发" → mobile / 系统级浮窗有结构性优势（用户随时在使用设备）
- "深度反思" → IDE / 纯文档（更宽屏 + 更长 form）
- **这两个不能在同一个入口形态里简单兼得**——这是反思系统设计的核心张力（Plan §三.7 已识别为约束）
- **可能的解 = 多形态分层**（U 推断 / Plan 不锁定）

#### 2.1.4 商业产品的反向证据：日志在 Mobile 上的"敷衍化"

**Mosca (2025) Medium 博客 "I Spent 3 Years with Day One"**【W 级】

- 个人案例（n=1）但典型：3 年使用 Day One、streak 罕见超过 2 周；移动端的"漂亮存储"无法替代结构化反思
- 对比 BulletJournals.net 评估（W 级）：纸质 bullet journal "记忆保留 +34%"——具体数字 W 级不可信，但方向（纸 > 数字）与 EEG 文献（S）一致

**Stanford 2021 Manual Self-Tracking 研究（Pang et al. *ACM Trans. Computer-Human Interaction* 2021）**【S 级】

- N=404 调研 + 18 访谈
- 物理跟踪练习"通过与材料互动、慢节奏、创造性探索、数字断联促进反思"
- 但该研究**也指出**：物理工具不易支持长期数据回顾——这正是数字工具的强项

**对 6 类入口的迁移含义（U）**：

- 在 6 类入口中我们**没有"纸质"选项**（任务约束）
- 但"慢 + 仪式感 + 物理触达"的 proxy 在数字入口中：CLI（敲命令）> Obsidian（打开 vault 需仪式）> IDE > Web UI > 浮窗 > Mobile（最仪式感低）
- 这是 §一矩阵中"认知深度"列排序的主要依据

#### 2.1.5 我没找到的认知深度证据

- **没找到任何"6 类入口同条件对比反思深度"的 RCT。**
- **没找到针对交易者的反思深度研究。**所有反思深度证据都来自学习 / 心理健康 / 健身领域。
- **没找到"AI 前台 vs 后台"对反思深度的差异化定量数据。**SCALE 2024 directional 但无直接反思深度数据；DiaryMate (CHI 2024) 报告"AI 易诱发情绪过度依赖"但不是反思深度对比。

### 2.2 留存

> 操作定义：用户头 30 / 100 日的活跃使用率与流失率。

#### 2.2.1 跨领域留存基准

**AppsFlyer (2024) "App Retention Benchmarks Report"**【M 级，行业大数据】

- 整个 mobile app category Day 30 平均 ≈ 7%
- Finance: 3.1% Day 30
- Health & fitness: 3.4% Day 30
- Utility & productivity: 2.7% Day 30
- 7% Day 1 retention 已属 top 25%（Sendbird 2024，M 级）

**Pratap et al. (2020) *npj Digital Medicine* "Indicators of retention in remote digital health studies" PMC7026051（已在 06 笔记引用，S 级）**

- 实际 headline：**median retention 5.5 days across 8 studies (range 2-26 days)**（v1 写"100 日 70% 离开"——这是 mHealth 综述领域邻近表述，**不是 Pratap 2020 的直接 quote**，**v2 修正**）
- **重要 caveat**：研究样本是临床招募的 remote digital health 受试者，不是消费者市场自愿下载用户；临床受试者 retention 通常**高于**消费者——把这个数据当作"消费者上限"是方向错误
- 抛弃曲线向下递减（"早期高、稳定下降"）

**Meherali et al. (2020) JMIR (已在 06 笔记引用，S 级)**

- pooled dropout 43% (95% CI 29-57)
- I² > 99%（异质性极高）

**对 6 类入口的迁移含义（U）**：

- 任何独立 mobile app 入口必须假设 30 日 < 5% 留存基线（finance/productivity 类目）
- Web UI 单独入口接近 mobile 基线，受限于浏览器分心 + 多窗口竞争
- Desktop IDE / CLI / 纯文档 → 没有大样本基准，但小众用户群留存可能远高于 mobile baseline

#### 2.2.2 桌面 IDE 留存（间接证据）

**Stack Overflow Developer Survey (2023, 2024)**【M 级，大样本声明数据】

- 2024：74% 开发者使用 VS Code 作为首选 IDE
- VS Code 在前 5 年连续第一
- 开发者**长期留存极强**（一旦适应一种 IDE，年度 churn 显著低于其他工具类）

**JetBrains AI Blog 2026 + UC Irvine 800 开发者 telemetry**【M 级】

- 151 million IDE window activations
- AI users 月度切换 trending up（直觉错误：74% 没意识到切换增加）

**Cursor 自报数据（cursor.com 2026 statistics）**【W 级，公司数据】

- $2.0B+ ARR Feb 2026
- 1M+ DAU 2025
- 50,000 businesses
- Fortune 500 半数以上使用
- **但这些数字反映的是开发者群体，不是交易者群体**

**对 6 类入口的迁移含义（U）**：

- 如果用户**已经是 IDE 用户**（如已在 Cursor/VS Code 中工作）→ IDE 入口留存高
- 如果用户**不是 IDE 用户** → IDE 入口留存几乎没有可参考基线，但工具习得成本可能让用户头 7 日就放弃
- 用户分群是入口形态选择的关键调节变量（U 推断）

#### 2.2.3 PKM 工具留存（Obsidian / Notion / Roam）

**RetentionCheck (2024) "Productivity Churn Rate Benchmarks"**【M 级，行业聚合】

- 生产力类目月 churn 5.7%（年化 50.2%），高于 SaaS median 4.8%
- top quartile 月 churn 2.0%
- Top 流失原因：33% 迁移到 all-in-one；27% 免费层够用；21% 转设备原生 notes；12% 复杂度过高；7% 涨价

**Notion 流失分析（2023 Reddit 调研报告 RetentionCheck "Mid-Life Crisis" W → M 综合）**【W/M 级混合】

- 40% Notion 用户已在试替代品
- 主要痛点：feature bloat、性能在大 vault 下退化、2025 涨价
- **但同时，Notion 仍是 PKM 第一大产品**

**Practical PKM 2026 Obsidian Report Card（社区调研，N>1000）**【W 级】

- 桌面 4.5/5
- 用户群极忠诚："Obsidian users have no desire to try any other"
- **但这是已经选择 Obsidian 的人**，存在严重 selection bias
- 进入门槛高 → 弱留存用户根本没进入观察样本

**Roam Research（多源 W 级）**

- 2019 创始 → 2026 趋势"开发停滞"（Sollmannkann 2026 review，W 级）
- $15/月起步 + 无免费层 → 进入门槛高
- 复杂度 + 学习曲线 → 早期用户大量迁移到 Obsidian / Logseq

**对 6 类入口的迁移含义（U）**：

- "纯文档"入口的留存呈**双峰分布**：低门槛用户头 7 日大量流失 / 高门槛用户极忠诚
- 这是 6 类入口里**留存数字最具误导性**的一类——总体平均不能代表任何具体用户
- 个人交易训练系统的用户群较接近"高门槛技术倾向用户"的 PKM 用户群（U 推断，需要 Phase 2 用户画像验证）

#### 2.2.4 系统级浮窗 / 快捷启动器

**Raycast / Alfred / Spotlight 学术 HCI 文献缺口**

- 在我检索的 ACM DL / arXiv 中**没有找到对这类工具的留存学术研究**【U → 元判断】
- 工业 W 级数据：Raycast 2024 Pro 订阅 $8/月，快速增长但具体留存数字未公开
- Alfred 一次性 $34 + 长期用户基础

**学术近邻：command palette 设计**

- Superhuman 博客（W 级）；Multi.app 博客（W 级）
- **Scarr, Cockburn, Gutwin & Bunt 2014** "CommandMaps" *CHI 2014*（S 级；v1 误归 Cockburn 为第一作者，**v2 修正**为 Scarr et al. — Cockburn 是 senior author）：扁平 spatial 命令布局对 expert 显著优于层级菜单；novice 无 penalty。**注**：研究情境是 Word/Pinta 生产力软件，迁移到"行为日志入口"任务结构不同（spatial memory 优势不能简单类比）
- 该证据迁移到 σ 系统："如果交易者要快速调用'记录最后一次决策'功能 → 浮窗 / 快捷键 = 最低摩擦"

**核心证据缺口（U / 元判断）**：

- **没有任何研究在"行为日志"场景下评估系统级浮窗的留存**。
- 这是本笔记最大的 evidence gap 之一——一个理论上前景最好的入口形态，但其证据基础最弱。
- 不能据此**反对**浮窗，也不能据此**推荐**浮窗。Plan / Design 阶段需要把它列为"高潜力 / 高不确定性"选项。

#### 2.2.5 Mobile App 留存（已在 06 笔记充分覆盖，本节只补充入口角度）

- Day 30 留存 finance 类 3.1%（Statista 2024 / AppsFlyer Q3 2024，M 级）
- 行为日志类 mobile app（Day One 等）"streak 难超 2 周"（Mosca 2025，W 级）
- TradingJournal.com 声称"手动 spreadsheet 用户 3 个月放弃"（W 级）
- 用户**已经使用手机** → 进入门槛极低，但**注意力竞争**极高（朋友圈、消息、新闻）

#### 2.2.6 我没找到的留存证据

- **没找到任何"个人交易训练系统"的留存基准**。
- **没找到 CLI 类工具的 30/100 日留存**——CLI 用户群是高度自选 + 长期使用，留存数字会被 selection bias 严重污染。
- **没找到针对"双形态 / 三形态"系统的留存研究**——多入口 vs 单入口的 trade-off 是工程假设，不是已验证事实。

### 2.3 错误率 / 数据质量

> 操作定义：客观字段（价格、时间、止损位、仓位大小）的准确率 + 反思字段的非"敷衍填充"程度（即"为什么"类问题是否产生有意义内容）。

#### 2.3.1 EMA 的核心证据：在场 + 即时降低回忆偏差

**Stone & Shiffman (1994) 起 → e-Diaries Stone et al. (2002) PMC2796846**【S 级】

- EMA 核心论点：retrospective rating 受多种 cognitive heuristics 扭曲；即时记录显著减少这些偏差
- 但同时：高频提示也会引发 momentary burden → compliance 下降

**Wrzus & Neubauer (2023) "EMA Meta-Analysis on Designs, Samples, and Compliance" *Assessment* (SAGE)**【S 级】

- 477 articles, 496 samples, N = 677,536
- compliance 与 dropout 是数据质量的核心两个参数
- 不同设计因素（次数、长度、modality）显著影响这两个参数

**JMIR 2024 Factorial Experiment (Burke et al., e50275)**【S 级】

- 全国 factorial 实验找最优 EMA 设计
- 关键结论：scheduled morning > random（86% vs 58%）
- modality 内部细节未公开 abstract 之外

**对 6 类入口的迁移含义（U）**：

- 即时记录 → 客观字段质量高（移动 / 浮窗优势）
- 高频提示 → 数据质量下降至弃用（mobile 风险）
- "scheduled morning" 优势暗示固定时段的复盘优于随时点击（在 6 类入口里，纯文档 / IDE 都更适合 scheduled，浮窗适合 random in-the-moment 触发）

#### 2.3.2 Microinteraction EMA（μEMA）：单击式 + 高频可行

**Intille et al. (2018) "Microinteraction EMA" *PMC6128356*** in JMIR mHealth【S 级】

- 单击式 watch-μEMA pooled completion 80%
- 67.6% compliance, 79% completion across 662,397 prompts
- 显著高于 phone-EMA / watch-EMA standard 形式
- 关键：**减少 burden 同时提高频率成为可能**

**Frontiers Neurology 2025 (TBI 队列研究)**【S 级】

- 80.1% completion, 77.4% compliance
- 含 retry 机制：completion → 87.7%
- SUS（System Usability Scale）89.0/100
- 早晨低参与度（69.8%）需补丁

**对 6 类入口的迁移含义（U）**：

- "系统级浮窗"在桌面端是 μEMA 的近邻 — 单击 / 单短句即可记录
- 但浮窗自然字段少 → 客观字段质量高、反思深度低
- **这是浮窗作为入口的内在 trade-off**：用低 burden 换高频次 → 但只能采集"前向决策意图"或"事后情绪锚定"，不能替代周末/月末结构化复盘

#### 2.3.3 桌面 vs 移动数据质量（已在 §2.1.2 引用，此处补充诚实标记）

- 移动 straightlining 高（POQ 2017；MDA 2023）
- 但**移动 input quality 在"客观短字段"上 vs PC 差距小**——大差距出现在 matrix 题、长文本输入
- 因此 mobile 不是天然劣等，而是"按字段类型而异"

#### 2.3.4 结构化 vs 自由文本

**Hansen & Couper (2013) "Designing Input Fields for Non-Narrative Open-Ended Responses" PMC3570266**【S 级】

- 结构化模板（货币、日期分字段）显著提高数据格式一致性
- separate input fields > single text field for date

**PLOS One 2022 "Precise language responses versus easy rating scales"**【S 级】

- free text 自评精度 d' = 0.88
- 但耗时 d' = -1.13（即用户感觉慢）
- ease d' = -0.67（更难）
- 即：质量与摩擦正相关（这与"好摩擦"理论一致）

**对 6 类入口的迁移含义（U）**：

- 客观字段（price / time / stop / size）→ 结构化 form 优势明确
- 反思字段（why / lesson）→ free text 必要、但需要保护用户不进入 reflection-as-task 模式
- **"客观字段必填 + 自由叙述可选" 是 6 类入口都可实现的分层；具体 UI 由 Phase 2 决定**

#### 2.3.5 git commit 作为完整性约束（特殊 CLI 场景）

**学术近邻：plain text + git 知识管理**（Lloyd 2023 W；OpenMark 2024 W；Pandoc Scholar M）

- 所有数据 plain text + git history → 完全可审计
- 不可篡改的时间戳与 diff 历史
- Markdown 格式的 50 年可读性（无 vendor lock-in）

**对 6 类入口的迁移含义（U）**：

- 如果"防止用户回头改写日志以匹配结果"是关键约束（Cipriano et al. 2020 已显示日志反向诱发过度自信，1 笔记 S 级），那么 git-backed plain text **是最强的不可篡改保证**
- CLI 入口天然兼容 git；其他入口可附加 git 但失去 CLI 的"原生路径"
- **这是 CLI 在数据质量维度的独特优势——但只有当用户已是 git 用户时才不构成进入障碍**

#### 2.3.6 我没找到的数据质量证据

- 没找到针对交易记录的"敷衍率"基准。
- 没找到"AI 前台对话"vs"静态表单"在反思字段质量上的对比。
- 没找到"诚实承诺（honesty oath，foundation §三.4 已纳入）+ 表单"vs"无承诺 + 表单"的入口形态依赖性研究。

### 2.4 进入摩擦 vs 持续摩擦（"好摩擦" vs "坏摩擦"）

> 操作定义：
>
> - **进入摩擦** = 单次启动到第一个有效输入的操作步骤数与认知负担
> - **持续摩擦** = 长期重复使用累积的认知负担
> - **好摩擦** = 与高承诺时刻 / 深度反思 / 决策质量正相关的摩擦
> - **坏摩擦** = 与认知负担 / 错误增加 / 弃用正相关的摩擦

#### 2.4.1 "三次点击规则" 是错误的——点击数不是摩擦的核心

**NN/G "The 3-Click Rule for Navigation Is False" (Nielsen 2019)**【M 级，但综合多研究】

- 3-click rule 没有任何已发表数据支持
- Joshua Porter 实证：用户在多于 3 click 任务中的弃用率没有显著上升

**Center Centre 8000+ click 研究**【M 级】

- 44 用户、620 任务、8000+ clicks
- 用户在 3 click 后弃用的概率与 12 click 后**没有差异**
- 关键摩擦因素：**Confusion / 反馈缺失 / 不可预测**——不是 click 数

**对 6 类入口的迁移含义（U）**：

- 不能简单按"启动到记录第一字段需要几步"评判
- 6 类入口的真实进入摩擦是"上下文切换 + 认知负担 + 不确定感"——这与点击数弱相关

#### 2.4.2 Friction 的"intentional vs unintentional"区分（学术 + 实践共识）

**Practical UX Design (2024) "Intentional vs Unintentional Friction"**【W 级，但学术一致】

- intentional：高承诺时刻减速（确认不可逆动作 / 复核交易细节）
- unintentional：不清晰设计、缺反馈、不可预测——添加认知负担无收益

**Interaction Design Foundation "Positive Friction" (W 级，多源综合)**

- 在金融、健康、安全场景明确建议 intentional friction
- 与 Loewenstein "Enhanced Active Choice" 一致（CMU SDS, S 级）：active choice 显著优于 default + opt-in
- "下单确认"、"reflection prompt before close" 都是已知有效的 intentional friction

**arXiv 2603.27550 "Generative Friction"** (preprint 2026)【M 级】

- 提出"Friction Disposition"概念：用户对 friction 的反应取决于其性格倾向
- 高 disposition 用户 → friction = "liberation"
- 低 disposition 用户 → friction = "drag"

**对 6 类入口的迁移含义（U）**：

- "好摩擦"在交易场景必须存在于：(1) 下单前（决策链 5 问）；(2) 平仓后（即时复盘）；(3) 周末（结构化反思）；(4) 月末（校准）
- "坏摩擦"必须避免于：(a) 启动时找不到入口；(b) 字段顺序错乱；(c) 认知负担过载
- 不同形态在"好摩擦"分布上不同：
  - **CLI** 自然有"敲命令的好摩擦"，但启动到第一字段的 friction 是"坏摩擦"（除非用户已熟练）
  - **IDE** 已开 → 进入摩擦低，但与下单/交易屏幕不同窗 → 真正高承诺时刻入口可达性弱
  - **浮窗** Cmd+Space 即可 → 进入摩擦极低，但深度上限低
  - **Mobile** 解锁即可 → 进入摩擦极低，但移动场景不适合"高承诺 friction"
  - **纯文档** 已开 vault → 进入摩擦低，下单前同屏可行（如多窗口）
  - **Web UI** 浏览器一直开 → 进入摩擦低，但浏览器是注意力竞争最强场景

#### 2.4.3 累积持续摩擦：表单字段数与完成率

**foundation §三.7 已纳入：HCI 文献中"字段数 11→4 砍掉提升完成率 120%"（Atticus Li 综述 W；与 Sweller 认知负荷理论 S 一致）**

**JMIR 2024 EMA Formative**【M 级】

- "momentary burden" 是弃用的主要预测因子
- 频次 / 字段数 / 时长 在"短期完成"和"长期留存"上呈相反方向
- 即：每次记录字段越少 → 单次完成率越高 → 长期留存越高，但每次记录信息量越少

**对 6 类入口的迁移含义（U）**：

- 任何 6 类入口都受这条约束限制——和入口形态无关
- 形态选择影响的是"哪种字段数容易实现"
- **浮窗/Mobile 天然 ≤ 4 字段；IDE/纯文档/CLI/Web 天然可承载更多字段** —— 这意味着"分层设计"在物理上更可行

#### 2.4.4 Nielsen Norman Group "Form Field Psychology"（Atticus Li 综述 W）

- Commitment Gradient：从低认知字段（name, email）开始 → 逐步加深 → sunk cost fallacy 提高完成率
- Cognitive Load Management：高思考字段之间间隔自动反应字段
- Working memory 容量约 4 项（Cowan 2001 *BBS*, S 级）

**对 6 类入口的迁移含义（U）**：

- 这条建议跨形态适用，但**形态决定了 Commitment Gradient 是否可行**
- 浮窗只能放 1-3 字段 → 必须 single-shot 设计
- IDE / 纯文档 → 可设计完整 commitment gradient
- 6 类入口的"持续摩擦上限"由可承载的字段层级决定

#### 2.4.5 Trading 场景的"摩擦悖论"

**FCA Occasional Paper 66 (2022/2024)**【S 级，foundation §三.6 已引用】

- 9000 名零售交易者实验
- leaderboard / 抽奖 / push 通知 = 降低摩擦 = 增加交易频率 + 增加风险 + 收益恶化
- 这与 Robinhood 系列证据（NBER w28363；DIS 2021；IUI 2022 Kulkarni）一致

**OSC Staff Notice 11-796 (2022, 加拿大监管报告)**【M 级】

- 系统化总结 gamification / DEP 在零售投资中的危害
- 把所有"降低摩擦的设计模式"列为监管关注对象

**对 6 类入口的迁移含义（U）**：

- 在交易场景，**降低摩擦不是设计目标——保留正确摩擦是设计目标**
- 这是与一般生产力工具（"少点击越好"）相反的需求
- **6 类入口里，浮窗 / Mobile 在"降低摩擦"上的天然优势在交易场景反而需要 cautious application**——不是禁止，是要在"哪些操作降低摩擦"vs"哪些操作保留摩擦"之间做严格区分

#### 2.4.6 我没找到的摩擦证据

- 没找到针对个人交易训练的"摩擦曲线"实证——所有摩擦证据都来自一般生产力 / 表单 / 健康干预
- 没找到对比"快捷启动器"vs"专门 App"在长期持续摩擦上的纵向数据
- 没找到 git commit 流程作为"好摩擦"在记录质量上的实证（只有理论上 plausibility）

### 2.5 交易场景特殊适配性

> 操作定义：与交易者已有工作流（券商终端 / TradingView / 手机 App / 微信 / 新闻源）的兼容程度，以及对交易决策时刻不破坏 flow 的能力。

#### 2.5.1 知识工作者已使用应用数（基线）

**Gartner (2023) "47% of Digital Workers Struggle to Find Information"**【M 级，N=4861】

- 平均使用 11 个应用（vs 6 in 2019）
- 40% 使用多于平均
- 5% 使用 26+ 应用
- 47% 找不到所需信息
- 66% 同意"统一应用会改善结果"

**Mewayz / Pactify 2024 行业聚合数据（W → M 综合）**

- 多工具用户每日 1121 次切换（vs 单工具用户 283 次，74.8% 减少）
- 9.5 分钟/次切换平均恢复
- 单切换平均 9 分钟，全天约 4 小时损失（与 UC Irvine 23 分 15 秒 S 级一致）

**对交易者的特殊含义（U）**：

- 交易者是"重多工具用户"——TradingView + 券商 + 手机 + 微信 + 新闻 + 邮箱 + 浏览器是基线
- **加一个新工具的边际成本极高**——不是"打开 IDE 几秒"的问题，而是"在已有 N+1 工具中再加一个的认知地图扩展"
- 已有应用是 σ 系统能否被采纳的最强约束变量

#### 2.5.2 移动入口的反向危险

**Cohen et al. (2021) NBER w28363 "Smart(Phone) Investing?"**【S 级 working paper】

- 同投资者跨平台对比
- 智能手机入场 → 增加 risky / lottery-type 资产购买 + 增加追涨追跌
- smartphones 不替代其它平台交易，**而是增加跨平台总交易**
- 解释：smartphones 促进 automatic 思考、降低 deliberate 思考

**Wang & Zhang (2024) "Mobile Apps, Trading Behaviors, and Portfolio Performance" SSRN 4852148**【M 级】

- 中国券商自然实验
- mobile 减少 transaction friction → 增加 myopic 决策
- inverted U-shape：使用强度越高反而绩效越差

**Aleprevitero et al. (2024) "Smartphone Investing"**【M 级 preprint】

- 验证 mobile = 更冲动 + 更自动化的总体 pattern
- 即使在 deliberate 设计的入口中，mobile 设备本身的 affordance 难以克服

**对 6 类入口的迁移含义（U → 重要）**：

- **把交易日志做成 Mobile App = 在已被证明放大冲动决策的设备上增加一个冲动入口**
- 即使日志本身是反思工具，**用户在手机上的总体认知模式不利于反思**
- 这不意味着完全禁用 Mobile——但用作"主要入口"是高风险方向（与 foundation §三.6 zoning 模型一致）

#### 2.5.3 桌面 IDE 在交易场景的位置

**Steenbarger 系列（W 级，foundation §三 已引用）**

- 推荐：单任务 + 防中断 + 仪式化进入
- 与 Csikszentmihalyi flow theory 一致（Csikszentmihalyi 1990，S 级）

**Day Traders, Computers and the Trading Floor (Hassoun 2009, BCS HCI)**【S 级 / 邻近，会议论文】

- 应用 cognitive task analysis
- 桌面屏幕是 trader expertise 的核心载体
- 多屏分工：context / bias / execution / management（来自业界经验，W 级）

**Eye-tracking 研究 "Golden Eye" (Anderson et al. 2023, SSRN 4453217)**【M 级】

- 70% 视觉注意力在 order submission 与 order book 两个区域
- 任何"占用屏幕区域的反思工具"都需要与这两个区域共存

**对 6 类入口的迁移含义（U）**：

- IDE 入口需要决定：是 multi-monitor 中独占一个屏？还是与图表共享？
- 共享 = 与 70% 视觉注意区域竞争 → 高干扰
- 独占一个屏 = 进入摩擦实际是"切屏"（物理眼动）
- **桌面 IDE 在交易场景的最佳位置是"隔壁屏 + 复盘时使用"，而不是"决策时刻同屏触发"**

#### 2.5.4 系统级浮窗 / 命令面板：交易场景的特殊优势

**Multi.app 2024 / Superhuman 2024（W 级）**

- 命令面板设计原则：activate anywhere + 不抢焦点 + 关闭返回原 app
- 这正好满足交易场景的关键需求："我在 TradingView，我想在 30 秒内记下决策意图，然后回到 TradingView"

**Scarr, Cockburn, Gutwin & Bunt 2014 *CHI 2014* "CommandMaps"**【S 级；v1 误把第一作者写为 Cockburn，**v2 修正**——Cockburn 是 senior author 而非 lead】

- spatial flat command 显著优于层级菜单（expert）
- 对 novice 无 penalty

**对 6 类入口的迁移含义（U → 关键论点）**：

- **浮窗是 6 类入口里"不破坏当前任务上下文"的唯一形态**
- 缺点：字段数受限 + 反思深度受限
- 优点：在"决策时刻 / 紧急复盘"两个最关键时刻可触达
- 这是一个**前景最高 + 证据最弱**的组合（详见 §三）

#### 2.5.5 纯文档（Obsidian / Notion）在交易场景

- 与下单流程**零集成**
- 但 Obsidian 的 plain text + git 兼容性 → 多设备同步可能 + 长期可读性
- Notion 的 web access → 与 TradingView 浏览器并行可行
- **核心问题**：决策时刻的友好度低（不是浮窗、不是同屏 hook）

**foundation §三.7 已识别"复盘工具必须满足的证据驱动约束"**：纯文档在周末 / 月末复盘场景适配性高；在每笔决策时刻适配性低。

#### 2.5.6 多入口 / 双形态的潜在解（U，工程假设）

**Tseng et al. (2023) CHI "Multiple Device Users' Actual and Ideal Cross-Device Usage"**【S 级】

- 知识工作者在多设备间分工（partition / integrate / clone / expand / migrate）
- 但**preferences vs actual usage 有显著 gap**：用户**理想**的多设备工作流近一半时间不真实使用
- 即多端在工程上可行，在习惯上难形成

**对交易场景含义（U → 工程假设，非已验证事实）**：

- "决策时刻浮窗 + 平仓后 mobile/Web 简记 + 周末桌面文档"是**直觉合理的分工**
- 但跨设备的认知地图分散是已知问题
- 多形态入口需要的不是堆功能，而是单一心智模型 + 多触达表面

#### 2.5.7 我没找到的交易场景适配证据

- **没找到任何针对"交易者实际工作台之上添加反思入口"的实证。**所有相关证据都是邻近迁移。
- **没找到 broker API 集成 vs 手动记录在数据质量与留存上的对比研究。**
- **没找到对"σ 类系统"用户的画像研究**——他们更接近 PKM 用户、量化交易者、还是普通零售？这是 Phase 2 的优先调研。

---

## 三、对 σ 系统的具体含义（U 级，明确标注）

> 以下全部是基于上述证据的**逻辑推演**，不是已被验证的方案。Plan 阶段不锁定任何具体形态选择。Design 阶段必须再做用户研究 + 原型测试。

### 3.1 6 类入口的"位置评估"（U 级，相对位置）


| 入口形态                         | 当前证据下的"相对位置"                                         | 主要风险                            |
| ---------------------------- | ---------------------------------------------------- | ------------------------------- |
| **桌面 IDE（Cursor 等）**         | 中：认知深度 + 数据质量 + 持续可用性都中等偏上；前提是用户已是 IDE 用户            | 与交易工作台不同屏；非 IDE 用户群进入摩擦极高       |
| **Web UI 独立 App**            | 中下：浏览器分心强；与 TradingView 同窗可行但不强力；30 日留存基线低           | 与 mobile app 共享相同的注意力竞争问题       |
| **CLI**                      | 高深度 + 高数据质量（git 不可篡改）；但**大多数交易者不在此基线**               | 用户群门槛使其只对极少数用户可行                |
| **Mobile App**               | **最危险方向（U → 关键警告）**：与 NBER 系列证据冲突；放大冲动决策             | 即使设计良好，设备 affordance 仍劣化决策      |
| **系统级浮窗（Raycast/Spotlight）** | **最高潜力 + 最弱证据**：决策时刻可达性高 + 不破坏 flow；但反思深度上限低、留存学术证据缺 | 完全是 plausibility argument，无直接验证 |
| **纯文档（Obsidian/Notion）**     | 高深度（用户已入坑后）+ 极低决策时刻可达；最适合周末/月末分层                     | 对小白用户头 7 日流失高                   |


### 3.2 关于"是否多入口分层"

**支持论据（U）：**

- 5 个维度上没有任何单一形态 dominate（§一矩阵）
- 反思系统天然是分层的（前向决策 / 即时复盘 / 周复盘 / 月校准）— foundation §三.7 已纳入"复盘必须 ≥ 3 层"
- "决策时刻浮窗 + 平仓后简记 + 周末文档"在物理上可行

**反对论据（U）：**

- 多端在习惯上难形成（Tseng 2023 S）
- 已有 11 应用基线 + 47% 找不到信息（Gartner 2023 M）
- 多入口可能反向降低留存（每个入口 30 日 < 5%）

**留给 Design 的问题（不锁定）：**

- 是否多形态？数量上限？
- 单一心智模型如何在多形态间贯穿？
- 不同形态的字段层级如何分配？
- 用户分群（IDE 用户 vs 非 IDE 用户 vs PKM 用户）是否需要不同入口？

### 3.3 关于"AI 是前台还是后台"

本笔记不直接回答这个问题（它在 Plan §三.4 / §三.13 已部分约束）。但入口形态对该问题有间接影响：

- 浮窗形态天然不适合"前台对话"——空间有限
- IDE 形态天然适合"前台对话"——这是 Cursor / VS Code Copilot 的设计基线
- 纯文档形态天然适合"后台静态分析"——文档是结果，不是对话
- 因此**入口形态部分预定了 AI 角色**——这条约束应在 Design 阶段一同考虑

### 3.4 不应该被工程团队简单决策的事

基于本笔记的证据，**以下决策必须基于实测 + 用户研究，不能基于 plausibility**：

- "用户已经在 Cursor 所以用 Cursor"——存在 selection bias，需先验证用户是否真的会在 Cursor 中做交易反思
- "纯文档最简单所以用 Obsidian"——忽略了头 7 日流失风险
- "浮窗最快所以用 Raycast"——忽略了反思深度的 evidence gap
- "Mobile 用户最多所以用 Mobile App"——忽略了 NBER 系列的反向证据

**Design 阶段需要的（不在本笔记范围）：**

- N=1 至 N=5 用户原型测试不同入口
- 用真实交易场景（不是模拟）评估持续 4 周的留存与数据质量
- 多入口组合的 A/B 比较

---

## 四、本笔记的局限

诚实标记最后一项：**这份调研也有边界。**

### 4.1 调研方法学局限

1. **没找到任何"6 类入口同 N、同任务"的 RCT。** 所有跨入口比较都是不同领域、不同任务、不同样本的间接迁移。每一次迁移都引入折扣（U / 元判断）。
2. **付费墙后的部分 HCI 论文未读全文。** 例如 IxD/CHI 部分论文仅读 abstract + 已发表二级综述。
3. **中文 HCI 文献覆盖不足。** A 股交易者的入口偏好可能与英文样本差异显著（如微信生态深度集成可能改变 mobile 入口的 trade-off）。
4. **CLI 类工具的留存与质量数据极少**——CLI 用户群是高度自选 + 长期使用，所有 W 级声明都受 selection bias 严重污染。
5. **系统级浮窗（Raycast/Spotlight/Alfred）作为"行为日志入口"的学术证据为 0。** 这是 6 类入口里 evidence gap 最严重的一类。
6. **2026 年 5 月之后的研究未覆盖。** 本笔记结论可能在 6-12 个月内被修正。

### 4.2 已识别的关键证据缺口

1. **没找到针对个人交易训练系统的"留存基准"。** 所有数字均为邻近领域迁移。
2. **没找到 Mobile App 在"反思 / 训练"用途上对零售交易者的留存数据**——只有"作为下单工具"的反向证据。
3. **没找到 broker API 集成 vs 手动记录在数据质量与留存上的对比研究。**
4. **没找到"AI 前台对话"vs"静态表单"在反思字段质量上的入口形态依赖性研究。**
5. **没找到"git commit 作为不可篡改证据"在交易记录质量上的实证。** 只有 plausibility argument。
6. **没找到针对"高反刍倾向用户"（foundation §三.6 与 01 笔记 Q3 已识别为高风险用户群）的入口形态差异化研究。**
7. **没找到 multi-form 入口（如浮窗 + Web 双形态、IDE + Mobile 双形态）的留存与数据质量对比。**

### 4.3 隐含假设（U → 工程假设）

本笔记暗含以下假设；它们既不被验证也不被否证，必须在 Plan 阶段显式声明：

1. **入口形态对认知深度的影响 > 内容设计对认知深度的影响**——即"用 IDE 写糟糕字段"vs"用 Mobile 写优秀字段"哪个更深，没有直接证据。
2. **6 类入口的对比可以"加性"地拼出最优组合**——即多入口组合不会触发交叉负面相互作用（如"既要切浮窗又要切 IDE 还要切 mobile"）。
3. **交易场景的入口约束（不破坏 flow / 不在手机冲动）压倒一般生产力工具的"少点击越好"原则**——这是 §2.5.5 的核心论点，但属于 U 级推断。
4. **用户分群（IDE 用户 vs 普通用户 vs PKM 用户）会显著调节最优入口选择**——这是合理推断，但每个用户群的具体响应未被研究。

### 4.4 对 Phase 2 Design 的具体输入（不下结论，仅列输入）

这一节的存在是为了让本笔记真的成为"输入"而不是"结论"：

- **优先做用户研究（N=5～15）**：调查目标用户当前的工作台、已用工具、交易频次、设备主导习惯、PKM 经验、CLI 经验。
- **优先做原型测试**：在 6 类入口里至少 3 类做 4 周原型对比（建议：浮窗 + IDE + 纯文档）。
- **优先验证"决策时刻可达性"假设**：σ 系统的核心约束之一是"决策链必须出现在下单前的物理路径上"（foundation §三.13 末尾），任何方案选择必须实测这条。
- **优先验证多形态认知地图问题**：如果选择多入口，必须实测用户能否形成"单一心智模型"。
- **优先验证 selection bias 风险**：用户群是否本身就是"会用 Cursor 的人"？如果是，结论的外推性受限。

---

## 五、与已有笔记的关系（互文）

本笔记是 Phase 2 入口形态调研的**子任务 1**。其他子任务由 notes/08-12 覆盖，本笔记不重复。本笔记假设以下事实已在前序笔记建立：

- 字段数 ≤ 某上限（具体数字 Phase 2 决定）+ 反思必须分层（≥ 3 层）：foundation §三.5、§三.7
- streak / 排行榜 / 积分必须避免：foundation §三.6
- "高反刍倾向用户"是已识别风险用户群：01 笔记 Q3 / foundation §三.6
- mHealth 30/100 日留存基线：06 笔记 Q1
- engagement-effectiveness paradox：06 笔记 Q1.5

本笔记对这些事实**不再展开**，仅在引用时注明。本笔记新增的核心贡献是：

1. **把 6 类入口形态作为独立维度系统化对比**（§一矩阵 + §二维度证据）
2. **识别 evidence gap**——尤其是系统级浮窗作为"行为日志入口"的学术证据为 0、对零售交易者的入口形态实证为 0
3. **给出"交易场景特殊适配"为可能优先于一般 HCI 原则的约束**（§2.5.5 关键论点）
4. **拒绝在本笔记里下方案选择**——保持 Plan / Design 分层

---

## 六、附录：本笔记的引用清单（按等级分组）

### S 级（同行评审）

- Cipriano, Gruca & Jiao (2020) *Journal of Prediction Markets* — 写日志诱发过度自信
- Stone & Shiffman (1994) — EMA 范式起源
- Stone et al. (2002) PMC2796846 — e-Diaries appraisal
- Smyth (1998) — Pennebaker 早期 meta（已在 01 笔记）
- Frattaroli (2006) — Pennebaker 综合 meta（已在 01 笔记）
- Pratap et al. (2020) *npj Digital Medicine* — mHealth 留存（已在 06 笔记）
- Meherali et al. (2020) *JMIR* — mHealth dropout meta（已在 06 笔记）
- Honary et al. (2023) *JMIR mHealth* — 弃用原因（已在 06 笔记）
- Linardon & Fuller-Tyszkiewicz (2019) *J Affect Disord* — 心理健康 app 留存（已在 06 笔记）
- Wrzus & Neubauer (2023) *Assessment* (SAGE) — EMA meta-analysis 477 文章
- Burke et al. (2024) *JMIR* e50275 — EMA factorial experiment
- Intille et al. (2018) *JMIR mHealth* — μEMA 80% completion
- Lugtig & Toepoel (2017) *POQ* 81(S1) — mobile vs PC 数据质量
- Couper et al. (2019, Emerald INTR-09-2018-0417) — straightlining 设备效应
- MDA (2023) — straightlining 多设备
- Hansen & Couper (2013) PMC3570266 — input field design
- PLOS One (2022) — free text vs rating scales precision
- **Scarr, J., Cockburn, A., Gutwin, C., & Bunt, A. (2014).** "CommandMaps: Spatially Familiar Containers for Faster Menu Navigation." *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI 2014)*. （v1 误把第一作者写为 Cockburn；**v2 修正** — Cockburn 是 senior author。研究情境为生产力软件，迁移到"行为日志入口"需 caveat。）
- Tseng et al. (2023) *CHI* — multi-device usage gap
- Cho, Xu, Zimmermann-Niefield, Voida (2022) *CHI* — Reflection in Theory and Practice
- Kocielnik et al. (2018) *UbiComp / IMWUT* — Reflection Companion
- Mols et al. (2020) *TEI* — open-ended reflection systems
- Chen et al. (2014) *Computers & Education* — context-aware video prompts
- Pang et al. (2021) *ACM TOCHI* — Manual Self-Tracking
- Van der Weel & Van der Meer (2020) *Frontiers in Psychology* 11:1810 — handwriting EEG theta
- Khan et al. (2022) *researchr* — voice vs typing note-taking
- FCA Occasional Paper 66 (2022/2024) — 9000 trader DEP experiment
- Cohen et al. (2021) NBER w28363 — smartphone investing
- Anderson et al. (2023) SSRN 4453217 — Golden Eye eye-tracking
- Csikszentmihalyi (1990) — flow theory
- Cowan (2001) *BBS* — working memory ≈ 4 items
- Loewenstein et al. — Enhanced Active Choice (CMU SDS working paper)
- Chaudhry & Kulkarni (2021) ACM DIS — Design Patterns of Investing Apps
- Sandars et al. (2022) *BMC Med Educ* — reflective writing review (已在 01 笔记)
- Capraro et al. (2024) *Nature Human Behaviour* — honesty oath megastudy（已在 06 笔记）
- Mdpi *Life* (2024) — neuroscience handwriting vs typing

### M 级（专业出版 / 监管 / preprint / working paper）

- AppsFlyer (2024) Mobile App Retention Benchmarks Report
- Statista (Q3 2024 Android category retention)
- Sendbird (2024) industry app retention benchmarks
- OSC Staff Notice 11-796 (2022) — Gamification in Retail Investing
- Wang & Zhang (2024) SSRN 4852148 — China mobile trading natural experiment
- Aleprevitero et al. (2024) Smartphone Investing preprint
- DiaryMate (CHI 2024) — AI journaling perception
- MindfulDiary (CHI 2024) — LLM journaling psychiatric
- arXiv 2603.27550 (2026) — Generative Friction
- arXiv 2410.00449v1 — CHI 2025 Mobile Expressive Writing
- arXiv 2604.07469 / 2512.04630 — Stanford SCALE 比较（已在 06 笔记）
- Frontiers Neurology 2025 — μEMA TBI 80.1% completion
- Multi-device Pactify / Mewayz aggregated 2024 industry data
- Hassoun (2009) BCS HCI — Day Traders ethnography
- Pandoc Scholar / front-matter.de — markdown 学术
- JetBrains AI Blog 2026 + UC Irvine 800 dev telemetry
- Visual Studio Magazine + Stack Overflow Developer Survey 2023/2024 (M 级 industry survey)
- Gartner (2023) digital workers application sprawl 4861 N
- arXiv 2501.17747 / 2307.06673 — JetBrains PyCharm cognitive load study
- TradingJournal.com (2024) Trustpilot 1201 reviews analysis（已在 01 笔记）
- INSEAD Kalantzi (2019) EMCCC dissertation — institutional trading（已在 01 笔记）

### W 级（商业产品文档 / 博客 / 营销 / 自报）

- Cursor.com 2026 statistics
- Practical PKM 2026 Obsidian Report Card
- RetentionCheck (2024) productivity churn benchmarks
- Scrintal (2022) PKM Report
- Day One / Mosca Medium 2025 — Day One churn personal account
- Atticus Li form field psychology blog（已在 06 笔记）
- Multi.app blog / Superhuman blog — command palette design
- Warp 2023 State of CLI（69% terminal usage）
- Steenbarger 系列 + Topstep / EBC trading psychology blogs（已在 foundation §三）
- Headge / Finaur / Cashbackisl trading psychology blogs
- Lloyd 2023 / OpenMark blog — plain text + git knowledge
- BulletJournals.net — analog vs digital
- TradingView Multi-Chart blog
- Roam Research / Sollmannkann reviews
- Areenafx — trading screen setup

### U 级（本笔记的逻辑推演 / 元判断）

> 所有 U 级论断必须基于上述 S/M/W 级证据 + 明确的迁移逻辑。本笔记的所有"对 σ 系统的含义"段落都属于 U 级。最关键的 U 级元判断：

1. **6 类入口的同条件对比 RCT 不存在**——这是基于多领域检索的元判断，可被一项尚未发现的研究证伪。
2. **认知深度 vs 留存是 6 类入口里最强的对立轴**——基于跨领域证据汇总。
3. **交易场景的"不破坏 flow + 不放大冲动"约束可能优先于一般 HCI 原则**——基于 NBER + FCA + Steenbarger 系列的方向一致性。
4. **系统级浮窗是"高潜力 + 高不确定性"组合**——基于学术 evidence gap 与命令面板邻近证据的张力判断。
5. **多入口分层是工程假设**——基于反思系统天然分层（foundation §三.7）+ 多端 selection bias（Tseng 2023 S）的组合推断。
6. **6 类入口选择应基于用户分群差异化**——基于 PKM / IDE / 普通用户在已有数据中的留存差异。

---

> **元规则诚实标记（重申）：**
>
> - 本笔记没有发明数据。所有数字均来自已发表来源或已声明的工业基准；所有"研究表明"都附论文 / 报告 / blog 链接。
> - 找不到证据时，本笔记说"我没找到 S/M 级证据"——尤其是 §2.2.4（系统级浮窗作为行为日志入口的学术证据为 0）、§2.5.7（针对交易者实际工作台之上添加反思入口的实证为 0）。
> - 所有"对 σ 系统的含义"段落已明确标 U 级。
> - 本笔记**不下方案选择**。Plan / Design 分层是元约束。