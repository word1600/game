# Unit 12 - TOEIC WORD 1600 UFO 게임

## 📅 **생성 정보**
- **생성일**: 2025년 9월 5일
- **생성 방법**: Unit 11 템플릿 기반
- **총 단어 수**: 45개

## 🎯 **게임 특징**
- **게임 시간**: 5분 타이머
- **점수 시스템**: 정답 +10점 / 오답 -5점
- **보너스 게임**: 타이핑 게임 (+5점)
- **TTS 지원**: 미국식/영국식 발음
- **UFO 격추 게임**: 단어 맞추기

## 📚 **단어 카테고리**

### 1. **자격 및 인증**
- certification (자격증, 증명서, 인증)
- authorization (인가, 허가, 승인)
- disqualification (실격, 자격 박탈)
- earned (취득했다, 얻었다)
- qualified (자격이 있는, 적격한)
- eligible (자격이 있는, 적격한)
- requirement (요구사항, 필요조건)
- criteria (기준, 판단 기준)

### 2. **대기 및 줄서기**
- wait in line (줄을 서서 기다리다)
- queue (줄 서다, 줄)
- cut in line (새치기 하다)
- line up (줄을 서다)
- stand in line (줄을 서서 기다리다)
- waiting list (대기 명단)
- reservation (예약, 예매)
- booking (예약, 예매)

### 3. **입장 및 접근**
- entering (들어가기)
- as soon as (하자마자, 곧)
- mad rush (광란의 돌진, 쇄도)
- crowd (군중, 사람들)
- entrance (입구, 진입)
- exit (출구, 퇴장)
- access (접근, 이용)
- admission (입장, 허용)

### 4. **시간 및 순서**
- first come, first served (선착순)
- priority (우선순위, 우선권)
- sequence (순서, 연속)
- order (순서, 명령)
- turn (차례, 순서)
- appointment (약속, 예약)
- schedule (일정, 스케줄)
- deadline (마감일, 기한)

### 5. **상황 및 상태**
- situation (상황, 형편)
- condition (조건, 상태)
- circumstance (상황, 환경)
- status (상태, 지위)
- position (위치, 지위)
- level (수준, 단계)
- stage (단계, 무대)
- phase (단계, 국면)

### 6. **행동 및 활동**
- activity (활동, 행동)
- action (행동, 조치)
- behavior (행동, 태도)
- conduct (행동, 지휘)
- performance (성과, 공연)
- operation (운영, 수술)
- procedure (절차, 과정)
- process (과정, 처리)

### 7. **결과 및 성과**
- result (결과, 성과)
- outcome (결과, 성과)
- achievement (성취, 업적)
- success (성공, 성과)
- failure (실패, 실패작)
- progress (진전, 발전)
- improvement (개선, 향상)
- development (발전, 개발)

## 🚀 **접속 방법**

### **온라인 접속**
- **URL**: `https://word1600.github.io/game/unit12/`
- **지원 브라우저**: Chrome, Firefox, Safari, Edge
- **모바일 지원**: 반응형 디자인

### **로컬 테스트**
```bash
# 로컬 서버 실행
python -m http.server 8000

# 브라우저에서 접속
http://localhost:8000/unit12/
```

## 🎮 **게임 방법**

1. **게임 시작**: "Game Start" 버튼 클릭
2. **단어 확인**: 화면 상단의 한글 단어와 품사 확인
3. **UFO 격추**: 날아오는 UFO 중 정답을 FIRE 버튼으로 격추
4. **점수 획득**: 정답 시 +10점, 오답 시 -5점
5. **보너스 게임**: 정답 후 타이핑 게임으로 +5점 추가 획득
6. **TTS 활용**: 스페이스바로 발음 듣기

## 🔧 **기술 정보**

### **파일 구조**
```
unit12/
├── index.html          # 메인 HTML 파일
├── game.js            # 게임 로직 및 엔진
├── style.css          # 스타일시트
├── README.md          # 이 문서
├── assets/            # 게임 에셋 (이미지, 사운드, 폰트)
│   ├── *.png          # UFO, 미사일, 배경 이미지
│   ├── *.mp3          # 배경음악 및 효과음
│   └── fonts/         # 한글 폰트
└── data/
    └── unit12.json    # 단어 데이터 (45개)
```

### **주요 기능**
- **반응형 디자인**: 모바일/데스크톱 최적화
- **TTS 통합**: 브라우저 내장 음성 합성
- **사운드 시스템**: 배경음악 및 효과음
- **캐시 관리**: 자동 캐시 무효화
- **에러 처리**: 네트워크 오류 대응

## 📊 **성능 최적화**

- **이미지 최적화**: WebP 형식 지원
- **사운드 압축**: MP3 최적화
- **코드 압축**: CSS/JS 최소화
- **캐싱 전략**: 적절한 캐시 헤더 설정

## 🐛 **문제 해결**

### **일반적인 문제**
1. **단어 로딩 실패**: 네트워크 연결 확인
2. **사운드 재생 안됨**: 브라우저 사운드 권한 확인
3. **TTS 작동 안함**: 브라우저 음성 합성 지원 확인
4. **모바일 터치 문제**: 브라우저 터치 이벤트 지원 확인

### **개발자 도구 활용**
- **F12**: 브라우저 개발자 도구 열기
- **Console**: 오류 메시지 확인
- **Network**: 리소스 로딩 상태 확인
- **Application**: 캐시 및 저장소 확인

## 📝 **업데이트 내역**

### **v1.0 (2025-09-05)**
- Unit 12 초기 생성
- 45개 단어 데이터 포함
- Unit 11 템플릿 기반 최적화
- 모든 기능 정상 작동 확인

## 🎯 **다음 계획**

- **Unit 13**: 다음 단어 세트 준비
- **기능 개선**: 사용자 피드백 반영
- **성능 최적화**: 로딩 속도 개선
- **새로운 기능**: 추가 게임 모드 검토

---

**개발자**: AI Assistant  
**프로젝트**: TOEIC WORD 1600 UFO Game  
**라이선스**: 교육용 무료 사용