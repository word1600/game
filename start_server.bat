@echo off
echo 🚀 UFO Word Game 로컬 서버 시작
echo ======================================

:check_port
netstat -an | findstr :8000 >nul
if %errorlevel% equ 0 (
    echo ❌ 포트 8000이 이미 사용 중입니다.
    echo 🔍 사용 중인 프로세스 확인 중...
    netstat -ano | findstr :8000
    echo.
    echo 💡 다른 포트로 시작하시겠습니까? (y/n)
    set /p choice=
    if /i "%choice%"=="y" (
        echo 💡 사용할 포트 번호를 입력하세요 (예: 8001, 8002)
        set /p port=
        goto start_server
    ) else (
        echo ❌ 서버 시작을 취소했습니다.
        pause
        exit
    )
) else (
    set port=8000
    goto start_server
)

:start_server
echo.
echo 🌐 포트 %port%에서 서버를 시작합니다...
echo 📍 접속 URL: http://localhost:%port%/
echo.
echo 🎮 게임 접속 방법:
echo    - Unit 1: http://localhost:%port%/
echo    - Unit 2: http://localhost:%port%/unit2/
echo    - Unit 3: http://localhost:%port%/unit3/
echo    - Unit 4: http://localhost:%port%/unit4/
echo    - Unit 5: http://localhost:%port%/unit5/
echo.
echo ⚠️  서버를 중지하려면 이 창을 닫거나 Ctrl+C를 누르세요.
echo.
echo 🚀 서버 시작 중...
python -m http.server %port%





