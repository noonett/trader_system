# Phase 2 多模型 Review 操作手册

> 这个目录包含 5 份 prompt 模板，专门用于让不同 AI 模型 review **Phase 2 入口形态调研**（`research/entry_form_research_2026.md` + `research/notes/07-12`）。
>
> 与 Phase 1 的 [`review_prompts/`](../review_prompts/) 是**平行**关系：Phase 1 的 prompts 是关于"证据基础（Plan 宪法）"，Phase 2 的 prompts 是关于"入口形态调研（Plan→Design 桥梁）"。
>
> Phase 1 已经验证多模型 review 的实证价值（不同模型的盲区不重叠）。Phase 2 调研由 6 个并行 Claude 子智能体完成，**所有子智能体共享同一模型偏见**——所以 Phase 2 调研更需要外部多模型 review。

---

## 一、Phase 2 的 5 个视角（与 Phase 1 不同）

Phase 1 的 5 个视角是：行为金融学者 / 实战交易者 / HCI 研究者 / 临床心理学家 / 朴素读者。

Phase 2 调研聚焦"入口形态/技术栈"——所以视角侧重**HCI / UX / 行为设计**：

| Prompt | 视角 | 主要审查 |
|---|---|---|
| 01 | HCI / UX 研究者（更深入） | 6 类入口对比的方法学 + 跨域迁移有效性 |
| 02 | 行为改变 / mHealth / 习惯形成专家 | 留存基线、JITAI 应用、engagement-effectiveness paradox |
| 03 | 软件工程 / 工具实现 实战派 | git/markdown/SaaS 介质选型实际可行性 + vendor lock-in |
| 04 | 临床心理学家（高反刍/OCD/抑郁/赌博）| No-AI 选项的临床安全充分性 |
| 05 | 中国 A 股交易者实战 / 中文用户 | 微信生态 / iOS 沙盒 / 同花顺 / 朴素中文用户视角 |

**为什么不重复 Phase 1 的"行为金融学者"和"5+年盈利交易者"视角？**——因为 Phase 2 调研的内容（入口形态、AI 形态、介质、端、上下文切换）是 HCI/UX 主导的，行为金融学者和盈利交易者的核心专长不在这里。

**为什么 Phase 1 没有"中国 A 股 / 中文用户"视角？**——因为 Phase 1 是普适的"证据宪法"。Phase 2 是入口形态选择，**用户实际在中国 A 股 + 期货市场**——文化和工作流的本地适配性必须明确审视。这是 Phase 2 调研明确标注的盲区之一（中文 HCI 文献覆盖不足）。

---

## 二、操作步骤

### 步骤 1：准备文档

需要让 reviewer 看到的文档：
- **主文档**：[`research/entry_form_research_2026.md`](../entry_form_research_2026.md)（汇总）
- **支撑材料**：[`research/notes/07_entry_form_comparison.md`](../notes/07_entry_form_comparison.md) 到 [`12_no_ai_option.md`](../notes/12_no_ai_option.md)（6 份原始调研）
- **Phase 1 上下文**：[`research/foundation_2026.md`](../foundation_2026.md) v5（如需要交叉对照）

**最小输入**：把 `entry_form_research_2026.md` 全文给 reviewer + 让 reviewer 知道有 6 份子调研可深挖。

**完整输入**：把汇总 + 6 份子调研全部给 reviewer（如果模型上下文允许）。

### 步骤 2：选择 5 个不同模型

推荐组合（与 Phase 1 一致）：

| 模型 | 已知特性 |
|---|---|
| Claude (Anthropic) | 长形式、谨慎、强诚实标记倾向 |
| GPT-5 / GPT-4o (OpenAI) | 直接、引用准确性强 |
| Gemini 2.0 (Google) | 文献覆盖偏 Google Scholar 强 |
| DeepSeek V3 / R1 | 中文文献覆盖好、论证密度高 |
| Grok 3 (xAI) | contrarian 倾向，可能挑战默认假设 |

每个模型分配 1-2 个 prompt（避免一个模型同时跑 5 个视角导致角色串味）。

**特别建议**：
- **05 中国 A 股 / 中文用户视角** → 强烈推荐 DeepSeek（中文文献优势）
- **01 HCI / UX 深入视角** → 强烈推荐 Gemini（学术覆盖）
- **04 临床心理学** → 推荐 Claude（hedging 倾向有助于临床安全）

### 步骤 3：复制 prompt + 运行

每份 prompt 文件包含完整 prompt（在三个反引号之间）。**复制 prompt 整段 → 回车 → 粘贴 entry_form_research_2026.md 全文**。如果模型上下文允许，**接着再粘贴 notes/07-12 的关键章节**。

### 步骤 4：保存输出

为每份 review 创建一个文件：

```
research/pr_phase2_review_<role>_<model>.md
```

例如：
- `research/pr_phase2_review_hci_gemini.md`
- `research/pr_phase2_review_clinical_claude.md`
- `research/pr_phase2_review_chinese_deepseek.md`

### 步骤 5：交给主 agent 整合

把全部 review 的文件路径告诉主 agent，由它做 v2 修订（参考 Phase 1 v5 的整合流程）。

---

## 三、每份 prompt 的强制要求

为对抗 sycophancy（model 的"很有意思"敷衍），每份 prompt 都强制要求：

1. **必须给至少 3-5 处不同意见**（否则视为低质量 review）
2. **每条意见必须标证据等级 S/M/W/U**
3. **遇到不熟悉的领域必须明确说"我不熟悉"**而不是编造
4. **必须直接回答某些 yes/no 型尖锐问题**（每份 prompt 末尾的 "Final Verdict"）
5. **必须列出 reviewer 自己的盲区**（即模型可能漏掉的）

---

## 四、Phase 2 review 的特殊关注点

每份 prompt 都包含 5 个共同问题（即"通用尖锐问题"）：

1. **Phase 2 调研的"6 维度对比矩阵"是否有重大方法学瑕疵？**
2. **"入口按时刻分层组合"（盘前/盘中/盘后/异步）的合成结论是否过度自信？**
3. **No-AI 必须作为高风险用户默认路径的论证是否足够？**
4. **本调研的 6 份子笔记由同一模型生成——是否产生了系统性偏见？**
5. **针对中国 A 股 + 期货用户群的本地化盲区是什么？**

加上每个角色特定的 5-10 个问题。

---

## 五、与 Phase 1 review 的方法学差异

| 维度 | Phase 1 review（review_prompts/） | Phase 2 review（本目录） |
|---|---|---|
| Review 对象 | foundation_2026.md（Plan 宪法） | entry_form_research_2026.md + notes/07-12 |
| 视角 | 学者/盈利交易者/HCI/临床/朴素读者 | HCI（深入）/行为改变/工具实战/临床/中国 A 股 |
| 调研产出深度 | Phase 1 6 份调研由同一 Claude 跑 | Phase 2 6 份调研由 6 个并行 Claude 子智能体跑（仍同模型） |
| 主要风险 | 跨领域证据缝合脆弱性 | HCI 跨域迁移 + 中文/A 股本地化盲区 |
| 已识别新增 | （无） | 本调研明确说"调研者偏向"+"中文 HCI 覆盖不足"是盲区 |

---

## 六、何时不做 review？

**不要跑 review** 的情况：
- 你已经准备启动 Phase 2 Design 且对调研结果满意
- 时间紧迫（multi-model review 需要几小时）

**应该跑 review** 的情况（推荐）：
- 你对调研结论中"按时刻分层"或"No-AI 强制"等结构性建议有疑虑
- 你在中国 A 股语境工作（强烈推荐 05 视角）
- 你想验证 Phase 1→Phase 2 的方法学一致性

---

## 七、最重要的元规则

> 元规则在 Phase 2 review 阶段同样适用：
>
> **没有证据就说"我不知道"。** AI reviewer 编造一个"d=0.55 的研究"比 admit "我不熟悉" 更危险。如果你看到 review 里出现奇怪的引用，**反向 fact-check 它**。

诚实标记是双向的——既约束作者，也约束 reviewer。
