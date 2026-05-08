@echo off
REM sigma-relay Windows 快速启动脚本
REM 双击运行或在 cmd/PowerShell 中执行

echo ==========================================
echo   sigma-relay v0.1 - ATAS Trade Capture
echo ==========================================
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 未安装或不在 PATH 中
    echo 请安装 Python 3.10+: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM 进入 sigma-relay 目录
cd /d "%~dp0"

REM 安装依赖（首次运行）
if not exist ".venv" (
    echo [SETUP] 创建虚拟环境...
    python -m venv .venv
    echo [SETUP] 安装依赖...
    .venv\Scripts\pip install -r requirements.txt
    echo.
)

REM 激活虚拟环境并启动
echo [START] 启动 sigma-relay on 127.0.0.1:9733 ...
echo [INFO]  按 Ctrl+C 停止
echo.
.venv\Scripts\python server.py
pause
