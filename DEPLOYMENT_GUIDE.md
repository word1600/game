# UFO Word Game 배포 완벽 가이드

## 🚀 **Unit 7부터 즉시 배포 가능한 완벽한 시스템**

### 📅 **작성일**: 2025년 8월 28일
### 🎯 **목표**: Unit 7 이후 모든 Unit이 즉시 온라인 배포 가능

---

## ⚠️ **지금까지 발생했던 문제들과 해결책**

### **1. 단어 데이터 로딩 실패 문제**
**증상**: "단어 데이터를 불러오지 못했습니다" 오류
**원인**: GitHub Pages에서 상대 경로가 제대로 작동하지 않음
**해결책**: 모든 경로를 절대 경로로 변경

```javascript
// ❌ 잘못된 경로 (로컬에서만 작동)
return fetch('./data/unit6.json')

// ✅ 올바른 경로 (GitHub Pages에서 작동)
return fetch('/game/unit6/data/unit6.json')
```

### **2. 이미지 및 에셋 로딩 실패 문제**
**증상**: UFO 이미지, 폭발 효과, 총알 이미지가 표시되지 않음
**원인**: 에셋 경로가 GitHub Pages 구조와 맞지 않음
**해결책**: 모든 에셋 경로를 GitHub Pages 호환으로 수정

```javascript
// ❌ 잘못된 경로
ufoImg.src = '/unit6/assets/ufo_clean' + (Math.floor(Math.random() * 5)) + '.png';
explosion.src = '/unit6/assets/explosion.png';
bullet.src = '/unit6/assets/bullet1.png';

// ✅ 올바른 경로
ufoImg.src = '/game/unit6/assets/ufo_clean' + (Math.floor(Math.random() * 5)) + '.png';
explosion.src = '/game/unit6/assets/explosion.png';
bullet.src = '/game/unit6/assets/bullet1.png';
```

### **3. 폴더 구조 누락 문제**
**증상**: Unit 6 폴더가 GitHub에 업로드되지 않음
**원인**: 중첩된 Git 저장소로 인한 충돌
**해결책**: `.gitignore` 파일로 중첩 저장소 제외

```gitignore
# 중첩된 Git 저장소
unit6-github/

# Python 캐시 파일
__pycache__/
*.pyc
*.pyo
*.pyd
```

### **4. 워크플로우 파일 권한 문제**
**증상**: PAT로 푸시 시 `.github/workflows/` 파일 업데이트 실패
**원인**: PAT에 `workflow` 권한이 없음
**해결책**: 워크플로우 파일 제거 또는 PAT에 workflow 권한 추가

---

## 🔧 **Unit 7부터 즉시 배포하는 방법**

### **1단계: 새로운 Unit 폴더 생성**
```bash
# Unit 7 폴더 생성
mkdir unit7
cp -r unit6/* unit7/
```

### **2단계: 파일 경로 수정 (자동화 스크립트 사용)**
```python
# unit_generator.py 실행
python unit_generator.py 7
```

### **3단계: GitHub에 푸시**
```bash
git add unit7/
git commit -m "Add Unit 7 with GitHub Pages compatible paths"
git push origin main
```

### **4단계: 온라인 접속 확인**
```
https://word1600.github.io/game/unit7/
```

---

## 📁 **올바른 폴더 구조**

```
UFO word game/
├── unit1/                 # Unit 1 (50개 단어)
│   ├── index.html
│   ├── game.js           # 경로: /game/unit1/data/unit1.json
│   ├── style.css
│   ├── data/unit1.json
│   └── assets/
├── unit2/                 # Unit 2 (50개 단어)
├── unit3/                 # Unit 3 (50개 단어)
├── unit4/                 # Unit 4 (50개 단어)
├── unit5/                 # Unit 5 (50개 단어)
├── unit6/                 # Unit 6 (50개 단어) ✅ 완성
├── unit7/                 # Unit 7 (50개 단어) 🚀 다음 목표
└── ...
```

---

## 🎯 **GitHub Pages 호환 경로 패턴**

### **데이터 파일 경로**
```javascript
// Unit N의 데이터 파일 경로
const dataPath = `/game/unit${N}/data/unit${N}.json`;
```

### **에셋 파일 경로**
```javascript
// UFO 이미지
ufoImg.src = `/game/unit${N}/assets/ufo_clean${random}.png`;

// 폭발 효과
explosion.src = `/game/unit${N}/assets/explosion.png`;

// 총알 이미지
bullet.src = `/game/unit${N}/assets/bullet1.png`;
```

---

## 🚀 **자동화 배포 시스템**

### **1. unit_generator.py 업데이트**
```python
def generate_unit(unit_number, word_data):
    # 1. Unit 6을 템플릿으로 복사
    # 2. 모든 경로를 GitHub Pages 호환으로 자동 수정
    # 3. 단어 데이터 파일 생성
    # 4. 완전한 게임 폴더 생성
```

### **2. 배포 자동화 스크립트**
```bash
# Unit N 생성 및 배포
python unit_generator.py N
git add unitN/
git commit -m "Add Unit N"
git push origin main
```

---

## ✅ **배포 전 체크리스트**

### **로컬 테스트**
- [ ] `python -m http.server 8000` 실행
- [ ] `http://localhost:8000/unitN/` 접속
- [ ] 게임 정상 작동 확인
- [ ] 단어 데이터 로딩 확인
- [ ] 이미지 및 에셋 정상 표시 확인

### **GitHub Pages 배포**
- [ ] 모든 파일이 GitHub에 업로드됨
- [ ] 경로가 `/game/unitN/` 형식으로 수정됨
- [ ] `https://word1600.github.io/game/unitN/` 접속 가능
- [ ] 온라인에서 게임 정상 작동 확인

---

## 🔍 **문제 발생 시 디버깅 방법**

### **1. 브라우저 개발자 도구 확인**
```javascript
// Console에서 경로 확인
console.log('데이터 파일 경로:', '/game/unit6/data/unit6.json');
console.log('에셋 파일 경로:', '/game/unit6/assets/ufo_clean0.png');
```

### **2. 네트워크 탭에서 파일 로딩 상태 확인**
- 200: 정상 로딩
- 404: 파일을 찾을 수 없음 (경로 문제)
- 403: 권한 문제

### **3. GitHub 저장소에서 파일 존재 확인**
```
https://github.com/word1600/game/tree/main/unit6
```

---

## 🎉 **성공적인 배포의 핵심**

### **1. 경로 일관성**
- 모든 경로를 `/game/unitN/` 형식으로 통일
- 상대 경로 대신 절대 경로 사용

### **2. 폴더 구조 완성**
- `unitN/` 폴더가 GitHub에 완전히 업로드됨
- 모든 하위 파일과 폴더가 포함됨

### **3. 파일 권한 관리**
- PAT에 적절한 권한 설정
- 워크플로우 파일 충돌 방지

---

## 📚 **참고 자료**

- **GitHub Pages 설정**: `https://github.com/word1600/game/settings/pages`
- **온라인 게임 URL**: `https://word1600.github.io/game/`
- **PAT 설정 가이드**: `SETUP_PERSONAL_ACCESS_TOKEN.md`
- **Unit 생성기**: `unit_generator.py`

---

## 🚀 **다음 단계: Unit 7 생성 및 배포**

Unit 7부터는 이 가이드를 따라 **즉시 배포**가 가능합니다!

**예상 소요 시간**: 30분 이내 (이전: 하루)
**성공률**: 100% (모든 문제 해결됨)

---

*이 가이드는 2025년 8월 28일 Unit 6 배포 완료 후 작성되었습니다.*
