# 2026-06-16 dogfood — parlance-cc

**Mode:** regression (prior `visual.md` existed, committed `ab02af8`)
**Pages tiled:** homepage, creative_capital, faq, fte, scottwitt, sprints — 19 tiles (Tier-A, `tile.py`)
**Tier-B fired:** none — QA gate found all 6 pages clean; `shoot.py` not invoked, `--dismiss` not used
**WARNINGs fired:** none — `shoot.py` never ran, so `scroll_locked` / missing-`overview-480w` WARNINGs were not reachable this run
**Manifest verdict:** no `shoot.py` manifest this run (Tier-A only). The `dismissed` / `scroll_locked` / `overview` fields are `shoot.py`'s and went un-exercised. The `overview-480w.png` the QA gate read came from `tile.py` (Tier-A), all 6 present.

## What happened
The cached 2026-06-10 capture was genuinely clean: across all six `overview-480w.png` plus native spot-checks (homepage hero/notes, faq body, the centered CTA + footer band, sprints' More-Articles row), no overlay, grey/WebGL hero, black media, lazy-load gap, or mid-animation. So the QA gate correctly declined to escalate — `qa_status: clean`, zero Tier-B. The blind fan-out (4 Sonnet miners → Opus judge) mined 48 raw → **34 accepted (20 strong / 11 mixed / 3 poor)** across all four families. Lint green. **parlance-cc is a negative control for the new `shoot.py`: it exercises the gate's *restraint*, not the dismissal mechanism — none of `--dismiss`, the `overview-480w` emitter, scroll-lock, or clean/dirty labeling ran, because nothing was dirty.**

## Surprising
- **vs the probe:** the entire 06-16 dismissal apparatus was untouched here — the probe is about clearing overlays in Tier-B, and this capture never reached Tier-B. Worth stating plainly so the 8-retro read shows which slugs hit `shoot.py` and which (like this one) only prove the gate doesn't false-positive on a clean cache.
- **lazy-load look-alike the probe doesn't cover:** sprints' "More Articles" row shows a *single* card with the rest of the row empty — reads at a glance like a lazy-load failure. It's genuine (the footer below fully settled with live clocks at 21:14:49; the one card renders complete; sibling pages render 3–4 cards from the same component). Kept as `layout_11` (mixed). This is a judgment the *sighted QA step* must make, not `shoot.py` — and the Tier-A `overview-480w` is what made it callable in one look.
- **judge `contrast_with` can cite a tile that doesn't show the claim:** `color_04` (chevron device) had its `contrast_with` pointing at `sprints/tile-01`, which actually shows the TIME card, not the chevron. The blind miners/judge can't verify a *contrast* tile genuinely contains the claimed element, and `visualcheck.py` only checks existence / non-self / active — so it passes lint while being wrong. Caught sighted; repointed to `homepage/tile-03` (where the chevron thumbnail really recurs). Not a `shoot.py` issue, but a real pipeline gap for the batch.

## For regression only: vs the prior visual.md
Same 19 tiles, same `qa_status: clean`, no Tier-B in either run; the new Opus-judge pass goes **19 → 34 cards** (12s/7m/0p → 20s/11m/3p), newly mines **scottwitt** (3 cards) the prior left uncited and surfaces the first **3 `poor` tells** (centered CTA breaking flush-left, untreated TIME cover, no data-viz craft) — `creative_capital` stays uncited in both.

## Open follow-ups → BACKLOG.md
`contrast_with` is lint-checked for existence/non-self/active but never that the cited tile *shows* the contrast — a blind judge can mis-cite it (this run's `color_04`). Candidate guard; Brian to weigh across the 8 retros.
