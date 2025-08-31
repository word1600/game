@echo off
echo ========================================
echo Simple Unit 6 Test
echo ========================================
echo.

echo [1/4] Checking current directory...
echo Current: %CD%
echo.

echo [2/4] Changing to Unit 6 directory...
cd unit6-github\unit6
echo New directory: %CD%
echo.

echo [3/4] Checking Unit 6 files...
if exist "index.html" echo ✓ index.html found
if exist "game.js" echo ✓ game.js found
if exist "style.css" echo ✓ style.css found
if exist "data\unit6.json" echo ✓ unit6.json found
echo.

echo [4/4] Starting Unit 6 server...
echo Server will start on http://localhost:8006
echo Press Ctrl+C to stop
echo.
python -m http.server 8006
pause


