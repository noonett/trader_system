# Stage 0 工具 deprecation 说明（2026-05-06）

## 背景

项目原计划经历 Stage -1 → Stage 0 → Stage 1+ 渐进搭建。Phase 1 + Phase 2 调研（2026-05-03 至 2026-05-06）发现：

- 旧 Stage 0 决策链是开放式 Q1-Q5（What/Why 主导），与 implementation intention 文献的 if-then 范式不一致（foundation §三.4 + Gollwitzer & Sheeran 2006, d=.27-.66）
- 旧 trade-journal-template 与 BCT identity 维度（Michie 2013 BCTTv1 13.x）不兼容
- 旧 position_sizer.py 是独立脚本，未嵌入决策链工作流
- Why 类提问触发反刍（Watkins & Teasdale 2004, S 级），v0 改为 What 主导 + if-then 形式

用户 2026-05-06 明确"老项目完全不要考虑，不用考虑兼容"。

## 处置

本目录下的文件都已被 v0 σ 系统（详见 [research/design_proposal_2026.md](../../research/design_proposal_2026.md)）取代。
保留这些文件仅作历史回溯；任何新交易请使用 v0 工作流（sigma/ + trades/）。

## 新版本位置

| 旧文件 | 新位置 | 变化 |
|---|---|---|
| decision-chain.md | sigma/decision-chain.md | if-then 形式 + 第一人称 identity 表述 + 禁 Why 问题 |
| trade-journal-template.md | trades/YYYY/MM/YYYY-MM-DD-symbol-dir.md | 一文聚合（盘前 if-then + 决策链 + 盘后 EMA + 异步复盘）|
| tools/position_sizer.py | 嵌入决策链 If 5 + Q5a 来源校验 | 不再独立脚本；仓位计算在决策链中完成 |

## 保留的真实交易记录

[trades/2026/05/2026-05-04-mgc-202606-long.md](../../trades/2026/05/2026-05-04-mgc-202606-long.md) 是用户在旧 Stage 0 下记录的真实交易——保留在原位，不移动、不删除。v0 KPI 计算从 v0 启动日开始，不回溯。
