# 多模型 review 操作手册

> 这个目录包含 5 份 prompt 模板，用于让不同 AI 模型（Claude / GPT / Gemini / DeepSeek / Grok 等）独立 review `research/foundation_2026.md`。
>
> 目的：通过让不同训练偏见的模型分别批评同一份文档，找出我（作者本人）的盲区——这是诚实标记体系在 review 阶段的应用。

---

## 一、为什么要这么做

详细论证见对话历史。简版：

- 找真实领域专家 review 成本高、回复率低
- 同一个 AI 扮演 5 类专家 = 同模型 5 个角色 = 共享同一套训练偏见，找不到模型本身的盲区
- **不同 AI 模型有不同训练数据 / 不同偏好 / 不同盲区** → 多模型 review = 真正的多元同行评议

---

## 二、操作步骤

### 步骤 1：准备文档

把 [research/foundation_2026.md](../foundation_2026.md) 复制成纯文本，准备好待用。或者直接给链接：

```
https://github.com/noonett/trader_system/blob/cursor/sigma-system-redesign-bc89/research/foundation_2026.md
```

> ⚠️ 部分模型（特别是 web 界面版本）可能拒绝 fetch 外部链接，建议直接粘贴全文。foundation 约 600 行，常见模型上下文都能装下。

### 步骤 2：选择 5 个不同模型

推荐组合（U 级，基于业界已知特性）：

| 模型 | 已知特性 | 访问方式 |
|---|---|---|
| **Claude (Anthropic)** | 长形式、谨慎、强诚实标记倾向 | claude.ai |
| **GPT-5 / GPT-4o (OpenAI)** | 直接、引用准确性强 | chatgpt.com |
| **Gemini 2.0 (Google)** | 文献覆盖偏 Google Scholar 强 | gemini.google.com |
| **DeepSeek V3 / R1** | 中文文献覆盖好、论证密度高 | chat.deepseek.com |
| **Grok 3 (xAI)** | 风格 contrarian、挑战默认 | x.ai/grok |

**至少用 3 个不同模型**。少于 3 个，多元价值大幅下降。

### 步骤 3：每个模型分配 1-2 个角色

5 份模板对应 5 类专家视角。可以**同一模型跑多个角色**（不同 chat session），但**优先让不同模型跑不同角色**——多元价值最大化。

推荐分配（举例）：

| 模型 | 角色 |
|---|---|
| Claude | 行为金融学者（角色 A）|
| GPT | 实战交易者（角色 B）|
| Gemini | HCI / mHealth 研究者（角色 C）|
| DeepSeek | 临床心理学家（角色 D）|
| Grok | 朴素读者（角色 E）|

或者按你直觉调整。

### 步骤 4：每个 chat session 喂 prompt + 文档

把对应的 prompt 模板（如 [01_behavioral_finance_scholar.md](01_behavioral_finance_scholar.md)）复制完整内容到 chat → 然后**回车** → 然后把 foundation_2026.md 全文粘贴进去 → 等模型输出。

### 步骤 5：保存输出

每个模型的输出保存为：

```
research/review_results/01_behavioral_finance_scholar_<model>.md
research/review_results/02_practitioner_trader_<model>.md
...
```

例如：`research/review_results/01_behavioral_finance_scholar_claude.md`

### 步骤 6：把所有 review 结果交给我

我会做：
1. 交叉对比 5 个模型的 5 份 review
2. 提取**多个模型同时指出的盲区**（这些最值得严肃对待）
3. 整理成 `research/review_synthesis.md` 综合报告
4. 决定哪些 review 意见纳入 v5 修订
5. 全程严格诚实标记每条意见的来源（哪个模型、哪个角色）

---

## 三、5 份 prompt 模板

| 文件 | 角色 | 主要审查方向 |
|---|---|---|
| [01_behavioral_finance_scholar.md](01_behavioral_finance_scholar.md) | 行为金融学/实验经济学学者 | 散户行为研究的引用准确性、反向证据遗漏 |
| [02_practitioner_trader.md](02_practitioner_trader.md) | 5+ 年实战盈利交易者 | 学术结论 vs 实战可行性差距 |
| [03_hci_ux_researcher.md](03_hci_ux_researcher.md) | HCI / mHealth / behavior change app 研究者 | 工具留存设计、engagement-effectiveness paradox |
| [04_clinical_psychologist.md](04_clinical_psychologist.md) | 临床心理学家（CBT/ACT 背景） | 反刍风险、情绪调节、self-monitoring 临床应用 |
| [05_naive_reader.md](05_naive_reader.md) | 朴素读者（非交易者、非技术从业者） | "对外行是不是太复杂"、动机和定位是否成立 |

---

## 四、模板的共同结构

每份模板包含：

1. **角色设定**（你是谁、你的专业背景）
2. **评估任务**（请你做什么）
3. **6 个必答挑战问题**（共通的诚实标记问题）
4. **角色专属的 3-5 个深度问题**
5. **输出格式要求**（结构化、明确分级）

每份模板都要求模型：
- 标注每条意见的证据等级（S/M/W/U）
- 指出至少 1 处明确的引用错误或假设漏洞
- 不要客气说"很有意思"——必须给出尖锐挑战
- 如果某领域不熟悉，明确说"不熟悉"

---

## 五、注意事项 / 已知问题

1. **模型可能产生"满意度高但批评弱"的输出**：这是 sycophancy 偏向。模板里强制要求"必须给出至少 3 处不同意"来对抗这一点。
2. **不同模型对中文 vs 英文敏感度不同**：foundation 是中文，部分模型（如 Grok）可能对中文学术引用支持较弱。如果发现某模型输出明显劣化，换一个模型重跑。
3. **付费墙后的论文**：模型不会真的去读论文全文，它依赖训练数据中的知识。如果它说"这篇论文我没读过"，是诚实的，应当接受。
4. **不要喂完整 PR 描述**：只喂 foundation_2026.md 全文 + 对应 prompt。PR 描述会让模型变成"评 PR 是否要 merge"而不是"评内容是否站得住脚"。
5. **每个模型独立 chat**：不要让模型互相看到别人的 review，否则会出现 anchoring 效应（后跑的模型会附和先跑的）。

---

## 六、保密性

如果你介意 foundation 内容被 OpenAI / Google 用于训练：

- ChatGPT 商业版 / API 可以禁用训练
- Claude API 默认不训练
- 个人 Web 版本通常会用于训练（除非你关掉）

但 foundation 里都是公开学术引用 + 设计思考，没有敏感信息。我个人判断公开训练风险低。

---

*完成日期：2026-05-05 | 维护者：claude-opus-4.7 | 用法：跑完后把 review_results/ 全部交给我*
