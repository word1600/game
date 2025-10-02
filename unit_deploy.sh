#!/bin/bash

# Unit 자동 배포 스크립트
# 사용법: ./unit_deploy.sh [Unit번호] [커밋메시지]

set -e  # 오류 발생 시 스크립트 중단

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 함수 정의
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 매개변수 확인
if [ $# -lt 1 ]; then
    print_error "사용법: $0 <Unit번호> [커밋메시지]"
    print_error "예시: $0 21"
    print_error "예시: $0 21 \"Add Unit 21 - TOEIC Word UFO Game\""
    exit 1
fi

UNIT_NUMBER=$1
COMMIT_MSG=${2:-"Add Unit $UNIT_NUMBER - TOEIC Word UFO Game"}

print_status "Unit $UNIT_NUMBER 배포를 시작합니다..."

# 1. 현재 디렉토리 확인
if [ ! -d "unit$UNIT_NUMBER" ]; then
    print_error "unit$UNIT_NUMBER 폴더가 존재하지 않습니다!"
    print_error "먼저 Unit $UNIT_NUMBER 파일들을 생성해주세요."
    exit 1
fi

# 2. Git 상태 확인
print_status "Git 상태를 확인합니다..."
if ! git status > /dev/null 2>&1; then
    print_error "Git 저장소가 아닙니다!"
    exit 1
fi

# 3. 변경사항 확인
print_status "변경사항을 확인합니다..."
if [ -z "$(git status --porcelain)" ]; then
    print_warning "커밋할 변경사항이 없습니다."
    exit 0
fi

# 4. 모든 파일 스테이징
print_status "변경사항을 스테이징합니다..."
git add .
print_success "파일 스테이징 완료"

# 5. 커밋 생성
print_status "커밋을 생성합니다..."
git commit -m "$COMMIT_MSG"
print_success "커밋 생성 완료: $COMMIT_MSG"

# 6. 원격 저장소에 푸시
print_status "원격 저장소에 푸시합니다..."
if git push origin main; then
    print_success "푸시 완료!"
else
    print_error "푸시 실패! 수동으로 확인해주세요."
    exit 1
fi

# 7. 배포 상태 확인
print_status "배포 상태를 확인합니다..."
print_warning "GitHub Pages 배포는 약 2-5분 소요됩니다."
print_status "배포 완료 후 다음 URL에서 확인하세요:"
print_status "https://word1600.github.io/game/unit$UNIT_NUMBER/"

# 8. 배포 확인 스크립트 실행 (선택사항)
if command -v curl > /dev/null 2>&1; then
    print_status "배포 상태를 확인합니다 (30초 후)..."
    sleep 30
    
    URL="https://word1600.github.io/game/unit$UNIT_NUMBER/"
    if curl -s --head "$URL" | head -n 1 | grep -q "200 OK"; then
        print_success "Unit $UNIT_NUMBER 배포 완료! 🎉"
        print_success "접속 URL: $URL"
    else
        print_warning "아직 배포가 완료되지 않았습니다. 잠시 후 다시 확인해주세요."
        print_warning "URL: $URL"
    fi
else
    print_warning "curl이 설치되지 않아 자동 확인을 건너뜁니다."
    print_warning "수동으로 URL을 확인해주세요: https://word1600.github.io/game/unit$UNIT_NUMBER/"
fi

print_success "Unit $UNIT_NUMBER 배포 프로세스 완료!"
print_status "다음 단계: 온라인에서 게임 테스트"
