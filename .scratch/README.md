# .scratch/ —— 临时中转目录（**不要 merge 到 master**）

本目录仅用于在 cloud agent 与本机之间传输临时文件，**不属于 σ 系统的代码或文档**。

## 当前内容

- `medical-report-2026-05-08/` —— 钟钊灵女士病情研究分析报告（家属备查），目标是放到 noonett/tmp 仓库。来源是 cloud agent 这次会话的研究分析，无关 σ / α 引擎。

## 使用方式

1. 在本机：`git fetch origin && git checkout cursor/medical-export-transit-82f4`
2. 把 `.scratch/medical-report-2026-05-08/` 整个文件夹拷贝到任意位置（如 `~/Desktop/`）
3. 在本机的 noonett/tmp 仓库 clone 中放入该文件夹，自行 commit + push
4. 切回 master：`git checkout master`
5. 删除本地分支：`git branch -D cursor/medical-export-transit-82f4`
6. 删除远程分支：`git push origin --delete cursor/medical-export-transit-82f4`

## 为什么走这个路径

Cursor cloud agent 的 GitHub token 是 trader_system 仓库专属 installation token，无法 push 到其他仓库（如 noonett/tmp）。这是 Cursor 的安全设计，无法绕过。所以唯一可行的路径是通过当前仓库的临时分支中转。
