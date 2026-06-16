# 2026-06-16 dogfood — doordash-com

**Mode:** tricky (new — no prior visual.md; non-telehealth consumer/gig marketplace)
**Pages tiled:** homepage · merchant · business · dasher · about (dashpass skipped — 970-byte thin page)
**Tier-B fired:** `homepage` (www.doordash.com) `--dismiss` **Y → blocked by Cloudflare bot wall, not adopted**; `business` (work.doordash.com) `--dismiss` **Y → success, cookie banner cleared, adopted**
**WARNINGs fired:** **none** — on any render (the bot wall fired zero; see Surprising #1)
**Manifest verdict:** adopted Tier-B (business) → `dismissed=true · scroll_locked=false · overview=overview-480w.png` ✓ · homepage Tier-B (walled, discarded) → `dismissed=true · scroll_locked=false · overview=emitted` but `title="Just a moment..."`, 1 tile
**Result:** 27 active tiles → 33 cards (15 strong / 13 mixed / 5 poor) · `qa_status: recapture-used`

## What happened
The QA vision gate flagged one load-bearing overlay — the consumer homepage hero buried under a sign-in modal + dark scrim — and a site-wide `position:fixed` cookie banner sitting on every page's footer tile. Ran `shoot.py --dismiss` on `www.doordash.com` to recover the hero; it returned a Cloudflare "verify you are human" interstitial (deterministic across two runs), so homepage fell back to cached Tier-A with the modal tile excluded. The same `--dismiss` on the `work.doordash.com` subdomain rendered the real page and cleanly cleared the bottom cookie banner (top nav kept) → adopted those tiles. Footer cookie banners on merchant/dasher/about (low-value legal strip) were excluded rather than re-rendered. Mining + judge returned 33 cards; all 5 `poor` structural cards spot-checked genuine against their native tiles.

## Surprising
- **#1 (the big one) — a Cloudflare bot wall passes every shoot.py guard silently.** `www.doordash.com` served a "Just a moment…" challenge; shoot.py captured it as a clean 1-tile render with `dismissed:true`, `scroll_locked:false`, overview emitted, and **no WARNING**. The new pipeline has zero bot-wall/interstitial detection, so an upstream challenge produces a clean-*looking*-but-useless Tier-B tile set — the exact "silently-wrong, not loud" failure the approach doc warns against, except the source is an upstream wall, not an overlay edge. Only the human QA vision step caught it. The probe's 8 sites never hit this (FINDINGS didn't list it as a limit).
- **#2 — the wall is www-only.** `work.` / `get.` / `dasher.` marketing subdomains render fine; only the consumer apex walls headless Chrome. So Tier-B is viable for DoorDash's B2B/dasher pages but **not** for the one page that actually needed it (the modal-covered consumer hero) — that tile is simply lost.
- **#3 — `--dismiss` cleared a real cookie banner cleanly** (business), reproducing the probe's mydrhank pattern (cookie gone via the page's own affordance, top nav kept, 0 harm) — first confirmation on a giant non-telehealth consumer marketplace, not just the probe cohort.
- **#4 — overview-480w did its job.** Both the cached (tile.py) and Tier-B (shoot.py) overviews drove the contamination triage; the overview is what surfaced the *site-wide* footer cookie banner repeating across pages. The `tile.py` Tier-A path already emits the same overview, so the QA gate read cached and re-rendered pages uniformly — exactly the #4 intent.
- **#5 — the cookie banner is footer-only.** Being `position:fixed; bottom:0`, it lands solely in each page's last tile (over the legal strip), so it's never hero contamination — the exclude-path handled it. Only the homepage's *centered* modal was load-bearing, and that was the un-recoverable one.

## For regression only: vs the prior visual.md
N/A — tricky/new site. No prior `visual.md` existed for doordash-com; the old pipeline never wrote one, so there's nothing to diff.

## Open follow-ups → BACKLOG.md
- **shoot.py has no bot-wall / interstitial guard.** A Cloudflare "Just a moment…" challenge renders as a clean 1-tile capture (`dismissed:true`, overview emitted, no WARNING). Candidate loud guard: known challenge markers (`title=="Just a moment..."`, Cloudflare Ray-ID body) **or** the structural tell (single viewport-height tile + near-zero loaded images, `loaded 0/1`) → `WARNING [url]: looks like a bot-wall/interstitial, not the page — exclude or capture via a non-walled subdomain.` (Per instructions: logged, **not** patched.)
- **Stale per-page manifest after a failed Tier-B.** shoot.py writes a per-page `manifest.json`; tile.py writes only the roll-up `tiles/manifest.json`. After the walled homepage render, the per-page shoot manifest lingered claiming homepage was a 1-tile dismissed render — tile.py's Tier-A restore didn't overwrite it. Had to delete it by hand so provenance wasn't falsely labeled. Minor footgun worth a one-line note in the SKILL's "loud-not-silent" bullet.
