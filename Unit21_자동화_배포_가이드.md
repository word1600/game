# Unit 21+ 자동화 배포 가이드

## 🎯 목적
Unit 20에서 발생한 문제를 재발 방지하고, 향후 Unit 생성 시 완벽한 자동화를 보장합니다.

---

## 📋 사전 준비사항

### 1. 필수 파일 확인
- [ ] `data/unitN.json` - Unit N 단어 데이터 파일 존재
- [ ] `enhanced_validator.py` - 데이터 검증 도구 준비
- [ ] 이전 Unit 템플릿 (unit19 또는 unit20) 준비

### 2. 환경 설정
- [ ] Git 저장소 상태 확인 (`git status`)
- [ ] 원격 저장소 연결 확인 (`git remote -v`)
- [ ] VS Code 터미널 준비 (한국어 경로 문제 회피)

---

## 🚀 자동화 배포 프로세스

### 방법 1: 자동화 스크립트 사용 (권장)

#### Windows 환경
```cmd
# Unit 21 배포 예시
unit_deploy.bat 21

# 커스텀 커밋 메시지와 함께
unit_deploy.bat 21 "Add Unit 21 - TOEIC Word UFO Game with new features"
```

#### Linux/Mac 환경
```bash
# 실행 권한 부여 (최초 1회만)
chmod +x unit_deploy.sh

# Unit 21 배포 예시
./unit_deploy.sh 21

# 커스텀 커밋 메시지와 함께
./unit_deploy.sh 21 "Add Unit 21 - TOEIC Word UFO Game with new features"
```

### 방법 2: 수동 배포 (스크립트 실패 시)

#### 1단계: 파일 생성 및 테스트
```bash
# Unit N 폴더 생성 및 파일 복사
# (이전 Unit 템플릿 기반으로 수동 복사)

# 로컬 테스트
python -m http.server 8000
# 브라우저에서 http://localhost:8000/unitN/ 접속 테스트
```

#### 2단계: Git 배포
```bash
# 모든 변경사항 스테이징
git add .

# 커밋 생성
git commit -m "Add Unit N - TOEIC Word UFO Game"

# 원격 저장소에 푸시
git push origin main
```

#### 3단계: 배포 확인
```bash
# Git 상태 확인
git status

# 배포 완료 대기 (2-5분)
# 온라인 접속 테스트: https://word1600.github.io/game/unitN/
```

---

## 🔧 문제 해결 가이드

### 문제 1: 스크립트 실행 권한 오류
**증상**: `Permission denied` 또는 `Access denied`
**해결책**:
```bash
# Linux/Mac
chmod +x unit_deploy.sh

# Windows (관리자 권한으로 실행)
# 또는 PowerShell에서 실행 정책 변경
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 문제 2: Git 푸시 실패
**증상**: `git push origin main` 실패
**해결책**:
```bash
# 원격 저장소 상태 확인
git remote -v

# 인증 문제인 경우 Personal Access Token 사용
git config --global credential.helper store

# 강제 푸시 (주의: 다른 변경사항 덮어쓸 수 있음)
git push origin main --force
```

### 문제 3: 한국어 경로 문제
**증상**: PowerShell에서 경로 인식 오류
**해결책**:
- VS Code 터미널 사용
- 또는 Git Bash 사용
- 또는 영어 경로로 프로젝트 이동

### 문제 4: 배포 지연
**증상**: 푸시는 성공했지만 온라인 접속 불가
**해결책**:
- GitHub Actions 탭에서 배포 상태 확인
- 5-10분 대기 후 재시도
- GitHub Pages 설정 확인

---

## 📊 배포 상태 확인 방법

### 1. GitHub Actions 확인
1. GitHub 저장소 → Actions 탭
2. 최근 워크플로우 실행 상태 확인
3. 실패 시 로그 확인하여 오류 원인 파악

### 2. 온라인 접속 테스트
```bash
# curl로 상태 확인 (Linux/Mac)
curl -I https://word1600.github.io/game/unitN/

# PowerShell로 상태 확인 (Windows)
Invoke-WebRequest -Uri "https://word1600.github.io/game/unitN/" -Method Head
```

### 3. 브라우저 테스트
- URL: `https://word1600.github.io/game/unitN/`
- 게임 로딩 확인
- 단어 데이터 로드 확인
- 게임 기능 테스트

---

## 🎯 Unit 생성 체크리스트

### 사전 준비
- [ ] Unit N 데이터 파일 준비 (`data/unitN.json`)
- [ ] 데이터 검증 통과 (`python enhanced_validator.py data/unitN.json`)
- [ ] 이전 Unit 템플릿 준비
- [ ] Git 저장소 상태 확인

### 파일 생성
- [ ] `unitN/` 폴더 생성
- [ ] 모든 파일 복사 및 수정
- [ ] `index.html` 제목 수정
- [ ] `game.js` 경로 및 로그 메시지 수정
- [ ] `style.css` 버전 업데이트
- [ ] `README.md` 생성

### 로컬 테스트
- [ ] 로컬 서버 실행 (`python -m http.server 8000`)
- [ ] 브라우저 접속 테스트
- [ ] 게임 기능 정상 작동 확인
- [ ] 단어 데이터 정상 로드 확인

### 배포
- [ ] 자동화 스크립트 실행 또는 수동 배포
- [ ] Git 상태 확인 (`git status`)
- [ ] 모든 파일 스테이징 (`git add .`)
- [ ] 커밋 생성 (`git commit`)
- [ ] 원격 푸시 (`git push origin main`)

### 배포 확인
- [ ] GitHub Actions 상태 확인
- [ ] 온라인 접속 테스트
- [ ] 게임 기능 최종 검증
- [ ] 배포 완료 보고서 작성

---

## 🚨 주의사항

### 1. Git 작업 전 필수 확인
- 현재 브랜치 확인 (`git branch`)
- 원격 저장소 상태 확인 (`git status`)
- 다른 작업자와의 충돌 방지

### 2. 데이터 품질 관리
- 모든 단어 데이터는 검증기 통과 필수
- 발음 문제 단어 사전 제거
- 품사 표기 일관성 유지

### 3. 파일 구조 일관성
- 모든 Unit은 동일한 파일 구조 유지
- 에셋 파일 경로 정확성 확인
- 상대 경로 사용 권장

### 4. 배포 타이밍
- 작업 시간대 고려 (GitHub 서버 부하)
- 다른 Unit 배포와 충돌 방지
- 배포 후 충분한 테스트 시간 확보

---

## 📈 성능 최적화 팁

### 1. 배포 속도 향상
- 불필요한 파일 제외 (`.gitignore` 활용)
- 압축 가능한 파일 최적화
- 이미지 파일 크기 최적화

### 2. 안정성 향상
- 배포 전 로컬 테스트 철저히
- 단계별 검증 로직 추가
- 롤백 계획 수립

### 3. 모니터링 강화
- 배포 상태 자동 알림
- 성능 지표 추적
- 오류 로그 수집

---

## 🎉 성공 지표

### 정량적 지표
- 배포 시간: 30분 이내 (이전 Unit 수준)
- 오류 발생률: 0%
- 수동 개입 필요성: 최소화

### 정성적 지표
- 사용자 만족도 향상
- 개발자 스트레스 감소
- 프로젝트 안정성 확보

---

## 🔄 지속적 개선

### 1. 피드백 수집
- 각 Unit 배포 후 문제점 기록
- 사용자 피드백 수집
- 개선 사항 식별

### 2. 도구 업데이트
- 자동화 스크립트 지속적 개선
- 검증 도구 기능 확장
- 모니터링 시스템 강화

### 3. 문서화 업데이트
- 새로운 문제 해결 방법 추가
- 베스트 프랙티스 공유
- 트러블슈팅 가이드 확장

---

## 🏆 결론

이 가이드를 통해 Unit 20에서 발생한 문제를 완전히 예방하고, 향후 모든 Unit을 효율적으로 배포할 수 있습니다.

**핵심 성공 요소:**
1. **자동화 스크립트 활용** - 수동 작업 최소화
2. **단계별 검증** - 각 단계별 상태 확인
3. **문제 해결 준비** - 예상 문제에 대한 해결책 준비
4. **지속적 개선** - 피드백 기반 워크플로우 개선

**다음 Unit부터는 이 가이드를 따라 30분 내 완료를 목표로 합니다!** 🚀

---

*가이드 작성일: 2025년 10월 2일*  
*적용 대상: Unit 21부터 모든 향후 Unit*  
*목적: 완벽한 자동화 배포 보장*
