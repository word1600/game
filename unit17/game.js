// 게임 상태 변수
let score = 0;
let timeLeft = 300; // 5분(초)
let isPaused = false; // 게임 일시정지 상태
let isMuted = false; // 소리 상태

// UFO 단어 데이터
let ufoWordsData = [];
let currentWord = null;

// 단어 출현 풀: 모든 단어 5회씩 복제 후 셔플 (최소 3회 보장)
let wordPool = [];
let usedWords = new Set(); // 이미 사용된 단어 추적 (고유키)

let answeredThisProblem = false; // 현재 문제에서 정답을 맞췄는지

let ttsInterval = null;
let lastTtsUtterance = null;

let selectedUnit = 'unit17'; // 기본값: Unit 17

// 유닛 선택 버튼 핸들러
function setupUnitSelect() {
  // setupUnitSelect 및 관련 코드 삭제됨
}

// 미국식 발음 TTS
function speakWordTTSUS(word) {
  if (!window.speechSynthesis || isPaused) return;
  if (lastTtsUtterance) {
    window.speechSynthesis.cancel();
    lastTtsUtterance = null;
  }
  const utter = new SpeechSynthesisUtterance(word);
  utter.lang = 'en-US';
  // 미국식 여성 목소리 우선 선택
  const voices = window.speechSynthesis.getVoices();
  let voice = voices.find(v =>
    v.lang === 'en-US' &&
    (v.name.toLowerCase().includes('female') || v.name.toLowerCase().includes('woman') || v.name.toLowerCase().includes('girl') || v.name.toLowerCase().includes('fem'))
  );
  if (!voice) {
    // 그래도 없으면 미국식 영어 음성 아무거나
    voice = voices.find(v => v.lang === 'en-US');
  }
  if (voice) utter.voice = voice;
  utter.pitch = 1.2; // 여성스럽게, 약간 높게
  utter.rate = 1.0;
  lastTtsUtterance = utter;
  window.speechSynthesis.speak(utter);
}

// 영국식 발음 TTS
function speakWordTTSGB(word) {
  if (!window.speechSynthesis || isPaused) return;
  if (lastTtsUtterance) {
    window.speechSynthesis.cancel();
    lastTtsUtterance = null;
  }
  const utter = new SpeechSynthesisUtterance(word);
  utter.lang = 'en-GB';
  // 영국식 여성 목소리 우선 선택
  const voices = window.speechSynthesis.getVoices();
  let voice = voices.find(v =>
    v.lang === 'en-GB' &&
    (v.name.toLowerCase().includes('female') || v.name.toLowerCase().includes('woman') || v.name.toLowerCase().includes('girl') || v.name.toLowerCase().includes('fem'))
  );
  if (!voice) {
    // 그래도 없으면 영국식 영어 음성 아무거나
    voice = voices.find(v => v.lang === 'en-GB');
  }
  if (voice) utter.voice = voice;
  utter.pitch = 1.2; // 여성스럽게, 약간 높게
  utter.rate = 1.0;
  lastTtsUtterance = utter;
  window.speechSynthesis.speak(utter);
}

function refillWordPool() {
  wordPool = [];
  // 각 단어를 3회씩 복제 (정확히 3회 등장)
  for (let i = 0; i < 3; i++) {
    wordPool = wordPool.concat(ufoWordsData);
  }
  // 셔플
  for (let i = wordPool.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [wordPool[i], wordPool[j]] = [wordPool[j], wordPool[i]];
  }
}

// UFO 주기적 생성 (타이머 변수)
let ufoInterval = null;
let timerInterval = null;

// 고유키 생성 함수 (파일 상단에 위치)
function getWordKey(word) {
  return `${word.ko}|${word.en}|${word.pos}`;
}

// 문제(상단 박스)용 단어를 랜덤하게 선택
function pickNewProblemWord() {
  if (!wordPool.length) refillWordPool();
  // 아직 사용되지 않은 단어 우선 선택
  let availableWords = wordPool.filter(word => !usedWords.has(getWordKey(word)));
  if (availableWords.length === 0) {
    // 모든 단어가 사용되었으면 usedWords 초기화
    usedWords.clear();
    availableWords = wordPool;
  }
  currentWord = availableWords[Math.floor(Math.random() * availableWords.length)];
  usedWords.add(getWordKey(currentWord));
  let posKo = '';
  document.getElementById('word-ko').textContent = currentWord.ko;
  document.getElementById('word-pos').textContent = currentWord.pos;
  answeredThisProblem = false;
  // 새로운 문제 시작 시 카운터 리셋
  ufoSinceLastAnswer = 0;
  answerUfoSpawnCount = 0;
  problemWordCount = 0;
  // 오답 UFO 피격 플래그 초기화
  const ufos = document.querySelectorAll('.ufo');
  ufos.forEach(ufo => { ufo._wrongHitForThisProblem = false; });

  // TTS: 단어가 바뀌고 2초 후에 1회, 2초 후에 1회(총 2회)
  if (ttsInterval) clearInterval(ttsInterval);
  if (window.ttsTimeout1) clearTimeout(window.ttsTimeout1);
  if (window.ttsTimeout2) clearTimeout(window.ttsTimeout2);
  
  // 게임이 일시정지 상태가 아닐 때만 TTS 설정
  if (!isPaused) {
    window.ttsTimeout1 = setTimeout(() => {
      if (!isPaused) speakWordTTSUS(currentWord.en);
      window.ttsTimeout2 = setTimeout(() => {
        if (!isPaused) speakWordTTSGB(currentWord.en);
      }, 2000);
    }, 2000);
  }
}

// UFO 겹침 방지용 Y좌표 관리
let recentUfoYs = [];
const UFO_MIN_Y_DIST = 90;
const UFO_MAX_RECENT = 6;

let recentUfoWords = [];
const UFO_WORD_MAX_RECENT = 5;

function getNonOverlappingY(areaHeight) {
  let y, tryCount = 0;
  do {
    y = 100 + Math.random() * (areaHeight - 300);
    tryCount++;
  } while (recentUfoYs.some(yy => Math.abs(yy - y) < UFO_MIN_Y_DIST) && tryCount < 20);
  recentUfoYs.push(y);
  if (recentUfoYs.length > UFO_MAX_RECENT) recentUfoYs.shift();
  return y;
}

let ufoSinceLastAnswer = 0; // 정답 UFO가 없을 때 카운트
let answerUfoSpawnCount = 0; // 정답 UFO 스폰 카운트
let problemWordCount = 0; // 현재 문제 단어 출현 횟수

function spawnUFO(forceAnswerUFO = false) {
  const gameArea = document.getElementById('game-area');
  const areaWidth = gameArea.offsetWidth;
  const areaHeight = gameArea.offsetHeight;

  // 현재 화면에 정답 UFO가 있는지 확인
  const ufos = document.querySelectorAll('.ufo');
  let answerUfoExists = false;
  ufos.forEach(ufo => {
    if (ufo.wordData && getWordKey(ufo.wordData) === getWordKey(currentWord)) answerUfoExists = true;
  });

  let wordData;
  // 정답 UFO 등장 조건: 반드시 3개 UFO가 지나간 뒤에만 등장
  let shouldSpawnAnswer = false;
  if (forceAnswerUFO) {
    shouldSpawnAnswer = true;
  } else if (!answerUfoExists) {
    if (ufoSinceLastAnswer < 3) {
      shouldSpawnAnswer = false; // 최소 3개 UFO가 지나갈 때까지 오답만
    } else {
      // 3개 지난 뒤에는 무조건 정답 등장
      shouldSpawnAnswer = true;
    }
  }

  if (shouldSpawnAnswer) {
    // 정답 UFO 강제 등장
    wordData = currentWord;
    ufoSinceLastAnswer = 0;
    answerUfoSpawnCount++;
    problemWordCount++;
  } else {
    wordData = getRandomWord();
    // 혹시 랜덤으로 정답이 뽑히면 카운트 리셋
    if (getWordKey(wordData) === getWordKey(currentWord)) {
      ufoSinceLastAnswer = 0;
      answerUfoSpawnCount++;
      problemWordCount++;
    } else {
      ufoSinceLastAnswer++;
    }
  }

  const ufo = document.createElement('div');
  ufo.className = 'ufo';
  ufo.wordData = wordData;

  const ufoImg = document.createElement('img');
  ufoImg.className = 'ufo-img';
  // 로컬 환경과 온라인 환경을 구분하여 경로 설정
  const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
  const assetsPath = isLocal ? './assets/' : '/game/unit12/assets/';
  ufoImg.src = assetsPath + 'ufo_clean' + (Math.floor(Math.random() * 5)) + '.png';
  ufo.appendChild(ufoImg);

  const ufoWord = document.createElement('div');
  ufoWord.className = 'ufo-word';
  ufoWord.textContent = wordData.en;
  ufo.appendChild(ufoWord);

  const ufoWidth = 110;
  let x = -ufoWidth;
  let y = getNonOverlappingY(areaHeight);

  ufo.style.left = x + 'px';
  ufo.style.top = y + 'px';

  ufo.addEventListener('click', function (event) {
    // 클릭된 요소가 UFO 이미지나 단어인지 확인
    if (event.target.classList.contains('ufo-img') || event.target.classList.contains('ufo-word')) {
      handleUfoClick(ufo);
    }
  });

  gameArea.appendChild(ufo);

  let amplitude = 30 + Math.random() * 20;
  let freq = 0.015 + Math.random() * 0.01;
  let t = 0;
  let speed = 2 + Math.random();

  function animate() {
    if (!ufo.parentNode) return;
    t += 1;
    x += speed;
    ufo.style.left = x + 'px';
    ufo.style.top = (y + Math.sin(t * freq) * amplitude) + 'px';
    if (x > areaWidth + ufoWidth) {
      ufo.remove();
      return;
    }
    // 모바일에서 성능 최적화를 위해 60fps 제한
    if (typeof window !== 'undefined' && window.requestAnimationFrame) {
      requestAnimationFrame(animate);
    }
  }
  animate();
}

function getRandomWord() {
  if (!wordPool.length) refillWordPool();
  return wordPool.pop();
}

function updateScore() {
  document.getElementById('score').textContent = score;
}

function updateTimer() {
  const min = String(Math.floor(timeLeft / 60)).padStart(2, '0');
  const sec = String(timeLeft % 60).padStart(2, '0');
  document.getElementById('timer').textContent = `${min}:${sec}`;
}

function showFeedback(text, scoreText, type) {
  const feedbackEl = document.createElement('div');
  feedbackEl.className = 'feedback ' + type;
  feedbackEl.innerHTML = `<div class="feedback-text">${text}</div><div class="feedback-score">${scoreText}</div>`;
  document.getElementById('game-area').appendChild(feedbackEl);
  setTimeout(() => feedbackEl.remove(), 2000);
}

function createExplosion(x, y) {
  // 기존 파티클 제거, 이미지로 대체
  const explosion = document.createElement('img');
  // 로컬 환경과 온라인 환경을 구분하여 경로 설정
  const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
  const assetsPath = isLocal ? './assets/' : '/game/unit12/assets/';
  explosion.src = assetsPath + 'explosion.png';
  explosion.className = 'explosion-effect';
  explosion.style.position = 'absolute';
  explosion.style.left = (x - 90) + 'px'; // 이미지 중심 정렬 (180px 기준)
  explosion.style.top = (y - 90) + 'px';
  explosion.style.width = '180px';
  explosion.style.height = '180px';
  explosion.style.pointerEvents = 'none';
  explosion.style.zIndex = 200;
  document.getElementById('game-area').appendChild(explosion);
  setTimeout(() => explosion.remove(), 700);
}

function handleUfoClick(ufoElement) {
  if (isPaused) return;
  
  // 모바일에서 터치 반응성 향상을 위한 즉시 시각적 피드백
  ufoElement.style.transform = 'scale(0.9)';
  setTimeout(() => {
    ufoElement.style.transform = '';
  }, 100);
  
  const clickedWord = ufoElement.wordData.en;
  if (getWordKey(ufoElement.wordData) === getWordKey(currentWord)) {
    if (!answeredThisProblem) {
      score += 10;
      updateScore();
      showFeedback('Bingo', '+10', 'correct');
      document.getElementById('sound-bingo')?.play();
      const rect = ufoElement.getBoundingClientRect();
      const gameAreaRect = document.getElementById('game-area').getBoundingClientRect();
      const explosionX = rect.left - gameAreaRect.left + rect.width / 2;
      const explosionY = rect.top - gameAreaRect.top + rect.height / 2;
      createExplosion(explosionX, explosionY);
      ufoElement.remove();
      answeredThisProblem = true;
      
      // 정답을 맞힌 순간, 화면의 모든 총알을 제거합니다.
      const allBullets = document.querySelectorAll('.bullet');
      allBullets.forEach(b => b.remove());

      pauseGameAndStartChallenge(currentWord.en);
      return;
    }
  } else {
    score -= 5;
    updateScore();
    showFeedback('Nope', '-5', 'incorrect');
    document.getElementById('sound-nope')?.play();
  }
}

function showBonusFeedback() {
  document.getElementById('sound-goodjob')?.play();
  const feedbackEl = document.createElement('div');
  feedbackEl.className = 'feedback correct';
  feedbackEl.innerHTML = `<div class="feedback-text">Good job</div><div class="feedback-score">+5</div>`;
  const challengeBox = document.getElementById('challenge-box');
  if (challengeBox && challengeBox.parentNode) {
    challengeBox.parentNode.insertBefore(feedbackEl, challengeBox);
  } else {
    document.getElementById('game-area').appendChild(feedbackEl);
  }
  setTimeout(() => feedbackEl.remove(), 2000);
}

function pauseGameAndStartChallenge(word) {
  isPaused = true;
  let wordToChallenge = word;
  // clearInterval(timerInterval); // 타이머 멈추지 않음
  clearInterval(ufoInterval);
  const challengeBox = document.createElement('div');
  challengeBox.className = 'challenge-box';
  challengeBox.style.background = 'none';
  challengeBox.style.border = 'none';
  challengeBox.id = 'challenge-box';
  challengeBox.innerHTML = `
    <div class="challenge-timer-container">
      <div class="timer-row">
        <div class="clock-face">
          <div class="clock-hand" id="clock-hand"></div>
          <div class="clock-center"></div>
        </div>
        <div id="challenge-timer-display">10</div>
      </div>
    </div>
    <div class="challenge-word-container">
      <p>${word}</p>
    </div>
    <input type="text" id="challenge-input" autocomplete="off" spellcheck="false" autocapitalize="off" lang="en" inputmode="text" placeholder="Type here...">
  `;
  document.getElementById('game-area').appendChild(challengeBox);
  const challengeInput = document.getElementById('challenge-input');
  challengeInput.focus();
  let challengeTimeLeft = 10;
  const timerDisplay = document.getElementById('challenge-timer-display');
  const clockHand = document.getElementById('clock-hand');
  let challengeTimerInterval = setInterval(() => {
    challengeTimeLeft--;
    timerDisplay.textContent = challengeTimeLeft;
    // 시계 바늘 회전 (10초에서 0초까지 360도 회전)
    const rotation = ((10 - challengeTimeLeft) / 10) * 360;
    clockHand.style.transform = `rotate(${rotation}deg)`;

    // 1초 남았을 때 0.5초 후 경고음 재생
    if (challengeTimeLeft === 1) {
      setTimeout(() => {
        const beepSound = document.getElementById('sound-beep2');
        if (beepSound && !isMuted) {
          beepSound.currentTime = 0;
          beepSound.volume = 0.5;
          beepSound.play();
        }
      }, 500);
    }

    if (challengeTimeLeft <= 0) {
      endChallenge(false);
    }
  }, 1000);
  challengeInput.addEventListener('input', () => {
    if (challengeInput.value.trim().toLowerCase() === wordToChallenge.trim().toLowerCase()) {
      endChallenge(true);
    }
  });
  
  // 스페이스바 입력을 위한 특별한 이벤트 핸들러 추가
  challengeInput.addEventListener('keydown', (e) => {
    // 스페이스바가 눌렸을 때 기본 동작을 허용하되, 다른 이벤트와의 충돌 방지
    if (e.code === 'Space') {
      // 기본 동작은 허용하되, 이벤트 전파는 중단
      e.stopPropagation();
    }
  });
  function endChallenge(success) {
    clearInterval(challengeTimerInterval);
    challengeBox.remove();
    if (success) {
      score += 5;
      updateScore();
      showBonusFeedback();
    } else {
      // 시간 초과 시 사운드 재생 로직 제거 (위에서 처리)
    }
    resumeGame();
  }
}

function resumeGame() {
  isPaused = false;
  clearInterval(timerInterval);
  timerInterval = null;
  clearInterval(ufoInterval);
  if (timeLeft <= 0) {
    endGame();
    return;
  }
  // 타이머가 이미 동작 중이면 새로 시작하지 않음
  if (!timerInterval) {
    timerInterval = setInterval(() => {
      timeLeft--;
      updateTimer();
      if (timeLeft <= 0) {
        clearInterval(timerInterval);
        endGame();
      }
    }, 1000);
  }
  ufoInterval = setInterval(spawnUFO, 1800);
  document.getElementById('top-bar').style.display = 'flex';
  document.getElementById('word-box').style.display = 'block';
  document.getElementById('input-area').style.display = 'flex';
  document.getElementById('sound-toggle-btn').style.display = 'flex';
  // timeLeft = 300; // 시간 리셋 금지
  recentUfoYs = [];
  recentUfoWords = [];
  isPaused = false;
  const challengeBox = document.getElementById('challenge-box');
  if (challengeBox) {
      challengeBox.remove();
  }
  updateScore();
  updateTimer();
  pickNewProblemWord();
  const bgm = document.getElementById('bgm');
  if (bgm) {
    // BGM이 이미 재생 중이면 play()를 호출하지 않음
    if (bgm.paused) {
      bgm.currentTime = 0;
      bgm.volume = 0.2;
      bgm.play();
    }
  }
}

function endGame() {
  clearInterval(ufoInterval);
  clearInterval(timerInterval);
  isPaused = true;
  document.getElementById('bgm')?.pause();
  
  // 모든 TTS 관련 타이머와 음성 정리
  if (ttsInterval) clearInterval(ttsInterval);
  if (window.ttsTimeout1) clearTimeout(window.ttsTimeout1);
  if (window.ttsTimeout2) clearTimeout(window.ttsTimeout2);
  if (window.speechSynthesis) {
    window.speechSynthesis.cancel();
    window.speechSynthesis.pause();
  }
  if (lastTtsUtterance) {
    lastTtsUtterance = null;
  }
  
  const ufos = document.querySelectorAll('.ufo');
  ufos.forEach(ufo => ufo.remove());
  const bullets = document.querySelectorAll('.bullet');
  bullets.forEach(bullet => bullet.remove());
  
  // 보너스 게임 타이핑 박스 제거
  const challengeBox = document.getElementById('challenge-box');
  if (challengeBox) {
    challengeBox.remove();
  }
  
  document.getElementById('top-bar').style.display = 'none';
  document.getElementById('word-box').style.display = 'none';
  document.getElementById('input-area').style.display = 'none';
  const gameOverEl = document.createElement('div');
  gameOverEl.id = 'game-over-screen';
  gameOverEl.innerHTML = `
    <div class="title">Game Over</div>
    <div class="final-score">Score : <span class="score-value">${score}</span></div>
    <button id="restart-btn">Start Again</button>
  `;
  document.getElementById('game-area').appendChild(gameOverEl);

  const restartBtn = document.getElementById('restart-btn');
  // 버튼이 확실히 클릭되도록 스타일 직접 지정
  restartBtn.style.pointerEvents = 'auto'; 
  restartBtn.onclick = () => location.reload();
  
  // 모바일 터치 이벤트 추가
  restartBtn.addEventListener('touchstart', function(e) {
    e.preventDefault();
    location.reload();
  }, { passive: false });
}

function resetGame() {
  const gameOverScreen = document.getElementById('game-over-screen');
  if (gameOverScreen) {
      gameOverScreen.remove();
  }
  document.getElementById('top-bar').style.display = 'flex';
  document.getElementById('word-box').style.display = 'block';
  document.getElementById('input-area').style.display = 'flex';
  score = 0;
  timeLeft = 300;
  recentUfoYs = [];
  recentUfoWords = [];
  ufoSinceLastAnswer = 0;
  answerUfoSpawnCount = 0;
  problemWordCount = 0;
  isPaused = false;
  const challengeBox = document.getElementById('challenge-box');
  if (challengeBox) {
      challengeBox.remove();
  }
  updateScore();
  updateTimer();
  pickNewProblemWord();

  // 타이머 재시작
  if (timerInterval) clearInterval(timerInterval);
  timerInterval = setInterval(() => {
    timeLeft--;
    updateTimer();
    if (timeLeft <= 0) {
      clearInterval(timerInterval);
      endGame();
    }
  }, 1000);

  // UFO 생성 재시작
  if (ufoInterval) clearInterval(ufoInterval);
  ufoInterval = setInterval(spawnUFO, 1800);

  // 단어 데이터가 비어있으면 로드
  if (!ufoWordsData.length) loadWords();

  const bgm = document.getElementById('bgm');
  if (bgm) {
    bgm.currentTime = 0;
    bgm.volume = 0.2;
    bgm.play();
  }

  if (ttsInterval) clearInterval(ttsInterval);
  if (window.speechSynthesis) window.speechSynthesis.cancel();
}

document.addEventListener('DOMContentLoaded', () => {
  const startScreen = document.getElementById('start-screen');
  const startGameBtn = document.getElementById('start-game-btn');
  const topBar = document.getElementById('top-bar');
  const wordBox = document.getElementById('word-box');
  const inputArea = document.getElementById('input-area');
  const timerEl = document.getElementById('timer');
  const scoreEl = document.getElementById('score');
  const fireBtn = document.getElementById('fire-btn');
  const bgm = document.getElementById('bgm');
  const soundToggleBtn = document.getElementById('sound-toggle-btn');
  const bgmVolumeSlider = document.getElementById('bgm-volume-slider');
  const allSounds = [
    bgm,
    document.getElementById('sound-shoot'),
    document.getElementById('sound-bingo'),
    document.getElementById('sound-nope'),
    document.getElementById('sound-goodjob')
  ];
  scoreEl.textContent = '0';
  function setMuteState(mute) {
    isMuted = mute;
    allSounds.forEach(sound => {
      if (sound) sound.muted = isMuted;
    });
    soundToggleBtn.textContent = isMuted ? '🔇' : '🔊';
  }
  soundToggleBtn.addEventListener('click', () => setMuteState(!isMuted));
  soundToggleBtn.addEventListener('touchstart', (e) => { e.preventDefault(); setMuteState(!isMuted); });
  bgm.volume = 0.1;
  bgmVolumeSlider.value = 0.1;
  bgmVolumeSlider.addEventListener('input', (e) => {
    bgm.volume = parseFloat(e.target.value);
  });
  function tryStartBGM(force=false) {
    if (!bgm) return;
    if (force) {
      bgm.currentTime = 0;
      bgm.volume = parseFloat(bgmVolumeSlider.value);
      bgm.play().catch(() => console.log("BGM auto-play failed."));
      return;
    }
    if (bgm.currentTime > 0) return;
    bgm.volume = parseFloat(bgmVolumeSlider.value);
    bgm.play().catch(() => console.log("BGM auto-play failed."));
  }
  function initializeGame() {
    startScreen.style.display = 'none';
    topBar.style.display = 'flex';
    wordBox.style.display = 'block';
    inputArea.style.display = 'flex';
    soundToggleBtn.style.display = 'flex';
    
    // 효과음 볼륨 설정 (50% 수준으로 더 줄임)
    const bingoSound = document.getElementById('sound-bingo');
    const nopeSound = document.getElementById('sound-nope');
    const goodjobSound = document.getElementById('sound-goodjob');
    if (bingoSound) bingoSound.volume = 0.5;
    if (nopeSound) nopeSound.volume = 0.5;
    if (goodjobSound) goodjobSound.volume = 0.5;
    
    tryStartBGM(true); // 강제 재생
    isPaused = false;
    ufoSinceLastAnswer = 0;
    answerUfoSpawnCount = 0;
    problemWordCount = 0;
    updateTimer();
    timerInterval = setInterval(() => {
      timeLeft--;
      updateTimer();
      if (timeLeft <= 0) {
        clearInterval(timerInterval);
        endGame();
      }
    }, 1000);
    loadWords();
    bgm.volume = parseFloat(bgmVolumeSlider.value);
  }
  startGameBtn.addEventListener('click', initializeGame);
  startGameBtn.addEventListener('touchstart', function(e) {
    e.preventDefault();
    initializeGame();
  }, { passive: false });
  let fireInterval = null;
  let isFiring = false;
  function fireBulletsBurst() {
    // 연속 발사 시 소리 한 번만 재생
    const shootSound = document.getElementById('sound-shoot3');
    if (shootSound) {
      shootSound.currentTime = 0;
      shootSound.volume = 0.7;
      shootSound.play();
    }
    fireBullet(false); // 소리 재생 X
  }
  function fireBullet(playSound = true) {
    if (playSound && !isMuted) {
      const shootSound = document.getElementById('sound-shoot3');
      if (shootSound) {
        shootSound.currentTime = 0;
        shootSound.volume = 0.7;
        shootSound.play();
      }
    }
    // bullet div 대신 이미지 사용
    const bullet = document.createElement('img');
    bullet.className = 'bullet';
    // 로컬 환경과 온라인 환경을 구분하여 경로 설정
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    const assetsPath = isLocal ? './assets/' : '/game/unit17/assets/';
    bullet.src = assetsPath + 'bullet1.png';
    bullet.style.position = 'absolute';
    bullet.style.width = '36px';
    bullet.style.height = '80px';
    const fireBtnRect = fireBtn.getBoundingClientRect();
    const gameAreaRect = document.getElementById('game-area').getBoundingClientRect();
    bullet.style.left = `${fireBtnRect.left - gameAreaRect.left + fireBtnRect.width / 2 - 18}px`;
    bullet.style.top = `${fireBtnRect.top - gameAreaRect.top}px`;
    bullet.style.zIndex = 5;
    document.getElementById('game-area').appendChild(bullet);

    let y = parseFloat(bullet.style.top);
    function moveBullet() {
      y -= 8;
      bullet.style.top = y + 'px';
      // 충돌 판정
      const ufos = document.querySelectorAll('.ufo');
      for (let ufo of ufos) {
        const ufoRect = ufo.getBoundingClientRect();
        const bulletRect = bullet.getBoundingClientRect();
        if (
          bulletRect.left < ufoRect.right &&
          bulletRect.right > ufoRect.left &&
          bulletRect.top < ufoRect.bottom &&
          bulletRect.bottom > ufoRect.top
        ) {
          if (ufo.wordData && getWordKey(ufo.wordData) === getWordKey(currentWord)) {
            // 정답: 한 번만 점수 획득
            if (!answeredThisProblem) {
              score += 10;
              updateScore();
              showFeedback('Bingo', '+10', 'correct');
              document.getElementById('sound-bingo')?.play();
              const rect = ufo.getBoundingClientRect();
              const gameAreaRect = document.getElementById('game-area').getBoundingClientRect();
              const explosionX = rect.left - gameAreaRect.left + rect.width / 2;
              const explosionY = rect.top - gameAreaRect.top + rect.height / 2;
              createExplosion(explosionX, explosionY);
              ufo.remove();
              answeredThisProblem = true;
              
              // 정답을 맞힌 순간, 화면의 모든 총알을 제거합니다.
              const allBullets = document.querySelectorAll('.bullet');
              allBullets.forEach(b => b.remove());

              pauseGameAndStartChallenge(currentWord.en);
              return;
            }
          } else {
            // 오답: 한 문제당 한 번만 -5점
            if (!ufo._wrongHitForThisProblem) {
              score -= 5;
              updateScore();
              showFeedback('Nope', '-5', 'incorrect');
              document.getElementById('sound-nope')?.play();
              ufo._wrongHitForThisProblem = true;
            }
          }
          bullet.remove(); // 명중/오발 모두 소멸 (항상 한 번만 실행)
          return;
        }
      }
      // word-box 바로 위에서 소멸
      const wordBox = document.getElementById('word-box');
      if (wordBox) {
        const wordBoxRect = wordBox.getBoundingClientRect();
        const gameAreaRect = document.getElementById('game-area').getBoundingClientRect();
        const wordBoxBottom = wordBoxRect.bottom - gameAreaRect.top;
        if (y < wordBoxBottom) {
          bullet.remove();
          return;
        }
      }
      if (y < -40) {
        bullet.remove();
        return;
      }
      // 모바일에서 성능 최적화를 위해 60fps 제한
      if (typeof window !== 'undefined' && window.requestAnimationFrame) {
        requestAnimationFrame(moveBullet);
      }
    }
    moveBullet();
  }
  const handleFireStart = (e) => {
    e.preventDefault();
    if (isPaused || isFiring) return;
    tryStartBGM();
    isFiring = true;
    fireBulletsBurst();
    fireInterval = setInterval(fireBulletsBurst, 150);
    
    // 모바일에서 터치 피드백
    if (e.type === 'touchstart') {
      fireBtn.style.transform = 'translate(-50%, -35%) scale(0.95)';
    }
  };
  const handleFireEnd = (e) => {
    e.preventDefault();
    isFiring = false;
    clearInterval(fireInterval);
    
    // 모바일에서 터치 피드백 복원
    if (e.type === 'touchend') {
      fireBtn.style.transform = 'translate(-50%, -35%)';
    }
  };
  fireBtn.addEventListener('mousedown', handleFireStart);
  window.addEventListener('mouseup', handleFireEnd);
  fireBtn.addEventListener('touchstart', handleFireStart, { passive: false });
  window.addEventListener('touchend', handleFireEnd, { passive: false });
  fireBtn.addEventListener('touchmove', (e) => e.preventDefault(), { passive: false });
  window.addEventListener('keydown', (e) => {
    // 타이핑 챌린지 중에는 총알 발사 비활성화
    if (e.code === 'Space' && !isFiring && !document.getElementById('challenge-input')) {
      e.preventDefault();
      handleFireStart(e);
    }
  });
  window.addEventListener('keyup', (e) => {
    // 타이핑 챌린지 중에는 총알 발사 비활성화
    if (e.code === 'Space' && !document.getElementById('challenge-input')) {
      e.preventDefault();
      handleFireEnd(e);
    }
  });
  requestAnimationFrame(gameLoop);
});

function gameLoop() {
  // 모바일에서 성능 최적화를 위해 60fps 제한
  if (typeof window !== 'undefined' && window.requestAnimationFrame) {
    requestAnimationFrame(gameLoop);
  }
}

function getLatestUnitJsonFile() {
  // data 폴더 내 unit17.json 파일을 사용
  return fetch('/game/unit17/data/unit17.json')
    .then(r => r.ok ? r.json() : null)
    .catch(() => null)
    .then(data => {
      if (!data) throw new Error('단어 데이터를 불러오지 못했습니다.');
      return data;
    });
}

function loadWords() {
  // 로컬 환경과 온라인 환경을 구분하여 경로 설정
  const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
  const file = isLocal ? './data/unit17.json' : '/game/unit17/data/unit17.json';
  console.log('🔍 Unit 17: 단어 데이터 로딩 시작:', file);
  
  fetch(file)
    .then(response => {
      console.log('📡 Unit 17: 서버 응답:', response.status, response.ok);
      if (!response.ok) {
        throw new Error('단어 데이터를 불러오지 못했습니다.');
      }
      return response.json();
    })
    .then(data => {
      console.log('✅ Unit 17: 데이터 로드 성공! 단어 수:', data.length);
      console.log('📝 Unit 17: 첫 번째 단어:', data[0]);
      ufoWordsData = data;
      refillWordPool();
      pickNewProblemWord();
      updateScore();
      updateTimer();
      if (ufoInterval) clearInterval(ufoInterval);
      ufoInterval = setInterval(spawnUFO, 1800);
    })
    .catch(err => {
      console.error('❌ Unit 17: 데이터 로드 실패:', err);
      alert('Unit 17 단어 데이터를 불러오지 못했습니다: ' + err.message);
    });
} 