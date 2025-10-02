# 📋 Unit 18 생성 준비 가이드

## 📅 **작업 일시**
- **작업일**: 2025년 9월 23일 (화요일)
- **완료 시간**: 22:45
- **작업자**: AI Assistant

---

## 🎯 **Unit 17 생성 완료 요약**

### **✅ 성공적으로 완료된 작업**
1. **데이터 검증**: unit17.json (51개 단어) 검증 통과
2. **검증기 개선**: enhanced_validator.py에 pron.(대명사) 품사 지원 추가
3. **게임 생성**: Unit 16 템플릿 기반으로 Unit 17 완벽 생성
4. **로컬 테스트**: 모든 기능 정상 작동 확인
5. **온라인 배포**: GitHub Pages 자동 배포 완료
6. **문서화**: 완료 보고서 작성 완료

### **🌐 배포 정보**
- **온라인 URL**: `https://word1600.github.io/game/unit17/`
- **Git 커밋**: 4cf72c5
- **파일 수**: 27개 파일 추가
- **상태**: 정상 작동 확인됨

---

## 🚀 **Unit 18 생성 시 적용할 워크플로우**

### **🔍 1단계: 사전 준비 및 검증**
```bash
# 1. 데이터 파일 존재 확인
ls data/unit18.json

# 2. JSON 형식 검증 (오탈자 세심 확인)
python enhanced_validator.py data/unit18.json

# 3. 템플릿 상태 확인 (Unit 17 사용)
ls unit17/

# 4. 로컬 서버 환경 준비
python -m http.server 8000
```

**체크리스트**:
- [ ] 데이터 파일 존재
- [ ] JSON 검증 통과 (오류 0개)
- [ ] 오탈자 없음 확인
- [ ] 템플릿 폴더 정상
- [ ] 로컬 서버 실행

### **🚀 2단계: 게임 생성**
```bash
# 1. 폴더 생성 (Unit 17 템플릿 사용)
xcopy "unit17" "unit18" /E /I /H

# 2. 데이터 파일 복사
copy data\unit18.json unit18\data\unit18.json
del unit18\data\unit17.json

# 3. 파일 수정 (수동)
# - index.html: 제목, 버전 수정
# - game.js: 경로 및 설정 변경
# - README.md: Unit 18 전용 문서 생성
```

**체크리스트**:
- [ ] 폴더 생성 완료
- [ ] 데이터 파일 복사 완료
- [ ] index.html 수정 완료
- [ ] game.js 수정 완료
- [ ] README.md 생성 완료

### **🧪 3단계: 로컬 테스트**
```bash
# 브라우저에서 접속 테스트
# http://localhost:8000/unit18/
```

**체크리스트**:
- [ ] 게임 시작 화면 정상
- [ ] 단어 로딩 정상
- [ ] 게임 플레이 정상
- [ ] 음향 효과 정상
- [ ] TTS 기능 정상

### **📤 4단계: 온라인 배포**
```bash
# 1. Git 스테이징
git add unit18/

# 2. 커밋
git commit -m "Unit 18 게임 생성 및 배포 완료
- 상세한 작업 내역 포함"

# 3. 푸시
git push origin main
```

**체크리스트**:
- [ ] Git 스테이징 완료
- [ ] 커밋 메시지 작성 완료
- [ ] GitHub 푸시 완료
- [ ] 배포 URL 접속 확인

### **📝 5단계: 문서화**
- [ ] 배포 보고서 작성
- [ ] 프로젝트 현황 업데이트
- [ ] 다음 단계 준비

---

## 🔧 **Unit 18 생성 시 수정할 파일들**

### **1. index.html 수정 사항**
```html
<!-- 제목 변경 -->
<h1 class="game-title">TOEIC WORD 1600 / <span class="unit-text">Unit 18</span></h1>

<!-- 버전 업데이트 -->
<link rel="stylesheet" href="./style.css?v=1.27">
<script src="./game.js?v=1.19"></script>

<!-- 메타 태그 업데이트 -->
<meta http-equiv="Last-Modified" content="Mon, 23 Sep 2025 22:45:00 GMT">
```

### **2. game.js 수정 사항**
```javascript
// 기본 유닛 변경
let selectedUnit = 'unit18';

// 데이터 파일 경로 수정
const file = isLocal ? './data/unit18.json' : '/game/unit18/data/unit18.json';

// 에셋 경로 수정
const assetsPath = isLocal ? './assets/' : '/game/unit18/assets/';

// getLatestUnitJsonFile() 함수 수정
function getLatestUnitJsonFile() {
  return fetch('/game/unit18/data/unit18.json')
    .then(r => r.ok ? r.json() : null)
    .catch(() => null)
    .then(data => {
      if (!data) throw new Error('단어 데이터를 불러오지 못했습니다.');
      return data;
    });
}

// 모든 로그 메시지 수정
console.log('🔍 Unit 18: 단어 데이터 로딩 시작:', file);
console.log('📡 Unit 18: 서버 응답:', response.status, response.ok);
console.log('✅ Unit 18: 데이터 로드 성공! 단어 수:', data.length);
console.log('📝 Unit 18: 첫 번째 단어:', data[0]);
console.error('❌ Unit 18: 데이터 로드 실패:', err);
alert('Unit 18 단어 데이터를 불러오지 못했습니다: ' + err.message);
```

### **3. README.md 생성 템플릿**
- Unit 18 전용 문서 작성
- 단어 카테고리별 분류
- 게임 특징 및 접속 방법 포함
- 학습 목표 및 업데이트 내역 포함

---

## ⚠️ **Unit 18 생성 시 주의사항**

### **데이터 품질 관리**
- **오탈자 방지**: enhanced_validator.py 필수 사용
- **품사 형식 일관성**: 표준화된 품사 형식 사용
- **중복 단어 확인**: 동일한 단어 중복 방지
- **공백 오류 방지**: 수동 검토로 뒤쪽 공백 제거

### **로컬 테스트 강화**
- **모든 기능 테스트**: 게임 플레이, 음향, TTS 등
- **브라우저 호환성**: 다양한 브라우저에서 테스트
- **모바일 반응성**: 모바일 환경에서 테스트

### **배포 안정성**
- **단계별 확인**: 각 단계마다 세심한 점검
- **롤백 계획**: 문제 발생 시 이전 버전으로 복구
- **모니터링**: 배포 후 정상 작동 확인

---

## 📊 **현재 프로젝트 현황**

### **완료된 Unit 목록 (총 17개)**
1. Unit 1 ✅
2. Unit 2 ✅
3. Unit 3 ✅
4. Unit 4 ✅
5. Unit 5 ✅
6. Unit 6 ✅
7. Unit 7 ✅
8. Unit 8 ✅
9. Unit 9 ✅
10. Unit 10 ✅
11. Unit 11 ✅
12. Unit 12 ✅
13. Unit 13 ✅
14. Unit 14 ✅
15. Unit 15 ✅
16. Unit 16 ✅
17. **Unit 17** ✅ **오늘 완료**

### **다음 목표**
- **Unit 18**: 다음 생성 목표
- **데이터 준비**: unit18.json 검증 필요
- **템플릿**: Unit 17 기반 생성 예정

---

## 🎯 **Unit 18 생성 시 체크리스트**

### **생성 전**
- [ ] unit18.json 데이터 파일 존재 확인
- [ ] enhanced_validator.py로 데이터 검증
- [ ] Unit 17 템플릿 상태 확인
- [ ] 로컬 서버 환경 준비

### **생성 중**
- [ ] Unit 17 폴더를 Unit 18로 복사
- [ ] 데이터 파일 복사 및 정리
- [ ] index.html 수정 (제목, 버전, 메타 태그)
- [ ] game.js 수정 (경로, 설정, 로그 메시지)
- [ ] README.md 생성

### **테스트**
- [ ] 로컬 서버에서 접속 테스트
- [ ] 게임 기능 정상 작동 확인
- [ ] 단어 데이터 정상 로드 확인
- [ ] 에셋 파일 정상 로드 확인

### **배포**
- [ ] Git 스테이징
- [ ] 커밋 메시지 작성
- [ ] GitHub 푸시
- [ ] 온라인 배포 확인

### **문서화**
- [ ] 완료 보고서 작성
- [ ] 프로젝트 현황 업데이트

---

## 🔍 **검증된 워크플로우의 장점**

1. **오류 방지**: 단계별 검증으로 실수 최소화
2. **효율성**: 체계적인 진행으로 시간 단축
3. **일관성**: 표준화된 프로세스로 품질 보장
4. **추적성**: 상세한 문서화로 문제 해결 용이
5. **확장성**: 다음 Unit 생성 시 동일한 프로세스 적용

---

**🎉 Unit 18 생성 시 이 가이드를 참고하여 원활한 작업을 진행하세요!**

**작성일**: 2025년 9월 23일 (화요일)  
**작성자**: AI Assistant  
**목적**: Unit 18 생성 준비 가이드  
**상태**: 완료 ✅







