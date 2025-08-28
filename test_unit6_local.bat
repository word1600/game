@echo off
echo ========================================
echo Unit 6 Local Test - Localhost Server
echo ========================================
echo.

echo [1/3] Changing to Unit 6 directory...
cd unit6-github\unit6
if not exist "index.html" (
    echo ERROR: index.html not found!
    pause
    exit /b 1
)
echo ✓ Unit 6 directory found
echo.

echo [2/3] Starting local server on port 8000...
echo.
echo 🌐 Open your browser and go to: http://localhost:8000
echo.
echo [3/3] Server is running... Press Ctrl+C to stop
echo ========================================
python -m http.server 8000
pause

