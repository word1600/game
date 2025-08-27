# UFO Word Game Netlify 배포 가이드

## 🚀 Netlify 배포 방법

### **1단계: Netlify 계정 생성**
1. https://netlify.com 접속
2. "Sign up" 클릭
3. GitHub 계정으로 로그인

### **2단계: 프로젝트 배포**
1. Netlify 대시보드에서 "New site from Git" 클릭
2. GitHub 선택
3. 저장소 선택: `ufo-word-game`
4. Build settings:
   - Build command: 비워두기 (정적 사이트)
   - Publish directory: `.` (루트 디렉토리)
5. "Deploy site" 클릭

### **3단계: 도메인 설정**
1. 자동 생성된 도메인 확인 (예: `amazing-ufo-game.netlify.app`)
2. "Site settings" → "Domain management"에서 커스텀 도메인 설정 가능

## 📱 **접속 URL 체계**
```
메인 게임: https://[도메인].netlify.app/
Unit 1:   https://[도메인].netlify.app/          (50개 단어)
Unit 2:   https://[도메인].netlify.app/unit2/    (50개 단어)
Unit 3:   https://[도메인].netlify.app/unit3/    (50개 단어)
Unit 4:   https://[도메인].netlify.app/unit4/    (50개 단어)
Unit 5:   https://[도메인].netlify.app/unit5/    (50개 단어)
Unit 6:   https://[도메인].netlify.app/unit6/    (50개 단어)
```

## 🎯 **Netlify 장점**
- ✅ 완전 무료 (월 100GB 대역폭)
- ✅ 자동 HTTPS
- ✅ 글로벌 CDN
- ✅ 자동 배포 (git push 시)
- ✅ 폼 처리, 서버리스 함수 등 고급 기능
- ✅ 커스텀 도메인 지원

## 🔄 **자동 배포 설정**
1. GitHub 저장소와 연결
2. `git push`할 때마다 자동으로 사이트 업데이트
3. 배포 상태 모니터링 가능

