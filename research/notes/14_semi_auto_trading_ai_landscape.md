# 半自动交易 AI 助手的产品形态与设计模式调研

> 调研日期：2026-05-07
> 调研方法：Web 检索（arXiv、Springer、Frontiers、GitHub、商业产品文档、媒体评测）+ 项目已有 Phase 1-2 证据整合
> 证据等级：S（同行评审、可复现/方法学透明）/ M（专业出版/可信数据/工作论文/会议论文）/ W（行业博客、营销材料、未独立验证）/ U（基于已知文献的逻辑推演）
> 上下文：用户希望了解"效果比较好的半自动交易 AI 助手是怎么样的"。本笔记从当前市场产品、学术框架、开源实现三个层面梳理设计模式，并与 σ 系统的已有设计做对照。
>
> 与已有笔记的关系：
> - notes/03 已建立 AI 教练的整体证据基础
> - notes/09 已建立前台/后台/无 AI 的三选一对比矩阵
> - notes/07 已建立 6 类入口形态的对比证据
> - **本笔记不重复以上结论**，而是回答：**当前市场上"效果比较好"的半自动交易 AI 助手有哪些设计模式？它们的结构与 σ 系统的设计选择有什么对照关系？**

---

## 摘要

1. **"半自动"在当前市场有三种截然不同的含义**，它们的 AI 介入层次完全不同：
   - **(A) 信号生成 + 人工确认执行**：Holly AI（Trade Ideas）、TrendSpider Sidekick — AI 找机会，人决定是否下单
   - **(B) 策略构建 + 自动执行**：Composer — 人用自然语言/可视化描述策略，AI 翻译为规则后自动执行
   - **(C) 行为监控 + 纪律反馈**：TradeZella Zella AI、Edgewonk Tiltmeter、Plancana — AI 分析交易者自身行为模式和心理状态

   **σ 系统属于第三类（C），但加入了第一类都没有的"binding pre-commitment"强制层。这在当前市场产品中是独特的。**

2. **当前"效果好"的产品共享的设计特征**（跨 A/B/C 三类总结）：
   - **人保留最终决策权**——即使 AI 分析，执行仍由人确认（Holly 的"alerts-only"模式、Composer 的随时暂停）
   - **异步分析优先于实时干预**——Zella AI 的 "always-on" 分析是**盘后**呈现，不在决策瞬间打扰；Edgewonk 的 Tiltmeter 是**回顾工具**
   - **数据驱动的具体化反馈** > 通用建议——"你的伦敦盘反转交易 63% 失败"比"注意风控"有效
   - **低认知负担的持续记录**——自动同步（500+ 券商）或 <30 秒手动录入
   - **可视化纪律与绩效的关联**——Edgewonk 的 Tiltmeter 把纪律叠加在收益曲线上是核心创新

3. **学术前沿的多 Agent 框架**（TradingAgents、CFA Agentic AI）提出了一种**完全不同的范式**：多个 LLM Agent 扮演牛方/熊方分析师 + 风控 + 交易员 + 组合经理的辩论式决策。**这是全自动范式，不是半自动；它解决的是 α 问题（看懂市场），不是 σ 问题（管住自己）。** 对 σ 系统的直接价值有限，但其中"辩论式多视角分析"的结构可以在后台 AI 复盘报告中借鉴。

4. **项目已有调研（notes/03 + notes/09）已经覆盖了最关键的证据**——本笔记的增量贡献在于：把抽象的"前台/后台/无 AI"三选一落到**具体产品的功能设计**上，形成可操作的对照参考。

---

## 一、当前市场的三类半自动交易 AI 助手

### 1.1 A 类：信号生成 + 人工确认执行

> **核心理念**：AI 负责"看市场"，人负责"做决定"

#### Trade Ideas — Holly AI

**架构**【W 级，来源：产品文档 + 媒体评测】：
- **隔夜分析引擎**：每晚处理基本面、技术面、社交数据，在盘前给出次日交易建议
- **实时告警系统**：盘中分析 8,000+ 股票，使用 70+ 种策略方法，仅推送成功率 > 60% 的策略信号
- **策略优化工具**：OddsMaker 回测工具，用于精调策略参数

**半自动工作流**：
1. 盘前：查看 Holly 隔夜筛选结果（~50 条预建策略）
2. 盘中：Holly 实时推送符合条件的标的 + 声音告警
3. 交易者**自主决定**是否执行：查看图表 + 参数 → 手动在券商下单
4. 可选：连接 Brokerage Plus 模块实现半自动执行

**定价**：$127–$254/月

**σ 对照**：Holly 解决的是 α 问题（找交易机会），不是 σ 问题（管住自己）。它没有任何行为监控、纪律检测、偏误识别功能。如果一个交易者因为 FOMO 追高，Holly 不会阻止——它甚至可能因为实时推送**加剧**FOMO。（诚实标记：这是 U 级推论，未见 Holly 的行为效果独立评估）

#### TrendSpider — AI Sidekick

**架构**【W 级，来源：产品文档】：
- **自动技术分析**：自动识别图表形态（头肩、三角、通道等）、支撑阻力、趋势线
- **AI 策略实验室**：无代码训练预测性 ML 模型
- **云端告警 + 无代码 Bot**：自动监控、入场、出场、执行

**半自动工作流**：AI 自动标注 → 人确认 → 设定告警/Bot → 自动或手动执行

**定价**：$59–$99/月

**σ 对照**：同 Holly，纯 α 层工具。但 TrendSpider 的"无代码 Bot"模式与 Composer 接近，走向全自动而非半自动。

---

### 1.2 B 类：策略构建 + 自动执行

> **核心理念**：人用自然语言描述想法，AI 翻译为可执行规则，然后自动运行

#### Composer — No-Code Symphony

**架构**【W 级，来源：产品文档 + Alpaca Markets 博客】：
- **自然语言 → 策略**：用英文描述交易想法，AI 生成完整策略（"Symphony"）
- **可视化编辑器**：手动调整资产、参数、条件逻辑
- **回测验证**：对比历史数据 + 基准（S&P 500）
- **全自动执行**：策略上线后自动交易，支持股票/ETF/期权/加密
- **社区市场**：3,000+ 社区策略，80% 用户投资社区构建的策略

**2025 新功能 "Trade with AI"**【W 级】：
- "Find My First Symphony"：浏览社区策略
- "Help Me Choose"：回答 3 个问题 → AI 推荐 3 个策略（<60 秒）
- "Make My Own Symphony"：AI 从用户行为模式中识别交易模式 → 生成策略

**定价**：$32/月，$50 起投

**σ 对照**：Composer 是"把人的判断规则化后交给机器执行"的范式——它跳过了"管住自己"这个环节，直接消除了人在执行层的角色。这与 σ 系统的哲学根本不同：σ 认为**人必须经历决策过程才能成长**（foundation §三.2 anchoring 防御 + notes/03 Bastani 2024 撤掉后 -17%）。Composer 的问题是：如果市场环境变了、策略失效了，用户**没有独立判断能力来识别这一点**——因为他从未真正做过判断。

**诚实标记**：上述"σ 对照"是 U 级推论。Composer 可能反驳说"规则化本身就是 pre-commitment 的终极形态"——这有一定道理（Fischbacher 2017 的 stop-loss/take-gain 作为 pre-commitment 有 S 级支持）。区别在于 Composer 的规则是"何时买卖"的 α 规则，而 σ 的 pre-commitment 是"何时不能交易"的行为约束。

---

### 1.3 C 类：行为监控 + 纪律反馈 ← σ 系统最接近的类别

> **核心理念**：AI 不告诉你买什么，而是告诉你"你自己在做什么"

#### TradeZella — Zella AI

**架构**【W 级，来源：StockBrokers.com 评测 + 产品文档】：
- **自动日志**：500+ 券商同步，或文件上传/手动录入
- **Zella Insights AI**："Always-on"分析每一笔交易，自动标记行为模式、执行错误、重复性失误——**无需用户主动提问**
- **Zella Score**：综合一致性、最大回撤等因子的整体评分
- **50+ 数据报告**：胜率、盈亏比、策略表现追踪（Playbooks）
- **Trade Replay**：逐笔回放（Premium 才有逐 tick）

**半自动工作流**：
1. 交易时：正常下单（在券商平台）
2. 盘后：交易自动同步到 Zella
3. Zella AI 异步分析 → 标记模式（"你周一的交易胜率只有 32%"、"你在亏损后倾向加大仓位"）
4. 用户**主动查看**报告 → 调整行为

**定价**：$29–$49/月，无免费试用

**σ 对照**：
- **结构上最接近 σ 的后台 AI 异步报告**：Zella AI 的"always-on 分析 + 用户主动查看"与 notes/09 §四.2 推荐的"周/月异步复盘 → 后台 AI 报告"几乎完全吻合
- **缺失的部分**：
  - ❌ **无 binding pre-commitment**：Zella 不阻止你违规交易——它只在事后告诉你违规了
  - ❌ **无盘前 if-then 门禁**：没有决策链、没有实施意图强制
  - ❌ **无风控硬约束**：没有日损锁屏、没有仓位上限强制
  - ❌ **无临床安全筛查**：没有 PHQ-4/PGSI 门禁
- **Zella 的优势 σ 可借鉴的**：
  - ✅ 500+ 券商自动同步 — 消除手动录入的留存障碍
  - ✅ 50+ 数据化报告 — 具体化反馈胜过通用建议（与 Auer & Griffiths 2014 S 级一致）
  - ✅ Playbooks 策略追踪 — 让"哪个策略有效"变成数据而非感觉

**效果证据**：**无任何独立同行评审评估**（notes/03 §Q7.2 已确认）。评分来自 Trustpilot 4.7-4.8 和 TradingJournal.com 内部评测——均为 W 级。

#### Edgewonk — Tiltmeter + 心理标签

**架构**【W 级，来源：产品文档 + Zendesk 帮助中心】：
- **Tiltmeter**：核心创新——可视化交易纪律，绿色（遵守规则）/红色（违规）条带叠加在收益曲线上
  - 设置：用户创建入场/出场/管理评论标签 → 每笔交易评为正面/负面/中性
  - 效果：直观显示"纪律好的时期 = 赚钱时期"vs"纪律差的时期 = 亏钱时期"
- **自定义心理标签**（最多 20 个）：信心、压力、专注、冲动等
- **效率指标**：百分比显示你遵守规则的频率
- **Missed Trades 记录**：分析你犹豫错过的交易 → 识别自信问题
- **结构化复盘 Sessions**：日/周/月复盘卡 + 反思提示 + 教训追踪

**半自动工作流**：
1. 每笔交易后：手动评分（入场/出场/管理质量）+ 标记心理状态
2. 系统自动计算 Tiltmeter + 效率 + 心理关联
3. 定期 Sessions 结构化复盘

**定价**：一次性买断（$169），无订阅

**σ 对照**：
- **Edgewonk 的 Tiltmeter 是当前市场上最接近"纪律 ↔ 绩效可视化关联"的实现**
- **但它完全依赖用户手动评分**——notes/03 §Q2 的 Beighton 2018（反思退化为"表演性合规"S 级）风险在这里完全适用
- σ 系统的 `violations_scan.py` 是**自动化的违规检测**，不依赖用户自我评价——这在理论上比 Edgewonk 更可靠（U 级推论）
- **借鉴价值**：Tiltmeter 的"纪律叠加收益曲线"可视化是一个**极好的 WebUI Phase 3c 仪表盘设计参考**

#### Plancana — 实时 Tilt 检测

**架构**【W 级，来源：产品文档 + Google Play 页面】：
- **AI 情绪模式检测**：分析交易日志识别恐惧、贪婪、报复性交易
- **Confidence Checkpoints**：自动提示，防止过度交易和冲动决策
- **Psychology Rules Engine**：用户设定"交易准则"，AI 强制执行提醒
- **实时 Smart Notifications**：违规时告警 + 交易时段总结
- **情绪标记**：每笔交易记录情绪状态

**定价**：免费基础版 + 付费高级（具体定价未公开）

**σ 对照**：
- Plancana 的"Psychology Rules Engine"是**最接近 σ 的 if-then 门禁**的商业产品设计
- 但 Plancana 是**手机优先**——这与 notes/07 §摘要.6 的 NBER 证据（手机入口诱发更多追涨/碎片化决策，S/M 级）直接冲突
- Plancana 的"实时 Smart Notifications"是**前台 AI 介入**——notes/09 在 4/6 维度上给前台 AI 反向判定
- **诚实标记**：Plancana 12,000+ 用户的说法来自产品页面（W 级），无留存或效果的独立数据

---

## 二、学术前沿：多 Agent LLM 交易框架

### 2.1 TradingAgents（arXiv 2412.20138, 2024）

**架构**【M 级，arXiv preprint + GitHub 开源】：

| 组件 | 角色 | 方法 |
|------|------|------|
| **分析师团队**（4 个并行 Agent） | 基本面分析、情绪分析、新闻分析、技术分析 | 各自调用数据 API → 生成结构化报告 |
| **研究员团队**（辩论式） | 牛方 vs 熊方辩证讨论 | 强制正反两面审视，防止单一方向偏误 |
| **交易员 Agent** | 综合分析 + 研究结论做决策 | 合成多方信息 → 买/卖/持有 |
| **风控团队** | 监控波动率、回撤、流动性 | 建议仓位大小、止损、风险缓解 |
| **组合经理** | 最终审批 + 执行 | 模拟交易所 + 决策日志 |

**关键设计特征**：
- **混合通信协议**：结构化报告（存入全局状态）+ 自然语言辩论 → 防止长对话信息丢失
- **"快思考 vs 深思考"策略**：检索/摘要用快模型（降本），分析/辩论用深模型（保质量）
- **实验结果**：累积收益、Sharpe ratio、最大回撤均显著优于基线

**σ 对照**：
- TradingAgents 是**全自动** α 系统，不含任何"人在回路"设计
- **但其"辩论式多视角"结构对 σ 系统有间接价值**：σ 的后台 AI 周报可以借鉴"牛方/熊方对比分析"来呈现用户的交易记录——例如："**本周你做对的**（牛方视角）… **本周你做错的**（熊方视角）… **风控审计**（违规清单）"
- **诚实标记**：这一借鉴是 U 级推论，"辩论式复盘格式是否优于线性复盘"没有直接证据

### 2.2 CFA Institute — Agentic AI for Finance（2026）

**框架**【M 级，CFA Research Foundation】：

AI Agent 在金融领域的定位是"**bounded autonomy** + human-in-the-loop oversight"：
- AI Agent 作为"**supervised co-pilots, monitoring systems, and constrained execution modules**"嵌入人类决策流程
- 四层架构：数据感知 → 推理引擎 → 策略生成 → 受控执行
- 关键设计参数：自主权深度、模型异质性、执行耦合、基础设施集中度、监管可观察性

**核心判断**（引用原文）：系统性风险取决于"**agent architectures are distributed, coupled, and governed**"的方式，而非模型智能本身。

**σ 对照**：CFA 的"bounded autonomy"框架与 notes/09 §四.2 的结论高度一致——AI 的介入应是受约束的、可观察的、人可随时覆盖的。σ 系统的"前台 AI 仅在用户已独立完成认知工作后启用"是 bounded autonomy 在个人训练场景的实例化。

### 2.3 实际交易者如何使用 LLM（2025-2026 社区观察）

**来源**：Substack（RogueQuant）、Medium、MindStudio 教程【W 级，个人经验分享】

观察到三种使用模式：

| 模式 | 描述 | 复杂度 | 与 σ 的关系 |
|------|------|--------|-----------|
| **Prompt 工程优化策略** | 让 ChatGPT/Claude 互相竞争优化策略参数；"prompt 质量决定 80% 的 edge" | 中 | α 层，与 σ 无关 |
| **24/7 自主 Agent** | Claude Code Routines 每 15-30 分钟循环：获取数据 → 生成信号 → 执行交易 → 记录日志 | 高 | 全自动 α，与 σ 背道而驰 |
| **Multi-Agent 系统** | "CEO" Agent 监控 + 专用策略 Agent（期权、scalping）| 极高 | 纯工程实验，缺乏风控约束 |

**关键观察**：
- **"auto-journaling by agent"** 是一个有意思的交叉点：Agent 自动记录每笔交易的推理过程 → 形成可审计的决策日志。σ 系统可以从中借鉴"AI 生成的交易推理日志"作为后台审计的输入——但前提是**人自己也必须独立写下推理**，否则又回到认知卸载。
- 社区强调"paper trading first"——与 σ 系统"训练资金"概念一致
- **诚实标记**：这些都是个人经验帖，样本量=1，无法评估效果，且存在幸存者偏差

---

## 三、MCP 生态中的金融工具（2025-2026）

**来源**：GitHub awesome-mcp-servers 列表【W 级】

| 工具 | 功能 | 与 σ/α 的关系 |
|------|------|--------------|
| **financekit-mcp** | 17 种金融工具：技术分析（RSI/MACD/布林带/ADX）、风险指标（VaR/Sharpe/Sortino/Beta）、组合分析 | α 层数据工具，可作为 WebUI Agent 的 tool-use 扩展 |
| **SignalFuse MCP** | 加密交易信号融合（情绪 + 宏观体制 + 市场结构）| α 层，加密专用 |
| **Helium MCP** | 实时新闻智能 + 偏差评分 + ML 期权定价 | α 层信息工具 |

**σ 对照**：这些工具全部是 α 层（看懂市场），σ 系统当前不需要。但当 α 引擎建设时，MCP 协议的 tool-use 架构与 WebUI 的 `tools.ts` + `repo.ts` 设计可以无缝集成。

---

## 四、跨产品设计模式提取

综合 A/B/C 三类产品 + 学术框架，提取**效果较好的半自动交易 AI 助手共享的设计模式**：

### 模式 1："异步分析，主动查阅"

**定义**：AI 在后台持续分析，结果在用户主动查看时才呈现；不在交易决策瞬间打扰。

**产品实例**：Zella AI（always-on 但盘后呈现）、Edgewonk（回顾工具）、Holly AI（盘前报告）

**证据支持**：
- notes/09 对比矩阵：后台 AI 在 4/6 维度上至少次优或最优【U 级，基于 S 级子证据的整合】
- JITAI 行为改变 g=0.77（Wang 2023, k=21, N=592）【S 级】——JITAI 是"状态需要时才介入"的范式
- 静态 AI ≥ 对话 AI（Liu 2025 CRC 筛查 RCT）【S 级】

**σ 系统当前实现**：`make weekly-report` / `make monthly-calibration` → 后台 AI 生成异步报告 ✅
**可改进方向**：增加数据化可视报告（参照 Zella 50+ 报告 + Edgewonk Tiltmeter 的纪律-绩效关联可视化）

### 模式 2："具体化数据反馈" > "通用建议"

**定义**：基于用户个人交易数据的具体反馈（"你周一的胜率 32%"、"你在连亏后倾向加大仓位 2.3x"），而非通用风控建议。

**产品实例**：Zella Insights（自动模式标记）、Plancana（"你最近 10 笔亏损中 8 笔发生在'沮丧'情绪下"）、Edgewonk 心理标签关联

**证据支持**：
- Auer & Griffiths 2014（赌博机特异性消息 > 通用消息）【S 级】
- FX Replay 2026 综述：AI 能"cluster similar trades by structure and timing, highlight recurring mistakes"【W 级】
- 但 Steiss 2024 + IJETHE 2026 悖论：**反馈质量高不等于行为改变大**【S 级】

**σ 系统当前实现**：`violations_scan.py` 5 类违规检测 → 生成具体违规清单 ✅；`kpi_alert.py` KPI 告警 ✅
**可改进方向**：
- 增加"行为模式"级别的分析（不只是违规/不违规，还有"你的行为倾向"统计）
- 类似 Zella 的"你在 X 条件下的胜率是 Y%"统计

### 模式 3："纪律可视化"——把遵规与绩效的关联变成图

**定义**：用可视化手段让交易者看到"遵守规则的时期赚钱，违反规则的时期亏钱"。

**产品实例**：Edgewonk Tiltmeter（纪律条带叠加收益曲线）、Plancana（情绪 ↔ 绩效日历热力图）、FX Replay（AI 模式检测 + 回放）

**证据支持**：
- Morewedge 2015 debiasing training：互动 + 个性化反馈 → 偏误降幅 31.94%，2 个月维持【S 级】
- 但这些产品的纪律可视化**本身没有独立效果评估**——没有 RCT 对比"有 Tiltmeter vs 无 Tiltmeter"的交易者绩效差异

**σ 系统当前实现**：WebUI 尚为 chat-only，无仪表盘 ❌
**可改进方向**：Phase 3c 仪表盘可参考 Tiltmeter 设计——violations 时间线叠加收益曲线

### 模式 4："规则引擎 + binding 强制"——不只提醒，要执行

**定义**：用户预设规则（日损上限、仓位上限、产品黑名单），系统**自动执行**而不是建议执行。

**产品实例**：
- Plancana Psychology Rules Engine：用户设定 do/don't → AI 提醒（但只是提醒，不 binding）
- Composer：策略全自动执行（binding 但不含行为约束）
- **注意**：当前市面上**没有产品**做到"行为规则的 binding 执行"——即"你今天亏了 X，系统锁屏不让你继续交易"

**证据支持**：
- Fischbacher 2017：reminders 无效，actual ex-ante commitment 才有效【S 级】
- 在线赌博 RCT N=4,328：prompt-only 不降低净亏损【S 级】
- FCA 2024 N=9,000：降低摩擦 → 交易频率↑ + 风险↑ + 收益恶化【S 级】

**σ 系统当前实现**：`violations_scan.py` + git pre-commit hooks + red-zone schema → binding 层 ✅
**这是 σ 系统相对于所有竞品的独特优势**：市面产品都停留在"提醒"层（soft constraint），σ 系统设计了"执行"层（hard constraint）。

### 模式 5："自动记录 + 低摩擦同步"

**定义**：交易记录自动从券商同步，减少手动录入的留存障碍。

**产品实例**：Zella（500+ 券商）、Plancana（MT4/5、ByBit、Tradelocker）、TradeZella（file upload / manual <30s）

**证据支持**：
- 行业估计交易日志 80% 在 2 周内放弃（W 级，未独立验证）
- mHealth 30 日留存 ~7%（AppsFlyer 2024，M 级）
- 减少录入摩擦在理论上提升留存——但 notes/07 §摘要.5 警示："三次点击规则"无支持（S/M 级），真正重要的是"点击的认知负担和清晰度"

**σ 系统当前实现**：手动 markdown 交易记录模板 ✅，但无自动同步 ❌
**可改进方向**：如果 WebUI 后续接入券商 API 自动同步，将显著降低日常使用摩擦。但需警惕：自动同步可能**降低用户对交易的主动反思**（"反正系统会记"→ 认知卸载）。这是 notes/09 §2.1 的核心研究空白之一。

### 模式 6："盘前结构化检查"

**定义**：在交易时段开始前，强制完成一个结构化的状态自检 + 计划设定。

**产品实例**：Plancana（AI 生成交易计划 + 每日目标 + 风管规则）；Edgewonk（Sessions 日/周/月复盘卡）

**证据支持**：
- Implementation intentions d=0.65（Gollwitzer & Sheeran 2006, 94 项测试）【S 级】
- σ 系统的盘前 if-then 模板正是这一设计的实现

**σ 系统当前实现**：`sigma/templates/pre-market.md` + `traders/default/daily/` ✅ 已是核心工作流

---

## 五、人-AI 协作的关键风险（学术证据更新）

### 5.1 Automation Bias 仍是最大系统性风险

**2025 Springer 综述**（Exploring automation bias in human-AI collaboration: a review and implications for XAI）【S 级】：
- Automation bias 不是简单的"过度信任"——涉及 AI 素养、专业经验、认知特征、信任动态的**复杂交互**
- **XAI（可解释 AI）不能解决 automation bias**：过于技术化、苛刻或简单的解释反而**强化误置信任**
- **最有效的干预是 active user engagement**——增加验证努力可降低对 AI 错误推荐的盲从
- **含义（U 级）**：σ 系统的"用户先独立完成认知工作再看 AI"设计（foundation §三.2 anchoring 防御）**恰好是这份综述推荐的方向**

### 5.2 人-AI 协作的真实状态远比预期简单

**Frontiers 2024 系统综述**（Human-AI collaboration is not very collaborative yet）【S 级】：
- 当前人-AI 交互被**简单范式主导**：AI 建议 → 人接受/拒绝，很少有真正的交互式协作
- 对 σ 系统的含义：**不必追求复杂的协作设计**。简单的"后台报告 + 用户查阅 + 手动调整"可能就是当前最合理的形态。

### 5.3 预期态度强预测表现

**Harvard Data Science Review 2026**（Bias in the Loop: How Humans Evaluate AI-Generated Suggestions）【S 级】：
- 对 AI 持怀疑态度的人**更可靠地检测 AI 错误**
- 对 AI 持好感的人更容易盲从
- **含义（U 级）**：σ 系统应**主动培养用户对 AI 输出的健康怀疑**——这与 foundation 的"AI 不是裁判，是镜子"定位一致

---

## 六、对 σ 系统的整合对照

### σ 系统已经做对的（相对于市场产品）

| σ 设计选择 | 市场对照 | 优势 |
|-----------|---------|------|
| binding pre-commitment（violations_scan + hooks + red-zone） | 所有竞品都只做"提醒" | 唯一做到"执行层"约束的设计（S 级支持：Fischbacher 2017, FCA 2024） |
| 盘前 if-then 模板（implementation intentions） | Plancana 有 AI 交易计划；其他竞品无 | d=0.65 元分析支持（S 级） |
| 前台 AI 受限 + 用户先独立完成认知工作 | 所有竞品的 AI 都是"随时可用" | notes/09 四维度反向证据 + Springer 2025 automation bias 综述 |
| 后台异步复盘报告 | Zella AI 类似但无违规检测 | JITAI g=0.77 行为改变（S 级） |
| 临床安全筛查（PHQ-4/PGSI） | 所有竞品都没有 | foundation §三.11 独有设计 |

### σ 系统可以从市场学到的

| 市场产品特征 | σ 当前缺失 | 建议优先级 |
|------------|----------|----------|
| **自动券商同步**（Zella 500+ 券商） | 手动 markdown 录入 | 中（留存影响大，但有认知卸载风险；可作为 Phase 3d 的可选层） |
| **纪律-绩效可视化**（Edgewonk Tiltmeter） | WebUI 无仪表盘 | 高（Phase 3c 仪表盘的核心参考；Morewedge debiasing S 级支持可视化反馈） |
| **行为模式统计**（Zella "你周一胜率 32%"） | violations_scan 只做二元违规/不违规 | 中（扩展 violations_scan → pattern_analysis 层） |
| **情绪标记**（Plancana/Edgewonk） | 交易模板无情绪字段 | 低-中（有 Sbarra 2013 高反刍风险需设计避开；可参考 Edgewonk 的"正/负/中"简化标记而非自由文本表达） |
| **Trade Replay 逐笔回放** | 无 | 低（工程复杂度高；对 A 股场景需接入行情数据源） |
| **社区策略分享**（Composer 3,000+ 策略） | 无 | 不建议（与 σ "个人 N=1 训练"定位冲突） |

### σ 系统不应该学的

| 市场产品特征 | 不学的理由 |
|------------|----------|
| 手机优先设计（Plancana） | NBER Cohen 2024/2025：手机入口诱发追涨/碎片化决策（S/M 级）|
| 实时 AI 推送干预（Plancana Smart Notifications） | notes/09：前台 AI 在 4/6 维度反向；FCA 2024：push 增加风险交易（S 级）|
| AI 对话式交易建议（Holly chat） | Bastani 2024 -17%；认知卸载（S 级）|
| 拟人化 AI 人格（"你的 AI 交易伙伴"） | Hodge 2023：拟人化恶化处置效应（S 级）|
| 全自动策略执行（Composer） | 与 σ "人必须经历决策过程才能成长"哲学冲突（foundation §三.2）|

---

## 七、本笔记的局限

1. **所有产品效果评估都是 W 级**：没有任何一个交易 AI 助手有独立同行评审的效果研究（notes/03 §Q7.2 已确认此空白）。"效果比较好"只能从产品设计模式和邻近领域证据推断，不能从直接效果数据判断。

2. **中国市场产品未覆盖**：本调研以英文产品为主。A 股/港股场景的交易助手（如同花顺智能助手、东方财富 AI、雪球等）未调研。这些产品可能有不同的设计模式。

3. **"效果好"的定义本身模糊**：用户留存高 ≠ 交易绩效好（notes/09 §2.2 engagement-effectiveness paradox）。本笔记把"效果好"分解为"设计模式与已知证据一致"来处理，这是 U 级处理方式。

4. **开源 / 自建 AI 交易助手未深入调研**：GitHub 上有大量开源交易 bot（Freqtrade、Jesse、Hummingbot 等），但它们基本都是全自动 α 系统，不是半自动 σ 系统。

5. **本笔记的"σ 对照"全部是 U 级推论**：把产品特征与学术证据做交叉对比是逻辑推演，不是直接验证。

---

## 引用清单

### 学术来源（S/M 级）

- arXiv 2412.20138 (2024). TradingAgents: Multi-Agents LLM Financial Trading Framework. Tauric Research.
- arXiv 2603.13942v1 (2026). AI Agents in Financial Markets: Architecture, Applications, and Systemic Implications.
- CFA Institute RPC (2026). Agentic AI for Finance: Workflows & Case Studies.
- Springer (2025). Exploring automation bias in human-AI collaboration: a review and implications for explainable AI. *AI & Society*.
- Frontiers in Computer Science (2024). Human-AI collaboration is not very collaborative yet: a taxonomy of interaction patterns in AI-assisted decision making.
- Harvard Data Science Review 8.2 (2026). Bias in the Loop: How Humans Evaluate AI-Generated Suggestions.
- ScienceDirect (2025). Uncovering the dynamics of human-AI hybrid performance: A qualitative meta-analysis.
- Bastani et al. (2024). *PNAS*. [已在 notes/03 引用]
- Wang et al. (2023). JITAI meta-analysis. [已在 notes/09 引用]
- Fischbacher, Hoffmann & Schudy (2017). *Management Science*. [已在 notes/03 引用]
- Auer & Griffiths (2014). *International Gambling Studies*. [已在 notes/03 引用]
- FCA (2024). Occasional Paper 66. [已在 foundation 引用]
- Gollwitzer & Sheeran (2006). *AESSP*. [已在 notes/03 引用]
- Morewedge et al. (2015). *Policy Insights BBS*. [已在 notes/03 引用]
- Hodge et al. (2023). *J. Behavioral Finance*. [已在 notes/03 引用]
- Cohen et al. (2024/2025). Robinhood mobile trading studies. NBER/SSRN. [已在 notes/07 引用]

### 产品与行业来源（W 级）

- Trade Ideas Holly AI: trade-ideas.com/hollyguide/
- TrendSpider: trendspider.com/product/
- Composer: composer.trade/
- TradeZella: tradezella.com/ + StockBrokers.com review (2026)
- Edgewonk: edgewonk.com/ + edgewonk.zendesk.com/ (Tiltmeter)
- Plancana: plancana.com/features
- FX Replay: fxreplay.com/learn/ (2026 AI trading overview)
- Tradeciety: tradeciety.com/best-online-trading-journals (2026)
- TradingAgents GitHub: github.com/tauricresearch/tradingagents
- RogueQuant Substack: roguequant.substack.com (trader LLM prompt engineering)
- MindStudio blog: mindstudio.ai/blog/ (Claude Code trading agent tutorial)
- awesome-mcp-servers: github.com/TensorBlock/awesome-mcp-servers (finance MCP tools)
- finder.com/stock-trading/ai-trading-bot (2026 AI bot comparison)
- traderssecondbrain.com/guides/tradezella-review (2026)

---

> **本笔记终极结论（U 级）**：
>
> 当前市场上"效果比较好"的半自动交易 AI 助手可以分为三类——信号生成（A）、策略执行（B）、行为监控（C）。σ 系统属于第三类但更进一步：它不只监控行为（Zella AI / Edgewonk），还**强制执行行为约束**——这在当前商业产品中是独特的。
>
> **σ 系统的独特性在于把学术证据（binding pre-commitment S 级、if-then d=0.65 S 级、前台 AI 反向证据 S 级）转化为工程设计**，而市场产品普遍停留在"提醒但不强制"的软约束层。
>
> 可以从市场学到的主要是**体验层面的设计**：纪律-绩效可视化（Tiltmeter）、具体化行为模式统计（Zella Insights）、低摩擦数据录入（券商同步）——这些不改变 σ 的核心架构，而是改善用户体验和留存。
>
> **诚实标记**：以上所有"效果好"的判断都基于产品设计模式与已知证据的一致性分析（U 级），不基于产品本身的效果数据——因为**没有任何交易 AI 助手有独立同行评审的效果评估**。
