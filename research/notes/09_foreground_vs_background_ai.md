# 前台 AI vs 后台 AI vs 无 AI 的认知卸载证据对比

> 调研日期：2026-05-05
> 调研方法：Web 检索（Nature Comm Psychology、JMIR、arXiv 2026、Frontiers、PNAS、Springer、IZA、FCA、academic.oup.com、Wikipedia 学术索引）+ 已有 Phase 1 证据重新切片
> 证据等级：S（同行评审、可复现/方法学透明）/ M（专业出版/可信数据/工作论文/会议论文）/ W（行业博客、营销材料、未独立验证）/ U（基于已知文献的逻辑推演）
> 上下文：Phase 2 入口形态调研的子任务 3。Phase 1 foundation v5 已 merge；本笔记是 Phase 2 Design 的一份输入，**不预设任何技术栈**。
> 与已有笔记的关系：notes/03 已建立"AI 教练在专业训练中是否有效"的整体证据基础；本笔记不重复，而是回答 03 没回答的具体问题——**当我们已经决定可能用某种形式的智能反馈时，"前台对话 vs 后台静默 vs 完全不用"哪一种最优？**

---

## 摘要

1. **"前台 vs 后台 vs 无"是三种相互独立的设计维度，证据强度极不对称**：
   - "前台 AI 损害技能保留与持续力"是 **S 级证据**（Bastani 2024、Liu 2026 N=1222、Kosmyna 2025、MS×CMU 2025、Salmoni-Schmidt-Walter Guidance Hypothesis）；
   - "后台 AI 静默分析的认知效果"目前**几乎是研究空白**（Linardon 2024 的 184 篇 mHealth 综述只有 10.3% 的研究把"参与 vs 效果"做了正式建模；通用"silent observer"研究多在欺骗/伦理而非技能训练）；
   - "无 AI"是一个长期被低估的有效对照——在多个领域（写作、运动技能、CBT）"无 AI"组的长期表现并不显著差于 AI 组，部分场景（高反刍人群、撤回测试）反而更好。

2. **关键的新证据（Phase 1 没引用过）**：
   - **Liu, Christian, Dumbalska, Bakker, Dubey (2026, arXiv 2604.04721)**：N=1,222 三组 RCT，AI 暴露 **仅 ~10 分钟** 后撤掉，AI 组 solve rate 0.57 vs 对照 0.73；放弃率 0.20 vs 0.11。**关键调节因素**：取直接答案的人受损最严重，**只取 hint 的人无显著差异**。这是 Bastani 2024 的快速重复 + 机制分离实验。【S 级】
   - **Salmoni, Schmidt & Walter (1984, *Psych Bulletin*) "Guidance Hypothesis"**：高频/连续反馈在保留/迁移测试上**比 50% 频率反馈更差**——运动学习领域 40 年的稳定证据。**这意味着"AI 持续反馈"在原理上接近"高频 KR"，可能本来就违背运动学习的最优反馈频率。** 【S 级】
   - **JITAI 元分析对比**：行为改变 g=0.77 (Wang 2023, k=21, N=592)，心理健康 g=0.15 (2025, k=23, N=2,563)。**JITAI ≠ 前台 AI**——它是"只在状态需要时打扰"，**结构上更像本笔记定义的"后台 AI 偶发干预"**。这是后台范式有效性的最强单点证据。【S 级】
   - **Liu et al. (2025) 静态 AI vs 对话 AI RCT (CRC 筛查 intent)**：静态 AI 单条信息 vs 对话 AI 三轮对话——**对话 AI 用户多花 3.5 分钟却没有更好效果**，作者建议"简洁、定向化的静态 AI 信息可能比复杂对话代理更有效"。这直接打击"前台对话比静态规则好"的默认假设。【S 级】
   - **Renkl & Atkinson 2003+ Faded Worked Examples**：**渐进式撤掉支架本身就是有效的学习设计**，不撤反而限制熟练学习者。这是"AI scaffolding fade"在前 LLM 时代的奠基证据。【S 级】

3. **Wise feedback 迁移到 AI 的状态：未直接验证 + 强警示信号**。Yeager 2014 wise feedback 的有效性建立在**师生关系信任 + 身份信号传递**上——"我给你高标准的反馈是因为我相信你的能力"。AI 缺乏长期关系积累、身份信号、共同历史。**没有任何 RCT 用 Yeager 的精确 wording 测试 AI 投递 wise feedback。** 现有 AI 反馈研究（Steiss 2024、Stanford SCALE 2024、IJETHE 2026）**指向同一悖论：质量上 AI 反馈 ≥ 人类反馈，但行为变化与采纳率反而更弱**。AI 缺少"被尊重"信号的传导通道。

4. **三选一的判定（详见 §一对比矩阵）**：在六个维度上证据都不指向同一个赢家——
   - **认知卸载**：无 AI = 后台 AI > 前台 AI（前台显著差，强证据）
   - **留存/习惯形成**：背景 AI ≈ 前台 AI > 无 AI（如果"无 AI"是裸自我管理；但 mHealth 整体流失基线很高，差距不一定大）
   - **错误检测**：后台 AI ≈ 前台 AI ≫ 无 AI（明确指向 AI，方向不区分前后台）
   - **用户主动思考**：无 AI ≥ 后台 AI > 前台 AI（前台对此维度损害最大）
   - **高反刍/临床安全**：后台 AI ≥ 无 AI > 前台 AI（前台 AI 加 Why 类提问对高反刍者风险最大）
   - **实施成本/维护**：无 AI ≫ 后台 AI > 前台 AI（成本数量级差异）

5. **核心整合判断（U 级）**：证据**不支持**任何单一形态作为系统级默认。最一致的方向是"**默认无 AI 或后台 AI；前台 AI 仅在用户已经独立完成认知工作之后启用，且能被随时关闭**"——即 σ 系统应将"前台 AI"视为一个**可选的、滞后的、用户主动调用的层**，而非主入口。这与 foundation v5 §三.2 的"反馈/规则验证组件不预设是 AI、不主动归因、对照镜而非裁判"的方向一致。

---

## 一、前台 vs 后台 vs 无 AI 的对比矩阵

> **定义（本笔记口径）：**
> - **前台 AI（foreground AI）**：以对话或对话化界面为主要交互方式，主动向用户呈现内容、占用用户视觉/注意力主通道。包括：ChatGPT 风格对话、AI 教练实时干预、push notifications、conversational tutoring。**特征**：用户必须读/回应。
> - **后台 AI（background AI）**：在用户不直接交互的情况下持续/异步分析其行为或数据，输出在用户主动查询时才被看见，或仅在异常时打扰（exception-based）。包括：trade surveillance、JITAI（仅触发时打扰）、anomaly alerts、digital phenotyping、weekly digest 报告。**特征**：用户在 99% 时间感觉不到 AI 存在。
> - **无 AI（no AI）**：纯静态规则、表单 validation、checklist、模板、分级文档、人类教练/同伴问责。**特征**：完全可预测、无 LLM 推理、无生成式输出。

| 维度 | 前台 AI | 后台 AI | 无 AI | 证据强度 / 关键来源 |
|---|---|---|---|---|
| **1. 认知卸载** | ❌ **强反向证据**：撤掉后 -17%（Bastani 2024）、persistence 损失（Liu 2026）、神经连接最弱（Kosmyna 2025）、CT 退化（MS×CMU 2025） | ⚠️ **几乎无直接研究**：理论上少卸载，但 trade surveillance 等系统**不针对用户认知工作**，对"用户技能"是中性 | ✅ **默认无卸载**，但代偿可能转移到搜索引擎、Excel、外部记忆；脑机制保持完整 | S（前台反向）/ U（后台中性）/ S（无 AI 默认） |
| **2. 留存 / 习惯形成** | ⚠️ **混合**：短期 engagement 高（Wang & Fan 2025 g=0.46 学习感知）；新颖效应 4-8 周衰减（Liu 2025）；frequency 与学习无显著相关（Frontiers 2025 ITS 一年研究）；push notification 增加曝光但无总用量提升 (PMC 169162) | ⚠️ **混合**：JITAI 行为改变 g=0.77（Wang 2023, k=21）但心理健康 g=0.15（2025, k=23）；passive sensing 可维持高质量数据（Nature 2024）；**无 head-to-head vs always-on** | ⚠️ **基线流失高**：mHealth 30 天 50% / 100 天 70% 流失（Pratap 2020）；交易日志 80% 两周内放弃（W）；**但 Linardon 2024：184 篇 RCT 仅 10.3% 把 engagement 与效果做关联** | M+S 混合 |
| **3. 错误检测** | ✅ **强**：实时拦截，自动化偏误研究表明 AI 警示纠正 26% 错误（Adjust for Trust 2025）；但 ⚠️ **automation bias 7% 翻判正确判断**（Pathology 2024） | ✅ **强**：trade surveillance 行业标准（NICE Actimize、TradingTechnologies），ED clinical alerts 35-48% 减时（BMC Med Inform Decis Making 2025）；**异步发现 ≥ 实时拦截**（取决于风险时间窗） | ❌ **弱**：依赖 self-detection；Dunning-Kruger 表明能力差者认不出自己错（飞行安全研究 W）；checklist 类静态工具仅在已知错误模式上有效 | S |
| **4. 用户主动思考 / Critical Thinking** | ❌ **强反向证据**：MS×CMU 2025 N=319（CT 转向"验证 AI"）；Liu 2026 persistence 损失 + 直接答案最严重（N=1222）；Microsoft Aether 2022 综述；**frictionless AI** (Nature Comm Psychology 2026) 论证 AI 默认设计与 desirable difficulty 直接冲突 | ❓ **几乎无研究**：理论上不打扰主思考过程，但也不引导反思；"被观察"效应可能轻微提升认知投入（virtual observer cheating 研究 Cambridge）但未在技能训练验证 | ✅ **默认完整**：desirable difficulty / generation effect / retrieval practice 强证据（Karpicke & Roediger 2008 *Science*）；motor learning Guidance Hypothesis（高频反馈反而损害保留） | S（前台反）/ U（后台不明）/ S（无 AI 正） |
| **5. 高反刍 / 临床安全** | ❌ **风险最高**：(a) 前台对话天然包含 Why 类提问 → Watkins & Teasdale 2004 触发反刍；(b) Sbarra 2013 高反刍者表达写作 9 个月后情绪更糟；(c) 拟人化 AI 强化情感卷入 → Hodge 2023 处置效应恶化；**但** Therabot RCT (Heinz 2025 *Nature Mental Health*) MDD d=0.85 显示**结构良好的 CBT 前台 AI 在临床上有效**——是矛盾点 | ✅ **较安全**：不主动唤起反刍；passive sensing 在自杀风险预测中**预测力低于 active**（Nature 2024 综述）但**伤害也更小**；不卷入情感叙事 | ⚠️ **已知子群风险**：Sbarra 2013（高反刍者写日志变差）；Cipriano 2020（写预测理由诱发过度自信）；**结构化 vs 表达性写作**（Frattaroli 2006、narrative expressive writing 2017）方向不同 | S（前台对高反刍风险）/ M（后台中性）/ S（无 AI 子群风险） |
| **6. 实施成本 / 维护负担** | ❌ **最高**：LLM API ~$0.01-0.10/query；TCO 估计 340-580% 低估（Stabilarity 2026 W/M）；Reliability 99.9% 困难；prompt drift；幻觉测试持续；ITS 多 agent 系统延迟问题（arXiv 2604.24110） | 🟡 **中**：可使用本地 ML 模型 + 静态告警规则；trade surveillance 商业化成熟；passive sensing 数据隐私是**主要 cost**（电池 + 用户同意） | ✅ **最低**：静态 checklist / 表单 validation / Markdown 模板；维护近零；可版本化；可追溯；用户可读 | S（产品工程文献，跨 W/M） |

> **诚实标记 — 本矩阵的边界**：
> - "无 AI"列里的"无"是相对的：用户可能仍依赖 Google、Excel、计算器、模板。本笔记不主张"原始大脑训练优于一切"——重点是排除**生成式 AI 或机器学习决策辅助**。
> - "后台 AI"是一个新兴概念，本笔记的多数论断方向是 U（基于已知文献的逻辑外推）；唯一较强的是 JITAI 元分析。
> - **没有任何研究做过严格的"前台 AI vs 后台 AI vs 无 AI"三臂 RCT**。本矩阵所有判定都是从相邻文献的 inference，不是直接证据。

---

## 二、各维度的关键证据

### 2.1 认知卸载（Cognitive Offloading）

#### 2.1.1 前台 AI ≫ 认知卸载（强 S 级证据）

【S 级，Phase 1 已引】
- **Bastani et al. (2024, *PNAS*)**：N≈1,000 高中生，撤掉 AI 后 GPT Base 组 -17%。详见 notes/03 §Q1.4。
- **Kosmyna et al. (2025, "Your Brain on ChatGPT", arXiv 2506.08872)**：4 个月、EEG。LLM 用户脑连接最弱、所有权感最低。
- **Lee et al. (Microsoft × CMU, 2025, CHI)**：N=319 知识工作者。CT 从"参与思考"转为"验证 AI 输出"。

【S 级，Phase 1 未引——本笔记新增】
- **Liu, Christian, Dumbalska, Bakker, Dubey (2026, arXiv 2604.04721)** "AI Assistance Reduces Persistence and Hurts Independent Performance"：
  - **N=1,222** 三组 RCT。这是 Bastani 2024 的快速重复 + 机制实验。
  - **Experiment 1 (N=354, fractions)**：AI 组 solve rate 0.57 vs 对照 0.73 (p<0.001)；skip rate 0.20 vs 0.11 (p=0.031)。
  - **Experiment 2 (N=667, replication with controls)**：AI 组 0.71 vs 对照 0.77 (p=0.020)。
  - **Experiment 3 (N=201, reading comprehension)**：效应推广到阅读理解。
  - **关键的机制分离**：61% 用户取直接答案；**取直接答案的人受损最严重，只取 hint 的人与对照组无显著差异**——这是认知卸载机制的直接证据。
  - **效应在仅 ~10 分钟暴露后即出现**——不是长期暴露的累积。
  - 作者结论："AI conditions people to expect immediate answers, denying them the experience of working through challenges independently. Persistence is foundational to skill acquisition."

【S 级】
- **Risko & Gilbert (2016, *Trends Cog Sci*) Cognitive Offloading 综述（衍生于 PMC 8358584 引用）**：外部记忆辅助提升即时表现但损害长期记忆形成；当用户**显式有"未来需独立完成"目标时**，可几乎完全抵消损害——**"目标设定"是关键调节因素**。

【M 级】
- **Gerlich (2025, *Societies* 15(1))**：N=666 横断面调查，AI 使用与 CT 显著负相关，cognitive offloading 完全中介。**横断面相关，不能因果。** 但与实验证据方向一致。

#### 2.1.2 后台 AI 对认知卸载的研究空白

【U 级，研究空白】
- 本调研未找到**任何专门测试"后台 AI（异步分析、不主动打扰）是否产生认知卸载"** 的研究。
- 推论：后台 AI 因不在决策瞬间介入，理论上不替代用户认知工作；但**用户知道有 AI 在监控自己**这一事实是否本身改变行为，目前研究多在 AI 安全/欺骗领域（Cambridge Experimental Economics 2024：cheating with virtual observer），不在技能训练。
- **诚实标记**：这是 σ 系统设计层最大的研究空白之一。如果 σ 选择"后台 AI 周期性 audit"，**目前没有直接证据它优于前台 AI 的认知卸载防御**——只有理论方向。

#### 2.1.3 无 AI 的"代偿卸载"问题

【M/U 级】
- **Sparrow et al. (2011, *Science*) Google effect**：人在能搜索时记得更少——卸载先于 AI。无 AI 不等于"全脑训练"。
- 对交易场景的含义（U）：交易者无 AI 时仍可能依赖 TradingView 信号、Excel 公式、社交媒体推荐——σ 系统的"无 AI"必须明确**也禁用其他外部认知拐杖**才能产生差异；否则可能只是把卸载从 LLM 转到搜索引擎。

#### 2.1.4 维度判定

| 形态 | 净证据 |
|---|---|
| 前台 AI | ❌ **强反向**（S 级，多份独立 RCT） |
| 后台 AI | ❓ **未验证**（无研究，理论中性） |
| 无 AI | ✅ **默认基线**（但需配套禁用外部认知拐杖） |

**指向**：本维度证据**强烈支持"非前台"**，但"无 AI 直接优于后台 AI"无证据。

---

### 2.2 留存 / 习惯形成

#### 2.2.1 前台 AI 的留存数据

【S 级】
- **ChatGPT 学习元分析新颖效应（Liu 2025, JCAL）**：4-8 周或 5-10 周时效果最大；更长干预未必有更大效果——**新颖性贡献了短期效应估计**。
- **Frontiers 2025 ITS 941 学生一年研究**：使用频率与学习收益**无显著相关**。
- **Linardon (2024, BMC Digital Health)**：184 篇 DMHI RCT 综述，**只 10.3% 真正分析"engagement → outcomes"路径**；分析后 effect size 从 -0.14 移到 -0.18（per-protocol vs ITT），样本量平均减少 33%——**engagement 不是 outcomes 的 proxy**。

【S 级】
- **Hueller, Reimann & Warren (2023, *J Assoc Consumer Research*)**：6 实验 N=3,766。**streak 长期降低留存**——把"可选"扭曲为"避免损失"焦虑性义务。前台 AI（push notifications + streak）正好踩在这条反向证据上。

【M 级，新增】
- **JMIR mHealth (2018) "To Prompt or Not to Prompt" microrandomized trial**：tailored push 增加 24h 内 app engagement 概率约 3.9%；周末效应略大但不显著；**自适应 timing 没有持续优于非自适应**。
- **PMC 169162 (PLOS One)** push notification frequency: intelligent 与 daily 在 view 量上 d=0.47-0.50 高于 occasional，**但总 app usage 无显著差异**——曝光增加，使用未必增加。

#### 2.2.2 后台 AI 的留存数据

【S 级，新增——本笔记主新发现】
- **JITAI 元分析 (Wang et al. 2023, k=21, N=592)**：行为改变 g=0.77 (95% CI 0.32-1.22, p<0.001)。**JITAI 是"只在状态需要时介入"的范式**，结构上接近后台 AI。
- **JITAI 心理健康元分析 (2025, k=23, N=2,563)**：g=0.15 (95% CI 0.05-0.26, p=0.003)——小但显著。
- **诚实标记**：JITAI ≠ 纯后台。它是"后台监控 + 偶发前台介入"。在异步 audit + 周期性报告意义上，JITAI 是已有元分析支持的最接近候选。
- **JITAI 现状**：71% 现有研究是 feasibility/usability，仅少数 efficacy；高质量 RCT 仍少（Soton 2024）。
- **mHealth depression apps systematic review (2021, JMIR)**：71% 仅自我报告，18% 结合被动测量"作为进度指标而非 adaptive trigger"——**真正的 JITAI 在产业里几乎不存在**。

【M 级】
- **EMA 元分析 (Wen et al. 2017, SAGE)**：average compliance 79%（scheduled 86%、random 58%）；9 周下降 1-2%/周；提供**金钱激励显著提升 compliance**。
- **后台 + 异步报告**：Linardon 综述显示纯被动 + 周期 digest 类设计的 efficacy 数据极少。

#### 2.2.3 无 AI 的留存数据

【M/W 级】
- mHealth 流失基线 30 天 50% / 100 天 70%（Pratap 2020；Meherali 2020 *JMIR* 17 项研究 pooled dropout 43%）。
- 交易日志行业内部 80% 在 2 周内放弃（W 级，TradingView/TraderSync 行业说法，无独立验证）。
- **诚实标记**：上述不是"无 AI"特定数据——它是 mHealth/学习类 App 的整体基线。"无 AI"组没有 baseline 高于这个数字的有力证据。

#### 2.2.4 关键反直觉证据

【S 级】
- **静态 vs 对话 AI RCT (Liu et al. 2025, arXiv 2507.08211)**：CRC 筛查 intent。静态 AI 单条信息 vs 对话 AI 三轮对话——**对话用户多花 3.5 分钟却没更好效果**；作者建议"简洁、定向化的静态信息可能比复杂对话代理更可扩展和临床可行"。
  - **这直接打击"前台对话 = 更好留存/效果"的默认假设**。

【S 级】
- **AI 静态消息 vs 个性化纸质材料**（Capraro 2024 类型，详见 notes/06）：21,506 人 megastudy 显示 honesty oath 类静态干预效应稳健。**前台 AI 没有击败结构化静态设计**。

#### 2.2.5 维度判定

| 形态 | 净证据 |
|---|---|
| 前台 AI | ⚠️ **混合**：高 engagement 但与 outcome 关联弱；新颖效应 4-8 周衰减；streak/notification 反例强 |
| 后台 AI | ⚠️ **混合，证据少**：JITAI 行为改变 g=0.77（最强单点），但目前几乎无产品按 JITAI 真实部署 |
| 无 AI | ⚠️ **基线流失高**，但与 AI 形态差距未必显著 |

**指向**：**没有形态在留存维度上明确胜出**。最强的单一证据是 JITAI 的 g=0.77，但 JITAI 是混合范式而非纯后台；纯前台对话的"用得多≠效果好"反直觉证据稳健。

---

### 2.3 错误检测

#### 2.3.1 前台 AI 错误检测

【S 级】
- **AI assist 减低决策错误**："Adjust for Trust"（arXiv 2502.13321, 2025）：**inserting forced pauses 减少 inappropriate reliance 38%、改善决策准确率 20%**。
- **Bucinca et al. (2021)** "To Trust or to Think"：cognitive forcing functions 显著降低 over-reliance；**但这些设计在主观满意度上排名最低**。
- **Microsoft Aether (2022) overreliance review**：人很少分析性地评估个体 AI 推荐，多数发展"是否跟随 AI"的整体启发式。
- **"culturally biased AI" (arXiv 2508.09297, 2025)**：有偏 AI 反而**激发批判性审视**，"过度中性 AI 让用户失去判断动力"。

【S 级】
- **Pathology automation bias (arXiv 2411.00998, 2024)**：病理专家 7% 时刻把原本正确判断"翻"成 AI 错误建议，时间压力下加重——前台 AI 错误检测的反向风险。
- **Adjust for Trust 数据**：医生在高信任时把 26% AI 误诊接受为正确；低信任时仅 8%。

#### 2.3.2 后台 AI 错误检测（**最强候选**）

【M-S 级，行业证据】
- **Trade surveillance 行业**：NICE Actimize、TradingTechnologies、Hadrius、Knowtice、Quod Financial 等都基于**ex-post / 异步异常检测**（spoofing、wash trade、ramping、disposition effects）；行业标准。
  - **诚实标记**：这些是**合规检测**，针对违法/违规交易；并非"训练个人交易员变好"。但范式（监控 + 异常告警 + 异步审查）直接迁移。
- **临床 ML alerts**：Mayo Clinic ML deteriorating-patient alert 减少响应时间 35.4%、干预时间 48.5%（medRxiv 2021）。**"异常即告警，正常时静默"** = 后台 AI 的核心价值主张。
- **AI clinical decision support pragmatic trial (medRxiv 2022)**：异步触发干预统计上减少 escalation。

【M 级，trading 商业产品 W 警示】
- **TradeUpCoach** 自称 10-30 秒前预测认知漂移（W 级，未独立验证）。
- **Edgyx Ora**：post-trade emotion tagging + 12+ bias 识别（W 级）。
- **Vigil**：post-hoc trade audit against rule sets（W 级）。
- **诚实标记**：这些产品的**结构是后台 AI**，但效果数据全为营销层。值得借鉴**结构**，不能引用其**效果**。

#### 2.3.3 无 AI 错误检测

【S 级，反向】
- **Dunning-Kruger 效应**：能力差的人最难识别自己错——self-detection 在高复杂度场景效果有限。
- 飞行安全研究（Wright State 2015 W/M）：飞行员对事故 underreporting 严重，"dark figures" 巨大；高 self-monitoring 的人也漏掉 systematic errors。

【M/S 级】
- **静态 checklist 在已知错误模式上有效**：医学手术 checklist 显著降低并发症（Haynes 2009 *NEJM* checklist trial）。但前提是**错误模式已知**——交易场景的"未知未知"无法被静态规则覆盖。

#### 2.3.4 维度判定

| 形态 | 净证据 |
|---|---|
| 前台 AI | ✅ **强**，但有 over-reliance / 7% 翻判反向风险；need cognitive forcing |
| 后台 AI | ✅ **强**（行业标准），且没有 over-reliance 风险（用户不在决策瞬间被 AI 推） |
| 无 AI | ❌ **弱**：限于已知错误模式 + 静态 checklist |

**指向**：**这是 AI（前台或后台）相对于"无 AI"明确占优的维度**。三选一时**前台 vs 后台不区分胜负**——但后台无 over-reliance 风险，**安全性更高**。

---

### 2.4 用户主动思考

#### 2.4.1 前台 AI 损害主动思考的证据

【S 级，Phase 1 已引】
- MS×CMU 2025（CT 转向"验证 AI 输出"）。
- Bastani 2024（依赖外援后撤掉时表现下降）。
- Kosmyna 2025（神经连接最弱、所有权最低）。
- METR 2025（资深开发者用 AI 慢 19% 但自评快 20%）。

【S 级，Phase 1 未引——本笔记新增的三份关键证据】
- **Liu et al. (2026, arXiv 2604.04721)**：N=1,222，10 分钟即出现 persistence 损失；机制是**条件反射式期待即刻答案**。这是"AI 损害用户主动思考"的最大样本 + 最严格 RCT 之一。
- **Salmoni, Schmidt & Walter (1984, *Psych Bulletin*) Guidance Hypothesis**：高频/连续反馈在保留/迁移测试上**比 50% 频率反馈更差**。**含义**：前台 AI 默认是"高频反馈"形态，违背运动学习 40 年的证据。Frontiers Neuroscience 2016（多通道反馈协调）有反例，但保留+迁移上 Guidance Hypothesis 仍是基准。
- **"Against frictionless AI" (2026, *Nature Communications Psychology*)**：论证当前 AI 设计与 desirable difficulty 范式直接冲突；frictionless = 即时完整答案 = 短视协作者；**moderate friction 实际上促进学习、生成意义、支持动机**。

【S 级】
- **Karpicke & Roediger (2008, *Science*) retrieval practice / desirable difficulty**：检索练习显著优于反复阅读；学生**主观偏好阅读**（即低难度感），但学得**更少**。
  - **隐含**：用户主观更喜欢 AI 即时回答（低 friction），但学得更少——这是 reflection-satisfaction tradeoff 在 AI 时代的预演。

#### 2.4.2 中间证据：Socratic / Cognitive Mirror 的尝试

【S 级】
- **Stanford SCALE Initiative (2024)** Socratic vs non-Socratic AI N=122：Socratic engagement 显著上升，**学习不显著**；部分学生觉得不够有用。
- **Cognitive Mirror Framework (Frontiers Education 2025)**：把 AI 重新定位为"被教的学习者"；**理论框架，无 RCT**。
- **OnlineMate (arXiv 2509.14803, 2025)**：使用 ToM 推断学习者心理状态；**框架展示，未对照**。

#### 2.4.3 中间证据："coach not crutch"反例

【S 级】
- **arXiv 2502.02880 (2025) "Coach not crutch"**：AI 写作教练实验。**AI access 组改进比无 AI 组多，且付出更少 effort**。机制是"viewing AI 高质量 examples = 主动 practicing"——AI 提供 high-quality 个性化样本而非 interactive coaching 是关键。
- **诚实标记**：这是当前少数证据**反向**指向"前台 AI 能改善而非损害"的，但作用机制是**examples**（被动观察）而非**对话**（主动卸载）。它不一定推翻其他反向证据。

#### 2.4.4 后台 AI 主动思考维度

【U 级，几乎空白】
- 后台 AI 不主动呈现内容，**不诱发**用户思考；但也不损害。
- 中性。
- **可能的间接证据**（U 级）：观察者效应。Cambridge Experimental Economics 2024（virtual observer cheating）显示 active observer avatar 显著降低 cheating——**"被监视"会激活某些反思**。但这是道德监督，不是技能训练，不能直接迁移。

#### 2.4.5 无 AI 维度

【S 级，正向】
- 默认完整：retrieval practice、generation effect、self-explanation、metacognitive prompts 的所有正向证据都建立在"用户独立完成认知工作"前提上。

#### 2.4.6 维度判定

| 形态 | 净证据 |
|---|---|
| 前台 AI | ❌ **强反向**（5+ S 级独立 RCT） |
| 后台 AI | ❓ **未验证，理论中性** |
| 无 AI | ✅ **基线最优**（与 desirable difficulty / retrieval practice / generation effect 一致） |

**指向**：本维度证据最强反对**前台 AI**作为主入口。

---

### 2.5 高反刍 / 临床安全

#### 2.5.1 前台 AI 的特定风险

【S 级，Phase 1 已引】
- **Sbarra, Boals, Mason et al. (2013, *Clinical Psych Sci*)**：高反刍者写表达性日志 9 个月后情绪恢复**更差**（M=-0.18 vs +0.16）。
- **Watkins & Teasdale (2004, *J Abnormal Psych*)**："Why" 类提问触发反刍。

【U 级，本笔记推论】
- **前台 AI 对话天然包含 Why 类提问**：所有 LLM 教练默认 prompt（"为什么觉得这个 setup 好？"、"为什么没遵守止损？"）正好踩在 Watkins & Teasdale 的反向证据上。
- **拟人化的强化效应**：Hodge 2023 显示拟人化 robo-advisor 恶化处置效应。前台 AI 默认拟人化更高（对话语气、"我认为"、"我建议"）→ 卷入感更强 → 高反刍者风险叠加。

#### 2.5.2 前台 AI 的反例（CBT 聊天机器人）

【S 级】
- **Heinz et al. (2025, *Nature Mental Health*) Therabot RCT**：MDD d=0.85-0.90，GAD d=0.79-0.84，8 周维持。**这是迄今 LLM 心理教练最强单点证据**——**结构化 CBT 协议下的前台 AI 是治疗性的**。
- **诚实标记**：Therabot **不是 generic 对话**；它是按 CBT 协议结构化的、目标在症状缓解的。把它泛化为"前台 AI 对高反刍者安全"是过度外推。
- **CBT chatbot meta-analysis (2025, k=29)**：抑郁短期 g=-0.55、焦虑 g=-0.26；follow-up 时抑郁 g=-0.32、焦虑不显著。**整体证据 certainty "very low to low"**（作者自评）。

#### 2.5.3 后台 AI 临床安全

【U/M 级】
- **Passive sensing 自杀风险预测**（npj Mental Health Research 2024）：**预测力低于 active 数据**——3/4 研究发现无增量价值。但**伤害也低**：不主动唤起反刍，不诱发情感卷入。
- **诚实标记**：后台 AI 的临床安全数据**几乎不存在**——这是研究空白，不是已验证的"安全"。但理论上它**不诱发反刍** / 不情感卷入是其设计优势。

#### 2.5.4 无 AI

【S 级】
- Cipriano 2020 投资日志诱发过度自信（详见 notes/01）。
- Sbarra 2013 高反刍者表达写作变差。
- **无 AI 不等于安全**——书写本身可能产生伤害。但伤害模式**已知**（Sbarra），可以通过设计避免（用 narrative 而非 expressive、用 What 而非 Why、用结构化模板而非自由书写）。

#### 2.5.5 维度判定

| 形态 | 净证据 |
|---|---|
| 前台 AI | ❌ **风险最高**（默认 Why 提问 + 拟人化 + 卷入），但结构化 CBT 协议是反例 |
| 后台 AI | ❓ **理论较安全**，无证据 |
| 无 AI | ⚠️ **已知子群风险**（高反刍者），但有可控设计模板 |

**指向**：本维度**强烈警示对高反刍者使用前台 AI**。Phase 2 的 onboarding 临床筛查（PGSI/PHQ-4，foundation §三.11）应作为前台 AI 的硬门禁。

---

### 2.6 实施成本 / 维护负担

#### 2.6.1 前台 AI 成本

【M 级，工程文献】
- **LLM API 成本数量级**（EngineersOfAI、Stabilarity Hub）：100k DAU 客服系统每日 ~$45,000/天 = $1.35M/月，可能超过产品收入 6.75x。
- **TCO 低估 340-580%**（Stabilarity 2026）：超出 API 价格的隐性成本——prompt 工程、context window 管理、错误处理、合规。100k 日请求月成本 $4,200-$127,000。
- **Reliability 99.9% 困难**（多 agent 系统延迟问题，arXiv 2604.24110, multi-agent ITS）。
- **Prompt drift / 幻觉**：医疗 AI 综述（npj Digital Medicine 2026）factual error rate 26-36%——交易场景错误率没有公开数据，但可推论不会低于医疗。

#### 2.6.2 后台 AI 成本

【M 级】
- 可使用本地 ML 模型 + 静态告警规则；trade surveillance 商业化成熟（NICE Actimize、TradingTechnologies）。
- Passive sensing 主要 cost 是数据隐私 + 用户同意 + 设备电池。
- **比前台低数量级**：因为不需要实时 LLM inference + conversation context 管理。

#### 2.6.3 无 AI 成本

【M 级】
- 静态 checklist / 表单 validation / Markdown 模板：维护近零；可版本化；可追溯；用户可读。
- 主要 cost：**初次设计**（必须仔细，不能事后调）和**用户接受度**（需要 UX 设计补偿生硬感）。

#### 2.6.4 维度判定

| 形态 | 净证据（每个用户每月成本数量级） |
|---|---|
| 前台 AI | $1-100/用户/月（LLM token） |
| 后台 AI | $0.1-10/用户/月（本地 ML + 异步）|
| 无 AI | $0/用户/月（增量） |

**指向**：本维度对**个人级 σ 系统**（自用工具）影响相对较小（用户数=1，成本可控）；对潜在产品化会成为决定性约束。

---

## 三、Phase 1 已引用证据的重新切片（按"前台 / 后台 / 无"重新归类）

> 这一节不重复 Phase 1 引用的研究本身，而是把它们**重新放到本笔记的三选一坐标系**里。

### 3.1 Bastani 2024 PNAS — 严格地是"前台 AI vs 无 AI"

- **GPT Base 组**：完全前台对话，无护栏。
- **GPT Tutor 组**：前台对话 + 教学 prompt 约束（仍前台）。
- **对照组**：无 AI（结构化 worksheet + 教师答疑）。
- **结论的精确语义**：撤掉前台 AI 后，曾用 GPT Base（无护栏前台）的人比从未用过的人 -17%。**论文本身没有研究"后台 AI"**。
- **σ 系统的重新提问**：Bastani 不能直接告诉你"后台 AI"是否更安全——只能告诉你**前台 AI 不带护栏对学习有害**。

### 3.2 METR 2025 — 严格地是"前台 AI 工具栈 vs 无 AI"

- 资深开源开发者使用 Cursor IDE / chat 等**前台对话工具**，慢 19%。
- **不是后台 audit**——开发者在**实际工作中**与 AI 对话。
- **σ 系统的重新提问**：METR 反向证据**不能外推到"trading post-hoc audit AI"或"周末复盘报告生成"**——这些是后台范式，METR 没测试。

### 3.3 MIT Kosmyna 2025 — 严格地是"前台 LLM 写作 vs Brain only"

- 第三组（Brain → LLM 切换）表现良好，第二组（LLM → Brain 切换）表现下降——**与"前台 AI 撤回后留下技能空缺"机制一致**。
- **没有"后台 AI 监控写作过程"组**。

### 3.4 Microsoft × CMU 2025 — 严格地是"前台 GenAI vs 不用"

- N=319 知识工作者，**与 AI 对话时 CT 转向"验证"**。
- **没有"后台 AI 审计已完成工作"组**。

### 3.5 Hodge 2023 — 是"前台拟人化 vs 后台无拟人化"

- robo-advisor 本身是后台资产管理工具；加入"拟人化前台对话"反而恶化处置效应。
- **这是一份"前台化伤害后台优势"的直接证据**——Phase 1 引用频次不高，但对本笔记**特别相关**。
- **σ 系统的重新提问**：把后台 AI 加上前台对话伪装是**最差的设计**。要么留在后台（异步报告），要么明确前台（接受其代价）；不要**用前台对话伪装后台分析**。

### 3.6 FCA 2024 + Robinhood — 严格地是"前台推送（无智能）vs 不推送"

- **FCA RCT N=9,000**：push notifications 增加交易 11%、风险投资 8%；points/prize 增加交易 12%、风险 6%；**低金融素养者交易频率提升尤其大**。
- **Robinhood 独立研究**：±5% 自动推送在 15 分钟内增加交易 ≥25%。
- **关键洞察**：**推送本身就是前台 AI 的最弱形式**（不需要 LLM，只需要规则触发的内容呈现），它在**真实金融场景已被证明系统性增加散户损失**。
- **σ 系统的重新提问**：任何带"主动 push 通知"特征的设计都已被一份 RCT + 一份大型自然实验定性为有害——前台 AI 的最低成本版本已经是有害的。

### 3.7 Yeager 2014 wise feedback — 严格地是"人类 + 前台书面"

- 这是**师生书面反馈**（教师在学生作文上手写评语）；**没有 AI**。
- 机制：长期师生关系 + 身份信号传递（"我给你高标准的反馈是因为我相信你的能力"）。
- **迁移到 AI 的难题**：
  - AI 没有长期关系积累。
  - AI 没有身份信号——它对所有用户都说"高标准"，所以"高标准"信号本身退化。
  - AI 缺乏"被尊重"的传导通道——用户知道 AI 不真正认识自己。
- **当前的 AI wise feedback 研究状态**：
  - 我**没有**在本调研中找到任何 RCT 用 Yeager 2014 的精确 wording 测试 AI 投递 wise feedback。
  - 已有 AI 反馈研究（Steiss 2024、Stanford SCALE 2024、IJETHE 2026）**指向同一悖论**：AI 反馈质量上 ≥ 人类反馈，但**行为变化与采纳率反而更弱**。
  - **诚实标记**：Yeager wise feedback 在 AI 形态上的迁移性是 σ 系统设计的关键未知。Phase 2 应作为**待验证假设**而非已知约束。

### 3.8 Beighton 2018 / Lelkes 2012 — 是"无 AI 反例"

- Beighton：制度化反思退化为"表演性合规"——无 AI 时也会发生。
- Lelkes：完全匿名（无观察者）让人**更敷衍**。
- **σ 系统的含义**：无 AI 不等于"诚实激励完整"——必须叠加"被他人/工具观察"的结构。后台 AI 提供"被监视"信号但不诱发反刍——**理论上是诚实激励的最优形态**，但无直接证据。

### 3.9 Cipriano 2020 / Sbarra 2013 — 是"无 AI 反例（用户自己写）"

- Cipriano：写预测理由诱发过度自信。
- Sbarra：高反刍者表达性写作变差。
- **σ 系统的重新提问**：无 AI 不等于"无伤害"。**结构化 + What 提问 + 客观证据**的设计能把无 AI 风险降到最低，但需要明确设计——不是"什么都不做"。

---

## 四、对 σ 系统的具体含义（U 级）

> 本节是 U 级——**基于已知文献的逻辑推演**。Phase 2 Design 的最终选择应在此基础上做工程权衡。

### 4.1 三选一的整合判断

| 维度 | 最优形态（按证据） | 次优 | 最差 |
|---|---|---|---|
| 认知卸载 | 无 AI = 后台 AI | — | 前台 AI |
| 留存 / 习惯形成 | 后台（JITAI） / 混合 | 前台 / 无 AI（差距未必显著） | 难判 |
| 错误检测 | 后台 AI = 前台 AI | — | 无 AI |
| 用户主动思考 | 无 AI = 后台 AI | — | 前台 AI |
| 高反刍 / 临床安全 | 后台 AI（推论） | 无 AI（已知子群风险）| 前台 AI |
| 实施成本 | 无 AI | 后台 AI | 前台 AI |

**净结论（U 级）**：
- **前台 AI 在 4/6 维度上是最差**（认知卸载、用户主动思考、高反刍、成本）；在错误检测维度上与后台 AI 持平；在留存维度上证据混合。
- **后台 AI 在 4/6 维度上至少是次优或最优**（认知卸载、错误检测、用户主动思考、高反刍）；只在成本上劣于无 AI。
- **无 AI 在 4/6 维度上至少是次优或最优**；只在错误检测和留存（如果不叠加问责机制）上明显劣势。

### 4.2 "三选一"在 σ 系统的现实分解

σ 系统不是单一接口；它有不同时刻：

| σ 时刻 | 推荐默认形态 | 理由 |
|---|---|---|
| **下单瞬间（决策链 5 问执行）** | **无 AI**（静态表单 + binding pre-commitment） | 用户主动思考维度 + 认知卸载维度都强反对前台 AI；成本最低；与 foundation §三.3 binding pre-commitment 一致 |
| **平仓后 30 分钟内的极简复盘** | **无 AI**（结构化模板）+ honesty oath | 同上；平仓时情绪高唤醒，前台 AI 反而易触发反刍 |
| **每周末 / 每月末的结构化复盘** | **后台 AI 异步报告**（如果有 AI）+ 用户主动 review | 异步 → 不诱发卸载；用户已自己回顾过；AI 是对照镜 |
| **任何时候用户主动求助** | **前台 AI（受限）**——但仅在用户先独立写下答案后才能调用 | foundation §三.2 anchoring 防御原则的实现 |
| **风控异常 / 红线触发** | **后台 AI 异常告警** + binding 锁定 | exception-based intervention 是后台 AI 的强项 |
| **生理/环境门禁** | **无 AI 静态规则**（睡眠 < X 小时禁开仓） | 不需要 AI 推理 |

**核心设计指针（U 级）**：
1. **默认形态 = 无 AI 或后台 AI**。前台 AI 是可选的、滞后的、用户主动调用的层。
2. **任何前台 AI 必须满足"先独立完成认知工作再 review"的 anchoring 防御**——这与 foundation v5 §三.2 一致。
3. **Liu 2026 的 "hint vs 直接答案" 机制**给出一个具体设计原则：**前台 AI 给 hint 不给答案**——hint 路径下没有 persistence 损失。
4. **拒绝伪装**：不要把后台 AI 包装成前台对话。Hodge 2023 的反例直接打击这一设计。
5. **Wise feedback 的 AI 投递**作为 Phase 2 待验证假设，**不**作为已确立约束。

### 4.3 与 Phase 1 foundation 的兼容性核查

| foundation §三 条目 | 本笔记的支持 / 修正 |
|---|---|
| §三.2 反馈/规则验证组件**不预设是 AI**、不主动归因、对照镜 | ✅ 强支持。本笔记进一步建议"默认即非 AI 或后台 AI" |
| §三.2 anchoring 防御（重要决策前必须用户先独立写下答案） | ✅ 强支持。Liu 2026 + MS×CMU 2025 直接证据 |
| §三.2 反馈时机分层（执行期 vs 反思期） | ✅ 强支持。motor learning Guidance Hypothesis（少 = 多）+ Linardon paradox |
| §三.2 重大回撤例外（人话支持） | ⚠️ **需 Phase 2 注意**：本笔记证据不足以判断重大回撤时前台 AI 是否安全。Therabot 反例提示**结构化 CBT 协议下前台 AI 可能可行**，但不在 σ 主入口 |
| §三.3 binding pre-commitment > 软提示 | ✅ 一致（FCA + Robinhood + Fischbacher） |
| §三.6 退出协议数据触发 | ✅ 后台 AI 异常告警是其天然实现路径 |
| §三.13 Phase 2 入口形态调研要求 | ✅ 本笔记完成的就是这个调研的子任务 3 |

### 4.4 没回答的问题（Phase 2 必须解决）

1. **后台 AI 异步报告的"用户读取率"是否高于前台对话**？无任何研究。
2. **"AI hint 路径" vs "AI 答案路径"在 trading 决策链中的工程实现**：5 问回答完后能否给 hint？hint 是否可能本身就是答案？
3. **后台 AI 触发的告警是否引发恐慌交易**？JITAI 元分析行为变化 g=0.77 来自健康场景；trading 场景未验证。
4. **AI 投递 wise feedback 的可行性**：找一份 RCT 还是先做 N-of-1 实验？
5. **"无 AI 静态规则"与 σ 系统现有 markdown 工作流的具体整合**——这是工程问题不是研究问题，但需在 Phase 2 Design 解决。

---

## 五、本笔记的局限

> 诚实标记的最后一项：**这份调研也有边界。**

### 5.1 研究空白（不是我没找，而是文献空白）

1. **没有"前台 AI vs 后台 AI vs 无 AI"三臂 RCT**——本笔记所有判定都是从相邻文献的 inference。
2. **后台 AI 在认知卸载、用户主动思考维度几乎无直接研究**——本笔记 §2.1.2 / §2.4.4 都是理论中性，不是已验证安全。
3. **AI 投递 wise feedback 的 Yeager-精确 RCT 不存在**。
4. **"在 trading 场景"的所有判定**都是从教育/医学/写作场景外推。**没有 trading 领域的"前台 vs 后台" RCT**——这是 Phase 1 调研 7 已揭示的空白，本笔记同样受其约束。
5. **个人级使用 vs 产品级部署**：本笔记的成本维度对个人 σ 系统影响小；对产品化决定性。Phase 2 必须明确目标用户基数。

### 5.2 调研方法学局限

1. **付费墙后的论文未读全文**：部分 SAGE/Wiley 期刊仅能引用摘要。
2. **arXiv preprint 占新证据的较大比例**：Liu 2026 (2604.04721)、"Against frictionless AI" 是 preprint/Nature Comm Psychology；preprint 等级低于同行评审。
3. **2026-05 之后的研究未覆盖**——本笔记结论可能在 6 个月内被修正。
4. **中文学术数据库未直接覆盖**：CNKI/万方未调研，中文 trading 场景研究可能漏失。

### 5.3 Phase 1 已知盲区的延续

- **Phase 1 调研 7（trading 场景 AI 教练）几乎完全空缺**：这意味着本笔记的所有"对 σ 系统含义"都是 U 级外推。
- **"AI 撤掉一周看看会怎样"的个人级 N-of-1 实验设计**（foundation §一调研 3）在本笔记没有具体方案——这是 Phase 2 Design 的工作。

### 5.4 本笔记定义层面的局限

- "前台 AI / 后台 AI / 无 AI"是**本笔记的口径**，文献中没有统一定义。例如：
  - JITAI 既可以是前台（推送通知）也可以是后台（被动监控）——本笔记把它视为"后台监控 + 偶发前台介入"的混合范式。
  - AI 实时高亮（IDE inline suggestion）是前台还是后台？本笔记倾向归为前台（占用注意力主通道），但边界模糊。
  - 周末 AI 报告是后台（用户主动 read）还是前台（呈现是 AI 主动）？本笔记倾向后台。
- **不同的定义口径会改变本矩阵的判定**。Phase 2 Design 需先固定口径再选方案。

### 5.5 关于"后台 AI 是否真的更安全"的最大保留

- 后台 AI **没有被反向证伪**，不等于**已被正向证实**。
- 一些可能的后台 AI 反向风险（U 级，未直接验证）：
  - **被监控感**长期是否产生焦虑（Hawthorne effect 反向）。
  - **异步报告**可能让用户**集中接收负反馈**（一周一次的 audit 比每天一次的轻量反馈，**情感冲击更集中**——这是潜在临床风险）。
  - **后台 AI 的"权威感"**可能在用户读到周报时反而**强化** automation bias（不在决策瞬间，但在反思瞬间被劫持）。
- **诚实标记**：这些风险都是 U 级推演。Phase 2 应作为待观察盲区。

---

## 引用清单

### 新增证据（Phase 1 未引）

- Liu, Christian, Dumbalska, Bakker, Dubey (2026). AI Assistance Reduces Persistence and Hurts Independent Performance. arXiv 2604.04721. **N=1,222 三组 RCT。**
- Salmoni, A. W., Schmidt, R. A., & Walter, C. B. (1984). Knowledge of Results and Motor Learning: A Review and Critical Reappraisal. *Psychological Bulletin*, 95, 355-386. **Guidance Hypothesis 奠基。**
- Schmidt, R. A. (1991). Frequent augmented feedback can degrade learning: Evidence and interpretations. *Tutorials in motor neuroscience*. **高频反馈反而损害保留。**
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist*. **Faded worked examples。**
- Wang et al. (2023). Using a complexity science approach to evaluate the effectiveness of just-in-time adaptive interventions: A meta-analysis. **k=21, N=592, behavior g=0.77。**
- 2025 JITAI mental health meta-analysis (PMC 12481328). **k=23, N=2,563, g=0.15。**
- Liu et al. (2025). Effect of Static vs. Conversational AI-Generated Messages on Colorectal Cancer Screening Intent. arXiv 2507.08211. **静态 ≥ 对话 AI。**
- IZA DP 18338 (2025). AI Tutoring Enhances Student Learning Without Crowding Out Reading Effort. **N=334，unrestricted ≥ restricted（restricted = "intensive bursts of prompting"）。**
- Bucinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI. CSCW '21. **forced confirmation 显著降低 over-reliance。**
- Adjust for Trust (2025). arXiv 2502.13321. **forced pauses -38% inappropriate reliance, +20% accuracy。**
- Frontiers Education (2025). The Cognitive Mirror: A Framework for AI-Powered Metacognition. **理论框架，无 RCT。**
- "Against Frictionless AI" (2026). *Nature Communications Psychology*. **frictionless 设计与 desirable difficulty 直接冲突。**
- Heinz, M., et al. (2025). Therabot RCT for the treatment of mental disorders. *Nature Mental Health*. **MDD d=0.85-0.90，结构化 CBT 前台 AI。**
- arXiv 2502.02880 (2025). "Coach not crutch": Evidence that AI can improve writing skill despite reducing effort. **反例，AI 提供 examples 而非对话。**
- Linardon, J. (2024). Engagement-effectiveness paradox in DMHIs (BMC Med Res Methodol; PLOS Digital Health 2024)。**184 项 RCT 综述。**
- Pratap, A. et al. (2020). The accuracy of passive phone sensors in predicting daily mood. **mHealth 流失基线。**
- Hueller, J., Reimann, M., & Warren, C. (2023). Streaks. *J Assoc Consumer Research*. **6 实验 N=3,766。**
- Karpicke, J. D., & Roediger, H. L. (2008). The Critical Importance of Retrieval for Learning. *Science*. **检索练习 vs 反复阅读。**
- Cambridge Experimental Economics (2024). (Not) alone in the world: Cheating in the presence of a virtual observer. **观察者效应。**
- Sparrow, B., Liu, J., & Wegner, D. M. (2011). Google Effects on Memory. *Science*. **认知卸载先于 AI。**
- Risko, E. F., & Gilbert, S. J. (2016). Cognitive Offloading. *Trends in Cognitive Sciences*. **目标设定是关键调节因素。**
- Optimizing Feedback Frequency in Motor Learning (2021). *Perceptual and Motor Skills*. **inverted U：50% 频率 ≥ 100% 频率。**
- Stabilarity Hub (2026, M/W). Cost-Effective AI: Total Cost of Ownership for LLM Deployments. **TCO 340-580% 低估。**
- arXiv 2604.24110 (2026). Latency and Cost of Multi-Agent Intelligent Tutoring at Scale. **多 agent 系统延迟与成本。**

### 行业产品（W 级，结构借鉴而非效果）

- TradeUpCoach (cognitive support system，背景实时干预 + 多模态信号)。
- Edgyx Ora (post-trade emotion + bias 分析)。
- Vigil (post-hoc trade audit)。
- KeelTrader (实时心理干预)。
- NICE Actimize / TradingTechnologies / Hadrius / Knowtice / Quod Financial (机构合规交易监控行业产品)。

### Phase 1 已引（重新切片，未重复）

- Bastani et al. (2024). *PNAS*。
- METR (2025). Measuring AI Impact on Experienced OS Developer Productivity。
- Kosmyna et al. (2025). Your Brain on ChatGPT. arXiv 2506.08872。
- Lee et al. (Microsoft × CMU, 2025). CHI 2025。
- Hodge et al. (2023). *J Behavioral Finance*。
- FCA (2024). Occasional Paper 66. Playing the Market。
- Robinhood notification trading study (Moss working paper, austinsmoss.github.io)。
- Yeager et al. (2014). *J Exp Psychol Gen*。
- Cipriano, Gruca & Jiao (2020). *J of Prediction Markets*。
- Sbarra et al. (2013). *Clinical Psychological Science*。
- Watkins & Teasdale (2004). *J Abnormal Psych*。
- Beighton (2018). Reflective practice and performative compliance。
- Lelkes et al. (2012). *J Exp Soc Psych*。
- Capraro et al. (2024). *Nature Human Behaviour*。
- Steiss et al. (2024). *Learning and Instruction*。
- Stanford SCALE (2024-2025) working papers on Socratic AI。
- Liu (2025). *J Computer Assisted Learning*。
- Frontiers (2025) ITS 941 学生一年研究。
- Frattaroli (2006) expressive writing meta-analysis。
- Goh et al. (2024). *JAMA Network Open*。
- npj Digital Medicine (2026) human-LLM clinical collaboration meta-analysis。
- Mayo Clinic ML alert (medRxiv 2021)。
- BMC Medical Informatics and Decision Making (2025) ED CrI alert system。

---

## 附：本笔记的关键反直觉发现汇总

| # | 反直觉发现 | 含义 |
|---|---|---|
| 1 | "前台对话 AI" 没有击败 "静态 AI 信息"（CRC 筛查 RCT, Liu 2025） | "对话比静态好"是默认假设，证据不支持 |
| 2 | AI 暴露 **10 分钟** 即引发 persistence 损失（Liu 2026 N=1222） | "短期使用无害" 假设崩塌 |
| 3 | hint 路径与答案路径在 persistence 损失上**有质的差异** | σ 系统的 AI 设计原则可由此具体化 |
| 4 | 50% 频率反馈 ≥ 100% 频率反馈（motor learning Guidance Hypothesis） | "更多反馈 = 更好" 直觉错误 40 年 |
| 5 | unrestricted AI ≥ restricted AI（IZA 2025）；restricted 触发 "intensive bursts of prompting" | "限制 AI = 保护学习" 不一定对 |
| 6 | 前台 cognitive forcing function 减少 over-reliance（Bucinca 2021），**但用户主观最不喜欢** | 用户偏好与学习效果再次对立 |
| 7 | 拟人化 robo-advisor 恶化处置效应（Hodge 2023） | 把后台分析包装成前台对话**最差** |
| 8 | passive sensing 自杀风险预测**力低于 active 数据** | 后台 AI 不是万能，至少在短期高敏感预测上 |
| 9 | Therabot RCT MDD d=0.85（结构化 CBT 前台 AI 有效） | 前台 AI 不是普遍有害——结构化协议是关键 |
| 10 | mHealth 71% depression apps **没有真正实现 JITAI**（仅自我报告） | 现有"后台 AI"产品多名实不符 |
| 11 | AI 反馈在质量上 ≥ 人类反馈，**但行为变化更弱**（Steiss 2024、IJETHE 2026） | wise feedback 迁移到 AI 的核心难题 |
| 12 | 无 AI 不等于无伤害——高反刍者写日志变差（Sbarra 2013） | "无 AI = 安全" 也是错觉，需要结构化设计 |

---

> **本笔记终极结论（U 级）**：
>
> 如果必须三选一作为 σ 系统主入口的默认形态，证据指向**"无 AI 或后台 AI"**——前台 AI 在 4/6 维度上证据反向。但**没有任何形态在所有维度都最优**：错误检测维度 AI（不论前后台）显著优于无 AI。
>
> **σ 系统的合理设计是分时刻分配形态**：
> - 决策瞬间 / 平仓后立即 / 生理门禁 → **无 AI 静态规则**
> - 周/月异步复盘 / 异常告警 / 行为模式监控 → **后台 AI（可选）**
> - 用户主动求助 / 离线学习 / 文献查询 → **前台 AI（受限，先独立写后 review）**
>
> 这个分配与 foundation v5 §三.2 / §三.3 / §三.6 一致，是本调研给 Phase 2 Design 的最具体输入。
>
> **诚实标记**：上述所有具体分配都是 U 级——基于已知文献的逻辑外推；没有任何 RCT 直接验证"按时刻分配 AI 形态"的设计在 trading 场景的有效性。Phase 2 应作为**初始假设 + N-of-1 个人验证**而非已确立约束。
