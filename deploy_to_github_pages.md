# UFO Word Game GitHub Pages 배포 가이드

## 🚀 GitHub Pages 배포 방법

### **1단계: GitHub 저장소 생성**
1. GitHub에 로그인
2. "New repository" 클릭
3. 저장소 이름: `ufo-word-game`
4. Public으로 설정
5. README 파일 생성 체크
6. "Create repository" 클릭

### **2단계: 로컬 프로젝트를 GitHub에 업로드**
```bash
# 현재 프로젝트 폴더에서
git init
git add .
git commit -m "Initial commit: UFO Word Game with 6 units"
git branch -M main
git remote add origin https://github.com/[사용자명]/ufo-word-game.git
git push -u origin main
```

### **3단계: GitHub Pages 활성화**
1. 저장소 페이지에서 "Settings" 탭 클릭
2. 왼쪽 메뉴에서 "Pages" 클릭
3. Source를 "Deploy from a branch"로 설정
4. Branch를 "main"으로 선택
5. "Save" 클릭

### **4단계: 배포 완료**
- 몇 분 후 `https://[사용자명].github.io/ufo-word-game/`에서 접근 가능
- 모든 Unit 게임이 온라인에서 실행됨

## 📱 **접속 URL 체계**
```
메인 게임: https://[사용자명].github.io/ufo-word-game/
Unit 1:   https://[사용자명].github.io/ufo-word-game/          (50개 단어)
Unit 2:   https://[사용자명].github.io/ufo-word-game/unit2/    (50개 단어)
Unit 3:   https://[사용자명].github.io/ufo-word-game/unit3/    (50개 단어)
Unit 4:   https://[사용자명].github.io/ufo-word-game/unit4/    (50개 단어)
Unit 5:   https://[사용자명].github.io/ufo-word-game/unit5/    (50개 단어)
Unit 6:   https://[사용자명].github.io/ufo-word-game/unit6/    (50개 단어)
```

## ⚠️ **주의사항**
- GitHub Pages는 정적 파일만 지원
- 현재 프로젝트는 완벽하게 호환됨
- 모든 assets, CSS, JavaScript가 정상 작동

## 🎯 **장점**
- ✅ 완전 무료
- ✅ 자동 HTTPS 지원
- ✅ 전 세계 어디서나 접근 가능
- ✅ 모바일/데스크톱 모두 지원
- ✅ 자동 배포 (git push 시)
