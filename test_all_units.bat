@echo off
echo ========================================
echo All Units Local Test
echo ========================================
echo.

echo [1/6] Testing Unit 1...
cd unit1
echo Starting Unit 1 server on port 8001...
start "Unit 1" cmd /k "python -m http.server 8001"
echo ✓ Unit 1 server started at http://localhost:8001
cd ..
echo.

echo [2/6] Testing Unit 2...
cd unit2
echo Starting Unit 2 server on port 8002...
start "Unit 2" cmd /k "python -m http.server 8002"
echo ✓ Unit 2 server started at http://localhost:8002
cd ..
echo.

echo [3/6] Testing Unit 3...
cd unit3
echo Starting Unit 3 server on port 8003...
start "Unit 3" cmd /k "python -m http.server 8003"
echo ✓ Unit 3 server started at http://localhost:8003
cd ..
echo.

echo [4/6] Testing Unit 4...
cd unit4
echo Starting Unit 4 server on port 8004...
start "Unit 4" cmd /k "python -m http.server 8004"
echo ✓ Unit 4 server started at http://localhost:8004
cd ..
echo.

echo [5/6] Testing Unit 5...
cd unit5
echo Starting Unit 5 server on port 8005...
start "Unit 5" cmd /k "python -m http.server 8005"
echo ✓ Unit 5 server started at http://localhost:8005
cd ..
echo.

echo [6/6] Testing Unit 6...
cd unit6-github\unit6
echo Starting Unit 6 server on port 8006...
start "Unit 6" cmd /k "python -m http.server 8006"
echo ✓ Unit 6 server started at http://localhost:8006
cd ..\..
echo.

echo ========================================
echo All Unit servers started!
echo ========================================
echo.
echo 🌐 Test URLs:
echo Unit 1: http://localhost:8001
echo Unit 2: http://localhost:8002
echo Unit 3: http://localhost:8003
echo Unit 4: http://localhost:8004
echo Unit 5: http://localhost:8005
echo Unit 6: http://localhost:8006
echo.
echo Each unit runs on a different port to avoid conflicts.
echo Close the command windows when done testing.
echo.
pause



