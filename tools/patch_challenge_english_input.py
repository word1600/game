# -*- coding: utf-8 -*-
"""Bonus challenge input: prefer English (latin) keyboard hints + strip Hangul."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

INPUT_RE = re.compile(
    r'<input type="text" id="challenge-input"[^>]*>',
    re.MULTILINE,
)

INPUT_REPLACE = (
    '<input type="text" id="challenge-input" '
    'autocomplete="off" spellcheck="false" autocapitalize="off" autocorrect="off" '
    'lang="en-US" inputmode="latin" translate="no" dir="ltr" '
    'placeholder="Type in English...">'
)

OLD_FOCUS = """  const challengeInput = document.getElementById('challenge-input');
  challengeInput.focus();"""

NEW_FOCUS = """  const challengeInput = document.getElementById('challenge-input');
  challengeInput.setAttribute('lang', 'en-US');
  challengeInput.setAttribute('inputmode', 'latin');
  challengeInput.setAttribute('translate', 'no');
  challengeInput.setAttribute('dir', 'ltr');
  challengeInput.setAttribute('autocorrect', 'off');
  challengeInput.focus();"""

OLD_HANDLER = """  challengeInput.addEventListener('input', () => {
    if (challengeInput.value.trim().toLowerCase() === wordToChallenge.trim().toLowerCase()) {
      endChallenge(true);
    }
  });"""

NEW_HANDLER = """  const onChallengeInput = () => {
    const v = challengeInput.value;
    const cleaned = v.replace(/[\\u3131-\\u318E\\uAC00-\\uD7A3]/g, '');
    if (cleaned !== v) {
      const pos = challengeInput.selectionStart;
      challengeInput.value = cleaned;
      const removed = v.length - cleaned.length;
      const newPos = Math.max(0, (pos == null ? cleaned.length : pos) - removed);
      try {
        challengeInput.setSelectionRange(newPos, newPos);
      } catch (_) {}
    }
    if (challengeInput.value.trim().toLowerCase() === wordToChallenge.trim().toLowerCase()) {
      endChallenge(true);
    }
  };
  challengeInput.addEventListener('input', onChallengeInput);
  challengeInput.addEventListener('compositionend', onChallengeInput);"""


def patch_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if "id=\"challenge-input\"" not in text:
        return False
    orig = text
    text, n_in = INPUT_RE.subn(INPUT_REPLACE, text, count=1)
    if n_in != 1:
        print("WARN input tag:", path, n_in)
    if OLD_FOCUS not in text:
        print("SKIP focus block:", path)
        return False
    text = text.replace(OLD_FOCUS, NEW_FOCUS, 1)
    if OLD_HANDLER not in text:
        print("SKIP handler:", path)
        return False
    text = text.replace(OLD_HANDLER, NEW_HANDLER, 1)
    if text != orig:
        path.write_text(text, encoding="utf-8", newline="\n")
        return True
    return False


def main():
    paths = [ROOT / "game.js"] + sorted(ROOT.glob("unit*/game.js"))
    for p in paths:
        if p.is_file() and patch_file(p):
            print("OK", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
