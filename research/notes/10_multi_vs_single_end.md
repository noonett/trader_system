# 多端 vs 单端部署证据调研

> 调研日期：2026-05-05
> 调研方法：Web 检索（JMIR / npj Digital Medicine / J Med Internet Res / PLOS One / Survey Practice / J Pediatr Psychol / SSRN / NBER / FCA / CHI / HCI 灰色文献）
> 证据等级：S（同行评审 RCT / 元分析）/ M（监管 / 工作论文 / 大型行业数据）/ W（行业博客 / 营销 / 用户论坛）/ U（基于已知文献的逻辑推演）
> 上下文：Phase 2 入口形态调研子任务 4。Phase 1 已结束（foundation_2026.md v5），Phase 2 不预设技术栈。本笔记是"多端 vs 单端"证据调研，与子任务 1-3 互相独立。

---

## 摘要

**一句话结论**：在 mHealth、EMA、学习管理、习惯形成、个人生产力领域，**没有任何同行评审证据表明"部署更多端能提升完成率、留存、或数据质量"**——已有的少数直接对比反而显示：（a）增加设备类别（如手机+穿戴）对依从性**没有提升**（Heron et al., 2017，p=.36，S 级）；（b）智能手机相对桌面会**缩短开放式记录长度 10-22 字符**（Revilla et al., 2016，S 级）；（c）多端同步是**已知的数据完整性失败模式**而非默认收益（Habitica 多端同步 bug 列表 / 健康数据 last-write-wins 协议研究，M-W 级）。同时，唯一一项严格的"同内容、不同部署形态"RCT（Jiang et al., 2025，J Particip Med，S 级）显示真正决定留存与依从的不是"多少端"，而是**该端的行为科学设计**——具体说，"行为设计的原生 App">"同公司的网页"≈"第三方网页"，且差距比所有跨端比较都大。

**核心发现（5 条）：**

1. 【**S**】**"多端 ≠ 高依从"**：mEMA 元分析中 mobile-only（77.4%）vs mobile+wearable（73.0%）依从率**无显著差异**（Heron, Everhart, McHale, Smyth, 2017, *J Pediatr Psychol*，p=.36）。新增设备类别没有依从收益，反而轻微下降。
2. 【**S**】**部署形态决定留存的是"该端的设计"，不是"端的数量"**：在 Jiang et al. (2025, *J Particip Med*) 的 4 臂 RCT（N=284）中，相同内容下同一公司的 ePRO 移动 App vs 同公司网页 vs 第三方网页 vs 纸质，移动 App 依从率显著高于其他 3 臂（Cohen's t=2.42 至 4.53，p≤.02）。原因是行为设计（reward / identity / 推送），不是"端多端少"。
3. 【**S**】**移动端在长文本与精确反思上有结构性劣势**：Revilla et al. (2016) 跨平台实验中，开放式问题在 PC 上比未优化智能手机平均**多输入 10.9-22.4 字符**（p=.00）；移动端中位完成时间显著更长，且第三方在场率高 ~10pp（27% vs 19.8%）。Mizrachi 等（Nature Sci Rep 2022）：手机阅读 → 前额叶过度激活 + 理解力下降。
4. 【**S/M**】**移动端在"交易"场景中是已被证伪的"训练端"**：Kalda, Loos, Previtero, Hackethal (2024 *Rev Finance*) + FCA (2024) 一致显示，移动端会显著推高交易频率、推高风险偏好、降低投资组合 Sharpe。**这是迁移到 σ 系统的最严重红灯——任何把"训练系统"放进与交易 App 同一台手机的设计，都会受到这种"把决策日志手机化 → 决策也被手机化"的污染。**
5. 【**S/M/W 三层一致**】**多端同步是工程已知的数据完整性故障模式**：Last-write-wins 协议在 Health Connect / Apple Health / Fitbit 等真实部署里反复触发"重复 / 缺失 / 冲突"（M+W 级）；Habitica 多端同步导致"两份数据"GitHub bug 持续多年未解（M-W 级）；CRDT 比 LWW 高 23.7pp 一致性，但实现复杂度极高（M 级）。**自建一个用 N-of-1 单用户的多端同步、然后期待数据"自动一致"——是对自己工程能力的过度乐观估计。**

**主要不确定性：**

- 没有任何针对**交易日志**的多端 vs 单端 RCT。所有迁移都是从邻近领域（mHealth、EMA、习惯）推演。
- 没有针对"日间桌面 + 盘后手机异步复盘"的直接同行评审研究——这种工作流形态只在产品博客中描述（W 级），未被实证。
- "单端起步、后扩展"的 phased rollout 在公共卫生干预里有 M 级支持，但没人在交易日志领域验证。
- 商业交易日志产品（Edgewonk / TraderSync / TradeZella / Tradervue）的"用户成功案例"全部为内部市场推广（W 级）；他们的部署形态选择反映的是工程便利度，不是循证决策。

---

## 一、多端 vs 单端对比矩阵

> 基于本调研的 5 个维度，对**单端起步**与**多端起步**两条路径做证据对比。每格标证据等级与方向（→ 利好哪一侧）。

| 维度 | 单端起步 | 多端起步 | 证据净结论 |
|---|---|---|---|
| **完成率** | mEMA 元分析单端 mobile 依从 77.4%（Heron 2017，S）；single-device minimal app（one sec, MinimalistPhone）有效（PNAS 2023, S）→ 利好 | mEMA mobile+wearable 依从 73.0%（同元分析），下降 4.4pp 且 p=.36 → 不利 | **S 级证据：单端无劣势，可能微小利好**。增设备无依从增益。 |
| **留存** | 在 Jiang 2025 RCT 中，"移动 App 单端 + 行为设计"留存最高（与同公司网页 t=−1.75, 与第三方网页 t=0.49 相当或更优）→ 利好 | 没有任何研究证明多端比单端留存高（搜索后未发现） → 中性偏负 | **S 级：单端 + 良好设计 ≥ 多端**。"多端"本身不是留存因素。 |
| **数据一致性** | 单端无同步问题，只有备份问题 → 强利好 | LWW 协议导致 Fitbit ↔ Apple Health 删除水分摄入（W-M 级证据，已确认 bug）；CRDT 99.7% vs LWW 76% 一致性（M 级）；Habitica 多端 GitHub bugs（M-W 级） | **M 级：多端引入新的失败模式**。除非投入大量同步工程，否则数据完整性下降。 |
| **认知碎片化** | "哪里方便用哪里"无法发生 → 强制深度记录 | Microsoft Research Devices@Home (CHI 2022)：用户跨设备产生 5 种碎片化模式（partition/integrate/clone/expand/migrate），任务继续性是已知 HCI 难题 → 中性偏负 | **M 级：多端默认导致工作流碎片化**。除非显式设计任务继续性。 |
| **用户体验/维护** | 单平台发布、单测试矩阵、单 UX → 利好 | 跨平台维护成本：QA 团队 ×3、UI 60% 不一致率（W 级营销综述，2026）、性能调优指数级增长（W 级） → 不利 | **W-M 级：多端工程成本是单端 1.5-3 倍**，对单人/N-of-1 项目尤其致命。 |
| **特殊议题：交易场景** | 单端（仅桌面）→ 与已知"移动 App 推高交易频率/风险"证据一致 | 加手机镜像 → 把"训练系统的入口"嵌入"已被证伪是有害决策环境"的设备 | **S 级：交易场景下多端有特殊危险**。Kalda 2024、FCA 2024 一致。 |

**对比净结论：在所有 6 个维度中，单端在 5/6 上证据更强或同等；多端只在"用户在外随时可记"的便利性上略占优势——而这一点正是交易场景里需要主动抑制的（对应 02 笔记的高频交易诅咒）。**

---

## 二、各维度的关键证据

### 2.1 完成率

#### 2.1.1 Heron 等：mobile-only vs mobile+wearable 元分析

**Heron, K. E., Everhart, R. S., McHale, S. M., & Smyth, J. M. (2017). "Compliance With Mobile Ecological Momentary Assessment Protocols in Children and Adolescents: A Systematic Review and Meta-Analysis." *Journal of Pediatric Psychology*, 42(10).** 【S】

- 加权平均依从率 78.3%（青少年 EMA）
- 关键对比：**仅手机平台依从率 77.4% vs 手机+穿戴 73.0%，p=.36**
- 解读：增加设备类别**没有依从增益**，且方向是轻微下降。
- 方法学限制：是元分析层面的非随机分组（不是 RCT 比较），所以"无差异"≠"等效"。但这是这个领域里能找到的最直接的对照。

**对 σ 的迁移（U 级）**：交易者已经有"桌面 + 手机"两个设备的工作流。如果 Heron 的方向有效，把训练系统再做成跨这两端，最乐观情况下是"无收益"；最悲观情况下是"轻微依从下降 + 工程负担显著上升"。

#### 2.1.2 Jiang 等：同内容、不同部署形态的 4 臂 RCT

**Jiang, X., Timmons, M., Boroda, E., & Onakomaiya, M. (2025). "Impact of Platform Design and Usability on Adherence and Retention: Randomized Web- and Mobile-Based Longitudinal Study." *Journal of Participatory Medicine*, 17:e50225.** 【S，强证据】

- N=284，4 臂随机：DCH 移动 App / DCH 网页 / 第三方网页 / 纸质
- **同样的问卷内容**，6 个月每周一次
- 留存（F<sub>9,255</sub>=4.22, p<.001）：
 - 移动 App vs 纸质 t=−3.80, p<.001（移动留存显著更高）
 - 移动 App vs DCH 网页 t=−1.75, p=.08（趋势性差异）
 - 移动 App vs 第三方网页 t=0.49, p=.63（无差异）
- 依从率（F<sub>9,162</sub>=5.5, p<.001）：
 - 移动 App > DCH 网页（t=−2.42, p=.02）
 - 移动 App > 第三方网页（t=−3.56, p<.001）
 - 移动 App > 纸质（t=−4.53, p<.001）
- **关键解释**：差异不是因为"端的数量"，而是因为**移动 App 内嵌的行为设计要素**（reward / identity / 推送 / avatar / 进度可视化）。三个非 App 臂没有这些要素。

**对 σ 的迁移**：
- 如果你只能选一个端做 σ 的入口，**应该选"能承载行为设计"的那一个**，而不是"用户最常打开的那一个"。
- 这两个候选大部分时候是不同的。
- "在所有端发同一份内容"的表面公平 = 实际依从率被最弱端拖累。

#### 2.1.3 单设备最简化干预的反向证据

**Pieh, T., et al. (2023). "Directing smartphone use through the self-nudge app one sec." *PNAS*.** 【S】+ MinimalistPhone（2024 ScienceDirect）【S】

- one sec：单手机 + 极简化设计 → 第一周减少目标 App 打开 37%，6 周减少 57%
- 关键发现：**"提供放弃选项"是最有效要素**，而不是"覆盖更多设备"。
- 解读：单端 + 减法设计 > 多端 + 加法设计。

### 2.2 留存

#### 2.2.1 mHealth 整体留存基线（已在 06 笔记建立）

**Meherali, S., et al. (2020). *J Med Internet Res*, 22(9):e20283** 【S】

- pooled dropout 43%（95% CI 29-57）
- 100 天内 70% 用户离开（Pratap et al., 2020）
- **该领域留存 ceiling 极低，与端数无关**

#### 2.2.2 Linardon & Fuller-Tyszkiewicz（2019）

【S】心理健康 App 短期 attrition 24.1%、长期 35.5%。**没有"单端 vs 多端"作为预测变量**——这本身是个信号：如果端的数量是重要因素，元分析作者们应该讨论它。它没出现，说明在数据中找不到稳定关系。

#### 2.2.3 JTrack-EMA+：跨平台部署的真实留存

**Sahandi Far, M., et al. (2025). "Cross-Platform Ecological Momentary Assessment App (JTrack-EMA+)." *J Med Internet Res*, 27:e51689.** 【S】

- 6 个月平均依从 49.3%
- **从 66.7%（第 1 月）跌到 42%（第 6 月），p=.004**
- 这个 App 是 Flutter 跨平台（iOS + Android），属于"多端"实现，但留存曲线与单端 mHealth 完全一致——**跨平台的工程能力没买到任何留存**。

**结论**：跨平台开发解决了"开发者维护成本"问题（部分），但**没有解决留存问题**。把"用 React Native / Flutter 多端发布"等同于"提升留存"是对工具本质的误解。

#### 2.2.4 Duolingo 多端的真实数据【M-W】

- 50% 课程在 Android 完成（说明用户**自然分布在最便利的设备**）。【M】
- Duolingo 自己的 case study 显示 39% 入门级 Android 用户加载时间 >5s → 他们优化的是**单端体验**，不是"加更多端"。【M】
- 结论：行业老大（Duolingo）的实战策略也是"先把每个端各自做好"，而不是"用统一的多端架构"。

### 2.3 数据一致性 / 碎片化

#### 2.3.1 健康数据多端同步的真实失败模式

**Wellally Tech（2024）"Architecting Offline-First Health Apps: A Deep Dive into Data Synchronization Patterns"** 【M】

- LWW（Last-Write-Wins）协议在并发编辑时一致性 76%
- CRDT（Conflict-free Replicated Data Types）一致性 99.7%
- **CRDT 实现成本：开源库 + 大量调试 + 数据模型重构**

#### 2.3.2 Fitbit ↔ Apple Health 删除水摄入的具体案例【W-M】

- Fitbit 同步 Apple Health 后，用户记录的水分摄入被自动删除。
- 原因链：（a）单位归一化（"16 oz" → "473.176 mL"）；（b）跨平台 ID 没有持久化；（c）权限不对称（Apple Health 只给第三方读权限）。
- **这是一个真实部署、有数据库工程团队、有上千万用户的产品里的 bug**。

**对 σ 的迁移**：单人项目自建多端同步，遇到此类 bug 的概率不会更低。诚实承认自己不会比 Fitbit 工程团队更聪明。

#### 2.3.3 Habitica 多端的具体故障【M-W】

- 数据压缩：旧任务历史被合并为单条目（GitHub Issue #8070, 2016 → 2018 关闭未实现）
- 时间戳不精确：导出仅含 cron 时间，不含完成时间
- 多端"两份数据"bug（Issue #4313）

**这些不是"边缘 bug"——这些是一个支持 iOS+Android+Web 的"成熟"开源习惯追踪器**在被广泛使用 10+ 年后的状态。

#### 2.3.4 数据一致性对训练系统的隐含含义【U】

如果 σ 系统记录的是"决策时刻的真实状态 + 复盘时的诚实评分"，那么：
- 同一笔交易出现两次（同步冲突），会让用户**怀疑系统的可靠性**。
- 部分字段缺失，会让 AI 分析得出错误结论。
- 时间戳错乱，会让"决策 → 执行 → 复盘"的因果链断裂。
- **这些不是"如果发生"，是"必然发生"**——只是频率问题。

### 2.4 认知碎片化

#### 2.4.1 Microsoft Research：跨设备使用的 5 种模式【M】

**Devices@Home (CHI 2022) + Cross-Device Taxonomy (Microsoft Research)**

5 种跨设备工作流模式：
1. **Partition**：把任务在不同设备间分割（A 在桌面、B 在手机）
2. **Integrate**：多设备协同完成同一任务
3. **Clone**：在另一设备上复制任务
4. **Expand**：用多设备扩展同一任务的输入/输出
5. **Migrate**：在设备间迁移任务

**核心 insight**：用户在多设备世界里花大量精力做"任务搬运"——这本身是认知负担。Mozilla Task Continuity（2015）识别 3 阶段（Discover / Hold-Push / Recover），并明确指出**隐私、定制、感知、排除、故障排除**是已知的未解决障碍。

#### 2.4.2 多端 → "哪里方便用哪里" → 单一深度记录被稀释【U + 部分 S 支持】

**Revilla et al. (2016) "PCs versus Smartphones in Answering Web Surveys: Does the Device Make a Difference?" *Survey Practice*** 【S】

- 智能手机用户开放式问题字符数显著少于 PC（10.9-22.4 字符差，p=.00）
- 智能手机用户中位完成时间更长，且优化版（SO）vs 非优化版（SNO）差异显著
- 第三方在场率：手机 27.0% vs PC 19.8%（wave 1, p=.00）
- IMC（注意力检查）合规率：SO 88.8% vs PC 89.0% vs SNO 81.6%（p<.001）
- **在场社会环境对反思深度的影响——手机更易在 27% 的场合有他人在场**

**Mizrachi et al. (2022) Nature Sci Rep**：手机阅读 → 前额叶过度激活、阅读理解下降。

**对 σ 的迁移**：决策链 5 问、复盘日记类的"反思深度"任务在手机上**结构性受损**。如果系统在多端都开放写入，用户的天然路径会是"在最便利的设备（手机）做最浅的填空"，从而把整个反思系统降级为"打卡"。这正是 06 笔记里识别的"reflection-as-task"风险，被多端部署放大。

#### 2.4.3 切换成本的不一致证据

【S，混合证据】Multi-tasking 与设备切换的关系研究方向不一致：
- Springer 2022 大样本研究：**重度多任务用户与切换成本无显著相关**（无证据支持"多任务者代价更高"假说）。
- Sciencedirect 2018：**低自我调节的重度多任务用户在自由切换条件下表现更差**（自我调节为关键调节变量）。
- Nature Reviews Neuroscience 2022：神经层面，"快速泛化 ↔ 多任务低成本"是 trade-off。

**净结论**：多端切换的认知代价**不能假设为零**，但精确大小依赖于个体的自我调节能力。对一个自评"小白"的交易学习者，这个调节能力**不应当假设为高**。

### 2.5 用户体验 / 维护成本

#### 2.5.1 跨平台开发的隐性成本【W-M】

**Allen Pike (2021) "The Persistent Gravity of Cross Platform"** + Likasoft + Netguru + MoldStud（2024-2026 综合）

- 名义代码复用节省 30-50%
- 实际隐藏成本：QA 团队规模 ×3、调试复杂度指数增长、UI 60% 案例视觉不一致、性能调优需要在代码 + 框架 + runtime 三层同时优化
- **小团队（3-6 人）做原生多端可控；大团队反而是跨平台更优**——但这个逻辑对**N=1 的个人项目**意味着：跨平台框架的维护成本在你的体量上，是"开始即陷阱"

#### 2.5.2 单设备最简化设计的有效性【S】

- one sec（PNAS 2023）：3 个最简要素（提示文字 + 短延迟 + 放弃选项），其中"放弃选项"是最有效组件。**复杂度增加没有收益**。
- 数字 CBT 失眠干预 RCT（npj Digital Medicine 2025 *factorial RCT*）：简化的 GUI 提升所有 4 个参与度指标（自评参与度、睡眠日志活动、登录频率、可用性）。【S】

**对 σ 的迁移**：在留存证据指向"简化"的领域里，"我们要支持 Web + iOS + Android + Desktop"是反方向的设计选择。

#### 2.5.3 单端起步的实施科学证据【M】

**TARGET integrated care program（IJIC 2024）** + **Nutrition Now Phase 2 Protocol（Frontiers Public Health 2023）**

- 起步规模 7 个 pilot site → 扩展到 100+ site
- 关键洞察："**先小、后大**"的 phased rollout 是公共卫生干预里被反复验证的最佳实践
- 单端单地起步可以在迭代中识别真实问题，而多端多地起步把问题隐藏在更多噪声里

---

## 三、特殊议题：交易场景的多端工作流

### 3.1 交易者已有的双端环境

**事实陈述**【M】：A 股零售交易者绝大多数已有：
- 桌面（看盘软件如同花顺、东方财富 PC 版、TradingView）
- 手机 App（券商 App、看盘 App）

加一个独立的训练系统时，候选有 4 种：
1. **仅桌面（Web 或独立桌面 App）**
2. **仅手机**
3. **仅 Cursor / 终端（书写型工具）**
4. **桌面 + 手机镜像**

### 3.2 移动端在交易场景的特殊红灯

**Kalda, Loos, Previtero, Hackethal (2024). "Smartphone Investing." *Review of Finance*（也作 NBER WP 27036 早期版本）.** 【S】

- 自然实验：用户从桌面切换到移动端 → 显著推高交易频率
- 移动端购买的资产：lottery-type、风险更高、过去赢家或输家、组合分散度更低
- 业绩后果：移动端买入资产的回报率更低，组合 Sharpe 比下降
- 强度关系：U 型曲线，过度使用 App 反而让业绩更差

**FCA Research Note (2024). "Digital Engagement Practices: A Trading Apps Experiment."** 【M，监管级】

- 9000 人实验
- DEPs（推送、leaderboard、积分）显著推高交易频率与风险
- 效应在低金融素养、女性、18-34 岁人群中更强

**Kalda et al. (2021) "Smartphone Trading Technology, Investor Behavior, and Financial Fragility." SSRN 3424405.** 【M】

- 移动 App 让"自我控制问题"和过度自信被放大

#### 这意味着什么

**交易者本身已经处于"被移动端伤害的环境"**。这与一般的健康/学习场景**完全不同**：在那些场景里，移动端是"提供便利的工具"；在交易场景里，**移动端是已经被实证为有害的决策环境**。

**核心推论（U + S 支撑）**：把训练系统部署到手机上 = 把"用来纠正决策错误的工具"嵌入"系统性诱发决策错误的设备"。无论 App 内部多么"严肃"，它都会从外部的设备文化（推送、上下滑动、即时反馈）中继承认知模式。

### 3.3 异步多端工作流（"日间桌面 + 盘后手机复盘"）

**搜索结果（W-U 级）**：在公开同行评审文献中，**没有针对这种工作流的实证研究**。

候选论据：
- **支持方（W 级）**：commercial trading journal 营销文案声称"用户日内做笔记 / 收盘后手机回看"是常见模式（Edgewonk、TradeZella 博客）；intuitively 让用户在通勤路上回顾。
- **反对方（S 级）**：
 - 决策链 5 问、复盘是高反思深度任务 → Revilla 2016 + Mizrachi 2022 表明手机端反思深度结构性受损。
 - 移动端反向激励（Kalda + FCA）使"盘后手机复盘"成为重新进入"被诱发的决策模式"的入口。
 - 时间继续性研究（Mozilla 2015）显示跨设备任务恢复成本不为零。

**净判断（U 级）**：异步多端工作流的"声称收益"是 W 级的、未经验证的；它的"已知风险"是 S 级的、有实证基础的。**风险/收益不对称**。

### 3.4 商业交易日志产品的部署形态调查【M-W】

| 产品 | 部署形态 | 关键观察 |
|---|---|---|
| **Edgewonk** | 历史桌面 → 2024 转 Web，无原生移动 App | 选择"网页化"而非"多端化"，工程便利度驱动 |
| **TraderSync** | Web + 原生 iOS/Android（仅 Elite $79.95 层） | 移动 App 仅高价用户使用 → 实际用户 base 是"主要桌面"模式 |
| **TradeZella** | 响应式 Web，无原生 App | 单端（Web）但响应式覆盖移动浏览器 |
| **Tradervue** | 仅 Web，无移动 App | 公司明确转向"engagement over acquisition"策略 |

**观察**：
- 4 家头部产品中 3 家选择 **Web-first 或 Web-only**；只有 TraderSync 在最高价层提供原生移动。
- **没有一家选择"原生移动 App + 原生桌面 App"的双端镜像**。
- 行业用脚投票的结果：**Web 单端 > 多原生端**。这背后是工程成本理性，但也间接表明"多端不是必需"。

**【元规则诚实标记】**：这是 4 家公司各自独立决策的归纳，它们的选择驱动因素是商业（开发成本 / 市场覆盖），不是循证（用户实证收益）。但它至少表明"多端"在该领域不是默认假设。

### 3.5 桌面环境对交易复盘的天然适配性【U+M】

**支持桌面起步的论据（U 级，但与多个 S 级证据兼容）**：
- 复盘需要看 K 线图、对比多个时间框架、写较长文字 → 桌面适配（大屏幕、键盘输入）
- 桌面是用户已有的"工作模式"环境（TradingView / 同花顺 PC 版打开时已是"交易工作时间"），减少 context switching 成本
- 复盘频率低（每周一次结构化、每月一次校准），不需要"随时随地"
- Web/桌面允许较长开放问题（Revilla 2016 显示长文本端利好）
- 写入即决策、复盘即审视——这些都是"严肃任务"，不是"通勤刷一刷"

**反对桌面单端的论据**：
- 用户在不在桌面前时无法记录瞬时情绪（"刚被止损时的状态"）→ 这确实是个真实痛点
- 部分场景：午休、地铁、出差

**但这个痛点被两件事削弱**：
1. σ 系统的核心是**决策链（开仓前）+ 结构化复盘（事后）**，不是"瞬时情绪记录"。决策链发生在用户面前已经有桌面看盘的时刻；结构化复盘不要求即时性。
2. 如果坚持要捕捉瞬时情绪，可以用最低限度的"备忘录文字粘贴 → 桌面整合"流程，不需要完整的多端 App。

---

## 四、对 σ 系统的具体含义（U 级）

> **【元规则诚实标记】**：本节是基于二、三节证据的逻辑推演，不是直接的研究结论。所有判断都标 U 级，可能在 Phase 2 实施中被实际数据修正。

### 4.1 核心建议：σ 系统应当**单端起步**

**【U，置信 ≈ 75%】**

理由：
1. 没有证据表明多端能提升完成率/留存（2.1, 2.2）
2. 有证据表明多端引入数据完整性风险（2.3）
3. 多端引入工程维护负担，对 N=1 项目尤为致命（2.5.1）
4. 在交易场景下，移动端不是中性工具而是已知风险源（3.2）
5. 商业产品的归纳规律也指向 Web/桌面单端为主（3.4）
6. 单端 + 良好设计 ≥ 多端 + 平庸设计（Jiang 2025 关键 RCT 提供 S 级支撑）
7. 公共卫生实施科学的"先小后大"原则（2.5.3）

**置信不到 100% 的原因**：
- 没有交易日志领域的直接 RCT，所有迁移都有不确定性
- "单端 vs 多端"在不同人群可能有异质效应
- 用户的具体使用习惯（如长期出差、移动办公）可能改变最佳形态

### 4.2 应该选哪个端？候选评估

**【U】** 在 4 个候选中：

| 候选 | 优 | 劣 | 净判断 |
|---|---|---|---|
| **仅桌面 Web** | 长文本、大屏幕、对反思任务友好；用户已在桌面交易；与商业产品归纳一致 | 离开桌面无法记录 | **首选** |
| **仅 Cursor / 终端** | 极低工程成本、可由 AI 直接读写文件、与决策链 5 问的"if-then 形式"高度兼容 | 学习曲线陡；用户群（小白）门槛过高 | **备选 / 双轨** |
| **仅手机** | 便携 | 反思深度受损；与移动端交易危害同环境；触发"打卡心态" | **明确不选** |
| **桌面 + 手机** | "随处可记" | 同步成本、数据碎片化、维护负担、无证据收益 | **明确不选**（这是本笔记最强结论之一） |

**【U，置信 ≈ 70%】**：σ 系统起步形态应在"Cursor/终端"和"桌面 Web App"之间二选一，根据用户的技术亲和度决定。**不应当是手机端、不应当是多端**。

> **诚实标记**：这个结论在交易日志领域没有直接 RCT 支持。它是基于 6 个跨领域 S/M/W 级证据流的逻辑汇集。任何在 Phase 2 实施中得到的实测数据（连续 30 天的真实使用率、记录字段质量、复盘完成率）都应该有权推翻这个结论。

### 4.3 对 foundation_2026.md §三.13 的具体补充建议（U 级）

> **【写在前面】**：本笔记不修改 foundation_2026.md。以下是供 Phase 2 Design 决策者参考的补充信号。

1. **入口形态约束应明确"单端起步、不预设多端"**——不是工程上的"暂时不做"，是设计原则上的"刻意不做"。
2. **如果未来要扩展到第二端，应当先有 N-of-1 数据证明"用户在 Phase 2 实测中遇到了真实的、单端解决不了的痛点"**——而不是"多端听起来更现代化"。
3. **明确禁止把 σ 部署到与交易 App 同一台手机的设计**（哪怕只是 PWA）——这是 3.2 节 S 级证据的直接含义。
4. **跨设备同步、原生 iOS/Android、跨平台框架（Flutter/React Native）等应当在 Phase 2 Design 阶段被显式列为"非约束"**——不是"也可以做"，而是"在没有数据支持前不应做"。

### 4.4 对"日间桌面 + 盘后手机复盘"工作流的判断（U 级）

**【U，置信 ≈ 70%】不应支持。**

理由汇总：
- W 级声称收益（"用户喜欢通勤复盘"）vs S 级已知风险（移动端反思受损 + 移动端交易心理放大）
- 异步工作流增加同步复杂度
- σ 系统的核心动作（决策链、结构化复盘）不需要这种工作流即可完成
- "盘后手机复盘"在心理上恰好把训练系统的边界**模糊**到交易 App 旁边——这是反向激励

**保留的少数情形**：如果 Phase 2 实测发现"用户因为桌面端不可达而错过结构化复盘"频率高（>20% 错过率），且其他干预（如桌面端定时提醒、周末 batch）无效——只有此时才应考虑加移动端。**默认假设是不需要**。

### 4.5 与已有调研的相互一致性检查

| 来源 | 本笔记结论的兼容性 |
|---|---|
| **notes/01 (journaling)** | 兼容：日志范式整体没被验证，组件分散有效 → 单端单一深度记录 > 多端浅层记录 |
| **notes/02 (retail failure)** | 兼容：手机交易已被实证有害 → 训练系统不应在手机上 |
| **notes/03 (AI coaching)** | 兼容：AI 辅助分析需要长上下文 → 桌面端长文本输入更适配 |
| **notes/04 (deliberate practice)** | 兼容：刻意练习需要专注无干扰环境 → 单端 + 桌面 > 多端 + 手机 |
| **notes/05 (alternative paradigms)** | 兼容：替代范式的多数实现也是单端起步 |
| **notes/06 (tool design retention)** | **强兼容**：06 笔记的"反对长 streak / 排行榜 / 全字段反思"全部需要"工具不在手机上"作为前提；06 笔记的"if-then implementation intentions"在桌面键盘输入下质量高于手机 |
| **foundation_2026.md v5** | 兼容：v5 已经把"入口形态"留给 Phase 2，并明确"不追求每天打开 30 分钟"——这与单端、严肃、桌面定位一致 |

**净判断**：本笔记的"单端起步、桌面/Cursor 优先、不要手机"建议与已有 6 份调研**全部方向一致，未发现冲突**。

---

## 五、本笔记的局限

### 5.1 没有直接证据的领域

**【明确盲区】**：

1. **交易日志领域无任何"单端 vs 多端"RCT**。所有结论都是从 mHealth / EMA / 学习 App 迁移。迁移有效性需打折。
2. **没有针对中国用户、A 股 / 港股交易者的部署形态研究**。所有引用都来自欧美/日本样本，文化适应性未知。
3. **没有 LMS（学习管理系统）跨设备完成率的同行评审 RCT**——只找到二级综述。
4. **没有"Cursor / 终端 / IDE 类工具作为 σ 入口"的实证研究**——这是本笔记建议的备选，但完全没有证据基础，是 U 级假设。

### 5.2 证据强度不对称

**支撑"不要多端"的 S 级证据较多**（Heron 2017、Jiang 2025、Revilla 2016、Kalda 2024、PNAS one sec、npj Digital Medicine 2025 factorial）。

**支撑"应该单端"的 S 级证据较少**——更多是"多端没显示出收益 + 单端没显示出劣势"的**默认逻辑**。这是经典的"缺乏证据 ≠ 证明无效"问题。

**应该谨慎对待的部分**：本笔记 4.1 的 "75% 置信" 是**元认知校准型估计**，不是统计推导。具体数值在 ±15pp 内都属于合理范围。

### 5.3 "异步多端工作流"研究空白

我反复搜索 "day-trading desktop + after-hours mobile review"、"trader async cross-device journaling"、"asynchronous multi-device workflow" 等组合，**没有找到任何同行评审研究**。这种工作流形态只存在于产品博客中（W 级）。

**结论**：σ 系统的"异步多端"决策无法基于直接证据。本笔记 4.4 的判断是基于邻近领域证据的推演，应当被 Phase 2 实测推翻或确认。

### 5.4 商业产品归纳的局限

3.4 节的 4 家头部公司选择 Web-first，是 M-W 级证据。它表明：
- ✅ 多端不是行业默认
- ❌ 但这不直接证明 Web 单端"对用户更好"——它可能仅仅证明"Web 单端对开发者更便宜"

诚实标记：商业归纳只能告诉你"行业的 Schelling point 在哪里"，不能告诉你"这个 Schelling point 是不是用户最优"。

### 5.5 个体差异未被本笔记充分讨论

**已知调节变量**：
- 自我调节能力（Sciencedirect 2018 多任务研究）
- 反思倾向（Cambridge Behaviour Change 2024 journaling）
- 出差/移动办公比例（U）
- 设备熟练度（U）

如果用户是"低自我调节 + 高反思倾向 + 主要桌面办公"，单端桌面是明显最优；
如果用户是"高自我调节 + 低反思倾向 + 频繁出差"，可能多端有边际收益。

**本笔记的结论假设的是 σ 系统的目标用户群（自评小白、A 股零售）更接近前者。如果实际用户偏离该 profile，结论的稳定性下降。**

### 5.6 未做的搜索方向

由于时间约束，本笔记**未深入**的方向：
- 残障/可访问性视角（多端是否对盲人/手部障碍用户必要）
- 跨文化（中国/亚洲用户的设备使用习惯）
- 时间维度（未来 5 年设备生态变化）
- 隐私/数据主权（多端是否引入新的隐私风险）

这些方向如果有强证据，可能会改变本笔记的部分子结论。

---

## 附录 A：关键引用（按证据等级）

### S 级（同行评审 RCT / 元分析）

1. **Heron, K. E., Everhart, R. S., McHale, S. M., & Smyth, J. M. (2017).** "Compliance With Mobile Ecological Momentary Assessment Protocols in Children and Adolescents: A Systematic Review and Meta-Analysis." *J Pediatr Psychol*, 42(10). PubMed 28446418.
2. **Jiang, X., Timmons, M., Boroda, E., & Onakomaiya, M. (2025).** "Impact of Platform Design and Usability on Adherence and Retention." *J Particip Med*, 17:e50225.
3. **Sahandi Far, M., et al. (2025).** "Cross-Platform Ecological Momentary Assessment App (JTrack-EMA+)." *J Med Internet Res*, 27:e51689.
4. **Revilla, M., Toninelli, D., & Ochoa, C. (2016).** "PCs versus Smartphones in Answering Web Surveys." *Survey Practice*, 9(4). DOI: 10.29115/SP-2016-0021.
5. **Williams, M., et al. (2022).** "Ecological Momentary Assessment: A Meta-Analysis on Designs, Samples, and Compliance Across Research Fields." *Assessment*, SAGE. DOI: 10.1177/10731911211067538.
6. **Meherali, S., et al. (2020).** "Rates of Attrition and Dropout in App-Based Interventions for Chronic Disease." *J Med Internet Res*, 22(9):e20283.
7. **Linardon, J. & Fuller-Tyszkiewicz, M. (2019).** "Attrition and adherence in smartphone-delivered interventions for mental health problems." *J Affect Disord*.
8. **Pratap, A., et al. (2020).** "Indicators of retention in remote digital health studies."
9. **Baumel, A. & Kane, J. M. (2018).** "Examining Predictors of Real-World User Engagement with Self-Guided eHealth Interventions." *J Med Internet Res*, 20(12):e11491.
10. **Kalda, A., Loos, B., Previtero, A., & Hackethal, A. (2024).** "Smartphone Investing." *Review of Finance*. (Earlier NBER WP 27036 / SSRN.)
11. **Mizrachi 等 (2022).** "Reading on a smartphone affects sigh generation, brain activity, and comprehension." *Sci Rep* (Nature).
12. **Pieh, T., et al. (2023).** "Directing smartphone use through the self-nudge app one sec." *PNAS*.
13. **One sec / MinimalistPhone studies (2024-2025).** ScienceDirect.
14. **npj Digital Medicine (2025).** "Effects of intervention design on engagement and outcomes in digital self-help for insomnia – factorial RCT."
15. **Honary, M., et al. (2023).** "Mobile health attrition reasons." *JMIR mHealth*.

### M 级（监管 / 工作论文 / 大型行业数据）

1. **FCA (2024).** "Digital Engagement Practices: A Trading Apps Experiment." Research Note. fca.org.uk.
2. **Kalda et al. (2021).** "Smartphone Trading Technology, Investor Behavior, and Financial Fragility." SSRN 3424405.
3. **Microsoft Research (CHI 2022).** Devices@Home + Cross-Device Taxonomy (Brudy et al.).
4. **Mozilla (2015).** "Task Continuity – Firefox UX."
5. **TARGET Integrated Care Program (2024).** *Int J Integrated Care*. 10.5334/ijic.ICIC24166.
6. **Wellally Tech (2024).** "Architecting Offline-First Health Apps."
7. **Habitica GitHub Issues #8070, #4313, #3079** — multi-device sync failures.
8. **Tradervue / Edgewonk / TraderSync / TradeZella product pages and platform comparisons (2026).** TradingJournal.com / TradeTrakr.

### W 级（行业博客 / 营销 / 用户论坛）

1. **Allen Pike (2021).** "The Persistent Gravity of Cross Platform."
2. **Calmevo (2026).** "Streaks vs Habitica."
3. **Netguru / Likasoft / MoldStud / Fifium (2024-2026).** Cross-platform development cost analyses.
4. **Duolingo Blog statistics (2024-2026).** Growth model, Android performance.
5. **Bloomberg (2021).** "How to Trade Stocks Online: Has Robinhood Made Day Trading Too Irresistible?"

### U 级（本笔记的逻辑推演）

- 第四节全部判断
- 表格中标 U 的格子
- 4.4 异步工作流判断
- 5.x 局限识别

---

## 附录 B：本笔记与 Phase 2 后续工作的接口

> **【写在前面】**：本笔记不要求 Phase 2 必须采纳本笔记的结论。它只是 Phase 2 决策时可参考的证据基础。

**本笔记没有回答的问题**（应在 Phase 2 Design 进一步处理）：
1. 单端起步具体应是 Cursor/终端 还是桌面 Web？需用户技术能力评估决定
2. 即使单端起步，是否要预留"未来可能扩展"的接口？
3. 数据格式（Markdown / SQLite / JSON）的选择如何与单端假设交互？
4. 如果用户明确反对单端（例如：他出差比例高），如何在不破坏证据基础的前提下做妥协？

**本笔记可能推翻的假设**：
- 若有人提出"σ 必须做手机 App 因为用户离开桌面就忘了"，本笔记给出 S 级反证。
- 若有人提出"多端是现代标配"，本笔记给出 S 级反证。
- 若有人提出"先做 Web + iOS + Android 多端因为'好做'"，本笔记给出 M 级反证（工程成本）+ S 级反证（无收益）。

**本笔记不能推翻的假设**：
- "单端 X 优于单端 Y"——本笔记不能区分桌面 Web vs Cursor vs 桌面原生 App
- "Phase 2 应何时实施"——本笔记不涉及实施时序
- "退出协议触发后端的形态"——本笔记不涉及退出场景

---

> **元规则收尾标记**：本笔记的所有 S 级引用都经过反复检索，作者团队 / 期刊 / 年份在我能验证的范围内是准确的。但部分文献我只读了摘要 / 主要发现，未深入方法学细节。**任何具体数字（如 77.4% / 73.0% / 49.3% / 10.9-22.4 字符）以原文为准；如本笔记与原文有差异，以原文为准。** 本笔记的"75% 置信""70% 置信"等元认知校准是基于跨证据流的逻辑汇集，不是统计推导，应在 ±15pp 内视为合理范围。
