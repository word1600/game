# Unit 12 생성 완벽 가이드
## 🎯 **스트레스 없는 원활한 진행을 위한 완벽한 체크리스트**

---

## 📋 **Unit 12 생성 전 필수 준비사항**

### **1. 데이터 준비 (가장 중요!)**
```bash
# 1단계: 데이터 파일 존재 확인
ls data/unit12.json

# 2단계: JSON 검증 (필수!)
python json_validator.py data/unit12.json
```
**✅ 검증 통과 시에만 다음 단계 진행**

### **2. 템플릿 확인**
- [ ] Unit 11 폴더 구조 완벽 확인
- [ ] Unit 11 게임 기능 정상 작동 확인
- [ ] 최신 수정사항 반영 상태 확인

---

## 🚀 **Unit 12 생성 단계별 실행 가이드**

### **Step 1: 폴더 생성**
```bash
# Unit 11을 템플릿으로 Unit 12 폴더 생성
xcopy "unit11" "unit12" /E /I /H

# 생성 확인
dir unit12
```

### **Step 2: 데이터 파일 관리**
```bash
# Unit 12 데이터 파일 복사
copy data\unit12.json unit12\data\unit12.json

# 불필요한 데이터 파일 삭제
del unit12\data\unit*.json

# Unit 12 전용 데이터만 복사
copy data\unit12.json unit12\data\unit12.json
```

### **Step 3: 파일 수정 (체계적으로 진행)**

#### **3.1 index.html 수정**
```html
<!-- 변경 전 -->
<h1 class="game-title">TOEIC WORD 1600 / <span class="unit-text">Unit 11</span></h1>

<!-- 변경 후 -->
<h1 class="game-title">TOEIC WORD 1600 / <span class="unit-text">Unit 12</span></h1>
```

```html
<!-- 캐시 버전 업데이트 -->
<link rel="stylesheet" href="./style.css?v=1.21">
<script src="./game.js?v=1.13"></script>

<!-- 메타 태그 업데이트 -->
<meta http-equiv="Last-Modified" content="Mon, 05 Sep 2025 09:00:00 GMT">
```

#### **3.2 game.js 수정 (중요!)**
```javascript
// 1. 기본 유닛 변경
let selectedUnit = 'unit12'; // 기본값: Unit 12

// 2. 데이터 파일 경로 수정
const file = isLocal ? './data/unit12.json' : '/game/unit12/data/unit12.json';

// 3. 에셋 경로 수정 (모든 위치에서)
const assetsPath = isLocal ? './assets/' : '/game/unit12/assets/';

// 4. getLatestUnitJsonFile() 함수 수정 (중요!)
function getLatestUnitJsonFile() {
  return fetch('/game/unit12/data/unit12.json')
    .then(r => r.ok ? r.json() : null)
    .catch(() => null)
    .then(data => {
      if (!data) throw new Error('단어 데이터를 불러오지 못했습니다.');
      return data;
    });
}

// 5. 로그 메시지 수정
console.log('🔍 Unit 12: 단어 데이터 로딩 시작:', file);
console.log('📡 Unit 12: 서버 응답:', response.status, response.ok);
console.log('✅ Unit 12: 데이터 로드 성공! 단어 수:', data.length);
console.log('📝 Unit 12: 첫 번째 단어:', data[0]);
console.error('❌ Unit 12: 데이터 로드 실패:', err);
alert('Unit 12 단어 데이터를 불러오지 못했습니다: ' + err.message);
```

### **Step 4: README.md 생성**
```markdown
# Unit 12 - TOEIC WORD 1600 UFO 게임

## 📅 **생성 정보**
- **생성일**: 2025년 9월 5일
- **생성 방법**: Unit 11 템플릿 기반
- **총 단어 수**: [단어 수]개

## 🎯 **게임 특징**
- **게임 시간**: 5분 타이머
- **점수 시스템**: 정답 +10점 / 오답 -5점
- **보너스 게임**: 타이핑 게임 (+5점)
- **TTS 지원**: 미국식/영국식 발음
- **UFO 격추 게임**: 단어 맞추기

## 📚 **단어 카테고리**
[단어 카테고리별 분류]

## 🚀 **접속 방법**
- **온라인**: `https://word1600.github.io/game/unit12/`
- **로컬**: `http://localhost:8000/unit12/`
```

---

## 🧪 **로컬 테스트 가이드**

### **Step 1: 서버 실행**
```bash
python -m http.server 8000
```

### **Step 2: 올바른 URL 접속**
```
http://localhost:8000/unit12/
```
**⚠️ 중요**: 반드시 `/unit12/`로 끝나야 함!

### **Step 3: 브라우저 캐시 문제 해결**
1. **강제 새로고침**: `Ctrl + F5`
2. **개발자 도구**: `F12` → Network 탭 → "Disable cache" 체크
3. **시크릿 모드**: `Ctrl + Shift + N` (Chrome)

### **Step 4: 테스트 체크리스트**
- [ ] 게임 제목: "Unit 12" 표시
- [ ] 단어 데이터 정상 로드 (콘솔 로그 확인)
- [ ] UFO 생성 및 움직임
- [ ] 마우스/터치로 UFO 격추
- [ ] 정답/오답 처리
- [ ] 점수 시스템 작동
- [ ] 타이머 카운트다운
- [ ] 보너스 타이핑 게임
- [ ] TTS 발음 기능
- [ ] 사운드 효과 재생

---

## 📤 **배포 가이드**

### **Step 1: Git 스테이징**
```bash
git add unit12/
git add data/unit12.json
```

### **Step 2: 커밋**
```bash
git commit -m "Unit 12 게임 생성 및 배포 완료

- Unit 12 폴더 구조 생성 (Unit 11 템플릿 기반)
- [단어 수]개 단어 데이터 포함 ([주제] 관련)
- 게임 엔진 및 UI Unit 12 전용으로 수정
- 단어 로딩 경로 및 에셋 경로 수정
- README.md 파일 생성
- 로컬 테스트 완료"
```

### **Step 3: 푸시**
```bash
git push origin main
```

### **Step 4: 배포 확인**
- **온라인 URL**: `https://word1600.github.io/game/unit12/`
- **배포 시간**: 1-5분 소요
- **모든 기능 정상 작동 확인**

---

## ⚠️ **자주 발생하는 문제와 해결 방법**

### **문제 1: 잘못된 URL 접속**
- **증상**: Unit 1이 표시됨
- **원인**: `localhost:8000/` (루트)로 접속
- **해결**: `localhost:8000/unit12/`로 접속

### **문제 2: UFO가 나타나지 않음**
- **증상**: UFO 이미지 404 오류
- **원인**: 에셋 경로 수정 누락
- **해결**: `game.js`에서 모든 `/game/unit11/` → `/game/unit12/` 변경

### **문제 3: 잘못된 단어 표시**
- **증상**: 이전 Unit 단어들이 표시됨
- **원인**: `getLatestUnitJsonFile()` 함수 미수정
- **해결**: 함수 내부 경로를 unit12로 수정

### **문제 4: 브라우저 캐시 문제**
- **증상**: 이전 버전 파일 로드
- **원인**: 브라우저 캐시
- **해결**: 강제 새로고침 (`Ctrl + F5`) 및 캐시 버전 업데이트

### **문제 5: JSON 데이터 오류**
- **증상**: 단어 로딩 실패
- **원인**: JSON 형식 오류
- **해결**: `python json_validator.py data/unit12.json` 실행

---

## 🎯 **Unit 12 생성 성공 기준**

### **기능적 완성도**
- [ ] 모든 게임 기능 정상 작동
- [ ] 단어 데이터 정상 로드
- [ ] 사용자 인터페이스 완성

### **기술적 완성도**
- [ ] 코드 오류 없음
- [ ] 경로 참조 정확성
- [ ] 브라우저 호환성

### **배포 완성도**
- [ ] 온라인 접속 가능
- [ ] 모든 에셋 정상 로드
- [ ] 사용자 경험 최적화

---

## 📝 **Unit 12 생성 후 작업**

### **1. 문서화**
- [ ] Unit 12 생성 보고서 작성
- [ ] 워크플로우 가이드 업데이트
- [ ] 다음 Unit 생성 템플릿 준비

### **2. 품질 관리**
- [ ] 사용자 피드백 수집
- [ ] 버그 리포트 모니터링
- [ ] 성능 최적화 검토

### **3. 다음 단계 준비**
- [ ] Unit 13 생성 계획 수립
- [ ] 새로운 기능 개발 검토
- [ ] 사용자 요청사항 반영

---

## 🚀 **최종 체크리스트**

### **생성 전**
- [ ] `data/unit12.json` 존재 및 검증 완료
- [ ] Unit 11 템플릿 상태 확인
- [ ] 필요한 도구 준비 완료

### **생성 중**
- [ ] 폴더 구조 생성 완료
- [ ] 모든 파일 수정 완료
- [ ] 데이터 파일 관리 완료
- [ ] README.md 생성 완료

### **테스트**
- [ ] 올바른 URL로 접속
- [ ] 브라우저 캐시 문제 해결
- [ ] 모든 기능 정상 작동 확인

### **배포**
- [ ] Git 커밋 및 푸시 완료
- [ ] 온라인 배포 확인
- [ ] 문서화 완료

---

**🎉 이 가이드를 따라하면 Unit 12 생성이 스트레스 없이 원활하게 진행됩니다!**

**작성일**: 2025년 9월 5일  
**목적**: Unit 12 원활한 생성  
**상태**: 완료


