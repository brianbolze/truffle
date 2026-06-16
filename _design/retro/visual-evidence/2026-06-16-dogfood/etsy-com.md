# 2026-06-16 dogfood — etsy-com

**Mode:** tricky (no prior visual.md — first visual layer for this slug)
**Pages tiled:** homepage, categories, sell, about, impact, press — 6 pages / 31 tiles. Mined: homepage + sell + about + impact + press (28 tiles); `categories` set aside (clean but low-signal text directory, not an exclusion).
**Tier-B fired:** none — QA gate found all 6 pages clean at native res; no escalation warranted, so `--dismiss` never ran.
**WARNINGs fired:** none — `shoot.py` never ran; `tile.py` emitted no warnings.
**Manifest verdict:** N/A — no `shoot.py` manifest written (no Tier-B). Only the Tier-A `tile.py` manifest exists, which carries no `dismissed` / `scroll_locked` / `overview` fields.

## What happened
Tier-A tiling + the QA gate carried the whole run. All six cached payloads (2026-05-31, US locale / basic proxy) were clean at native resolution — no cookie/consent banner, newsletter modal, grey/WebGL hero, black media card, or lazy-load gap. The new `--dismiss` / overview / scroll-lock paths in `shoot.py` had nothing to act on, so I did **not** escalate — manufacturing a re-render on a clean page would violate the skill's faithful-first discipline and produce a misleading dogfood. Blind mine returned **44 cards** (22 strong / 15 mixed / 7 poor) from 67 mined, 4/4 families reporting; every `poor` structural card spot-checked against its native tile (all real, no capture artifacts); `visualcheck.py` exit 0.

## Surprising
- **A "tricky" candidate came back clean — so this dogfood exercised QA *restraint*, not `shoot.py`.** A big consumer marketplace was a plausible overlay/cookie-banner case, but the cached capture carried none. This is exactly probe [FINDINGS](../../../../experiments/2026-06-16-tier-b-dismissal/FINDINGS.md) limit #5 (live ≠ capture-time): a live `--dismiss` re-render *today* might surface a consent/sign-in overlay the 05-31 capture never had — which is precisely *why* we don't re-render clean pages. Net: **zero lines of the new Tier-B code ran** on etsy.
- **Overview emission paid off on the Tier-A side only.** The 6 `overview-480w.png` thumbnails (from `tile.py`, pre-existing) made the QA triage fast and reliable; `shoot.py`'s *new* overview emission was not exercised here (no Tier-B). The #4 "overview ship-it" win holds, but its `shoot.py` half is still untested by this slug.
- **Judge self-count muddle, as the workflow anticipates.** The judge's prose `notes` contradicted itself on the count ("...44 IDs? no..."); the workflow's array count (44, matching the 22+15+7 polarity sum) is authoritative and correct. The known-flaky self-count guard held — no action needed.

## For regression only: vs the prior visual.md
N/A — etsy is tricky, not regression. No prior `visual.md` existed (the old pipeline never wrote one for this slug); this is the first visual layer written for it, so there's nothing to diff.

## Open follow-ups → BACKLOG.md
None for etsy specifically. **Cohort note (not a BACKLOG item):** etsy ran zero new `shoot.py` code — at least one other dogfood slug must actually trigger `--dismiss` (and ideally a `scroll_locked` case) for the port from `probe.py` to be genuinely exercised. Etsy is best read as a **negative control**: evidence the QA gate doesn't over-escalate on a clean capture.
