@echo off
echo ========================================
echo Port Status Check
echo ========================================
echo.

echo [1/3] Checking current directory...
echo Current directory: %CD%
echo.

echo [2/3] Checking if Python is available...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not available!
    echo Please install Python or check PATH
    pause
    exit /b 1
)
echo ✓ Python is available
echo.

echo [3/3] Checking port usage...
echo Checking ports 8000-8006...
netstat -an | findstr ":800"
echo.

echo ========================================
echo Port check completed
echo ========================================
pause



