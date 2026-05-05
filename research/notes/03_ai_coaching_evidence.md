# AI 辅助/AI 教练在专业训练中的效果调研

> 调研日期：2026-05-05
> 调研方法：Web 检索（Nature/Springer/Wiley/PNAS、JAMA Network Open、Educational Psychology Review、SSRN、arXiv、MIT Media Lab、METR、Microsoft Research、ERIC 等）
> 证据等级：S（同行评审、可复现/方法学透明）/ M（专业出版/可信数据/工作论文）/ W（行业博客、营销材料、未独立验证）/ U（基于已知文献的逻辑推演）
> 上下文：本笔记是为交易员训练系统的 AI 教练组件做证据评估而写。前两份调研已完成（01 日志范式、02 散户失败根因），本文专门评估"把 AI 当作教练/守门人/反馈者"这一设计的实证基础。

---

## 摘要

1. **"AI 作为辅导者能加速学习"在 2023-2026 的元分析中被反复支持**，效应量大约在 g = 0.39 ~ 0.87 之间（异质性高），与 VanLehn 2011 报告的 ITS 效应量（d ≈ 0.76）量级一致。但**几乎所有这些研究的因变量是"考试成绩 / 知识测验 / 一次性任务表现"，不是"长期行为改变"或"高度模糊的真实场景决策质量"——也就是不是交易场景**。
2. **存在一个稳健的、令人不安的反向证据**：当 AI 帮助被撤掉以后，使用过 AI 的人**比从未用过 AI 的人表现更差**（Bastani et al. 2024 PNAS：高中数学 −17%；Anthropic 2026 内部 RCT：编程理解 −17%；MIT Kosmyna et al. 2025：写作的脑连接度、记忆度、所有权感都最低）。METR 2025 RCT 还显示资深开源开发者用 AI 反而**慢 19%**——但他们自己以为快了 20%（感知-现实差距 39 个百分点）。
3. **交易/金融领域几乎没有同行评审的"AI 教练"研究**。"63% 表现提升"等数字全部出自商业产品营销或公司博客（HOC Trade、TradeUpCoach），未经独立验证。Robo-advisor 文献（D'Acunto, Rossi, Utkus）显示算法**确实能改善多元化和处置效应**，但**最需要帮助的人最不愿意用**，且加入"拟人化社交设计"反而恶化结果。
4. **"管住自己"的几个核心组件有强证据**：implementation intentions（d = 0.65, Gollwitzer & Sheeran）、self-explanation（g = 0.55）、metacognitive prompts（g = 0.40-0.50）、debiasing training（持续 2 个月、迁移到现场 +19% ~ +29%, Morewedge 等）、stop-loss/take-gain 作为 pre-commitment（实验上确实减少处置效应）。**但"用 LLM 实现这些组件"和"传统形式实现这些组件"的等效性，目前没有 trading 领域的实验数据。**
5. **"在下单前问 5 个问题"这种设计有部分支持，但不能套用 d 值**：implementation intentions / 反思 prompts / 自我解释的元分析效应量来自学校/健康场景，**不是交易场景**。Cipriano et al. 2020（写投资日记诱发过度自信，已在 01 笔记记录）和 Steiss et al. 2024（AI 反馈质量高但学生采纳更差）暗示设计良好的 prompt 也可能产生反效应。
6. **底线判断**：把 AI 作为"教练 + 守门人 + 反馈者"是一个**有理论支持、有相邻领域间接证据、但在交易场景上几乎没有直接验证**的工程假设。最大的已知风险是 (a) 自动化偏误 / 认知卸载使用户长期能力反而下降，(b) AI 幻觉给出错误建议被用户采纳，(c) 新颖效应消退后效果衰减。这些风险**已有 S 级证据，不是猜测**。

---

## Q1：AI 辅导/LLM 教练的最新元分析

### Q1.1 ChatGPT/LLM 时代（2023-2026）的元分析

【S 级，多项独立元分析，但效应量异质性极大】

主要元分析及其效应量：

| 元分析 | 研究数 | 主要效应量 (Hedges' g) | 备注 |
|---|---|---|---|
| Wang & Fan (2025, *Humanities & Social Sciences Comm.*) | n.r. | 学习成绩 g = 0.867；学习感知 g = 0.456；高阶思维 g = 0.457 | 偏向高估；多为短周期研究 |
| 35 项实验研究元分析 (Nature *HSS Comm.* 2026) | 35 | g = 0.670 | |
| Liu et al. (2025, *J. Computer Assisted Learning*, EJ1484315) | 34 | g = 0.68 (cognitive g = 0.795；competency g = 0.711；affective g = 0.507) | |
| Liu (2025, *JCAL*, jcal.70096) | n.r. | g = 0.577 | |
| 26 项研究元分析 (Springer *Education and Information Technologies* 2025) | 26 | g = 0.392 | "small overall effect"，最保守的估计 |
| 39 项实验/准实验元分析 (sciopen.com 2025) | 39 | g = 0.623 | |
| 52 项研究元分析（preprint, ResearchSquare 2025） | 52 | g = 1.193 | preprint，未审稿，可能存在 small-study bias |
| Meta-analysis on LLM effects, 133 studies (arXiv 2509.22725, 2025) | 133 | "uneven impact"；强效应来自 sustained tutor 干预 | 强调设计依赖性 |

**诚实标记：** 这些元分析的效应量分布在 g = 0.39 ~ 1.19 之间，**这种异质性本身是一个警示信号**——意味着"AI 是否有效"高度依赖具体设计、学科、人群、对照组选择。把它们平均成"AI tutoring works, d ≈ 0.5"是过度简化。

### Q1.2 老一代 ITS 元分析的延续

【S 级】

- VanLehn (2011, *Educational Psychologist* 46(4))：人类一对一辅导 d = 0.79；ITS d = 0.76；step-based ITS 与人类一对一辅导**统计上不可区分**。这是经典基准。
- Kulik & Fletcher (2016) 与 Ma et al. (2014) 对 ITS 的元分析支持 VanLehn 的结论。
- 2024 年 APA 综述 (psycnet 2024-91807-026)：ITS"learning gains rival human tutors"被新数据继续支持。
- 但 K-12 系统综述 (Nature *npj Science of Learning* 2025)：ITS vs **non-intelligent** tutoring systems 的优势"mitigated"（即 ITS 没有比普通练习题系统好太多）——**对照组的选择是核心**。
- Frontiers (2025) 941 名学生一年纵向研究：ITS 使用频率与学习收益**没有显著相关**。这是对"用得越多越好"假设的反例。

### Q1.3 Bloom 2-Sigma 问题与 AI 的现状

【S 级】

- Bloom (1984) 经典基准：一对一人类辅导 vs 普通课堂 = +2σ。
- 2025 EEF (Education Endowment Foundation) 元分析（83 项研究）：
  - 对话式 AI 教练（Khanmigo、GPT-based）：+0.62σ vs 无辅导
  - 传统 ITS（如 MATHia）：+0.45σ
  - 结构化练习系统（IXL、Khan Academy）：+0.25σ
- Stanford 2025 元分析：AI 辅导效应量 0.4-0.8σ，**比之前任何"可规模化干预"都接近 Bloom 的 2σ 目标，但仍低于一对一人类辅导**。
- 直接比较：对话式 AI 教练 vs 一对一人类辅导，gap = -0.20σ（AI 更差）。

### Q1.4 旗舰研究：单点支持但有方法学局限

**Kestin et al. (2024, Harvard, "PS2 Pal" study)**【S 级，但 n 小】
- 194 名学生，被试内交叉设计，AI 辅导（基于 ChatGPT，配置了教学规则）vs 主动学习课堂。
- 发现：AI 组学习更多、用时更短、自报告 engagement 显著更高。
- 限制：两个物理主题（表面张力、流体）；2 周；考试是"知识掌握"不是真实复杂决策。
- **诚实标记**：这是被广泛传播的"AI 教练击败教授"故事，但 n 小，对照组是大班课不是一对一辅导，**不能直接外推到训练高复杂度技能**。

**Bastani, Bastani et al. (2024, *PNAS*, "Generative AI without guardrails can harm learning")**【S 级，最重要的反例】
- 土耳其 TED Ankara Koleji 高中 ~1,000 学生；3 个臂：无 AI 对照、GPT Base（裸 ChatGPT）、GPT Tutor（带教学约束）。
- 在练习时：GPT Base 提升 48%、GPT Tutor 提升 127%。
- **AI 撤掉后的真实考试**：GPT Base 组比从未用过 AI 的对照组**差 17%**；GPT Tutor 组与对照组没有显著差异。
- **结论**：不带护栏的 AI 不仅没帮助学习，它**主动伤害了学习**。这一发现**是评估 AI 教练设计时最关键的单点证据**。
- 机制：用户把 AI 当"答案机器"，不再做认知工作；当外援撤走，技能并未真正掌握。

**Layered vs Direct Feedback (arXiv 2604.07469, 2026)**【S 级】
- 比较"分层鼓励 + prompt + 答案"的 scaffolding 反馈 vs 直接给出反馈。
- 发现：layered scaffolding **显著降低学习效果**，尽管 engagement 和正面感受上升。
- **这个反例与"AI 应该用 Socratic 提问而不是直接答案"的直觉相反**——精心设计的分层 scaffolding 也可能是认知卸载的伪装。

### Q1.5 哪些领域有效，哪些无效？

【S 级整体趋势 + M 级具体分布】

有效域（合理结构化 + 可验证的事实性知识）：
- 数学（Khan/Khanmigo + 传统 ITS 都有强证据）
- 编程入门（教学场景；与"职业开发"不同）
- 语言学习/阅读理解
- 医学结构化案例模拟（学生层面）

效果模糊或负面的域：
- 高阶批判性思维（Microsoft/CMU 2025、MIT Kosmyna 2025）
- 资深专家（METR 2025、JAMA Network Open 2024）
- 真实开放式工作环境（Anthropic 2026, METR 2025）
- 长期技能保持（一旦 AI 撤走）

**对交易训练的启示**：交易包含"有结构的部分"（执行规则、风险计算、知识点）和"高度模糊的部分"（环境识别、判断、决策）。**AI 教练在前者有相邻领域证据支持，在后者没有任何直接证据**。

---

## Q2：AI 教练在专业训练中的具体研究

### Q2.1 医学

【S 级】

- **Goh et al. (2024, JAMA Network Open, *"Large Language Model Influence on Diagnostic Reasoning"*）**：50 名内科医生 RCT，GPT-4 作为辅助资源 vs 传统资源——**诊断推理评分无显著差异**（中位数 76% vs 74%, p=0.60）。但 GPT-4 单独完成同样任务比两组医生**高 15-16 个百分点**——AI 比人强，但 AI 给医生用却没让医生更强。这是一个**关键悖论**。
- **Goh et al. (2024 medRxiv, *"Management Reasoning"*）**：92 名医生扩展 RCT，**LLM 辅助管理推理改善 6.5%（p<0.001）**——比诊断推理任务更易获益。
- **Schmidgall et al. (2024, *BMC Medical Education*)**：21 名医学生 RCT，4 次结构化 AI 反馈训练，临床决策评分显著提升（3.60 vs 3.02），强效应。但 N 小、学生层面、为期短。
- **影像学住院医（observational）**：LLM 帮助识别遗漏发现，住院医前期 vs 后期报告改善。
- **诚实标记**：医学是 LLM 教练研究最丰富的领域之一，但**结果分歧**——学生水平有效、专家水平往往没差异或略有损害（automation bias）。

### Q2.2 编程

【S 级 + M 级，最有冲突的领域】

**正面**：
- GitHub/Microsoft RCT（Peng et al. 2023）：n=95 开发者完成简单 HTTP server 任务，Copilot 组**快 55.8%**。但任务设定是简单且良定义。
- Accenture × GitHub 内部研究（n.r.）：宣称 +55% 速度。
- GitHub 内部 RCT 202 名经验开发者：通过单元测试的概率高 53.2%、错误率低 13.6%。
- Demirer et al. (2025, MIT Working Paper)：4,867 名开发者跨三个公司的 RCT，**任务完成 +26.08%**；新手获益更大。

**负面 / 修正**：
- **METR (2025) RCT**【S 级，最重要的反例】：16 名资深开源开发者，246 个真实 issue，AI 允许 vs 禁止随机分配。**用 AI 慢 19%**；但开发者预期快 24%、事后认为快 20%——**感知-现实差距 39 个百分点**。这是迄今为止"经验丰富的真实任务"最严肃的实验。
- **Uplevel (2025) 实地分析 ~800 开发者**：Copilot 对 cycle time/throughput/code quality "no significant improvement"；**bug 率上升 41%**【M 级，业界研究非同行评审】。
- **Anthropic (2026) RCT**【M 级，业界研究】：AI 辅助学习者在理解测验上比无 AI 学习者**低 17%**；将 AI 用作概念问答（"为什么"）的人得分 ≥65%，将 AI 当代码生成器的人得分 <40%。
- **Longitudinal repo 研究 (arXiv 2601.13597)**：早期接入 coding agent 时收益大、后续衰减；引入了 sustained 18-39% 的静态分析警告与认知复杂度上升——"agent-induced technical debt"。
- **CACM 2025 综述"AI Deskilling Paradox"**：AI 使专家技能衰退、阻碍学习者技能习得，且用户察觉不到这一过程。

**对交易训练的启示**：编程是 AI 辅助最被广泛使用的真实场景。**它的最佳证据混合，且最严肃的资深者 RCT 显示净负面**。这是反对"AI 一定有用"的直接经验数据。

### Q2.3 法律

【S 级】

- **Choi et al. (Univ. Minnesota Law Review 2024)**：法学院学生 RCT，GPT-4 在简单选择题上有帮助，**复杂论文题没有**。**底部学生改善、顶部学生表现下降**——一个"均衡器"效应。
- **AI Assistance in Legal Analysis (SSRN 4539836)**：N=70 研究生使用 AI，**速度大幅提升、质量略有提升**——典型 AI 模式。
- 法律写作工具（LegalWriter）N 小但显示结构化反馈能改善学生写作。

**启示**：与编程同模式——**AI 作为均衡器，对底部用户有帮助、对顶部用户可能有害**。如果交易者初期是新手（小白），方向上对 AI 有利。

### Q2.4 体育（运动技能）

【M 级，多为单点小规模研究】

- 网球 8 周 N=46 干预（preprint, 2024）：AI 视频分析使发球准确率 65→72%、速度 160→163 km/h，对照无变化。
- CoachMe (ACL 2025)：参考视频对比的运动指令生成模型，在花滑/拳击 instruction 质量上比 GPT-4o 提升 31.6-58.3%。
- Personalized Motion Guidance Framework (arXiv 2510.10496)：51 名棒球投手验证。
- **诚实标记**：体育领域研究多是工程展示，N 通常 <50，对照粗糙。运动技能客观可测（这是优点），但**研究质量整体低于教育/医学元分析**。

### Q2.5 沟通技能（演讲、谈判、工作沟通）

【M 级，多为小规模 pilot】

- 公开演讲机器人教练（IJSR 2025, N=50）：高接受度，专家验证反馈相关。
- AI 演讲教练焦虑研究：报告 25.2% 焦虑下降、60.5% 能力上升——但样本量与对照设计未透明。
- VR 谈判训练（HNU "Beat the Bot"）：VR + AI 学习成功超过传统角色扮演——单点。
- **重要的修正**（arXiv 2509.22545, 2025）：Trucey AI 教练 vs 传统手册，**手册在易用性和心理赋权上击败 AI**；AI 减少恐惧但其指导冗长片段化导致用户迷茫。
- **Japan RCT (Nature *Sci Rep* 2025, N=102)**：AI 正面反馈提升职场自我效能；负面反馈仅在用户有高情感支持时才提升——AI 反馈与人类支持是**互补而非替代**。
- **Quasi-experimental N=63 white-collar 工人**：单次教练后，**人类教练在洞察、工作联盟、目标达成、信任等所有维度上均高于 AI 教练（Alpina）**。
- **诚实标记**：沟通/教练领域的 AI 研究**普遍 N 小、对照弱、自报告占主导**。看起来正面，但证据强度低于学校/医学。

---

## Q3：AI 守门人 / 防止冲动的设计

### Q3.1 If-then 计划（Implementation Intentions）

【S 级，证据非常强】

- **Gollwitzer & Sheeran (2006, *Advances in Experimental Social Psychology*)**：94 项独立测试的元分析，**总效应 d = 0.65**（中到大效应），跨广泛行为目标。
- **更新元分析（Sheeran, Listrom & Gollwitzer，cited in kops.uni-konstanz）**：642 项独立测试，效应量 0.27-0.66 不等。
- **关键调节因素**：if-then 格式比一般意图更有效；高动机更有效；rehearsal 增强效果。
- 应用于冲动行为：implementation intentions 显著降低冲动认知、情感、行为（Achtziger 等多项研究）。

**对"在下单前问 5 个问题"的支持**：
- 这本质是一个 implementation intention（"在 X 情境下做 Y"）的 prompt 化版本。**在原型支持上有强证据**。
- 但**无任何研究专门测试"AI 实时执行 if-then prompt 是否比纸质 / 静态 checklist 更有效"**。

### Q3.2 Self-Explanation（自我解释）

【S 级】

- **Bisra et al. (2018, *Educational Psychology Review*)**：64 项研究、~6,000 被试元分析，prompted self-explanation **g = 0.55**（中-大效应）。
- 数学领域专门元分析：在程序性、概念性知识与迁移上有 small-to-moderate 改善。
- 关键调节：开放式 > 多选；高质量 scaffolding 增强；学习者熟练度变化时需调整。

**对训练系统的启示**：要求交易者在每笔交易前后做"自我解释"（你为什么入场？ 你看到的是什么？）有强证据支持——**前提是开放式自由文字而非选择题**。

### Q3.3 Metacognitive Prompts（元认知提示）

【S 级】

- **Zheng et al. (2022, *J. Computer Assisted Learning*, EJ1333210)**：CBL 环境下元认知 prompts 元分析——self-regulated learning 活动 g = 0.50；学习成果 g = 0.40。
- **2025 元分析（sciopen.com）32 项实验**：在线 SRL 上元认知 prompt 有正向效应。
- **Generative AI 环境下的 metacognitive support（ERIC EJ1479919, 2025）**：N=68 的 4 周准实验，无 metacognitive support 的学生**在 GenAI 环境下 SRL 水平反而下降**——重要警示。

### Q3.4 Forced Pause / 冷静期

【S/M 级，混合证据】

- 短暂强制等待（~1 秒）改善决策准确性，最小化认知负荷；2.5 秒等待反而增加 irritation（Nature *Sci Rep* 2025, s41598-025-87119-z）。
- **Imas, Kuhn et al. (SSRN 2880386, "Waiting to Choose")**：信息接收与选择之间插入等待期使 myopic（短视）选择**显著减少**。
- 消费者冷静期（cooling-off）40 年自然实验：实际取消率低（53% 商家报告"从不取消"）；**仅书面通知效果差，口头 + 书面更好**——纯被动通知效果有限。
- 在线赌博 RCT（N=4,328, naturalistic）：登记/首次充值时 prompt 设置存款上限**没有显著降低净亏损**——尽管设限率上升。**单纯 prompt 不够，需要执行机制**。
- 但小型 RCT（Auer & Griffiths 2014, N=43）：电子赌博机时间限制 pop-up **显著缩短赌博时间**。**信息特异性消息（"你已经亏了 X"）比通用消息有效**。

**对交易训练的启示**：
- 入场前 1-3 秒的强制 pause 有合理支持（不是大效应，但是低成本）
- **被动 prompt（"请确认"）效果弱**；具体化、与用户当前状态绑定的 prompt（"你今天已经亏了 ¥X，这笔交易让你接近日损上限"）效果更好
- **需要执行机制（自动化的、binding 的），不是建议**

### Q3.5 Pre-commitment in Trading

【S 级，但研究较少】

- **Fischbacher, Hoffmann & Schudy (2017, *Management Science*）**：实验显示 stop-loss / take-gain 订单作为 pre-commitment 工具**显著降低处置效应**；机制是增加亏损实现，不是减少盈利实现。
- **关键发现**：**reminders 无效，actual ex-ante commitment 才有效**。这与赌博 pop-up 研究一致。
- AEA 2022 working paper：人们计划时接受"loss-exit"风险但实践中早砍盈利、追加亏损；提供 commitment device 后接受风险的人变多——**说明计划自我与执行自我的脱节是结构性的**。

**对训练系统的启示**：硬约束（自动止损、日损锁屏）的证据**强于**软约束（提醒、问题）。系统设计应优先 binding mechanism，prompt 只是辅助。

---

## Q4：AI 反馈 vs 人类反馈

### Q4.1 写作场景

【S 级】

- **Steiss et al. (2024, *Learning and Instruction*)**：人类反馈在 5 个评判类别中 **4 项胜过 ChatGPT**（清晰方向、准确性、关键特征优先级、支持性语气）；ChatGPT 只在"基于评分标准"上更好。差距适中，考虑时间节省 ChatGPT 仍有用。
- **AI 与人类的"反馈质量 vs 学生采纳"悖论（Springer *IJETHE* 2026, s41239-026-00579-9）**：CoT prompt 产生的 AI 反馈**质量高于**教师反馈，但**学生作文修订改善并不更多**——质量好不等于影响行为。**这是一个对"AI 反馈更高质量 ⇒ 用户更进步"假设的直接反例**。
- AI 与同伴反馈：AI 提供描述性反馈、同伴识别问题——互补而非替代。
- 自动写作评估（AWE）元分析（Frontiers, 2023）：g = 0.55，但异质性很大。

### Q4.2 工作场景

【S/M 级】

- AI vs 人类管理（SSRN 4739430，14 周 pilot）：AI 教练 "HARRi" 行为改变效果**与人类管理者相当**；初步证据显示 AI + 人类组合最佳。
- AI 与情感支持的互补（Nature *Sci Rep* 2025, N=102）：AI 正面反馈直接提升自我效能；负面反馈需要人类社会支持的存在才有效。
- N=63 quasi-experimental：单次会话后 **人类教练在所有 8 项指标上均高于 AI 教练（Alpina）**——洞察、工作联盟、目标达成、承诺、信任、保密、shame 等。

### Q4.3 心理治疗（CBT 聊天机器人，与"教练-反馈"最接近的高质量证据带）

【S 级，但证据等级评定为 low-very low 因偏倚风险】

- **Meta-analysis (PubMed 41813041, 2025)**：CBT 聊天机器人对抑郁短期 g = -0.55、焦虑 g = -0.26；follow-up 时抑郁 g = -0.32，焦虑不显著。
- **Therabot RCT (NEJM AI 2025)**：MDD d = 0.85-0.90、GAD d = 0.79-0.84，8 周 follow-up 维持。**这是 LLM 心理教练目前最强的单点证据**——但是单一研究、与等待对照，需要更多复制。
- 引用作者自评："overall evidence certainty is **very low to low**"——**这一领域看似有效，但研究方法学整体薄弱**。

### Q4.4 AI 反馈的固有局限：幻觉与错误建议

【S 级，证据强】

- 临床摘要中：幻觉 1.47%，遗漏 3.45%（Nature *npj Digital Medicine* 2025）。
- 患者提问：4 个主流 chatbot 答 5-13% **不安全**，21.6-43.2% 有问题。
- 对抗性临床输入：幻觉率 50-82%；prompt 缓解可降到 44%（仍很高）。
- 综合医疗决策（1,000 合成 transcripts）：在某些情况 LLM 错误地"降级"威胁生命的紧急情况到自我管理或常规随访——高达 54.8%。

**对交易训练的启示**：交易领域的 LLM 输出错误率没有公开评估，但**几乎可以肯定不会低于医学**——市场环境的复杂性和对抗性高于规范化的临床问诊。AI 教练给出"看起来正确"的错误建议、用户因 automation bias 接受它，是结构性风险。

---

## Q5：AI 辅助元认知训练

### Q5.1 Metacognitive Prompts 在 AI/CBL 环境

【S 级】

- 直接元分析效应量见 Q3.3：g = 0.40-0.50。
- "Cognitive Mirror" 框架（Frontiers 2025）：把 AI 重新定位为"被教的学习者"而非"无所不知的源"——反直觉但理论上能减少 over-reliance。**但缺少强对照实验**。
- 在 GenAI 环境下，**没有 metacognitive support 的学生反而 SRL 下降**（ERIC EJ1479919, 2025）——这是"AI 帮你思考导致你不思考"的实验证据。

### Q5.2 Debiasing Training（AI 之前的传统证据）

【S 级，对训练系统设计有重要参考】

- **Morewedge et al. (2015, *Policy Insights from Behavioral & Brain Sciences*)**：单次 debiasing 训练，**互动游戏 ≥ -31.94% 偏误降幅**、视频 ≥ -18.60%；**2 个月后仍维持 -23.57% / -19.20%**。覆盖 confirmation bias、bias blind spot、归因谬误、锚定、代表性、社会投射等。
- **Sellier, Scopelliti & Morewedge (2019, *Psychological Science*)**：290 名研究生，**debiasing 训练迁移到现场**，未告知背景的商业案例上低劣方案选择率 -19~29%。
- 投资场景 debiasing：信息反馈干预降低处置效应，但 3 个月后衰减（Frontiers 2024）；理性与情感 warning 都能消除处置效应（Dobrich 等）。
- 经验采样训练对 myopic loss aversion 有效。
- **Morewedge 的训练形式是计算机互动游戏 + 个性化反馈——这与 LLM agent 的可能形式高度兼容**。

### Q5.3 自动错误模式识别（Pattern Recognition by AI）

【M-W 级，证据基本上在商业产品宣称层面】

- TradeUpCoach："Phase 0 研究"，使用屏幕活动 + 鼠标键盘 + 语音 + 生物识别预测 10-30 秒前的认知漂移——**未发表、无验证数据**。
- HOC Trade："63% 表现提升"——发表在 Medium 公司博客，**未经独立验证、未同行评审**。
- ZenTrader（Astor & Adam 2011, Springer LNCS）：GSR + 蓝牙告警的概念原型，n=12，发表在 INFORMS conference proceedings。**proof-of-concept，不是效应研究**。
- Atlantis Press 会议论文（Kerala 散户研究）：AI 辅助调节锚定、可得性 bias——单一研究、会议级别同行评审、N 与方法学不透明。

**诚实标记**：这是本调研最薄弱的证据带。**关于"AI 自动检测交易者偏误并给出实时反馈"的同行评审实证研究，截至 2026-05 我没有找到任何可信案例**。所有"63% 提升"、"3 倍盈利"等数字均出自商业产品营销。

---

## Q6：AI 教练的负面效应

### Q6.1 自动化偏误（Automation Bias）

【S 级，强证据】

- **Pathology automation bias（arXiv 2411.00998, 2024）**：病理专家在 **7%** 的时刻把原本正确的判断"翻"成 AI 的错误建议。时间压力下严重程度上升。
- **Trust & Reliance experiment (Computers in Human Behavior 2024)**：**仅"知道建议来自 AI"就足以引发 over-reliance**——即使 AI 与上下文信息和用户自身利益冲突，被试仍跟随。
- 皮肤科医生研究（JMIR 2025）：QA 330 个临床决策，识别"mere exposure effect"和"false confirmation bias"——医生在不确定时改正确诊断；AI 确认错误诊断阻止医生寻找替代信息。
- **关键发现**：trust calibration 是问题的核心，且很难做对。

### Q6.2 认知卸载（Cognitive Offloading）

【S 级】

- **MIT Kosmyna et al. (2025, "Your Brain on ChatGPT"，arXiv 2506.08872)**：N=54，4 个月，3 次同条件 + 第 4 次切换，EEG。**LLM 用户在神经、语言、行为各层面都最低**；脑连接最弱；自我引用准确度最低；所有权感最低。**Brain → LLM 切换者表现良好；LLM → Brain 切换者表现下降**——暗示依赖会形成。
- **Gerlich (2025, *Societies* 15(1))，N=666 调查**：AI 使用与批判性思维**显著负相关**，由认知卸载完全中介。年轻人 AI 依赖更高、CT 更低。**但是横断面相关研究，不能证因果**。
- **Microsoft × CMU (Lee et al. 2025, CHI 2025)**：N=319 知识工作者，936 条真实任务报告。**对 AI 越信任越不批判性思考**；CT 没有消失，而是从"参与思考"转为"验证 AI 输出"——**质变而非量减**。

### Q6.3 学习者长期能力下降

【S 级】

- Bastani PNAS 2024（已引）：高中数学，撤掉 AI 后比从未用过 AI **差 17%**。
- Anthropic 2026 RCT：AI 学习者理解 -17%。
- **CACM "AI Deskilling Paradox"（2025）**：综述论证 AI 助手**加速专家技能衰退**与**阻碍学习者技能习得**，并且用户**察觉不到**。
- METR 2025（已引）：资深开发者 -19% 速度，自我感知 +20%。
- **核心机制**：persistence（坚持）是学习的强预测因子；AI 削弱 persistence——10 分钟练习后撤掉 AI，使用者比从未用过 AI 的人更快放弃。

**对交易训练的启示**：这是反对"重度依赖 AI 教练"最强的证据带。它意味着如果设计错了，AI 教练会让交易者**长期能力下降同时自以为在进步**——而交易场景里"自以为进步"的代价是真金白银。

---

## Q7：交易/金融领域的具体研究

### Q7.1 直接关于"AI 教练改变交易行为"的研究

【几乎为空】

- **未找到任何同行评审的、设计严谨的、关于 AI 教练（chatbot/LLM 反馈/实时干预）改善散户交易行为的 RCT 或长期纵向研究**。
- 唯一接近的是 Kerala 散户研究（Atlantis Press 会议论文）：AI 辅助调节认知偏误的影响。**单一会议论文，不能作为强证据**。
- arXiv 2604.18373 / 2308.00016 / 2510.08068：研究 AI **agent**（不是人类）的偏误以及 agent 之间的反馈循环。**与人类 trader 教练的研究目标不同**。

### Q7.2 商业产品独立学术评估

【完全空缺】

- TraderSync、Edgewonk、TradeZella、TradeNote、HOC Trade、TradeUpCoach、NeuroTrader、M1NDTR8DE：**全部没有独立同行评审用户研究**。所有"提升 X%"宣称来自营销材料。
- TraderSync 的 "Cypher AI" 教练功能：未独立验证。
- TradeZella 的 8 类测试评分（9.4/10）来自 TradingJournal.com 的内部评测——非学术评估。

### Q7.3 Robo-advisor（最相关的金融领域 AI 干预）

【S 级】

- **D'Acunto, Prabhala & Rossi (2019, *Review of Financial Studies*, "The Promises and Pitfalls of Robo-Advising"）**：使用 robo-advisor 后投资组合更分散、降低 home bias、降低费用、增加被动 + 债券、减少现金 + 个股、Sharpe ratio 上升、风险下降。
- **Rossi & Utkus (2024, *J. Financial Economics*）**：扩展确认；同时显示 robo 服务**减少投资者花在管理上的时间**——一种功能性卸载。
- **Reher & Sokolinski (2024, RFS)**：**最受益者是原本多元化差、低股票暴露、缺乏经验、高现金、高费用基金的投资者**——也就是新手最受益。
- **Hodge et al. (2023, *J. Behavioral Finance*）社交设计反例**：当 robo-advisor 加上拟人化设计（人名、自然语言）时，**处置效应反而变大、表现变差**——因为用户咨询变少。**这是一个微妙的负面证据：让 AI 教练"更人性化"未必改善行为**。
- **算法厌恶**（experimental, 2021）：**最差的交易者最不愿意采用 robo-advisor**——选择性偏倚。能选择性 override 时算法厌恶下降。

### Q7.4 EEG / 生物信号 + AI 干预

【M 级，多为概念验证】

- *Sensors* 2023 (sensors-23-03474)：EEG + 深度学习分类交易者情绪。带止损/限价的交易者情绪更正面；不带的更负面。**但是分类研究、不是干预效应研究**。
- ZenTrader（Astor & Adam 2011）：proof-of-concept，n 小。
- 一项研究（Monash, 2024）：心率"先行"于下单的交易者赚得更多——**相关性研究，不是干预**。

**底线**：交易领域的"AI 教练"是一个**理论上合理、产品市场已经形成、但没有学术验证基础**的状态。这与教育、医学领域的研究密度形成强烈对比。

---

## Q8：AI 助手长期使用对人的影响

### Q8.1 资深专业者负面证据

【S 级】

- METR 2025（详见 Q2.2）：资深开源开发者 **-19% 速度**，自评 +20%——感知-现实差距 39 分。
- Microsoft × CMU 2025（Lee et al.）：知识工作者使用 AI 时 CT 未消失而是**重定向到 AI 输出验证**；高 AI 信心 ⇒ 低 CT。
- Goh et al. JAMA Network Open 2024：内科医生用 GPT-4 诊断推理无改善。

### Q8.2 学习者新颖效应消退

【M 级】

- 2024 Frontiers ITS 940 学生一年研究：使用频率与学习收益无显著关联——暗示新颖效应可能贡献了短期效应估计。
- ChatGPT 学习元分析中：**4-8 周或 5-10 周时效果最大**（Liu 2025），更长干预未必有更大效果——这暗示某种新颖性 + 短期参与机制。

### Q8.3 长期写作技能

【S/M 级混合】

- Warwick 2025 大型研究 4,820 名本科生 2016-2025 跨期论文：**写作风格变得更正式、出现 ChatGPT 词汇标记，但实际成绩与反馈无显著变化**——这是一个有趣的"风格漂移但能力未降"的横断面证据。
- arXiv 2502.02880 "Coach not crutch" 实验：在某种设计下，AI 比 Google 例子或人类编辑反馈更能改善写作——同时降低用户精力。**可能的反例**。
- MIT Kosmyna 2025（认知债务）：4 个月，LLM 组持续表现更差、神经连接更弱。

**综合**：长期效果的证据**整体倾向负面或零**，但有少数设计良好的干预显示正向迁移。**关键变量是 AI 是否被设计成"促人思考"还是"代替思考"**。

---

## Q9：理论模型在 AI 教练中的实证验证

### Q9.1 Vygotsky ZPD / Scaffolding

【S/M 级】

- ZPD 与 scaffolding 被广泛引用为 LLM 教学的理论基础。
- 实证：175 名学生的 quasi-experimental 显示 scaffolded GenAI 使用提升知识、CT、reflective use，认知负荷下降（MDPI Education 2025）。
- 反例：**layered scaffolding 反而降低学习成果**（arXiv 2604.07469, 2026），尽管 engagement 上升。
- 28% 学生被动接受 AI 答案不批判审视（Calculus limit study, JITE 2024）。
- "Tool, tutor, or crutch?"（Springer 2025）：grounded theory 显示 AI 既可作支架也可作卸载，**取决于学习者参与方式**——不是工具属性而是使用模式。

### Q9.2 Socratic Tutoring（提问式 AI 教练）

【S 级，但结果令人意外】

- **Stanford SCALE Initiative (2024) RCT N=122 高中生**：Socratic AI vs 非 Socratic AI——**Socratic 显著提升 engagement 与 interaction，但学习提升不显著，部分学生觉得不够有用**。step-by-step reasoning 反而对简单预测题提升表现。
- Georgia Tech N=173 本科：Socratic AI 在难度上升时缓冲表现下降——"buffering effect"。
- **Retention 限制**：AI 移除后学生应用所学到新情境困难。

**与"在下单前问 5 个问题"设计的相关性**：Socratic 提问的实证证据是**engagement 增加，知识获取不一定**——意味着用 Socratic prompt 守门可能让交易者觉得"被认真对待"，但**不能保证他们因此变得更好**。这与 "implementation intentions 有效" 是不同维度的证据。

### Q9.3 Self-Determination Theory（SDT）

【M 级】

- Yang & Aurisicchio 在 SDT 框架下提出 10 条对话式 AI 设计指南（自主、胜任、关联）——**指南级，非实验验证**。
- HNU EFL 学习者研究：autonomy 中介 perceived support 与 engagement——支持 SDT 框架适用。
- Frontiers 2026 高等教育研究：agentic AI 感知影响 autonomy 支持感受，影响自学动机。**多为感知-感知关联，非客观成果**。

### Q9.4 角色比较：什么样的 AI 教练最有效？

【M 级综合】

- **教学者/答案给予者**：短期任务表现高，长期技能保持差（Bastani 2024）。
- **Socratic 提问者**：engagement 高，学习收益不一定更高（Stanford 2024）。
- **反馈者**：质量与效果脱节（Steiss 2024、IJETHE 2026）。
- **"被教的学习者"（Cognitive Mirror）**：反直觉地可能减少卸载——但缺少强对照实验。
- **同伴**：未见严肃对照实验。

**整合判断（U 级）**：有效的 AI 教练设计可能不是单一角色，而是**根据用户当前阶段动态切换**——新手期偏教学者+反馈者，进阶期偏 Socratic 提问者，专家期偏审计者。但这是合理推断，**没有实验数据支持**。

---

## 综合判断：对交易训练系统设计的启示

### A. 强证据支持的设计选择

| 设计 | 主要证据 | 效应量级 | 证据等级 |
|---|---|---|---|
| 入场前 if-then 计划 prompt（"如果价格 X，就 Y"） | Gollwitzer & Sheeran 2006 | d ≈ 0.65 | S |
| 要求开放式自我解释（"为什么入场？"） | Bisra et al. 2018 | g ≈ 0.55 | S |
| 元认知 prompt（"你在做什么阶段的判断？"） | Zheng et al. 2022 | g ≈ 0.40-0.50 | S |
| 硬 pre-commitment（自动止损、日损锁屏） | Fischbacher et al. 2017 | 显著降低处置效应 | S |
| 1-3 秒强制 pause | Nature *Sci Rep* 2025 | 改善准确率，最小化负担 | S |
| Debiasing 训练（互动游戏 + 个性化反馈） | Morewedge et al. 2015、Sellier et al. 2019 | -19~32%，2 个月持续 | S |
| 结构化、个性化反馈而非通用建议 | Auer & Griffiths 2014 (gambling) | 监管干预级 | S |

**这些设计的元素与组件已被验证；但"以 LLM 实时执行它们的版本是否等效于传统形式"没有交易领域的直接验证。**

### B. 合理推断但无直接交易证据（U 级）

- "AI 实时识别用户当前的偏误模式并给出对应反馈"——理论合理（Morewedge 训练是离线的，把它做成实时是工程外推）；但无 trading RCT。
- "AI 帮交易者复盘并提取模式"——比"AI 帮医生诊断"难度更高（市场噪声更大、反馈滞后），但未被研究。
- "AI 作为同伴/伙伴而非权威"减少 automation bias——理论方向正确（Cognitive Mirror）但缺实验。
- "Socratic AI 比 Direct AI 更适合训练高复杂度技能"——直觉支持，Stanford 2024 RCT 在高中阶段未证实。

### C. 应该警惕或避免的设计（有反证据）

| 应避免 | 反证据 | 等级 |
|---|---|---|
| 让 AI 直接给出"该不该交易"的判断 | Bastani PNAS 2024（撤掉后 -17%）；automation bias 7% 翻判（pathology） | S |
| 重度依赖 AI 让用户在每个决策点都向 AI 确认 | MIT Kosmyna 2025（神经连接最弱、所有权最低）；Lee et al. 2025（CT 退化）；CACM 2025 综述 | S |
| 让 AI 反馈"听起来高质量"但变成被动消费 | Steiss 2024、IJETHE 2026（质量与影响行为脱节） | S |
| Layered Scaffolding 优先（鼓励→提示→答案） | arXiv 2604.07469（学习成果反而下降，尽管 engagement 上升） | S |
| 拟人化、社交化的 AI 教练（"你的虚拟朋友"） | Hodge 2023 robo-advisor 社交设计→处置效应增大 | S |
| 仅靠被动 prompt（"请确认你确认要下单"） | 在线赌博 RCT N=4,328 显示 prompt-only 不降低净亏损 | S |
| 假设 AI 反馈与人类教练等效 | N=63 quasi-experimental 显示人类教练在所有 8 项指标上更好；JAMA Network Open 2024 显示资深医生使用 LLM 无改善 | S/M |

### D. 给本训练系统的具体修正建议（U + 推断）

基于上述证据，**σ 引擎（管住自己）** 部分如果继续以 AI 为核心组件，应做以下修正：

1. **AI 不是裁判，是 Socratic 提问者 + 行为日志记录者 + 模式识别建议者**——不是"AI 说不行就不行"的最终决策者。最终决策权与责任明确归交易者。
   - 证据：Bastani 2024、Lee et al. 2025、CACM 2025

2. **关键的"硬约束"必须 binding，不能依赖 AI 提醒或用户意志**——日损锁屏、止损在执行层、单笔风险硬上限。AI 只在 binding 之上做软层。
   - 证据：Fischbacher 2017、在线赌博 RCT 2021

3. **入场前 5 个问题** 的设计要：
   - 开放式而非选择题（self-explanation literature）
   - 与当前状态绑定的具体化（"你今天已经亏了 ¥X"），不是通用模板
   - 1-3 秒最低 pause 强制
   - 答完后允许 override，但 override 本身被记录
   - 证据：Bisra 2018、自我解释 g = 0.55；Auer & Griffiths 2014

4. **AI 反馈应明确其错误率与不确定性**，不要呈现为"AI 说……所以……"。降低 automation bias 的关键设计。
   - 证据：Pathology 7% 翻判、Trust & Reliance 实验

5. **必须设计"独立练习 → 与 AI 对照 → 反思差异"循环**，避免连续 AI 暴露下的认知卸载。
   - 证据：MIT Kosmyna 2025（Brain → LLM 路径表现良好，LLM-only 路径表现最差）

6. **每周/每月的 debiasing 干预 + 对自身模式的总结**——把 Morewedge 模型移植到交易场景。
   - 证据：Morewedge 2015、Sellier et al. 2019

7. **用户长期表现追踪应包括"AI 撤掉一周看看会怎样"的能力测试**——主动检测自己是否产生卸载。
   - 证据：Bastani 2024、METR 2025（无此测试用户会高估自己的能力）

8. **不要做"AI 朋友 / 拟人化人格化"**——已有反例。AI 应是冷静的工具。
   - 证据：Hodge 2023

### E. 最大的诚实

本设计的核心赌注是：**"用 AI 实时执行已经被验证的元认知/守门组件，是否能在散户交易这个未经测试的场景中产生正向作用"**——这句陈述的每个部分单独有证据，但整体是一个未验证的工程假设。

**这意味着：**
- 不能宣称"AI 教练能让你成为好交易员"——没有证据
- 可以宣称"我们用了一组在相邻领域被验证的工具，并在交易场景里测试它们"——这是诚实的
- **必须建立你自己的反馈数据**：每月跟踪自己的"使用 AI 时表现 vs 不使用 AI 时表现"——这就是你的个人级 RCT
- 必须随时准备**否定自己的设计假设**——如果半年后数据显示你越用 AI 越差，应当撤掉而不是优化它

**对训练系统建设阶段的建议**：
- **不要把 AI 教练定为系统核心**——它是一个增强层，不是基础层
- 基础层应是：交易日志（即使 01 笔记显示日志范式整体未验证）+ 硬约束（pre-commitment）+ 周期性 debiasing 训练
- AI 在每一层都可以辅助（生成提问、识别模式、撰写反馈），但**它的失败应当被设计成不致命**

---

## 引用清单

### Q1：AI 辅导/LLM 元分析
- VanLehn, K. (2011). The relative effectiveness of human tutoring, intelligent tutoring systems, and other tutoring systems. *Educational Psychologist*, 46(4).
- Wang, J., & Fan, W. (2025). The effect of ChatGPT on students' learning performance, learning perception, and higher-order thinking. *Humanities and Social Sciences Communications*, 12(1). [s41599-025-04787-y]
- Liu et al. (2025). The Impact of ChatGPT on Students' Academic Achievement: A Meta-Analysis. *J. Computer Assisted Learning*. [10.1111/jcal.70096]
- Generative AI meta-analysis (39 studies). *Sciopen* 2025.
- Generative AI meta-analysis (26 studies). *Education and Information Technologies* 2025. [10.1007/s10639-025-13420-z]
- A Meta-Analysis of LLM Effects on Students. arXiv 2509.22725 (2025).
- Education Endowment Foundation (2025) AI tutoring meta-analysis (83 studies).
- Bloom, B. S. (1984). The 2 Sigma Problem. *Educational Researcher*.
- Kestin, G. et al. (2024). PS2 Pal AI tutor at Harvard. Working paper.
- Bastani, H. et al. (2024). Generative AI without guardrails can harm learning. *PNAS* (article 2422633122) / SSRN 4895486.
- To Layer or Not to Layer (2026). arXiv 2604.07469.

### Q2：领域研究
- Goh, E. et al. (2024). LLM Influence on Diagnostic Reasoning: RCT. *JAMA Network Open*.
- Goh, E. et al. (2024). LLM Influence on Management Reasoning: RCT. medRxiv 2024.08.05.
- Schmidgall et al. (2024). LLMs improve clinical decision making of medical students. *BMC Medical Education*.
- Peng, S. et al. (2023). The Impact of AI on Developer Productivity (GitHub Copilot RCT). MSR.
- Demirer, M. et al. (2025). MIT working paper on Copilot (4,867 devs).
- METR (2025). Measuring the Impact of Early-2025 AI on Experienced OS Developer Productivity.
- Anthropic (2026) internal RCT, cited in Groundy 2025 review.
- Choi, J. & Monahan, A. (2024). Lawyering in the Age of AI. *Minnesota Law Review* 109(1).
- AI Assistance in Legal Analysis (SSRN 4539836).
- Tennis serve AI motion analysis (preprints 2024-2025).
- CoachMe (ACL 2025).
- Personalized Motion Guidance Framework (arXiv 2510.10496).
- AI feedback occupational self-efficacy RCT (Japan, *Sci Rep* 2025, s41598-025-94985-0).
- AI vs Human Management 14-week pilot (SSRN 4739430).
- White-collar AI vs Human Coach quasi-experiment (CENTAUR/Reading 2025).
- AI Negotiation coach evaluation (arXiv 2509.22545).

### Q3：守门/反思组件
- Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis. *Advances in Experimental Social Psychology* 38.
- Sheeran, P., Listrom, R., & Gollwitzer, P. M. Updated meta-analysis (642 tests). KOPS Konstanz.
- Bisra et al. (2018). Inducing Self-Explanation: A Meta-Analysis. *Educational Psychology Review*.
- Zheng, J. et al. (2022). Metacognitive Prompts in CBL: Meta-Analysis. *J. Computer Assisted Learning*. [ERIC EJ1333210]
- Sciopen (2025). Metacognitive prompts on online SRL meta-analysis (32 studies).
- Pause before action (2025). *Sci Rep* (s41598-025-87119-z).
- Imas et al. Waiting to Choose. SSRN 2880386.
- Auer, M., & Griffiths, M. (2014). Time-limit pop-up RCT. *International Gambling Studies* 14(2).
- Online gambling RCT (PMID 33751702).
- Fischbacher, U., Hoffmann, G., & Schudy, S. (2017). The causal effect of stop-loss and take-gain orders on the disposition effect. *Management Science*.
- Cooling-off period 40-year natural experiment (Univ. Pittsburgh Law Review).
- Dynamic risky choice & commitment devices (AEA 2022 working paper).

### Q4：AI vs 人类反馈
- Steiss, J. et al. (2024). Comparing the quality of human and ChatGPT feedback. *Learning and Instruction*. [S0959475224000215]
- Springer IJETHE (2026) AI vs Teacher Feedback CoT prompt. [s41239-026-00579-9]
- Frontiers (2023) Automated Writing Evaluation meta-analysis.
- He, Y., et al. CBT Chatbot Meta-Analysis. PubMed 41813041.
- Heinz, M. et al. (2025). Therabot RCT. *NEJM AI*.
- LLM hallucination & medical errors:
  - npj Digital Medicine s41746-025-01670-7 (text summarization)
  - npj Digital Medicine s41746-026-02428-5 (patient questions)
  - Communications Medicine s43856-025-01021-3 (adversarial)
  - medRxiv 2026.03.23 (synthetic transcripts)

### Q5：元认知/Pattern Recognition
- Morewedge, C. K. et al. (2015). Debiasing Decisions. *Policy Insights from Behavioral & Brain Sciences*.
- Sellier, A.-L., Scopelliti, I., & Morewedge, C. K. (2019). Debiasing Training Improves Decision Making in the Field. *Psychological Science*.
- Frontiers (2024) Information & context debiasing disposition effect.
- Cognitive Mirror framework. Frontiers Education 2025 (1697554).
- Cognitive offloading and SRL. ERIC EJ1479919 (2025).
- Atlantis Press (2024) Kerala day traders AI bias paper.

### Q6：负面效应
- Trust and Reliance on AI (2024). *Computers in Human Behavior*. [S0747563224002206]
- Automation Bias in AI-assisted Medical Decision-making (Springer 2024). [978-3-658-47422-5_27 / arXiv 2411.00998]
- JMIR (2025) Dermatologists psychological factors. [e58660]
- Kosmyna, N. et al. (2025). Your Brain on ChatGPT: Cognitive Debt. arXiv 2506.08872 / MIT Media Lab.
- Gerlich, M. (2025). AI Tools and Critical Thinking. *Societies* 15(1).
- Lee, H. P. et al. (2025). The Impact of Generative AI on Critical Thinking (Microsoft × CMU). CHI 2025.
- AI Deskilling Paradox (2025). Communications of the ACM.
- Frontiers (2025) Outsourcing cognition. [1645237]
- Does AI assistance accelerate skill decay? (2024). *Cognitive Research: Principles and Implications*. [s41235-024-00572-8]

### Q7：交易/金融
- D'Acunto, F., Prabhala, N., & Rossi, A. G. (2019). The Promises and Pitfalls of Robo-Advising. *Review of Financial Studies* 32(5).
- Rossi, A. G., & Utkus, S. P. (2024). The diversification and welfare effects of robo-advising. *J. Financial Economics* 157.
- Reher, M., & Sokolinski, S. Who Benefits from Robo-Advising? (SSRN 3258088 / 3552671).
- Hodge, F. D. et al. (2023). When do robo-advisors make us better investors? *J. Behavioral Finance* (S2214804323000101).
- Algorithm aversion in trading (Univ. Pisa 2021 working paper).
- ZenTrader (Astor & Adam, 2011, Springer LNCS).
- EEG-Based Emotion Classification with Risk Control (Sensors 2023, sensors-23-03474).
- Heart rate / GSR & trading performance (Monash 2024; SSRN 5156137).
- Atlantis Press (2024) AI assistance & cognitive bias in Kerala traders.
- 商业产品（无独立学术评估）：TraderSync, Edgewonk, TradeZella, TradeUpCoach, HOC Trade, NeuroTrader.

### Q8：长期影响
- METR (2025). Early-2025 AI on Experienced OS Devs.
- Lee, H. P. et al. (2025). Microsoft × CMU Critical Thinking Survey.
- Anthropic (2026) RCT (cited via Groundy 2025).
- Kosmyna et al. (2025) MIT cognitive debt.
- Warwick (2025). Style, sentiment, quality of undergraduate writing in the AI era.
- Coach not crutch (2025). arXiv 2502.02880.
- Frontiers (2025) ITS frequency study (1738655).

### Q9：理论框架
- Vygotsky, L. S. (1978). *Mind in Society*.
- Stanford SCALE Initiative (2024). Socratic vs Non-Socratic AI RCT.
- Socratic Mind (2025) Georgia Tech buffering effect study.
- Scaffolding Generative AI as a Tutor (MDPI Education 2026, 16(4)/651).
- ChatGPT-generated help vs human tutor authoring (PLOS One 2024, pone.0304013).
- Tool, tutor, or crutch? (Springer 2025, s40594-025-00592-w).
- Yang, X., & Aurisicchio, M. (2021). Designing Conversational Agents using SDT. selfdeterminationtheory.org.
- AI chatbot and user satisfaction (Korea Contents Assoc. 2020).
- Agentic AI in Higher Education (Frontiers AI 2026, 1738774).
- Enhancing Critical Thinking via Socratic Chatbot (arXiv 2409.05511).

---

## 调研者备注

- 本笔记侧重负面/反例的搜索，因为正面文献容易被推广（厂商有动机），反面文献需要主动找。
- 没有访问 Web of Science / Scopus 的索引服务，依赖 web search + 摘要级阅读。一些关键论文（Fischbacher 2017、Goh 2024 JAMA Network Open）只读了摘要与二手综述描述。
- 多个引用是 2025-2026 的 preprint，未来可能被审稿修订甚至撤稿，使用时应再次核查。
- 三份调研合在一起的隐含结论：交易日志范式、散户失败根因、AI 教练范式——**没有一项有"已被验证用于零售交易者训练"的强证据**。整个训练系统都建立在合理的间接证据 + 工程假设之上。这不是失败，但需要被坦诚承认。
