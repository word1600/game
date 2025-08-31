# UFO Word Game - Unit 7

영어 단어 학습을 위한 UFO 슈팅 게임입니다.

## 🎮 게임 특징

- **스페이스바 지원**: "play hooky", "behind schedule" 등 복합 단어 입력 가능
- **TTS 발음**: 미국식/영국식 발음 제공
- **반응형 디자인**: 모바일/데스크톱 모두 지원
- **사운드 효과**: BGM 및 효과음 포함

## 🚀 배포된 게임

GitHub Pages를 통해 배포되었습니다:
- **URL**: `https://[username].github.io/[repository-name]`

## 📁 파일 구조

```
├── index.html          # 메인 HTML 파일
├── game.js             # 게임 로직
├── style.css           # 스타일시트
├── data/
│   └── unit7.json      # 단어 데이터 (하이픈 제거됨)
├── assets/
│   ├── *.png           # 게임 이미지
│   ├── *.mp3           # 사운드 파일
│   └── fonts/          # 폰트 파일
└── unit7/              # Unit 7 전용 파일들
```

## 🔧 최근 업데이트

- ✅ 하이픈 제거: "play-hooky" → "play hooky"
- ✅ 스페이스바 입력 지원
- ✅ 입력 필드 최적화 (`inputmode="text"`)
- ✅ 이벤트 핸들러 개선

## 🎯 게임 방법

1. **시작**: "Start Game" 버튼 클릭
2. **UFO 클릭**: 정답 단어가 적힌 UFO 클릭
3. **타이핑**: 10초 내에 단어 정확히 타이핑
4. **점수**: 정답 시 +10점, 타이핑 성공 시 +5점

## 📝 단어 예시

- "play hooky" (땡땡이 치다)
- "behind schedule" (일정에 뒤처진)
- "help yourself" (마음껏 드세요)
- "is known for" (~로 잘 알려져 있다)

## 🛠️ 기술 스택

- HTML5
- CSS3
- JavaScript (ES6+)
- Web Speech API (TTS)
- GitHub Pages (배포)

## �� 라이선스

MIT License
