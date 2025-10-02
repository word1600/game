# Unit 11 생성 준비 템플릿

## 📅 **생성 예정일**: 2025년 9월 5일 이후

## 🎯 **Unit 11 생성 목표**
- Unit 11 UFO Word Game 생성 및 온라인 배포
- Unit 10을 템플릿으로 사용하여 최신 기능 반영
- 새로운 단어 데이터 통합 및 게임 최적화

## 📋 **Unit 11 생성 체크리스트**

### **1. 데이터 준비 단계**
- [ ] `data/unit11.json` 파일 존재 확인
- [ ] JSON 검증 도구로 데이터 검증 실행
  ```bash
  python json_validator.py data/unit11.json
  ```
- [ ] 단어 수 및 주제 확인
- [ ] 데이터 품질 검증 (오탈자, 중복, 형식 등)

### **2. 템플릿 준비 단계**
- [ ] Unit 10 폴더 구조 확인
- [ ] Unit 10 게임 기능 검증
- [ ] 최신 수정사항 반영 상태 확인

### **3. Unit 11 폴더 생성**
```bash
# Unit 11 폴더 생성 (Unit 10 템플릿 기반)
xcopy "unit10" "unit11" /E /I /H

# 데이터 파일 복사
copy data\unit11.json unit11\data\unit11.json

# 불필요한 데이터 파일 정리
del unit11\data\unit*.json
copy data\unit11.json unit11\data\unit11.json
```

### **4. 파일 수정 작업**

#### **4.1 index.html 수정**
- [ ] 게임 제목: "Unit 10" → "Unit 11"
- [ ] 메타 태그 업데이트 (Last-Modified 등)
- [ ] 캐시 무효화 설정 확인

#### **4.2 game.js 수정**
- [ ] `selectedUnit`: 'unit10' → 'unit11'
- [ ] `loadWords()` 함수: `unit10.json` → `unit11.json`
- [ ] `getLatestUnitJsonFile()`: 경로 수정
- [ ] 모든 에셋 경로: `/game/unit10/` → `/game/unit11/`
- [ ] 로그 메시지: "Unit 10" → "Unit 11"
- [ ] 에러 메시지: "Unit 10" → "Unit 11"

#### **4.3 README.md 생성**
- [ ] Unit 11 전용 문서 작성
- [ ] 단어 카테고리별 분류 및 설명
- [ ] 게임 특징 및 접속 방법 포함
- [ ] 생성일 및 생성 방법 기록

### **5. 로컬 테스트 단계**
```bash
# 로컬 서버 실행
python -m http.server 8000

# 브라우저에서 접속 테스트
# http://localhost:8000/unit11/
```

#### **5.1 테스트 항목**
- [ ] 게임 로딩 정상 작동
- [ ] 단어 데이터 정상 로드
- [ ] UFO 생성 및 격추 기능
- [ ] TTS 발음 기능
- [ ] 보너스 타이핑 게임
- [ ] 점수 시스템 작동
- [ ] 타이머 기능
- [ ] 사운드 효과

#### **5.2 문제 해결**
- [ ] 단어 로딩 실패 시: `game.js` 경로 참조 확인
- [ ] 에셋 로딩 실패 시: 에셋 경로 확인
- [ ] 콘솔 로그 확인하여 오류 메시지 분석
- [ ] 브라우저 개발자 도구 활용

### **6. Git 커밋 및 배포**

#### **6.1 Git 스테이징**
```bash
# Unit 11 관련 파일 추가
git add unit11/
git add data/unit11.json
```

#### **6.2 커밋 메시지 템플릿**
```
Unit 11 게임 생성 및 배포 완료

- Unit 11 폴더 구조 생성 (Unit 10 템플릿 기반)
- [단어 수]개 단어 데이터 포함 ([주제] 관련)
- 게임 엔진 및 UI Unit 11 전용으로 수정
- 단어 로딩 경로 및 에셋 경로 수정
- README.md 파일 생성
- 로컬 테스트 완료
```

#### **6.3 배포 실행**
```bash
# 커밋
git commit -m "Unit 11 게임 생성 및 배포 완료
- Unit 11 폴더 구조 생성 (Unit 10 템플릿 기반)
- [단어 수]개 단어 데이터 포함 ([주제] 관련)
- 게임 엔진 및 UI Unit 11 전용으로 수정
- 단어 로딩 경로 및 에셋 경로 수정
- README.md 파일 생성
- 로컬 테스트 완료"

# 푸시
git push origin main
```

### **7. 배포 확인**
- [ ] 온라인 URL 접속: `https://word1600.github.io/game/unit11/`
- [ ] GitHub Pages 배포 완료 확인 (1-5분 소요)
- [ ] 모든 기능 정상 작동 확인
- [ ] 모바일 환경에서도 테스트

## 🔧 **Unit 10에서 Unit 11로 변경해야 할 항목들**

### **파일별 수정 사항**

#### **index.html**
```html
<!-- 변경 전 -->
<h1 class="game-title">TOEIC WORD 1600 / <span class="unit-text">Unit 10</span></h1>

<!-- 변경 후 -->
<h1 class="game-title">TOEIC WORD 1600 / <span class="unit-text">Unit 11</span></h1>
```

#### **game.js**
```javascript
// 변경 전
let selectedUnit = 'unit10'; // 기본값: Unit 10

// 변경 후
let selectedUnit = 'unit11'; // 기본값: Unit 11
```

```javascript
// 변경 전
const file = isLocal ? './data/unit10.json' : '/game/unit10/data/unit10.json';

// 변경 후
const file = isLocal ? './data/unit11.json' : '/game/unit11/data/unit11.json';
```

```javascript
// 변경 전
const assetsPath = isLocal ? './assets/' : '/game/unit10/assets/';

// 변경 후
const assetsPath = isLocal ? './assets/' : '/game/unit11/assets/';
```

```javascript
// 변경 전
console.log('🔍 Unit 10: 단어 데이터 로딩 시작:', file);

// 변경 후
console.log('🔍 Unit 11: 단어 데이터 로딩 시작:', file);
```

## 📊 **Unit 11 생성 후 확인 사항**

### **기능 테스트**
- [ ] 게임 시작 화면 정상 표시
- [ ] 단어 데이터 정상 로드 (콘솔 로그 확인)
- [ ] UFO 생성 및 움직임
- [ ] 마우스/터치로 UFO 격추
- [ ] 정답/오답 처리
- [ ] 점수 시스템 작동
- [ ] 타이머 카운트다운
- [ ] 보너스 타이핑 게임
- [ ] TTS 발음 기능
- [ ] 사운드 효과 재생
- [ ] 게임 종료 처리

### **성능 테스트**
- [ ] 로딩 속도 확인
- [ ] 메모리 사용량 확인
- [ ] 브라우저 호환성 확인
- [ ] 모바일 반응형 확인

### **배포 확인**
- [ ] 온라인 URL 정상 접속
- [ ] 모든 에셋 정상 로드
- [ ] GitHub Pages 배포 상태 확인
- [ ] CDN 캐시 반영 확인

## 🎯 **Unit 11 생성 성공 기준**

1. **기능적 완성도**
   - 모든 게임 기능 정상 작동
   - 단어 데이터 정상 로드
   - 사용자 인터페이스 완성

2. **기술적 완성도**
   - 코드 오류 없음
   - 경로 참조 정확성
   - 브라우저 호환성

3. **배포 완성도**
   - 온라인 접속 가능
   - 모든 에셋 정상 로드
   - 사용자 경험 최적화

## 📝 **Unit 11 생성 완료 후 작업**

1. **문서화**
   - Unit 11 생성 보고서 작성
   - 워크플로우 가이드 업데이트
   - 다음 Unit 생성 템플릿 준비

2. **품질 관리**
   - 사용자 피드백 수집
   - 버그 리포트 모니터링
   - 성능 최적화 검토

3. **다음 단계 준비**
   - Unit 12 생성 계획 수립
   - 새로운 기능 개발 검토
   - 사용자 요청사항 반영

---
**작성일**: 2025년 9월 5일  
**작성자**: AI Assistant  
**상태**: 준비 완료



















