# 2026-06-16 dogfood — ro-co

**Mode:** regression
**Pages tiled:** homepage, weight-loss, pricing, hair-loss, os
**Tier-B fired:** os only — `--dismiss` **n** (no overlay in any cached payload)
**WARNINGs fired:** none
**Manifest verdict:** dismissed=false · scroll_locked=false · overview=overview-480w.png ✓

## What happened
QA gate read the 5 per-page overviews: 4 pages clean Tier-A; `os` carried the same lazy-load gap as the 06-14 baseline — empty right columns where the Care Delivery / Pharmacy / Lab app-UI mockups float. Re-rendered os faithful (no `--dismiss`) through the new `shoot.py`: 19/23 images loaded, mockups + gradient blobs recovered (confirmed on native tiles), clean per-page manifest, no stderr WARNING, `overview-480w.png` emitted. Blind mine (Sonnet ×4) → judge (Opus) → step-4 spot-check → 29 cards, lint green.

## Surprising
- **`--dismiss` never had cause to fire.** ro.co is a pure lazy-load Tier-B case — zero overlay across all 5 cached payloads — so this regression member exercises the *faithful-default* path + overview emission + the new manifest labeling, **not** the affordance dismissal. Consistent with the probe's no-overlay controls (sorafuel/warbyparker: no-op). The dismissal path is simply unexercised by ro-co; it needs an overlay member to dogfood.
- **shoot.py doesn't clean its out-dir, and doesn't reconcile the root tiler manifest** (the one genuinely new edge here). The Tier-B page is taller than the cached shot (scrollHeight 9274 vs 8946), so the new `tile-07-y07874.png` didn't overwrite the stale Tier-A `tile-07-y07546.png` → an **orphan tile** survived in the dir. And the root `tiles/manifest.json` (source: `tile`) still points os's last tile at y07546, now a **dangling reference**, while the per-page `tiles/os/manifest.json` (source: `shoot`, with `dismissed/scroll_locked/overview`) is correct — the two manifests disagree about os and nothing reconciles them. The probe never hit this (it rendered into fresh dirs, not into an existing Tier-A tile tree). Orthogonal to `--dismiss`; an overview/labeling-rollout × existing-tiler interaction. I removed the orphan and assembled the active tile list from the per-page shoot manifest, so it never reached the miners. **Logged, not patched** (per brief).
- **overview-480w is necessary-but-not-sufficient for pale recovered media.** At 480w the os overview *still looked empty* — the soft watercolor gradient blobs wash out in the downsample — so the overview alone would have falsely "failed" the re-render. Native-tile spot-check was required to confirm the mockups loaded. The labeling/manifest win is real; the overview's QA value drops for low-contrast media (and the SKILL already says to fall back to tile spot-check — here that fallback was load-bearing even with overview present).
- (env, not shoot.py) playwright isn't on the Bash-tool's default `python3` (`/usr/bin/python3`); needed the real pyenv `3.11.9` binary. Known shim-gotcha flavor.

## For regression only: vs the prior visual.md
27→29 cards; `qa_status` unchanged (recapture-used), same single Tier-B page (os); family mix shifted **layout 7→5 / color 6→8 / icon 6→8** — the new run surfaced more color & iconography tells, and the step-4 spot-check dropped 3 `poor` layout over-calls (incl. the goal-selector grid the 06-14 run rated **strong**). os re-rendered fresh so its last-tile offset moved (y07546→y07874), but cited os tiles overlap on the stable early offsets (y0/1220/2440/3660/4880).

## Open follow-ups → BACKLOG.md
Tier-B re-render into an existing capture leaves an orphan tile + a stale/dangling root `tiles/manifest.json` for the re-rendered page — `shoot.py` should clean its out-dir and/or the run should reconcile the root tiler manifest (else a glob-based consumer reads stale/missing os geometry).
