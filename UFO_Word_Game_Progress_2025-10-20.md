# UFO Word Game - Daily Progress (2025-10-20)

## Summary
- Created safety checkpoint (commit, tag, branch) before tablet fixes.
- Fixed tablet start-screen text rendering on `unit20` (`style.css` media query tweaks).
- Stabilized TTS on tablets: warm-up, voices-ready, resume, BGM ducking.
- Adjusted asset/data paths in `unit20` to relative paths for LAN tablet access.
- Implemented tablet-only TTS policy in `unit20`: suppress first word; from second word speak GB once.
- Rolled out tablet-only TTS policy to `unit1`–`unit10` keeping PC/phone behavior unchanged (US then GB).

## Git Safety
- Branch: `feat/tablet-fixes`
- Tag: `safety-pre-tablet-fixes`
- Checkpoint commit before changes.

## Changes by Area
- Unit 20:
  - `style.css`: tablet typography smoothing under 768–1024px.
  - `game.js`: robust TTS init (voices ready, warm-up, resume, BGM pause during speech), relative paths, tablet policy (first word none, then GB once).
  - `index.html`: cache-bust `game.js` to ensure latest on device.
- Units 1–10:
  - `game.js`: tablet-only TTS policy added (first word none; then GB once). PC/phone remain US+GB.

## Testing
- PC localhost: OK (Unit 20).
- Tablet over LAN: start-screen text OK; data loads via relative paths; first utterance artifacts mitigated by suppressing first word and using GB-only thereafter.

## Outstanding
- Apply the same tablet-only TTS policy to Units 11–20.
- Optional: unify TTS helpers across units to reduce duplication.

## Next Steps (2025-10-21)
1. Roll out tablet-only TTS policy to `unit11`–`unit20`.
2. Quick regression pass on PC/phone to confirm US+GB remains.
3. If desired, centralize TTS init/utilities.
