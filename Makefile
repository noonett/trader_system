# σ 系统后台批处理入口
# 对应 design_proposal_2026.md §三.2.2 / §三.2.3

.PHONY: weekly-report monthly-calibration violations-scan all help

help: ## 显示帮助
	@echo "σ 系统后台批处理命令："
	@echo "  make weekly-report        — 生成 AI 周读报告 prompt + 跑违规扫描"
	@echo "  make monthly-calibration  — 生成 AI 月校准报告 prompt + 跑 KPI alert"
	@echo "  make violations-scan      — 单独跑违规扫描"
	@echo ""
	@echo "周末流程：make weekly-report"
	@echo "月末流程：make monthly-calibration"

weekly-report: violations-scan ## 周末：AI 周读报告 + 违规扫描
	@bash scripts/weekly_report.sh

monthly-calibration: violations-scan ## 月末：AI 月校准报告 + KPI alert
	@bash scripts/monthly_calibration.sh
	@python3 scripts/kpi_alert.py

violations-scan: ## 跑 5 类违规检测
	@python3 scripts/violations_scan.py

all: weekly-report ## 全部跑一遍（等同 weekly-report）
