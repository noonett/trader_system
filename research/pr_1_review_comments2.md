# PR #1 Review Comments 2 — GPT-5.5

**Reviewer**: GPT-5.5  
**Target PR**: https://github.com/noonett/trader_system/pull/1  
**Target Branch**: `cursor/sigma-system-redesign-bc89`  
**Review Type**: 文档 / 研究 Plan review（非代码变更 review）  
**Intended Use**: 可复制到 GitHub `Files changed` 的行内评论  

---

## 总体判断

这份 PR 的方向是正确的：它把 Phase 1 明确定位为证据基础和约束清单，而不是提前锁定技术方案。尤其是 v4 对 Plan / Design 分层的清理，是必要且有价值的。

**诚实标记：这是我基于 PR 描述、`research/foundation_2026.md`、`research/notes/01_journaling_evidence.md`、`research/notes/03_ai_coaching_evidence.md`、`research/notes/06_tool_design_retention.md` 以及项目元规则的交叉阅读后作出的 review 判断。**

主要风险不在代码实现，而在文档作为后续 Phase 的“宪法”时，仍存在几类问题：

1. 证据等级标注不一致；
2. Plan / Design 分层仍有少量残留混用；
3. synthesis 文档与 notes 之间有版本冲突；
4. 部分强资产配置/系统约束表述超过了所引用证据能直接支持的范围；
5. 少量文本/编码问题会降低文档可信度。

---

## Inline Review Comments

### 1. `research/foundation_2026.md:5`

> 调研由 5 个独立子任务并行完成，每份原始笔记保存在 [research/notes/](notes/)。本文件是它们的整合结论 + 设计含义。

这里写“5 个独立子任务”，但 PR 实际包含 `notes/01` 到 `notes/06` 六份调研，且本文后面也有“调研 6”。建议统一为“6 个”，否则作为 Plan 阶段“宪法”会出现证据追踪错误。

**来源状态**：基于 PR 文件清单与本文内部结构的直接一致性检查。

---

### 2. `research/foundation_2026.md:39`

> 合理置信度：
> - "结构良好的复盘 + 客观证据 + 外部反馈对交易者有用"：70%
> - "把范式商品化为'每天写日志 + AI 看'就一定有效"：40%
> - "无差别推广给所有人"：20%（部分人群明确会变差）

这里的 70% / 40% / 20% “合理置信度”没有说明估算方法。按项目元规则，应标为 U 级并写清楚“这是基于哪些前提的逻辑推演”，否则容易把主观校准包装成准统计结论。

**来源状态**：项目 `CLAUDE.md` 要求“基于逻辑推演但无直接来源的 → 标注诚实标记”；这里的百分比目前没有直接出版来源或计算方法。

---

### 3. `research/foundation_2026.md:156`

> | 应集成 | 被动基线（财富资金 100% 被动） | **S+** | **Stage -2 必备** |

文档第 7 行定义的证据等级是 S / M / W / U，但这里引入了 `S+`。建议要么扩展证据等级定义并说明 `S+` 的判定标准，要么回到 S 级。否则会破坏全篇证据标注的一致性。

**来源状态**：基于本文第 7 行证据等级定义的内部一致性检查。

---

### 4. `research/foundation_2026.md:181`

> | **用户满意度与学习效果负相关** | S | Stanford SCALE 2024-2025; Karpicke & Roediger 2008 Science; arXiv 2604.07469; arXiv 2512.04630 "reflection-satisfaction tradeoff" |

这里把 Stanford SCALE / arXiv preprint 组合标成 S 级，但 `notes/06` 第 560 行自己把 Stanford SCALE 标为 M 级工作论文，且 arXiv preprint 也不应自动等同同行评审。建议统一降级或拆分标注：同行评审为 S，工作论文 / preprint 为 M 或单独 P。

**来源状态**：基于本文第 7 行对 S 级的定义、`notes/06_tool_design_retention.md:560` 对 Stanford SCALE 的 M 级标注，以及出版状态一致性检查。

---

### 5. `research/foundation_2026.md:247`

> | "1 年稳定表现 → 你是好交易者" | 改为"1 年是判断 edge 的统计最小窗口，���承诺改善" |

这里出现编码损坏：`���承诺改善`。建议修复为预期文本，例如“不承诺改善”。这是小问题，但会影响文档可信度。

**来源状态**：基于文件文本的直接检查。

---

### 6. `research/foundation_2026.md:345`

> **与第 2 层方法的关系**：所有 9 个 S 级证据组件都是为第 1 层目标服务的。

这里仍写“所有 9 个 S 级证据组件”，但上文第 299 行已经改为 12 个组件。建议统一为 12，或解释哪些是核心 9、哪些是新增 3。当前会让 Phase 2 不知道应以哪个清单为准。

**来源状态**：基于 `foundation_2026.md:299` 与本行之间的内部一致性检查。

---

### 7. `research/foundation_2026.md:370`

> | 必须是硬约束的环节 | 不可依赖软提示的原因 |

这一节说 Plan 不承诺具体技术实现，但表格里已经出现“开仓必须同时挂止损单才算合法记录”“产品过滤器技术性禁入”“日损锁定”等具体政策 / 执行形态。建议改成“必须具备 binding pre-commitment / enforced friction”这一级约束，把“同时挂止损单、锁屏、禁入”等作为 Phase 2 备选实现。

**诚实标记**：这是基于 PR 自己设定的 Plan / Design 分层目标作出的逻辑推演。直接来源是 `foundation_2026.md:368` 对“具体技术实现由 Phase 2 决定”的声明。

---

### 8. `research/foundation_2026.md:413`

> Stage -2 强制：
> - 长期财富资金 100% 被动（基于 SPIVA）

“长期财富资金 100% 被动 ETF”是很强的资产配置结论。SPIVA 支持“被动基线 / 默认路径更有证据优势”，但不直接推出所有用户长期财富都应 100% ETF，尤其用户市场包括 A 股 / 港股 / 期货，税务、币种、可得产品、现金需求都可能不同。建议改为“以被动基线为默认，并要求主动偏离必须被显式辩护”。

**来源状态**：SPIVA 2024 支持多数主动基金长期跑输指数；“100% ETF 适合所有长期财富资金”是额外的资产配置推论，需标为 U 级或降为 Phase 2 / 财务规划约束。

---

### 9. `research/foundation_2026.md:260`

> | "记录得越细越好" | Frontiers 2023（投入度低则效应消失）；Beighton 2018（仪式化退化） | **限制日志字段在 10 个核心**，超过造成退化 |

这里说“限制日志字段在 10 个核心”，但后文第 453 行又说字段具体数字推到 Phase 2，第 469 行又写“字段砍到 ≤6”。建议清理为 Plan 级约束：“必须有字段上限，并由 Phase 2 通过可用性证据确定具体数字”。否则 v4 的 Plan / Design 分层仍有残留冲突。

**来源状态**：基于 `foundation_2026.md:260`、`:453`、`:469` 的内部一致性检查。

---

### 10. `research/notes/03_ai_coaching_evidence.md:486`

> AI 不是裁判，是 Socratic 提问者 + 行为日志记录者 + 模式识别建议者

这里仍把 AI 定义为“Socratic 提问者 + 行为日志记录者 + 模式识别建议者”，并在第 492-497 行继续保留“入场前 5 个开放问题”。这与 foundation v4 的“不预设 AI 形态”以及 `notes/06` 的“开放问题弱于 if-then”存在冲突。建议在该 note 顶部或本段标注“这是 v4 前的中间建议，最终以 foundation v4 synthesis 为准”。

**来源状态**：基于 `foundation_2026.md:349-362` 与 `notes/06_tool_design_retention.md:221` 的交叉一致性检查。

---

## 多视角总结

### 证据方法学视角

PR 的优势是主动区分 S / M / W / U，并大量暴露反证据。主要问题是少数地方将 preprint / working paper 与同行评审证据合并标成 S，或引入未定义的 S+。

### Plan / Design 分层视角

v4 已明显比 v3 干净，但“100% 被动 ETF”“必须同时挂止损单”“字段 10 / ≤6”等表述仍部分越过 Plan 层，进入 Design 或具体政策层。

### 交易风控视角

新增被动基线、退出协议、产品过滤器、硬约束方向正确。但对“长期财富资金 100% 被动”的表述应更谨慎，避免从“默认基线”滑向“未经个体约束检验的资产配置指令”。

### 用户训练 / 行为设计视角

PR 正确识别了满意度与学习效果可能冲突、游戏化在交易中可能有害、完全私密不等于最诚实。建议 Phase 2 重点解决“诚实激励机制”和“最低有效使用阈值”，而不是只设计表单或 AI prompt。

### 文档治理视角

作为后续 Phase 的“宪法”，foundation 文档需要比普通 research note 更严格：数字、证据等级、组件数量、Plan/Design 边界都应统一，否则后续 Design 会引用到互相冲突的约束。

---

## Suggested Resolution Before Merge

建议 merge 前至少处理：

1. 修正“5 个调研”与“9 / 12 个组件”的版本残留；
2. 修复编码损坏；
3. 统一 S / M / W / U / S+ 证据等级；
4. 把字段数、ETF 100%、止损执行形态等具体方案降回 Plan 级约束；
5. 给 `notes/03` 中与 v4 synthesis 冲突的中间建议加状态说明。

**诚实标记：这是基于文档作为后续 Phase 输入的治理风险推演；不是说这些问题会导致系统方向错误，而是说它们会降低后续 Design 阶段的可执行一致性。**
