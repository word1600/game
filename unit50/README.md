# Unit 50 - TOEIC WORD 1600 UFO 게임

## 게임 정보
- **Unit 번호**: 50 (최종 Unit)
- **총 단어 수**: 50개
- **데이터**: `data/unit50.json` (로컬 후보: `unit50/data/unit50.json`, `../data/unit50.json`)

## 게임 특징
- **게임 시간**: 5분 타이머
- **점수**: 정답 +10 / 오답 -5, 보너스 타이핑 +5
- **TTS**: 미국식 발음
- **데이터 경로**: `data/unit50.json` → 실패 시 `../data/unit50.json`

## 단어 주제 요약
- **규격·군사**: specification, requirement, ambiguity, aircraft, acceptance, combat helmet, meet, strict, military, contractor, thoroughly
- **구조·잠수함**: structure, framework, disorder, submarine, extremely, strong, internal, withstand, enormous, pressure
- **지자체·자문**: county, reorganized, consultant, enrich, improve, deplete
- **훈련·농업**: simulated, training exercise, experience, irrigation, farmland, major, railroad, transport
- **창조·의료**: knowledge, invent, create, imitate, treatment, advanced, rescue, method, farming
- **금융**: delinquent, overdue, timely, loan account, debt, session

## 접속
- 로컬: `http://localhost:8000/unit50/`
- 온라인: https://word1600.github.io/game/unit50/

## 업데이트
- **v1.0**: Unit 49 템플릿 기반 Unit 50 게임 추가 (`unit50/`, `data/unit50.json`).

## JSON 수정 시
- 실행 점검 후 데이터 오류 발견 시 `data/unit50.json` 교체 → `unit50/data/unit50.json` 동기화 → 푸시만으로 반영 가능 (`game.js` 변경 불필요).
