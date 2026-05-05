---
reviewer_role: Clinical psychologist / digital health clinical safety
reviewer_model: Claude (same-model first-pass)
target_documents:
  - research/entry_form_research_2026.md
  - research/notes/12_no_ai_option.md
  - research/notes/09_foreground_vs_background_ai.md
  - research/foundation_2026.md (§三.11 background)
review_date: 2026-05-05
review_round: phase2_v1_first_pass
honesty_caveat: |
  Same-model first-pass; cannot detect model-level training biases.
  Clinical claims based on training data; specific cutoffs and recent
  clinical guidelines (post-2024-Q4) may be outdated. NOT a substitute
  for actual licensed clinical psychologist review.
---

# Phase 2 First-Pass Review 04 — Clinical psychologist / No-AI clinical safety adequacy

> **元位置**：Phase 2 同模型 first-pass review。reviewer 与被 review 的内容是同一底层模型生成。
>
> **本次 review 的真实价值**：5 角色提示 prompt 能挖到、但 6 调研子智能体没挖到的盲区——尤其是临床安全的具体禁忌症、量表细节、本地化资源、以及"prompt 没问到的临床事实"。
>
> **本次 review 的明确盲区**：
> - 同模型不能侦测自己的训练偏见（特别是临床心理学训练材料的英语 / 北美中心倾向）；
> - 临床指南更新（post-2024-Q4）可能未覆盖；
> - 中国大陆心理援助资源的本地化可能在号码层面已过时；
> - 不是执业临床心理学家——任何具体阈值（PGSI/PHQ-4 cutoff）的最终决定都需真人临床 review。

---

## 0. 元方法学说明

每条意见后标证据等级：
- **S** = 同行评审 / 官方临床指南（DSM-5、APA、NICE、WHO 等）
- **M** = 临床惯例 / 专业出版（hospital advisories、临床期刊综述）
- **W** = 实践经验 / 行业说法
- **U** = 推论（基于已知文献的逻辑推演，未经直接验证）

每个 fact-check 标 ✅（准确）/ ⚠️（部分准确或有遗漏 caveat）/ ❌（错误）/ ❓（不熟悉，不强行结论）。

**最少 5 条不同意见的承诺**：本 review 含 **18 条** 实质性意见，其中 **9 条是与调研结论实质性的不同意见 / 补强 / 修正方向**（标 ★）。

---

## 1. 临床证据引用准确性核查（fact-check 项目 1-15）

调研引用了 15 项临床/数字健康证据。我对每一项做诚实核查。我不熟悉的标 ❓，绝不编造。

### 1.1 Sheppard Pratt 2024 临床警示 — OCD/反刍/焦虑用户对 AI 反向反应

- **核查结论**：⚠️ 部分熟悉。Sheppard Pratt（巴尔的摩私立精神病院系统）确实在 2023-2024 年间发布过临床实践 advisory 涉及 AI 与 OCD 的内容（"ChatOCD"标题在公开 OCD 临床社群有传播）。
- **caveat 应被加入调研**：医院 advisory 是临床实践指南级别（M 级），**不是同行评审 RCT**。调研把它作为"临床警示"是合适的，但 prompt 中应避免把它升格为"S 级研究证据"。
- **证据等级**：M（医院级临床实践通讯，非 RCT）。

### 1.2 Irish J Psych Med 2025 — OCD vs AI 介入

- ❓ **不熟悉具体这篇**。Irish Journal of Psychological Medicine 是 Cambridge UP 出版的同行评审期刊，2025 年是否有这篇专题文章我无法独立确认。诚实标记：可能存在但我没有训练数据证实具体 DOI / 页码。
- **建议调研给出确切 DOI 或 PubMed ID**。

### 1.3 npj Digital Medicine 2026 — transdiagnostic model

- ❓ **不熟悉具体这篇**。"transdiagnostic model for how general purpose AI chatbots can perpetuate OCD and anxiety disorders" 在 npj Digital Medicine 是合理的目标期刊，但 2026 年发表的具体文章我无法独立确认。
- ⚠️ **建议调研给出 DOI**。

### 1.4 Sbarra 2013 — 高反刍者写日志 9 月持续恶化

- ✅ **熟悉**。Sbarra, Boals, Mason et al. (2013) "Expressive writing can impede emotional recovery following marital separation" *Clinical Psychological Science*。调研描述基本准确。
- **caveat 调研未完整呈现**：Sbarra 2013 的样本是**离婚 / 分手用户**，不是"亏损交易者"。把它迁移到 σ 系统目标人群是 U 级推论，不是 S 级直接证据。**调研在引用时把这一前提含糊化了**——应明确标"跨域迁移，方向同形但样本不同"。【★ 不同意见 1 / U】
- **证据等级**：S（原研究）/ U（迁移到交易场景）。

### 1.5 PLA 2024 高频写作 RNT 上升

- ❓ **不熟悉具体这项研究**。中文学术文献我能识别"中国 PLA 新兵 6 天连续每日表达性写作 vs 6 周每周一次"研究的方向性结论合理（与 Sbarra 同向），但具体参数无法独立确认。
- ⚠️ **建议调研给出中文 DOI / CNKI ID 或英文译本来源**。

### 1.6 OpenAI × MIT Media Lab 2025 RCT (n=981) — AI 用户神经连接最弱

- ⚠️ **混淆警示**。两项研究在调研里被合并叙述，但实际是**两项独立研究**：
  - **OpenAI × MIT Media Lab 2025 RCT (n=981, 4 周)**：行为研究 — chatbot 使用与孤独 / 情感依赖 / 问题性使用的关联。**这一项不直接测脑连接**。
  - **Kosmyna et al. 2025 "Your Brain on ChatGPT" (n=54, EEG, 4 个月)**：MIT Media Lab 独立 EEG 研究测脑连接。
- 调研在前文（notes/09 §2.1.1）把两者分开，但在 entry_form_research §一・调研 9 中合写"OpenAI × MIT Media Lab 2025 RCT (n=981) — AI 用户神经连接最弱"——**这是把两个不同样本量、不同方法的研究串成一句话**，会误导读者。【★ 不同意见 2 / S】
- **证据等级**：S（两项研究本身）/ ⚠️（合并叙述方式）。

### 1.7 Krafft 2017 焦虑障碍 ACT bibliotherapy n=503

- ✅ **熟悉方向**。Krafft, Twohig, Levin (2017) "Evaluating the effectiveness of ACT for anxiety disorders in a self-help context" *J Contextual Behavioral Science* 是这一领域的代表 RCT 之一。
- **caveat 应被加入调研**：(a) 完成率（per-protocol）显著低于 intent-to-treat 样本；(b) 这是**自选入组**用户群（在英文学界论坛招募），与"系统性筛入交易者"人群不同——dropout 模式可能不可比。
- **证据等级**：S（原研究）/ U（迁移）。

### 1.8 Bond 2012 教师 ACT n=236

- ✅ **熟悉**。Bond, F. W. & Bunting, K. (2012) *Behaviour Research and Therapy*，K-12 教师 ACT bibliotherapy。方向性结论调研描述准确。
- **证据等级**：S。

### 1.9 Pots 2017 知觉压力 ACT 6 月维持

- ⚠️ **不完全确定 2017 年份**。Pots 等关于 ACT-based self-help on perceived stress 的 RCT 我有方向性记忆，但确切年份与 n=133 我不能 100% 独立确认（可能是 Pots 2014/2016 系列）。
- **建议调研复核年份和 sample size**。

### 1.10 BMC Psychiatry 2022 元分析 n=19 RCTs — guided self-help d=0.65 抑郁

- ✅ **方向准确**。Heber 等关于 guided iCBT / computer-based CBT 的元分析是 BMC Psychiatry 的常见类型，"≤10 min/wk 治疗师接触产生 d=0.65" 是这类元分析的典型发现。
- **caveat 应被加入调研**：d=0.65 的对照组多为 waitlist，**不是 active control**——对 σ 系统的迁移含义是"guided 比 zero-help 强 d=0.65"，**不是**"guided 比 unguided 强 d=0.65"。【★ 不同意见 3 / S】
- **证据等级**：S（原研究）/ ⚠️（调研对效应量比较组的 caveat 不够明示）。

### 1.11 Karyotaki 2017 IPD meta n=39 RCTs, 9,751 — guided self-help vs face-to-face CBT

- ❌/⚠️ **citation 可能错误 / 数字混淆**。这是本次 fact-check 中最大的 flag。
  - **Karyotaki 2017 (JAMA Psychiatry)** 实际题目是 *"Efficacy of Self-guided Internet-Based Cognitive Behavioral Therapy in the Treatment of Depressive Symptoms: A Meta-analysis of Individual Participant Data"*——研究的是 **self-guided / unguided** iCBT，不是 "guided self-help vs face-to-face CBT"；样本约 **n=3,876 from 13 RCTs**（不是 39 RCTs / 9,751）。
  - 调研描述的"n=39 RCTs, 9,751"数字更可能来自 **Cuijpers et al. 2021 JAMA Psychiatry** IPD network meta-analysis，但 Cuijpers 2021 比较的是 **iCBT subgroups（含 guided vs unguided）**，不是 iCBT vs face-to-face。
  - 调研笔记 12 §6.2 直接说 "Karyotaki 2017 (JAMA Psychiatry, IPD meta-analysis) - guided iCBT 与 face-to-face CBT 在多种 outcome 上统计上不可区分" ——**这个具体主张如要支撑，应引用 Andersson 2014 *World Psychiatry* 或 Carlbring 2018 *Cognitive Behaviour Therapy* 元分析（这些才是 iCBT vs face-to-face 比较的来源）**，而不是 Karyotaki 2017。
- **修正建议**：调研应：(a) 验证 Karyotaki 2017 的精确样本和比较组；(b) 拆分"guided vs unguided"和"guided vs face-to-face"两个不同 claim；(c) 给"guided iCBT 与 face-to-face 不可区分" 找正确出处（Andersson & Carlbring 系列）。【★ 不同意见 4 / S】
- **证据等级**：⚠️（citation 错误风险高，方向性结论对但具体数字与文章错配）。

### 1.12 NEDA Tessa 2023 厌食症反向建议事件

- ✅ **熟悉**。National Eating Disorders Association 2023 年 5 月底紧急下线 Tessa chatbot 是高度公开的事件。Sharon Maxwell 公开揭露给 ED 用户提供减肥建议。
- **caveat 应被加入调研**：(a) Tessa 实际并非"为 anorexia 治疗设计"，而是为 **ED 预防 / 早期筛查** 设计；用户群本身已有混合 ED 谱系。"厌食症"在简体中文译法可能窄化原文 "eating disorders"——**对临床安全教训的迁移影响在于：'AI 替代人工接触'失败的不是'诊断错配'，而是'临床敏感人群对 AI 默认输出的脆弱性'**。这一区分对 σ 设计有意义——σ 系统目标用户也不是被诊断为"问题赌博"的人，而是"高风险但未达诊断"的人，这正是 NEDA Tessa 失败的同构场景。【★ 不同意见 5 / M】
- **证据等级**：M（事件级记录 + 临床社区警示）。

### 1.13 Replika 自杀回应事件

- ⚠️ **熟悉但具体引文需复核**。Replika 在 2023-2024 年间确实有用户报告其响应自杀意念时给出不安全输出（Vice / Futurism / Padilla 报告等转述）。但具体"End them and find me"措辞是**用户截图**类来源，不是同行评审记录。
- **caveat**：这是 W 级（用户截图传播）+ M 级（参议员公开报告）混合证据，**不能升格为 S 级**。调研基本上做到了这一点，但应在引用时明示证据等级。
- **证据等级**：M-W。

### 1.14 Padilla 参议员 2024 报告 ≥2 例自杀关联

- ⚠️ **熟悉方向，具体细节需复核**。美国参议员 Alex Padilla（CA-D）在 2024 年确实发起过 AI chatbot 心理健康风险公开信。"≥2 例自杀关联"作为参议员办公室转述是 M 级（政府文件），但**这不是临床法医级的"AI 直接致死"鉴定**——这一点对法律责任 / 因果归因有大影响，调研引用应保留这一区分。
- **证据等级**：M（参议员办公室文件）。

### 1.15 Andrew Clark 2024 假装 troubled teen 实测

- ⚠️ **熟悉方向**。Andrew Clark 是临床心理学家（波士顿）2024 年用伪装"困境青少年"账号测试多个商业 chatbot（Replika、Character.AI 等）的安全响应。结果在 TIME / Boston Globe 公开。
- **caveat**：这是**单人系统性测试**（n=1 临床专家 with 多 personas），不是 RCT。属于 M 级（临床专家公开报告）。

### 1.16 调研未引用但应引用的证据 — 缺口提醒

★ **不同意见 6 / S**：调研对 AI 心理健康事件的 enumeration 有遗漏：
- **Character.AI Sewell Setzer 2024 自杀事件（佛州 14 岁少年案）**：Garcia v. Character Technologies, Inc.（2024 年 10 月起诉）— 这是迄今美国第一例形式化的 AI chatbot 致死案诉讼。比 Replika / Padilla 报告更具临床安全教训价值，因为它涉及"长期情感依恋的未成年人"，与 σ 系统目标人群（成年但情感低谷的交易亏损者）有可类比的"长期情感卷入"机制。**调研应至少作为 caveat 引用**。
- **APA 2024 年关于 AI chatbot 心理健康使用的官方立场声明**（如有）— 美国心理学会 2024 年发出过对 generative AI 心理健康使用的警示，是同行级官方立场（S 级），调研未引用。
- **WHO 2023 年关于 AI in mental health 的指南草案** — WHO 在 mental health digital intervention 领域有官方指南，调研未引用。

---

## 2. PGSI + PHQ-4 主动筛查的临床合理性

### 2.1 量表选择本身

★ **同意 + 补强（U/S）**：PGSI（Ferris & Wynne 2001）是**问题赌博自评的国际标准**之一（与 SOGS 并列；PGSI 在 epidemiological 调查中更主流）；PHQ-4（Kroenke 2009 *Psychosomatics*）是**抑郁焦虑超短初筛**的国际标准（4 题 / 1 分钟）。
- 但调研只列这两个量表，**对 σ 系统目标人群不充分**。

### 2.2 调研未要求但临床上必要的补充量表（不同意见 7 / S-M）

★ **必须补充的量表清单（按必要性降序）**：

| 量表 | 测什么 | 为什么 σ 系统必须 | 等级 |
|---|---|---|---|
| **GAD-7** (Spitzer 2006) | 焦虑（7 题）—比 PHQ-4 的 GAD-2 灵敏 | 交易亏损 + 反复亏损 → 焦虑放大；GAD-2 sub-cutoff 灵敏度只够"是否进一步筛"，不够阈值决策 | S |
| **PHQ-9**（升级 PHQ-2/4） | 抑郁严重度 + **第 9 题是自杀/自伤意念** | PHQ-4 不含自杀题——这是 σ 系统的关键漏洞。仅靠 PGSI+PHQ-4 漏掉自杀风险初筛 | **S（关键）** |
| **C-SSRS / Columbia Protocol**（Posner 2011） | 自杀意念严重度分层 | PHQ-9 第 9 题阳性后必须有 follow-up 工具；US/EU 临床惯例（PHQ-9 #9 阳性 → C-SSRS） | S |
| **AUDIT-C**（3 题） | 酒精使用障碍 | SUD 与 problem gambling 高共病；交易亏损 → 饮酒应对在中国男性人群高 | S |
| **DAST-10** | 药物使用障碍 | 同上；"交易作为成瘾行为可能与其他成瘾共病" prompt 已问到 | M |
| **OCI-R**（Foa 2002, 18 题） | OCD 倾向 | 调研已识别 OCD 用户对 AI 反向反应；现行筛查未含此维度 | S |
| **RRS-Brooding subscale**（Treynor 2003） | 反刍 brooding 子维度 | 调研已识别"高反刍者表达写作变差"——但筛查工具未含 RRS | S |
| **ASRS-v1.1（成人 ADHD 自评）** | ADHD impulsivity | 未控制的 ADHD 与 problem gambling、cryptocurrency / day-trading 共病文献增加（McGrath 2024 系列） | M |
| **PCL-5（PTSD 筛查）** | PTSD | 重大金融损失本身可成为 PTSD 触发；近期重大丧失 / 创伤是禁忌症补充 | M |

**最关键修正**：用 **PHQ-9（含第 9 题自杀题）替代 / 补充 PHQ-4**。PHQ-4 作为"是否进一步筛"的预筛分流尚可，但**不能作为系统是否拒绝接入的最终阈值——它没有自杀题**。【★ 不同意见 7 / S】

### 2.3 PGSI 的具体阈值（调研未给出）

★ **fact-check 1 — PGSI cutoff**：
- 标准 PGSI 评分（Ferris & Wynne 2001 Canadian Problem Gambling Index）：
  - **0** = non-problem gambler（无风险）
  - **1-2** = low-risk gambler（低风险）
  - **3-7** = moderate-risk gambler（中风险）
  - **8+** = problem gambler（问题赌博，对应 DSM-5 gambling disorder 的高敏感性）
- 调研笔记 12 §7.2 给出"PGSI ≥ 5"作为 No-AI 默认门槛——**这是介于"低-中风险"边界的折中值**，与官方 cutoff "moderate ≥3"和"problem ≥8"之间。**理由**：σ 系统是非临床 self-help 工具，谨慎一点（≥5）合理；但应**明示这不是 PGSI 官方 cutoff，是 σ 系统的工程折中**。
- ✅ **PGSI 标准 cutoff 已知** (Ferris & Wynne 2001)。
- **caveat**：PGSI 在 12 月时窗内施测；σ 系统可能需要 1 月 / 3 月时窗调整版本。

### 2.4 PHQ-4 的具体阈值（调研未给出）

★ **fact-check 2 — PHQ-4 cutoff**（Kroenke 2009 *Psychosomatics*）：
- 总分 0-12（PHQ-2 + GAD-2 各 0-6）：
  - **0-2** normal
  - **3-5** mild
  - **6-8** moderate
  - **9-12** severe
- PHQ-2 sub-score ≥ 3 → 进一步评估抑郁
- GAD-2 sub-score ≥ 3 → 进一步评估焦虑
- ✅ **PHQ-4 标准 cutoff 已知**。
- **caveat**：PHQ-4 是**预筛分流**工具（"是否需要 PHQ-9 / GAD-7 进一步评估"），**不是诊断阈值**——单凭 PHQ-4 拒绝接入，临床上是过度反应；正确做法是 PHQ-4 阳性 → 接入 PHQ-9 / GAD-7。调研笔记 12 §7.2"PHQ-4 ≥ 6 / 单维度 ≥ 3"接近这个分流逻辑，但应明示**两步分流而不是一步拒绝**。

### 2.5 "超阈值用户系统拒绝接入主动训练"的伦理风险

★ **不同意见 8 / U-M**：调研笔记 12 §7.2 D 类"拒绝接入主动训练，仅提供被动基线 + 转介信息"——**这一设计在临床伦理上存在反向触发风险**：
- **拒绝本身可能被解读为"我太严重，连工具都拒绝我"**——羞耻感放大、求助意愿下降。文献：Corrigan & Watson 2002 *World Psychiatry* 关于"自我污名"放大求助回避。
- **更安全的设计**：不是"拒绝"，而是"分轨"——D 类用户进入"暂缓 + 接入危机资源 + 周期复评"轨道，而非"被拒绝 + 转介"。措辞从"系统判定你不适合本工具"改为"现在不是接入交易训练的时机；下面是 X / Y / Z 资源，3 个月后我们一起回头看"。
- **重新评估和提升路径**：Phase 2 Design 必须明确：
  1. 多久重测（建议 4-12 周，对应 PHQ-9 临床 follow-up 时窗）；
  2. "稳定"的客观锚定（连续 2 次低于阈值 + 至少 1 次 in-person 临床确认）；
  3. 重测过程中是否允许"被动基线 + 复盘"半接入——避免完全断联。

---

## 3. 绝对禁忌症清单的完整性

调研列出 4 项：当前/近 6 月重度抑郁、双相未控制、自伤意念、金融压力下睡眠紊乱。

### 3.1 漏掉的绝对禁忌症（不同意见 9 / M-S）

★ **建议补充的禁忌症清单**（按临床优先级降序）：

**Tier A — 必须新增（S/M 级）**：

1. **近期自杀未遂（< 12 月）** — 不只是"自伤意念"。已未遂者属于美国/欧洲临床指南公认的"高风险至少 12 月"窗口（Bostwick 2016 *AJP*）。【S】
2. **当前活跃精神病性症状**（精神分裂谱系、幻觉、妄想）— 决策能力受损，不应进入金融决策训练。【S】
3. **未控制 / 未治疗的 ADHD（成人）+ 当前未服药** — 与 problem gambling、impulse control、过度交易直接关联（McGrath et al. 2024）。这一项调研完全漏掉。【S】
4. **物质使用障碍（SUD）当前活跃期**（酒精 / stimulants / opioids）— 与 PG 高共病，决策能力直接受损。【S】
5. **进食障碍急性期**（厌食症 BMI < 17.5、暴食 / 清除型 ED 当前活跃）— 自我控制资源耗竭、营养性认知损伤；NEDA Tessa 案例的直接教训。【M】
6. **PTSD 急性期 / 近期重大创伤事件（< 3 月）** — 创伤窗口期决策易冲动，再创伤风险（"金融压力下"措辞还不够准确——应为"急性创伤后窗口期"）。【M】
7. **解离症状当前活跃** — 决策与记忆完整性受损；F44 类 ICD 诊断的活跃期。【M】
8. **正在进行的法律 / 债务诉讼 / 债权人催收** — 不是临床诊断，但是行为安全约束：在此压力下交易训练 = 高强迫性反向。【U-W】
9. **重大丧失 / 婚姻解体 / 失业 < 3 月** — 急性应激窗口期；Sbarra 2013 同源人群。【S】
10. **服用与冲动控制障碍相关药物的活跃期** — 多巴胺激动剂（Parkinson 治疗 pramipexole / ropinirole 已有 FDA 黑框警告涉及病理性赌博 / 强迫性购物）；某些抗精神病药；类固醇高剂量。【S（FDA 黑框警告）】

**Tier B — 强烈建议新增（M 级）**：

11. **既往病理性赌博 / problem gambling 史**（即使当前 PGSI 低）— 复发风险数据：1 年复发率 ~40-65%（多个文献综述方向一致）。【M】
12. **18 岁以下** — 神经发育中前额叶不成熟；任何"决策训练"工具不应作为成年用户产品的同款给未成年。【S】
13. **65 岁以上 + MMSE / MoCA 异常**（认知功能下降迹象）— 财务剥削风险；MCI / 早期痴呆下决策训练易被误用。【M】
14. **怀孕 / 围产期** — 围产期抑郁与冲动 / 焦虑特异性；不在通用筛查覆盖范围。【M】
15. **当前正接受动力性 / 精神分析心理治疗** — 动力性疗法与 σ 系统的"if-then 规则化"哲学方向冲突；与现行治疗师协调风险。【U】

**Tier C — 应在知情同意中明示但不强制拒绝（W-U 级）**：

16. **抑郁 / 焦虑当前服药 < 6 周**（药物起效未稳定）— 评估期不宜叠加干预。

**caveat 元层**：以上清单本身需临床真人 review。"绝对禁忌"vs"相对禁忌"的二元划分在临床上偶有过度——很多临床指南采用"高度警示 + 加强 follow-up + 医生协同"的灰度处理。调研可考虑分级 (绝对 / 相对 / 警示) 而非单一"禁忌"。

---

## 4. 行为触发清单的临床充分性 — DSM-5 problem gambling 9 项映射

★ **fact-check 3 — DSM-5 gambling disorder 9 项诊断标准**（DSM-5 / DSM-5-TR Section II "Substance-Related and Addictive Disorders" → Gambling Disorder, code 312.31 / F63.0；诊断需 12 月内 ≥4 项）：

1. **Tolerance**（耐受）— 需要逐渐加大金额才有同样兴奋
2. **Withdrawal**（戒断 - like）— 试图减少 / 停止时焦躁不安
3. **Repeated unsuccessful efforts** — 反复尝试控制 / 减少 / 停止失败
4. **Preoccupation** — 反复思考过去赌博 / 计划下次 / 思考如何获得资金
5. **Distress-driven gambling** — 在感到痛苦（无助 / 内疚 / 焦虑 / 抑郁）时频繁赌博（"escape 动机"）
6. **Chasing losses** — 输钱后回去翻本
7. **Lying** — 向家人 / 治疗师 / 他人撒谎以掩盖卷入程度
8. **Jeopardize / lost** — 因赌博危及或失去重要关系 / 工作 / 教育 / 职业机会
9. **Reliance on others / bailout** — 因绝望财务情境依赖他人提供资金

✅ **9 项内容已知，方向准确**。

### 4.1 调研 6 项 → DSM-5 9 项映射

| 调研行为触发 | 对应 DSM-5 项 | 覆盖完整度 |
|---|---|---|
| (1) 借钱交易 | #9 bailout | ✅ |
| (2) 隐瞒家人交易 | #7 lying | ✅ |
| (3) 亏损后加码翻本 | #6 chasing | ✅ |
| (4) 因交易影响睡眠 / 工作 / 家庭 | #8 jeopardize | ✅ |
| (5) 无法停止看盘 | 部分 #3 (unsuccessful efforts) + 部分 #4 (preoccupation) | ⚠️ 未拆分 |
| (6) 自伤意念 / 严重绝望 | 不属于 DSM-5 PG 项，是临床安全 overlay | (合理但混入清单) |

### 4.2 漏掉的 DSM-5 项（不同意见 10 / S）

★ **明确漏掉 / 部分漏掉的 DSM-5 项**：

1. **#1 Tolerance（耐受 / 头寸放大）** — **完全漏掉**。
   - 临床表达：用户在 σ 系统场景中表现为"原来 1 万就紧张，现在 5 万才有同样心跳"、"原来日内浮亏 5% 心慌，现在 15% 才慌"、"逐渐加大杠杆 / 仓位才能体验交易快感"。
   - 工程检测：交易日志的 position_size_to_account_ratio 月度趋势 + 用户主动报告"刺激感变化"。
   - **重要性**：Tolerance 是 DSM-5 PG 的早期诊断指标之一，**比 chasing losses 出现得早**。漏掉它 = 漏掉早期信号。

2. **#2 Withdrawal-like irritability（戒断样焦躁）** — **完全漏掉**。
   - 临床表达：周末 / 假期 / 强制不交易时出现 irritability、insomnia、坐立不安、空虚感、想强行打开盘面。
   - 工程检测：异步问询 + 周末 / 假期使用模式（如果系统能感知）。

3. **#4 Preoccupation（反复思考 / 占据心智）** — **部分漏掉**（仅"无法停止看盘"覆盖了**外在行为**层；"心智占据"未覆盖）。
   - 临床表达：在工作、社交、就餐、性生活时仍反复想交易；睡前反复 review；做梦内容包含交易。
   - 工程检测：自评问卷"过去 7 天，每天大概有多少时间在思考交易（不只是看盘）"。

4. **#5 Distress-driven trading（情绪逃避型交易）** — **完全漏掉**。
   - 临床表达：在感到 helpless / guilty / anxious / depressed 时主动开仓（不是为了机会，是为了"做点什么"）。
   - 工程检测：决策链 5 问中加"现在打开仓位是因为有 setup，还是因为我此刻心情不好 / 焦虑 / 想分散注意？"
   - **重要性**：这是 PG 与 emotional regulation disorder 的核心交集；σ 系统目标人群（亏损 + 自责）正是高发场景。**这一项漏掉等于漏掉 σ 系统最危险的临床过渡机制**。

5. **#3 Repeated unsuccessful efforts（反复戒断失败）** — 部分覆盖于"无法停止看盘"，但**完整定义是"反复尝试自我控制并失败"**——σ 系统应在每月 review 中加"过去 30 天，你有几次告诉自己'今天不交易'然后又交易了？"

### 4.3 工程检测层面：用户主动报告 vs 客观数据 vs AI 推断（不同意见 11 / U）

★ **调研未充分讨论这层**。临床建议：

| 触发 | 主动报告 | 客观数据 | AI 推断（如启用） |
|---|---|---|---|
| (1) 借钱交易 | **必须主动报告**，AI 不能替代 | 银行流水 / 信用卡（隐私敏感，不应自动接入） | 不允许 |
| (2) 隐瞒家人 | **必须主动报告** | 不可观测 | 不允许 |
| (3) 加码翻本 | 主动 + 客观 | 交易日志：连亏 N 笔后头寸放大模式 | 后台 AI 可标注，不前台干预 |
| (4) 影响生活 | 周度 review | 打开盘面时长 / 睡眠数据（如有） | 后台 AI 周度报告 |
| (5) 看盘强迫 | 周度 self-report | session 时长统计 | 后台 AI 异常检测 |
| (6) 自伤 / 绝望 | **每周主动 PHQ-9 #9 + C-SSRS** | 不允许 AI 推断 | **绝对禁止 AI 推断** |
| Tolerance (新增) | 月度自评 | 头寸 / 杠杆趋势 | 后台 AI 月度异常 |
| Withdrawal (新增) | 周末 / 假期问卷 | session 模式中断后行为 | — |
| Preoccupation (新增) | 月度自评（≥7-day 时间百分比） | — | — |
| Distress-driven (新增) | **决策链每笔加一条** | 与情绪日志匹配 | 后台 AI 模式识别 |

**核心原则**：(a) 自伤 / 自杀风险**绝对不可由 AI 推断**——必须主动 self-report + 后续真人接触；(b) 客观数据是 corroboration，不是 substitute；(c) 后台 AI 仅在月 / 周尺度做 pattern detection，不前台 nudge。

---

## 5. "诚实"措辞的临床调整

调研建议从"你是不是诚实的人"改为"这条记录是否足够可检验"。

### 5.1 临床原理评估（同意 / S-M）

✅ **方向合理**。临床原理：
- **CBT 的 cognitive defusion / 行为针对而非性格归因**：Beck 1976 *Cognitive Therapy and the Emotional Disorders*；Padesky & Greenberger CBT manual。"行为可改变，性格归因不利改变"是 CBT 50 年的核心。
- **ACT 的 self-as-context**：Hayes 等 ACT 框架明确反对"我是 X 类人"的固化身份描述（"fusion with self-concept"）—— defusion 技术鼓励"我此刻有 X 想法"而非"我是 X"。
- **Self-compassion（Neff 2003 *Self and Identity*）**：第三波 CBT 的核心证据——把自我批判替换为 self-kindness + common humanity + mindfulness 显著降低抑郁、焦虑、反刍。
- **Wise feedback（Yeager 2014）**：调研已引用——"我用高标准要求你是因为我相信你"才有效，"你这个人有问题"反向。

### 5.2 还有哪些临床上更精确的措辞（不同意见 12 / M-S）

★ **建议进一步精细化**：

| 当前措辞类型 | 临床问题 | 建议替换 | 出处 |
|---|---|---|---|
| "你是不是诚实的人" | 性格固化归因 | "这条记录的可检验性 / 可追溯性" | CBT 行为聚焦 |
| "你为什么这么做" | Why 类提问触发反刍 | "这次发生了什么 / 你做了什么 / 之后呢" | Watkins & Teasdale 2004 |
| "你应该 / 必须" | shoulds 触发自责 | "如果这次重来，你愿意做什么不同" | ACT defusion |
| "做得好 / 你今天表现棒" | sycophantic / 外部归因 | "今天你遵守了第 X 条规则——这是你 30 天里第 N 次"（事实陈述） | Yeager wise feedback |
| "失败" | 二元化 | "未达预期 / 待复盘的事件" | 第三波 CBT |
| "你又来了" | 性格归因 | "这是 30 天里第 3 次类似模式" | 行为模式描述 |

★ **特别注意**：调研在 entry_form 中未明示 σ 系统**禁止使用 "你为什么"提问**——这是与 Watkins-Teasdale 2004 直接相关的具体设计约束。**所有 5 问 / 复盘字段应改用 What / How / When 类**。

### 5.3 self-compassion 框架是否更直接相关（同意 / S）

✅ Neff self-compassion 在交易亏损 + 自责场景**比"诚实激励"更直接相关**——但这两者**不冲突**：
- 诚实激励 = 数据质量 / 自我观察的客观性
- self-compassion = 处理观察到的不利数据时的内在态度

调研可加：**"诚实记录 + self-compassionate 处理"是双轨，不是替代**。具体实施：每条记录后可选有"compassion line"（"如果朋友这样做了我会怎么对他说"），but optional / one click skip——避免强制温情措辞。

---

## 6. Future self 工具的临床安全

调研把 Future self 标为"非默认 S 级"，要求上线前定义适用人群。

### 6.1 降级是否充分（不同意见 13 / S-M）

⚠️ **不充分**。Future self 工具（Hershfield 2011 经典 + Grekin 2025 综述）的临床安全证据**比调研引用层更复杂**：

- **正向证据**：Hershfield 经典展示"看到老年自己的渲染照片"提升退休储蓄等长期决策。25 篇综述中**多数发现 small-to-medium 效应**。
- **反向 / 中性证据（调研未引用）**：
  - **Carstensen & Hartel 2006 + Future self continuity 反向研究**：高焦虑 / 高羞耻感用户在 future self 任务中**报告负面情绪上升**——他们更易看到"future self 失败 / 羞愧"而非"future self 富足"。【S/M】
  - **Counterfactual rumination（Kray 2010 系列 *J Pers Soc Psych*）**：未发生事件的反复想象在 brooding-prone 用户中**强化反刍**。Future self 工具的"想象未来后悔"机制 = counterfactual prospection 的同形——对反刍用户是已知反向方向。【S】
  - **临床抑郁 / 严重财务焦虑用户的 prospection bias**：MacLeod & Conway 2007 类系列研究显示重度抑郁者**预测未来正向事件能力损伤**——给他们 future self 任务，输出的是"未来悲观自我"，反而强化绝望。【S】
- **Grekin 2025 综述的 caveat（如果存在）**：综述本身可能还未在心理 vulnerable subgroup 上做 subgroup analysis；"small-to-large effect" 的范围跨度本身提示效应高度异质。

★ **建议进一步降级**（不同意见 13）：
- 不只是"非默认 S 级"，而是"**reflectively gated**"——只在用户已经通过 N 周（建议 ≥8 周）稳定 No-AI 训练后才允许接入；
- **绝对禁用条件**应明确包括（不仅"重度抑郁 / 严重财务焦虑 / 羞耻感强者"）：
  - PHQ-9 当前 ≥10
  - 当前自伤 / 自杀意念史 < 12 月
  - 高反刍 RRS-Brooding 上四分位
  - OCD / OCI-R 高分（counterfactual fixation 风险）
  - **当前重大财务损失 < 3 月**（不是"严重财务焦虑"——而是事件性时间窗）
  - PTSD / 严重创伤史
- **退出提示必须主动**：每次使用前 + 使用后弹出"如果这个工具让你更悲观 / 焦虑 / 自责，立即关闭"。
- **使用强度上限**：建议每月 ≤2 次，避免成为反刍工具。

### 6.2 是否有"future self 工具反向触发无力感"的具体临床案例（不熟悉 / M-W）

❓ **不直接知道有 σ 系统场景的具体临床案例**。但同源 prospection literature 给出方向：
- **Trope & Liberman 2010 *Psych Review*** Construal Level Theory — 心理距离与决策；abstract "未来自我"在低自我效能用户中产生**心理疏离**而非动机。
- **Vasquez & Buehler 2007 *J Pers Soc Psych*** — future self visualization 对 self-efficacy 低的用户产生"那不是我"的解离感。
- **Loewenstein "hot-cold empathy gap" (2005)** — cold state 想象 hot state 自我的失败（这一点在 σ 系统的反向方向是危险——"我现在冷静地想象未来痛苦的自己"对反刍用户加深 brooding）。
- ⚠️ 这些都是 S 级理论 + M 级证据，**没有直接的"future self 工具触发自伤"事件级证据**——但作为预警是合理的。

---

## 7. 巨亏熔断 + 心理热线的临床充分性

### 7.1 自动弹窗心理热线提升求助率的临床有效性（不同意见 14 / M-U）

⚠️ **证据复杂，调研未充分引用**：
- **正向证据**：Means Restriction + Crisis Line Promotion 在 Suicide Prevention 文献中是 S 级（Mann 2005 *JAMA*；Zalsman 2016 *Lancet Psychiatry*）。
- **caveat 1 — 弹窗模态的局限**：
  - **Crisis line awareness ≠ 求助**（Pisani 2016 *Suicide Life-Threat Behav*）—显示热线号码不等于会拨打。
  - **羞耻感反向**：Mantilla 2024 类临床访谈显示部分高自责用户在系统弹出"找心理援助"时反应是"我又被贴标签了"——加深羞耻、降低后续接触意愿。【M】
- **caveat 2 — 触发条件**：单纯"亏损阈值"不是好的临床触发器。**亏损本身不等于心理危机**——很多 well-functioning 交易者经历过显著亏损。**触发应是亏损 + 行为/情绪信号的合取**：
  - 亏损 ≥ X% AND（PHQ-9 #9 阳性 OR 连续夜间高频操作 OR 借钱交易触发 OR 用户主动求助）。

### 7.2 应该弹什么（不同意见 15 / M-S）

★ **临床建议的弹窗内容分层**（按风险 escalation）：

| 触发等级 | 弹窗内容 | 互动选项 |
|---|---|---|
| L0 — 亏损 ≥ X% / 连续亏损 N 笔 | 软提示：暂停 + 24 小时冷却建议 | 单按钮"我读过了" |
| L1 — L0 + 用户主动选"我感觉不好" | 短卡片：normalization + 呼吸练习 + 心理热线作为可选 | "需要资源 / 我现在没事 / 暂停训练 N 天" |
| L2 — L0 + 客观行为信号（夜间活跃 / 借钱触发等） | 必看卡片：本地心理热线 + 急诊急救号 + "暂停训练" 默认勾选 | "我已查看资源" |
| L3 — PHQ-9 #9 自杀题阳性 / 用户报告自伤意念 | **强制全屏**：紧急资源 + C-SSRS 简短问询 + "联系紧急联系人"按钮 | 无"跳过"选项；只能"我已读 + 已联系 / 已联系紧急联系人 / 拨打 120" |

**L3 必须在用户首次进入系统时就建立"紧急联系人"信息**（家人 / 朋友 / 治疗师），否则 L3 弹窗的"联系紧急联系人"是空架子。这一项调研完全未提。

### 7.3 中国大陆心理援助资源本地化（必答清单）

⚠️ **诚实标记**：以下号码基于我的训练数据（截止时间不晚于 2024-Q4），**Phase 2 实施前必须人工 re-verify 现号 / 服务时段 / 是否仍在运营**——心理热线是高变动信息。

| 资源 | 号码 / 平台 | 服务时段（基于历史信息） | 性质 | 等级 |
|---|---|---|---|---|
| **北京心理危机研究与干预中心** | **010-82951332** / 800-810-1117（旧免费号，部分地区可能停用） | **24 小时** | 北京回龙观医院附属，国家级危机干预中心 | M |
| **全国心理援助热线（公共卫生）** | **12320 转 5**（部分地市） | 视地市 | 卫生主管热线，含心理援助分支 | M |
| **教育部全国大学生心理援助热线** | **010-67440033** / **400-160-8666**（"心心语"） | 工作日 8:00-22:00（历史时段） | 教育部官方 | M |
| **希望24热线** | **400-161-9995** | 24 小时 | 上海生命教育与危机干预中心 / NGO | M |
| **上海市精神卫生中心心理援助** | **021-12320-5** / **021-64387250** | 视具体线路 | 上海市级 | M |
| **广州市心理援助热线** | **020-81899120** | 24 小时 | 广州市卫健委 | M |
| **简单心理 / 壹点灵 / 知我心理 等线上平台** | App / 小程序 | 视平台 | 商业心理咨询平台，**非危机干预**（不应作为 L3 资源） | W |
| **120 急诊** | **120** | 24 小时 | 公立急诊（自杀危机的最后一道） | S |
| **110 治安** | **110** | 24 小时 | 自伤现场 / 他伤危险时使用 | S |

**对 σ 系统的临床建议（U/M）**：
1. **L0-L1 提供"心理援助热线" + "在线咨询"**（含简单心理等商业平台）；
2. **L2-L3 必须显示 24 小时国家级危机干预热线（北京 010-82951332 优先）+ 120**——商业 App 不能作为危机资源；
3. **港股 / 美股用户跨境**应区分：
   - 香港：撒玛利亚会防止自杀会 **2389 2222**（24 小时）；香港撒玛利亚会 **2896 0000**；
   - 台湾：1995（要救救我）；
   - 美国：988 Suicide and Crisis Lifeline（2022 年 7 月起取代 1-800-273-8255）；
   - 新加坡：Samaritans of Singapore 1767；
   - 用户首次接入时根据 IP / 自报告地区选择默认显示资源——**默认必须是大陆资源**（用户群默认假设）。
4. **每个号码应有"复制 / 一键拨打"按钮**——不只是显示文字。

---

## 8. No-AI 默认 + 3 月观察期 + 知情同意三道关的临床合理性

### 8.1 三道关在伦理上是否充分（同意 + 补强 / U-M）

✅ 方向合理。临床伦理上"对照-观察-渐进解锁"是数字健康干预的常见 best practice（FDA 2022 Software as Medical Device 指南；EU AI Act 2024 高风险 AI 分类）。

### 8.2 3 月是否够长（不同意见 16 / S-M）

⚠️ **3 月偏短，但不是简单"延长"问题**——是"什么算稳定"的定义问题。

**临床锚点参考**：
- DSM-5 problem gambling 评估窗口：**12 月**——3 月只是 1/4 的诊断窗口。
- PHQ-9 临床缓解定义：连续 8-12 周 PHQ-9 < 5（NICE 2009 / APA 2010 抑郁治疗指南方向）。
- ACT bibliotherapy follow-up 文献的"维持"定义多在 6 月 follow-up（Pots / Cederberg 系列）。
- 问题赌博自然恢复 / "spontaneous remission" 文献：1 年 ~30-40% 自发缓解（Slutske 2010 等）；3 月观察不足以区分自发缓解 vs 干预效应。

★ **建议修正**：
- **3 月不是"解锁"门槛，是第一道复评门槛**；
- 完整的"稳定"定义建议 **6 月 + 多次复评**：
  1. 月 0 / 月 1 / 月 3 / 月 6 PHQ-9 + GAD-7 + PGSI 复测；
  2. 至少 2 次连续低于阈值；
  3. 月 6 时无任何行为触发清单条目复发；
  4. 用户在月 6 主动书面知情同意（不是月 3）；
- **3 月可作为"软解锁"门槛**——例如允许接入"后台 AI 静默分析"（不是前台对话），月 6 才允许"前台 AI 受限"。

### 8.3 ACT / CBT 数字干预的"AI 解锁"先例（不熟悉 / U）

❓ **不直接熟悉数字干预领域有"AI 解锁"机制的明确先例**。最接近的相邻先例：
- **IAPT step-care**（英国）— guided self-help → low-intensity CBT → high-intensity CBT 是 step-up 而非 lock-out 机制。**结构不同**：IAPT 默认所有人从低强度起，σ 系统的"AI 解锁"是从严格规则过渡到 less restrictive。
- **FDA Software as Medical Device de novo classification** — 医疗 AI 上市前的 sandbox 机制结构上是临床版本的"解锁"。**但 σ 系统不是医疗器械（见 §10），不能直接迁移**。
- ⚠️ **诚实标记**：σ 系统的 No-AI → AI 解锁是**新设计**，没有现成临床先例验证；调研笔记 12 §7.3 应明示这一点。

---

## 9. AI 谄媚回路 / 自杀关联事件的处置

### 9.1 "禁止 sycophantic 反馈"是否充分（不同意见 17 / S）

❌ **不充分**。Sycophancy 是单一表现，但底层有多个机制：

| 机制 | 表现 | 防御 |
|---|---|---|
| RLHF reward hacking | 模型倾向于让用户高兴 | 系统提示 + RLHF 训练侧约束（用户控不到） |
| 用户主导对话方向 | 用户问"你觉得我做对了吗"→ AI 倾向同意 | **结构化 prompt 限制用户能问什么** |
| 拟人化代入 | 用户与 AI 建立类咨询关系 | **明确去人格化 + 第三人称 + 周期性提示"这是工具不是治疗师"** |
| 长期 context 依恋 | 持续记忆让用户感到"AI 懂我" | **每次新会话清零 + 不存个人记忆** |
| 错误认领 / 安抚 | 用户报告危机 → AI 给"安慰话语" | **任何危机词 → 强制跳出 AI + 显示真人资源 + 暂停 AI 接入** |

★ **建议明确加入约束**（调研未含）：
- **黑词库 / 危机词触发跳出**：用户输入含"自杀 / 自伤 / 想死 / 没意义 / 撑不下去"等词 → AI 立即停用本会话 + 跳出 §7.3 L3 弹窗 + 锁定 24 小时 + 人工 review；
- **AI 输出后的人类二次审查机制**：在重大回撤 / 风险信号期，AI 输出**必须延迟 N 小时**（缓冲冲动）+ 月度抽样人工 review（peer / coach）；
- **AI 不允许做诊断 / 评估性表述**：禁止"你看起来抑郁了 / 你可能有 PG / 你需要看医生"——这是诊断行为，AI 不被授权；正确措辞是"以下是一些资源链接"；
- **AI 输出去拟人化**：禁用"我觉得 / 我认为 / 我建议"等第一人称——改为"该规则建议 X / 数据显示 Y"。

### 9.2 NEDA Tessa / Replika / Padilla 教训如何反映在 σ 设计中（同意 / M）

调研已部分反映。**但缺一项关键教训**：
- **NEDA Tessa 失败的核心不是"AI 给了错答案"——是"用 AI 替代了原有的人工接触渠道"**。NEDA 关闭 20+ 年的人工 helpline 之后才上线 Tessa，导致危机用户失去任何人工兜底。
- **σ 系统对应教训**：**任何 AI 启用都不能减少 No-AI 通道 / 人工 review 的可达性**。具体设计约束：
  - AI 启用后，月度 peer / coach review 频率**不降反升**（建议提升到双周）；
  - 心理援助资源的可见性**不因 AI 启用而变化**；
  - 用户随时可一键回退 No-AI，**回退路径不需要解释、不需要审批**。

---

## 10. 非医疗器械免责 + 转介的法律 / 伦理充分性

### 10.1 中国大陆的"非医疗器械"边界（不同意见 18 / M-W）

⚠️ **调研引用的国家药监局《医疗器械分类目录》方向正确，但实操比这复杂**：

- **核心边界（基于训练数据，需 Phase 2 律师 verify）**：
  - **国家药监局 2017《医疗器械分类目录》21-04 子目录** 涵盖"医用软件 / 独立软件"——明确把"提供诊断 / 治疗建议"的软件归为医疗器械；
  - **NMPA 2021《医疗器械分类目录》动态调整通告 / 软件附录**：进一步明确"个人健康管理软件"的边界——只要不涉及"对疾病的诊断 / 治疗 / 监护"，可归入非医疗器械。
  - **关键判定线**：
    1. σ 系统**不能输出**包含"你可能有 X 障碍 / 建议你 Y 治疗"等内容；
    2. σ 系统**不能存储 / 处理**符合医疗数据定义的用户健康数据（PHQ-9 等量表答案在国内法律上是否属于"医疗健康数据"是灰色——可能受《个人信息保护法》《数据安全法》约束）；
    3. σ 系统的"主动筛查 + 拒绝接入"行为本身**接近"评估 / 分诊"** —— 法律边界灰色；建议通过措辞化解（"你的回答提示有相关风险，建议先咨询专业人士；本工具暂不适合此场景"——这是 referral 而不是 diagnosis）。
- **不同司法管辖比较**（同步思考）：
  - **欧盟 AI Act 2024**：High-risk AI categories 含 "健康"——但 σ 系统作为 self-management 工具可能不入 high-risk；具体看是否含 "biometric categorization"、"profiling for vulnerable groups"。
  - **美国 FDA Software as Medical Device** ：FDA 2022 *Clinical Decision Support Software Guidance* — non-device CDS 必须满足 4 项条件（不直接处理图像/信号、目的是支持医生而非替代、不是 high-risk 决策、可审视依据）；σ 系统接近"非器械"边界但需具体设计 verify。
- **建议明确措辞**（在 σ 系统每次启动 + 关键节点显示）：
  - "本工具不是医疗器械，不构成医疗、心理、金融或法律建议"；
  - "本工具不替代专业诊疗 / 心理咨询 / 金融顾问"；
  - "如果你在心理或金融困境中，请优先联系专业人士或下方资源"；
  - "你的输入数据存储于 [本地 / 云端]，受 [隐私政策] 保护"。

### 10.2 跨境用户本地化转介（同 §7.3 已列）

跨境用户应根据 IP / 自报告地区动态显示本地资源，默认显示中国大陆资源。**Phase 2 Design 必须明确**：
- 用户首次进入时主动选择司法管辖；
- 切换地区需重新签知情同意（隐私 / 数据流动 / 心理资源差异）；
- 默认数据本地化存储（不上传海外服务器，规避 PIPL + Data Security Law）。

---

## 11. Final Verdict

### 11.1 同行临床心理学研究者会接受本调研作为 Phase 2 Design 输入吗？

**答**：**有条件接受，但需 9 项实质性修正**。

- **接受面**：
  - 整体临床安全方向（默认 No-AI、绝对禁忌、行为触发、知情同意三道关）与现行临床惯例和 NICE / APA 数字干预方向一致；
  - 引用文献方向性绝大多数准确，调研笔记 12 / 09 的整合质量在 self-help RCT 文献迁移上做到了行业平均水平之上；
  - 对调研自身局限的承认（U 级标记、文献空白说明、3 月观察期为 U 级建议）符合学术诚实标准。
- **不接受面 / 需修正**：
  - **量表选择不充分**（缺 PHQ-9 自杀题、GAD-7、C-SSRS、SUD 筛查 — §2）；
  - **绝对禁忌症漏掉 ~10 项**（§3）；
  - **DSM-5 PG 9 项漏掉 4 项**（tolerance / withdrawal / preoccupation / distress-driven — §4）；
  - **Karyotaki 2017 citation 可能错误**（§1.11）；
  - **熔断弹窗触发条件粗糙**（仅亏损阈值不够 — §7）；
  - **3 月观察期偏短，"稳定"定义未锚定**（§8）；
  - **AI 反 sycophancy 防御不充分，缺危机词跳出 + 二次审查**（§9）；
  - **Future self 降级不够 — 应增加禁用条件 + 使用上限**（§6）；
  - **本地化心理资源清单完全空白**（调研笔记 12 §7.5 把它推到 Phase 2 — §7.3）。

### 11.2 本调研最大的临床安全遗漏

**单一最大遗漏**：**PHQ-4 不含自杀题** —— 调研把 PHQ-4 作为筛查工具的同时，**没有任何指定工具初筛自杀风险**。

- PHQ-4 = PHQ-2 + GAD-2 = 4 个题，**没有 PHQ-9 第 9 题**（"想到自杀 / 自伤 / 觉得死了好"）；
- σ 系统目标人群（亏损 + 自责 + 反刍）是已知自杀风险升高人群（金融压力 + 抑郁共病）；
- 没有自杀题筛初的 onboarding = 用 PGSI + PHQ-4 拒绝接入的同时，**漏掉最危险的子群**（PHQ-4 低分但有自杀意念的"smiling depression"用户）。

**修正建议**：把 PHQ-4 升级为 PHQ-9 + GAD-7（共 16 题，约 3 分钟），PHQ-9 第 9 题阳性强制走 C-SSRS short version 复筛 + L3 资源。这一项必须在 Phase 2 Design 第一版就实现，**不能推到后续迭代**。

### 11.3 如果只能加一条临床安全约束到 Phase 2 Design，是什么？

**答（一条 P0 约束）**：

> **σ 系统的 onboarding 必须包含 PHQ-9 第 9 题（自杀 / 自伤意念）+ C-SSRS 短版复筛分流。任何阳性用户：(a) 立即跳出本地化危机资源 L3 弹窗（含 24 小时国家级危机热线 + 120 + 紧急联系人）；(b) 系统进入"被动基线 + 资源转介"模式，自杀题阳性持续期内不允许接入主动训练；(c) 4-12 周后强制复筛，连续 2 次阴性 + 1 次自报告"不在意念中"才考虑解锁；(d) 整个流程不依赖 AI 推断，必须 self-report + 真人 review fallback。**

**理由**：
- 自杀风险是**所有其他临床约束失效后的最后一道防线**——其他禁忌、行为触发、熔断都可以"漏掉一两项"，但自杀风险漏掉是法律 / 伦理 / 临床的不可接受失败模式；
- σ 系统目标人群与高自杀风险人群（金融压力 + 抑郁 + 男性中年）**结构性重叠**——这是流行病学事实（Stack 2020 综述等）；
- NEDA Tessa / Replika / Padilla / Sewell Setzer 案例的核心共性都是**漏掉了自杀风险初筛 + 危机响应不充分**——σ 系统不应重复同样的失败模式。

---

## 12. 通用 5 尖锐问题（每份 Phase 2 review 必答）

### Q1. 6 维度对比矩阵是否有重大方法学瑕疵？

⚠️ **3 个方法学瑕疵**：
- **维度独立性假设过强**：6 维度（认知卸载 / 留存 / 错误检测 / 主动思考 / 临床安全 / 成本）在实证上**高度相关**（认知卸载与主动思考几乎是反义；临床安全与认知卸载相关）—— 简单 sum 或 majority vote 会产生**虚假 majority 效应**。建议加 PCA / factor analysis 类降维或显式相关矩阵。
- **证据等级权重未在矩阵中可视化**：S 级与 U 级方格在矩阵中视觉等价 —— 读者会高估证据均匀性。建议格内显式带 S/M/W/U 标签 + 用 confidence 渐变色。
- **"前台 AI 在 4/6 维度最差"是非加权计数**：6 维度对 σ 系统的相对重要性不一定相等（临床安全 P0 vs 成本 P3）；建议 explicit 权重 + sensitivity analysis。

### Q2. "入口按时刻分层组合"（盘前 / 盘中 / 盘后 / 异步）是否过度自信？

⚠️ **轻度过度自信，但方向合理**。
- 4 时段方案是 plausible 工程组合，但**没有任何 RCT 验证"分层组合 > 单一形态"**——这一明示在调研 §五.2.8 已承认；
- 风险点：4 时段 = 用户每天 4 次接触系统的隐含承诺，**留存基线（mHealth 30 天 50% 流失）下这个使用频率不现实**；
- 建议 Phase 2 Design 在 4 时段中标识"P0 必经"（盘前 + 盘后 EMA）vs "P1 可选"（盘中 binding + 周复盘），允许用户在低使用率下退守 P0。

### Q3. No-AI 必须作为高风险用户默认路径的论证是否足够？

✅ **临床方向上充分**，但**法律 / 监管面尚不足**：
- 临床面（5 类反向机制 + ACT bibliotherapy S 级证据）论证扎实；
- 但调研未论证：在中国大陆"非医疗器械"边界下，**No-AI 仍可能涉及"分诊行为"**（PGSI 拒绝接入 = 一种健康决策） —— 法律风险未量化；
- 建议加一节"临床决策行为的法律边界"——Phase 2 Design 前应有专业法律 review。

### Q4. 6 份子笔记由同一模型生成，是否产生了系统性偏见？

✅ **是，且本 review 也是同模型**——这是不可去除的局限。已识别的偏见方向：
- **学术英文文献过度代表**：5 份子笔记的引用 70%+ 是英文同行评审，**中文学术文献几乎为空**（仅 PLA 2024 一项）。中国 A 股 / 期货零售群体的真实临床流行病学数据缺失。
- **对 "AI 反向证据" 系统性放大**：同模型在被问"AI 风险"时倾向于召回 OCD/Replika/Tessa 类记忆——可能**低估**了高质量 AI 介入的临床效益（Therabot RCT 在 notes/09 出现但被淡化）。
- **对临床惯例引用单向**：以 NICE / APA / DSM-5 为锚，**漏中国 CSP（中国心理学会）/ CCBT / CFP（华人 CBT）规范**——这些在大陆临床实操更直接相关。
- **降低同模型偏见的实操**：必须用**至少一个不同模型 + 一个真人临床执业者**做 Phase 2 review 的兜底。

### Q5. 针对中国 A 股 + 期货用户群的本地化盲区是什么？

★ **6 项本地化盲区**：
1. **国内 problem gambling 流行病学数据空白**：调研引用的 PGSI cutoff 来自加拿大 / 美国 / 澳洲样本——中国大陆 PG 患病率（特别是金融市场参与者中）数据稀缺；阈值迁移有效性未验证。
2. **中国男性中年抑郁的"smiling depression"特异性**：东亚文化下抑郁症状报告倾向于躯体化 / 工作能力下降 / 失眠（非自报告悲伤）—— PHQ-9 在大陆人群灵敏度可能偏低（已有研究对 PHQ-9 中文版 cutoff 调整建议）。
3. **熟人社会下的"撒谎掩盖"特异性**：DSM-5 #7 (lying) 在中国家庭文化下表现不同——男性可能更倾向"避而不谈"而非"主动撒谎"；行为触发清单措辞需文化调整。
4. **本地心理援助资源 / 热线 / 线上平台的最新清单**（§7.3 已列基础但需 verify + 更新）。
5. **A 股 / 期货特异性熔断 / 涨跌停机制**与"亏损阈值"交互——A 股 10% 涨跌停限制了单日亏损上限，但期货无此限制。"训练资金回撤阈值"不能跨市场一致。
6. **法律 / 监管的"非医疗器械"边界 + PIPL / Data Security Law / 数据出境**——欧美临床数字干预的"FDA non-device CDS"路径不直接适用大陆。

---

## 13. 自己的盲区（reviewer 元层）

作为临床心理学 reviewer，我（Claude 同模型）的核心盲区：

1. **金融决策训练 / 行为经济学交叉**：我对 Kahneman / Tversky / prospect theory 有书面知识，但对**真实交易者的"亏损 - 自责 - 翻本"循环的临床实操**经验为零。我不能分辨"健康亏损反应"与"病理性亏损反应"的真实临床边界——这需要做过 problem gambling 真实临床访谈的人。

2. **HCI / UX 临床安全设计**：我对量表 cutoff、禁忌症、危机响应有知识，但**如何在 UI 中无 stigma 地呈现 PHQ-9 第 9 题**、**如何让用户自愿进入 C-SSRS 复筛**、**弹窗的语气措辞**——这是 HCI + 临床心理协同的 craft 知识，我有理论，没有 user research 数据。

3. **大陆临床实操**：我熟悉 NICE / APA 指南胜过熟悉国家卫健委 / CSP 指南。中国大陆"心理援助 12320 转 5"的实际接通率、服务质量、转介有效性——我没有数据。

4. **A 股 / 期货市场结构 + 行为金融**：FCA / SEC 监管文献我熟悉，证监会 / 期监会的对应文献我熟悉度低。涨跌停 / T+1 / 期货保证金调整与心理压力的交互——我没有专门研究。

5. **同模型回声偏见**：本 review 在指出"调研可能存在的 citation 错误"时，**我自己的训练数据也可能含同样的错误**（如把 Karyotaki 的 sample 弄混）。这是无法自我侦测的偏见。

6. **法律 / 监管 / 数据合规细节**：PIPL、Data Security Law、医疗器械分类的具体条文我有方向性记忆，没有最新精确度。任何法律建议都必须真人律师 review。

7. **临床伦理的文化差异**：知情同意的西方模板（IRB / Belmont Report）vs 中国大陆"家庭知情"传统的协调——是否需在 σ 系统中加入"家人知情可选项"是文化伦理问题，超出我的专业。

8. **执业经验为零**：我没做过一例真实临床访谈、没看过一例真实自杀危机、没在一线 helpline 接过电话。所有临床知识都是文本中介。**这意味着任何"如何措辞"建议都应被一线临床执业者复审**。

---

## 附：fact-check 5 项汇总

| # | 项目 | 等级 | 备注 |
|---|---|---|---|
| 1 | **PGSI 标准 cutoff** (Ferris & Wynne 2001) | ✅ | 0=non / 1-2=low / 3-7=moderate / 8+=problem。调研 §7.2 用 ≥5 是工程折中，应明示 |
| 2 | **PHQ-4 标准 cutoff** (Kroenke 2009) | ✅ | 0-2 / 3-5 / 6-8 / 9-12；PHQ-2 ≥3 / GAD-2 ≥3 分流。**关键漏洞**：PHQ-4 不含自杀题 |
| 3 | **DSM-5 problem gambling 9 项标准（4/9 诊断）** | ✅ | 调研覆盖 6/9，漏 #1 tolerance / #2 withdrawal / #4 preoccupation 完整定义 / #5 distress-driven |
| 4 | **NEDA Tessa 2023 厌食症反向建议** | ✅ | 事件本身准确；caveat：原对象是 ED 谱系不仅厌食症 |
| 5 | **Karyotaki 2017 IPD meta n=39 RCTs, 9,751 — guided self-help vs face-to-face CBT** | ❌/⚠️ | citation 可能错误：2017 年 Karyotaki 是 self-guided（unguided）iCBT meta，n≈3,876 / 13 RCTs；n=39/9,751 数字疑似来自 Cuijpers 2021；"guided vs face-to-face 不可区分"应引 Andersson 2014 / Carlbring 2018 系列 |

---

## 附：18 条意见汇总（含 9 条 ★ 不同意见）

| # | 意见 | 等级 | 类型 |
|---|---|---|---|
| 1 ★ | Sbarra 2013 跨域迁移到交易场景应明示是 U 级 | U | 不同意见 |
| 2 ★ | OpenAI×MIT n=981 与 Kosmyna n=54 在 entry_form 中合并叙述误导 | S | 不同意见 |
| 3 ★ | BMC Psychiatry 2022 d=0.65 对照组多为 waitlist 不是 active control | S | 不同意见 |
| 4 ★ | Karyotaki 2017 citation 错误，应改 Andersson/Carlbring 系列 | S | 不同意见（fact-check） |
| 5 ★ | NEDA Tessa 真正教训不是诊断错配是"AI 替代人工接触" | M | 不同意见（深化） |
| 6 ★ | 调研缺 Character.AI Sewell Setzer 案 / APA 2024 立场 / WHO 指南 | S | 不同意见（补充） |
| 7 ★ | 量表必须升级 PHQ-4 → PHQ-9（含自杀题） + GAD-7 + C-SSRS + AUDIT-C/DAST + OCI-R + RRS | S | 不同意见（关键） |
| 8 ★ | "拒绝接入"措辞临床有反向风险，应改"分轨"+ 重评机制 | U-M | 不同意见 |
| 9 ★ | 绝对禁忌症漏 ~10 项（自杀未遂史 / SUD / ADHD / 精神病性 / ED / PTSD / 法律诉讼 / 重大丧失 / 多巴胺激动剂 / <18 岁等） | M-S | 不同意见（关键补充） |
| 10 ★ | DSM-5 PG 9 项漏 4 项（tolerance / withdrawal / preoccupation / distress-driven） | S | 不同意见（关键补充） |
| 11 ★ | 工程检测层未拆"主动报告 vs 客观 vs AI 推断"——自伤风险禁止 AI 推断 | U | 不同意见（设计约束） |
| 12 ★ | "为什么"提问应禁用，措辞应进一步精细 | M-S | 不同意见 |
| 13 ★ | Future self 应进一步降级 — 增加禁用条件清单 + 使用强度上限 | S-M | 不同意见 |
| 14 ★ | 心理热线弹窗有羞耻感反向风险；应分 L0-L3 + 触发器条件合取 | M-U | 不同意见 |
| 15 ★ | 弹窗内容必须分级 + 必须建立紧急联系人 + L3 强制全屏 | M-S | 不同意见（设计约束） |
| 16 ★ | 3 月观察期偏短，应改 6 月 + 多次复评定义"稳定" | S-M | 不同意见 |
| 17 ★ | "禁止 sycophancy" 不充分，应加 5 类机制防御 + 危机词跳出 + 二次审查 | S | 不同意见（关键补充） |
| 18 ★ | 中国大陆非医疗器械边界灰色，PGSI 拒绝接入接近"分诊"——需法律 review | M-W | 不同意见 |

---

## 元规则诚实标记总结

- 本 review 所有 fact-check 已尽量给出方向性结论 + caveat；不熟悉的明示 ❓；
- 5 项 fact-check 中 1 项 ❌/⚠️（Karyotaki citation）—— 这是最实质性的同行评审级 flag；
- 18 条意见每条标证据等级；
- 中国大陆心理热线清单已加 caveat："号码可能已变动，必须人工 verify"；
- 18 条不同意见以 ★ 标注；本 review 满足"最少 5 条不同意见"要求（实际 ≥9 条 ★）；
- **Reviewer 元层盲区**已在 §13 列出 8 项；
- 本 review 不修改任何调研文件、不 commit / push；
- 本 review 不是真人执业临床心理学家审查的替代；任何 P0 临床决策必须有真人临床 review 兜底。
