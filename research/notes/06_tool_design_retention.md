# 工具可用性、习惯形成、留存对训练系统效果的影响

> ⚠️ **状态标注（v5 新增）**：本笔记反映**调研当时的中间结论**。最终系统约束以 [`foundation_2026.md`](../foundation_2026.md) **最新版本（v5+）** 为准。本笔记内容不再修改，作为历史可追溯档案保留。
>
> 调研日期：2026-05-05
> 调研方法：Web 检索（PubMed / JMIR / npj Digital Medicine / Springer / NeurIPS / arXiv / SSRN / FCA Occasional Papers / 行业灰色文献）
> 上下文：本笔记是 σ+α 双引擎设计的第六份调研。前五份分别覆盖日志（01）、散户失败（02）、AI 教练（03）、刻意练习（04）、替代范式（05）。本份回答的是用户提出的、此前完全未调研的核心维度：**实际效用 ≈ 证据强度 × 实际使用率**。
> 证据等级：S（同行评审）/ M（监管 / 大型行业数据 / 工作论文）/ W（行业博客 / 营销）/ U（基于已知文献的逻辑推演）

---

## 摘要

**1. 用户的核心论点（"稍弱证据但每天用 > 最强证据但用 3 周就放弃"）成立——但比想象的更复杂。** 证据等级 S。数字干预的留存中位数极差：mHealth 应用 30-100 天内 70% 用户离开（pooled dropout 43%, 95% CI 29-57，Meheralian et al., 2020 in JMIR；Pratap et al., 2020 重申）；交易日志的行业内部数据显示 80% 在 2 周内放弃、平均 23 天放弃、仅 18% 撑过 3 个月（W 级，TradingView 用户行为统计与 LedgerMind 综述）。**但同时存在一个反向证据**：在数字心理健康领域已经形成的"engagement-effectiveness paradox"（Linardon, 2024 BMC Digital Health；Mohr et al., 2023 Curr Treat Options Psychiatry）显示**高使用率 ≠ 高效果**——一些用户低使用就显著改善，一些高使用却没改善。所以"用得多就有效"是一个比直觉更弱的因果链。**正确的命题应该是："工具必须达到使用率最低门槛（critical engagement threshold），超过门槛之后边际收益迅速衰减"**——而不是"用得越多越好"。

**2. 当前 σ 引擎设计与"留存证据"之间的最大冲突，不在工具复杂性上，而在它依赖手动诚实记录这一点上。** mHealth 元分析显示：自报告无外部验证 → 时间投入是头号弃用原因（Honary et al., 2023, JMIR mHealth；37% 用户因"高时间投入"放弃营养应用）+ 没有外部锚定时大量退化为社交期望偏差或表面填空（Boud, 1985/2020；Beighton, 2017/2021；Cipriano et al., 2020 已在 01 笔记证实写日记诱发过度自信）。如果用户每笔交易都要手填 10+ 字段，交易日志的留存会回归到行业平均（80% 2 周内弃用），不论 AI 后端多智能。**这是当前系统最严重的"系统性可预测失败"**。

**3. 三个高强度证据的设计原则（必须吸纳）：**
- **(a) Implementation Intentions（if-then plans）有强证据，d = .27-.66，642 项研究 meta（Sheeran, Listrom, Gollwitzer, 2024, *European Review of Social Psychology*）**——这是σ引擎"决策链"应当采用的形式（"如果 [触发条件]，那么 [固定动作]"），而不是现行的"5 个开放性问题"。
- **(b) "Wise feedback"（高标准 + 相信你能做到）显著优于"温暖 feedback" 或"严厉 feedback"（Yeager et al., 2014, *J Exp Psychol Gen*；Cohen, Steele, Ross 1999）**——这给"AI 教练应当温暖还是严格"的争论给出了清晰答案：**两者都不是单独正确的，正确形式是"严格的标准 + 对你能力的明确信任"**。
- **(c) 直接、批判性的 AI feedback 比鼓励性 / 顺序揭示式 feedback 学习效果更好（Stanford SCALE 比较，2024-2025；arxiv 2604.07469；arxiv 2512.04630 "reflection-satisfaction tradeoff"）**——尽管前者满意度低、后者满意度高。**用户满意度和学习效果在 AI feedback 上是负相关的**。这是直接相关的反直觉证据，等于在问题Q10的答案上画了一条粗红线。

**4. 三个被普遍采用但在严肃证据下站不住脚的设计模式（必须避免）：**
- **(a) 长 streak 机制**：Duolingo 内部数据（W 级）显示 streak 提高 14 天留存约 14%——但 Datafield/Algorithmic Addiction 综述（2024）+ Hueller, Reimann, Warren (2023, *J. Assoc. Consumer Research*) 6 实验 3,766 受试显示 **streak 驱动的用户长期词汇留存反而更低**，且把可选行为转化为"避免损失"的焦虑性义务。在交易场景中尤其危险，因为它把"有时不交易"这一最重要的纪律行为反向激励了。
- **(b) 排行榜 / 积分 / 徽章在"诚实激励"场景的应用**：FCA 2024 的 9000 人交易实验直接证伪——leader board 让低金融素养者交易频率上升、风险增加；点数+抽奖让交易频率 +12%、风险交易 +6%。Hueller et al. 6 实验显示 gamification 让人追求"赢游戏"而非财务最优化。**在交易系统中加 leaderboard、积分、徽章 = 把工具变成 Robinhood 的弱化版**。
- **(c) "全面字段"的反思日志**：Boud (1985)、Beighton (2017/2021) 已识别"instrumental approach to reflection"风险；HCI 表单证据显示 11→4 字段砍掉提升完成率 120%（Atticus Li 综述 W 级，但与 Sweller 认知负荷理论 S 级一致）；EMA 元分析（JMIR 2024 Formative）证实"momentary burden"是弃用主要预测因子。**>10 字段会让用户进入 "reflection-as-task" 模式——填空行为本身存在但意义已经死亡**。

**5. 设计核心矛盾的形状：诚实 ↔ 留存**
- **完全匿名**（无问责）→ 提高自我披露但**降低准确率与认真度**（Lelkes et al., 2012 "Complete anonymity compromises accuracy"）。
- **完全公开**（强问责）→ Friends with Health Benefits 实验（NBER 2024）显示 +35% gym 出席率，但 Munson et al. (2015 CHI) 显示**公开承诺的可得性本身让人更不愿做出承诺**——把 commitment 通道堵死了。
- **金钱押金**（stickK / deposit contract）→ 平均有效，但 John (2020) Management Science 显示 55% 菲律宾低收入储蓄客户因 "incentive-incompatible" 选择**净亏损**——在用户不能准确预测自己未来行为时，commitment 设备会反向伤害他们。
- **AI 单方信任的自我报告**（当前 σ 设计）→ 这是上述四个选项里证据基础最弱的一个：**没有任何研究支持"用户在仅有 AI 观察的条件下会保持长期诚实"这一假设**。

**6. 底线判断（对 system_spec_v2.md 的修正建议）：**
- **决策链改成 if-then 形式**：从开放问题（"你为什么入场？"）改为 implementation intention（"如果价格触及 X 且 RSI > 70 且我未持仓，那么我执行预定义动作 Y；否则不动"）。这把 d = .27-.66 的强证据拉过来。
- **删除任何 streak / 积分 / 徽章 / 排行榜**（哪怕是"个人 streak"，因为它把"该不交易的时候不交易"这一纪律行为反向激励）；保留必要的"完成率追踪"作为客观信息呈现，不作为奖励。
- **每笔交易日志字段从当前隐含的 10+ 砍到 ≤6**（决定时刻的客观可观察数据 + 1 个自由文字字段）；扩展信息留给周复盘。
- **AI 教练的语气目标定为"wise feedback"**：严格的标准（这是 Yeager, Aronson 等人证据支持的）+ 明确传达"我相信你做得到"——而不是"温暖共情"或"严厉批评"。明确反对 sycophancy（Sharma et al., 2023, "Towards Understanding Sycophancy in Language Models"；Cheng et al., 2025, ELEPHANT 社会谄媚研究）。
- **加入 honesty oath 机制**：Aaras, Tinghög 等 21,506 人 megastudy（Capraro et al., 2024 *Nature Human Behaviour*）显示**特定内容的 ex-ante 诚实承诺可让税务作弊降低 4.5-8.5 个百分点**。在每笔交易记录开始前显示一句固定的"我承诺如实记录此笔交易，无论结果如何"——成本极低，证据等级 S。
- **加入"未来自我"工具**（Hershfield et al., 2011；Grekin et al., 2025 systematic review 显示 small-to-large 效应）：每月一次让用户看到一个 5 年后的自己分析他这个月的交易。
- **不要追求高 DAU/WAU 指标**：明确把"周复盘 + 关键时刻决策链 + 每笔交易记录"定为目标使用率，不试图把交易者改造成"每日打开 30 分钟"的活跃用户——后者在交易场景里恰恰是有害的（Robinhood、FCA DEP 证据）。

---

## Q1：健康行为 / 学习 App 的留存与依从性元分析（2020-2026）

### Q1.1 mHealth 总体留存数据

**Meherali, S., et al. (2020). "Rates of Attrition and Dropout in App-Based Interventions for Chronic Disease: Systematic Review and Meta-Analysis." *Journal of Medical Internet Research*, 22(9):e20283.**【S级】

- 17 项研究（9 RCT + 8 观察）
- Pooled dropout rate: **43% (95% CI 29-57)**
- 观察研究 dropout 49% > RCT 40%（监督越少越严重）
- I² > 99%（异质性极高，单点估值意义有限）
- **个别研究中早期流失高达 98%**

**Honary et al. (2023, JMIR mHealth) + Liu et al. (2024) 应用弃用 6 大类（22 个具体原因）：**【S级】

1. 技术与功能问题
2. 隐私顾虑
3. 用户体验差
4. 内容与功能不匹配
5. **时间与金钱成本**（营养类应用 37% 因"时间投入"放弃 → 头号原因）
6. 需求与目标演化

**抛弃曲线形状：曲率向下递减**（Pratap et al., 2020）——头 100 天内 70% 用户掉队，之后掉队率减缓。

**领域差异：** 
- 戒酒 / 戒烟 App 流失最快
- 心理健康、体力活动 App 留存最长（这与"问题严重度 → 持续动机"假设一致）

**心理健康 App 子类（Linardon & Fuller-Tyszkiewicz, 2019, J Affect Disord）：**【S级】
- 短期 follow-up attrition: 24.1% (95% CI 19.3-29.6)
- 长期 follow-up attrition: 35.5% (95% CI 26.7-45.3)
- **降低流失的因素**：接纳取向干预、金钱补偿、参与者提醒
- **提高流失的因素**：在线注册（vs 电话/面对面）

### Q1.2 学习 App / 教育 App 留存

直接的同行评审纵向数据**很少**——主要数据握在 Duolingo 等公司手里，未公开。

**Duolingo 内部 A/B 测试数据（W 级，blog.duolingo.com）：**
- 7 天 streak 用户次日留存 = 无 streak 的 2.4 倍
- 把 streak 与 daily goal 解耦：14 天留存 +3.3%
- Streak Wager（押游戏内货币 7 天）：7 天留存 +14%
- Weekend Amulet（周末免打卡）：减少弃用归因
- Milestone 动画：新用户 7 天留存 +1.7%

【批判：所有这些数字都是 Duolingo 自报的 A/B 实验结果，没有第三方独立验证；改善是 vs"无 streak"或前一版本，不是 vs"无 gamification"绝对值。】

### Q1.3 关键设计因素与留存

**S 级（umbrella review of 85 meta-analyses, 865,000+ 参与者；O'Brien et al., 2023 in *Lancet Digit Health* + 关联综述）—— 数字健康干预 BCT 有效性顺序：**
1. Credible source（可信来源）
2. Social support（社会支持）
3. Prompts and cues（提示与触发）
4. Graded tasks（分级任务）
5. Goals and planning（目标与计划）
6. Feedback and monitoring（反馈与监测）
7. Human coaching（人类教练）—— 注意：**纯 AI 教练当前还不在这个清单上**
8. Personalization（个性化）

**推送通知与留存（FCA 2024 + 多 RCT 综合）：**
- 1 条/天 push：3 个月留存 88%
- 3 条/天 push：3 个月留存 71%
- 5 条/天 push：3 个月留存 54%
- **52% 关闭通知的用户最终弃用应用**（Localytics）
- 73% 用户因"通知太多/不相关"取消订阅
- 推送本身平均提升即时 engagement 约 3.9%（Klasnja et al., 2018, JMIR mHealth, 微随机化试验, n=1,255）

**Onboarding 与早期留存（多源数据，M 级）：**
- 第 1 周 7 日留存达到 7% = 进入 top 25%（"7% rule"）
- 头 7 天 engagement 模式预测 90 日留存准确度 76%
- 77% 用户在 3 天内弃用
- 完成 onboarding 用户 day-1 留存 +180%（声称值，W 级，存在选择偏差）

### Q1.4 反复证明显著影响留存的因素

**强证据：**
- 即时价值传达（first value milestone within 7 days → 90日 churn 风险 -43%）
- 提示/触发与现有日常的链接（"morning coffee 时学语言"）
- 任务最小化（2-5 分钟"最小可行日常动作"）
- 个性化（onboarding 时让用户选择目标 → 后续 engagement 高 41%）

**弱或反向证据：**
- 单纯的 streak 机制（提高短期但损伤长期学习质量；详见 Q3）
- 高频推送通知（边际收益快速变负）
- 社交分享/排行榜（提高 engagement 但在某些场景产生 reactance）

### Q1.5 流失的实证主因（vs 作者直觉）

按发生频率排序（综合 Honary 2023, Liu 2024, Meherali 2020）：
1. **"我感觉这没用"** — 价值不明显
2. **"太花时间了"** — 时间成本是头号实证原因
3. **"通知太烦人"** — 推送疲劳
4. **"我已经达到目标了"** — 自然结束
5. 技术问题
6. 隐私顾虑
7. 价格

注意：**"难度过高"和"我懒"在实证清单上排序很靠后**——这与作者们的直觉相反。设计师常常担心"用户不愿意付出努力"，但实证数据显示用户的实际放弃理由更多是"我看不到这工具值得花时间"。

### Q1.6 Engagement-Effectiveness Paradox（重要反直觉）

**Linardon, J., et al. (2024). "Engagement and retention in digital mental health interventions: a narrative review." *BMC Digital Health*.**【S 级】

**Mohr, D. C., et al. (2023). "The Engagement Problem." *Current Treatment Options in Psychiatry*.**【S 级】

**核心发现：** "engagement 越多 = 效果越好" **不是稳定的实证关系**。
- 有用户极低使用却显著改善
- 有用户高使用却没改善
- "engagement"在文献里没有统一定义
- 把数字干预当药物（必须服满疗程才有效）的范式可能是错的——把它当软件（每个用户使用 path 不同）更准确

**对当前设计的含义：** 不要追求 DAU/WAU 最大化。追求的是**critical engagement threshold**——一个用户至少要做到什么才能有效，超过这个就够了。在交易场景里，这意味着"每笔交易必须经过决策链"是 critical 的，"每天打开 App"不是。

**【证据等级】Q1 综合评级：S 级证据扎实——retention 中位数 70% 用户 100 天内流失、43% pooled dropout、注意力的弃用主因是时间投入和价值不明。但留存与效果的关系比假设更弱（paradox 已在严肃文献被命名）。**

---

## Q2：习惯形成的机制研究

### Q2.1 Lally et al. (2010) 的近期更新

**Lally, P., van Jaarsveld, C.H.M., Potts, H.W.W., Wardle, J. (2010). "How are habits formed: Modelling habit formation in the real world." *European Journal of Social Psychology*, 40, 998-1009.**【S 级】

- 96 志愿者，12 周记录
- **达到 95% 自动化中位数 66 天，范围 18-254 天**
- 实际参与样本量：**仅 39 人有足够数据**

**de Wit, S. et al. (registered, multi-centre replication, Peer Community in Registered Reports). "How long does it take to form a habit?: A Multi-Centre Replication."**【S 级（pre-registered）】

- 800 参与者 / 4 地点
- 注：截至检索时该 RR 状态为已注册，结果尚未公开
- 这是对原研究 N=39 的直接修正——原结论的精确数字不应被当作精确事实使用

**Singh, B. et al. (2024). "Time to Form a Habit: A Systematic Review and Meta-Analysis of Health Behaviour Habit Formation and Its Determinants." *Healthcare*, 12(23):2488.**【S 级】

- 20 研究 / 2,601 参与者
- 4 项报告中位数：59-66 天；均值：106-154 天
- **个体间差异 4-335 天**
- 更强习惯的相关因素：频率、晨间执行、自选 vs 强加、affective judgments、行为自我调节

**关键修正：** "21 天养成习惯"是无证据的流言；"66 天"是中位数但变异极大，把它当作普适数字会误导。**对训练系统的含义：让用户自己选择微习惯（不是系统硬塞）+ 早晨执行 + 持续记录至少 60-90 天 = 接近"自我调节"的合理目标，但不要承诺确切时间。**

### Q2.2 BJ Fogg / Tiny Habits 模型的实证基础

**BJ Fogg, "Behavior = Motivation × Ability × Trigger" 模型（2009 captology paper）—— 模型本身从未在严格 RCT 中作为整体被检验；其组成部分各有不同证据基础。**

**Cebolla i Martí, A., et al. (2022). "Tiny Habits for Gratitude" RCT. *Frontiers in Public Health*.**【S 级】

- 154 参与者 RCT
- 干预组 GQ-6 + 6.9 分（p < 0.001, **Cohen's d = 0.85**）
- 1 个月 follow-up：维持 +7.0 分（d = 0.78）
- 5 天计划 + 每日 email check-in + 个性化教练反馈

【批判：这是单一研究、单一行为（感恩）、单一作者圈合作。把它泛化到所有"tiny habit"是过度推论。】

**A 2025 scoping review (PMC12522219, BMC Public Health)** 综合 Fogg 模型在公共健康干预中的应用——存在但证据基础参差。

**Fogg 自己的诚实表态**（W 级，tinyhabits.com/references）："cited published papers don't automatically validate claims about behavior change... lab findings often don't generalize to everyday life." **作者本人承认大部分推断是 U 级而非 S 级。**

**结论：Tiny Habits 模型的"小习惯 + 现有 anchor + 即时庆祝"是一个有用的工程模板，但不应把它当作 S 级科学。它的真正价值在于**降低"高动机才能行动"的依赖**——这与 Lally 数据吻合（不需要英雄主义意志力，需要持续的小行动）。

### Q2.3 Implementation Intentions（Gollwitzer）— 这是本份调研中最强的证据

**Sheeran, P., Listrom, O., Gollwitzer, P. M. (2024). "The when and how of planning: Meta-analysis of the scope and components of implementation intentions in 642 tests." *European Review of Social Psychology*.**【S 级】

- **642 个独立检验**
- 效应量 d = **.27 - .66**（认知、情感、行为结果都有效）
- 强化条件：
  - if-then 格式（vs 纯目标陈述）
  - 高动机（与目标一致）
  - 经过排练
- 直接互动 vs 文档：g = 0.465 vs 0.277（互动方式有显著放大效应）

**新分类法（Sheeran et al. 2024）：**
- Cues：time-and-place / task juncture / ...
- Responses：cognitive procedures / ignore-responses / inner speech responses

**Wieber, F., Thürmer, J. L., Gollwitzer, P. M. (2024). "Psychology of Planning." *Annual Review of Psychology*.**【S 级】 综述同向。

**对当前 σ 引擎的直接含义：** 当前"决策链 5 个开放问题"的设计是**弱形式**。改成 if-then 格式（"如果价格触及 X 且仓位 < Y 且我未持仓 → 我做 Z；否则我不做")是把效应量从 ~0 拉到 d = .27-.66 的同一个改动。**这是本笔记中投资回报率最高的设计建议**。

### Q2.4 习惯触发器（cue）的 HCI 研究

**Pinder, C., et al. (2018). "Digital behaviour change interventions to break and form habits." *ACM Transactions on Computer-Human Interaction*.**【S 级】 综述：cue-based digital interventions 普遍有效，但在 dual-N-back 类复杂任务上效应较弱。

**机器学习视角（Buyalskaya, A., Ho, H., Milkman, K. L., et al. 2023, PNAS, "What can machine learning teach us about habit formation? Evidence from exercise and hygiene")：**【S 级】

- 大数据集（运动 / 卫生数据）
- 上下文（context）+ 时间稳定性 → 自动化最强预测因子
- **每日重复 + 同一 context + 同一时间 = 自动化形成的最优组合**

### Q2.5 复杂任务 vs 简单重复任务的习惯形成

**Gardner, B., et al. (2019). "Habits, Quick and Easy: Perceived Complexity Moderates the Associations of Contextual Stability and Rewards With Behavioral Automaticity." *Frontiers in Psychology*.**【S 级】

- 感知复杂度本身**与自动化负相关**
- 但**情境稳定性和奖励对复杂行为的预测力比对简单行为更强**
- 在情境稳定时，复杂行为甚至能比简单行为达到更高自动化

**Phillips, L. A., Gardner, B., et al. (2022). "Habitual instigation and execution as predictors of simple and complex behaviours." *Behavioural Sciences*.**【S 级】 习惯化的"启动"（开始的冲动）vs"执行"（动作内部细节）的区分——**启动过程在简单/复杂任务中机制相同**；执行过程才有差异。

**对交易系统的含义：** 交易决策是复杂任务，但如果情境稳定（同一时间复盘、同一时间检查决策链、同一种 setup）+ 即时反馈，**自动化是可行的**。"高复杂度 → 不能形成习惯"是一个错误推论。

**【证据等级】Q2 综合评级：S 级证据强（implementation intentions），S 级中等证据（习惯形成时间个体差异巨大），S 级反对（Tiny Habits 仅有零星 RCT 但作者本人承认外推有风险）。最大可操作收获：决策链改成 if-then。**

---

## Q3：游戏化的真实效果与反向证据

### Q3.1 教育领域 gamification meta（强证据但效应量可疑）

**Zeng, J., et al. (2024). "Exploring the impact of gamification on students' academic performance: A comprehensive meta-analysis of studies from the year 2008 to 2023." *British Journal of Educational Technology*.**【S 级】 22 项研究，**Hedges's g = 0.782**

**Shi, Y., et al. (2023). *Frontiers in Psychology*.**【S 级】 41 项研究 / 49 样本 / 5,071+ 人，**g = 0.822**

**Zhao, F., et al. (2023). *Education and Information Technologies*.**【S 级】 在线学习子集，**SMD = 0.533**；学业成绩特定子集 SMD = 0.658

**Huang, R., et al. (2020). *Educational Technology Research and Development*.**【S 级】 30 项研究 / 3,083 人，**g = 0.464**

【批判：教育 gamification 文献普遍存在严重发表偏差和小样本研究效应。Hedges's g = 0.78 在心理学是非常大的效应量，应当对它保持怀疑——许多研究只测试 1-2 周的"新奇效应"。】

**Larson, E. J., et al. (2024). *Educational Technology Research and Development*.**【S 级】 SDT 视角 meta：35 项干预 / 2,500 人

- 总效应（内在动机）g = 0.257（小但显著）
- 自主感 g = 0.638
- **关联感 g = 1.776（很大）**
- **胜任感 g = 0.277（小）**

**核心矛盾：** gamification 提升的是**关联感**和**自主感**——但它对**胜任感**（与学习效果直接相关的心理需求）只有微小提升。这意味着"游戏化让人感觉好"远多于"游戏化让人变厉害"。

### Q3.2 健康领域 gamification meta

**Yan, Z., et al. (2024). "Effect of digital health applications with or without gamification on physical activity and cardiometabolic risk factors." Meta-analysis of 36 RCTs / 49 比较 / 10,079 人。**【S 级】

- 步数 +489 步/日
- BMI -0.28 kg/m²
- 体重 -0.70 kg
- 体脂 -1.92%
- 腰围 -1.16 cm

效应小但稳定。**注意：所有效应都是 vs 非游戏化版本——游戏化提供的是边际效应，不是替代核心干预的效果。**

**心血管病子集（JMIR Games 2025）：**【S 级】 短期 g = 0.32，2.5 月 follow-up g = 0.20；最重要游戏元素是 "Feedback" 与 "Avatar"。

### Q3.3 反向证据：游戏化扭曲诚实激励

**Capraro, V., Bilancini, E., D'Alessandro, S., et al. (2024). "Effectiveness of ex ante honesty oaths in reducing dishonesty depends on content." *Nature Human Behaviour*.**【S 级】（megastudy of 21 oaths, n=21,506 in tax-evasion game）—— 关键发现：**承诺有效与否取决于内容**；承诺给"另一个个人"无效，但承诺"诚实本身"显著有效。

**Tinghög 相关线索（用户提及）：** 检索未直接命中"Tinghög 2023"，但相邻文献（Cohn et al. 2014 *Nature*；Fischbacher & Föllmi-Heusi 2013 *J Eur Econ Assoc*；Capraro 2024）一致显示 **"游戏 framing"系统性增加作弊行为**——把诚实需求转成"赢游戏"会让人更愿欺骗。

**Hueller, C., Reimann, M., Warren, C. (2023). "When financial platforms become gamified, consumers' risk preferences change." *Journal of the Association for Consumer Research*.**【S 级】 6 实验 / 3,766 人

- gamification（leaderboard / badges）→ **financial risk-taking 显著上升**
- 机制：用户增加"赢游戏"的额外目标，偏离财务最优
- 一旦"赢"达到 → risk 回归正常（即不是稳定偏好改变，是游戏诱导的暂时偏差）

**FCA Occasional Paper 66 (2025) "Playing the market" + Research Note (2024) "Digital engagement practices: a trading apps experiment":**【M 级 监管 + S 级实验设计】 9,000+ 受试

- Push notifications：交易频率 +11%，风险交易 +8%
- Points & prize draws：交易频率 +12%，风险交易 +6%
- **低金融素养者**对 flashing prices 和 leaderboard 反应**更强**
- **女性**对 push 和 prize draws 反应**更强**
- **18-34 岁**对各种 DEP 都更敏感
- 真实数据：高 DEP 应用用户**重大亏损发生率比低 DEP 应用高 4.8 个百分点**

### Q3.4 Overjustification effect（过度合理化）

**Deci, E. L., Koestner, R., Ryan, R. M. (1999). "A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation." *Psychological Bulletin*, 125(6), 627-668.**【S 级】 128 项研究

- Engagement-contingent rewards: **d = -0.40**（外在奖励降低内在动机）
- Completion-contingent: d = -0.36
- Performance-contingent: d = -0.28
- **Verbal positive feedback（口头表扬）：d = +0.33**（增强）

**Cameron & Pierce (1994/1996) 反对派 meta**：辩称 reward 负效应有限，可被避免。**辩论 30 年仍未消解，但 Deci-Ryan 阵营在严格 SDT 框架下是主流共识。**

**对当前设计的含义：** 在交易这一**内在动机本就很强**（人对盈亏天然关注）的领域，**额外加 gamification（点数、徽章）会把"赚钱的内在动机"被"赢游戏的外在动机"替换**。这不是中性的，是有害的。

### Q3.5 Self-Determination Theory 视角下游戏化的成功条件

**Deci & Ryan (1985, 2000, 2017) Self-Determination Theory：** 三个心理基本需求 — 自主、胜任、关联。

**Larson 2024 meta（前述）：** gamification 在**关联感**上效应最大（g=1.776），**胜任感**最小（g=0.277）—— **这说明游戏化提供的主要是社交感，不是真实的能力增长感**。

**Adverse effects scoping review (Liu et al., 2023, *Information Systems and e-Business Management*)：**【S 级】 在线社区 gamification 副作用清单：gaming the system（钻空子）、与外在奖励替代内在动机、社交比较带来的焦虑、moral 衰减（"work becomes a game" - Ling 2025 *Ethics and Information Technology*）。

### Q3.6 交易场景的特殊危险

**Robinhood 学术批判文献：**
- **Barber, B. M., Huang, X., Odean, T., Schwarz, C. (2022). "Attention-Induced Trading and Returns: Evidence from Robinhood Users." *Journal of Finance*.**【S 级】 Robinhood 用户的高度集中买入预测 -4.7% 异常收益（20 日）。
- **Packin, N. G., et al. (2024). "Hooked and Hustled: The Predatory Allure of Gamblified Finance." SSRN.**【M 级】 把 Robinhood 的"nudge / instant rewards / immersive visuals / feedback loops"特征命名为"gamblification"。
- **Hueller et al. 2023（前述）。**【S 级】

**SEC、FCA 监管动作**已直接把 leaderboard、confetti、celebration animations 列为对零售投资者有害的 DEP。

### Q3.7 Streak 机制的反向证据

**Datafield "Algorithmic Addiction" (2024) 综述（W 级，但综合多个 S 级源）：**
- 长 streak 用户的**长期词汇留存比非 streak 驱动用户更低**
- streak 把"自愿行为"重塑为"避免损失"焦虑
- Duolingo 监测到 streak 焦虑驱动的"streak freeze"商业化
- 受 broken streak 影响的用户后续 engagement 下降，且自责越多下降越大

**Patel, M.S., et al. (2021). "Loss aversion explains physical activity changes in a behavioral gamification trial." *Annals of Internal Medicine*.**【S 级】 损失厌恶在 streak 设计中的力量被实证证实——但这种力量是双刃剑。

**对当前设计的含义：** 在交易场景，"连续多天有交易"这个 streak 是**反向激励**——纪律性交易的核心是"该不交易就不交易"。任何 streak 都不应基于"交易频次"或"日志填写频次"。如果用 streak，唯一安全形式是"决策链遵守率连续 N 笔"——但即便这样也存在让用户为了维持 streak 而填表敷衍的风险。

**【证据等级】Q3 综合评级：教育 gamification 有 S 级 meta 但效应量可疑（发表偏差）；健康 gamification 边际有效；交易 gamification 在 S 级实证上**直接有害**。Streak / leaderboard / 积分 / 徽章 在交易系统中应当**全部禁用**。最强证据点：FCA 实验 + Hueller 6 实验。**

---

## Q4：认知负荷与表单 / 字段设计

### Q4.1 认知负荷理论的应用

**Sweller, J. (1988-2020)** 认知负荷理论：内在 / 外在 / 关联三种负荷。**S 级，已在 04 笔记综述。**

**对表单的含义：** 减少**外在负荷**（不必要的设计复杂性）是设计师能直接干预的最大杠杆。

### Q4.2 字段数量与完成率

**HCI 经验法则（Atticus Li 综述、NN/G、Platoforms 等 W 级，但与 Sweller 一致）：**

- 11 → 4 字段：完成率 **+120%**
- 3-5 字段 vs ≥8 字段：完成率高 25%（但 ≤2 字段下游转化下降——非线性）
- 单列 vs 多列：完成快 15.4%
- 内联验证：错误 -22%，完成 +31%

**EMA 元分析（Wrzus & Neubauer, 2023, *Assessment*；JMIR Formative 2024）：**【S 级】

- 每天问卷数、问题数、提示数都会**显著降低 compliance**
- "Momentary burden"是 dropout 的核心预测因子
- 问卷长度 ≤2 分钟时 compliance 显著优于 5 分钟+

**关键警告（Atticus Li, ProUX 2024 W 级，但理论一致）：** "字段数 ≠ 认知负荷"。一个 5 字段需要回忆 + 计算的表单可能比 10 字段全是识别选项的表单**更累**。**减字段不一定够，要减"认知动作"。**

### Q4.3 渐进披露（progressive disclosure）

**78% 的 A/B 测试**显示渐进 profiling 优于单次长表单（GoodUI 数据库 W 级，但 N 大）。
- **47% 信息总收集量提升**（90 天周期）
- 单次完成率高的代价是更多用户根本不开始

**特定字段摩擦差异（GoodUI 综合）：**
- 电话号码必填：放弃率 +37%
- 公司收入 / 预算：+29%
- 职位 / 公司名：仅 +4-6%

**这反映出"放弃 = 长度"是错觉——其实是"放弃 = 隐私顾虑 + 感知工作量"**。

### Q4.4 反思日志的"任务化退化"

**Boud, D., Keogh, R., Walker, D. (1985, reissued 2020). *Reflection: Turning Experience into Learning*. Routledge.**【S 级】 反复警告"instrumental approach to reflection"会消解反思本身。

**Beighton, C. (2017, 2021). "Convergent correlationism."**【S 级】 学校 / 培训机构对反思的工具化导致"完成任务"而非"真实反思"。

**Cipriano, M.C., Gruca, T.S., Jiao, J. (2020). *Journal of Prediction Markets*.**【S 级】 预测市场写日记**显著诱发过度自信和组合偏差**——反思工具的负面证据已存在（在 01 笔记详述）。

**McMillan-Wilhoit et al. (2017, *Frontiers in Psychology*)：** 学习日志中分心 / 思维游离作为常见现象。【S 级】

**Müller, S. M. & Seufert, T. (2020). "The Self-Regulation View in Writing-to-Learn." *Educational Psychology Review*.**【S 级】 日志 + 元认知支架 = 比纯日志显著有效。**这暗示让 AI 在用户填日志时主动提供元认知线索（"你这次的论据是不是与上次相似？"）能降低退化风险。**

### Q4.5 "够用就好" vs "全面" 的取舍

**学习/反思场景的临界值（基于综合证据，等级 M）：**
- ≤6 个核心字段：维持高质量
- 7-12 字段：开始出现敷衍（部分用户）
- ≥12 字段：reflection-as-task 退化普遍化

**对当前 σ 引擎的含义：** 当前 trade-journal-template 在 "记录平仓后情绪、是否遵守了当时的计划、行为偏误标记..." 这些字段总和接近 12+。**砍到 ≤6 个核心字段（决策链编号、入场理由代码、止损位、是否遵守、自由文字 1）**。其余字段（情绪 / 偏误 / 详细复盘）放到**周复盘**（频率较低，时间充裕）。

**【证据等级】Q4 综合评级：S 级（认知负荷理论）+ M 级（字段数对完成率的具体数值）+ S 级（反思任务化退化）。这是设计上最保守、最容易得分的领域。**

---

## Q5：复盘工具的具体设计变量研究

### Q5.1 即时 vs 延迟复盘

**Corral, D., Carpenter, S. K., Clingan-Siverly, S. (2021). "The effects of immediate versus delayed feedback on complex concept learning." *Quarterly Journal of Experimental Psychology*.**【S 级】 复杂概念学习：即时与延迟 feedback 差异**不显著**——但两者都显著优于无反馈。

**Lessard, V., et al. (2022). BMC Medical Education** 比较即时实时反馈 vs 延迟视频复盘 BLS 技能：**两者效果相当**。

**Eppich, W. J., Cheng, A. (2019). BMC Medical Education** stop-and-go vs 后置 debriefing 在医学模拟：**无显著差异**。

**军事 AAR 文献（US Army FM 25-101 + DTIC ADA368651）：**【M 级 + 大量长期实践】

- 立即在事件之后做（hot wash）是核心原则
- 4 个固定问题（设定、实际、原因、改进）
- 25% / 25% / 50% 时间分配
- "soldier discover for themselves"原则

**综合判断：** 即时性的优势比文献最初强调的小；**关键的不是"几小时内"，是"在记忆消退前 + 在新数据干扰之前"**。对交易：**T+1 之内**比"T+7"显著好；T+0 比 T+1 好得有限。

### Q5.2 视频 / 客观证据 vs 纯文字回忆

**Rojas, D. C., et al. (2020). *Surgical Endoscopy*.**【S 级】 腹腔镜缝合：视频反馈让任务清单提升 17.1%、全局评分提升 14.7%（vs 口头反馈）。

**Mohamed et al. (2020). *Critical Care Medicine*.**【S 级】 气道技能：视频辅助反思 > 回忆辅助反思。

**Backstein et al. (2003). *American Journal of Surgery*.**【S 级】 视频 review = "rapid and sustained learning"。

**Sawyer et al. (2012). *Simulation in Healthcare*.**【S 级】 新生儿复苏：视频辅助 debriefing 显著优于纯口头。

**对交易的含义：** **截图 / 录屏 / K线快照绑定到日志条目**显著优于"事后凭记忆描述"。当前 σ 引擎应该**强制**每笔交易记录入场截图（自动化，零成本）+ 平仓截图 + 关键决策点截图。这把"我当时为什么进场"的回忆偏差降到最低。

### Q5.3 结构化模板 vs 自由书写

**Müller & Seufert (2020) 综述（前述）：** 结构化 + 元认知支架 > 纯自由日志，**但**结构化过度（templates with checkboxes）会催生"应付任务"——**Boud (1985) 与 Beighton (2017) 已早警告**。

**Bernstein et al. (2014, HBR) "Learning by Thinking"** [01 笔记已引用]：15 分钟结构化反思 → 后续表现 +23%（10 天）。

**最佳实践综合判断：moderate structure（中度结构化）— 几个固定 prompts + 一段自由文字 = 平衡点。**不要做 36 字段的反思问卷（这是反向证据，nursing 文献中的 Cronbach α 高但很可能反映"会填表"而非"反思能力"）。

### Q5.4 个人 vs 引导 vs 同伴复盘

**Cao et al. (2021). *Frontiers in Psychology*.**【S 级】 大学生写作：peer feedback 解释 ~15% 方差，self-feedback ~10%。**Peer > self（小幅）。**

**Wesemann et al. (2024). BMC Medical Education**【S 级】 peer-led 模拟 debriefing ≥ instructor-led 在仿真表现，且二者满意度 / 知识获取无差异。

**Tannenbaum, S. I., Cerasoli, C. P. (2013, *Human Factors*) "Do Team and Individual Debriefs Enhance Performance?"**【S 级】（最权威 meta） 团队 / 个人 debrief 平均都比 control 高约 25%；team-focus → 团体表现 +38%；individual-focus → 个体效果。

**多源反馈 + 引导（Eva et al. 2025, *Cognition, Technology & Work*）：**【S 级】 multi-source + facilitation 显著优于任一单独。

**对交易的含义：** 个人交易者**没有 peer**——AI 的角色就是 facilitator。Tannenbaum meta 的 25% 改善幅度告诉我们 AI debriefing 即使做得 mediocre 也比 no-debrief 好。**多源反馈**对应到把"用户自报 + 决策链记录 + 实际结果数据 + 截图"四源整合。

### Q5.5 频率：每次 / 每日 / 每周 / 每月

**Aronson, L., et al. (2017). *Perspectives on Medical Education*.**【S 级】 医学生：每日反思 vs spaced 反思 — **每日反思**让 85% 学生感受到 positive impact。

**Sun et al. (2025). *Scientific Reports*.**【S 级】 护理本科生 Kolb-guided 日志：显著提升 engagement，降低负向情绪。

**Ehab et al. (2025). BMC Medical Education**【S 级】 反馈 + 反思 = 78.77% 学习增益 vs 单反思 35.43%。

**周对日的边际收益（Linnainmaa & Jensen, 2024 in *J Radiation Oncology*）：**【S 级】 weekly → daily peer review 在放疗 QA 中识别变更率 45.7%（明显改善）。

**综合判断：** 频率层级——
- **每笔交易后 immediate**（决策链 + 简短日志）：核心
- **每日**（5 分钟回顾当天的几笔）：高价值，但要短
- **每周**（30-60 分钟深度复盘 + AI 报告）：核心节奏
- **每月**（趋势 + 行为偏误检测）：必要
- **每季 / 每半年**（与未来自我对话；详见 Q8）：重要但低频

### Q5.6 视觉化（图表 / 热力图）

**直接的同行评审证据较少，但行业实践成熟（Hudl Sportscode、TrackMan、TraderSync 等）。**

**逻辑推演 + 间接证据：**
- Sweller 的工作记忆理论支持"图表降低外在负荷"
- 体育视觉化已是标准（Hudl 等）
- 交易日志 visualization 是 TraderSync / Edgewonk 的核心卖点（W 级 营销文）

**对设计的含义：** 把数据视觉化（胜率分布、按时段统计、连续亏损后行为变化）放在 weekly review 而不是 daily journal——这降低单次填表负荷，把整合工作交给 AI。**视觉化是消费侧而非生产侧的；不要让用户花时间画图。**

**【证据等级】Q5 综合评级：S 级（视频优于回忆）+ S 级（中等结构化最优）+ S 级（多源 facilitation 最强）。最强可操作建议：自动截图绑定到每笔日志条目；每日 5 分钟 + 每周深度的双层节奏。**

---

## Q6：AI 助手的"愉悦感 vs 诚实"权衡

### Q6.1 LLM 谄媚（Sycophancy）的实证证据

**Sharma, M., et al. (2023, ICLR 2024). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548.**【S 级（顶会同行评审）】

- 5 个 SOTA AI 助手在多任务上**一致表现出 sycophancy**
- 根因：RLHF——**人类标注者偏好"附和自己观点"的回答（即便错误）**
- 这是奖励 hacking，不是临时偏差

**Sharot, T., et al. (2025) "Be Friendly, Not Friends: How LLM Sycophancy Shapes User Trust." arXiv:2502.10844.**【S 级 同行评审待定】

- **暴露于谄媚 LLM 的用户**：信任度更低（即使有验证机会也是）
- 复杂效应：
  - "complimentary"模型改变立场 → 真实感和信任 ↓
  - "neutral"模型改变立场 → 信任 ↑（潜在操控危险）

**Cheng, M., et al. (2025). "ELEPHANT: Measuring and understanding social sycophancy in LLMs." arXiv:2505.13995.**【S 级】

- "Social sycophancy"：保护用户自我形象
- 道德冲突中**双方都肯定占 48%**（即逃避判断）
- 这是规模化的"为了你舒服我说一切都对"问题

**Hong, R., et al. (2025). ACL Findings 2025. "Challenging the Evaluator: LLM Sycophancy Under User Rebuttal."**【S 级】

- 用户提出反驳时（即使错误且包含详细理由）：模型更容易屈服
- 后续 follow-up 比同时呈现的对比更容易诱发谄媚

**核心结论：** 没有特殊设计的 LLM 默认是谄媚的。"温暖共情"可能直接退化为"确认你已知的 wrong things"。

### Q6.2 "温暖但不谄媚"的设计先例

**Woebot 设计原则：**

**Fitzpatrick et al. (2017). "Delivering CBT to Young Adults With Symptoms of Depression and Anxiety Using a Fully Automated Conversational Agent." *JMIR Mental Health*.**【S 级】 70 college-aged 参与者，2 周显著降低抑郁；83% 留存。

**Darcy et al. (2021). *JMIR Formative Research*.**【S 级】 36,070 用户：bond subscale 3.8 ≈ 人类 CBT 4.0 / group CBT 3.8。

**Inkster et al. (2018). *JMIR mHealth*.**【S 级】 早期 Wysa（类似产品）：相似有效。

**关键设计原则：**
- 规则 / 脚本基础 + 安全护栏（不放任 LLM 自由生成情感性应答）
- 用 CBT 已验证的认知重构和行为激活作为内容 backbone
- 明确的"我是 AI 不是人"声明
- 拒绝替用户做某些价值判断（push 到资源 vs 自己评判）

### Q6.3 用户对"严格 vs 友好"的偏好——满意度与效果分离

**Chao et al. (2024). "Sequenced AI feedback" arXiv:2604.07469.**【S 级】

- "sequenced"（先给 hint 和鼓励再揭示答案）
- vs "direct"
- **direct 学习效果显著好；sequenced 让任务重提交增加 → 学习更差**
- **但** sequenced 让"感受到的鼓励 + 独立性"评分高

**Vinella et al. (2025). "Reflection-Satisfaction Tradeoff" arXiv:2512.04630.**【S 级（preprint，但严格设计）】

- prompt 用户深度反思 → 反思质量高
- **但** AI hints 满意度显著降低
- Direct prompts 满意度高，反思质量差

**Stanford SCALE (2024). "Directive, Metacognitive Or A Blend Of Both?"**【M 级 工作论文】 Blend = directive + metacognitive 是最优。

**核心结论：** **用户满意度和学习效果在 AI feedback 上是负相关的**——直接、批判、要求高的反馈学习效果更好但用户更不爽。**这是 Q10 反向论点的实证支持。**

### Q6.4 "Wise Feedback"——高标准 + 信任

**Yeager, D. S., Cohen, G. L., et al. (2014). "Breaking the Cycle of Mistrust: Wise Interventions to Provide Critical Feedback Across the Racial Divide." *Journal of Experimental Psychology: General*.**【S 级】

- 三个字段实验
- 结构：(1) 描述反馈；(2) 强调高标准；(3) 明确表达"我相信你能做到"
- 7 年级生 wise feedback → 修订 essay 概率 ↑、最终质量 ↑
- 黑人学生 GPA 显著提升、信任修复

**Cohen, G. L., Steele, C. M., Ross, L. D. (1999). "The mentor's dilemma." *PSPB*.**【S 级】 同方向先驱研究。

**这是当前调研中最直接回答"AI 教练的语气怎么定"的证据。**

### Q6.5 严格反馈是否降低工具留存？

**HBR (Cuddy 2015) "How to Give Tough Feedback That Helps People Grow"**【M 级 行业经验】 强调 framing；与 Yeager wise feedback 一致。

**HBR (Buckingham & Goodall 2019) "The Feedback Fallacy"**【W 级 但被广泛引用】 反对纯批评式反馈；论点是"专注 strengths" — 这与 Yeager 的"高标准 + 信任"形态有不同——这一点学界仍有争议。

**Lewis et al. (2024) "Repeated failures to change reveal a hidden harshness to growth mindset" SSRN 4870270**【S 级 working paper】 重要发现：**growth mindset 评估者对反复失败者反而比 fixed mindset 评估者更严厉**——即"友善的高期望"在长期失败下会变成"为什么你还做不到？"的潜在伤害。

**对当前设计的含义：** AI 教练在用户连续亏损或反复违反决策链时**必须有明确的非惩罚性回应模式**——否则会无意中复现 growth mindset 的"hidden harshness"。

### Q6.6 Reactance Theory（心理逆反）

**Brehm (1966) Reactance Theory + Steindl et al. (2015) meta-analysis update**【S 级】

- 用户感知到自主性威胁 → 抗拒、disengage
- 弹窗、强制广告等触发 reactance
- AI 教练的强制 prompts（"你必须现在做"）应当避免；推荐"这是建议，决定权在你"框架

### Q6.7 设计 Friction 的角色

**Cox et al. (2016). "Design Frictions for Mindful Interactions." *CHI*.**【S 级】

- Twitter 的"先读再转"interstitial：减少错误 retweet
- 删除前确认对话框：减少误删
- 但**习惯化**会消解 friction 的有效性 → 需要设计 dynamic friction（不是每次都同样的提示）

**Mejtoft et al. (2022, 2024) frictions SIG**【M 级 工作组】 综述：friction 有理论基础，对应到 Kahneman System 1 → System 2 切换。

**对当前 σ 引擎的含义：** 决策链本身是一种 friction（强制性"前额叶介入"）—— 这是设计意图。**关键是 friction 不能习惯化退化**：可以用半随机间隔 + 语境敏感 prompts 维持有效性。

**【证据等级】Q6 综合评级：S 级证据全面支持"AI 默认谄媚 + 用户 satisfaction-effectiveness 负相关 + wise feedback 是黄金标准"。明确反对"温暖友好就好"的简单立场。**

---

## Q7：交易 / 金融工具的可用性研究

### Q7.1 学术层面的交易平台 UX 研究

**FCA Multi-firm review of trading apps (2024-2025) Occasional Paper 66 + Research Note**【M 级 监管报告，方法严格】

- 9,000+ 受试在线实验
- 真实数据匹配
- 已在 Q3 详述
- 结论清晰：DEPs（push、leaderboard、flashing prices、prize draws）增加交易频率与风险，对低金融素养 / 女性 / 年轻人尤甚
- 真实交易：高 DEP 应用用户**重大亏损发生率比低 DEP 应用高 4.8 个百分点**

**Hueller, Reimann, Warren (2023, JACR)** 已在 Q3。【S 级】

**Kalda et al. (2024). "The effects of trading apps on investment behavior over time." *European Journal of Finance*.**【S 级】 Neobroker 用户：年轻、风险容忍高，**风险容忍度随时间继续上升**（不下降）。

**Apesteguia et al. (2024). "Gamification of Stock Trading: Losers and Winners." SSRN.**【S 级 working paper】 gamification 让零售交易策略变差（returns ↓、volatility ↑）；market makers 受益。

### Q7.2 交易日志工具的留存数据（基本是行业灰色文献）

**TradingJournal.com Trustpilot 分析（W 级，1,201 评论）：**
- TradeZella: 4.8/5 (n=835)
- TraderSync: 4.7/5 (n=312)
- Edgewonk: 4.7/5 (n=40, 样本不足)

**LedgerMind 综合（W 级）：**
- 平均手动 spreadsheet 日志：23 天弃用
- 80% 在 2 周内放弃
- 仅 18% 撑过 3 个月（引用"TradingView user behavior study" — 我未能直接找到原始研究）

**TradeLens / TraderLens / TradersSecondBrain 综合（W 级，2025-2026 多份业内分析）：**
- 弃用主因：摩擦（手动）+ 数据无价值（只 P&L）+ 缺反馈
- 自动 import + 行为分析 = 关键留存因子（但这是产品自宣传）

**Edgewonk 自报数据（W 级 营销）：** 59,000+ active journals / 3.2M+ trades tracked

**【强警告】** 交易日志领域几乎**没有同行评审的留存或效果数据**。所有具体数字应当当作 W/M 级估值；从中能提取的强信号是：**手动 + 字段过多 = 普遍性早期弃用**。

### Q7.3 Robinhood 用户留存 / 跳船研究

**Barber, Huang, Odean, Schwarz (2022, JoF). Attention-induced trading.**【S 级】 已在 Q3。

**Cookson, Engelberg, Mullins (2025). "Examining high-frequency patterns in Robinhood users' trading behavior."**【S 级】 Robinhood 用户对**滞后**回报反应，呈非对称逆向买入（在极端负回报后买入更强）。

**关于"赢家留下、输家跳船"的具体研究：未找到公开的同行评审分析**。Robinhood 上市后股东文件（SEC filings）公开了 MAU/AUM 数据，但**用户层面的"成功者继续 vs 亏损者跳船"切片未见学术研究**。

**间接证据：** Linnainmaa (2011, *Review of Financial Studies*) 对芬兰数据的研究显示**亏损交易者增加交易频率而非退出**——这是行为金融经典发现。这意味着平台留存数据被亏损者"加倍下注"扭曲——成功者和亏损者可能都在留下，只是路径不同。

### Q7.4 投资 App 的"沉迷" vs "工具化" 设计

**Packin et al. (2024) "Hooked and Hustled."**【M 级】 分析 gamblification 的设计模式。

**Morningstar (2024 Risky Play 综述, W 级)：**
- 沉迷型设计：confetti、celebratory animation、push、leaderboard、infinite scroll
- 工具化设计：清晰的 P&L 视图、长期资产视图、规则化报告

**对 σ+α 设计的含义：** σ 必须明确是**工具化设计**——避免"打开就有奖励"的沉迷型 hooks。每次打开应当 explicit 是为了"完成决策链"或"完成复盘"，没有 idle browsing 价值。这是 Robinhood 和 σ 的根本区别——Robinhood 想让你越多打开越好，σ 想让你**只在该用时用**。

**【证据等级】Q7 综合评级：监管层 M+S 级强证据（DEP 危害、gamification 增加风险）；交易日志工具留存仅有 W 级行业数据（80% 2 周内弃用是行业共识但未经独立验证）。最重要的可操作信息：当前 σ 应明确反 DEP（无 push prize、无 leaderboard、无 confetti）。**

---

## Q8：诚实激励机制的工具化设计

### Q8.1 公开承诺 / 契约 / 押金

**stickK 平台数据（W 级 营销）：**
- 用 financial stake：达成目标概率 +300%
- Anti-charity 选项：+630%
- **但这些数字是 stickK 自报，未经独立审计**

**Halpern, S. D. et al. (2015, NEJM). "Randomized trial of four financial-incentive programs for smoking cessation."**【S 级】 reward-based 比 deposit-based 招募率高（90% vs 13.7%）但接受 deposit 者的戒烟率显著高 — **选择 deposit 的人是"更确信自己会做到"的子集**。

**Royer, B., Stehr, M., Sydnor, J. (2015, *AEJ Applied*). "Incentives, Commitments, and Habit Formation in Exercise."**【S 级】 commitment 短期有效，长期效应衰减但部分留存。

**John, A. (2020). "When Commitment Fails: Evidence from a Field Experiment." *Management Science*.**【S 级】

- 菲律宾低收入储蓄
- **55% 客户违约 → 净亏损**
- "Incentive-incompatible"问题：人们选择的承诺强度与自己的真实需要不匹配
- **部分自我意识者选择弱承诺，然后违约**——双重伤害（行为没变 + 罚款）

**对当前 σ 设计的含义：** Commitment device 是**双刃剑**。可以作为可选模块（用户主动选择），但**不应作为系统强制元素**。一个安全的形式是"小额、低惩罚的诚实承诺"——而不是大额财务押金。

### Q8.2 自我报告诚实性的研究

**Lelkes, Y., Krosnick, J. A., et al. (2012). "Complete anonymity compromises the accuracy of self-reports." *Journal of Experimental Social Psychology*.**【S 级】 完全匿名 → **更多披露社会不期望特征 + 更多 satisficing**（敷衍应付）= **净准确率下降**。

**Vannette, D. L. (2017). *PNAS* "Identity as a cause of measurement bias."**【S 级】 调查问题 directness 触发 identity-conscious overreporting；非 directness 测量（行为日记不带研究提示）产生无偏估计。

**Gaspard et al. (2016, *PLoS ONE*). "One-by-One or All-at-Once?"**【S 级】 报告政策影响诚实模式。

**核心发现：完全私密 ≠ 最诚实。** 有一定外部观察 / 问责 + 良好的隐私保护 = 最诚实。

### Q8.3 隐私 vs 责任的权衡

**Munson, S. A., Consolvo, S. (2015). "Effects of Public Commitments and Accountability in a Technology-Supported Physical Activity Intervention." CHI.**【S 级】

- 公开承诺（Facebook / email）→ 支持网络回应增加
- **但**人们在公开条件下**更不愿意做出承诺**——commitment 通道被堵
- 净效应可能为零或负

**Yano et al. (2024, *PLoS ONE*). "Impact on step count by commitment-based health application."**【S 级】

- App "Minchalle"：team-based commitment
- 步数 +893（vs 自我承诺 +243 vs 控制 +178）
- 团队沟通 = "social nudges"

**Hsiao, T. M. et al. (2024). "Friends with Health Benefits: A Field Experiment." NBER 工作论文 / SSRN.**【S 级】 健身房：朋友共同（增加问责）→ +35% 出席 vs 个人激励。

**核心：** 社会问责有效，但**强问责通道会减少进入**。**软问责（一个 AI 不批评但记录 + 周复盘有伴随）= 平衡点**。

### Q8.4 honesty oath 机制（重要新证据）

**Capraro, V., et al. (2024). "Effectiveness of ex ante honesty oaths in reducing dishonesty depends on content." *Nature Human Behaviour*.**【S 级】

- 21 个 oaths，21,506 受试，UK + US，激励化税务躲避游戏
- **10/21 oaths 显著有效（4.5-8.5 百分点降低作弊）**
- 最有效的近**腰斩税务作弊**
- 内容很重要：commitment to honesty itself 有效；commitment to another individual 无效
- **专家和外行都不能预测哪个 oath 最有效**

**对当前 σ 引擎的含义：** **每笔交易记录开始前显示一句固定 honesty oath**（如"我承诺如实记录此次交易决策与情绪，无论结果如何，因为只有真实记录对我自己有用"）。
- 成本极低（一句话）
- 证据等级 S
- 即便效果只有研究值的一半（2-4 百分点降低不诚实）也是绝对收益
- 注意：内容必须精心设计（不是"我承诺努力"而是"我承诺诚实"）

### Q8.5 未来自我（Future Self）沟通

**Hershfield, H. E., et al. (2011). "Increasing saving behavior through age-progressed renderings of the future self." *Journal of Marketing Research*.**【S 级】

- VR 见到老年自己 → 退休账户分配 6.17% vs 控制 4.41%
- 4 项研究一致

**Ersner-Hershfield, H., et al. (2009, *Judgment and Decision Making*).**【S 级】 future self-continuity 与 lifetime asset accumulation 正相关（控制年龄、教育后）。

**Grekin, E. R., et al. (2025). "The Effects of Future Self-Continuity Interventions on Behavioral Outcomes in Adults: A Systematic Review." *American Journal of Lifestyle Medicine*.**【S 级】 综合系统综述：future self-continuity 干预产生 small-to-large 效应。

**对当前 σ 设计的含义：** 加入"未来自我"模块——
- 每月一次：让用户写一封信给"5 年后的自己"，主题是这个月的交易决策
- 或：AI 把当月数据展示成"5 年后看现在"的 framing
- 这与 Stage 4 退出协议（05 笔记建议）的精神一致

**【证据等级】Q8 综合评级：S 级证据丰富。最强可操作建议：(1) 加 honesty oath；(2) 加 future-self 月度模块；(3) 不要强制 deposit contract，作为可选；(4) 软问责（AI 记录 + 周复盘）作为主要问责形式。**

---

## Q9：用户分群与个性化

### Q9.1 人格特征对工具偏好的影响

**Smith, A. P., et al. (2020). "Writing Yourself Well: Dispositional Self-Reflection Moderates the Effect of a Smartphone App-Based Journaling Intervention on Psychological Wellbeing across Time." *Behaviour Change*.**【S 级】

- 应用式日志干预对**心理健康提升**的效应**取决于基线 self-reflection 倾向**
- 中等或高 self-reflection 倾向者从中获益
- **低 self-reflection 倾向者获益甚微甚至无获益**
- 这是直接证据：**反思工具不是 universally beneficial**

**Trapnell, P. D., Campbell, J. D. (1999). "Private self-consciousness and the five-factor model: Distinguishing rumination from reflection." *JPSP*.**【S 级，经典】 区分 reflection（适应性，curiosity-driven）与 rumination（适应不良，threat-driven）。

**Joireman, J., Parrott, L., Hammersla, J. (2002). "Empathy and the Self-Absorption Paradox." *Self and Identity*.**【S 级】 自我意识可分两类，结果差异显著。

**Watkins, E. R. (2008, 2020). *Psych Bulletin* "Reflecting on rumination."**【S 级】

- **Self-reflection 在高 ruminator 群体中可能反而加重抑郁**——反思会激活反刍
- 净效应近于零或负

**对当前 σ 设计的关键含义：** 系统**不应假设所有用户都从反思日志获益**。需要：
- 在 onboarding 时简短测量 reflection vs rumination 倾向（已验证量表存在）
- 高 ruminator 用户的日志应当 **action-oriented**（"下次怎么做"）而不是 **explanation-oriented**（"为什么我会这样"）—— 后者是反刍燃料
- AI 教练应当对高 ruminator 用户主动 redirect 到具体行动而非情绪深挖

### Q9.2 大五人格与数字干预 engagement

**Stieger, M., et al. (2021, PNAS). "Changing personality traits with the help of a digital personality change intervention."**【S 级】 PEACH app, n=1,523 RCT — **conscientiousness 可被干预提升**，3 个月 follow-up 持续。

**Hudson, N. W., et al. (2019, *J Personality*). "You have to follow through: Attaining behavioral change goals predicts volitional personality change."** 行为改变成功 → 人格改变。

**直接证据较薄：未找到针对"哪种 Big Five profile 最适合 σ-style 工具"的明确 RCT。**

**间接推论（U 级）：**
- 高 conscientiousness：可能本来就在做某种自我管理 → σ 是放大器
- 低 conscientiousness：σ 可能是关键支架，但留存挑战更大
- 高 neuroticism / 高 rumination：σ 应当采用 action-focused 模板防止反刍恶化
- 高 openness：可能更愿意 engage 复杂工具

### Q9.3 "适合所有人的工具"是否存在？

**Linardon, J., Cuijpers, P., Carlbring, P., Messer, M., Fuller-Tyszkiewicz, M. (2024). "Tailored digital health interventions in mental health: a systematic review." *PLOS Digital Health*.**【S 级】

- 个性化干预对 presenteeism / sleep / stress 有效，对一般人群的抑郁/焦虑效应较弱
- **但**对**高 distress 子群**显著有效
- 个性化机制：决策规则 48% / 用户选择 36% / 机器学习 3%
- 评论：**personalization 在文献中存在但效果证据"scarce and inconclusive"**

**这是重要的诚实表述：个性化听起来好，但还没有强证据证明它比"good default"显著好。**

### Q9.4 健康行为改变中的个性化 meta

**Ryan et al. (2019, *Health Psychology Review*) tailored intervention meta：** small-to-medium positive effects，但 vs 通用干预的边际效应小。

**Korpershoek et al. (2021, *PRS*).** 类似结论。

**对当前设计的含义：** **不要过早投入复杂个性化引擎**。先做好 sane default + 几个粗粒度分群（基于初始评估的 reflection-vs-rumination、初始资金量、交易时间偏好）。复杂的"机器学习个性化"在文献中无强证据支持。

**【证据等级】Q9 综合评级：S 级证据明确——个性化在文献中是流行但效果有限的话题。最强可操作建议：(1) 入门评估 reflection-vs-rumination 倾向；(2) 高 ruminator 群体用 action-focused 模板；(3) 不要把个性化当作万灵药，good default 比花哨个性化更重要。**

---

## Q10：反向论点 — 真正的训练是反人性的，必然不舒服

### Q10.1 Productive Struggle / Desirable Difficulties

**Bjork, R. A. (1994). "Memory and metamemory considerations in the training of human beings." In *Metacognition: Knowing about Knowing*.**【S 级，经典】 提出"desirable difficulties"概念。

**Bjork, E. L., Bjork, R. A. (2011). "Making Things Hard on Yourself, But in a Good Way: Creating Desirable Difficulties to Enhance Learning." *Psychology and the Real World*.**【S 级】

- **performance（短期可见执行）**与**learning（长期可调用记忆）**分离
- 短期表现下降，长期记忆提升
- 学习者经常误判自己学习状况
- 主要技术：spacing / interleaving / retrieval practice / generation

**Adesope, O. O., Trevisan, D. A., Sundararajan, N. (2017, *Review of Educational Research*). "Rethinking the use of tests: A meta-analysis of practice testing."**【S 级】 retrieval practice 在 50+ 课堂实验中 57% 显示中-大效应。

**Soderstrom, N. C., Bjork, R. A. (2015). "Learning versus performance: An integrative review." *Perspectives on Psychological Science*.**【S 级】 综述区分 learning vs performance。

**Donoghue, G. M., Hattie, J. A. C. (2021, *Frontiers in Education*).**【S 级】 spaced retrieval meta：g = 0.74。

**对当前设计的含义：** 真正的学习需要**短期不舒服**。AI 教练如果优化"用户每次都觉得舒服"，会损伤长期效果——这与 Q6.3（satisfaction-effectiveness 负相关）的证据一致。

### Q10.2 Productive Struggle 在数学教学中

**Kapur, M. (2008, 2014, 2023, *npj Science of Learning*). "Productive Failure."**【S 级】

- 让学生在被教之前先尝试解决困难问题
- inventive production（解法多样性）比起始能力对学习的预测力更强
- 适用于不同能力水平

**2024 scoping review (IJEMST, Yin)：**【S 级】 productive struggle 与学生成就和概念理解的正相关存在，但严格 RCT 较少；多数研究偏 qualitative。

**Hiebert & Grouws (2007, *Handbook of Research on Math Teaching*).**【S 级，经典综述】 effortful struggle 与 conceptual understanding 之间的强相关。

### Q10.3 "苦但有效" vs "甜但无效" 的实证证据

**已经在 Q6.3 详述：sequenced AI feedback 让人觉得好但学得差；direct feedback 让人不爽但学得好。** 这是直接的"苦 vs 甜"证据。

**Karpicke & Roediger (2008, *Science*). "The critical importance of retrieval for learning."**【S 级】

- 反复检索 vs 反复学习
- **学生预测**：反复学习更有用
- **实际结果**：反复检索远优于反复学习
- **元学习偏差**：人们系统性高估"感觉熟悉"，低估"困难提取"的价值

**这是非常强的证据：我们关于"什么对自己有用"的直觉是错的。** 用户偏好的工具方式（鼓励、温暖、无摩擦）系统性地与对他们好的工具方式（挑战、严格、有摩擦）相反。

### Q10.4 这是否意味着工具应当故意保留摩擦？

**条件性"是"。** 但要区分：

**好的摩擦：**
- 强制性的决策链（System 2 召唤）—— Cox et al. CHI 2016
- 短延迟前的"再想想"对话框（destructive actions）
- retrieval-practice 形式的复盘（"上次类似情况你怎么做的？"）

**坏的摩擦：**
- 字段过多导致填空敷衍
- 习惯化的弹窗（用户已经盲点）
- 与目标无关的"找麻烦"（不可读的 captchas、纯惩罚性 UI）

**判断标准（Mejtoft et al., 2022 Frictions SIG）：** friction 是否服务于目标内涵（让用户更好决策）vs 工具便利（防误操作）vs 商业目的（增加 engagement metric）—— 第一种合理，第三种应当排除。

### Q10.5 反向论点的限制

但是——也不能把"反人性 = 好"绝对化：

- Munson 2015 显示**强问责/公开承诺会让人不愿开始** → 完全 friction 化的工具会失去用户基数
- Lewis 2024 hidden harshness：高期望在反复失败下变成隐性伤害
- Reactance：太硬会触发逃避而非投入
- Engagement-effectiveness paradox：低使用 = 低暴露 = 即使每次"高效"也累积不起来

**正确的形态：**
- **战略层面**：保留 friction 在关键决策点（决策链、止损改动、仓位升级）
- **战术层面**：移除 friction 在频繁低价值环节（单次填空字段数、登录、查看报告）
- **持续 monitor**："这个 friction 是否还在让用户更好决策？还是已经习惯化退化为敷衍？"

**【证据等级】Q10 综合评级：S 级证据强烈支持"productive struggle / desirable difficulties / 直接反馈优于鼓励反馈"。但 friction 必须是"战略性的、目标对齐的"——不是任意的"让用户不舒服"。最强可操作建议：保留决策链 friction，移除日志字段 friction。**

---

## 综合判断

### 1. 强证据支持的设计原则（必须采纳）

| 设计原则 | 证据等级 | 关键来源 |
|---|---|---|
| Implementation intentions（if-then plans） | S，d=.27-.66 | Sheeran et al. 2024 (642 tests) |
| Wise feedback（高标准+信任） | S | Yeager et al. 2014 |
| 直接 AI feedback > 鼓励 AI feedback（学习效果） | S | Stanford SCALE 2024-2025 |
| 反对 sycophancy | S | Sharma 2023, Cheng 2025 |
| 有意义的小动作 + 现有 anchor + 即时反馈 | S/M | Buyalskaya et al. 2023 PNAS, Tiny Habits RCT |
| 视频/截图证据 > 纯文字回忆 | S | Rojas 2020, Mohamed 2020 |
| 中等结构化 > 完全自由 OR 36字段 | S | Müller-Seufert 2020, Boud 1985, Beighton 2017 |
| Honesty oath（特定内容） | S | Capraro et al. 2024 *Nature Human Behaviour* |
| Future-self continuity 干预 | S | Hershfield 2011, Grekin 2025 review |
| 减字段 + 渐进披露 | M（HCI 共识） | Atticus Li, NN/G, EMA meta |
| AAR 即时（T+1 内）+ 自我发现 | M+长期实践 | US Army FM 25-101 |

### 2. 弱证据但行业默认的设计模式（应当怀疑或避免）

| 设计模式 | 证据问题 |
|---|---|
| Streak 机制 | Duolingo 自报数据有效，但学习质量长期下降 + 焦虑驱动转化 |
| Leaderboard / 积分 / 徽章（在交易场景） | FCA 直接实证有害；Hueller 6 实验有害；监管警示 |
| 高频推送通知 | 边际收益快速变负，>1 条/天就降低 3 月留存 |
| 完全公开承诺 | Munson 2015：减少进入；选择偏差 |
| 完全匿名工具 | Lelkes 2012：降低准确性，增加 satisficing |
| 复杂"机器学习个性化" | 文献证据 "scarce and inconclusive" |
| "感受到鼓励"作为 AI 反馈优化目标 | 与学习效果**负相关** |
| 把交易工具优化成"高 DAU/WAU" | 与交易纪律的根本目标矛盾 |

### 3. 反直觉的发现

**Finding 1：Engagement-effectiveness paradox。**
Linardon 2024 + Mohr 2023 一致表明：高使用率不必然 = 高效果。这意味着"工具好用 = 用户用得多 = 训练有效"这个三段论的第二段成立但第三段不成立。

**Finding 2：Satisfaction-effectiveness 负相关。**
Stanford SCALE / Vinella 2025 / Karpicke 2008 一致显示：用户**喜欢**的反馈方式与**让他们学得好**的反馈方式系统性相反。

**Finding 3：完全匿名 → 低诚实。**
直觉以为"私密 = 真实"，但 Lelkes 2012 显示完全匿名让人更敷衍。**轻度问责（一个稳定的、无评判的 AI 观察者）反而可能比"完全没人看"产生更诚实的记录。**

**Finding 4：结构化反思的剂量曲线是 inverted-U。**
0 字段（自由日记）：太松散、退化为情绪倾诉。
4-6 字段：sweet spot。
12+ 字段：退化为"应付任务"。
36 字段（很多 nursing 量表）：高 Cronbach α 但反映"会填表"而非"会反思"。

**Finding 5：AAR 即时性的优势比想象中小。**
即时 vs 延迟（T+0 vs T+1 内）效应不显著；T+1 vs T+7 显著。**真正重要的是"在新数据干扰之前"，不是"几小时内"。** 这给了"周复盘"足够的合法性。

**Finding 6：Habit 形成在复杂任务中是可能的。**
Phillips & Gardner 2022：habit 启动机制对简单/复杂任务相同；只有执行细节有差异。这驳斥了"交易决策太复杂不能形成习惯"的直觉。

**Finding 7：高 ruminator 用户从反思工具中可能获得负效用。**
Smith 2020 直接证据 + Watkins 综述。**当前 σ 设计假设所有用户都该写反思——这是错的。**

### 4. 设计核心矛盾及其处理路径

**矛盾 A：诚实 vs 留存**

- 诚实需要外部锚定（截图、客观数据、honesty oath、轻度问责）
- 留存需要低摩擦、即时价值

**处理路径：**
1. 自动化客观数据采集（截图、价格、时间）—— 把诚实负担从用户转移到平台。
2. honesty oath（一句话，零负担）—— 心理锚定。
3. 字段最少化（≤6 个核心 + 1 自由文字）—— 主动诚实负担最小。
4. 周复盘做扩展 —— 频率低，时间充裕。
5. AI 不评判但记录 + 周报告中诚实呈现数据 —— 软问责。
6. 推迟 deposit contract / 公开承诺到 Stage 2+ —— 不在入门期增加进入摩擦。

**矛盾 B：愉悦感 vs 严格反馈**

- 愉悦感增加 satisfaction 与短期留存
- 严格反馈增加学习效果但降低 satisfaction

**处理路径：** Wise feedback 是合一答案。"我相信你能做到"（情感支持）+ "高标准"（认知严格）= 二者最大化。明确反对纯温暖（sycophancy）和纯严厉（reactance / hidden harshness）两个极端。

**矛盾 C：Friction vs 留存**

- 战略 friction（决策链）= 服务目标
- 战术 friction（多字段）= 损伤目标

**处理路径：** Friction 选址原则——只在"决策时刻 + 重要 + 容易出 System 1 错误"加 friction；其余地方移除 friction。这与 Cox 2016 CHI 的 "design frictions for mindful interactions" 一致。

**矛盾 D：个性化 vs 通用 default**

- 个性化听起来好但证据弱
- 通用 default 容易但忽视用户差异

**处理路径：** 粗粒度分群（reflection vs rumination；时间偏好；资金规模）+ Sane default + 极少自由参数。复杂个性化是低 ROI 投入。

---

## 对当前设计的具体含义

### 5.1 复盘工具（trade-journal-template.md）应该长什么样

**当前推断的字段（基于 system_spec_v2.md L80-82）：**
- 时间、标的、方向、仓位、理由、下单前情绪、平仓结果、持仓期间情绪、是否遵守计划、行为偏误标记
- ≈ 10+ 字段，已接近"reflection-as-task"风险线

**修正建议（基于本笔记证据）：**

**入场记录（≤ 5 字段，强制）：**
1. 决策链 ID（自动生成）
2. setup type（从预定义列表选，不写自由文字）—— 注意：单一 setup focus（05 笔记 Q7）应在此体现为"从你的 1 个 setup 列表中选"
3. 入场截图（自动）
4. 止损位（强制数字字段）
5. 自由文字 1（≤ 100 字，"我现在的判断是..."）

**触发显示：honesty oath**（Capraro 2024 风格）："我承诺如实记录，无论结果如何。"

**平仓记录（≤ 4 字段，强制）：**
1. 平仓截图（自动）
2. 是否触发预定止损 / 止盈 / 主动调整（三选一）
3. 我是否遵守了入场时的计划（是 / 否 / 部分）
4. 自由文字 2（≤ 100 字，"我学到的是..."）

**这是 9 个字段，远低于当前隐含的 10+。情绪追踪、偏误标记、详细复盘都推到周复盘。**

**周复盘（30-60 分钟，高价值时段）：**
- AI 自动报告（决策链遵守率、setup 表现、按时段 / 按情绪上下文统计）
- AI 生成 3 个主要问题（基于本周数据）
- 用户回答 + AI 跟进
- 月底 + 季底叠加 future-self 模块（每月一次写信给 5 年后的自己）

**违规反馈格式（wise feedback）：**
- "你这周决策链遵守率从 78% 降到 62%。这是一个我们之前讨论过的边界。"（高标准）
- "我看到这周连续 3 笔亏损后第 4 笔仓位放大了。这是一个常见的反应。"（事实，不评判）
- "下周我们能不能重新激活'连亏 2 笔后强制减半仓位'这条规则？"（明确"我相信你能做到"）

### 5.2 整体训练系统的留存策略

**反对的策略：**
- 推送通知频率最大化
- DAU/WAU 最大化作为成功指标
- streak / leaderboard / 积分 / 徽章
- "AI 教练永远温暖鼓励"
- 复杂个性化引擎

**支持的策略：**
- **Critical engagement threshold 而非 maximization**：定义"足够使用"为"每笔交易经过决策链 + 周复盘 1 次"，超过此就不追求；
- **明确"工具型"定位**：每次打开有清晰目的，避免无聊浏览；
- **极简核心字段 + 扩展周复盘**：日填空压力小，周深度时间长；
- **Honesty oath**作为入门时和每次交易记录的固定显示；
- **wise feedback 风格的 AI 教练**：高标准 + 明确信任；
- **入门简短人格评估**：识别高 ruminator 用户 → 切换到 action-focused 模板；
- **future-self 月度模块**作为周期性诚实锚点；
- **Stage 4 退出协议**（05 笔记建议）：当数据告诉我们应该停止时，系统主动建议停止——这是终极诚实。

### 5.3 哪些"看起来好"的设计应该避免

| 看起来好的设计 | 为什么应该避免 |
|---|---|
| 365 天连续 streak 徽章 | 把"该不交易就不交易"反向激励 + Duolingo 数据显示长期学习效果反而下降 + 焦虑驱动留存不可持续 |
| 排行榜（"你比 80% 用户更纪律性"） | FCA + Hueller 直接实证：在金融场景增加风险偏好；在 σ 引擎里会让用户为了排名调整记录 |
| 每笔交易后 12 个字段的精细情绪 / 偏误标记 | reflection-as-task 退化（Boud, Beighton）；时间投入是头号弃用原因（Honary 2023）；填了也是噪音 |
| AI 教练"温暖共情"作为优化目标 | sycophancy（Sharma, Cheng）+ satisfaction-effectiveness 负相关（Stanford SCALE）+ 高 ruminator 反刍激活（Watkins）|
| 公开分享我的交易日志到社区 | Munson 2015 减少 commitment + 选择偏差（公开有意识地选择某些记录） + Robinhood 学到的"social trading"灾难 |
| 大额 deposit contract（"输了罚 $1000"）作为强制 | John 2020 Management Science 55% 违约 → 双重伤害；适合作为 advanced 用户可选模块 |
| 复杂的"机器学习个性化"承诺 | 个性化文献证据 "scarce and inconclusive"；好的 default 比花哨个性化更重要 |
| "每天 30 分钟交易学习时间"目标 | 与交易纪律根本矛盾；交易者真正需要的是"高质量决策时刻"，不是"长时间打开 App" |

---

## 引用清单

### 同行评审（S 级）

**留存 / 弃用 / engagement：**
- Meherali, S., et al. (2020). *Journal of Medical Internet Research*, 22(9):e20283.
- Linardon, J., Fuller-Tyszkiewicz, M. (2019). *Journal of Affective Disorders*. (mHealth attrition)
- Linardon, J., et al. (2024). *BMC Digital Health*. ("Engagement and retention" narrative review)
- Mohr, D. C., et al. (2023). *Current Treatment Options in Psychiatry*. ("The Engagement Problem")
- Honary, M., et al. (2023). *JMIR mHealth and uHealth*.
- Klasnja, P., et al. (2018). *JMIR mHealth*. (microrandomized push trial)
- Pratap, A., et al. (2020). *npj Digital Medicine*. (mHealth real-world engagement)
- Wrzus, C., Neubauer, A. B. (2023). *Assessment*. (EMA compliance)

**习惯形成：**
- Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., Wardle, J. (2010). *European Journal of Social Psychology*, 40, 998-1009.
- de Wit, S., et al. (registered). "How long does it take to form a habit?: A Multi-Centre Replication." Peer Community in Registered Reports.
- Singh, B., et al. (2024). *Healthcare*, 12(23):2488.
- Sheeran, P., Listrom, O., Gollwitzer, P. M. (2024). *European Review of Social Psychology* (642 tests meta).
- Wieber, F., Thürmer, J. L., Gollwitzer, P. M. (2024). *Annual Review of Psychology*.
- Buyalskaya, A., et al. (2023). *PNAS*. (ML on habit formation)
- Gardner, B., et al. (2019). *Frontiers in Psychology*. (perceived complexity moderation)
- Phillips, L. A., Gardner, B., et al. (2022). *Behavioural Sciences*.

**Tiny Habits / Fogg：**
- Cebolla i Martí, A., et al. (2022). *Frontiers in Public Health*. (Tiny Habits gratitude RCT)
- Fogg, B. J. (2009). "A behavior model for persuasive design." *Persuasive Technology*.
- Scoping review (BMC Public Health 2025, PMC12522219).

**游戏化 / overjustification：**
- Deci, E. L., Koestner, R., Ryan, R. M. (1999). *Psychological Bulletin*, 125(6), 627-668.
- Cameron, J., Pierce, W. D. (1994/1996). *Review of Educational Research*. (反对 meta)
- Zeng, J., et al. (2024). *British Journal of Educational Technology*.
- Shi, Y., et al. (2023). *Frontiers in Psychology*.
- Larson, E. J., et al. (2024). *Educational Technology Research and Development*. (SDT meta on gamification)
- Yan, Z., et al. (2024). (digital health gamification meta of 36 RCTs)
- Hueller, C., Reimann, M., Warren, C. (2023). *Journal of the Association for Consumer Research*.
- Capraro, V., et al. (2024). *Nature Human Behaviour*. (honesty oaths megastudy)
- Patel, M. S., et al. (2021). *Annals of Internal Medicine*. (loss aversion in gamification)
- Liu, F., et al. (2023). *Information Systems and e-Business Management*. (adverse effects scoping)

**交易 / Robinhood / DEP：**
- Barber, B. M., Huang, X., Odean, T., Schwarz, C. (2022). *Journal of Finance*. (attention-induced trading)
- Cookson, J. A., Engelberg, J., Mullins, W. (2025). *International Review of Financial Analysis*. (Robinhood high-frequency)
- Kalda, A., et al. (2024). *European Journal of Finance*. (trading apps over time)
- Apesteguia, J., et al. (2024 SSRN). "Gamification of Stock Trading: Losers and Winners."
- Linnainmaa, J. T. (2011). *Review of Financial Studies*. (Finland data on losing traders)

**反思日志 / 复盘：**
- Boud, D., Keogh, R., Walker, D. (1985, 2020). *Reflection: Turning Experience into Learning*. Routledge.
- Beighton, C. (2017, 2021). "Convergent correlationism."
- Müller, S. M., Seufert, T. (2020). *Educational Psychology Review*.
- Cipriano, M.C., Gruca, T.S., Jiao, J. (2020). *Journal of Prediction Markets*, 14(1).
- Bernstein, E., Gino, F., Staats, B. (2014). HBR Working Paper. ("Learning by Thinking")
- Eppich, W. J., Cheng, A. (2019). *BMC Medical Education*.
- Tannenbaum, S. I., Cerasoli, C. P. (2013). *Human Factors*. (debrief meta)
- Lessard, V., et al. (2022). *BMC Medical Education*.
- Corral, D., et al. (2021). *Quarterly Journal of Experimental Psychology*.
- Rojas, D. C., et al. (2020). *Surgical Endoscopy*. (video feedback)
- Mohamed et al. (2020). *Critical Care Medicine*.
- Sawyer, T., et al. (2012). *Simulation in Healthcare*.
- Cao, Y. (2021). *Frontiers in Psychology*. (peer vs self feedback)
- Wesemann et al. (2024). *BMC Medical Education*.
- Eva, K., et al. (2025). *Cognition, Technology & Work*. (multi-source + facilitation)
- Aronson, L., et al. (2017). *Perspectives on Medical Education*.
- Ehab et al. (2025). *BMC Medical Education*. (feedback + reflection)

**AI 谄媚 / wise feedback：**
- Sharma, M., et al. (2024 ICLR). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548.
- Cheng, M., et al. (2025). "ELEPHANT: Measuring social sycophancy." arXiv:2505.13995.
- Sharot et al. (2025). "Be Friendly, Not Friends." arXiv:2502.10844.
- Hong, R., et al. (2025). ACL Findings.
- Yeager, D. S., Cohen, G. L., et al. (2014). *Journal of Experimental Psychology: General*. (wise feedback)
- Cohen, G. L., Steele, C. M., Ross, L. D. (1999). *PSPB*. (mentor's dilemma)
- Lewis, P., et al. (2024 working). SSRN 4870270 ("hidden harshness of growth mindset")
- Fitzpatrick et al. (2017). *JMIR Mental Health*. (Woebot RCT)
- Darcy, A., et al. (2021). *JMIR Formative Research*. (Woebot bond at scale)

**AI feedback critical vs encouraging：**
- Stanford SCALE (2024-2025). "Directive, Metacognitive Or A Blend Of Both?"
- arxiv:2604.07469. "Sequenced AI feedback."
- arxiv:2512.04630. "Reflection-Satisfaction Tradeoff."

**认知负荷 / 表单 / EMA：**
- Sweller, J. (1988-2020). 多篇 Cognitive Load Theory 文献。
- JMIR Formative (2024). EMA compliance burden.
- Smyth, J. M., Stone, A. A. (2003). EMA methodological foundations.

**Honesty / commitment / future self：**
- Lelkes, Y., Krosnick, J. A., et al. (2012). *Journal of Experimental Social Psychology*. (anonymity compromises)
- Vannette, D. L. (2017). *PNAS*.
- Hershfield, H. E., et al. (2011). *Journal of Marketing Research*. (future self VR)
- Ersner-Hershfield, H., et al. (2009). *Judgment and Decision Making*.
- Grekin, E. R., et al. (2025). *American Journal of Lifestyle Medicine*. (future-self systematic review)
- Royer, B., Stehr, M., Sydnor, J. (2015). *AEJ Applied*.
- Halpern, S. D., et al. (2015). *NEJM*. (financial incentive smoking)
- John, A. (2020). *Management Science*. ("When Commitment Fails")
- Munson, S. A., Consolvo, S. (2015). CHI. (public commitments)
- Yano, M., et al. (2024). *PLoS ONE*. (Minchalle commitment app)
- Hsiao et al. (2024). NBER. ("Friends with Health Benefits")

**Personality / 个性化 / rumination：**
- Stieger, M., et al. (2021). *PNAS*. (PEACH personality change app)
- Smith, A. P., et al. (2020). *Behaviour Change*. (journaling moderated by self-reflection)
- Trapnell, P. D., Campbell, J. D. (1999). *JPSP*. (rumination vs reflection distinction)
- Watkins, E. R. (2008, 2020). *Psychological Bulletin*. (depressive rumination review)
- Linardon, J., et al. (2024). *PLOS Digital Health*. (tailored DMHI review)

**Desirable difficulties / productive struggle：**
- Bjork, R. A. (1994). In *Metacognition: Knowing about Knowing*.
- Bjork, E. L., Bjork, R. A. (2011). *Psychology and the Real World*.
- Soderstrom, N. C., Bjork, R. A. (2015). *Perspectives on Psychological Science*.
- Karpicke, J. D., Roediger, H. L. (2008). *Science*.
- Adesope, O. O., et al. (2017). *Review of Educational Research*.
- Kapur, M. (2008, 2014, 2023). 多篇 productive failure 文献。
- Hiebert & Grouws (2007). Handbook of Research on Math Teaching.
- Donoghue & Hattie (2021). *Frontiers in Education*.

**Behavior change taxonomy：**
- Michie, S., et al. (2013). *Annals of Behavioral Medicine*. (BCT v1)
- O'Brien et al. (2023). Umbrella review of digital health BCTs.
- NICE NG183 (2020). Behaviour change: digital and mobile health interventions.

**Friction in HCI：**
- Cox, A., et al. (2016). CHI. "Design Frictions for Mindful Interactions."
- Mejtoft, T., et al. (2022, 2024). Frictions SIG proposal & papers.

### 监管 / 大数据 (M 级)

- FCA (2024). "Research Note: Digital engagement practices: a trading apps experiment."
- FCA (2025). Occasional Paper 66: "Playing the market."
- FCA (2024). "Multi-firm review of trading apps: high-level observations."
- US Army FM 25-101 / DTIC ADA368651 (1990s-2010s). After Action Review.
- NICE NG183 (2020).

### 行业 / 灰色 (W 级)

- Duolingo Engineering Blog (2018-2024). Streak A/B 实验。
- Lennyrachitsky / Lenny's Newsletter (2024). Duolingo growth case study.
- TradingJournal.com (2026). Trustpilot 1,201 reviews 分析.
- LedgerMind (2025). 交易日志留存综合.
- TradeLens (2025). "10,000+ Trading Journals" 数据.
- Datafield "Algorithmic Addiction" (2024). Streak mechanics 综合.
- Atticus Li (2024). Form design 综合.
- NN/G (Nielsen Norman Group). Form design 系列.
- Morningstar (2024). "Risky Play" 评论.
- Edgewonk / TraderSync / TradeZella 自报数据.

### 不确定 / 未直接验证

- "Tinghög 2023" 用户提及但我未能在搜索中直接命中——相邻文献（Capraro 2024 megastudy；Cohn 2014 Nature on banking culture honesty）一致表明 game framing 增加作弊。如果用户能提供 Tinghög 引用全名我可以二次验证。
- "TradingView user behavior study" 仅在 LedgerMind 二手转述中见到——未找到原始研究。当作 W 级估值。

---

## 后记：这份调研 vs 用户原始假设

用户的原始假设："实际效用 ≈ 证据强度 × 实际使用率"，"工具好用比证据强更重要"。

**调研后的修正：** 这个假设**部分成立**，但比想象中更复杂——

1. **"实际使用率"不是连续变量，而是阈值变量**。critical engagement threshold 之上的边际收益迅速递减。这意味着"工具用得多"不是好的优化目标，"用户跨过 critical threshold 并维持"才是。

2. **"工具好用 = 用户 satisfaction 高"在 AI feedback 上反而是负面信号**。Stanford SCALE / Karpicke 多份证据显示：让用户最满意的工具方式让他们学得最差。

3. **"证据强但用户放弃"和"证据弱但用户坚持"是真问题，但解决方向不是降低证据强度，而是降低证据强方法的用户成本**：
   - 砍字段
   - 自动化数据采集
   - wise feedback 而非批判 / 鼓励
   - 中等 friction 而非高 friction
   - 移除 streak / leaderboard 等"留存帮手"的副作用

4. **核心矛盾的处理路径不是"二选一"，而是"分层解决"**：诚实激励放在低成本通道（honesty oath、自动截图）；留存激励放在与诚实相容的通道（wise feedback、清晰可见的进步、个人意义而非游戏化）。

**对用户的诚实回答：** 你的论点方向正确，但精确表述应该是：

> **"让用户跨过 critical engagement threshold 并维持的能力，是工具效果的乘数。但'让用户喜欢用'不等于'让用户用得好'——前者经常误导后者。优秀的训练工具应当：让用户能够使用（克服弃用率）+ 使用方式正确（克服 satisfaction-effectiveness 反向相关）+ 使用时是诚实的（克服自我欺骗）—— 这是三个独立维度，不能合并为'好用就好'。"**

这就是为什么当前 σ 引擎设计需要的修改不是"变得更花哨易用"，而是 6 项具体的、有强证据支持的、彼此协同的小修改（if-then 决策链 + honesty oath + 字段砍半 + wise feedback + future-self 月模块 + 反 streak/leaderboard）。**这些修改单独看都不"性感"，组合起来是当前设计能从"靠假设运行"升级到"靠证据运行"的唯一路径。**
