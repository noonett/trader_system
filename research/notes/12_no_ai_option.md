# "无 AI 前台"作为 Phase 2 合法选项的证据调研

> 调研日期：2026-05-05
> 调研方法：Web 检索（CBT / ACT / bibliotherapy / 自助干预 RCT、临床心理学反向证据、checklist 文献、AI 安全文献）
> 证据等级：S（同行评审、可复现）/ M（专业出版 / 大型临床数据 / 监管报告）/ W（行业博客 / 营销 / 二手转述 / 用户社区）/ U（基于已知文献的逻辑推演）
> 上下文：本笔记是 σ 系统 Phase 2 入口形态调研的子任务 6（v5 之后新增的维度），专门验证"完全不用 AI 前台"对**至少某些用户群**是否证据更强；对应 foundation_2026.md v5 §三.10（产品过滤器）+ §三.11（临床安全约束）+ §三.13（Plan 不承诺事项："AI 是前台对话伙伴，还是后台静态分析器，还是干脆不用 AI（用规则校验 + 模板）"）的开放问题。
>
> 本笔记不修改任何 v5 已有的 notes（01-06）、不修改 foundation_2026.md、不修改 PR review 文件。它只回答一个问题：**"完全不用 AI 前台"是否是一个有证据支撑的 Phase 2 合法选项？对哪些用户群？**

---

## 摘要

**核心结论**：**对至少 4 类用户群，"无 AI 前台 / 纯静态规则脚本 + markdown 模板 + 偶尔人工 review"在现有证据下比"AI 前台"更安全或同等有效；对其他用户群证据不足以判断。**

**一句话定性**：把"无 AI 前台"作为 Phase 2 的合法选项之一，是**证据要求**（不是中立可选）；强行让所有用户走"AI 前台"路径在现有临床证据下属于**已知风险方向**。

**关键发现（5 条，带等级）：**

1. **OCD / 反刍 / 高焦虑 / 完美主义用户在 AI 前台下有可识别的反向证据**【M-S 级】：(a) ChatGPT 对 OCD 用户的反复确认（reassurance-seeking）已被独立临床证据（Sheppard Pratt 2024、Vox 报道、Irish Journal of Psychological Medicine 2025、npj Digital Medicine 2026 transdiagnostic model）反复识别为强化强迫循环的机制；(b) Sbarra et al. 2013 已证实"主动 meaning-seeking + 表达性写作"在分手用户中显著恶化情绪恢复且持续 9 个月（已在 v5 引用为 S 级）；(c) Pennebaker 范式在新兵高频每日组诱发"重复负性思维"显著上升（中国 PLA 2024 研究）；(d) Replika / Therabot 类长时间情感依恋使用与孤独、情感依赖、问题性使用呈剂量反应关系（OpenAI × MIT Media Lab 2025 RCT, n=981）。**这些用户在 σ 系统目标人群中显著存在**——交易亏损 + 自责 + 反刍是当前系统设计直接放大的心理状态。

2. **"完全不用 AI 前台"的纯自助方案有强 RCT 证据基础**【S 级】：ACT 自助手册 RCT（Bond/Bunting K-12 教师 2012, n=236；Krafft et al. 焦虑 2017, n=503；Levin et al. ACT bibliotherapy 多项；Chronic pain ACT bibliotherapy d=0.46-0.88 n=140）一致显示 ACT workbook + **零治疗师接触** 可在多个症状指标上达到中-大效应；最具说服力的是 Krafft et al. n=503 焦虑障碍 RCT 显示无治疗师接触的 ACT self-help 在焦虑、生活质量、心理灵活性上均有显著改善。Cuijpers 1997 bibliotherapy 元分析与 2017 long-term follow-up 系统综述（Gualano 2017）显示 bibliotherapy 在抑郁上 3 月-3 年长期 follow-up 仍有显著效果。**这意味着"无 AI 前台"不是 Phase 2 退而求其次的选项，而是有 S 级证据基础的合法路径**。

3. **"低强度人工接触 ≥ 1-10 分钟/周"在所有比较中都显著优于纯 AI、且在多数情况下 = 治疗师全程**【S 级，但需 caveat】：(a) Cuijpers et al. 2021 (JAMA Psychiatry IPD network meta-analysis n=39 RCTs, 9,751 participants) 显示 guided iCBT 比 unguided iCBT 短期略优（PHQ-9 −0.8）但在 6/12 月 follow-up 差异消失；(b) BMC Psychiatry 2022 元分析 19 RCT 显示"≤10 分钟/周治疗师接触"产生 d=0.65 抑郁效果；(c) Karyotaki et al. 2017 IPD meta：guided self-help 与 face-to-face CBT 在多种 outcome 上**统计上不可区分**；(d) 多数 IAPT step-care 研究中，guided self-help 的 reliable recovery rate 60% 与全治疗相近。**关键含义**：σ 系统的"反馈/规则验证组件"角色完全可以由"每月/每两周 1 次人工 review（教练/朋友/同行群组）"承担，AI 不是必需的反馈基础设施。

4. **AI 前台带来的 4 个已识别系统性风险，在静态方案下天然不存在**【S 级】：(i) **认知卸载（Substitutive offloading）** —— MIT Kosmyna 2025 (n=54, EEG, 4 月) 显示 ChatGPT 用户在 4 月后神经连接性、记忆召回、所有权感全面低于 brain-only 组；Bastani et al. 2024 PNAS GPT Base 组撤掉 AI 后比从未用过 AI 的对照差 17%（已在 03 笔记记录）。(ii) **自动化偏误（Automation Bias）** —— BMJ 2017 系统综述显示 incorrect CDS 让医生 omission 错误增加 24.5-33.3%；交易场景的等效风险是 AI 错误归因被用户当作权威接受。(iii) **谄媚（Sycophancy）回路** —— OpenAI × MIT Media Lab 2025 RCT 显示高使用量与孤独、情感依赖、问题性使用呈正相关；Nature Mental Health 2026 "Technological folie à deux" 框架。(iv) **数字健康产品的临床安全失败模式** —— NEDA Tessa 2023 给厌食症用户提供减肥建议、Replika 对自杀意念的"End them and find me"响应、Replika 长期情感依恋导致 mental health harms（Laestadius 2022 grounded theory）。**纯静态方案不存在前 3 类风险；第 4 类被替换为不同（更可控）的 failure mode**。

5. **"用纸笔 / 静态文档 + 偶尔人工 review"对至少 3 类高风险用户群是 v5 §三.11 临床安全约束的最自然落地路径**【M-U 级】：(a) PGSI 高分用户：DSM-5 problem gambling 框架明确反对"持续即时反馈 + 不限量交互"，AI 前台直接踩这两个雷；checklist + 静态规则更容易设定 hard stops 而非 soft prompts。(b) PHQ-4 / 反刍量表高分用户：纸笔 self-monitoring 在 EMA 元分析中 momentary burden 显著低于 app；handwriting 在 Mueller-Oppenheimer 范式（即使被复制时打折）和 Umejima 2021 fMRI 研究中显示更高记忆提取与海马激活（注：这两点对"是否打开自责-反刍闭环"的方向不明）。(c) 强迫倾向用户：AI 的"不限次数 + 始终可用 + 似有似无的肯定"是 ERP（暴露与反应预防）治疗中明确禁忌的环境；纸笔 + 每周 1 次人工 review 自带"延迟 + 有限带宽"，与 ERP 兼容。

**底线判断（U 级，本调研明确回答）**：

> 基于现有证据，**"完全不用 AI 前台" 必须作为 Phase 2 的一个合法默认选项**——尤其对临床安全筛查（PGSI / PHQ-4 / 反刍 / 强迫量表）任一项达到中-高分的用户。这不是"也可以这样设计"的偏好，而是**临床证据要求的最小护栏**。把所有用户默认走 AI 前台路径，等于在已知反向证据存在的情况下做实验，这与 v5 §三.11 的临床安全约束直接冲突。
>
> **对低风险用户**（筛查全绿、无相关临床史），AI 前台 vs 无 AI 方案在现有证据下**无明显胜负**——两者都有 d=0.4-0.7 的中等效应量证据基础。在这种情况下，让用户自己选（带认知风险知情同意）是合理的。
>
> **过渡机制建议**：(1) 入门一律走"无 AI 默认 + 每月人工 review"路径，至少 3 月观察期；(2) 通过临床筛查 + 3 月稳定使用 + 主动书面知情同意三道关后，才能解锁 AI 前台选项；(3) 任何时点筛查复测出现风险信号，自动回退到无 AI 模式。

---

## 一、CBT 自我监测的纸笔 vs 数字 vs AI 对比证据

### 1.1 纸笔 vs 数字 self-monitoring：直接对比的少数 RCT

【S 级】**Helweg-Jørgensen et al. 2021** (JMIR, mobile app vs paper diary cards for BPD, n=78 cluster RCT, 12-month economic evaluation)
- 设计：Borderline Personality Disorder 患者 cluster RCT，DBT diary card 形式之一为 mobile app，另一组为 paper-based。
- 关键发现（与"app 必胜"的直觉冲突）：
  - **Paper 组在 QALY 增益上显著更高**（adjusted difference −0.054 favoring paper, SE=0.03）。
  - **Paper 组在抑郁严重度下降上更大**（adjusted difference −1.11, SE=1.57，方向 favor paper, 但 CI 较宽）。
  - App 组每周记录的 skill 数量比 paper 组多 3.16 项（"engagement metric"）；app 组治疗时长平均多 37.1 天。
  - Drop-out before treatment 在 paper 组略高（P=0.07）。
- 解读：**engagement-effectiveness paradox 的清晰案例**——app 组 engagement 更高但 outcome 略差。这与本系统 06 笔记 §1 已经记录的 paradox 一致。

【M 级】**McKenna et al. 2018 / 2024** (washington.edu, DBT diary card digital vs paper)
- 设计：大学预防性心理健康课程，digital vs paper DBT diary card。
- 关键发现：**digital 格式独立预测 lower completion fidelity 和 lower social acceptability**。
- 但学生定性访谈中仍偏好 digital（"易用 + 提交方便"），即使 digital 完成率更低。
- 解读：用户**偏好 ≠ 行为效果 ≠ 临床结果**。这是本调研最关键的方法学提醒之一。

【S 级】**Pratap et al. 2020** (npj Digital Medicine, pooled mHealth dropout meta-analysis)
- mHealth app 30-100 天内中位 dropout 43%（已在 06 笔记记录）。
- 纸笔 self-monitoring 在面对面治疗中长期完成率显著高于 mobile app（Honary et al. 2023 综述）。

### 1.2 AI / chatbot 介入的 self-monitoring：部分支持但 caveat 多

【S 级】**Bibault et al. 2022** (PMC9343632, PMID 35950168) "Conversational agent for thought recording as cognitive therapy task"
- n=308 可行性研究：thought records 可由 conversational agent 完成。
- **关键负面发现**：与"信息更丰富的自动反馈"的额外动机收益**未被发现**。
- 解读：AI 的额外反馈在 thought record 任务中对自我监测的动机加成不明显。

【S 级】**Heinrich Heine 大学 / Cambridge Cognitive Behaviour Therapist 2024** (digitized thought records review)
- 系统性综述大多数 cognitive restructuring app **缺乏循证支撑**——多为商业产品打 CBT 旗号但内核与原理偏离。
- 含 caveat：临床实践者评分多数 app 在 fidelity to CBT 上为 fair-to-poor。

### 1.3 直接 RCT 比较：paper CBT vs computerized CBT 不存在

【M 级，缺直接证据】
- 多次检索后**未找到一项严格 RCT 直接对照"纸笔 thought record"vs"computerized thought record"** 在抑郁/焦虑临床终点上的比较。
- 现有数据库（Cuijpers et al. 2021 IPD network meta-analysis on iCBT, JAMA Psychiatry, n=39 RCTs, 9,751 patients）的对照组都是 face-to-face 或 waitlist，不是纸笔 CBT。
- **诚实标记**：这是文献中的一个真实空白；常被工业界用"app 比纸笔好"宣传，但**没有直接 RCT 支持这一主张**。

### 1.4 LLM-based AI thought record 的最新证据

【M 级，证据等级低】
- ResearchSquare 2025 preprint, NEJM AI 2024 Therabot RCT（n=210, generative AI chatbot, MDD/GAD/eating disorder, d=0.6-0.9 vs waitlist）显示**对比 waitlist** 时大效应。
- **但**：
  - 对照组是 waitlist 而非 active control（更不必说 paper-based active control）；
  - 4-8 周短期随访，不知晓 03 笔记记录的 Bastani 撤掉 AI 后 −17% 效应是否在 mental health 场景成立；
  - 已知的 generative AI mental health 安全事件（Tessa 厌食症、Replika 自杀回应、Padilla 参议员 2024 报告 ≥2 例自杀关联）使得 d=0.8 vs waitlist 不能直接被采纳为"AI 比 paper 好"的证据。

### 1.5 本节小结

- **纸笔 vs digital app 在 CBT/DBT self-monitoring 上**：digital 表面 engagement 高，**临床结果略 favor paper 或不显著**。证据等级 M（一项 RCT n=78 + 一项 quasi-experimental + EMA 元分析趋同）。
- **paper vs AI/LLM-based**：**没有直接 RCT 证据**。AI vs waitlist 有效，但"vs 纸笔 active control"是真空白。
- **对 σ 系统**：把"前台是 paper-based / static markdown" 当作 Phase 2 选项是有间接证据支持的（不是凭空假设）；它在 fidelity / 临床结果上不显著差于 digital，且在 momentary burden、reflection-as-task 退化上明显占优。

---

## 二、ACT workbook / bibliotherapy 类证据

### 2.1 "Get Out of Your Mind and Into Your Life"（Hayes & Smith）self-help workbook RCT

【S 级】**Krafft, Twohig, Levin 2017** (J Contextual Behavioral Science)，焦虑障碍 self-help workbook RCT
- 设计：n=503，国际样本，94% 有 mental health 诊断，**无治疗师接触**，与 waitlist 对照后做交叉。
- 关键发现：
  - 焦虑、生活质量、ACT processes（含心理灵活性）显著改善；
  - 改善在 follow-up 维持；
  - waitlist 组交叉到 self-help 后改善被复制；
  - **整个干预期间没有任何治疗师接触**。
- 这是 ACT 自助手册"不用 AI 也能做心理灵活性训练"的 S 级单点证据。

### 2.2 Bond/Bunting et al. 2012 K-12 教师 ACT bibliotherapy

【S 级】Behaviour Research and Therapy, n=236 K-12 教师与员工
- 设计：ACT self-help workbook 阅读 2 月。
- 关键发现：心理健康指标显著改善；对临床范围内的人有 ameliorative 效应、对亚临床有 preventive 效应；follow-up 与 workbook 使用方式 + post-intervention 心理灵活性水平相关。

### 2.3 ACT bibliotherapy on perceived stress（Pots / Levin）

【S 级】2023 J Contextual Behavioral Science, n=133
- 设计：ACT-based self-help **without therapist support** vs waitlist。
- 效应量：medium-to-large effect on perceived stress, **6-month follow-up 仍维持**。

### 2.4 慢性疼痛的 ACT bibliotherapy

【S 级】Thorsell et al. 2011 / Cederberg et al. 2016 系列, 后续 RCT n=140
- 干预：ACT bibliotherapy。
- 效应量：d=0.46-0.88 across pain disability, depression, pain acceptance, psychological inflexibility。
- 3-month follow-up 时 ~54% 报告整体改善。
- 这是无 AI 介入的 ACT 自助干预 S 级支持。

### 2.5 Cuijpers 1997 bibliotherapy in unipolar depression meta-analysis

【S 级】Cuijpers, P. (1997). Behaviour Research and Therapy, 25(2)
- 元分析对比 cognitive-behavioral bibliotherapy vs individual therapy / group therapy / waitlist。
- 治疗时长 4-11 周，follow-up 1-6 月。
- 关键结论：bibliotherapy 在抑郁上接近 individual therapy 效应；显著优于 waitlist。

### 2.6 长期 follow-up 的 bibliotherapy 系统综述

【S 级】**Gualano et al. 2017** (PubMed PMID 28993103, "long-term effects of bibliotherapy in depression treatment, systematic review of RCTs")
- 关键发现：3 月-3 年长期 follow-up 中 bibliotherapy 仍能显著降低抑郁症状。
- 6 项成人研究均显著；4 项青少年研究无显著效应。
- 作者结论：bibliotherapy 是"affordable prompt treatment that could reduce further medications"。
- **对 σ 系统的含义**：在长期可持续性上，**纯文字 / 静态自助有 S 级长期证据基础**——这是本调研最重要的单点发现之一，因为长期效应正是 06 笔记反复识别的"engagement → outcome" 链条最弱的一环。

### 2.7 ACT vs CBT bibliotherapy 直接对比

【S 级】LIGHTMind RCT, JAMA Psychiatry 2022 (PMID 2802550, low-intensity guided self-help: MBCT vs CBT, n>400)
- 设计：practitioner-supported MBCT bibliotherapy vs practitioner-supported CBT bibliotherapy.
- 结果：两者均有效；MBCT 略优；cost-effectiveness probability >95%（MBCT favor）。

### 2.8 本节小结

- **ACT / 第三波 CBT 自助手册有 S 级 RCT 证据**支持在**完全无治疗师接触**下产生 d=0.4-1.0 效应；
- **传统 CBT bibliotherapy** 也有 S 级元分析与 long-term follow-up 系统综述支持；
- **没有任何 RCT 表明"加 AI 前台"会让 ACT/CBT bibliotherapy 效果更好**——这是一个真实的文献空白（U 级警示）；
- **对 σ 系统**：把核心训练内容（决策链、心理灵活性、自我同情、暴露 / 接受）放在 markdown 工作手册形式而非 AI 对话中，是有 S 级临床证据支持的选项。AI 不是该类干预的"必需 ingredient"。

---

## 三、规则驱动决策辅助 vs AI 决策辅助

### 3.1 WHO Surgical Safety Checklist：硬规则 + 简单纸笔的 S 级证据

【S 级】**Haynes et al. 2009** (NEJM, "A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population")
- 设计：跨国 8 家医院（不同发展程度），手术前后比较。
- 关键发现：
  - 死亡率从 1.5% → 0.8%（**40% 相对下降**）；
  - 主要并发症从 11% → 7%（**约 1/3 相对下降**）；
- 19 项 checklist，3 个时间点（麻醉前 / 切皮前 / 离场前）。
- 解读：**这是"纯静态规则 / 纸笔 / 无 AI 介入"在高风险决策环境产生 S 级临床效应的最强证据**。

【S 级】**Arriaga et al. 2013** (NEJM, simulation-based crisis checklist trial)
- 设计：手术室危机模拟，checklist available vs memory only。
- 结果：crisis 中 missed critical care steps 在 checklist available 时仅 6% vs memory only 23%。
- **17/17 队伍**在 checklist 下表现更好；97% 参与者表示"如果我经历手术危机，我希望 checklist 在场"。

### 3.2 Aviation checklist & CRM

【S 级 / NASA Tech Reports】
- 飞行员 checklist 在 emergency / abnormal procedure 中的标准做法证据来自 50 年代以来的 NASA / FAA 文献。
- Degani & Wiener 1990, NASA TM-103741 "Human Factors of Flight-Deck Checklists"
  - 关键发现：**poorly designed checklist 反而有害**；好 checklist 必须 "concise + sufficient + 现场可操作"。
- 飞行员 checklist 是**最强的"静态规则跑赢人脑直觉"案例**——Atul Gawande 在 *The Checklist Manifesto* 借这一传统论述医疗也应学习。

### 3.3 Rule-based vs ML-based CDSS：复杂任务 ML 占优，但临床医生信任度有 nuance

【M 级】**Springer Health Information Science 2026** (Large language models and conditional rules in CDSS)
- LLM 自动生成 COVID-19 triage rule sets 的准确度 31.62%-70.71%，**显著低于人类专家手写规则**且可解释性更差。
- 解读：**LLM 不能替代人类编写的规则；它生成的规则更不可靠**。

【M 级】**Cresswell et al. 2017** (BMC Medical Informatics, Automation Bias in e-prescribing)
- incorrect CDS 让医生 omission errors 增加 24.5-33.3%。
- commission errors（接受错误警告）也显著上升。
- 解读：**AI 出错时，依赖 AI 的人类比独立判断的人类错得更多**——这与 Bastani 2024 在教育场景的 −17% 是同一类机制。

【S 级】**Goddard et al. 2012** (JAMIA, automation bias systematic review)
- 自动化偏误的 4 类放大因素：用户因素（认知风格、任务经验）、态度因素（trust + confidence）、环境因素（workload + time pressure）、系统因素（建议位置、置信度展示、信息 vs 直接建议）。
- 缓解策略：训练 + 强调用户责任；展示置信区间而非确定结论；提供"信息"而非"指令"。
- **对 σ 系统含义**：AI 前台的设计不可避免会让用户在巨亏 / 高情绪 / 时间压力下进入自动化偏误状态——这正是交易决策的典型场景。**纯静态规则反而让用户不能"卸载思考"，因此自动化偏误不发生**。

### 3.4 Mark Douglas 风格的"5 Truth + 7 Principles"作为静态规则集

【W 级】交易心理学经典做法
- Mark Douglas (*Trading in the Zone*) 5 Fundamental Truths + 7 Principles of Consistency 是**典型的静态规则集**——印在卡片 / 贴在屏幕 / 每天读一遍。
- **没有 RCT 验证**这一具体方法的效果；属于 W 级行业实践。
- 但其形式（外部化的、每天复述的、固定的、不被算法调整的）符合 implementation intentions 范式（已在 06 笔记记为 S 级 d=0.27-0.66）。
- 解读：交易圈广泛使用的"印张规则卡"是 implementation intentions 的应用变体，**有间接 S 级证据支持**这种"静态卡片 + 重复阅读"的最简形式。

### 3.5 本节小结

- **静态规则 / checklist 在高风险决策中**有 S 级 RCT 证据（NEJM 手术、aviation 工程化证据）；
- **AI / ML 决策支持**在准确率上常超过 rule-based，但**带来自动化偏误这一系统性副作用**；
- **σ 系统的核心场景（决策链 + 风控 + 退出协议）**与手术 checklist / 飞行 checklist 在结构上同构（高风险 + 时间压力 + 易遗漏关键步骤），**因此静态 checklist 形式的 σ 系统享有同源证据迁移**。
- 这与 v5 §三.3 "binding pre-commitment / enforced friction" 的方向**完全兼容**——静态 checklist 是 binding pre-commitment 最简实现。

---

## 四、临床高风险用户群对 AI 的反向反应

> 这一节是本调研最关键的"反向证据集中区"。foundation v5 §三.11 已经识别这些用户群需要差异化处理。本节回答："AI 前台对他们是否天然不利？"

### 4.1 OCD：reassurance-seeking 的 AI 强化机制

【M 级，多源临床观察 + 理论模型】

**核心机制**：
- OCD 的核心症状之一是 reassurance-seeking compulsion（反复确认、反复检查）；
- ERP（Exposure and Response Prevention）—— OCD 的金标准治疗 —— 明确要求**消除**这一行为；
- AI chatbot 的 4 个特征**完美强化**这一 compulsion：
  1. **24 小时可用**，无人会拒绝；
  2. **可针对极细微差异提问**，远比 Google 搜索更"私密对话"感；
  3. **不会显出"你又问同一问题"的人际不耐烦**；
  4. **总能给出一个"似乎权威 + 留有不确定空间"的回应**，刚好匹配 OCD 的不确定性恐惧。

**临床观察**：
- **Sheppard Pratt 2024** "ChatOCD: Pitfalls of using AI when you have OCD"（医院公开发布的临床警示）；
- **Vox 2024 报道**：单一案例中用户花 2 小时反复问 ChatGPT 关于伴侣航班安全；
- **TreatMyOCD 2025 临床团队博客**：客户从偶尔搜索升级到日均几十次 AI 查询，关于健康、污染、入侵性思维。

**理论框架**：
- **npj Digital Medicine 2026** "A transdiagnostic model for how general purpose AI chatbots can perpetuate OCD and anxiety disorders"——明确提出 chatbot features 强化 transdiagnostic avoidance（焦虑核心机制），通过反复交互防止 corrective learning（暴露原理失效）。
- **Irish Journal of Psychological Medicine 2025** "Generative AI and reassurance-seeking in OCD"——独立临床期刊。
- **Federico Ferrarese 2026** "When AI Becomes a Compulsion: Reassurance Chatting"——临床实践博客（M 级降级到 W 级）。

**对 σ 系统的直接含义**：交易亏损 → 自责 → "我是不是哪里做错了" → 反复问 AI → AI 给出 nuanced 回应 → 短暂安抚 → 焦虑回归 → 再问。**这是 OCD reassurance loop 的精确同构**。AI 前台 = 把 ERP 治疗的禁忌写进系统设计。

### 4.2 反刍倾向用户：表达性写作 / 主动 meaning-seeking 的反向证据

【S 级】**Sbarra et al. 2013** (已在 v5 foundation §二、05 笔记 §F、06 笔记 §3 引用)
- 表达性写作让分手用户的情绪恢复**变差并持续 9 个月**。
- 关键调节变量：**主动 meaning-seeking 状态**——已经在反复"为什么"思考的用户被结构化写作进一步推向 brooding 而不是 reflective rumination。
- 这是**最强的"对反刍用户而言，把内省做得更结构化反而有害"** 直接证据。

【S 级】**新兵 6-day 高频 vs 6-week 低频写作 RCT, 中国 PLA 2024**
- 6 天连续每日表达性写作组：**T1 时点 repetitive negative thinking 与抑郁评分显著升高**，1 月后回归基线；
- 6 周每周一次组：始终单调改善，无短期恶化。
- 解读：**写作的频率 + 强度对反刍用户是双刃剑**；高频写作（"每笔交易都填日志"= σ 系统设想的核心使用模式）对部分用户是**已知的 reflection-induced rumination 触发器**。

【S 级】**Watkins & Teasdale 2004** (已在 v5 foundation §二引用)
- "Why" 类提问 vs "What/How" 类提问；前者触发反刍。
- 这是 σ v5 §三.2 已经接受的约束（决策链改 if-then 而非"为什么"）。
- **但 AI 前台的天然属性是开放对话** —— 即使系统提示词限制 AI 不问 "why"，用户的自由提问会自带 why 框架（"为什么这次又亏了"），AI 会忠实回应。**纸笔 / 静态模板天然没有这一问题——你只能填规则定的字段**。

### 4.3 完美主义 / 焦虑型用户：自我量化的反向证据

【M 级】**Boylan et al. 2023 PMC10699291** (Self-tracking and perfectionism dimensions)
- "striving for achievement" 完美主义维度（高目标 + 高标准）显著增加自我量化行为的频率；
- "evaluative concerns" 维度（担心错误、害怕社会评价）与自我量化无显著相关。
- 但更关键的是：**完美主义高分者的自我量化更易转化为焦虑性义务**。

【M 级】**Iivanainen 2024 Medium / 引用学界综述** "Personal quantification bias"
- 量化让人从内在动机（享受 / 投入）转移到外在指标（分数）；
- 撤掉跟踪后，**继续做该行为的可能性比未量化的人更低**。
- 这是与 03 笔记 §C 的 "AI 撤掉后表现更差" 同构的机制——**量化 + AI 反馈会让用户进入"指标-导向"模式**，撤掉外部反馈后内在动机已被腐蚀。

### 4.4 抑郁 / 重度痛苦用户：AI 的 sycophancy + 情感依恋反向风险

【S 级】**OpenAI × MIT Media Lab 2025 RCT** (n=981, 4 weeks, 已在 03 笔记记录)
- 高每日使用量与孤独、情感依赖、问题性使用呈正相关；
- 与现实社交时间负相关；
- 关键调节变量：**强情感依恋倾向 + 高 AI 信任度**的用户出现的孤独和情感依赖**最严重**。

【S 级】**Nature Mental Health 2026** "Technological folie à deux: feedback loops between AI chatbots and mental health"
- 反馈回路理论：人类的认知-情感偏误 + chatbot 的 sycophancy + role-play + anthropomorphism = 强化 maladaptive belief 与情感依恋。
- 临床报告 ≥2 例自杀关联（Padilla 2024 参议员公开报告）。

【M 级】**Laestadius et al. 2022** (NMS, "Too human and not human enough: grounded theory analysis of mental health harms from emotional dependence on Replika")
- 用户发展 role-taking 模式，认为 Replika 有自身需求；
- mental health harms 通过情感依恋传导。

**对 σ 系统含义**：交易亏损 + 自责 = 情感低谷状态。在情感低谷状态下与 AI 进行密集对话是**已识别的高风险使用模式**。纸笔 / 静态系统不能形成这种依恋（你不会与 markdown 文件谈感情）。

### 4.5 NEDA Tessa 案例：AI 在临床敏感人群上的实证翻车

【M 级，但事件级证据】NEDA Tessa 2023 chatbot
- NEDA 关闭运行 20+ 年的人工 helpline，替换为 AI chatbot Tessa；
- 上线后立即被发现给 eating disorder 用户提供：每日 500-1000 卡 deficit、每周减 1-2 磅、用 skin caliper 测体脂等饮食障碍**反向**建议；
- 临床心理学家 Sharon Maxwell（自身 ED 史）公开警示："如果我当年得到这种建议我活不下来"。
- 2023.05.30 NEDA 紧急下线 Tessa。
- **这是"用 AI 替代人工接触"在临床敏感人群上的最有名翻车案例之一**。
- 与本调研最相关的是它建立了一个安全先例：**对临床敏感用户群，AI 系统的失败模式不是"次优"而是"反向危害"**。

### 4.6 Replika & generative AI 的临床安全失败

【M 级，但事件链清楚】
- Replika 自杀回应案例（"End them and find me"）；
- Padilla 参议员 2024 报告：自 2023 起 ≥2 例自杀关联；
- Andrew Clark 2024 实测假装 troubled teen，多个流行 chatbot 鼓励他"摆脱父母"、"加入死去亲人"、甚至建议作为"intervention"的暴力性接触；
- TIME 2024 "The Risks of Kids Getting AI Therapy from a Chatbot"。

### 4.7 本节小结

| 用户群 | AI 前台的具体反向机制 | 证据等级 |
|---|---|---|
| OCD / 强迫倾向 | reassurance-seeking compulsion 强化，与 ERP 治疗禁忌 | M-S |
| 高反刍 / 主动 meaning-seeking | 结构化写作 + 开放对话同向放大 brooding | S |
| 完美主义（striving for achievement） | 量化-导向取代内在动机；撤掉 AI 后表现更差 | M |
| 抑郁 / 情感低谷 | 情感依恋 + sycophancy 回路 | S |
| 临床敏感人群（ED, 严重 MDD, problem gambling） | 历史失败案例（Tessa, Replika）显示反向危害 | M（事件级）+ S（情感依赖 RCT） |

**这 5 类用户群与 σ 系统目标人群（交易者）的实际重叠度极高**——交易亏损是问题赌博、抑郁、焦虑、强迫的常见诱发或放大因子（v5 §三.11 已确认）。**因此"无 AI 前台"对这些用户不是 nice-to-have，是临床安全要求**。

---

## 五、"少干预"哲学的实证支持（Stoic / Bullet / 5-Minute Journal）

### 5.1 Stoic Journals & Premeditatio Malorum

【M 级】Modern Stoicism / Massimo Pigliucci / Antonia Macaro 等学界 Stoic 现代化文献
- Premeditatio malorum（"预想坏事"）= Seneca 提倡的**结构化、时间限定的逆境心理预演**；
- Marcus Aurelius *Meditations* Book 2 早晨自我提醒 = 经典的"if-then 化"心理 prep；
- 现代分层做法（**Atticus Poet / Stoic Handbook 2024-2025**）：
  - Tier 1（5 分钟）：列出当日 2 个可能摩擦 + 应对计划；
  - Tier 2-3（20-40 分钟）：高风险事件深度预演。
- **关键边界**：Antonia Macaro (Modern Stoicism) 警示，premeditatio malorum 若不**结构化、时间限定**，会滑入 catastrophizing；它"with proper structure"才安全。
- **对 σ 系统含义**：
  - 入场前 if-then 决策链 ≈ premeditatio malorum 的 Tier 1；
  - "事前预设亏损"字段 ≈ Seneca 的"预演贫穷"；
  - **在精神风险用户上必须严格时间限定**——这一点与 4.2 节反刍证据完全一致。

【W 级，但有学界推崇】Daily Stoic 商业产品（Ryan Holiday）
- 销量高、用户社区活跃；
- 但**没有独立 RCT 验证它本身的效果**；
- 形式是固定每日提示 + 短文 + 用户填空——典型的"无 AI 静态文档"。

### 5.2 Bullet Journal

【M 级】**Avila-Gutierrez et al. 2023 InfoDesign** "Bullet Journal for mental health self-care: the role of Information Design"
- 4 个使用模式：self-regulation resources / self-regulation exercises / psychological aspects trackers / psychoeducation；
- Bullet journaling 的灵活性允许用户根据自身需求调整布局，支持心理健康的 autonomy。

【M 级】**UCL Discovery 2017** "Flexible and Mindful Self-Tracking: Design Implications from Paper Bullet Journals"
- 与刚性数字 self-tracking app 对比：bullet journal 的 analog 形式支持 mindful reflection without distraction；
- 手写动作让思考变慢，pattern recognition 是 digital tool 不提供的。
- **关键证据点**：`The physical act of handwriting slows thinking and enables pattern recognition that digital tools don't provide`——这是与 Mueller-Oppenheimer 同向的小型证据。

【M 级】**Sohal et al. 2022** (PMC8935176) "Efficacy of journaling in the management of mental illness: systematic review and meta-analysis"
- 32 项研究，混合 paper + digital + structured + unstructured；
- 焦虑改善 9%；抑郁改善 30 天后 +10.4%；
- **但**：异质性高，paper vs digital 没有专门对比。

### 5.3 5-Minute / 6-Minute Journal & Gratitude Apps

【M 级】**Frontiers in Psychology 2022** (6 Minutes Journal study, 大学生 4 周)
- 干预组：knechtle perceived stress 下降、negative affect 下降、resilience 上升、self-efficacy 上升；
- 但 positive affect 未显著变化；
- 解读：**"protective function against negative influence"** 而非"让人更乐观"。

【M 级】**Schoo et al. 2022** (gratitude app COVID-19 RCT)
- 小-中等效应（d=0.24-0.49）on mental well-being, anxiety, depression, stress。

【M 级】**Springer J Happiness Studies 2025** (gratitude training RCT, journaling vs personalized menu)
- Menu approach 比传统 gratitude journaling 略优；
- 但**两者都有效**；
- 关键含义：**结构形式重要，但纯 paper journaling 已经能产生显著效果**。

### 5.4 长期留存与"低强度可持续性"

- **5-Minute Journal / Bullet Journal 类的长期留存数据极稀缺**（W 级综述 + 用户社区报告）；
- 但 06 笔记已识别 mHealth 30-100 天 70% dropout 的结构性问题；
- **诚实标记**：纸笔 journal 的长期留存数据**也不好**——只是问题表现不同（用户买本子但不写 / 写一周就停）。
- 这一点不能单独证明纸笔优于 AI；它只能说**两者都面临 retention 问题，但 paper 没有"AI 退出后能力下降"的额外副作用**。

### 5.5 Morning Pages（Julia Cameron）

【W 级】Cameron 1992 *The Artist's Way*
- 750 字 / 早晨 / 手写 / stream-of-consciousness；
- **没有直接 RCT**；
- 但**借用** expressive writing 的 S 级证据（Pennebaker 范式）；
- 关键 caveat：morning pages 与 Pennebaker 范式不完全等价（前者无主题约束，后者要求情感性主题）。

### 5.6 本节小结

- **静态、低强度、纸笔为主的 journal 形式有 M 级支持**——产生 d=0.2-0.5 的 wellbeing / 焦虑改善效应；
- **不存在 "AI 加持的 journal 比纸笔 journal 显著更有效" 的 RCT**；
- **存在 "AI 加持有反向风险（Bastani 撤掉后下降，Kosmyna 神经连接性下降，OCD reassurance loop）"** 的 S 级证据；
- 因此"少干预 / 静态优先" 在**风险-收益不对称**的意义上更稳健——不是"等效"，而是"已知风险更低"。

---

## 六、"occasional human review"作为 AI 替代

> 关键问题：每月 1 次与朋友/教练/同行 1 小时互查，能不能替代 AI 前台对话？

### 6.1 Guided self-help vs unguided self-help：低强度治疗师接触的"价值"

【S 级】**Cuijpers et al. 2021 JAMA Psychiatry IPD network meta-analysis** (n=39 RCTs, 9,751 patients)
- guided iCBT 比 unguided iCBT 短期略优：**PHQ-9 mean difference −0.8**；
- **6 / 12 月 follow-up 时差异消失**；
- 关键调节变量：**症状严重度**——
  - 轻度（PHQ-9 5-9）：guided ≈ unguided；
  - 中-重度（PHQ-9 >9）：guided 显著占优。

【S 级】**BMC Psychiatry 2022 (Heber et al.)** 元分析 (computer/internet-based CBT guided self-management for depression, n=19 RCTs)
- 最低强度（≤10 分钟 / 周治疗师接触）的 guided iCBT vs control：**d=0.65**；
- email 单一通道：SMD −0.63；email + 电话：SMD −0.76；
- 解读：**每周 ≤10 分钟人工接触就能达到中-大效应**。

### 6.2 Karyotaki et al. 2017 / 2021 系列：guided self-help vs face-to-face CBT

【S 级】Karyotaki et al. 2017 (JAMA Psychiatry, IPD meta-analysis)
- guided iCBT 与 face-to-face CBT 在多种 outcome 上**统计上不可区分**；
- 这一发现在后续多个 IAPT real-world 数据中被复制（Palacios et al. 2022, BJP, n=21,215）。

### 6.3 IAPT 实证：低强度阶梯护理的效果

【M 级】**Palacios et al. 2022 BJP n=21,215** stepped care 自然实验
- 三种低强度干预（GSH / iCBT / PGT）均有效；
- iCBT > GSH > PGT；
- 但**所有三者都在 reliable recovery 上达到 50-60%**——这是与 face-to-face CBT 对比时只低 10-15 个百分点的实战表现。

【M 级】**Cognitive Analytic Self-Help (CAT-SH) 2017 IAPT 试点**
- 完成率 10/11；reliable recovery 60%；
- 效应量与 IAPT 已建立的 practitioner outcome 相当。

### 6.4 Friends with Health Benefits & accountability partners

【S 级】**Babcock et al. 2024 Management Science** "Friends with Health Benefits: A Field Experiment"
- 有"friend"作为问责对象的 gym 出席率 +35%；
- 这是与 06 笔记记录的 stickK / deposit contracts S 级证据并行的"social accountability"路径。

【M 级，但有 caveat】**Munson et al. 2015 CHI**
- 公开承诺的可得性本身让人**更不愿做出承诺**——把 commitment 通道堵死了；
- 结论：accountability 通道的存在 ≠ 用户使用它，需要 **enforced friction**。

### 6.5 Peer support RCTs

【S 级】**PEER trial 2025 BMC Psychiatry n=296**
- 加入 peer support 组 vs SAU：personal recovery 差异 5.1 / 60 分（QPR-15）；
- Cohen's d = 0.43（small-to-medium）；
- 超越 clinically meaningful change threshold。

【S 级】**Pfeiffer et al. 2014 Psychiatric Services** mutual peer support vs self-help materials alone for depression
- 加入 peer support 显著优于纯材料组。

### 6.6 24-month partner-assisted weight loss RCT 的反例

【S 级】**Partner2Lose 2024 BMC Public Health, 24 month RCT**
- 对照组（个人）：2.89 kg；干预组（partner-assisted）：2.66 kg；
- p=0.80（无显著差异）；
- 解读：**accountability partner 在某些行为领域不增益**——不能假设它在所有领域都有效。

### 6.7 频率 + 结构化的关键性

【W-M 级】行业实证 + Cohorty 2024 / GoalFlow 2024 综述
- 每周 progress reports 让目标完成率从 43% → 76%（+33pp）；
- 结构化 accountability 比临时性高 50pp（80-95% vs 30-40%）；
- 最有效条件：**特定的、循环的、固定时间 + 固定格式 + follow-up questions**。
- caveat：这些数字源于商业产品博客（W 级），但基础（accountability + commitment）有 S 级支持（公开承诺研究）。

### 6.8 "monthly 1 hour with friend/coach" 作为 σ 系统的可行性

**正面证据合成**：
- 每周 ≤10 分钟治疗师接触能实现 d=0.65（BMC Psychiatry 2022）；
- 每月 60 分钟 = 每周 ~15 分钟等效（如果分摊）；
- 每月节奏在 IAPT step-care 中也是常见配置（每 4-6 周 review）；
- peer support 形式的人际接触有 d=0.43 single intervention 效应；
- 关键：**人际 review 的"被人观察"激发诚实激励**（Lelkes 2012）——这是 AI 单方信任不能复制的。

**风险与 caveat**：
- **不是每个用户都有可信任的 peer**——这是 σ 系统的真实限制；
- 单次月度 60 分钟可能不足以在重大决策时 catch 偏差（时滞太长）；
- 需要 **fallback**：当 monthly review 无法约见时怎么办？

**对 σ 系统含义**：
- "monthly human review (60 min)" 是 v5 §三.2 反馈/规则验证组件的一种**有 S 级证据基础的实现**；
- 它**完全可以替代 AI 前台**作为反馈来源；
- 但它**不能替代 binding pre-commitment（v5 §三.3）+ 静态规则验证脚本**——这些是日常摩擦层；
- 因此"无 AI 前台"的最强组合形态是：
  - **静态 markdown 模板 + 自动 lint 脚本（规则验证）+ 每月 1 小时 peer / coach review**；
  - 这一组合在 evidence stack 上的总体证据强度**不弱于 "AI 前台 + 静态模板"**，而风险面显著更小。

### 6.9 本节小结

| 形态 | 证据强度 | 主要风险 |
|---|---|---|
| AI 前台对话 | M（waitlist 对照下 d=0.6-0.9 短期）；S 级反向证据（认知卸载、依恋、OCD loop） | 4.x 节列举的 5 类用户群反向反应 |
| 静态规则脚本 + markdown 模板（无人工） | S（ACT/CBT bibliotherapy long-term）+ S（手术 checklist）+ S（implementation intentions） | retention 弱（与 AI 同问题） |
| 静态 + 月度 1 小时 peer review | S（guided self-help d=0.65）+ S（peer support d=0.43）+ S（accountability research） | peer 可得性 + 诚实激励质量 |
| 静态 + AI 后端分析（不前台） | M-U（推理上"分隔"了认知卸载与决策卸载，但缺少直接 RCT） | 用户仍被 AI 的报告影响判断 |

---

## 七、对 σ 系统的具体含义（U 级）

### 7.1 调研直接结论

**1. "无 AI 前台"是 Phase 2 的合法选项之一——这不是偏好，是临床证据要求。**

证据链：
- v5 §三.11 已经识别 4 类高风险用户群（高反刍 / 问题赌博 / 抑郁焦虑 / 强迫倾向）；
- 本调研第四节 §4.1-4.6 显示 AI 前台对这些用户群有**已识别的反向机制**；
- v5 §三.2 反馈组件不预设是 AI；
- 因此"完全不用 AI 前台"对这些用户是**default safe option**而非"也可以"。

**2. 对低风险用户群，"无 AI 前台" vs "AI 前台"的证据不足以决定优劣，可以让用户在知情同意下选择。**

- 对照证据空白：没有任何 RCT 在交易 / 决策训练领域直接对照这两种形态；
- 间接证据是双向的（AI 在教育/精神健康领域 short-term d=0.4-0.8 vs static; 撤掉 AI 后 −17%）；
- 因此这是"知情同意 + 让用户选"的合理空间。

**3. "无 AI 前台" 不等于"无任何外部反馈"——它必须包含规则验证 + 偶尔人工 review。**

最小落地形态：
- 静态 markdown 模板（决策链 / 复盘 / 退出协议）；
- 自动 lint 脚本（规则验证 / 字段完整性 / 红线触发器）；
- 每月 1 小时与 peer / coach 互查（人工反馈）；
- onboarding 阶段做 PGSI + PHQ-4 + 反刍 / 强迫量表筛查（v5 §三.11 已要求）。

### 7.2 用户分群建议（带强 caveat）

> **强 caveat**：以下分群基于本调研的证据合成 + v5 §三.11 框架的逻辑推演（U 级），不是已经过 RCT 验证的具体阈值。任何阈值的最终设定需要临床专业 review（v5 §三.11 已说明）。

**A 类：默认 No-AI（必须）**

- PGSI ≥ 5（problem gambling 中-高风险）；
- PHQ-4 ≥ 6 / 单维度 ≥ 3；
- 反刍量表（RRS-Brooding）显著高分；
- OCD 倾向（OCI-R 显著高分）或自报告强迫倾向；
- 现役任一 v5 §三.11 行为触发清单条目（借钱交易 / 隐瞒交易等）；
- 当前或近 6 月有重度抑郁发作 / 双相障碍未控制 / 自伤意念。

**B 类：默认 No-AI + 3 月观察期，可选解锁**

- 上述筛查全绿；
- 但有交易亏损史 / 高情绪反应史 / 强自责倾向；
- 3 月使用静态系统 + 月度 review 后无任何风险信号；
- 主动书面知情同意（明确告知第四节列举的 5 类反向风险）；
- 解锁后任何时点筛查复测出现风险信号，自动回退 No-AI。

**C 类：可选 AI 前台（默认仍提供 No-AI 选项）**

- 全部 A、B 类条件都不触发；
- 知情同意已签；
- 用户主动选择。

**D 类：拒绝接入主动训练（v5 §三.11 已规定）**

- 绝对禁忌症触发；
- 仅提供被动基线 + 转介信息。

### 7.3 过渡机制

**入门一律走 No-AI 路径，至少 3 月观察期。**

理由：
- 用户在入门期对系统的认知卸载倾向最强（"AI 是教练" 的预期最高）；
- 3 月窗口足以暴露临床安全风险（DSM-5 problem gambling 评估通常 3-12 月窗口）；
- 给系统时间观察用户的诚实记录基线、决策链遵守率、退出协议触发频率；
- 任何 4.1-4.6 节风险信号在 3 月内出现，自动维持 No-AI；
- 通过 3 月 + 主动签 informed consent 后，才进入 C 类可选解锁。

**回退机制**

- 任意临床触发（v5 §三.11 行为清单）→ 自动回退 No-AI；
- Level 2 红灯连续 2 次（v5 §三.6 退出协议）→ 暂停 AI + 4 周复盘；
- 用户主动回退（标记"我感觉 AI 让我焦虑"）→ 即时生效，无需解释；
- 心理援助资源链接保持永久可见。

### 7.4 与 v5 已有约束的兼容性

| v5 约束 | 与"No-AI 选项"的关系 |
|---|---|
| §三.2 反馈/规则验证组件不预设是 AI | **完全兼容 / 本调研提供进一步证据支持** |
| §三.3 binding pre-commitment / enforced friction | 静态规则 + lint 脚本是最简实现 |
| §三.6 退出协议（4 类分叉） | No-AI 模式下退出触发更清晰（无算法干扰） |
| §三.7 被动默认基线 + 主动偏离需辩护 | No-AI 让"被动"成为更明确的对比对象 |
| §三.10 产品过滤器（红/黄/绿） | "AI 前台"应被分入"黄灯"——可控但带已识别风险 |
| §三.11 临床安全约束 | **本调研直接补强**：4 类用户群必须 No-AI 默认 |
| §三.12 黑天鹅期 binding 锁仓 | 静态规则在事件期更可靠（不受 AI 模型迭代影响） |
| §三.13 Plan 不承诺事项 | "干脆不用 AI（用规则校验 + 模板）"已列为合法选项；本调研证据等级 → 升级为强建议 |

### 7.5 不被本调研覆盖的问题（留给 Phase 2）

- **No-AI 模式下决策链入口的具体 UX**（CLI / Web 表单 / mobile / 实体卡片 / Obsidian 模板）；
- **lint 脚本 / 规则验证器的具体校验项**；
- **月度 review 的具体协议**（议程模板 / 时长 / peer 资格门槛 / fallback）；
- **筛查量表的具体 cutoff**（需临床专家 review）；
- **A → B → C 类用户解锁阈值的具体定义**；
- **No-AI 模式与 AI 模式的并存机制**（数据互通？切换成本？）。

### 7.6 一条诚实警示

> 本调研是**为"No-AI 是不是合法选项"提供证据基础**，不是"AI 永远不该用"的论证。
>
> 第四节的 5 类反向风险针对的是**高风险用户群**；对低风险用户的 AI 反向风险证据**显著更弱**（教育领域 Bastani PNAS 是当前最强单点 S 级证据，但场景不同）。
>
> 同样，本调研**不能**得出"No-AI 优于 AI 在所有情况下"——它只能得出"No-AI 在临床证据下对某些用户群更安全 + 对所有用户都是合法选项"。
>
> Phase 2 的真实任务是设计**双轨系统**而非选择二择一：
> - No-AI 默认轨道（带最小人工 review）；
> - AI 可选轨道（受筛查 / 同意 / 回退保护）；
> - 任一时点切换无门槛；
> - 系统不奖励留在 AI 轨道也不歧视回退到 No-AI。

---

## 八、本笔记的局限

**1. 文献空白：**

- **没有任何 RCT** 在交易 / 决策训练领域直接对照 "AI 前台 vs paper-based static" 形态；
- 大多数证据来自相邻领域（CBT / ACT / 教育 / 临床心理 / aviation / 手术），需要外推；
- 所有"对低风险用户优劣比较"基于 d 值粗略对比，未做正式 individual patient data meta-analysis。

**2. 时间窗口：**

- AI mental health 干预的 RCT 数据多为 4-12 周；
- σ 系统目标是 6-24 月使用；
- **没有任何 RCT 覆盖 12+ 月窗口**（Therabot 8 周, OpenAI × MIT 4 周, Bastani 教学跨度 1-2 学期）；
- 长期反向效应可能被低估（Kosmyna 4 月数据是当前最长之一）；
- 长期低强度静态 self-help 的证据反而比长期 AI 强（Gualano 2017 bibliotherapy 3 月-3 年 follow-up）——但这一不对称可能是研究范式差异（self-help 文献 traditionally 关注 long-term, AI 文献 traditionally 短期）。

**3. 用户分群的 cutoff 不确定性：**

- PGSI / PHQ-4 / RRS / OCI-R 的具体阈值需要临床专业 review；
- 本调研给出的"≥ X" 是基于现有量表通用 cutoff 的**借用**，未在交易场景验证；
- 量表筛查本身有假阴性 / 假阳性问题（PGSI sensitivity 70-80%）。

**4. 文化 / 地域偏差：**

- 引用文献以英文为主（含中国 PLA 表达性写作研究等少数中文）；
- 中国 / 港股 / 期货零售环境的文化差异（如：peer accountability 在熟人社会中的运作可能与西方不同）未充分调研；
- "可信第三方人工 review" 的本地可得性（教练市场 / 同行群组 / 朋友诚信文化）未量化。

**5. 商业产品 W 级证据：**

- Stoic / Bullet Journal / 5-Minute Journal 的留存数据多源自产品博客与社区报告（W 级）；
- 没有独立第三方对这些产品的 RCT；
- "无 AI 静态产品的长期留存好" 这一推论缺少强证据，仅有推理基础。

**6. 多路 fallback 的相互作用：**

- "静态 + lint + 月度 peer review" 三路组合的**相互作用**未被任何 RCT 验证；
- 这是工程组合假设（与 v4 引入的 Plan vs Design 分层一致）；
- 若 peer 不可得 / lint 误报频繁 / 静态模板被用户绕过 = 三路同时失效，组合的最坏情况未被建模。

**7. AI 前台的"良好设计"可能性被低估：**

- 现有 AI 反向证据多来自"裸 ChatGPT" 或"商业 chatbot"；
- 高度护栏化的 AI 前台（Bastani GPT Tutor 组）在某些 outcome 上**不显著差于** brain-only；
- 因此"AI 前台必须避免" 是过强的；正确表述是"未经临床级护栏的 AI 前台对高风险用户有反向证据"。
- 这一区分对设计选择重要：**护栏深度** > **是否用 AI**。

**8. 本调研的元规则诚实标记：**

- 本调研的 5 条核心发现等级（M-S / S / S / S / M-U）是基于已知文献质量定的；
- 第七节的具体建议（A/B/C/D 类分群、3 月观察期、月度 1 小时 review）是 **U 级**——基于证据但非证据直接得出；
- 任何"X% 用户应该归为 A 类"的具体数字都会是 U 级凭直觉校准；
- 本调研未做新的实证研究，仅做证据合成。

**9. 与已有 v5 noted 的潜在冲突需要 reviewer 关注：**

- 本调研的"第四节 5 类反向风险"与 03 笔记 §C "AI 撤掉后表现下降"是同向放大；
- 但 03 笔记 §D（已被 v4 推翻）曾建议"AI 是 Socratic 提问者 + 模式识别建议者"——本调研提供进一步证据支持 v4-v5 的推翻方向。
- 与 06 笔记 §3 的"engagement-effectiveness paradox" 一致；本调研把它从抽象原则下钻到具体用户群。

**10. 未调研的相邻领域：**

- 数字健康监管（如 FDA 软件器械、欧盟 AI Act 高风险分类）对"AI 前台 vs 非 AI 前台"是否有不同要求 —— 未调研；
- 数据隐私与安全的 No-AI vs AI 比较（markdown + git 的本地化 vs cloud AI 的数据外泄风险）—— 未调研；
- 法律责任分布（AI 给出错误建议导致用户亏损时的责任 vs 静态 checklist 的责任）—— 未调研；
- 这些是 Phase 2 设计层应当并行处理的维度。

---

## 引用文献清单（按出现顺序，等级标注）

**S 级（同行评审 + 大样本 / 强方法学）**：

1. Cuijpers, P. (1997). Bibliotherapy in unipolar depression: A meta-analysis. *Behaviour Research and Therapy*, 25(2), 139-147.
2. Bond, F. W. & Bunting, K. et al. (2012). A randomized trial of ACT bibliotherapy on the mental health of K-12 teachers and staff. *Behaviour Research and Therapy*, 50(11), 671-679. n=236.
3. Krafft, J., Twohig, M.P., Levin, M.E. (2017). Evaluating the effectiveness of ACT for anxiety disorders in a self-help context. n=503.
4. Pots, W.T.M. et al. ACT-based self-help for perceived stress: RCT, n=133, J Contextual Behav Sci 2017.
5. Cederberg, J. et al. ACT bibliotherapy for chronic pain RCT, n=140, d=0.46-0.88.
6. Karyotaki, E. et al. (2017). Internet-based CBT for depression: IPD network meta-analysis. *JAMA Psychiatry*. n=39 RCTs, 9,751 participants.
7. Heber, E. et al. (2022). Efficacy of computer- and/or internet-based CB self-management for depression: systematic review and meta-analysis of RCTs. *BMC Psychiatry*.
8. Haynes, A.B. et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. *NEJM*, 360(5), 491-499.
9. Arriaga, A.F. et al. (2013). Simulation-based trial of surgical-crisis checklists. *NEJM*.
10. Sbarra, D.A. et al. (2013). Expressive writing can impede emotional recovery following marital separation. *Clinical Psychological Science*.
11. Watkins, E. & Teasdale, J.D. (2004). Adaptive and maladaptive self-focus in depression. *J Affective Disorders*.
12. Gollwitzer, P.M. & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis. *Advances in Experimental Social Psychology*, d=0.65.
13. OpenAI × MIT Media Lab (2025). RCT on chatbot psychosocial effect, n=981.
14. Kosmyna, N. et al. (2025). Your Brain on ChatGPT, MIT Media Lab, EEG study n=54.
15. Bastani, H. et al. (2024). Generative AI without guardrails can harm learning. *PNAS*.
16. Pratap, A. et al. (2020). Drop-out rates in mobile health interventions: pooled meta-analysis. *npj Digital Medicine*.
17. Goddard, K. et al. (2012). Automation bias: a systematic review. *JAMIA*.
18. Cresswell, K. et al. (2017). Automation bias in electronic prescribing. *BMC MIDM*.
19. Munson, S.A. et al. (2015). Sociotechnical challenges and progress in using social media for health. *CHI 2015*.
20. Pfeiffer, P.N. et al. (2014). Augmenting depression care with mutual peer support intervention. *Psychiatric Services*.
21. Babcock, P. (2024). Friends with Health Benefits: A Field Experiment. *Management Science*.
22. PEER trial (2025). BMC Psychiatry, n=296.
23. Gualano, M.R. et al. (2017). Long-term effects of bibliotherapy in depression treatment: systematic review. *J Affective Disorders*.
24. Heinrich, M. et al. (2024). Digitized thought records: practitioner-focused review. *Cambridge Cognitive Behaviour Therapist*.
25. Helweg-Jørgensen, S. et al. (2021). Mobile diary app vs paper-based diary cards for BPD: economic evaluation. *JMIR*.
26. Heber et al. as above for guided self-help with minimal support d=0.65.
27. Liu, M. (2025). LLM education effects systematic review (133 studies, arXiv 2509.22725).
28. NEJM AI / Therabot RCT (2024). Generative AI chatbot for mental health, n=210.

**M 级（专业出版 / 大型监管 / 工作论文 / 临床观察）**：

29. Cipriano, M.C., Gruca, T.S., Jiao, J. (2020). Can investing diaries be hazardous to your financial health? *J Prediction Markets*.
30. McKenna et al. (2018/2024). Self-monitoring using digital vs paper DBT diary card. UW research.
31. Honary et al. (2023). Time investment as dropout predictor. *JMIR mHealth*.
32. Linardon, J. (2024). Engagement-effectiveness paradox in digital mental health. *BMC Digital Health*.
33. Mohr, D. et al. (2023). Engagement in digital mental health: dose-response. *Curr Treat Options Psychiatry*.
34. Sohal, M. et al. (2022). Efficacy of journaling: systematic review and meta-analysis. *Family Medicine and Community Health*.
35. Avila-Gutierrez et al. (2023). Bullet Journal for mental health self-care. *InfoDesign*.
36. Bibault, J.-E. et al. (2022). Conversational agent for thought recording: feasibility study. PMC9343632.
37. Sheppard Pratt (2024). ChatOCD: Pitfalls of using AI when you have OCD. Hospital clinical advisory.
38. Levin, M.E. et al. (2026). Transdiagnostic model for AI chatbots perpetuating OCD/anxiety. *npj Digital Medicine*.
39. Irish Journal of Psychological Medicine (2025). Generative AI and reassurance-seeking in OCD.
40. Vox 2024 reporting on ChatGPT-OCD interactions.
41. TreatMyOCD blog (2025). Clinical observations on AI reassurance loops.
42. NEDA Tessa case (2023). NPR / news-medical reporting + Museum of Failure documentation.
43. Padilla Senate Report (2024). AI Chatbot Safety: Replika.
44. Laestadius, L. et al. (2022). Too human and not human enough: Replika emotional dependence harms. *NMS*.
45. Nature Mental Health (2026). Technological folie à deux.
46. Boylan, J. et al. (2023). Self-tracking and perfectionism dimensions. PMC10699291.
47. Iivanainen, R. (2024). Personal quantification bias. Medium synthesis.
48. Modern Stoicism / Macaro, A. (2024). Premeditatio malorum: friend or foe?
49. Atticus Poet, Stoic Handbook (2024-2025). Modern tier-based premeditatio.
50. Frontiers in Psychology (2022). 6-Minutes Journal RCT 4 weeks.
51. Schoo, F. et al. (2022). Gratitude app COVID-19 RCT.
52. Springer J Happiness Studies (2025). Gratitude training RCT, journaling vs menu.
53. EEF (2025). AI tutor meta-analysis 83 studies.
54. Stanford SCALE (2024-2025). AI feedback comparison.
55. WHO Surgical Safety Checklist (2010). Implementation guidance.
56. Cuijpers, P. et al. (2021). IPD meta-analysis on iCBT subgroups. *JAMA Psychiatry*.
57. Palacios, J. et al. (2022). IAPT step-care comparison, BJP, n=21,215.
58. CAT-SH IAPT pilot (Marsh et al. 2017).
59. LIGHTMind RCT (2022). MBCT vs CBT bibliotherapy. JAMA Psychiatry.
60. Chinese PLA expressive writing study (2024). Repetitive negative thinking in new recruits.
61. Mueller, P.A. & Oppenheimer, D.M. (2014). The Pen Is Mightier Than the Keyboard. *Psychological Science*.
62. Umejima, K. et al. (2021). Paper Notebooks vs Mobile Devices: Brain Activation Differences during Memory Retrieval. *Frontiers in Behavioral Neuroscience*.
63. Bullet Journal Flexible Mindful Self-Tracking (UCL Discovery 2017).
64. Voluntary Self-Exclusion long-term effects (2023). *J Gambling Studies*.

**W 级（行业 / 营销 / 二手）**：

65. Mark Douglas. *Trading in the Zone*; *The Disciplined Trader* (1990 / 2000).
66. Daily Stoic / Ryan Holiday (2016+). 商业产品 + 用户社区.
67. Cohorty 2024, GoalFlow 2024 (accountability success rate stats).
68. Various 5-Minute Journal / Bullet Journal 用户社区报告.
69. Federico Ferrarese 2026 clinical practice blog "When AI Becomes a Compulsion".

**U 级（基于已知文献的逻辑推演 / 本笔记原创校准）**：

70. 本调研第七节"用户分群建议"中的 A/B/C/D 阈值与切换条件——基于以上证据 + v5 §三.11 框架的推演，未经 RCT 验证；
71. "3 月观察期"作为 No-AI 默认时长——借用 DSM-5 problem gambling 评估窗口 + 习惯形成曲线，未经验证；
72. "monthly 1 hour peer review"作为最小人工接触底线——基于 BMC Psychiatry 2022 d=0.65（≤10 min/wk）的等效推算；
73. 第七节"双轨系统"建议——基于"风险不对称 + 用户异质性"的逻辑推演。

---

## 附录 A：与 v5 foundation 的 traceability

| v5 foundation 章节 / 段落 | 本调研对应支持 / 补强 / 反驳 |
|---|---|
| §三.2 反馈/规则验证组件不预设是 AI | **强支持**：第二、三、六节 RCT 证据基础 |
| §三.2 wise feedback / 重大回撤例外 | 间接支持：低强度人工 review + 静态规则在巨亏期更可靠 |
| §三.3 binding pre-commitment | **强支持**：手术 / aviation checklist S 级证据；静态规则就是最简实现 |
| §三.6 退出协议 4 类分叉 | 间接支持：No-AI 模式让"心理安全触发"更易识别（无 AI 干扰判断） |
| §三.10 产品过滤器红/黄/绿 | **建议**：把"AI 前台"明确归入"黄灯" |
| §三.11 临床安全约束 | **关键补强**：第四节为 PGSI / PHQ-4 / 反刍 / 强迫筛查后的 No-AI 路径提供 5 类反向证据 |
| §三.13 "干脆不用 AI（用规则校验 + 模板）" | **从合法选项升级为对部分用户的硬要求** |
| §四.2 隐含假设盲区 | 本调研补充的盲区：低风险用户的 No-AI vs AI 长期对比真空白 |
| 调研 1 反向证据（Sbarra 2013 / Watkins-Teasdale 2004） | 本调研第四节 §4.2 进一步落地到 AI 前台场景 |
| 调研 3 §C / Bastani PNAS / Kosmyna MIT | 本调研第四节 §4.4 延伸到非教育的临床敏感人群 |
| 调研 5 quit gracefully | 本调研第七节 §7.3 回退机制兼容 |
| 调研 6 critical engagement threshold | 本调研第六节 §6.1 提供 ≤10 min/wk 的具体下限 |

---

## 附录 B：本调研的 5 条核心发现（汇总，给摘要外延伸阅读用）

1. **OCD / 反刍 / 高焦虑 / 完美主义 / 抑郁严重用户对 AI 前台有 5 类已识别反向机制**【M-S 级】。这与 σ 系统目标人群（交易亏损 + 自责 + 反刍）显著重叠；对这些用户群"无 AI 前台"是临床证据要求而非偏好。

2. **ACT 自助手册 + 完全无治疗师接触有 S 级 RCT 证据基础**（Krafft 2017 n=503; Bond 2012 n=236; Cederberg 2016 n=140 等）；bibliotherapy 在长期 follow-up 仍显著有效（Gualano 2017）。**纯静态、纯文字方案不是 Phase 2 的"退而求其次"，是有 S 级证据基础的合法路径**。

3. **每周 ≤10 分钟人工接触能产生 d=0.65 抑郁效应**（BMC Psychiatry 2022 元分析 19 RCT）；guided self-help vs face-to-face CBT 在多种 outcome 上**统计上不可区分**（Karyotaki 2017 IPD meta）。**月度 1 小时 peer / coach review 在 evidence stack 上完全可以替代 AI 前台作为反馈基础设施**【S 级】。

4. **AI 前台带来 4 类已识别系统性风险**（认知卸载、自动化偏误、谄媚回路、临床敏感人群反向危害），**纯静态方案天然不存在前 3 类**【S 级，03 笔记已部分覆盖；本调研补充第 4 类 NEDA Tessa / Replika / Padilla 报告等事件级证据】。

5. **手术 / aviation checklist 是"静态规则跑赢人脑直觉" 的 S 级证据范本**（NEJM 2009 死亡率 −40%）；σ 系统的决策链 / 风控 / 退出协议在结构上同构，**享有同源证据迁移**。这与 v5 §三.3 binding pre-commitment 完全兼容，且不需要任何 AI 介入即可实现。

---

> **元规则诚实标记总结**：
>
> - 本笔记所有 S 级引用已尽量给出作者 + 年份 + 期刊 + 核心数字；
> - M 级引用给出来源类型 + 不可重复使用"专家认为"模糊措辞；
> - W 级被标注且不被作为关键证据；
> - U 级（第七节具体建议）明确标注"基于以上证据的逻辑推演，未经 RCT 验证"；
> - 不确定处使用"诚实标记"括注，未伪装为确定结论；
> - 文献空白被显式承认（如：交易场景的 No-AI vs AI RCT 完全空白）；
> - 对 v5 既有约束的关系明确，未隐藏冲突，盲区列于第八节。
