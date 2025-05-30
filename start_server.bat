@echo off
echo Starting SIMO KHDN FastAPI Server on port 8069...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import fastapi, uvicorn, requests, jinja2" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install fastapi uvicorn requests jinja2 pandas openpyxl pyodbc
)

REM Create logs directory if not exists
if not exist "logs" mkdir logs

REM Start the server
echo.
echo Starting server at http://localhost:8069
echo Press Ctrl+C to stop the server
echo.

python main.py