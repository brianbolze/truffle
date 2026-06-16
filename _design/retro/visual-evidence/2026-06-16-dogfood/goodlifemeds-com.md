# 2026-06-16 dogfood — goodlifemeds-com

**Mode:** regression
**Pages tiled:** homepage, semaglutide, sexual_health, weight_loss (40 tiles; Tier-A from the 2026-06-04 payloads, then all four re-rendered Tier-B)
**Tier-B fired:** all 4 pages with `--dismiss` (the active set) + homepage & semaglutide *also* rendered faithful (no flag) as A/B controls — **6 renders total**
**WARNINGs fired:** **none** — and that absence *is* the finding (the failure was silent)
**Manifest verdict:** every render `dismissed=true` (where flagged), `scroll_locked=false`, `overview-480w.png` emitted — all clean, yet the overlay was never cleared

## What happened
The QA gate flagged a site-wide "Your Privacy Choices" consent overlay over content on all four cached pages, so I re-rendered each Tier-B with `--dismiss`. Every run exited 0 with no stderr WARNING — but `--dismiss` **did not clear the CMP**: it stayed pinned lower-right in every live tile (confirmed on native tiles of all four pages; the homepage/semaglutide faithful controls carry it identically, so `--dismiss` was a verified no-op, not a partial clear). Its buttons ("Allow" / "Don't Allow" / "More choices") are off `DISMISS_LABELS`, Escape doesn't close it, and — per the baseline's diagnosis — it sits behind a *closed shadow root* the affordance finder's `querySelectorAll` can't even see into. The blind miners/judge treated the corner as a capture caveat by construction; I dropped the one card the judge emitted *about* the CMP plus two layout `poor` reads that failed native-tile spot-check, and shipped **26 cards** with a loud Provenance caveat. (The semaglutide teal "0" is a real empty-input BMI calculator — `layout_05` reads it as a *strong* component — not a stuck count-up; my early artifact worry was a false alarm, matching the baseline.)

## Surprising
- **The safe ceiling failed *silent*, not loud.** Probe FINDINGS limit #1 says an un-dismissable banner "must **fail loud** (exclude/caveat), never silently-wrong." It didn't. The CMP doesn't lock scroll, so `scroll_locked` stayed `false` and `overview` emitted — the only two loud signals both passed. `dismissed=true` reports what *ran*, not whether it *worked*; there is no "overlay still present after dismiss?" check anywhere in the manifest or stderr.
- **Removing the structural-hide was a real capability loss *here*.** The approach doc dropped CONSENT_MOUNTS as "cleared nothing affordance didn't." goodlifemeds is the counterexample: the baseline's *only* path to a clean tile was **hiding the Transcend mount** (its note: click-dismiss "missed it — duplicate widget + closed shadow root"). Affordance-only has no fallback, so the new pipeline can't clear what the old one could.
- **A closed shadow root is a failure mode the 8-site probe never hit** — the dismiss buttons aren't reachable by `querySelectorAll` at all, so the affordance finder is blind *before* the off-list-label problem even applies. Two independent reasons it can't clear this CMP.
- **overview-480w hid the corner CMP** (false-negative at 480w) — I misread the first faithful overview as clean; the native-tile spot-check is what caught the contamination. The new overview is necessary but not sufficient for a fixed corner overlay.
- **The blind judge can't fully self-police the caveat/card line** — it surfaced the CMP as a `poor` *design* card (well-intentioned flag) rather than excluding it. The human spot-check (SKILL step 4) is load-bearing, exactly as written.

## For regression only: vs the prior visual.md
`qa_status` unchanged (`recapture-used`); same 4 pages, same 40-tile shape; re-render date 06-15→06-16. Card count **16→26** is mostly curation philosophy (baseline hand-curated 16 of 38 accepted; this run ships 26 of 29, dupes already merged in-judge per the "comprehensive, not capped" contract), not a quality delta. The real diff: **baseline tiles were CMP-clean (old pipeline hid the consent mount); these tiles carry the un-cleared CMP** + a loud caveat + an occluded lower-right corner.

## Open follow-ups → BACKLOG.md
Affordance-only `--dismiss` *silently* fails on closed-shadow-root / off-list-label CMPs (Transcend "Your Privacy Choices") — no WARNING fires. Worth a backlog line: add a post-dismiss **"overlay still present?"** loud check (persistent fixed high-z element after dismiss → warn), and reconsider a narrow, opt-in structural-hide for this CMP class the probe's 8 sites didn't include.
