# Retro — Blokes visual-evidence run (2026-06-15)

First `/visual-evidence` run on an already-captured company (`joiandblokes-com`). Landed clean: [`store/joiandblokes-com/visual.md`](../../../store/joiandblokes-com/visual.md), 14 cards, lint exit 0. The artifact is trustworthy; two process lessons worth keeping.

## Lesson 1 — Tier-B is not a free upgrade

The cached tiles had one mild, *predictable* artifact: Firecrawl's full-page stitching re-composites the fixed nav bar once per scroll segment, so a white band intermittently overlays content. I escalated to Tier-B (`shoot.py`) to remove it — and traded down. The live site fired a "Stay Connected" newsletter modal over the content, and three of four renders collapsed to 1–2 tiles (a consent/modal wall blocked full-page capture). Reverted to Tier-A; final evidence is cached-only.

**Why it was the wrong call:** the workflow's BLIND prompt already tells miners to treat compositing artifacts as capture caveats, and the judge rejects artifact-derived cards. The nav band was *already handled*. I re-rendered to fix a problem the pipeline absorbs by design — and a live page is a moving target (modals, consent walls, lazy gaps) the cached snapshot isn't.

**Takeaway:** reserve Tier-B for contamination that destroys evidence the page *depends on* (grey WebGL hero, black media cards) — not cosmetic stitching artifacts the blind layer already discounts. A mild *known* artifact in a clean cached capture beats an unknown live render.

## Lesson 2 — the judge under-prunes

The fan-out mined 50 raw cards; the judge accepted **42**. The contract target is **8–14**. So the "prune/merge" pass kept ~84% — barely a filter. I curated to 14 by hand (balanced across families, honest strong/mixed/poor mix) and renumbered ids.

It worked, but it means the human synthesizer is doing the judge's job. If this recurs across companies, the judge prompt likely needs a hard count ceiling ("keep the 10–14 highest-signal, one card per distinct tell") rather than the soft "prune and merge" it has now. Worth an experiment before changing the prompt.

## Smaller notes

- **Path duality.** Lint wants repo-relative `tile_path`; miner agents run in the project cwd (not the Web Research repo) and need absolute paths to read the PNGs. Passed absolute to the workflow, rewrote to relative when authoring. A run launched from inside the Web Research repo wouldn't hit this — worth a line in SKILL.md.
- **Quality held.** Sonnet miners + Opus judge produced calibrated cards — distinctive strengths (dark/light dual palette, custom donut + decline-chart data-viz) cleanly separated from finish slips (stock feature icons, wireframe-y phone mockup). No taste-word vibes.

## Net

Output: good. Process: one avoidable detour (Tier-B) and one latent gap (judge ceiling). Both cheap to fix.
