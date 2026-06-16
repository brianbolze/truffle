# 2026-06-16 dogfood — mydrhank-com

**Mode:** regression
**Pages tiled:** homepage, category-weight-loss, category-longevity, pdp-compounded-semaglutide, pdp-nad-injection (5 pages, 24 tiles)
**Tier-B fired:** all 5 pages, `--dismiss` = **yes** (single render each; no dual-render)
**WARNINGs fired:** **none** — no `scroll_locked`, no missing `overview-480w` on any page
**Manifest verdict:** `dismissed=true` (5/5) · `scroll_locked=false` (5/5) · `overview=overview-480w.png` (5/5)

## What happened
Every cached Firecrawl payload carried the site-wide "We use cookies" consent strip stamped over high-value regions (hero, product grids, PDP calculator/FAQ), so the QA gate called Tier-B on all five. `shoot.py --dismiss` cleared the strip affordance-only — Escape + a click on its own **"Reject all"** control — and on every page the sticky nav survived, the page never scroll-locked, and an `overview-480w.png` was emitted for the QA re-scan. Clean tiles across the board; **zero exclusions, zero WARNINGs**. Blind mine → judge produced 21 cards (39 raw), lint exit 0.

## Surprising
- **The probe's mydrhank prediction held exactly** ("bottom cookie strip + sticky nav → affordance clears cookie via reject-all, nav kept") — but the *cached* shot showed the banner **mid-content, not bottom-pinned**: Firecrawl composites the sticky strip at its scroll position into the full-page PNG, so the live "bottom strip" lands over the hero/grids in the cached image. Capture-time ≠ live position (echoes FINDINGS limit #5). The dismiss target is the same either way.
- **New `overview-480w` (#4) worked first-try on all 5** — no `magick` failures, no missing-overview WARNING. The independent low-risk win behaved as designed.
- **Old pipeline clicked "Accept all"; new clicks "Reject all"** (negative-first affordance order). Banner clears identically; only the provenance wording changes. Tiles are visually equivalent to the baseline's.
- **Forced scroll-lock reset never fired** — as the approach doc flagged it wouldn't here; mydrhank was never locked. Still an unexercised path.
- **Stale per-page manifest after re-tile (minor):** `tile.py` rewrites only the top-level `tiles/manifest.json` (`source: tile`); it leaves each page's prior `manifest.json` (`source: shoot`, from the old run) in place. Here `shoot.py --dismiss` overwrote all 5, so final state is correct — but a page left at Tier-A would keep a stale shoot-manifest beside cached-derived tiles.
- **SKILL `--out-dir <today>` vs source-capture-date dir:** SKILL step 2 writes Tier-B into `captures/<today>/tiles/<page>`, but the baseline + VISUAL.md keep tiles under the dossier date (`2026-06-03`). I rendered into `2026-06-03` to keep the regression apples-to-apples; literal `<today>` would split tiles across two date dirs while `source_capture` stays the dossier date. Doc ambiguity worth resolving.
- **Judge self-count typo:** notes say "39 → 24 accepted" but the array, `accepted_count`, and polarity all sum to **21**. Cosmetic; data is consistent.

## For regression only: vs the prior visual.md
Same 5 page dirs cited, `qa_status` no drift (recapture-used → recapture-used), `source_capture` unchanged — but **card count 31 → 21** (typography 7→5, layout 10→7, color 8→5, iconography 6→4; polarity 13/10/8 → 8/9/4); the new judge merged more aggressively (39→21 vs baseline 38→31), so the delta is blind-mine/judge variance, not a Tier-B effect — both reads land the same through-line ("disciplined template, shallow imagery").

## Open follow-ups → BACKLOG.md
- Resolve the SKILL `--out-dir <today>` vs source-capture-date-dir ambiguity (one line) — pick one so Tier-B tiles don't fork across date dirs while `source_capture` stays the dossier date.
- Optional: have `tile.py` drop/refresh stale per-page `manifest.json` left by a prior `shoot.py` run, so a Tier-A-only page can't carry a `source: shoot` manifest.
