# 上下文切换成本与"必经之路"调研

> 调研日期：2026-05-05
> 调研方法：Web 检索（认知心理学 / HCI / 交易行为 / EMA / 数字干预 / 行为经济学 / 临床信息学）
> 证据等级：S（同行评审 / 系统综述 / 大型 RCT）/ M（监管机构论文 / 大型行业数据 / 工作论文）/ W（行业博客 / 营销 / 单一团队产品材料）/ U（基于已知文献的逻辑推演）
> 上下文：Phase 2 入口形态调研的子任务 5。这是 Phase 1 多模型 review（Gemini 5 视角 + GPT-5.5 5 视角）一致指出的 Phase 2 必查维度——"如果决策链入口出现在用户实际下单前的物理路径上，效果如何？如果不能，系统会不会只记录'愿意记录的交易'而漏掉最危险的冲动交易？"
> 状态：本笔记是 Phase 2 调研档案；不在此处下设计决定。设计决定由 Phase 2 整体 review 后写入 `foundation_2026.md`。
> 元规则提示：所有论述带证据等级。无来源 = U 级 + "诚实标记"。

---

## 摘要（先读这一页）

**1. 上下文切换的认知成本是 S 级硬证据，但日常应用对单笔交易的"毫秒"成本并不致命；致命的是"事件间的注意力残留"和"已经在另一个心境里"。**【S】
- Rogers & Monsell（1995, *J Exp Psychol Gen*）以及 Kiesel et al.（2010, *Psychol Bull* 综述 400+ 研究）证明：在受控实验中切换两类简单任务的反应时增加 100–500 ms（"switch cost"）；即使给到 1.2 秒准备时间也存在不可消去的 "residual switch cost"。
- 但毫秒级切换成本不是日常争议焦点——真正在 σ 决策链场景里起作用的是 **Leroy（2009, *Organ Behav Hum Decis Process*）的 attention residue**：注意力从任务 A 转到任务 B 后，A 的认知活动仍在持续干扰 B；即便完成了 A 也不能完全消除残留。
- **暗示**：把 σ 入口放在"用户从下单工作台切出去到独立 App 写字"这条路径上，付出的不只是切换时间，还有从"交易工作台心境"切到"反思心境"再切回去时的注意力残留 —— 这一段的总成本远高于教科书引用的"23 分钟"标语。

**2. 知识工作者每天 1,200 次应用切换是 M-W 级数据，"23/25 分钟恢复全焦点"是引用层级混乱的常见标语，原始证据较薄。**【M / W 标语溯源】
- HBR 2022 / 工业咨询数据（Qatalog & Cornell, 2022, M 级灰色文献 / Meister Co. 二次引用）：知识工作者平均每天 ~1,200 次应用切换，~9% 工作时间用于切换重定向；典型注意停留 ~3 分钟。
- Mark, González & Harris（2005, CHI *No Task Left Behind?*, S 级）：信息工作者平均每个"工作球体"持续 12 分钟、然后被中断；57% 的工作球体被中断，多数中断当日恢复但需经过 2 个以上中间活动。
- Mark et al.（2008, CHI *The Cost of Interrupted Work*, S 级）：被中断者完成任务的速度其实**更快**（与同侪压力一致），代价是更高的压力、挫折和工作量感。
- "中断后 23 分钟恢复全焦点"在 Mark 的原文中**未直接出现**——这是后期媒体对 Mark 系列研究的二次包装（W 级标语）。原始研究中给出的更接近"任务多被打断、当日内可恢复但伴随注意残留"。
- **暗示**：用"23 分钟"做设计依据是不诚实的；但用 Mark 工作球体 / 中断频率 + Leroy attention residue 这一组 S 级证据做设计依据是稳妥的。

**3. 即时记录（EMA）vs 事后回忆的数据质量差距是 S 级证据：偏差是系统性的、不是均值噪声。**【S】
- Shiffman, Stone & Hufford（2008, *Annu Rev Clin Psychol*）以及 Maes 等 EMA validity systematic review（2022, *Perspect Behav Sci*）：EMA 减小回忆偏差、提升生态效度；retrospective 评分相比 EMA 均值通常**偏高**，被解释为对"显著时刻"的过度加权（peak / end bias）。
- 一项 person-oriented 分析（Cain et al., 2024, *J Person-Oriented Res*）显示约 50% 个体的 retrospective 评分与 EMA 均值无显著差异——也就是说**偏差非均匀，对一部分人很严重，对另一部分人不显著**。在交易场景里，这恰好意味着**最容易出问题的那部分用户最容易回忆失真**（U 级推论，等下展开）。
- EMA 总体依从率：~79%（Williams et al., 2024 EMA meta-analysis），有金钱激励时显著更高（M-S 级）。
- **暗示**：让交易者"事后写日志"对低风险交易者数据质量影响小，但对高风险 / 冲动型交易者影响大——而后者恰好是系统最需要数据的人群。

**4. 下单冲动的可拦截窗口在神经经济学层面已有量化：核心拦截点是"想到 → 下单"之间的几秒到几十秒。**【M / S】
- Bossaerts 等（EPFL Infoscience）：极端时间压力（1 秒决策窗口）下交易者表现为**冲动性高价买入**、对预期奖赏极度敏感、对方差/偏度反而不敏感；3–5 秒窗口下冲动性消失（S 级，但样本受限）。
- Decision Neuroscience 综述：subthalamic nucleus 在风险决策**任务开始前**就已经显现"是否将做高风险决策"的神经活动模式（Zaghloul et al., 2018, *eNeuro*）；这意味着冲动倾向在显意识"按下买入"之前已经存在。
- Loewenstein 系列 hot-cold empathy gap（Loewenstein, 2005, *Health Psychol*；Read & van Leeuwen, 1998）：身处"hot state"的人**系统性低估**自己当下情绪对决策的影响；即"我现在不是被情绪驱动的"这个判断本身就是被情绪驱动的。
- **暗示**：拦截必须发生在**进入 hot state 之前或刚进入之时**——一旦订单页打开、手指悬停在按钮上，干预的有效性急剧下降。这给"σ 入口位置"画了一条很硬的边界。

**5. 浏览器扩展 / 系统级干预的有效性是有的，但**仅对"被高风险刺激暴露的子集"显著**；普通用户中影响接近 0。**【S】
- NewsGuard NYU 实验（Aslett et al., 2022, *Sci Adv* — "News credibility labels have limited average effects on news diet quality and fail to reduce misperceptions"）：在 3,000+ 受试中，平均效应近 0；**对最重度的虚假新闻消费者**有显著改善。
- StayFocusd / Freedom 类阻断软件的 Microsoft Research 32 人 field study（Mark et al., 2018）：阻断显著提高自评专注度，**对最受社交媒体干扰的人收益最大**；但对低自控用户阻断**反而提高压力**（不休息、过劳）。
- Patterson et al.（Cornell MOOC, 2020）：commitment device（预先设定时间限制）**有效**（+24% 学习时间、+0.29 SD 成绩、+40% 完成率）；reminder 和 site-blocker **无显著效果**。
- **暗示**：扩展 / 浮窗类介入对"最该被介入的子集"是有效的——这跟交易里"最该被拦截的冲动交易"完美对应。但对普通日子的普通交易，扩展的边际效应是 0 甚至负的（增加压力）。**这是一个高方差工具：好用是真的好用，没用是真的没用。**

**6. "好摩擦" vs "坏摩擦"的边界是有清晰判据的，并不是含糊的"看场景"——核心判据是：摩擦阻挡的是用户当下未来都会后悔的行为，还是用户深思熟虑也想做的行为。**【S / M】
- Sunstein "Sludge"（2019, *Duke Law Journal*；2021, *Behav Public Policy*）：sludge = 阻挡用户去做对自己有利的事的摩擦；nudge / good friction = 阻挡用户去做未来会后悔的行为的摩擦。
- Lukoff, Lyngs et al.（CHI 2022）的 DSCT 自决理论框架：**强制力 vs 易绕过**是连续谱，强制力高 → 用户达成目标但触发心理反弹弃用；强制力低 → 不达成目标。**最优解是"用户已经将动机内化"时使用中等强制力**——对仍处于动机外化的用户，强制摩擦反而提高弃用率。
- Buzinski & Price（2015, "Don't Tell Me What to Do"）+ 心理反弹（reactance）综述：**对自由感的威胁会触发反向行为**——这是设计强制摩擦时的硬约束。
- 25 小时延迟显著降低冲动消费意愿；10 分钟延迟没有显著效果（Moser et al., 2019, CHI Impulse Buying；S 级，但样本小）——**冷却期长度 < 几小时基本无效**。
- **暗示**：σ 决策链如果短到 30 秒（轻量），缺乏改变冲动的力量；如果长到 25 小时（重量），交易机会消失、用户必然弃用。**真正可工作的 zone 是 1–5 分钟的"在场强制思考"**——并且这必须以"用户已部分认同"为前提，否则触发反弹。

**7. EHR 临床决策支持是一个反向警示：alert override 率 46–96%、其中 72.5% 在 3 秒内被点掉（自动化驳回）。**【S】
- Bryan et al.（2022, *JAMIA*）+ 系统综述（Page et al., 2017）：临床医生对决策支持弹窗的关闭已经**形成习惯**——不是看完再决定，而是手指自动点掉。
- **暗示**：σ 决策链如果以"打断式弹窗"形式介入交易工作台，**几次重复后会形成"自动驳回"习惯**。决策链的形式本身决定了它会不会变成 alert fatigue 的下一例。

---

> **元命题（U 级，但建立在以上 1–7 之上）**：
>
> 决策链如果落在用户**实际下单前的物理路径上**，会面临两个相反的力：
>
> （正向）抓住 hot state 形成前的窗口、利用 EMA 数据质量优势、利用注意残留较小的同一心境、避免事后回忆偏差。
>
> （反向）增加切换成本、可能触发 alert fatigue / 心理反弹、强制力过强会被绕过、强制力过弱会被忽视。
>
> **决定哪一边赢的，是入口形态、强制力梯度、是否落在用户已经在的工作台、以及用户是否已经部分内化动机。**
>
> 一个直接答案是不可能的；但一个"哪些组合显然不工作"的反向答案是可能的，本笔记后面会给出。

---

## 一、context switching 的认知成本基础证据

### 1.1 经典 task switching 文献（毫秒级）

**Rogers, R. D., & Monsell, S. (1995). "Costs of a predictable switch between simple cognitive tasks." *Journal of Experimental Psychology: General*, 124(2), 207-231.**【S】
- 受试者交替分类字符对的"奇偶"或"辅元"——切换 trial 反应时显著高于重复 trial。
- 给到 0.6 秒准备时间，switch cost 部分降低；给到 1.2 秒，仍存在 "residual switch cost"。
- 残留代价被归因于"由刺激触发的外源性 task-set 重构"——即**只有在新刺激出现时，新的任务规则才被激活**。
- 结论：人无法预先全部"想好换任务"——总有一部分必须等到刺激出现才能完成切换。

**Monsell, S. (2003). "Task switching." *Trends in Cognitive Sciences*, 7(3), 134-140.**【S】
- 综述。switch cost 经 400+ 研究复现。
- 切换成本由多个机制叠加：task-set inertia（前一个任务的激活/抑制残留）、stimulus-response 干涉、proactive interference。
- 最近 stimulus-response 经验、prior trial 比例都显著影响 switch cost 大小。

**Kiesel, A., Steinhauser, M., Wendt, M., Falkenstein, M., Jost, K., Philipp, A. M., & Koch, I. (2010). "Control and interference in task switching—A review." *Psychological Bulletin*, 136(5), 849-874.**【S】
- 系统综述，含 4 个部分：实验范式、准备机制、干扰现象、未来方向。
- 关键结论：n-2 task-repetition cost（连续 ABA 比 CBA 慢）证明**抑制刚做完的任务会留下持续 1+ trial 的痕迹**——这是 attention residue 的实验室证据基础。

**Wylie, G. & Allport, A. (2000). *Psychological Research*, 63 — "Task switching and the measurement of switch costs"**【S】
- 开始系统刻画 residual switch cost 的来源；区分"自上而下重构"vs"自下而上由刺激触发的重构"。

**Strobach, T. et al.（2024 update meta；Springer *Psychological Research*）"The effect of age on task switching."**【S】
- 切换成本随年龄上升而增加，但不是简单线性。这与"老练交易者切换成本更小"的常识一致，但要小心 selection bias。

### 1.2 attention residue（这是真正在 σ 场景里起作用的层级）

**Leroy, S. (2009). "Why is it so hard to do my work? The challenge of attention residue when switching between work tasks." *Organizational Behavior and Human Decision Processes*, 109(2), 168-181.**【S】
- 两个实验，n ≈ 200。
- 核心定义：attention residue = "持续中的认知活动，关于刚刚停下的任务 A，即便已经在做任务 B"。
- 关键反直觉：**仅仅完成任务 A 不能消除残留**——需要在完成 A 时存在时间压力，才能"切干净"。
- 这意味着：如果交易者在做任务 A（看图）时被允许**不慌不忙**地切到任务 B（写日志），残留**反而更多**。
- 直接含义：σ 决策链如果让用户在"不紧迫"的情况下从交易工作台切到反思工作台，可能会让交易工作台的认知激活长时间残留——继续触发"还有交易机会要看"的入侵思维。

**Leroy & Glomb (2018, OBHDP)**：anticipation of time pressure on resumption 也产生 attention residue ——**预期未完成任务会被恢复，本身就是认知负担**。

**Masicampo & Baumeister (2011, *Journal of Personality and Social Psychology*) — "Consider it done! Plan making can eliminate the cognitive effects of unfulfilled goals"**【S】
- Zeigarnik 效应的现代延伸。
- 实验：未完成目标干扰执行功能任务（不影响一般知识任务）。
- **关键发现**：仅仅写下"什么时候、用什么步骤完成"——**不需要真正完成**——就能消除干扰。
- 直接含义：交易者如果在交易前**已经写下** if-then 决策链，那"是否要交易"这个 open loop 不会持续占用 working memory；但如果决策是**事后写**，它在交易过程中始终是 open loop，干扰下一笔交易判断。**这是支持"前置决策链"而不是"事后日志"最强的认知科学证据之一。**

### 1.3 中断与恢复（Mark / Czerwinski / Iqbal 等 HCI 工业研究）

**Mark, G., González, V. M., & Harris, J. (2005). "No task left behind? Examining the nature of fragmented work." *CHI 2005*.**【S】
- 24 名信息工作者，约 1,000 hours 观察。
- 平均每个"工作球体"（连续做某件事）= **12 分钟**，之后被切换。
- **57% 的工作球体被中断**。
- 多数中断当日恢复，但典型恢复前**至少 2 个中间活动**。
- **"23/25 分钟"这个数字 Mark 原文没有给出**——查阅原 PDF 确认。

**Mark, G., Gudith, D., & Klocke, U. (2008). "The cost of interrupted work: More speed and stress." *CHI 2008*.**【S】
- 被中断者完成任务的速度反而**更快**（被 deadline 压力补偿）。
- 代价是**更高的压力、更高的挫折、更高的工作量感**——身体/情绪代价 > 时间代价。

**Czerwinski, M., Horvitz, E., & Wilhite, S. (2004). "A diary study of task switching and interruptions." *CHI 2004*.**【S】
- 11 名信息工作者，连续观察 + 日记。
- 平均每天 **50 个不同任务/项目**。
- **40% 的中断任务永远没有恢复**。
- 直接含义：如果交易者打开了 σ 决策链表单但在中途被市场行情打断，按 40% 的概率这个表单永远不会被填完——除非 σ 设计把"未完成的决策链"硬性绑到下单流程上。

**Cutrell, E., Czerwinski, M., & Horvitz, E. (2001). "Notification, disruption, and memory." *Interact 2001*.**【S】
- IM 中断对搜索任务的影响。
- 早期中断 > 晚期中断对主任务目标遗忘的影响。
- 高相关性消息中断的 disruptiveness 显著降低。
- 直接含义：σ 决策链如果在用户**早期**（看盘阶段）打断，更容易让用户"忘了自己原本要干嘛"——这恰好是想要的"打断冲动"效果。

**Iqbal, S. T., & Horvitz, E. (2007). "Disruption and recovery of computing tasks." *CHI 2007*.**【S】
- 27 名 Microsoft 员工，软件应用使用 + 报警追踪。
- 中断后从应用切换到处理报警再回到原任务的"resumption lag"实测数据。
- 与 Altmann & Trafton (2002, *Cognitive Science*) "memory for goals" 模型一致——8 秒预警可以让恢复显著加快。

**Trafton, J. G. et al. (2003). "Preparing to resume an interrupted task: Effects of prompts and goal rehearsal." *Int J Human-Computer Studies*.**【S】
- "ready-to-resume plan" 显著降低 attention residue。

**Parnin, C. & Rugaber, S. (2009). *ICPC 2009*：编程任务被中断后**只有 10% 的会话在 1 分钟内恢复 coding**；典型恢复需 15 分钟。**【S】

**关于"23/25 分钟恢复"标语的溯源**【W 级标语】：
- HBR 2022 "How Much Time and Energy Do We Waste Toggling Between Applications?"（Qatalog & Cornell 灰色文献，Meister 二次引用）写到"the average time to fully return to work following an interruption is 25 minutes 26 seconds"。
- 原始数据来源是 Mark 团队的某次工业项目，但同行评审发表的版本中**未给出这个具体数字**——它出现在媒体采访和咨询报告里。
- **诚实标记**：我未能在 Mark 的同行评审论文中直接找到"23 分钟"或"25 分 26 秒"作为正式发表的统计量；这是流传广但溯源弱的标语。在 σ 设计中**不应作为依据引用**。

### 1.4 应用切换次数的工业数据

**Qatalog & Cornell University Ellis Idea Lab (2022)** — 数据被 HBR 2022 报道【M / W】：
- 知识工作者每天 **~1,200 次应用切换**（toggling）。
- 累计每周 ≈ 4 小时用于"切换重定向"——约 **9% 工作时间**。
- 一个 Fortune 500 例子：执行单笔供应链 transaction 需要切换 22 个应用约 350 次；某员工日均 3,600+ toggles。

**Pratap et al. (2017) IMWUT** — 大规模手机使用研究【S】：
- 5,811 年累计使用数据（29,279 设备）。
- 平均 **60 次/天 phone interactions**；每次 session < 7 分钟，单 app 使用 < 2 分钟。
- 设备解锁仅占 46%（其他 54% 是"看一眼锁屏"）。

**Mewayz Blog 综合 W 级（注意层级低）**：
- 多工具用户 vs 一体化平台用户对比：1,121 vs 283 daily app switches；多工具用户每天损失 ~98 分钟在切换上。

### 1.5 这一节的硬结论（写到 σ 设计里时可引用）

| 维度 | 数值 / 范围 | 等级 |
|---|---|---|
| 受控实验 task switch cost | +100–500 ms | S |
| 残留 task-set 干扰（n-2 cost） | 持续 1+ trial | S |
| Attention residue 持续时间 | 至少几分钟，未量化 | S |
| 信息工作者 working sphere 长度 | ~12 分钟 | S |
| 工作球体被中断比例 | 57% | S |
| 被中断任务永不恢复比例 | 40% | S |
| 软件 alert 关闭习惯化（< 3 秒驳回） | 72.5% | S |
| 知识工作者每天应用切换次数 | ~1,200（Qatalog） | M-W |
| "23/25 分钟恢复"标语 | 标语，原文无 | 不可信引用 |

---

## 二、交易者工作台的真实形态

### 2.1 典型交易者的应用栈

按用户给出的五类做调查：

**(A) TradingView**【M-W】
- 前端图表 + 多浏览器 / 桌面应用。Layout 系统支持多 chart workflow。
- 直接整合 Tradovate（期货）、ByBit/OKX/BingX/BitGet（加密）等 brokers。
- 用户分两类：
  - 仅图表/分析：在 TradingView 看，下单去券商终端。
  - 图表+下单一体：通过整合 broker 直接在 TradingView 下单。
- 浏览器扩展生态丰富（Leader.Trade, TradingView Magical Keyboard Shortcuts, Remix AI Copilot 等）——**有可介入空间**。

**(B) 中国 A 股券商终端 / 同花顺 / 东方财富**【M / W】
- 同花顺：~21M MAU；东方财富：~19M MAU；涨乐财富通：~11M MAU；大智慧：~6M MAU（2025 数据）。
- 形态：PC 桌面客户端 + 移动 App，前者主要用于看盘 / 技术分析，后者用于下单和资讯。
- 东方财富的"股吧"（社区）日均发帖 100w+——这是强力的"羊群"环境，FCA 9000 人实验显示 leaderboard / 社区 +12% 交易频率（FCA 2024, M-S 级）。
- **关键事实**：在 A 股场景，看盘（同花顺/东财 PC）和下单（券商客户端 / 同花顺手机版）通常**不在同一软件**——很多用户在 PC 看 + 手机下。
- **暗示**：A 股场景的"必经之路"问题更严重——下单这个动作可能发生在用户**已经离开桌面**的状态，桌面端的浏览器扩展类干预**完全无法触达**。

**(C) 期货 / 国际经纪终端**【M】
- IBKR Trader Workstation (TWS) Mosaic：多 panel workspace，可拖拽。
- Bloomberg Terminal（高端）：图表 + 新闻 + 即时通讯 + 下单一体。
- 这一类是"一站式"——下单前的所有信息都在同一个软件里，**意味着 σ 浏览器扩展无法触达，独立 App / 浮窗反而更可能**。

**(D) 移动 App（Robinhood / 同花顺 / 雪球 / 富途 / 老虎等）**【M-S】
- Robinhood 用户平均 **12 分钟/天**（2025 Q4，DAU 2.6M，时间被认为"中等"，Apptopia 数据）【M】。
- Smartphone 投资行为：Kalda et al. (2021, NBER w28363, S 级)——同一投资者在 smartphone 上比 desktop 上**更倾向于买高风险/lottery-type 资产、追涨杀跌**；smartphone 引发的购买 Sharpe 比率显著低于 desktop。
- Barber, Huang, Odean & Schwarz (2022, *Journal of Finance*) "Attention-Induced Trading and Returns: Evidence from Robinhood Users"——retail attention 集中在 attention-grabbing 个股，随后跑输市场。
- **暗示**：移动 App 是冲动行为最严重、又最难介入的场景。系统级浮窗在 iOS 上几乎不可能（沙盒），Android 略好但仍受限。

**(E) 微信群 / Telegram / 雪球评论 / Twitter**【M】
- WeChat 推荐对个股 abnormal returns 显著（Yang et al., 2021, *Physica A*, M）。
- 社交平台沟通增加跟随者交易频率（Liu et al., 2022, *Journal of Financial Innovation*）——但增加的交易**对未来表现负面**。
- Internet posting → 羊群效应在中国 fund 市场被记录（Wei et al., 2022, *Humanities and Social Sciences Communications*）。
- **暗示**：交易冲动的"种子"经常**不在交易工作台**——而在微信群或社交平台。这个事实对"σ 入口位置"是关键约束：如果只守在交易工作台门口，就漏掉了"在群里看到一个推荐 → 30 秒后跑去券商下单"这条最常见的冲动路径。

### 2.2 真实交易者一天的物理路径（重建，部分 U 级）

基于 Robinhood 12 min/DAU、同花顺 PC + 移动双端、社交群信息流，**典型 A 股 / 港股 / 期货散户工作日的物理路径推断**（U 级合成）：

```
06:30 起床
07:00–08:30 微信群 / 雪球 / Twitter / 财经新闻 App（吸收"今日要看什么"信息）
                                ↓ 决定要做的板块 / 标的，往往在这里就部分形成
09:00–09:25 集合竞价；同花顺/通达信 PC 端打开看盘
09:30–11:30 持续看盘；TradingView/同花顺画线、看指标；穿插刷微信群
                                ↓ 中间随时可能"看到一个朋友赚了 → 我也试试"的 hot state 触发
11:30–13:00 午休，但通常还看群、看新闻
13:00–15:00 持续盯盘；下单经常在最后 30 分钟集中
15:00–17:00 收盘后看收盘评论、写交易日志（如果坚持写的话）
晚上 微信群 / 雪球继续刷；偶尔回看自己的当日交易
```

**关键观察**（U 级）：
1. **"决定要交易"的种子可能出现在五个完全不同的物理位置**：微信群、新闻 App、TradingView 图表、同花顺看盘、券商 App 下单页。**任何一个单点拦截都会漏掉至少 60% 的入口**。
2. **冲动交易的特征是从"种子"到"下单"的时间窗口短**——可能短到 5–30 秒（看到群里推荐 → 立即跳到 App 下单）。在这个窗口里能介入的形态**只有：系统级浮窗 / 浏览器扩展 / 设备级 / 必经之路嵌入券商页面**。独立 App 是来不及的。
3. **"事后复盘"为什么会漏掉冲动交易**：因为冲动交易**在用户的叙事里不存在**。事后回忆时，用户会重构出"我看到了 XX 信号所以买了"——而真实的因果是"我在群里看到 X 哥又赚了 → 我心里痒 → 我打开 App → 我找了个看起来合理的理由 → 我买了"。EMA 即时记录 vs 事后回忆的偏差研究（§3）正好命中这个失真。

### 2.3 这一节的硬结论

| 命题 | 证据等级 |
|---|---|
| 散户每天接触至少 5 类信息源 | U（推论） |
| TradingView 用户分两类（仅分析 / 整合下单） | M |
| 中国 A 股 PC 看盘 / 移动下单分离常见 | M-W |
| Smartphone 加剧冲动交易 | S（NBER w28363） |
| 微信群 / 社交内容是冲动种子的常见来源 | M |
| 冲动交易种子→下单可短至 5–30 秒 | U（合成自神经研究 §4 + Robinhood 行为研究） |

---

## 三、"在场记录"vs "事后记录"的数据质量

### 3.1 EMA 与 retrospective 的标准对比

**Shiffman, S., Stone, A. A., & Hufford, M. R. (2008). "Ecological momentary assessment." *Annual Review of Clinical Psychology*, 4, 1-32.**【S】
- 经典综述。EMA = "在自然环境中、对当下行为/经验的多次抽样"。
- 设计目标即"减小回忆偏差、提高生态效度"。
- 直接对比 retrospective 评估时，EMA 在多数构念上显示**系统性差异**（不只是噪声）。

**Stone, A. A., et al. (1998 起多篇)** ：retrospective recall 高估强度 + peak/end bias（与 Kahneman 1993 一致）——人们对体验的记忆受最强时刻 + 终点的不成比例加权。

**Maes, I. et al. (2022, *Perspectives on Behavior Science*) — "Ecological Momentary Assessment: A Systematic Review of Validity Research"**【S】
- EMA 与"金标准"客观测量的相关性中等到高，显著高于 retrospective。

**Wenze, S. J. & Miller, I. W. (2010, *Clinical Psychology Review*)** ：EMA 在精神病学领域已成为效度参照——情绪障碍的 retrospective 评估与 EMA 的差异有时 > 1 SD。

**Cain, A. et al. (2024, *Journal for Person-Oriented Research*) — "Are retrospective assessments means of people's experiences?"**【S】
- **关键的反直觉发现**：约 50% 个体的 retrospective 评分与 EMA 均值**无显著差异**——也就是说"EMA 总比 retrospective 好"是过度泛化。
- 但另外约 50% 个体存在显著差异——这意味着**偏差非均匀**。
- 在交易场景里，**最高情绪化、最高冲动倾向的人往往是 retrospective 偏差最大的人**（U 级推论，但与 EMA 文献一致）。

### 3.2 EMA 在赌博 / 冲动决策场景的应用

**Kelly et al.（MDPI 2021）** ：positive outcome expectancy 与赌博行为的 EMA 关联研究。

**UPPS-P + EMA 研究（OSF preprint 2024）**：14 天 EMA 跟踪，UPPS-P 中"Lack of Premeditation"分量是赌博时间最稳健的预测因子。

**JMIR Research Protocols 2026** ：14 天 EMA + smartwatch 生理监测的赌博预测协议——这是**最接近 σ 系统设想的设计**：把"决策前的状态"作为可观察信号。

**直接含义**：
- 在赌博 / 冲动决策研究里，**"决策前的状态"已被证实是可被 EMA 捕捉的可信信号**——前提是抓住"决策前"那个窗口。
- 反过来说：**事后回忆"我当时是不是冲动"完全不可信**——这是为什么散户事后写交易日志几乎没用的核心机制证据。

### 3.3 即时干预 vs 延迟干预的效果差

**JITAI 综述（Hardeman et al., 2019, *Health Psychology Review* / Wang & Miller 2020, *Annual Review of Psychology*）**【S】：
- JITAI = 在"用户最需要支持的那个时刻"提供干预。
- 数学要求：(a) 状态可被传感器/EMA 捕捉，(b) 干预可在合适窗口送达，(c) 用户当时可接收。

**Mental health JITAI meta-analysis (BMJ Mental Health, 2025)**【S】：
- 23 项研究，pooled g = 0.15（small），但 6 个月后效果保留。
- 短干预（< 6 周）的效果保留更好（g = 0.71）。
- 主要挑战：低依从、用户在最需要时反而最难接受。

**Klasnja et al.（2018, *JMIR mHealth*, 微随机化 RCT, n=1,255）**：
- push notification +3.9% engagement，但效果随天/时段变化巨大。
- 周末 12:30 PM 效果最好（+11.8%）。

**直接含义**：
- "即时记录"如果只是记录、没有反馈，效果≈普通 EMA。
- "即时干预"（即记录 + 当场反馈）效果更大但极其依赖时机。
- **σ 决策链如果只是"在交易前问 5 个问题"——这是 EMA。如果是"问问题 + 给出 if-then 强制规则 + 仓位计算"——这是 JITAI。后者证据基础更强。**

### 3.4 这一节的硬结论

| 命题 | 等级 |
|---|---|
| EMA 比 retrospective 在均值上偏差小、生态效度高 | S |
| retrospective 偏差**不是均匀**——对约 50% 人很严重 | S |
| 冲动 / 高情绪倾向者的 retrospective 偏差最大 | S+U（合成） |
| EMA 对冲动决策研究是金标准 | S |
| JITAI（EMA + 干预）效果 g ≈ 0.15，短干预保留更好 | S |
| 决策前状态是可捕捉的可信信号 | S |
| 事后回忆"我是不是冲动"不可信 | S+U |

---

## 四、下单冲动的可拦截窗口

### 4.1 决策时间窗口的神经经济学证据

**Bossaerts, P. et al. — EPFL Infoscience: "Neurophysiological evidence on perception of reward and risk: Implications for trading under time pressure"**【S】
- 受试者在 1 秒、3 秒、5 秒决策窗口下做交易选择。
- 1 秒：表现为"buying impulsiveness"——倾向于以更高价买入；对 expected reward 极敏感；对 variance/skewness 反而钝化（"风险盲"）。
- 3–5 秒：冲动消失，variance 钝化也消失，对 skewness 敏感升高。
- **关键含义**：人脑处理 reward 和 risk 是**分开**的，且 risk 处理需要更长的神经时间。1 秒的决策完全跳过了 risk 评估神经回路。

**Lo, A., Repin, D. — "Direct access trading" fMRI study (2017, *Frontiers in Neuroscience*)**【S】
- 真实交易者 fMRI。
- **expertise 与 PFC 激活负相关**——老练交易者的 PFC 激活反而**更低**（自动化处理）。
- 自信交易者 strategic decision-making 区域激活更弱。
- **直接含义**：随着经验积累，交易决策**逃离了**前额叶审议——这既是好事（高效）又是坏事（自动化误差被锁死）。
- 对 σ 系统的意义：**老手不需要的不是更长的思考时间，而是 if-then 决策链来锁住正确的自动化路径**。新手需要的是**强制 PFC 介入**——也就是真正的"思考冷却期"。

**Zaghloul, K. A. et al. (2018, *eNeuro*) — "Subthalamic Neural Activity Patterns Anticipate Economic Risk Decisions"**【S】
- subthalamic nucleus 在**任务开始前**就显示了"将要做高风险决策"的活动模式。
- 这意味着：**冲动倾向比显意识更早**——你"决定要冒险"在你"觉得自己决定要冒险"之前。
- 直接含义：拦截冲动如果只在"按下买入按钮前"，已经太晚了——决策已经在大脑里完成了。**有效拦截必须更早**。

**Frontotemporal regulation of subjective value (2020, *J Neurosci*)**【S】
- DLPFC 通过下调主观价值来抑制 intertemporal choice 中的冲动。
- 直接含义：**让 DLPFC 介入是抑制冲动的核心生物学机制**。"看 5 秒钟图表 + 写下入场理由"恰好是激活 DLPFC 的标准方式。

### 4.2 hot-cold empathy gap

**Loewenstein, G. (2005). "Hot-cold empathy gaps and medical decision making." *Health Psychology*.**【S】
- 处于 hot state（情绪化）的人**系统性低估**当下情绪对决策的影响。
- "我现在不是被情绪驱动的"是被情绪驱动的人的典型自评。
- 反向同理：处于 cold state 的人也**低估** hot state 将如何影响自己。
- 直接含义：在 cold state 写好的"决策链"是 hot state 的真正约束——**只有在 cold state 写下 + 在 hot state 强制执行**这一组合才能跨越 empathy gap。

**Read, D. & van Leeuwen, B. (1998). "Predicting hunger: The effects of appetite and delay on choice." *OBHDP*.**【S】
- 经典示范：饥饿状态下的人对未来选择的预测**完全不像**自己未来在饱腹下做的选择。

**直接含义**：交易者"明天我一定不冲动"在 cold state 下说的话——hot state 的他不会执行——除非有 commitment device 锁住。

### 4.3 冷却期长度的经验证据

**Moser, C. et al. (2019, CHI) — "Impulse buying: Designing for self-control with e-commerce"**【S，但样本小】
- **25 小时延迟**：显著降低冲动消费的 felt urge 和 purchase intent。
- **10 分钟延迟**：100% 的人仍在购物，无显著效果。
- 中间区段未充分研究。

**消费者保护文献 / cooling-off period 法律评估（St. John's Law Review, 2024）**【M】
- 三天 rescission period 在多数场景下使用率极低（<1%）；只有当 oral + written 都给出时才显著提高使用率。
- "illusory consumer protection"的批评。
- 直接含义：**单纯有冷却期 ≠ 用户真的会冷静**——冷却期 + 主动提醒 + 重新评估流程 才有效。

**Bckwon (Wharton) "Causes of delay in consumer decision making"** — **延迟决策本身是积极行为**，但需要外部支撑。

### 4.4 这一节的硬结论：冲动可拦截窗口的真实形状

```
[t = -∞]                                          [t = -10s]              [t = 0 下单]
     │                                                  │                       │
     │    ─── cold state（未触发）───                    │ ─── hot state ───     │
     │                                                  │                       │
   时间充裕的"前置规则书写"             冷却期/介入                 太晚了
   ✓ implementation intention（Gollwitzer）           ✓ 只对约 50%概率有效     ✗ neural evidence 已经
   ✓ if-then 决策链（计划本身免费 1+ 周成本）          ✓ DLPFC 强制介入            完成决策
   ✓ Masicampo & Baumeister "consider it done"        ✓ 25-hour 显著                hot-cold gap
                                                        但10-min 无效            交易者听不进
```

最有效的拦截发生在 **t < -10 分钟**（hot state 形成前）；
最不可靠的拦截发生在 **t = -10s 到 0**（hot state 已经形成）；
事后干预（t > 0）只能改善 next 笔交易，**不能挽救当前**。

| 命题 | 等级 |
|---|---|
| 1 秒决策下 risk 评估神经回路被跳过 | S |
| 老练交易者的决策 PFC 介入更少 | S |
| subthalamic nucleus 在显意识前就预测风险偏好 | S |
| hot state 中人系统性低估自身情绪影响 | S |
| 25 小时延迟显著降低冲动；10 分钟无效 | S（小样本） |
| 冷却期 + 主动提醒 比单纯冷却期有效 | M |
| 拦截窗口的"sweet spot"在 hot state 形成前 | S+U（合成） |

---

## 五、4 类介入形态 × 5 类工具的物理可达性矩阵

### 5.1 介入形态的物理可达性定义

**可达性 = (a) 能否在用户的物理路径上出现 + (b) 能否在 hot state 形成前介入 + (c) 能否被绕过的难度 + (d) 能否避免触发 alert fatigue / reactance**

四类介入形态：
- **(I) 浏览器扩展**：跑在 Chrome / Edge 内，能注入页面元素，能拦截/延迟跳转，但只能在浏览器内有效。
- **(II) 系统级浮窗**：操作系统层面的悬浮窗口（macOS Floaty 类、Android System Alert Window、iOS 完全不可能）。
- **(III) 独立 App**：用户主动打开的应用。
- **(IV) 文档**：Notion / Obsidian / 纸质笔记本——纯被动记录工具。

### 5.2 矩阵

| 工具 / 介入形态 | (I) 浏览器扩展 | (II) 系统浮窗 | (III) 独立 App | (IV) 文档 |
|---|---|---|---|---|
| **TradingView Web** | ✓✓ 可注入图表/订单页面 | ✓ macOS/Windows OK | ✗ 隔离 | ✗ 完全隔离 |
| **TradingView 桌面 App** | ✗ 不能注入 native | ✓ 可悬浮 | ✗ 隔离 | ✗ 隔离 |
| **TradingView 移动 App** | ✗ 不能注入 | ✗ iOS 沙盒；Android 受限 | ✗ 切换出去 | ✗ 切换出去 |
| **A 股券商 PC 客户端**（同花顺、通达信） | ✗ 桌面 native | △ Windows 可悬浮 | ✗ 切换 | ✗ 切换 |
| **A 股券商移动 App** | ✗ | ✗ iOS / Android 受限 | ✗ 切换 | ✗ 切换 |
| **国际 broker 桌面**（IBKR TWS） | ✗ native | △ 可悬浮但小窗 | ✗ 切换 | ✗ 切换 |
| **国际 broker 移动**（Robinhood, IBKR Mobile） | ✗ | ✗ | ✗ | ✗ |
| **微信群**（PC 微信 / 手机微信） | ✗ 桌面 native | △ 可悬浮 | ✗ 切换 | ✗ 切换 |
| **新闻 App / 雪球 / 财经类 App** | △ Web 端 OK | △ 桌面悬浮 | ✗ 切换 | ✗ 切换 |
| **桌面浏览器内查看 A 股相关网页** | ✓✓ | ✓ | ✗ | ✗ |

**符号**：✓✓ = 强可达；✓ = 可达；△ = 部分可达；✗ = 不可达

### 5.3 关键观察

**观察 1：移动场景几乎所有形态都不可达。**
- iOS 沙盒禁止 system overlay（除非 PiP / Live Activity，但都不是介入用途）。
- Android 的 System Alert Window 权限越来越被收紧（Android 12+ 需要用户手动开启 + 应用商店审查严格）。
- **后果**：σ 系统对移动端冲动交易**没有任何技术手段做强制介入**——这是设计阶段必须接受的物理边界。
- 唯一可工作的方案：让用户**主动**在 hot state 之前打开 σ App + 写下规则；hot state 形成时只能依赖**用户已经内化的规则**（Gollwitzer's implementation intention）。

**观察 2：A 股桌面客户端是 native 应用，浏览器扩展完全不可达。**
- 同花顺 PC 客户端 / 通达信 PC 客户端 / 多数券商客户端都是 Windows native（Win32 / Electron 包装）。
- 浏览器扩展**仅对在浏览器中查看 A 股网页（如东方财富 web）的用户有效**。
- 实际场景：A 股重度散户**通常用 PC 客户端而非浏览器**——浏览器扩展形态对 A 股用户**覆盖率低**。

**观察 3：浏览器扩展对 TradingView Web 用户高度可达，对其他场景覆盖低。**
- TradingView 的 web 版用户群是浏览器扩展形态的**核心受众**。
- 跨工具一致性（一个扩展对所有 broker 都生效）很难达成——每个 broker 页面结构不同。

**观察 4：文档形态在所有场景都不可达，只能依赖用户主动打开。**
- 这就是当前 σ Stage 0 的形态——一个 Markdown 模板。
- 留存率证据（§01 笔记 + tradingjournal.com 综述）：**80% 用户在 2 周内放弃**。
- **不是文档形态本身不行，而是文档形态的"可达性"= 用户主动意愿，这个意愿在 hot state 下为零。**

**观察 5：系统浮窗在桌面端有效，移动端基本不可达。**
- Floaty / WindowTop / DeskPins 类工具证明 macOS / Windows 浮窗技术成熟。
- 浮窗作为"提醒"形态有 EHR 类比警示——alert fatigue 风险（§7）。
- 浮窗作为"必经之路"（强制点击才能继续）会触发 reactance。
- 中等强制力浮窗（提示但不阻塞）证据基础最弱——可能既不够强又触发 reactance。

### 5.4 综合可达性评分（U 级综合）

| 形态 | 可达性 | hot state 前介入能力 | 难绕过 | 不触发 fatigue/reactance | 综合 |
|---|---|---|---|---|---|
| 浏览器扩展（仅 Web 用户） | 高（仅子集） | 高 | 中 | 中 | 中-高 |
| 桌面浮窗 | 中 | 中 | 高（强制版） | 低（fatigue 风险） | 中 |
| 独立 App | 用户意愿 | 低（hot state 用户不打开） | N/A | 高（不打扰） | 低 |
| 文档 | 用户意愿 | 极低 | N/A | 高 | 极低 |

**没有任何单一形态在所有四个维度上都过关。**

### 5.5 这一节的硬结论

| 命题 | 等级 |
|---|---|
| iOS 移动端不可能做系统级强制介入 | S（OS 限制） |
| A 股 PC 客户端不被浏览器扩展触达 | S（架构事实） |
| 文档形态可达性=用户意愿，在 hot state 下为 0 | M-S |
| 没有单一形态覆盖所有 5 类工具场景 | S（矩阵分析） |
| 任何方案都需要**多形态组合 + 接受边界** | S+U（合成） |

---

## 六、好摩擦 vs 坏摩擦的边界证据

### 6.1 sludge / good friction 的判据

**Sunstein, C. R. (2019). "Sludge and ordeals." *Duke Law Journal*, 68, 1843-1883.**【S】
- sludge = 阻挡用户做对自己有利之事的摩擦。
- good friction = 阻挡用户做未来会后悔之事的摩擦。
- 判据本身依赖**用户未来偏好**——但 hot-cold empathy gap (§4) 告诉我们这个"未来偏好"很难直接测量。
- Sunstein 提出 "sludge audit" 方法：定期审查机构施加的摩擦是否真有正当理由。

**Sunstein, C. R. (2021). *Sludge: What stops us from getting things done and what to do about it.* MIT Press.**【M】
- 把 sludge 概念扩展到一切让"该完成的事"难完成的摩擦。
- 9.78 billion hours 美国年度纸面工作 ≈ $264 billion——sludge 的规模化代价。

**Behavioural Public Policy 2022 — "Sludge audits"**【S】
- 系统化审查方法：(1) 列出所有摩擦点 (2) 估算成本 (3) 评估必要性 (4) 重设计。

### 6.2 self-control tool / 强制力梯度

**Lukoff, K., Lyngs, U., Alberts, L., Hiniker, A. (2022). "How the design of digital self-control tools can support psychological autonomy." *CHI 2022*.**【S】
- 数字自控工具按强制力分类。
- 强制力 vs 易绕过 是连续谱：
  - 弱：易绕过 → 不达成目标
  - 强：难绕过 → 达成目标但触发反弹弃用
  - 中：trade-off 但仍不完美
- 关键洞察：**自决理论（Deci & Ryan, 2000）**——内化动机的用户对中等强制力反应良好；外化动机的用户被强制力激起反弹。

**Buzinski, S. & Price, M. (2015). "Don't tell me what to do." *Personality and Social Psychology Bulletin*.**【S】
- 自由感被威胁 → 反向行为（boomerang effect）。
- 直接对 σ 决策链的硬约束：**任何"必须填"的字段都会触发部分用户的反弹**——填假数据、敷衍应付、最终弃用。

**Mark, G. et al. (2018, Microsoft Research) — "How blocking distractions affects workplace focus and productivity."**【S】
- 32 名信息工作者 RCT。
- 阻断软件提高自评专注度。
- **反直觉发现**：低自控用户在阻断下**压力更高**——他们继续工作不休息（"被强制专注"反而失去自我调节）。
- 含义：强摩擦对**已有部分自控的用户**有用；对**完全没有自控的用户**反而伤害。

**Patterson, R. (2020, Cornell, MOOC RCT)**【S】
- 三种工具对比：commitment device（预先承诺时间限制）、reminder、site-blocker。
- commitment device：+24% 学习时间、+0.29 SD 成绩、+40% 完成率。
- reminder 和 site-blocker：**无显著效果**。
- 含义：**用户预先主动承诺的强制力 > 系统单方施加的强制力**——这是 σ 设计最重要的一条 design principle。

### 6.3 alert fatigue 的反例（坏摩擦的临床警示）

**Phansalkar, S. et al. (2014, *JAMIA*)**【S】 / **Page, N. et al. (2017, *JMIR Med Inform*) 系统综述**【S】
- EHR 临床决策支持系统的 alert override 率：46.2%–96.2%（drug-drug interaction：95.1%）。
- 即使知道 alert 重要，临床医生仍 override 大多数。

**Bryan, M. et al. (2022, *JAMIA*) — "Habit and Automaticity in Medical Alert Override"**【S】
- **72.5% 的 alerts 在 3 秒内被 dismiss**；13.2% 在 1 秒内。
- 这是 automaticity，不是审议。
- 直接含义：**任何弹窗式干预，重复几次后都会变成"手指自动点掉"的反射**——σ 决策链如果是弹窗形式，几周后就会被驯化为自动驳回。

### 6.4 commitment device 的回旋镖

**John, A. (2020, *Management Science*) — "When commitment fails: Evidence from a regular saver product in the Philippines"**【S】
- 55% 的低收入储蓄客户**净亏损**于"承诺储蓄"产品（罚金 > 收益）。
- commitment device 在用户**不能准确预测自己未来行为**时**伤害**用户。

**Carrera, M. et al. (2022, *Review of Economic Studies*) — "Who chooses commitment? Evidence and welfare implications"**【S】
- 约 **50% 的人同时为"提高 gym 出勤"和"降低 gym 出勤"两个相反目标买单**——他们不知道自己真正想要什么。
- 直接含义：**对自我认知不清的新手交易者，强 commitment device 反而可能锁住错误的目标**。

### 6.5 这一节的硬结论：好摩擦的判据

**摩擦是"好"的，当且仅当**：
1. 它阻挡的行为是用户**预先主动承诺要避免**的（Patterson 2020 + Lukoff 2022）。
2. 它的强度与用户当前**动机内化程度**匹配（Lukoff 2022）。
3. 它**不重复到形成驳回习惯**（Bryan 2022）。
4. 用户**可以理解为什么这个摩擦在那里**（Sunstein 2019）。
5. 它**不锁住用户认知错误的目标**（Carrera 2022）。

**摩擦是"坏"的，当**：
1. 它在用户没有承诺时被强加。
2. 它强度高于用户动机内化程度。
3. 它频繁出现以至于成为反射点击。
4. 它没有可理解的理由。
5. 它锁住了用户后悔的目标。

| 命题 | 等级 |
|---|---|
| good friction 与 sludge 的核心差异是"用户未来偏好" | S |
| 用户预先承诺的强制力 > 系统单方强制力 | S（Patterson） |
| 强制力必须匹配动机内化程度 | S（Lukoff） |
| 重复弹窗 → automaticity 驳回 | S（Bryan） |
| 50% 用户对自我认知不清 → commitment 反伤 | S（Carrera） |
| **中度强制力 + 用户预先承诺 + 不重复**是 sweet spot | S+U（综合） |

---

## 七、对 σ 系统的具体含义（U 级）

> **本节全部为 U 级推论。** 所有结论建立在 §1–§6 的 S/M 证据之上，但具体设计选择是基于这些证据的**逻辑组合**——其有效性需要在系统试点 + 周复盘中持续校验。
>
> 这一节不替代 Phase 2 整体 review 后的设计决定。它给出的是"哪些组合显然不工作"+ "哪些组合的赔率较好"。

### 7.1 哪些组合显然不工作（淘汰）

**(a) "事后回忆 + 文档形态"**
- 数据质量低（§3 retrospective bias）。
- 漏掉冲动交易（用户的叙事不包含冲动）。
- 留存率低（§01 笔记 + 行业 80%/2 周）。
- **淘汰理由**：在所有维度上都是最弱的组合。

**(b) "强制弹窗 + 高频重复"**
- 几周后形成 alert fatigue 自动驳回（§6.3）。
- 触发 reactance（§6.2）。
- 不解决 hot state 的核心问题（用户驳回后心境已经定型）。
- **淘汰理由**：复制 EHR 的失败。

**(c) "纯靠系统单方施加摩擦"**
- Patterson 2020 显示 site-blocker / reminder 单方施加 = 无效。
- 用户没有 internalize 时强制力会反弹。
- **淘汰理由**：证据基础几乎为 0。

**(d) "事后日志 + 长字段表单"**
- §06 笔记已经证明 11→4 字段砍掉提升完成率 120%。
- 时间投入是 mHealth 弃用的头号原因（§01）。
- 与 retrospective bias 叠加。
- **淘汰理由**：当前 σ Stage 0 的隐含设计，已知不工作。

**(e) "依赖移动端系统级强制介入"**
- iOS 物理上不可能（沙盒）；Android 可能但权限收紧。
- 即使技术可行，移动端 hot state 的拦截窗口太短（5–30 秒）。
- **淘汰理由**：物理边界。

### 7.2 哪些组合赔率较好（候选 zone）

**核心 design pattern（U 级，但建立在 S/M 证据之上）**：

```
[cold state, 交易日开盘前]
  ├─ 必经动作 1：写下今日"if-then 决策链"
  │  - 形式：implementation intention（Gollwitzer 2024 meta d=0.65）
  │  - 写下 = open loop 关闭（Masicampo 2011），不再干扰当日交易
  │  - 字段数 ≤ 6（Sweller cognitive load + §06 笔记）
  │  - 用户主动承诺（Patterson 2020）
  │  - 写完后"今日交易规则"以**用户已承诺的形式**存在
  │
[trading hours, 进入 hot state 之前]
  ├─ 介入形态 1：仅在用户**违反自己写的 if-then 规则时**触发提示
  │  - 不是每笔交易都打断（避免 alert fatigue）
  │  - 不是泛泛"你确定吗"（被忽略）
  │  - 而是"你今天写的是 X，但你正在做 Y"——这是 cold state 的他对 hot state 的他说话
  │  - 跨过 hot-cold empathy gap 的最有效方式（Loewenstein 2005 + Read 1998）
  │
[trading hours, 已下单]
  ├─ 必经动作 2：30 秒内 EMA 即时记录
  │  - 字段 ≤ 4（情绪状态 / 触发源 / 是否符合规则 / 一句话）
  │  - 时间窗口越短，retrospective bias 越小（§3）
  │  - 触发源是关键：微信群？图表？新闻？这决定下次拦截位置
  │
[end of day, cold state 重新到来]
  ├─ 简短复盘：今日规则执行率
  │  - 不是详细分析
  │  - 而是"今天违反了几次自己写的规则"
  │  - 这是周复盘的输入材料
  │
[weekly, cold state]
  └─ 周复盘：调整下周 if-then 规则
     - 基于本周即时记录的累积
     - bias 类型识别（与 §06 wise feedback 配合）
     - 下周新承诺
```

### 7.3 入口位置的具体含义

**核心问题：σ 系统的入口最适合放在用户工作流的哪个位置？**

> **U 级回答（标 U；保留 Design 决策空间）：**
>
> **入口不是单一位置，而是三个位置的组合**——其中两个是**必经之路**，一个是**用户主动**：
>
> 1. **早晨开盘前的"规则书写"**（必经之路 + 用户主动）—— 最关键的入口。
>    - 物理上：σ 系统 = 早晨打开交易工作台之前必须经过的一道门。
>    - 形态上：可以是浏览器主页 / 桌面 dashboard / 启动脚本 / 手机锁屏待办——只要是用户**已经会做的动作**（如打开浏览器、解锁手机）就**自然必经**这道门。
>    - 内容上：今天的 if-then 决策链（不是开放问题，是结构化承诺）。
>    - 这一步落地的位置应当**最小依赖技术栈选择**——文档、网页、App 都可以，关键是"必经"。
>
> 2. **交易工作台旁边的"规则提醒浮窗"**（必经之路，但被动触发）—— 第二关键。
>    - 物理上：桌面浮窗 / 浏览器扩展，**仅在用户即将违反自己今早写的规则时**触发。
>    - 形态上：必须**轻量、可无损跳过**（避免 reactance），但**信息够刺痛**（cold-state 的你写给 hot-state 的你）。
>    - 移动端**不强求**——接受物理边界。
>
> 3. **下单后 30 秒的"即时记录"**（用户主动，但极短）—— 第三关键。
>    - 物理上：独立 App / 网页表单 / 浮窗。
>    - 形态上：≤ 4 字段，30 秒可填完。
>    - 不追求"必经"——只追求"足够近、足够快"，让 EMA 而非 retrospective。
>    - 当用户没填时，**不强制**——不填本身是数据（"这一笔可能就是冲动交易"）。
>
> **不放在工作流里的位置**：
>
> - **下单按钮前的强制审议**（× 弹窗形态）：违反 §6.3 alert fatigue。
> - **每次打开 App 强制问候**：reactance 风险高。
> - **周末长报告**（× 单独文档）：retrospective bias、留存差。
>
> **最危险的设计幻觉**：
>
> 期待用户**事后老实回忆冲动交易**——这是不可能的（§3.4 + §2.2 的合成证据）。**最危险的冲动交易必须由"前置规则 + 即时拦截"两道门一起拦**，事后记录无论如何都不可能补救漏掉的那部分。

### 7.4 这一节本身的限制

- 上述设计是基于已有证据的**最佳赔率组合**，不是"已知有效"——任何具体设计都需要**用户行为验证**。
- 用户是单一个人（trader 训练系统），样本 n=1，无法跑 RCT。
- 因此**必须依赖周复盘 + 即时记录数据本身**作为反馈回路。
- "三个入口位置"的具体技术形态（浏览器扩展 / Electron / 独立 App / Notion 等）**故意没有指定**——这是 Phase 2 接下来的子任务（基础设施 / 工程选型）的事，本调研只回答"在哪里"和"形态约束"，不回答"用什么技术做"。

---

## 八、本笔记的局限

### 8.1 证据等级的不平衡

- **S 级证据**集中在认知心理学（task switching, attention residue, EMA）和健康行为（implementation intentions, JITAI）。这两个领域的证据基础较厚。
- **M 级证据**集中在 FCA / NBER 的交易行为研究。这部分证据虽然质量高但样本通常是 broad retail，不一定适用于"小白训练交易员"这个特殊人群。
- **W 级标语 / 灰色文献**普遍存在于"context switching cost"的工业讨论中——"23 分钟"是典型例子。本笔记尝试对所有标语溯源，但仍可能有 W/U 级断言混进 S 段落。读者请按"证据等级"重新加权。

### 8.2 直接证据的缺口

**完全缺失或证据极弱的命题**（U 级，需要谨慎）：
- "在 σ 决策链场景下"具体的 switch cost / attention residue 量化数据——没有交易场景的实验。
- 浏览器扩展类工具在**交易**场景的 RCT——没有公开的此类研究。
- "强制规则书写"对**单一交易者**的长期行为改变——n=1 设计，本质上是案例研究。
- 中国 A 股散户在 PC + 移动双端的真实切换路径数据——只能通过 WeChat / 同花顺等公开数据推断。
- 微信群 → 下单的真实时间窗口分布——完全没有公开数据，本笔记的"5–30 秒"是 U 级估计。

### 8.3 文化 / 语言偏向

- 主要文献基于英语世界，A 股散户的实际工作流主要靠中文媒体推断（同花顺/东财数据来自财富号、新浪财经）——这一部分可信度低于其他部分。
- 中国监管环境下"商品期货 / A 股 / 港股"用户行为差异可能很大——本笔记没有区分。

### 8.4 调研者偏向（self-disclosure）

- 调研者（这个 AI 助手）有可能偏向"能说出明确结论的方向"——例如倾向于得出"前置规则 > 事后记录"这种工整结论。
- 真实情况可能更模糊：**很多用户在事后记录中也能成长**——只是过滤掉了冲动交易这一类。
- 本笔记的"σ 系统的入口最适合放在哪里"是**赔率较好的猜测**，不是**唯一正确答案**。
- 本笔记**未经多模型 review**——它本身需要 Phase 2 的 review 流程检验。

### 8.5 没有覆盖的维度

- **用户长期意愿衰减**：早晨规则书写在第 1 周容易，第 4 周不容易——本笔记没有探讨"必经之路"本身的弃用率。
- **隐私 / 监管**：交易数据本身的法律含义（A 股、期货账户合规要求）。
- **协作 / 社交**：σ 是否考虑分享给同伴——这是 §02 笔记 Friends with Health Benefits 触及但本笔记没有展开。
- **多账户 / 多市场**：用户在 A 股 + 港股 + 期货同时活跃时，决策链如何统一。

### 8.6 与其他调研笔记的关系

- §01（journaling evidence）：本笔记继承"自报告 + 时间投入是头号弃用原因"的 S 级证据。
- §02（retail failure）：本笔记继承"FCA DEP / Robinhood 数据"的 M 级证据。
- §03（AI coaching）：本笔记没有探讨"AI 反馈何时介入"——这是 σ 系统的另一根支柱，本笔记 silent。
- §04（deliberate practice）：本笔记的"早晨规则书写 + 周复盘"与刻意练习框架一致，但本笔记没有详细展开 deliberate practice 的具体协议。
- §05（alternative paradigms）：本笔记没有探讨"完全不用 App"的极端方案（如手账 / mentor 制）——这是 §05 已经覆盖。
- §06（tool design / retention）：本笔记是 §06 的"物理路径"侧的延伸——§06 主要回答"什么会导致弃用"，本笔记回答"什么位置可以避免被绕过"。

---

## 附录 A：核心引用一览（按证据等级）

### S 级（同行评审 / 系统综述 / 大型 RCT）

1. Rogers, R. D., & Monsell, S. (1995). *J Exp Psychol Gen*, 124(2), 207-231.
2. Monsell, S. (2003). *Trends in Cognitive Sciences*, 7(3), 134-140.
3. Kiesel, A. et al. (2010). *Psychological Bulletin*, 136(5), 849-874.
4. Leroy, S. (2009). *OBHDP*, 109(2), 168-181. — attention residue。
5. Masicampo, E. J. & Baumeister, R. F. (2011). *J Pers Soc Psychol*. — open loops / Zeigarnik。
6. Mark, G., González, V. M., & Harris, J. (2005). *CHI 2005* — No Task Left Behind?
7. Mark, G., Gudith, D., & Klocke, U. (2008). *CHI 2008* — Cost of Interrupted Work。
8. Czerwinski, M., Horvitz, E., & Wilhite, S. (2004). *CHI 2004*。
9. Cutrell, E., Czerwinski, M., & Horvitz, E. (2001). *Interact 2001*。
10. Iqbal, S. T., & Horvitz, E. (2007). *CHI 2007*。
11. Trafton, J. G. et al. (2003). *Int J Human-Computer Studies*。
12. Altmann, E. M., & Trafton, J. G. (2002). *Cognitive Science*。
13. Parnin, C. & Rugaber, S. (2009). *ICPC 2009*。
14. Shiffman, S., Stone, A. A., & Hufford, M. R. (2008). *Annu Rev Clin Psychol*, 4, 1-32. — EMA 经典综述。
15. Maes, I. et al. (2022). *Perspectives on Behavior Science* — EMA validity 系统综述。
16. Wenze, S. J. & Miller, I. W. (2010). *Clinical Psychology Review*。
17. Cain, A. et al. (2024). *J Person-Oriented Res* — retrospective vs EMA 个体差异。
18. Hardeman, W. et al. (2019). *Health Psychology Review* — JITAI 综述。
19. Klasnja, P. et al. (2018). *JMIR mHealth* — 微随机化 RCT。
20. Bossaerts, P. et al. — EPFL Infoscience — trading under time pressure。
21. Lo, A., Repin, D. (2017). *Frontiers in Neuroscience* — trader fMRI。
22. Zaghloul, K. A. et al. (2018). *eNeuro* — subthalamic nucleus 风险预测。
23. Loewenstein, G. (2005). *Health Psychology* — hot-cold empathy gap。
24. Read, D. & van Leeuwen, B. (1998). *OBHDP* — appetite & delay。
25. Gollwitzer, P. M. & Sheeran, P. (2006). 系列 meta — implementation intentions（d ≈ 0.65）。
26. Sheeran, P., Listrom, & Gollwitzer (2024). *European Review of Social Psychology* — 642-study meta。
27. Aslett, K. et al. (2022). *Sci Adv* — NewsGuard NYU 实验。
28. Mark, G. et al. (2018). Microsoft Research — blocking distractions。
29. Patterson, R. (2020). Cornell — MOOC commitment device RCT。
30. Lukoff, K., Lyngs, U., Alberts, L., Hiniker, A. (2022). *CHI 2022* — DSCT autonomy。
31. Buzinski, S. & Price, M. (2015). *PSPB* — Don't Tell Me What to Do。
32. Sunstein, C. R. (2019). *Duke Law Journal* — Sludge and Ordeals。
33. Sunstein, C. R. (2021). *Behavioural Public Policy* — Sludge audits。
34. Moser, C. et al. (2019). *CHI* — Impulse buying / e-commerce friction。
35. Phansalkar, S. et al. (2014). *JAMIA* — alert override。
36. Page, N. et al. (2017). *JMIR Med Inform* — alert fatigue 系统综述。
37. Bryan, M. et al. (2022). *JAMIA* — habit and automaticity in alert override。
38. John, A. (2020). *Management Science* — commitment device backfire。
39. Carrera, M. et al. (2022). *Review of Economic Studies* — who chooses commitment。
40. Godden & Baddeley (1975). *British J of Psychology* — context-dependent memory（注：2021 Murre 复制失败）。
41. Wood, W. & Neal, D. T. (2007). *Psychological Review* — habit interface。
42. Pratap, A. et al. (2017). *IMWUT* — large-scale phone usage。
43. Mental health JITAI meta-analysis (2025). *BMJ Mental Health*。
44. Kalda, A. et al. (2021). NBER w28363 — Smart(Phone) Investing。
45. Barber, B. M., Huang, X., Odean, T., & Schwarz, C. (2022). *Journal of Finance* — Robinhood 注意诱导。

### M 级（监管 / 大型行业数据 / 工作论文）

1. FCA Occasional Paper 66 (2024) — Digital Engagement Practices。
2. FCA Research Note (2024) — 9000-person trading experiment。
3. CFTC (2024) — Retail Traders Futures。
4. Robinhood Q4 2025 投资者材料（12 min/DAU、DAU/MAU 数据）。
5. 同花顺 / 东方财富 / 涨乐财富通 MAU 数据（来源：2025 中国证券服务 APP 监测报告）。
6. WeChat / 雪球 trading 影响相关 *Physica A* / *Humanities & Social Sciences Communications* 文章。

### W 级（行业博客 / 营销）

1. HBR (2022) "How Much Time and Energy Do We Waste Toggling Between Applications?" — Qatalog & Cornell。
2. tradingjournal.com Trustpilot 1,201 评论分析。
3. tradelens.vip "Why You Keep Losing Trades" — 10,000+ 日志数据声称（厂商）。
4. tradesviz "State of Journaling 2024"。
5. Microsoft / Floaty / Mewayz 等行业博客数据。

### U 级（本笔记的逻辑推演）

1. "冲动交易种子→下单可短至 5–30 秒"——基于 1 秒决策风险盲（Bossaerts）+ Robinhood 移动行为研究 + 微信群影响研究的合成。
2. "拦截窗口的 sweet spot 在 hot state 形成前"——基于 §4 全部证据的合成。
3. "三个入口位置的组合"——基于 §1–6 的逻辑组合，尚无直接 RCT。
4. "对自我认知不清的新手，强 commitment device 可能锁住错误目标"——基于 Carrera 2022 + 用户特征的推断。
5. "高情绪 / 高冲动倾向者的 retrospective 偏差最大"——基于 EMA 文献的逻辑外推，未有直接 trader 研究。

---

## 附录 B：与其他笔记交叉引用

- §01（journaling evidence）：本笔记 §3 与 §06 的"自报告无外部验证"主题强相关。
- §02（retail failure）：本笔记 §2 引用 FCA / NBER / Robinhood 的同一组数据。
- §03（AI coaching）：本笔记 §6 的 wise feedback 概念在 §03 已经详细展开。
- §04（deliberate practice）：本笔记 §7 的"周复盘"与 §04 deliberate practice 协议一致。
- §05（alternative paradigms）：本笔记接受了"工具不一定是 App"的边界。
- §06（tool design / retention）：本笔记是 §06 在"物理路径"侧的延伸。

---

> **元规则承诺**：本笔记的所有论述按 S/M/W/U 标注。"诚实标记"在三处使用：(a) "23 分钟"标语未在 Mark 原文找到；(b) "5–30 秒冲动种子→下单"是 U 级合成；(c) "三个入口位置组合"是基于已有证据的最佳赔率猜测，不是已知正确答案。
>
> 所有 S 级引用都尽量给到作者-年份-期刊；所有 M 级数据给到机构或研究项目；W 级数据明确标为行业灰色；U 级合成在每节末或附录 A.U 集中标识。
>
> 本笔记**不修改** `foundation_2026.md`，**不修改**其他 notes，**不 commit / push**——按用户指令，唯一动作是创建 `research/notes/11_context_switching_cost.md`。
