# 2026-06-16 dogfood — alange-soehne-com

**Mode:** tricky (no prior visual.md — first run on this site)
**Pages tiled:** homepage, all-timepieces, manufacture, heritage (45 Tier-A tiles)
**Tier-B fired:** homepage only — **both** faithful (no `--dismiss`) and `--dismiss`. **Neither shipped** — fell back to cached Tier-A.
**WARNINGs fired:** `scroll_locked` ×2 (faithful + `--dismiss`). No missing-overview WARNING (magick fine both runs).
**Manifest verdict** (`--dismiss` run, preserved off-store): `dismissed=true`, `scroll_locked=true`, `overview=overview-480w.png`, `source=shoot`. Final shipped set: **cached Tier-A, `qa_status: exclusions-noted`**, 32 active tiles, 29 cards (15 strong / 8 mixed / 6 poor).

## What happened
Cached Tier-A was clean almost everywhere — confident editorial heros, a disciplined product grid, bespoke engraving illustration. Two QA flags: (1) **all-timepieces** lazy-load gap — Firecrawl shot the 26k-px catalogue before the lower product images loaded, leaving text-only cards from tile-09 on; excluded tiles 09–21, kept the loaded top rows 00–08 (the grid/card/photography evidence is all there). (2) **homepage** carried a region-notice strip and looked like the right `--dismiss` candidate, so I ran Tier-B both ways. The live Chrome load throws a **scroll-locking overlay `--dismiss` can't clear** — the lock held, the hero came back as a black block, tiles were mislabeled. The cached hero was *cleaner* than the re-render, so I reverted homepage to cached and mined that. Blind 4-miner + judge fan-out then ran on 32 tiles; all 6 `poor` cards spot-checked against native tiles (all real design tells, zero artifacts).

## Surprising
*(vs [probe FINDINGS](../../../../experiments/2026-06-16-tier-b-dismissal/FINDINGS.md) / [approach doc](../../../2026-06-16-tier-b-approach.md))*

- **The "locked but un-dismissable" edge is real — and it fired the unproven fallback, which also failed.** The probe (limit #2) said dismissal released *both* locked sites for free and the forced `overflow/position` reset was "never exercised… unproven belt-and-suspenders." Here `--dismiss` did **not** release the lock, so `release_scroll_lock` ran its forced reset — and that **also** failed (`scroll_locked=true` under `--dismiss` means both paths lost). First live exercise of the fallback; it didn't work. This is exactly FINDINGS limit #1's banner-with-no-recognized-affordance case, now observed.
- **…but the loud-not-silent ceiling worked as designed.** The un-dismissable overlay produced a `scroll_locked` WARNING on stderr, not a silently-wrong tile set. The intended safe behavior (fail loud → exclude/caveat/fall back) is what let me catch it and revert. The guard earned its keep.
- **Tier-B was net-negative vs Tier-A here — inverting the escalation assumption.** The approach doc treats Tier-B as the *cleaner* escalation. On this site the cached Firecrawl hero (the "25" date-wheel macro) was clean, while live Chrome rendered the hero black + scroll-locked. "Re-render to recover a contaminated page" assumed the re-render is better; sometimes cached wins and the right move is to *not* ship Tier-B. Worth making explicit in the SKILL: cached-vs-Tier-B is a comparison, not an automatic upgrade.
- **`shoot.py` doesn't clean its out-dir.** Re-rendering into a dir that already held Tier-A tiles left **both sets coexisting** — shoot.py's y-suffixes differ from tile.py's, so nothing overwrote; old crops + new tiles mixed, while overview/manifest got clobbered. The SKILL says "replace the page's tiles," but the operator must do the replacing (rm the dir first). Not patched (per brief) — logged.
- **`source_url` (#7) bit exactly as the doc warned.** homepage's stored `sourceURL` is the bare geo-redirecting domain, not the region-resolved URL; the rest of the dossier is `us-en`. So the re-render URL was a judgment call (I used `…/us-en/` to match the cohort). Confirms the paired #7 note is a real papercut, not hypothetical.

## For regression only: vs the prior visual.md
N/A — tricky mode, no prior visual.md existed.

## Open follow-ups → BACKLOG.md
- `shoot.py` should clear its `--out-dir` before writing (or warn on a non-empty dir) — re-rendering over Tier-A tiles silently leaves a mixed set.
- Un-dismissable scroll-lock is a live, reproducible case (alange homepage): the forced-reset fallback fired and failed. Decide the sanctioned response — detect iframe/shadow-DOM CMPs, or document "fall back to cached / exclude" as the answer and stop treating the forced reset as a fix.
- SKILL nuance: Tier-B is a *comparison* against cached, not an automatic upgrade — when the re-render is worse (black hero, scroll-lock), keep cached and ship `exclusions-noted`.
