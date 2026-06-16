# 2026-06-16 dogfood — joinfridays-com

**Mode:** regression
**Pages tiled:** homepage, pricing, weight_loss, testosterone, whats_included (5)
**Tier-B fired:** all 5 pages, `--dismiss` = **yes** on every one (single render each; no dual-render — overlay-only contamination, no WebGL/lazy)
**WARNINGs fired:** **none** (no `scroll_locked`, no missing-overview, across all 5 stderr captures)
**Manifest verdict:** `dismissed=true` ·  `scroll_locked=false` · `overview=overview-480w.png` — uniform on all 5

## What happened
The clean dogfood case. Every page's cached `2026-06-04` hero carried the same fixed `#cookie-consent-dialog` "Cookie Settings" widget (Accept All / Reject All / Customize) pinned bottom-right over real content — so the QA gate called Tier-B `--dismiss` on all five, matching the prior run's all-5 decision but now via affordance-only dismissal instead of the retired vendor list. Affordance-only cleared the dialog on every page with the top nav and hero content intact, exactly as the probe predicted for this site. `overview-480w` emitted cleanly on all five (no montage hack); QA-gated the re-renders the same way it reads cached pages. Mining: 60 raw → 51 accepted cards, lint exit 0.

## Surprising
- **Toolchain gap (the one real snag).** The skill's documented `python3 scripts/shoot.py` fails here — PATH `python3` is `/usr/bin/python3` 3.9.6 with **no playwright**. `tile.py` runs fine on it (stdlib), so the gap is invisible until the first `shoot.py` call. Had to drive Tier-B with the pyenv binary (`~/.pyenv/versions/3.11.9/bin/python3`, the only interpreter carrying playwright). Logging, not patching — but the skill's bare-`python3` line is environment-fragile for the Tier-B step.
- **Matched the probe, didn't surprise it.** The probe cleared joinfridays' `#cookie-consent-dialog` via *accept all*, 0 harm; the dogfood reproduced that on all 5 pages, 0 harm, no scroll-lock. Confirmatory, not novel — the overlay's buttons are `[Accept All, Reject All, Customize]` in DOM order, so the first scoped target clicked is Accept All (negative-first label priority is per-element, not cross-element).
- **Overlay persisted capture→live.** Opposite of the probe's functionhealth limit #5 (live Ketch banner the capture never saw): here the dialog present at `2026-06-04` capture was *still* live at `2026-06-16` re-render, so `--dismiss` had a genuine overlay to clear on every page.
- **Judge over-count (not shoot.py-related).** Judge prose claimed "31 accepted" but the array held **51** — the known judge-miscount the workflow already guards against (counts come from arrays). Drove a large card-count jump (below).

## For regression only: vs the prior visual.md
Same `qa_status: recapture-used`, same `captured_at`/`source_capture`, same Tier-B `2026-06-16` tile set (regenerated, path-compatible — all 20 prior-cited tiles still exist and validate). **Card count 34 → 51** (+17: typography 8→11, layout 12→21, color 8→9, iconography 6→10); distinct tiles cited 20 → 26. The delta is judge under-merge (the 51-vs-31 miscount), not a pipeline regression — the shoot.py changes themselves produced clean, equivalent tiles.

## Open follow-ups → BACKLOG.md
- Skill-doc: `shoot.py`'s `python3` invocation assumes playwright is on the resolved `python3`; here it needs the pyenv binary. Worth a one-line note in SKILL.md (or a `$PYBIN`-style resolve) so the Tier-B step isn't environment-fragile.
