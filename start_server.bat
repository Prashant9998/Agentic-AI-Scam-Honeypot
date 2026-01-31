@echo off
REM ================================================
REM UNIFIED SERVER STARTUP SCRIPT
REM ================================================
REM This script starts the unified server that runs
REM both the API and serves all HTML files
REM ================================================

echo.
echo ========================================
echo AGENTIC HONEYPOT - UNIFIED SERVER
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Checking dependencies...
pip show fastapi >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required packages...
    pip install -r requirements.txt
)

echo [2/3] Starting server...
echo.
echo Server will be available at:
echo   - Main Page:  http://localhost:8000
echo   - Main App:   http://localhost:8000/app
echo   - API Tester: http://localhost:8000/tester
echo   - Combined:   http://localhost:8000/combined
echo   - API Docs:   http://localhost:8000/docs
echo.
echo Press CTRL+C to stop the server
echo.

REM Start the unified server
python server.py

pause
