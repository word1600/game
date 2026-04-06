# -*- coding: utf-8 -*-
"""One-off: add normalizePosForDisplay to unit*/game.js (UTF-8, no BOM)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NEEDLE = """function getWordKey(word) {
  return `${word.ko}|${word.en}|${word.pos}`;
}

// 문제(상단 박스)용 단어를 랜덤하게 선택"""

BLOCK = """
// 짧은 품사 표기 → 화면 표시용 한글 병기 (JSON은 n./v. 등 그대로 둬도 됨)
function normalizePosForDisplay(pos) {
  if (pos == null || String(pos).trim() === '') return '';
  const POS_MAP = {
    'phr.v.': 'phr.v.(구동사)',
    'n.': 'n.(명사)',
    'v.': 'v.(동사)',
    'adj.': 'adj.(형용사)',
    'adv.': 'adv.(부사)',
    'prep.': 'prep.(전치사)',
    'conj.': 'conj.(접속사)',
    'pron.': 'pron.(대명사)',
    'interj.': 'interj.(감탄사)',
    'num.': 'num.(수사)',
    'det.': 'det.(한정사)',
  };
  return String(pos)
    .trim()
    .split(',')
    .map((part) => {
      const raw = part.trim();
      if (!raw) return '';
      if (/\\([가-힣·]/.test(raw)) return raw;
      const key = raw.toLowerCase();
      return POS_MAP[key] || raw;
    })
    .filter(Boolean)
    .join(', ');
}
"""

REPLACEMENT = """function getWordKey(word) {
  return `${word.ko}|${word.en}|${word.pos}`;
}
""" + BLOCK + """
// 문제(상단 박스)용 단어를 랜덤하게 선택"""

OLD_LINE = "document.getElementById('word-pos').textContent = currentWord.pos;"
NEW_LINE = "document.getElementById('word-pos').textContent = normalizePosForDisplay(currentWord.pos);"


def main():
    for p in sorted(ROOT.glob("unit*/game.js")):
        text = p.read_text(encoding="utf-8")
        if "normalizePosForDisplay" not in text:
            if NEEDLE not in text:
                print("SKIP (no needle):", p)
                continue
            text = text.replace(NEEDLE, REPLACEMENT, 1)
        if OLD_LINE not in text:
            print("SKIP (no word-pos line):", p)
            continue
        text = text.replace(OLD_LINE, NEW_LINE, 1)
        p.write_text(text, encoding="utf-8", newline="\n")
        print("OK", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
