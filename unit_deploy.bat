@echo off
REM Unit 자동 배포 스크립트 (Windows 버전)
REM 사용법: unit_deploy.bat [Unit번호] [커밋메시지]

setlocal enabledelayedexpansion

REM 매개변수 확인
if "%~1"=="" (
    echo [ERROR] 사용법: %0 ^<Unit번호^> [커밋메시지]
    echo [ERROR] 예시: %0 21
    echo [ERROR] 예시: %0 21 "Add Unit 21 - TOEIC Word UFO Game"
    exit /b 1
)

set UNIT_NUMBER=%~1
set COMMIT_MSG=%~2
if "%COMMIT_MSG%"=="" set COMMIT_MSG=Add Unit %UNIT_NUMBER% - TOEIC Word UFO Game

echo [INFO] Unit %UNIT_NUMBER% 배포를 시작합니다...

REM 1. 현재 디렉토리 확인
if not exist "unit%UNIT_NUMBER%" (
    echo [ERROR] unit%UNIT_NUMBER% 폴더가 존재하지 않습니다!
    echo [ERROR] 먼저 Unit %UNIT_NUMBER% 파일들을 생성해주세요.
    exit /b 1
)

REM 2. Git 상태 확인
echo [INFO] Git 상태를 확인합니다...
git status >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git 저장소가 아닙니다!
    exit /b 1
)

REM 3. 변경사항 확인
echo [INFO] 변경사항을 확인합니다...
git status --porcelain | findstr /r "." >nul
if errorlevel 1 (
    echo [WARNING] 커밋할 변경사항이 없습니다.
    exit /b 0
)

REM 4. 모든 파일 스테이징
echo [INFO] 변경사항을 스테이징합니다...
git add .
if errorlevel 1 (
    echo [ERROR] 파일 스테이징 실패!
    exit /b 1
)
echo [SUCCESS] 파일 스테이징 완료

REM 5. 커밋 생성
echo [INFO] 커밋을 생성합니다...
git commit -m "%COMMIT_MSG%"
if errorlevel 1 (
    echo [ERROR] 커밋 생성 실패!
    exit /b 1
)
echo [SUCCESS] 커밋 생성 완료: %COMMIT_MSG%

REM 6. 원격 저장소에 푸시
echo [INFO] 원격 저장소에 푸시합니다...
git push origin main
if errorlevel 1 (
    echo [ERROR] 푸시 실패! 수동으로 확인해주세요.
    exit /b 1
)
echo [SUCCESS] 푸시 완료!

REM 7. 배포 상태 안내
echo [INFO] 배포 상태를 확인합니다...
echo [WARNING] GitHub Pages 배포는 약 2-5분 소요됩니다.
echo [INFO] 배포 완료 후 다음 URL에서 확인하세요:
echo [INFO] https://word1600.github.io/game/unit%UNIT_NUMBER%/

REM 8. 배포 확인 (PowerShell 사용)
echo [INFO] 배포 상태를 확인합니다 (30초 후)...
timeout /t 30 /nobreak >nul

powershell -Command "try { $response = Invoke-WebRequest -Uri 'https://word1600.github.io/game/unit%UNIT_NUMBER%/' -Method Head -TimeoutSec 10; if ($response.StatusCode -eq 200) { Write-Host '[SUCCESS] Unit %UNIT_NUMBER% 배포 완료! 🎉' -ForegroundColor Green; Write-Host '[SUCCESS] 접속 URL: https://word1600.github.io/game/unit%UNIT_NUMBER%/' -ForegroundColor Green } else { Write-Host '[WARNING] 아직 배포가 완료되지 않았습니다. 잠시 후 다시 확인해주세요.' -ForegroundColor Yellow } } catch { Write-Host '[WARNING] 배포 상태 확인 실패. 수동으로 확인해주세요.' -ForegroundColor Yellow }"

echo [SUCCESS] Unit %UNIT_NUMBER% 배포 프로세스 완료!
echo [INFO] 다음 단계: 온라인에서 게임 테스트

pause
