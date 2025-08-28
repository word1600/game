@echo off
echo Quick Unit 6 Test
echo.

echo Current directory: %CD%
echo.

echo Checking Unit 6 files...
if exist "unit6-github\unit6\index.html" (
    echo ✓ index.html found
) else (
    echo ❌ index.html NOT found
)

if exist "unit6-github\unit6\game.js" (
    echo ✓ game.js found
) else (
    echo ❌ game.js NOT found
)

if exist "unit6-github\unit6\data\unit6.json" (
    echo ✓ unit6.json found
) else (
    echo ❌ unit6.json NOT found
)

echo.
echo Starting Unit 6 server on port 8006...
echo Open browser: http://localhost:8006
echo Press Ctrl+C to stop
echo.

cd unit6-github\unit6
python -m http.server 8006
pause

