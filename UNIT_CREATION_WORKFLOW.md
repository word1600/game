# UFO Word Game Unit 생성 워크플로우
# JSON 파일 검증 → 게임 생성 → 배포

## 🔍 **1단계: JSON 파일 검증**

### **검증 도구 실행**
```bash
# JSON 파일 검증 (Unit 10 예시)
python json_validator.py data/unit10.json
```

### **검증 항목**
- ✅ JSON 구조 정상성
- ✅ 필수 필드 존재 (`ko`, `en`, `pos`)
- ✅ 빈 값 확인
- ✅ 영문 단어 형식 (영문자, 공백, 하이픈, 아포스트로피만)
- ✅ 한글 단어 형식 (한글, 영문자, 숫자, 공백, 쉼표, 괄호만)
- ✅ 품사 형식 검증
- ✅ 중복 단어 확인
- ✅ 연속된 공백 확인

### **검증 통과 시에만 다음 단계 진행**

## 🚀 **2단계: 게임 생성**

### **검증 통과 후 실행**
```bash
# Unit 폴더 생성 (Unit 10 예시)
xcopy "unit9" "unit10" /E /I /H

# 데이터 파일 복사
copy data\unit10.json unit10\data\unit10.json

# 불필요한 데이터 파일 삭제
del unit10\data\unit6.json
del unit10\data\unit7.json
del unit10\data\unit8.json
del unit10\data\unit9.json
```

### **파일 수정 작업**
1. **index.html 수정**
   - 게임 제목: "Unit 9" → "Unit 10"

2. **game.js 수정**
   - `selectedUnit`: 'unit9' → 'unit10'
   - `loadWords()` 함수: `unit9.json` → `unit10.json`
   - `getLatestUnitJsonFile()`: 경로 수정
   - 모든 에셋 경로: `/game/unit9/` → `/game/unit10/`
   - 로그 메시지: "Unit 9" → "Unit 10"

3. **README.md 생성**
   - Unit 전용 문서 작성
   - 단어 카테고리별 분류
   - 게임 특징 및 접속 방법 포함

## 📤 **3단계: 배포**

### **로컬 테스트**
```bash
# 로컬 서버 실행
python -m http.server 8000

# 브라우저에서 접속 테스트
# http://localhost:8000/unit10/
```

### **문제 해결**
- 단어 로딩 실패 시: `game.js`의 경로 참조 확인
- 에셋 로딩 실패 시: 에셋 경로 확인
- 콘솔 로그 확인하여 오류 메시지 분석

### **온라인 배포**
```bash
# Git 스테이징
git add unit10/
git add data/unit10.json

# 커밋
git commit -m "Unit 10 게임 생성 및 배포 완료
- Unit 10 폴더 구조 생성 (Unit 9 템플릿 기반)
- 54개 단어 데이터 포함
- 게임 엔진 및 UI Unit 10 전용으로 수정
- 단어 로딩 경로 및 에셋 경로 수정
- README.md 파일 생성
- 로컬 테스트 완료"

# 푸시
git push origin main
```

### **배포 확인**
- 온라인 URL: `https://word1600.github.io/game/unit10/`
- GitHub Pages 배포 완료 확인 (1-5분 소요)

## ⚠️ **오류 발생 시 대응**

### **JSON 오류 수정 가이드**
1. **빈 필드**: 해당 필드에 올바른 값 입력
2. **형식 오류**: 영문/한글 형식 규칙 준수
3. **품사 오류**: 허용된 품사 형식 사용
4. **중복 단어**: 중복 제거 또는 수정

### **허용된 품사 형식**
- `n.`, `v.`, `adj.`, `adv.`, `prep.`, `conj.`, `interj.`
- `n.(명사)`, `v.(동사)`, `adj.(형용사)`, `adv.(부사)`
- `prep.(전치사)`, `conj.(접속사)`, `interj.(감탄사)`
- `n. phr.`, `v. phr.`, `adj. phr.`, `adv. phr.`
- `v.past`, `v.s`, `v.ing`

## 📊 **Unit 10 생성 성공 사례**

### **Unit 10 생성 과정**
```
🔍 Unit 10 생성 시작...
==================================================
✅ 기존 유닛 구조 확인 완료
✅ Unit 9 템플릿 복사 완료 (31개 파일)
✅ Unit 10 전용 파일 수정 완료
✅ 데이터 파일 경로 수정 완료
✅ 로컬 테스트 성공
✅ Git 커밋 및 배포 완료

==================================================
📊 Unit 10 생성 결과:
   - 총 단어 수: 54개
   - 생성된 파일: 28개
   - 수정된 파일: 4개
   - 온라인 URL: https://word1600.github.io/game/unit10/
🎉 Unit 10 생성 및 배포 완료!
```

### **주요 수정 사항**
- `index.html`: 제목 "Unit 9" → "Unit 10"
- `game.js`: 모든 경로 참조 수정
- `data/unit10.json`: 54개 단어 데이터
- `README.md`: Unit 10 전용 문서

## 📋 **Unit 11 생성 준비 체크리스트**

### **1. 데이터 준비**
- [ ] `data/unit11.json` 파일 존재 확인
- [ ] JSON 검증 도구로 데이터 검증
- [ ] 단어 수 및 주제 확인

### **2. 템플릿 선택**
- [ ] Unit 10을 템플릿으로 사용
- [ ] 최신 기능 및 수정사항 반영

### **3. 생성 명령어**
```bash
# Unit 11 폴더 생성
xcopy "unit10" "unit11" /E /I /H

# 데이터 파일 복사
copy data\unit11.json unit11\data\unit11.json

# 불필요한 데이터 파일 삭제
del unit11\data\unit*.json
copy data\unit11.json unit11\data\unit11.json
```

### **4. 수정 작업**
- [ ] `index.html`: 제목 "Unit 10" → "Unit 11"
- [ ] `game.js`: 모든 "unit10" → "unit11" 변경
- [ ] `README.md`: Unit 11 전용 내용 작성

### **5. 테스트 및 배포**
- [ ] 로컬 테스트 실행
- [ ] 문제 발생 시 경로 수정
- [ ] Git 커밋 및 푸시
- [ ] 온라인 배포 확인

## 🎯 **결론**

**JSON 파일 검증은 게임 생성 전 필수 단계입니다!**

- ✅ 오탈자 사전 방지
- ✅ 게임 오류 최소화
- ✅ 사용자 경험 향상
- ✅ 배포 후 문제 예방

**검증 통과 후에만 게임 생성을 진행하시기 바랍니다!**



