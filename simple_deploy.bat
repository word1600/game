@echo off
echo Simple Unit 6 Deploy
echo.

cd unit6-github
echo Current directory: %CD%
echo.

echo Git status:
git status
echo.

echo Adding file...
git add unit6/game.js
echo.

echo Committing...
git commit -m "Fix Unit 6"
echo.

echo Pushing...
git push origin main
echo.

echo Done!
pause


