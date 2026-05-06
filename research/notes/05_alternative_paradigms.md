# 交易者成长的替代范式调研

> ⚠️ **状态标注（v5 新增）**：本笔记反映**调研当时的中间结论**。最终系统约束以 [`foundation_2026.md`](../foundation_2026.md) **最新版本（v5+）** 为准。本笔记内容不再修改，作为历史可追溯档案保留。
>
> 调研日期：2026-05-05
> 调研方法：Web 检索（同行评审期刊优先 + 监管数据 + 大型纵向数据集 + 关键作者著作）
> 上下文：本笔记是 σ+α 双引擎设计（手动日志 + AI 教练 + 决策链 + 凯利仓位）的"竞争范式审视"。前四份调研已确立日志（01）、散户失败（02）、AI 教练（03）、刻意练习与元认知（04）的证据基线。本份回答的是：**当前设计是不是站在最强证据的方向上？是不是有被忽视的更优范式？**
> 证据等级：S（同行评审）/ M（专业数据/监管/工作论文）/ W（行业博客/营销/二手转述）/ U（基于已知文献的逻辑推演）

---

## 摘要（直接结论先行）

**1. 最强证据的路径是"被动投资"，不是"训练成为优秀交易者"。** 证据等级 S+。SPIVA 截至 2024 年末的 24 年数据显示：15 年区间内，**任何主动管理基金类别都没有超过半数能跑赢被动指数**（S&P Dow Jones Indices, 2024）。零售直接交易方面，巴西 (Chague & Giovannetti, 2019/2020) 持续 300 天以上的日内股票交易者 91% 亏损、期货交易者 97% 亏损；ESMA 监管数据：71.6% 零售 CFD 账户亏损（部分券商 89%）。这是迄今证据等级最高的事实。**任何"训练散户成为优秀交易者"的系统，都必须先承认自己在挑战一个被高质量证据高度怀疑的目标**。

**2. 但这不意味着 σ+AI 系统应该被替换为被动投资——这取决于用户的真实目标。** 如果目标是"用最少认知成本最大化期望终值"，被动投资几乎是最强选择。如果目标是"通过严肃实践训练自己的决策能力 + 心理纪律 + 不确定性容忍度"——被动投资完全无法提供这些训练负载。AGENTS.md 里的用户定位（"小白起步，认知驱动，目标成为优秀交易者，AI 是伙伴而非工具"）是后者，不是前者。**因此当前系统的合法性建立在"认知工程目标 ≠ 财富最大化目标"上**——这点必须在 system_spec_v2.md 里更明确写出来，否则会用 EV 框架批判 σ 引擎是不公平的。

**3. 对当前 σ+AI 设计威胁最大、最值得重视的替代/互补范式是：**
   - **互补（应该集成）**：单一 setup 聚焦（Q7，S 证据：变异度小、反馈环更紧）；HRV 生物反馈（Q3，S 证据：vmHRV 与决策质量相关，单次会话可改善执行注意力）；扑克式过程-结果分离思维 / Annie Duke "resulting" 警惕（Q5，S 证据，与决策链可融合）；公开承诺与社会问责（Q12，S 证据，d 中等但稳定）。
   - **替代候选（用户应当主动选择是否走）**：纯规则化系统交易（Q1，证据混合：基础设施回测过拟合 60%+ 失败率，但若用户能写代码且专注于风险控制则避开了行为偏误）；被动投资（Q6，最强证据）。
   - **应该警惕（弱证据 / 可能有害）**：纸上交易长时间替代真实交易（Q2，唯一严格研究显示模拟盘表现与真实交易表现负相关）；跟单（Q11，监管警告 + 心理副作用 = 增加风险偏好）；金钱激励先行（Q8，证据反向：高赌注下偏差更强而非更弱）；纯传统课程（Q9，CFA 在零售直接交易场景几乎无证据）。

**4. 当前 σ+AI 设计有 3 个严重的"空白盲区"是任何替代范式都不能修复、必须由设计本身解决的：**
   - **退出机制盲区**：系统没有内嵌"如果 6-12 个月后数据告诉你不应继续做主动交易，请系统化地切换到被动投资"的协议。这是诚实的最高形式——承认训练可能失败本身就是一种胜利。
   - **样本量盲区**：σ 引擎假设 20-100 笔交易后能用统计观察发现行为模式。但 5 bb/100 的扑克玩家需要 ~22,500 手才达到 1σ 置信；55% 胜率交易者需要 ~380 笔达到 95% 置信（TradeProb formula）。**当前的 50 笔阈值在统计上几乎完全是噪音**——用户和 AI 都会从噪音中"看到"虚假的模式。
   - **"诚实记录"激励盲区**：σ 引擎依赖手动诚实记录，但没有外部验证机制。所有有效的诚实激励研究（Q12）都依赖"被他人观察"或"金钱抵押"——AI 单方面信任用户的自我报告，是这一系统最脆弱的环节。

**5. 一个被严重低估的替代范式："quit gracefully"——把训练系统设计成可能输出"你应该停止主动交易"的系统。** 这个选择并未在原 13 个问题中被提出，但它在证据上的位置最强：Linnainmaa 的 Finland 数据显示亏损交易者会增加交易频率而不是退出；Brazilian/Taiwanese 数据显示 75-97% 的人在 1-2 年内退出，但**退出本身是被动发生的（亏光为止），而不是被系统主动建议的**。一个真正诚实的训练系统应当**主动建议用户在某些数据条件下停止训练**。

**6. 底线判断（对 system_spec_v2.md 的修正建议）：**
   - 保留 σ 引擎，作为"行为框架"而非"成为优秀交易者的工具"。重新定位 σ 的目标为："**让你在主动交易这件事上不被自己骗，并在数据告诉你应该停止时能听见**"——这是有强证据支持的（合规自我监控、implementation intentions、AAR）。
   - 在 Stage 0 之前增加 **Stage -2：被动投资基线**——用户的"不参与训练"的资产应当 100% 被动配置。这把"训练资金"和"长期财富资金"分开，用 Thaler 的心理账户研究作支撑（这是健康的 mental accounting）。
   - 在 σ 引擎里增加 **Stage 4：退出协议**——设定明确的退出条件（决策链遵守率 + 实际收益 + 主观痛苦三维），数据触发时强制讨论"是否切换被动"。
   - 单一 setup 聚焦（Q7）应作为 Stage 1 的强制选择项，而非可选——这是在 wicked 环境里把环境部分"驯化"为更 kind 的工程化操作。
   - HRV 监测（Q3）作为 Stage 2 升级项加入，先做趋势观察（"你的 HRV 在亏损序列后下降几天？"）而非实时干预。
   - 删除"把日志做大做全"的隐含目标——证据告诉我们日志的核心价值是"被诚实记录"，不是"被精细记录"。10 个核心字段足够，超过 20 个会造成 reflection-as-task 的退化（01 笔记已论述）。

---

## 各范式分别评估

### Q1：纯规则化系统/算法交易（Systematic / Algorithmic Trading）

**核心假设**：把交易决策完全交给规则/代码，把人从执行环节移除，可以彻底绕开行为偏误这一核心问题。

**证据**：

【M 级】机构层面证据中等：Northern Trust (2024) 数据显示，过去三年（2022-2024）系统化策略在美国大盘股上比主观策略多 20bp 净 alpha，波动更低。但这是**机构-机构**对比，不是"机构-散户"对比。散户能不能把这个优势复制到自己身上是分开的问题。

【M 级】**散户量化的真实失败模式**：
- Stanford 2025 研究：**58% 零售算法策略在上线 3 个月内崩溃**（来源：Stanford 研究，二手转述）。诚实标记：原文我没找到直接链接，应当当作 M 级而非 S 级。
- p-hacking 研究（Harvey & Liu, 2014/2015；Bailey, López de Prado et al., 2014）：测试 100 个指标变体，至少一个偶然"显著"的概率达 99.4%。**研究 200 万策略的 p-hacking 数据集（Yan & Zheng, 2017 SFI 工作论文）结论：单假设检验下大多数 outperformance rejection 都是假阳性**。
- Quantopian 数据：**8.3 万用户提交策略，最终被部署的极少数（具体百分比未公开）**。Quantopian 公司本身 2020-2022 年累计亏损约 270 万美元，2020 年关停策略市场。
- 实际案例：3.8R 期望、2.9 利润因子的回测策略在 10 周内崩塌至 -1.2R / 0.88 PF（Signal Pilot 案例文档，W 级，但与上面学术研究方向一致）。

【S 级】Bailey, Borwein, López de Prado, Zhu (2014, *Notices of the AMS*)：**The Probability of Backtest Overfitting (PBO) ≥ 50% 是常态**。回测 Sharpe ratio 对实盘 Sharpe 几乎没有预测力（R² < 0.025）。这是数学事实，不是观点。

【M 级】QuantConnect 平台数据：100,000+ 注册量化用户，47.7 万社区用户。但**没有公开的"用户真实收益分布"统计**——这是行业标准做法（不公开会让人难以评估）。已部署 Alpha Market 策略的成功因素是 Sharpe + CAGR，但这是"被订阅"成功，不是"赚钱"成功。

【M 级】行为偏误绕开的悖论：纯规则化交易移除了执行偏误，但**把偏误转移到了"规则设计"环节**——人在选择哪些策略上线时仍然 cherry-pick。López de Prado (2018) "The 7 Reasons Most ML Funds Fail"：散户量化最常见失败是"selection bias on backtest results"。

**证据等级**：M（机构系统化有效证据较强；散户系统化几乎全部证据指向高失败率）。

**与 σ+AI 的对比**：

| 维度 | σ+AI（主观+训练） | 纯规则化系统 |
|---|---|---|
| 行为偏误绕开 | 部分（依赖决策链遵守） | 高（执行环节无偏误） |
| 选择偏误 | 决策时即时存在 | 推迟到策略选择 / 上线决定 |
| 学习曲线 | 数月-数年 | 编程 + 量化基础 1-2 年 |
| 失败模式 | 不诚实记录 / 不遵守流程 | 过拟合 / 数据窥探 / 实盘崩溃 |
| 适合用户 | 愿意做认知工作的人 | 有编程基础 + 数学/统计训练 |
| 资本要求 | 可以从小开始 | 微合约 ≥$10K，标合约 ≥$25K |

**互补还是替代**：

主要是**替代**关系（思路完全不同），但**有一个互补点**：σ 引擎的"决策链"本质上是把"主观判断" partial 系统化——这是从主观向系统化的连续光谱上的中间点。Stage 3+ 自然演化路径可以是"决策链规则越来越显式 → 部分自动化 → 部分系统化"。

**适合谁 / 不适合谁**：
- **适合**：有 Python/编程基础、数学统计背景、能容忍 6-18 个月看不到结果、对策略研发本身感兴趣的人。
- **不适合**：当前 AGENTS.md 描述的"小白起步、认知驱动、A 股+港股+期货"用户。除了门槛过高，A 股的 T+1、涨跌停板、零售-机构信息不对称使得回测过拟合的概率比美股更高。

**已知失败模式**：
1. 过拟合的回测让用户对策略真实 Sharpe 形成虚假信心（PBO ≥ 50%）。
2. Survivorship bias 让"成功量化博主"的可见性远大于失败者。
3. 实盘维护成本（数据、API、监控、断线处理）通常被低估 5-10 倍。
4. 一旦策略失效，没有 σ 引擎那样的"我做错了什么"的认知反馈机制——只能继续找新策略，最终变成 strategy chasing。

**结论（对当前设计的影响）**：纯规则化系统不是"小白的更优路径"。但 σ 引擎的设计应该**显式承认这是另一条路**，并在用户出现编程能力 + 量化兴趣时给予升级路径建议，而不是把用户锁定在主观训练里。

---

### Q2：模拟盘 / 纸上交易（Paper Trading）

**核心假设**：通过无风险的纸上交易，可以建立 setup 识别和执行流程，在不亏钱的前提下完成训练，然后无缝转向真实交易。

**证据**：

【S 级】**唯一一项严格的转移效应研究**：Goldstein, da Costa & Yoshinaga (2024, *Journal of Behavioral Finance* 25(4): 436-448) "Trading Simulations and Real Money Outcomes"。研究设计：分析了同时拥有模拟账户和真实账户的巴西交易者数据。

**关键发现**：
- 模拟盘表现最好的人，**真实账户表现显著更差**（"significantly underperform"）。
- 在模拟中更活跃 / 风险更高的人，更可能开真实账户，但仍然亏损更多。
- 作者结论："Without proper education regarding the hazards of active trading and accurate performance evaluation, stock simulator users may draw incorrect inferences regarding their trading skill."

**这一项研究本身就足以颠覆"模拟盘是无风险训练"的常识**——它显示模拟盘是**误导性训练**，不是无效训练。

【S 级】Cornil, Hardisty, Bart (2022) "Stakes and Investor Behaviors"（SSRN 4219861）：**同一投资者在真实账户中比在模拟账户中表现更差、偏差更强**。即"赌注越高，认知越差"。

【M 级】Alpaca 内部数据：57.1% 的纸上交易者在 30 天内进入实盘，75.1% 在 60 天内。这表明**实践中纸上交易主要是"环境检查"，不是"长期训练"**——用户感知到了模拟盘的局限。

**为什么模拟盘的转移失败**：

1. **缺乏情绪压力下的反应训练**——而情绪压力是真实交易最重要的差异变量（Lo & Repin 2002 NBER 8508 显示情绪反应越强，真实交易表现越差；Steenbarger-Lo-Repin 2005）。
2. **滑点、流动性、点差失真**——模拟假设完美成交，真实可达 0.1-0.5%（极端 1-3%）的滑点。一个 1.5:1 的纸面 PF 在实盘可能塌缩到 1.1:1（业界数据，W 级）。
3. **"如果赔了"的诚实评估缺位**——你知道这是假钱，所以决策会更激进、止损更宽。这种"激进版本"的你形成的肌肉记忆，在真实交易中会过冲。
4. **过度自信诱发**——Cipriano et al. 2020 直接证据 + Goldstein et al. 2024 间接证据，**模拟盘的成功体验是过度自信的最佳燃料之一**。

**证据等级**：S（且方向罕见地与"主流建议"相反）。

**与 σ+AI 的对比**：σ+AI 系统当前没有强调模拟盘——这是正确的。但 system_spec_v2.md Stage -1 描述里写"我们不在这个阶段模拟或纸上交易（那属于 Stage 0 的训练内容）"——这暗示 Stage 0 会包含模拟盘训练。**这一点应该删除或修正**。

**互补还是替代**：当前证据指向**应当限制模拟盘的使用**，仅作为"工具熟悉"和"流程跑通"用途，绝不应作为"训练胜率"的工具。

**适合谁 / 不适合谁**：
- **适合**：第一次开账户的人，用 1-2 周熟悉下单界面、止损/止盈设置等机械操作。
- **不适合**：试图通过纸上交易建立"我有 60% 胜率"信念的任何人——这一信念在转入真实交易时会被破坏，且破坏方式是过度自信下的爆仓。

**已知失败模式**：
1. **过度自信诱导**——纸上交易完全让人忽略情绪因子。
2. **错误的样本估算**——纸上 100 笔交易的胜率与真实 100 笔的胜率分布不同（Goldstein 等已证）。
3. **拖延实盘**——用纸上交易作为"我还没准备好"的合理化，导致永远不进入真正的训练环境。

---

### Q3：生物反馈 / 生理监测（HRV / GSR / 瞳孔追踪 / 皮电）

**核心假设**：交易决策的质量与生理状态相关，通过监测和反馈生理信号，可以在偏误形成前进行干预。

**证据**：

【S 级】**Lo & Repin 系列（最经典）**：
- Lo & Repin (2002, NBER WP 8508)：10 个外汇/衍生品交易员，皮电 / 心率 / 呼吸 / 肌电与市场事件高度相关；交易经验越多，反应越克制（"systematic differences related to experience"）。
- Steenbarger, Lo, Repin (2005, *American Economic Review* P&P 95(2): 352-359) "Fear and Greed in Financial Markets: A Clinical Study of Day-Traders"：80 名日内交易员，5 周追踪情绪强度。**情绪反应越强烈的交易员，盈亏越差**。
- Andrade, Odean, Lin (2022 PLOS ONE) "Real-time extended psychophysiological analysis of financial risk processing"：55 名职业交易员，5 天 E4 腕带监测。**心率、血容脉搏、皮电与交易决策、市场波动、产品类型、经验都有显著相关**。

【S 级】**Interoception 与生存率**：Kandasamy et al. (2016, *Scientific Reports* 6:32986) "Interoceptive Ability Predicts Survival on a London Trading Floor"：**心跳感知能力越强的伦敦交易员，盈利越多、在市场存活时间越长**——这是"gut feeling"的硬证据。

【S 级】**HRV 与决策质量**：
- vmHRV（vagally mediated HRV）越高的人决策能力越好（多项研究汇总，Forte et al. 2021 PubMed 33672004）。
- Heart-brain inhibitory circuit 假说：HRV 反映前额叶抑制功能（Thayer & Lane 整合模型）。

【S 级】**HRV 生物反馈训练能改善决策（RCT 级证据）**：
- Pizzoli et al. (2023, *Frontiers in Psychology* 14:1292983)：单次 HRV 生物反馈对**高压力个体**的执行注意力有显著正向效应；对低压力个体无效。
- Salvador et al. (2022, *Scientific Reports* 12:6171) "Learned self-regulation in top-level managers through neurobiofeedback training improves decision making under stress"：**23 名高管 RCT。** 神经反馈训练显著改善 intertemporal 和风险决策。
- Tinello et al. (2022) 系统综述：56% 的研究报告 HRV 生物反馈对执行功能有显著正向效应；注意力是受益最常见的领域；脆弱人群（压力暴露、运动员、退伍军人、ADHD、老年）受益更明显。

【M 级】**消费级穿戴的可信度**：
- Nature Scientific Reports 2025 验证：**Oura Gen 4 vs ECG 黄金标准 CCC = 0.99；Whoop CCC = 0.94；Apple Watch、Garmin、Polar 略低**。
- 但这些设备的"daily score"（恢复评分等）变异较大，趋势分析比单点更可靠。

**证据等级**：S（多个独立路线汇聚证据，且包含 RCT）。

**与 σ+AI 的对比**：σ+AI 完全没有覆盖生理维度。但生理维度可能是 σ 引擎数据采集环节中**唯一具备"非主观可验证性"** 的来源——HRV 不会撒谎，日志会。

**互补还是替代**：**强互补**。可以集成进 σ 引擎，方式：
1. 每天上午监测 HRV / RHR baseline（穿戴自动）。
2. 决策链第 4 问"我现在是什么情绪状态" + 客观 HRV 数据双重记录。
3. 长期分析："你在 HRV 比基线低 20% 的日子里下单的胜率是多少？"——这是行为偏误检测的可量化升级。

**适合谁 / 不适合谁**：
- **适合**：愿意佩戴穿戴设备的人。门槛中等（Oura $349 + 订阅，Whoop $30/月，Apple Watch HRV 免费但精度略低）。
- **不适合**：对穿戴设备有反感（隐私、不适感）的人。但有替代方案——单独的 HRV 应用（HRV4Training, Welltory）+ 手机摄像头测量，免费。

**已知失败模式**：
1. **过度依赖单日数据做决策**——daily HRV 噪音很大，应当看 7 天或 30 天趋势。
2. **把生理数据等同于"我应不应该交易"的硬规则**——这是新一种 over-reliance 偏误。生理数据应作为"额外注意"信号，不是"否决权"。
3. **测量噪声**：消费级设备在某些条件下精度下降（运动后、咖啡因、生病）。

**对设计的具体建议**：Stage 2 加入"生理基线"模块，先做趋势观察 1-3 个月，再考虑实时干预。不应在 Stage 0 引入（增加摩擦、稀释焦点）。

---

### Q4：同伴 / 社群学习（Trading Rooms / Discord / Reddit / Mentorship）

**核心假设**：通过与其他交易者的互动、反馈、模仿和导师指导，可以加速学习并减少孤独学习的盲区。

**证据**：

【S 级】**社群学习对交易表现的整体效应是负向的**：
- Heimer, R. (2016, *Review of Financial Studies* 29(11): 3177-3209) "Peer Pressure: Social Interaction and the Disposition Effect"：social network 上的交互**强化处置效应**，而不是减弱。
- Han, Hirshleifer, Walden (2023, *Journal of Financial Economics* 150(1): 139-165) "Social transmission bias and active trading"：社会传输 bias 系统性增加积极交易，而积极交易降低收益（"Active trading and (poor) performance: The social transmission channel"）。
- Bursztyn, Ederer, Ferman, Yuchtman (2014, *Econometrica* 82(4): 1273-1301) "Understanding Mechanisms Underlying Peer Effects: Evidence from a Field Experiment on Financial Decisions"：**当同伴宣布近期收益时，受试者更可能买进相同股票，但这些股票后续表现差，新投资者比对照表现更差**。
- Liaukonyte & Žaldokas (2022, *Management Science* 68(4): 2961-2982)：异常社交媒体讨论度高的股票，散户在交易和组合层面均跑输。

【S 级】**WSB 具体证据**：
- ScienceDirect 2024：WSB 注意力高的瞬间建仓的散户实现 **−8.5% 持有期收益**（vs 平均正向）。投资者对愤怒/厌恶情绪的反应大于对分析建议的反应。
- INET Oxford 2021：WSB 上的资产讨论是自我延续的兴奋传播，独立于基本面。
- arXiv 2308.09485：WSB 论坛活动与资产收益的 Granger 因果（meme stocks）。

【S 级】**Mentorship 的证据更复杂**：
- 学术 mentorship（导师-博士生）的元分析：弱-中正向（Eby et al. 2008, *Journal of Vocational Behavior* 72: 254-267, d ≈ 0.15-0.30）。
- **但"交易导师"在零售层面没有同行评审证据**——所有数据都来自商业培训机构的内部宣传。
- ForexMentorPro 数据：Q1 2024 英国零售投资欺诈损失 £55.2M，社交媒体（Instagram/TikTok）是主要传播路径。**74-89% 零售外汇账户亏损，但教练几乎一律承诺盈利**——这是欺诈识别红旗。

【S 级】**"同伴影响" 部分子机制有正向效应**：
- Heimer 2016 的另一面：**特定社交网络（已知优秀的、严格审查的）可以减少处置效应** 9-10%（在卖出 paper gain 上的概率下降）。
- Han et al. (2022) "Social finance" 综述：sophistication 高的同伴对 unsophisticated 个体有正向 social learning 效应。

**证据等级**：S（系统证据指向社群学习的整体效应是**负向**，但子机制有微弱正向）。

**与 σ+AI 的对比**：

σ+AI 是孤独学习。社群是同伴学习。前者避开了 herding 但失去了外部诚实约束。

**互补还是替代**：**有限的互补**——但限制非常关键：
- ✅ 应当寻求一个"严肃记账互查的小群"（2-5 人），定期公开自己的日志和回测结果。这是 Q12 公开承诺的现实形式。
- ❌ 应当远离任何"群里推票"、"信号发布"、"实时跟单"为主要内容的社群。这些社群证据指向是负向的。
- ❌ 应当对"付费交易导师"持高度怀疑——除非他们公开自己实时账户的实盘对账单（不是"教学账户"）。

**适合谁 / 不适合谁**：
- **适合（结构化同伴互查）**：愿意公开自己交易数据的人，能找到 2-5 个相同水平、严肃的同伴。
- **不适合（推票群/导师）**：所有人，除非能严格甄别（监管、对账单、退款条款）。

**已知失败模式**：
1. **Herding/Mimetic**：你以为自己在"学习"，实际上是在跟单（Han et al. 2023 的核心机制）。
2. **Confirmation echo chamber**：群里都说要涨，没有声音说不涨。
3. **Mentor 是骗子**：业界普遍存在的失败模式。

**对设计的具体建议**：
1. σ+AI 应当增加一个**"同伴互查协议"**——每月把脱敏的决策链记录与一个互查搭档交换审视。这是 Q12 的现实化。
2. AI 应当**拒绝执行"跟单 / 推票"指令**——明确写在系统约束里。

---

### Q5：游戏化 / 模拟训练（Prediction Market / 扑克 / 游戏化干预）

**核心假设**：通过游戏化方式（更紧的反馈环、更明确的胜负、更低的真实风险）训练决策能力，再迁移回交易。

**证据**：

【S 级】**扑克作为"姊妹领域"的可迁移证据**：
- Levitt & Miles (2011, NBER WP 17023) "The Role of Skill Versus Luck in Poker"：**高技能扑克玩家 ROI +30%，其他玩家 −15%。** 即扑克是技能游戏。
- Annie Duke (2018) *Thinking in Bets*（Penguin Random House）：核心论点 — 决策质量 ≠ 结果质量；reasoned outcome 反推决策质量是 "resulting" 偏误。Duke 拥有 Cognitive Psychology PhD（UPenn）+ 世界扑克冠军。她的框架与 Mauboussin (2012) "The Success Equation"（HBS Press）的"运气-技能光谱"一致。
- Palomäki et al. (2020, *Journal of Expertise* 3(2)) "Cognitive and behavioral correlates of gambling-related cognitions and gambling behaviors among poker players"：扑克玩家的概率估算虽然非完美但 reasonably calibrated（Liley & Rakow 2010, *Journal of Behavioral Decision Making*）。

**核心洞察（U 级，基于上述证据的逻辑推演）**：扑克与交易在结构上近似（不完全信息、概率决策、情绪管理、bankroll management），扑克学到的两件事**直接迁移**：
1. **过程-结果分离**（Annie Duke "resulting" 警惕）。
2. **bankroll management** = 仓位管理。Solver 是扑克版的"凯利仓位计算器"。

**但有不可迁移的部分**：扑克有 GTO solver（明确的最优解），交易没有等价物。这意味着扑克学得到的"GTO 偏离了多少"在交易中无法直接套用。

【S 级】**Prediction market 训练（Tetlock GJP）**：
- Tetlock & Mellers et al. (2014) "Forecasting Tournaments"：CHAMPS-KNOW 训练能改善预测精度。
- **但 2025 年方法学质疑**：Hauenstein, Mellers, Tetlock (2025, *Psychological Science* 36(1)) 用 IRT 重分析，发现 method variance 控制后，训练效应被实质性削弱、消除甚至反转。**这意味着我们对"概率训练能让人变成 superforecaster" 的信心要下调一档**。
- 04 笔记已论述。诚实标记：训练不是无效，但效应量从"显著"降到"不确定"。

【S 级】**财务决策游戏化的混合证据**：
- Tinghög et al. (2023, *Journal of Behavioral and Experimental Finance*) "Impact of gamification on mitigating behavioral biases of investors"：**部分偏误（overconfidence、disposition effect）可被游戏化减少；部分偏误（familiarity、status quo）反而增加**。
- Nyhus et al. (2021) 财务素养游戏对秋决策能力有正向但短期效应；长期保留性差。

【M 级】**Top Gun / 高密度模拟训练**：
- Above-Real-Time Training (ARTT) 在飞行员训练中支持转移效应（Sage Publications 2012）。
- **但飞行员训练的环境是 kind 环境**（规则稳定、反馈即时、有标准答案）；交易是 wicked。这一可迁移性受限。

**证据等级**：S（扑克 → 交易的概念迁移强；游戏化整体训练效应弱）。

**与 σ+AI 的对比**：σ+AI 没有显式游戏化，但决策链 5 问的本质上是 Annie Duke 框架的 implementation。

**互补还是替代**：**强互补**。
- ✅ 引入扑克训练作为 Stage 0 / Stage 1 的辅助：每天玩 100-500 手 micro stakes 的扑克，每周用 solver 复盘 10 个关键手。这建立的是**概率思维肌肉**——比直接用真钱在市场上学便宜得多。
- ✅ 引入 Good Judgment Open 平台的预测练习——每周回答 5-10 个长期预测问题，校准概率估算。
- ❌ 不应把 σ 引擎本身游戏化（积分、勋章、排行榜）——这会扭曲诚实激励（Tinghög 2023 显示游戏化制造新的偏误）。

**适合谁 / 不适合谁**：
- **适合**：愿意把"训练"和"市场"分开的人。
- **不适合**：把"扑克玩得好"等同于"交易能玩得好"的人——技能迁移有限，扑克是补充训练，不是替代训练。

**已知失败模式**：
1. **过度游戏化扭曲动机**——把目标从"诚实记录"扭曲为"得高分"。
2. **扑克偏向技能 + 交易偏向运气** → 玩扑克时建立的"技能可控感"在交易中是错觉。
3. **Tetlock 训练效应在 IRT 重分析后弱化**——所以预测市场训练不能作为系统的核心。

**对设计的具体建议**：在 Stage 1 阶段引入"扑克 + 预测市场"作为辅助训练，但不计入 σ 引擎的核心指标。

---

### Q6：被动投资作为"放弃训练"的最优解（Passive Indexing）

**核心假设**：对绝大多数零售投资者，把钱交给宽基 ETF + 长期持有 是期望效用最大的选择。"训练成为优秀交易者"是一个负 EV 的赌注。

**证据**：

【S 级】**SPIVA Year-End 2024（24 年累计数据，最高质量）**：
- 65% 主动管理大盘股基金跑输 S&P 500（2024 单年），高于 24 年均值 64%。
- **过去 15 年区间内，没有任何类别有过半的主动基金能跑赢被动指数**。
- Survivorship bias：约 25% 主动基金在 5 年内关闭/合并，让事后比较更对主动有利——但即便如此，它们仍跑输。

【S 级】**散户直接交易**：
- Barber & Odean (2000) *Journal of Finance* 55(2): 773-806："Trading is Hazardous to Your Wealth"：高频散户年化跑输基准 ~10pp。
- Barber, Lee, Liu, Odean (2014, *Review of Financial Studies*) Taiwan day traders：**75% 在 2 年内退出**。
- Chague & Giovannetti (2019/2020, *Brazilian Review of Finance*) Brazilian day traders：**97% 持续 300+ 天的期货日内交易者亏损；91% 股票日内亏损**。
- Linnainmaa et al. (2020) "Learning, Fast or Slow"：**74% 日内交易量来自有亏损史的人；97% 日内交易者后续仍可能亏损**——即"经验"未让他们改变行为。
- Locke & Mann (2015) Aspiring Professional Traders：**只有 ~15% 的新交易员存活超过 1 年**；存活者主要学到的是"对风险更舒适"，而非"风险调整后表现"——后者无证据改善。

【S 级】**被动 ETF 的散户对比研究**：
- SSRN 4145537：持有被动 ETF 的零售投资者**风险调整收益更高**（虽然仍然为负）；重仓被动 ETF 的散户交易更被动、风险更低。

【S 级】**福利经济学视角**：
- AEA 2022 working paper "How Competitive Is the Stock Market?"：被动投资让需求弹性下降 11%，主动应对只抵消 ~2/3。**这意味着市场不会因为更多人选被动而变得"对主动更有利可图"**——这是一个常被忽视的反直觉证据。
- Vanguard "Setting the Record Straight" (2017, white paper)：低费率的复利效应使被动在长期成为期望最优。

【M 级】**财务素养训练效应**：财务教育 RCT 元分析（Kaiser & Lusardi 2021, 76 RCTs, 160K+ 参与者）：
- 知识效应：~+0.25-0.33 SD（中等）。
- **行为效应：~+0.05-0.07 SD（小）**。
- 即"学财商"比"改变行为"容易得多。这进一步指向：让用户**直接做被动**，比"教育用户成为好交易者"是更高 EV 的干预。

**证据等级**：S+（这是本调研中证据最坚实的一条）。

**对系统核心假设的挑战**：

如果用户的目标是"财富最大化"——证据强烈、几乎无歧义地告诉我们：**95%+ 的零售直接交易者都应当做被动投资**。"训练成为优秀交易者"在期望意义上是负 EV 的赌注，因为：
1. 你需要持续 5+ 年盈利才能确认你不是运气好（Mauboussin paradox of skill：投资中 3 年期 85% 是运气，15% 是技能）。
2. 单个 5 bb/100 的扑克玩家需要 22,500 手才达到 1σ 置信；同等水平的交易员需要更多笔交易，但实际只能交易 200-500 笔/年。
3. 这意味着**统计上，大多数主动交易者一辈子都无法在 95% 置信区间确认自己有 edge**——他们的"好年份"和坏年份分布与运气分布相同。

**但这不意味着 σ+AI 系统应当被废弃**——前提是用户的目标已经不是"财富最大化"。

AGENTS.md 中用户定位为"小白起步、目标是成为优秀交易员、认知驱动、不追求速成、追求可持续的成长"。这个目标里**财富不是核心，认知成长是核心**。如果你认真对待这个定位：
- σ+AI 是"通过交易行为训练自己的决策能力"——它是一种**自我教育投资**，不是"赚钱投资"。
- 这一框架内，被动投资无法替代——它不提供训练负载。

**互补还是替代**：取决于目标。
- 如果目标 = 财富最大化 → 被动是替代，σ+AI 应当被弃。
- 如果目标 = 认知成长 → 被动是**互补**：用户的"非训练"资金（生活储蓄、退休资金）应当 100% 被动；用户的"训练资金"（被定义为"愿意完全亏掉的、用来学习的钱"）才进入 σ+AI 系统。

**适合谁 / 不适合谁**：
- **适合（被动）**：所有零售投资者的"主资金"。
- **不适合（被动）**：把交易作为认知训练工具的人——但他们的"训练资金"必须是被显式划分出来的、可承受全损的部分。

**已知失败模式**：
1. **Bogleheads 教条主义**：把"被动 = 唯一对的"扩展到"任何主动尝试都是道德错误"——这忽视了人类的认知发展需求。
2. **DCA 神话**：DCA 在 ⅔ 时间下不如一次性投入（Bogleheads wiki 自己承认）。
3. **被动 ≠ 无风险**：仍然受市场系统性下跌影响（如 2008、2020、2022），用户需要心理准备承受 -50% 的回撤。

**对设计的最重要影响**：

**新建议：在 Stage 0 之前增加 Stage -2"被动基线 + 训练资金分离"协议**：

- 用户必须先把财富的 80%+ 配置到被动 ETF（具体比例因风险承受度调整）——这是"long-term 资产"。
- 剩余 ≤20% 才进入 σ+AI 训练，且这部分资金必须**显式被定义为"完全可亏的"**——心理账户上视同学费。
- system_spec_v2.md 应当把这一点写为"诚实声明"，**与"我们要训练你成为优秀交易者"并列**：你大概率不会成为优秀交易者；这个系统的设计是为了在你失败的时候让失败可控、有学习价值，并在数据告诉你应该停止时让你能停止。

这一修改不削弱系统设计，反而让它更诚实、更稳健。

---

### Q7：单一技能聚焦训练（Single Setup Specialization）

**核心假设**：与其作"全能交易者"，不如选定一种特定的 setup（如日内跳空回补、周线突破、特定行业事件驱动），重复练到熟练，再决定是否扩展。

**证据**：

【S 级】**特定 vs 多样化练习的研究**：
- Kornell & Bjork (2008) "Learning concepts and categories: Is spacing the 'enemy of induction'?" *Psychological Science* 19(6): 585-592：**varied practice 长期保留更好但短期效率低**。
- Lavancier et al. (2020) JEP HPP "Specific Versus Varied Practice in Perceptual Expertise"：specific practice 训练中提升更快、近迁移更强；varied practice 长期更稳。
- *Royal Society Open Science* (Schöllhorn 2017) 体育领域：specific 短期效率高，varied 长期可迁移性强。
- Güllich et al. (2022, *Perspectives on Psychological Science*) 元分析 6,096 名运动员：**世界级运动员更常有 diverse 早期背景，少有 early specialization**。但需要注意——这是 elite 长期，不是初学者-1 年的尺度。

**对交易的应用解读（U 级，逻辑推演）**：
- 在 wicked 环境（交易）下，"varied practice 长期更好"的结论可能不直接适用——因为交易反馈延迟严重，varied 让你在每个 setup 上都不够样本量去看清。
- specific practice 在交易里有一个独特优势：**把 wicked 环境部分"驯化"为 kind 环境**。一个特定 setup 有相对稳定的触发条件、相对清晰的结果（涨/跌触发止损或止盈），这是少数能让"刻意练习"在交易中有效的方式。

【M 级】**业界共识的实践证据**：
- Linda Bradford Raschke 95% 集中在 E-mini S&P 500 期货日内（macro-ops.com 案例）。
- Edgewonk 2024 数据声称："1-3 个 strategy 集中比多 strategy 者表现更好"——但来源是商业博客，应当当作 W 级。
- Mark Minervini SEPA 系统：单一 setup（trend template + VCP）。

**证据等级**：S（教育心理学层面）+ M（交易实践层面）。

**与 σ+AI 的对比**：当前 system_spec_v2.md 没有强制单一 setup。这是缺陷。

**互补还是替代**：**强互补**。
- ✅ 单一 setup 让 σ 引擎的样本量积累有意义——同一类交易的 50-100 笔比"什么都做"的 100 笔有更高的统计信噪比。
- ✅ 单一 setup 让决策链 5 问的变量更稳定——每次都问"这是不是一个 X setup"、"这次的 X 触发条件是否齐备"，比开放性"我为什么觉得要涨"更有训练价值。
- ✅ 单一 setup 是把 wicked 环境工程化为 kind 子环境的具体方法——是 Hogarth 框架的实操应用（详 04 笔记）。

**适合谁 / 不适合谁**：
- **适合**：愿意限制自己交易选择空间的人。
- **不适合**：因 boredom 或 missed opportunity FOMO 难以坚持限制的人——但这些人本身就不该做主动交易。

**已知失败模式**：
1. **Setup 选错**：选了一个真实 edge ≤ 0 的 setup，反复做反复亏。这是 σ 引擎的退出协议必须能识别的。
2. **过度专门化导致样本不足**：如果一个 setup 一个月只触发 3-5 次，需要 2-3 年才积累 100 笔——这远超大多数零售用户的耐心。所以"单一 setup"应当**限定在中频 setup**（每月 10-30 笔）。
3. **Setup 在某种市场环境下停止工作**——再好的 setup 在错的环境（regime change）下都可能 90 天内 PnL 崩塌，详见 02 笔记 retail failure。

**对设计的具体建议**：

**新建议：Stage 1 强制单一 setup 协议**：
- 用户在进入 Stage 1 时必须**显式声明**自己将专注的 1 个 setup（最多 2 个）。
- 决策链第 1 问从"论据是什么" → "这是不是一个 [setup name]？满足触发条件 1, 2, 3 中的几个？"
- σ 引擎的胜率 / 盈亏比统计**按 setup 分别计算**——这才有统计意义。

---

### Q8：金钱激励 vs 学习导向（Real Money vs Paper Trading 的扩展讨论）

**核心假设**：一开始就用真钱小仓位，"学费"驱动的真实损失会比模拟盘训练更有效。

**证据**：

【S 级】**真钱激励的反向证据**：
- Cornil, Hardisty, Bart (2022) "Stakes and Investor Behaviors"（已在 Q2 引）：**同一投资者在真实账户中比在模拟账户中表现更差、偏差更强**。
- 这与"金钱激励应当让人更专注"的常识相反——真实金钱触发情绪 / 厌恶损失等系统 1 反应，反而恶化决策。

【S 级】**心理账户研究的支持**：
- Thaler (1985) "Mental Accounting and Consumer Choice", *Marketing Science* 4(3): 199-214。
- Thaler & Johnson (1990) "Gambling with the House Money and Trying to Break Even": *Management Science* 36(6)：先赚后亏 vs 先亏后赚的处理差异——同样金额，"house money effect"让人更激进。
- 应用解读：把"训练资金"显式标记为"已经亏掉的钱"（mental accounting trick），可以缓解真实损失的过度情绪化。

【M 级】**Linnainmaa (2010-2011) Finnish data**：
- 投资者**初始用小仓位，盈利后扩大、亏损后缩小**。这是理性贝叶斯学习——但与之并行的是"trade to learn even when expecting losses"，即**人会为了学习自己的能力而坚持交易**，即便预期是亏损的。
- 解读：真钱小仓位有一个独特价值——它生成关于"你自己的"分布信息，而模拟盘不行。

**证据等级**：S（双向证据，复杂）。

**与 σ+AI 的对比**：σ+AI 没有明确推荐"真钱小仓位"——这是一个隐藏假设需要明确化。

**互补还是替代**：**互补**——但需要谨慎设计。

正确的"真钱训练"配置（基于 Q2、Q6、Q8 综合证据）：
1. **训练资金** = 用户净资产的 1-5%（因风险承受度调整）。
2. 这部分资金从立账户那一刻起就**心理账户上归零**——不是"我的钱"，是"我的学费"。
3. 单笔风险 ≤ 训练资金的 1-2%。这意味着每笔最大损失 = 净资产的 0.01-0.10%。
4. **这个数值小到不会引发情绪反应，但真实到能产生反馈**。

**适合谁 / 不适合谁**：
- **适合**：能承受 1-5% 净资产损失而不影响生活的人。
- **不适合**：把全部储蓄投入"训练"的人——这不是训练，是赌博。

**已知失败模式**：
1. **训练资金扩大化**：尝到甜头后把更多钱挪进训练资金。这是 Linnainmaa Finnish data 的负面表现。
2. **训练资金亏完后不停止**：用主资金"补回来"——这是 95%+ 散户最终爆仓的具体路径。
3. **训练资金过小到没反馈**：单笔 1-10 元的损失对成年人几乎无情绪反应——失去了真钱的一个核心训练价值。Cornil et al. 的研究暗示，**金额必须"足够大到能让你不爽，但不会让你失眠"**——具体到收入，可能是单笔 $50-$500 的损失带宽。

**对设计的具体建议**：在 Stage 0 加入"训练资金边界"协议——明确数字、心理账户标记、单笔损失上限。

---

### Q9：传统教育（CFA / FRM / EPAT / 大学课程）vs 自学

**核心假设**：系统化的金融教育能让人成为更好的散户。

**证据**：

【M 级】**CFA 在零售直接交易上几乎没有证据**：
- 所有研究都是关于 CFA 持有人作为**基金经理 / 卖方分析师**的表现，而不是散户：
  - Andersson 1994 (FAJ)：CFA 管理基金风险更高、更分散，但与非 CFA 基金的差异不显著。
  - De Franco & Zhou (2009) *The Accounting Review*：CFA 分析师推荐表现更好。
  - Morningstar (2017) 57,512 新基金：CFA 经理更高 flow、更好结果。
  - 但这些研究的人群（机构 buy-side / sell-side）与"零售散户做主动交易"是**完全不同的市场结构和约束条件**。
- **CFA 课程内容（伦理、投组、估值、固收、衍生）几乎不覆盖"如何做主动短线交易决策"** ——即使学完，对零售短线交易的直接帮助有限。

【S 级】**财务教育对行为改变效应弱**：
- Kaiser & Lusardi (2021) 元分析（已在 Q6 引）：行为效应 +0.05-0.07 SD。即使学完，行为变化微小。

【M 级】**EPAT / Coursera 量化课程**：
- 没有独立验证学员是否变得盈利。商业课程几乎不做这种验证（出于商业利益）。
- QuantInsti EPAT 的"成功故事"页面是 W 级营销材料。

【S 级】**自学路径的成功率**：
- 没有干净数据。但 Brazilian / Taiwanese 数据显示零售散户的整体失败率不区分"学过课程"vs"没学过"。
- Wharton/UPenn Knowledge Center 的散户研究反复指出：**信息差不是核心瓶颈**——这意味着"获取更多专业教育"也不是核心解药。

**证据等级**：M（间接证据较强；散户直接交易场景几乎无证据）。

**与 σ+AI 的对比**：σ+AI 是"行为训练"，传统课程是"知识传授"——前者是 04 笔记主导的方向，后者主要是补充。

**互补还是替代**：**有限互补**。
- ✅ 用户应当在 Stage 0 之前完成最基础的"市场结构 + 基础术语 + 风险管理 + 估值方法"知识——这就是当前 glossary.md 的设计目标。已在 Stage -1 完成。
- ❌ 系统化课程（CFA 三级、FRM、EPAT）对零售散户来说**投入产出比低**：成本数千美元 + 数年时间，但行为效应仅 +0.05-0.07 SD。
- ✅ 学习"市场如何运作"（机构行为、做市、监管、税收）的零成本资源（专业书籍 + 监管报告）足够 90% 的散户需求。

**适合谁 / 不适合谁**：
- **适合**：想转行进入买方/卖方机构的人——这时 CFA 是行业准入门槛信号，与个人交易能力无关。
- **不适合**：作为零售直接交易盈利提升手段的人——证据告诉我们这不是这条路。

**已知失败模式**：
1. **Credentialism 谬误**：以为有 CFA = 能赚钱。证据反向。
2. **Sunk cost**：花了 $5K 学 EPAT 后，因不愿承认沉没成本而坚持做不擅长的量化。
3. **课程信息为主导**——而 wicked 环境下信息不是核心瓶颈，行为才是（Kaiser & Lusardi 2021）。

**对设计的具体建议**：保持当前 glossary.md 的轻量级 + 用户驱动路径。不强制添加任何课程要求。

---

### Q10：时序性结构（学习路径设计）

**核心假设**：学习的顺序至关重要——某些技能应当先于另一些技能学习，错误的顺序会显著降低学习效率甚至阻断学习。

**证据**：

【S 级】**Order effects 的存在性是确立的**：
- Ritter, Nerb, Lehtinen, O'Shea (eds.) (2007) *In Order to Learn: How the sequence of topics influences learning*, Oxford University Press。汇总跨领域证据：顺序影响学习速度、最终水平、有时甚至是否能学会。
- Renkl (2014) "Toward a model of worked example use" *Educational Psychologist*：worked example → fading prompts → independent problem solving 的顺序在数学/物理类领域有强证据。

【M 级】**对交易的特定顺序，没有 RCT**：
- 行业普遍说"先学心理 → 后学技术"或"先学风险 → 后学策略"，但这些都没有 RCT 验证。
- σ+AI 的"先建 σ 后建 α"是一个有逻辑的设计选择（详见 system_spec_v2.md），但不是经验证过的"最优顺序"。

【M 级】**Curriculum learning 在机器学习中的证据**：
- Bengio et al. (2009) "Curriculum learning"：从简单到复杂的训练顺序，能改善神经网络收敛速度和最终性能。但这是 ML 类比，不是直接证据。

【M 级】**学习曲线的"高原"现象**：
- 04 笔记已论述：技能习得有"OK plateau"——超过该平台需要刻意练习模式的转换。
- 应用：交易学习里"我不再变好了"是常态，应当是**预期之内**的，不是"我有问题"的信号。

**证据等级**：S（顺序效应一般原则）+ M（具体顺序在交易中无证据）。

**与 σ+AI 的对比**：当前 σ+AI 已经做了"σ 先 α 后"的顺序安排，并明确说这是逻辑推演。

**互补还是替代**：σ+AI 的 Stage -1 → Stage 0 → Stage 1 → ... 框架本身就是一个时序性结构，符合证据。

**核心建议（基于本次调研的整合）**：

最强证据支持的训练顺序（综合 Q1-Q13）：

1. **Stage -2（新建）**：被动投资基线 + 训练资金分离协议（基于 Q6 + Q8 证据）。
2. **Stage -1（已有）**：术语 + 风控规则 + 认知基线确认。
3. **Stage 0（已有）**：决策链 + 日志 + 仓位算法 + AI 守门。
4. **Stage 0.5（新建）**：单一 setup 选择 + 限制（基于 Q7 证据）。
5. **Stage 1**：σ 引擎完整运转 + 行为偏误检测（基于 04 笔记 + 现有设计）。
6. **Stage 1.5（新建）**：扑克 + 预测市场训练辅助（基于 Q5 证据）。
7. **Stage 2**：α 引擎介入（环境识别 + 资金流向） + HRV 监测（Q3）。
8. **Stage 3**：完整 α + σ 整合 + 数据驱动迭代。
9. **Stage 4（新建）**：退出协议 / 升级协议 / 转向被动协议（基于 Q6 + Q12）。

【M 级】**何时引入哪个组件的证据**：
- 决策链早 / 仓位算法早：implementation intentions d=0.65 在习惯形成早期效力最强（Gollwitzer & Sheeran 2006）。
- 复盘要靠样本：低于 50 笔的"行为模式分析"是噪音；50-100 笔后才有统计意义；500+ 笔后才接近 95% 置信。

**已知失败模式**：
1. **顺序变形**：用户跳过 Stage -2 直接全仓主动 → 心理账户混乱 → 系统失效。
2. **过度滞留**：Stage 0 滞留超过 6 个月，用户失去动力。这与 04 笔记的 attrition 数据吻合（前 100 天流失 70%）。
3. **过度推进**：跳到 α 引擎前未建立 σ 习惯——是 system_spec_v2.md 已经预见的失败。

---

### Q11：完全外包 / 跟单（Copy Trading）

**核心假设**：跟随专家的交易可以"绕过"自己的训练，逐步内化好交易者的决策。

**证据**：

【S 级】**跟单的整体心理副作用**：
- Apesteguia, Oechssler, Weidenholzer (2018) "Copy Trading", *Management Science* 64(12): 5772-5784：**显示他人成功信息会显著增加风险承担，跟单功能让效应更强**。结论："Copy trading platforms may lead to excessive risk taking and reduce ex ante welfare."
- Doering, Neumann, Paul (2015) ...trust signals：跟单决策依赖 affective trust（情感信任）多于 cognitive performance signals——即用户跟单基于"觉得这个人靠谱"而非基于"他真的有 edge"。

【M/S 级】**跟单的真实表现**：
- Wikifolio + eToro vs S&P 500 (2024 master's thesis)：跟单组合表现与 S&P 500 **无统计显著差异**——意味着跟单没有 alpha。
- 业界估计 60-95% 散户跟单亏损（多个监管来源汇总）。
- Ammann & Schaub (2020) 分析 eToro 数据：所谓"Popular Investors" 的过往表现与未来表现相关性弱。

【S 级】**FCA / ESMA 监管立场**：
- FCA 已将"自动执行的跟单"分类为 portfolio management，触发 suitability assessment 等合规义务。这本身就是行业监管对跟单"非中性"的承认。

**证据等级**：S（整体跟单的心理副作用 + 监管负面立场）。

**与 σ+AI 的对比**：σ+AI 试图建立用户**自己的**决策框架。跟单是把决策外包。

**互补还是替代**：**主要是反向**——跟单削弱 σ 引擎的核心训练价值（用户没在做决策，自然没有"我为什么这样决策"的反思素材）。

**适合谁 / 不适合谁**：
- **适合（在受限条件下）**：用户已经决定做被动 + 长期 + 单一可信策略（如跟单某个稳定的低费率基金经理）——但这本质上是"间接被动"，不是"训练"。
- **不适合（作为训练）**：所有想成为优秀交易者的人。

**已知失败模式**：
1. **过度自信传染**：跟单成功 → 误以为自己理解了 → 自己开始独立做 → 没有训练基础 → 爆仓。
2. **领头交易者风格漂移**：你跟单的人改变策略而不通知。
3. **执行延迟**：你的成交价 ≠ 领头价，slippage 累计后实际表现 << 公开表现。

**对设计的具体建议**：σ+AI 应明确**禁止用户在 σ 引擎记录中混入跟单交易**——它们不是"自己的决策"，记录之只会污染统计。如果用户做跟单，应在另外的"被动账户"做。

---

### Q12：基于诚实标记体系的更激进设计（Public Commitment / Reputational Stakes）

**核心假设**：诚实记录是 σ 引擎的最脆弱环节。强化诚实激励能让系统更稳健。

**证据**：

【S 级】**Public commitment / reputational stakes 的效应**：
- Schwartzstein & Sunderam (2017, Management Science) "Observability Increases the Demand for Commitment Devices"：可观察性显著增加对承诺装置的需求——即人们知道自己被看见时会自我约束更强。
- Halpern et al. (2014) UCL 在线实验：**reputational commitment 在减肥实验中反而效应负向（结束体重高 1.5 kg）**——可能是 "commitment overload"。注意这是健康领域，不是认知领域。
- Giné, Karlan, Zinman (2010) "Put Your Money Where Your Butt is" CARES smoking cessation：**6 个月戒烟成功率提高 3pp，效应在 12 个月仍存在**。这是金钱抵押 + 承诺的强证据。
- StickK 平台数据：**金融 + 社交承诺组合最有效**——单纯一种效应弱。

【S 级】**Accountability partner 效应**：
- Friends with Health Benefits (Berkeley/Haas, *Management Science* 2024)：约朋友一起去健身的健身率 +35%。
- Partner2Lose RCT (BMC Public Health 2024)：减肥伙伴 vs 个人的 24 月效果**无显著差异**。
- 综合：accountability partner 效应取决于具体实施方式，效应中等且有上下界。

【S 级】**Accountability 在自由意志情境的效应**：
- Lerner & Tetlock (1999) "Accounting for the Effects of Accountability" *Psychological Bulletin* 125(2): 255-275：**accountability 提高决策质量，但仅在**:
  - 决策者有能力做更复杂分析时；
  - accountability 是 process accountability（你怎么决策的）而非 outcome accountability（你最终得到什么）。
- 应用：σ+AI 的决策链是 process accountability，方向正确。

**证据等级**：S（中等-强）。

**与 σ+AI 的对比**：当前 σ+AI 是 AI 单方面信任用户的自我报告——是"私人记账"模式，没有外部诚实激励。

**互补还是替代**：**强互补**——这是当前设计最严重的盲区之一。

**具体加强建议**：

1. **Stage 1 加入"互查搭档"协议**（结合 Q4 + Q12）：
   - 用户找一个同期做 σ 训练的搭档。
   - 每月互发脱敏的决策链记录 + 交易日志。
   - 互相质询："你这次说的论据真的成立吗？""你的情绪记录是事后填的还是事前填的？"
   - 这是 process accountability，符合 Lerner & Tetlock 框架。

2. **金钱抵押选项**（可选）：
   - 用户可选择把一定金额抵押到 escrow（StickK 风格）。
   - 触发条件：决策链遵守率连续 4 周低于 70%（即当前 system_spec_v2.md 的 Level 1 黄灯条件）。
   - 触发时金额捐给"反慈善" charity。
   - 这是 Giné et al. CARES 风格的强承诺装置——但应当作为可选项，不强制。

3. **诚实声明流程**：
   - 每月做"诚实标记盘点"——用户回顾本月的日志，识别"哪些条目我当时没有完全诚实"。
   - 这一行为本身就是 process accountability 的应用。

【U/M 级】**区块链/不可篡改记录的真实需求**：

- 区块链能解决"记录被篡改"问题，但**当前 σ+AI 的核心问题不是篡改，是不诚实记录（人在记录的瞬间就没诚实）**。
- 不可篡改不能解决"没诚实"——它只能验证"记下来之后没改过"。
- 因此区块链对当前问题不是核心解药。
- **真正的诚实保障是"被同伴/AI 实时观察"——这是 reputational commitment 的核心机制**。

**已知失败模式**：
1. **Commitment overload**：把所有事情都做承诺装置，会带来反向效应（Halpern UCL 2014）。
2. **Theatrical accountability**：你和搭档"互相演"，没人真的质询。这要求搭档质量高。
3. **金钱抵押扭曲**：人为了"赚回抵押金"而做不诚实的形式合规——交"演给系统看的好日志"。

---

### Q13：神经反馈和注意力训练（Mindfulness / Meditation / Headspace）

**核心假设**：通过冥想、正念、注意力训练，可以改善情绪稳定性和决策质量，从而改善交易表现。

**证据**：

【S 级】**冥想对交易表现有混合证据**：
- Sankhanan & Pruksapong (2023, NIDA Thailand) 226 名 Thai trader：**更密集 mindfulness meditation 实践者报告更好的交易表现**。机制：mindfulness → 交易纪律 → 减少恐慌出货 → 改善表现。
- 同作者另一研究 193 名 Thai trader：**mindfulness 降低 impulse control difficulty → 改善表现，但仅在原本有 impulse control 问题的人身上有效**。对原本控制力强的人，**mindfulness 反而降低表现**。这是 Q13 最重要的发现——**冥想不是普适处方**。
- Wong (2022, Open University PhD thesis) 820 人实验：**state mindfulness 没显著降低 disposition effect，但显著降低整体交易频率**——这本身就是减少损耗的好结果。
- Andrade et al. (2024) GSR 研究：holistic practices（meditation, tai chi, exercise）作为交易成功预测变量之一，但因子混杂。

【S 级】**Mindfulness 一般效应**：
- MAAS / FFMQ 量表的 mindfulness 与心理健康相关——这是已确立的领域。
- Sedlmeier et al. (2012) 元分析 *Psychological Bulletin* 138(6): 1139-1171：**整体 effect size d ≈ 0.27-0.34**（中等偏弱）。
- Goyal et al. (2014) JAMA Internal Medicine：**冥想对焦虑、抑郁、痛苦的效应中等；对其他领域（认知、压力管理、注意力）的证据较弱**。

【M 级】**Headspace / Calm 等商业产品**：
- Bostock et al. (2019) "Mindfulness on-the-go: Effects of a mindfulness meditation app on work stress and well-being" *Journal of Occupational Health Psychology* 24(1): 127-138：Headspace 用户在工作压力和 wellbeing 上有改善，d ≈ 0.3-0.5。
- 但**没有 Headspace → 交易表现 的研究**。

【S 级】**注意力训练（attention training programs）**：
- Cognitive training 整体证据弱（Owen et al. 2010 *Nature*：BBC Brain Training 实验，N=11K，**对未训练任务的迁移几乎为零**）。
- 这与 Q5 prediction market 训练的方向一致——cognitive training 难以跨任务迁移。

**证据等级**：S（mindfulness 整体），M（mindfulness 对交易表现的具体证据）。

**与 σ+AI 的对比**：σ+AI 当前没有显式 mindfulness 模块。决策链第 4 问"我现在是什么情绪"是 mindfulness 的最弱形式（情绪命名）。

**互补还是替代**：**有限互补**——但需要谨慎。
- ✅ 对 impulse control 较差的用户：mindfulness 可能有帮助（Sankhanan & Pruksapong 2023）。
- ❌ 对 impulse control 较好的用户：mindfulness 可能反而降低表现（同上研究）。
- ✅ 决策链第 4 问"情绪命名"是低成本 mindfulness——保留。
- ⚠️ 强制每天冥想是否值得 → 证据弱，不应强制。

**适合谁 / 不适合谁**：
- **适合**：报告自己有"冲动下单"问题的用户。
- **不适合**：本身已经能保持冷静决策的用户——冥想可能让他们"过度冷静"，错过情绪信号的有用信息（注意：Lo & Repin 的证据指出情绪本身是有信息的，过度抑制有副作用）。

**已知失败模式**：
1. **过度抑制情绪**：把情绪当作"敌人"完全消除——但情绪的高频信号是有用的（Lo & Repin 2002, Kandasamy 2016 interoception）。
2. **Mindfulness as identity**：把"冥想做得好"等同于"交易做得好"——这是间接的虚假等价。
3. **Apps 上瘾**：每天打卡冥想 10 分钟，但没真正改变情绪反应模式。

**对设计的具体建议**：保留决策链第 4 问。不强制 daily meditation。**给用户提供可选项**："如果你识别自己有 impulse control 问题，下面的资源可以试试"——指向可信的 mindfulness 资源（Headspace 基础课、JKZ MBSR）。

---

### Q14（新增）：退出协议 / 转向被动的有计划失败（Quit Gracefully Protocol）

**核心假设**（这是我加入的第 14 个范式）：训练系统应当显式包含"如果数据告诉你不应继续做主动交易，请系统化地切换到被动投资"的协议。

**理由（综合证据）**：

- Q6 证据：被动是 95%+ 散户的最优解；训练成功成为优秀交易者的概率极低。
- Q2 证据：模拟盘表现与实盘表现负相关——所以"我在模拟盘上表现好"不能作为"我应当继续"的论据。
- Q4 证据：Linnainmaa 2010-2011 显示**亏损投资者会继续交易而不是退出**——意味着内在动机不会自动让人停止。
- Q12 证据：StickK 风格的预定义触发条件可以让"理性的过去自我"约束"非理性的未来自我"。
- 04 笔记：用户流失曲线显示前 100 天 70% 流失——所以"系统化退出"应当在 100 天前就能被触发。

**证据等级**：S（综合多条 S 级证据的逻辑推演）。

**具体协议设计**：

1. **预定义退出触发条件**（用户在 Stage 0 就签署）：
   - 12 个月后，扣除手续费的累计净收益 < 同期被动 ETF 收益 - 5pp
   - **OR** 决策链遵守率连续 3 个月低于 50%（已在 Level 2 红灯）
   - **OR** 单年最大回撤 > 30%
   - **OR** 训练 18 个月后仍未达到预设的"统计显著盈利"标准（基于 380+ 笔且 Sharpe > 1）

2. **退出触发时的强制讨论**：
   - 不是"系统判定你失败了"，而是"数据触发了我们当初签的协议——我们一起复盘"。
   - 三个选项：
     - 切换到被动（默认推荐）。
     - 重新设计 σ 引擎（如果失败原因是流程错误而非能力问题）。
     - 暂停 6-12 个月后再决定（如果生活状态明显在变）。
   - **不允许的选项**："再战 6 个月"——因为 Linnainmaa 数据显示这是 sunk cost fallacy 的具体表现。

3. **诚实化框架**：
   - system_spec_v2.md 必须显式承认"这个系统的胜率是低的——大多数尝试者最终会切换到被动"。
   - 这一诚实表达**反而增加用户信任**——而不是削弱。
   - "退出"被定义为"系统的成功"，不是"系统的失败"。

**与现有设计的对比**：

system_spec_v2.md 已有 Level 1/Level 2 的失败模式，但**没有显式的"切换到被动"路径**。当前的失败模式停留在"我们重新设计 σ 引擎"层面，没有承认"也许这条路不应继续"。

**具体修改建议**：在 system_spec_v2.md "失败模式与退出条件"章节末尾增加 **Level 3：黑灯——退出主动交易，转向被动**。

---

### Q15（新增）：单笔实验（N-of-1 Experiment）作为元学习方法

**核心假设**（我加入的第 15 个范式）：把每一个交易决策看作一个对自己的"假设检验"——比"积累胜率"更结构化。

**证据基础**：

【S 级】**N-of-1 trial methodology**：
- Lillie et al. (2011) "The N-of-1 clinical trial: the ultimate strategy for individualizing medicine" *Personalized Medicine* 8(2): 161-173：在医学中已成熟方法，让个体作为自己的对照。
- Zucker et al. (1997) JAMA *Journal of Clinical Epidemiology*：N-of-1 trials 在药物选择中比 RCT 平均更有用——因为个体差异大于群体均值差异。

【U 级】**对交易的应用**：
- 把每个 setup 看作"我对这个 setup 是不是有 edge 的假设"。
- 决策链 5 问中的"如果 10 笔交易，我预期几笔赚？"可以重写为"我假设我对此类交易的胜率是 X%；我将做 N 笔来验证"。
- 这一框架的好处：把"亏损"转换为"假设被证伪"——一个良性的科学态度，而非情绪损伤。

**与现有 σ 引擎的对比**：当前决策链第 5 问已经接近这一思想，但没明确化为"假设-检验"循环。

**具体建议**：在 σ 引擎第 5 问加入"实验注册"结构——你声明的胜率 X 和样本量 N（比如"我将做 20 笔此 setup 后才评估"），这样事后可以正式判定 reject/fail-to-reject。

---

## 范式对比矩阵

| 范式 | 证据等级 | 主要优势 | 主要劣势 | 与 σ+AI 关系 | 推荐 |
|---|---|---|---|---|---|
| **Q1 纯规则化系统** | M | 绕开行为偏误执行 | 过拟合 / 编程门槛 / 选择偏误转移 | 替代（不同路径） | 仅推荐有编程基础的用户 |
| **Q2 长期模拟盘训练** | S（反向） | 学习成本低 | **唯一严格研究显示与实盘表现负相关** | 应限用 | 删除当前隐含假设 |
| **Q3 HRV / 生物反馈** | S（含 RCT） | 客观可验证 / 改善执行决策 | 设备成本 + 数据噪音 | 强互补 | Stage 2 集成 |
| **Q4 社群 / 同伴学习** | S（整体反向） | 减少孤独学习盲区 | herding / mimetic / 推票群有害 | 有限互补（仅严肃同伴） | 引入互查协议；禁止跟单/推票 |
| **Q5 扑克 / Prediction Market 训练** | S | 概念迁移强（process-outcome 分离） | 不完全对应交易（无 GTO） | 强互补 | Stage 1.5 引入辅助训练 |
| **Q6 被动投资** | **S+** | 95%+ 散户的期望最优 | 不提供训练负载 | 互补（资金分离） | **Stage -2 强制基线** |
| **Q7 单一 setup 聚焦** | S（教育心理） | 工程化 wicked → kind / 提升信噪比 | setup 选错则反复亏 | 强互补 | Stage 0.5 强制单 setup |
| **Q8 真钱小仓位** | S（双向） | 真实情绪反馈 / 心理账户清晰 | 偏差更强 / 滑入主资金风险 | 互补（明确边界） | Stage 0 加边界协议 |
| **Q9 传统课程（CFA/EPAT）** | M（间接） | 知识体系完整 | 行为效应小 / 投入产出比低 | 弱互补 | 不强制 |
| **Q10 时序结构** | S+M | 高效顺序节省时间 | 具体顺序在交易中无验证 | 已是 σ+AI 的设计核心 | 维持 / 优化 |
| **Q11 跟单 / 完全外包** | S（整体反向） | 短期低门槛 | 增加风险偏好 / 没有训练 | 反向 | 禁止与 σ 训练混用 |
| **Q12 公开承诺 / 抵押** | S（中等强度） | 修补诚实记录最大盲区 | commitment overload 可能反向 | **强互补（最重要的补强）** | 引入互查搭档 + 可选金钱抵押 |
| **Q13 冥想 / 正念** | S（混合） | 对 impulse control 弱者有效 | 对自控者反而降低表现 | 有限互补（条件性） | 提供可选资源不强制 |
| **Q14（新）退出协议** | S（综合推演） | 避免 sunk cost / 承认 95% 失败概率 | 心理上抗拒"被告知失败" | **必加** | Stage 4 强制设计 |
| **Q15（新）N-of-1 实验** | S（医学迁移） | 让亏损成为假设证伪 | 需结构化训练才能习得 | 强互补 | 决策链第 5 问升级 |

---

## 综合判断

### 最强证据的路径：**被动投资（Q6） + 把"训练"心理账户化的训练资金分离**

这是本调研中证据等级最高、最难反驳的结论。任何不直面这一结论的训练系统设计，都是在用户面前隐藏一个关键事实。

但这不意味着 σ+AI 系统应该被废弃——它意味着 σ+AI 系统的**目标必须重新定位**：

- ❌ 错误的目标定位："让你成为优秀交易者，赚钱"——这与证据不符。
- ✅ 正确的目标定位："让你**通过严肃的主动交易实验**，训练自己的决策能力、情绪管理、不确定性容忍度——并在数据告诉你应该停止时让你能够诚实地停止"。

后者是认知工程目标，不是财富最大化目标——AGENTS.md 用户定位本身就是后者。

### 与现有设计互补、应当集成的路径

按证据强度排序：

1. **Q6 被动基线 + 训练资金分离**（Stage -2 新增）——证据等级 S+。
2. **Q12 公开承诺 / 互查搭档**（Stage 1 新增）——修补当前最严重的盲区。
3. **Q7 单一 setup 强制聚焦**（Stage 0.5 新增）——把 wicked 工程化为 kind。
4. **Q14 退出协议**（Stage 4 新增）——证据等级 S（综合推演）。
5. **Q3 HRV 生物反馈**（Stage 2 新增）——客观验证情绪记录。
6. **Q5 扑克 + 预测市场辅助训练**（Stage 1.5 新增）——便宜的概率思维训练。
7. **Q15 N-of-1 实验框架**（决策链第 5 问升级）——让亏损成为假设证伪。

### 应该放弃 / 警惕的路径

1. **Q2 长期模拟盘**——证据反向。仅作工具熟悉用，绝不作训练胜率用。
2. **Q11 跟单 / copy trading**——证据反向。明确禁止与 σ 训练混用。
3. **Q9 大额传统课程**（CFA/FRM/EPAT 作为零售提升手段）——投入产出比低。轻量级 glossary 已够。
4. **Q4 推票群 / 信号发布群 / 付费交易导师**（无独立验证）——证据反向 + 高诈骗率。

### 应该保持但谨慎使用的路径

1. **Q1 纯规则化系统**——不是小白路径，但可作为 Stage 3+ 升级方向。
2. **Q13 冥想 / 正念**——条件性有效，提供资源不强制。
3. **Q8 真钱小仓位**——必要的真实反馈，但需明确金额边界 + 心理账户。
4. **Q10 时序结构**——继续 σ → α 顺序，但应增加 Stage -2 和 Stage 4。

### 对 system_spec_v2.md 的具体修订建议

**优先级 P0（必须改）**：

1. 在文档开头加入"诚实声明"：本系统的目标不是让用户致富——证据指向 95%+ 散户的最优财富路径是被动投资。本系统的目标是让用户通过主动交易这一**认知训练介质**发展决策能力，并在数据不支持继续时让用户能够诚实地切换到被动。

2. 新建 Stage -2：被动基线 + 训练资金分离协议。

3. 新建 Stage 4：退出协议（基于 Q14 设计）。

4. 删除 Stage -1 中"我们不在这个阶段模拟或纸上交易（那属于 Stage 0 的训练内容）"的暗示——纸上交易在 Stage 0 也不应作为训练胜率工具。

**优先级 P1（高建议改）**：

5. Stage 0.5：单一 setup 强制选择 + 限制（基于 Q7）。

6. Stage 1：加入互查搭档协议（基于 Q12）。

7. Stage 2：HRV 趋势监测加入（基于 Q3）。

8. 决策链第 5 问升级为 N-of-1 实验注册（基于 Q15）。

9. σ 引擎指标章节：把"50 笔后做行为分析"调整为"100 笔基础信号 / 380+ 笔 95% 置信"——明确样本量的统计意义。

**优先级 P2（建议改）**：

10. Stage 1.5：扑克 + 预测市场辅助训练（基于 Q5）。

11. 决策链第 4 问保持，但增加可选的 mindfulness 资源（基于 Q13）。

12. 风险与边界章节：明确禁止跟单 / 推票群 / 付费导师 / 长期模拟盘等已被证据否定的路径。

---

## 引用清单（按本笔记出现顺序）

### 散户交易失败的核心数据（Q6 + Q1 + Q2）
1. Barber, B.M. & Odean, T. (2000) "Trading is Hazardous to Your Wealth", *Journal of Finance* 55(2): 773-806.
2. Barber, B.M., Lee, Y.T., Liu, Y.J. & Odean, T. (2014) "Do Day Traders Rationally Learn About Their Ability?", *Review of Financial Studies* 26(11).
3. Chague, F. & Giovannetti, B. (2019) "Day Trading for a Living?", SSRN 3423101.
4. Chague, F. & Giovannetti, B. (2020) "Day-trading stocks for a living?", *Brazilian Review of Finance*.
5. Linnainmaa, J. (2010) "Why Do (Some) Households Trade So Much?", *Review of Financial Studies* 24(5): 1630-1666.
6. Linnainmaa, J. et al. (2020) "Learning, Fast or Slow", *Review of Asset Pricing Studies* 10(1): 61-93.
7. Locke, P. & Mann, S. (2015) "Learning by aspiring professional traders: Learning to take risk", *Journal of Behavioral and Experimental Finance*.
8. ESMA Annual Statistical Report on EU Securities Markets — 截至 2024 数据，零售 CFD 账户 71.6% 亏损（部分券商 89%）。
9. SPIVA U.S. Year-End 2024 Scorecard, S&P Dow Jones Indices.

### 模拟盘转移效应（Q2）
10. Goldstein, da Costa & Yoshinaga (2024) "Trading Simulations and Real Money Outcomes", *Journal of Behavioral Finance* 25(4): 436-448.
11. Cornil, Hardisty & Bart (2022) "Stakes and Investor Behaviors", SSRN 4219861.
12. Cipriano, M.C., Gruca, T.S. & Jiao, J. (2020) "Can Investing Diaries be Hazardous to Your Financial Health?", *Journal of Prediction Markets* 14(1).

### 量化交易过拟合（Q1）
13. Bailey, Borwein, López de Prado, Zhu (2014) "Pseudo-Mathematics and Financial Charlatanism", *Notices of the AMS*.
14. Yan & Zheng (2017) "p-Hacking: Evidence from Two Million Trading Strategies", SFI Working Paper.
15. Harvey, Liu & Zhu (2016) "...and the Cross-Section of Expected Returns", *Review of Financial Studies* 29(1).
16. López de Prado (2018) *Advances in Financial Machine Learning*, Wiley.

### 生理监测 / HRV（Q3）
17. Lo, A.W. & Repin, D. (2002) "The Psychophysiology of Real-Time Financial Risk Processing", NBER WP 8508.
18. Steenbarger, Lo & Repin (2005) "Fear and Greed in Financial Markets", *American Economic Review* P&P 95(2): 352-359.
19. Andrade, Odean & Lin (2022) "Real-time extended psychophysiological analysis of financial risk processing", *PLOS One*.
20. Kandasamy et al. (2016) "Interoceptive Ability Predicts Survival on a London Trading Floor", *Scientific Reports* 6:32986.
21. Forte, Favieri & Casagrande (2021) "Heart Rate Variability and Decision-Making", PubMed 33672004.
22. Salvador et al. (2022) "Learned self-regulation in top-level managers through neurobiofeedback training improves decision making under stress", *Scientific Reports* 12:6171.
23. Pizzoli et al. (2023) "The effect of a single-session heart rate variability biofeedback on attentional control", *Frontiers in Psychology* 14:1292983.
24. Tinello et al. (2022) "Does Heart Rate Variability Biofeedback Enhance Executive Functions Across the Lifespan? A Systematic Review", *Journal of Cognitive Enhancement*.

### 同伴 / 社群效应（Q4）
25. Heimer, R. (2016) "Peer Pressure: Social Interaction and the Disposition Effect", *Review of Financial Studies* 29(11): 3177-3209.
26. Han, Hirshleifer & Walden (2023) "Social transmission bias and active trading", *Journal of Financial Economics* 150(1): 139-165.
27. Bursztyn et al. (2014) "Understanding Mechanisms Underlying Peer Effects: Evidence from a Field Experiment on Financial Decisions", *Econometrica* 82(4): 1273-1301.
28. Liaukonyte & Žaldokas (2022) "Anchoring Trading Decisions on Social Media Sentiment", *Management Science* 68(4).
29. Eby et al. (2008) "Does mentoring matter? A multidisciplinary meta-analysis", *Journal of Vocational Behavior* 72: 254-267.

### 扑克 / Prediction Market 训练（Q5）
30. Levitt, S.D. & Miles, T.J. (2011) "The Role of Skill Versus Luck in Poker", NBER WP 17023.
31. Duke, A. (2018) *Thinking in Bets*, Penguin Random House.
32. Mauboussin, M. (2012) *The Success Equation*, Harvard Business Review Press.
33. Hauenstein, Mellers & Tetlock (2025) "Reanalysis of IARPA ACE Tournament Data Using IRT", *Psychological Science* 36(1).
34. Tinghög et al. (2023) "Impact of gamification on mitigating behavioral biases of investors", *Journal of Behavioral and Experimental Finance*.

### 被动投资（Q6）
35. SPIVA U.S. Year-End 2024 Scorecard, S&P Dow Jones Indices.
36. Bogle, J.C. (1999) *Common Sense on Mutual Funds*, John Wiley & Sons.
37. Vanguard (2017) "Setting the Record Straight: Truths about Indexing", white paper.
38. AEA 2022 working paper "How Competitive Is the Stock Market?".
39. Kaiser, T. & Lusardi, A. (2021) "Financial education affects financial knowledge and downstream behaviors", *Journal of Financial Economics* 145(2): 255-272.

### 单一 setup / 专门化（Q7）
40. Kornell, N. & Bjork, R.A. (2008) "Learning concepts and categories: Is spacing the 'enemy of induction'?", *Psychological Science* 19(6): 585-592.
41. Güllich, A. et al. (2022) "What Makes a Champion? Early Multidisciplinary Practice, Not Early Specialization", *Perspectives on Psychological Science*.
42. Lavancier et al. (2020) "Specific Versus Varied Practice in Perceptual Expertise", *Journal of Experimental Psychology: Human Perception and Performance*.

### 心理账户（Q8）
43. Thaler, R. (1985) "Mental Accounting and Consumer Choice", *Marketing Science* 4(3): 199-214.
44. Thaler, R. & Johnson, E.J. (1990) "Gambling with the House Money and Trying to Break Even", *Management Science* 36(6).

### 财务教育 / CFA（Q9）
45. Andersson, P. (1994) "Are CFA Charterholders Better Equity Fund Managers?", *Financial Analysts Journal*.
46. De Franco, G. & Zhou, Y. (2009) "The Performance of Analysts with a CFA Designation", *The Accounting Review* 84(2): 383.

### 学习路径（Q10）
47. Ritter, F.E., Nerb, J., Lehtinen, E. & O'Shea, T.M. (eds.) (2007) *In Order to Learn*, Oxford University Press.
48. Bengio, Y. et al. (2009) "Curriculum learning", *Proceedings of the 26th Annual ICML*.

### Copy Trading（Q11）
49. Apesteguia, J., Oechssler, J. & Weidenholzer, S. (2018) "Copy Trading", *Management Science* 64(12): 5772-5784.
50. FCA "Copy trading" regulatory guidance.

### Commitment Devices（Q12）
51. Schwartzstein, J. & Sunderam, A. (2017) "Observability Increases the Demand for Commitment Devices", *Management Science*.
52. Giné, X., Karlan, D. & Zinman, J. (2010) "Put Your Money Where Your Butt is: A Commitment Contract for Smoking Cessation", *American Economic Journal: Applied Economics* 2(4).
53. Lerner, J.S. & Tetlock, P.E. (1999) "Accounting for the Effects of Accountability", *Psychological Bulletin* 125(2): 255-275.
54. Halpern, S.D. et al. (2014) UCL Reputational Commitment Weight Loss Experiment.
55. Berkeley/Haas (2024) "Friends with Health Benefits", *Management Science*.

### Mindfulness（Q13）
56. Sankhanan, P. & Pruksapong, P. (2023) "The Role of Mindfulness Meditation on Stock Trading Performance", NIDA Thailand.
57. Sankhanan, P. & Pruksapong, P. (2023) "Does mindfulness enhance stock trading performance?: the moderating and mediating effects of impulse control difficulties", NIDA Thailand.
58. Wong, E. (2022) "The role of mindfulness in financial decision-making", PhD thesis, Open University.
59. Sedlmeier, P. et al. (2012) "The psychological effects of meditation: a meta-analysis", *Psychological Bulletin* 138(6): 1139-1171.
60. Goyal, M. et al. (2014) "Meditation Programs for Psychological Stress and Well-being", *JAMA Internal Medicine*.
61. Bostock, S. et al. (2019) "Mindfulness on-the-go: Effects of a mindfulness meditation app", *Journal of Occupational Health Psychology* 24(1): 127-138.
62. Owen, A. et al. (2010) "Putting brain training to the test", *Nature*.

### Wicked Environment（Q10 + 04 笔记）
63. Hogarth, R.M. (2001) *Educating Intuition*, University of Chicago Press.
64. Kahneman, D. & Klein, G. (2009) "Conditions for Intuitive Expertise: A Failure to Disagree", *American Psychologist* 64(6): 515-526.
65. Lo, A. (2017) *Adaptive Markets*, Princeton University Press.

### Implementation Intentions（决策链理论基础）
66. Gollwitzer, P.M. & Sheeran, P. (2006) "Implementation Intentions and Goal Achievement: A Meta-analysis of Effects and Processes", *Advances in Experimental Social Psychology* 38: 69-119.

### Sample Size / Statistical Power（样本量盲区）
67. TradeProb sample size formula: N = (Z² × W × (1-W)) / (W - 0.5)²
68. Bailey, López de Prado et al. (2014) "Probability of Backtest Overfitting".

### N-of-1（Q15）
69. Lillie, E.O. et al. (2011) "The N-of-1 clinical trial: the ultimate strategy for individualizing medicine", *Personalized Medicine* 8(2): 161-173.
70. Zucker, D.R. et al. (1997) "Combining single patient (N-of-1) trials to estimate population treatment effects and individual patient responses", *Journal of Clinical Epidemiology*.

### 决策框架（其他）
71. Klein, G. (2009) "Streetlights and Shadows: Searching for the Keys to Adaptive Decision Making", MIT Press.
72. Kahneman, D. (2011) *Thinking, Fast and Slow*, FSG.

### 系统性 vs 主观（Q1）
73. Northern Trust (2024) "Systematic vs Discretionary Performance Analysis", insights research.
74. Confluence (2024) "Systematic vs Discretionary Trading", asset management research.

### Cross-reference 内部
75. /workspace/research/notes/01_journaling_evidence.md
76. /workspace/research/notes/02_retail_failure_2020_2026.md
77. /workspace/research/notes/03_ai_coaching_evidence.md
78. /workspace/research/notes/04_deliberate_practice_metacognition.md
79. /workspace/system_spec_v2.md
80. /workspace/AGENTS.md

---

## 诚实标记总结

本笔记的所有"证据等级"标注均基于 2026-05-05 的 web 检索 + 已知文献。需特别注意：

1. **Stanford 2025 研究 "58% 零售算法策略 3 个月内崩溃"** —— 我未找到直接学术论文链接；当作 M 级而非 S 级。
2. **"23%-30% 交易日志改善表现"** —— 这一数字反复出现在 Tradezella、Journalyze、TraderLens 等商业博客中，但**找不到追溯到原始学术研究**。01 笔记已论述。本笔记不援引这些 W 级数字作为证据。
3. **行业说法（"83% 散户失败"、"95% 失败率"等）** —— 在缺乏可追溯的、跨地区跨方法的精确统计前，本笔记使用最严格的来源数据：Brazilian 91-97%（Chague & Giovannetti，长持仓周期），ESMA 71.6-89%（CFD 短持仓周期），Taiwan 75% 退出率。这些是各自情境下严格的数字。
4. **σ 引擎与具体替代范式的"互补"判断** —— 对每一对范式的"强互补 / 有限互补"判断，是基于上述证据 + 设计逻辑的推演，不是被独立验证的"系统融合效应"——后者目前没有任何研究检验过。
5. **Q14（退出协议） + Q15（N-of-1）** —— 我加入的两个范式。它们的"证据等级"标注的是组件证据（StickK 的金钱抵押 / 医学 N-of-1），不是"在交易系统中应用这两个范式的整体效应"——后者无证据。

**对设计的最重要的、最诚实的判断（应当反复检视）**：

- 95%+ 的散户应当做被动投资。
- 训练自己成为优秀交易者的概率极低，且**统计上很多年都无法被确认是不是运气**。
- σ+AI 系统对一个普通用户的最实际价值，不是"让你赚钱"，而是"让你**在自己注定不能成为优秀交易者**这件事上学到东西，并在数据明确告诉你时不要再继续浪费时间和金钱"。
- 这一定位的诚实化是当前 system_spec_v2.md 与最强证据之间最重要的一致性补丁。
