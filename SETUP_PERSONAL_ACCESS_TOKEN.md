# Personal Access Token 설정 가이드

## 🔑 Personal Access Token이 필요한 이유
- GitHub에서 2021년 8월부터 패스워드 인증 중단
- Git push 시 인증을 위해 Personal Access Token 필요
- 보안 강화를 위한 GitHub 정책

## 📋 토큰 생성 방법

### 1. GitHub 설정에서 토큰 생성
1. GitHub.com → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)" 클릭
3. Note: "UFO Word Game Deploy" 입력
4. Expiration: "No expiration" 또는 적절한 기간 선택
5. Scopes: 다음 항목 체크
   - ✅ repo (전체 저장소 접근)
   - ✅ workflow (GitHub Actions 사용 시)

### 2. 토큰 복사 및 저장
- 생성된 토큰을 안전한 곳에 복사
- **중요**: 토큰은 한 번만 표시되므로 잃어버리면 재생성 필요

## ⚙️ Git 설정에 토큰 적용

### 방법 1: Git Config 파일 직접 수정
`unit6-github/.git/config` 파일에서:
```ini
[remote "origin"]
	url = https://word1600:YOUR_ACTUAL_TOKEN@github.com/word1600/game.git
```

### 방법 2: Git 명령어로 설정
```bash
cd unit6-github
git remote set-url origin https://word1600:YOUR_ACTUAL_TOKEN@github.com/word1600/game.git
```

## 🔒 보안 주의사항
- 토큰을 코드에 직접 하드코딩하지 마세요
- 토큰을 공개 저장소에 커밋하지 마세요
- 토큰이 노출되면 즉시 재생성하세요

## ✅ 설정 완료 후 테스트
```bash
cd unit6-github
git remote -v
git push origin main
```

## 🚨 문제 해결
- 인증 실패 시: 토큰이 올바른지 확인
- 권한 오류 시: 토큰에 적절한 권한이 있는지 확인
- 403 오류 시: 저장소 접근 권한 확인

