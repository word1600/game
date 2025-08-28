@echo off
echo ========================================
echo Unit 6 Fix Deployment - Safe Mode
echo ========================================
echo.

echo [1/5] Checking current directory...
cd unit6-github
if not exist ".git" (
    echo ERROR: Not a git repository!
    pause
    exit /b 1
)
echo ✓ Git repository found
echo.

echo [2/5] Checking git status...
git status --porcelain
echo.

echo [3/5] Adding modified game.js file...
git add unit6/game.js
if %errorlevel% neq 0 (
    echo ERROR: Failed to add file!
    pause
    exit /b 1
)
echo ✓ File added successfully
echo.

echo [4/5] Committing changes...
git commit -m "Fix Unit 6: Change selectedUnit from unit2 to unit6"
if %errorlevel% neq 0 (
    echo ERROR: Failed to commit!
    pause
    exit /b 1
)
echo ✓ Changes committed successfully
echo.

echo [5/5] Pushing to GitHub...
git push origin main
if %errorlevel% neq 0 (
    echo ERROR: Failed to push!
    pause
    exit /b 1
)
echo.

echo ========================================
echo ✓ Unit 6 fix deployed successfully!
echo ========================================
echo.
echo Please wait 1-3 minutes for GitHub Pages to update.
echo You can check the status at: https://word1600.github.io/game/unit6/
echo.
pause
