# Retro — Healthspan deep visual-evidence run (2026-06-15)

Brian asked to "go deep" on an important competitor (`gethealthspan-com`). Landed clean: [`store/gethealthspan-com/visual.md`](../../../store/gethealthspan-com/visual.md), **39 cards** across all four families, lint exit 0. Output is trustworthy and strategically useful — the strengths/weakness split was crisp (owned product/data assets strong; borrowed people-photography + empty dark transitions weak). Three process notes, two of which confirm prior lessons.

## Lesson 1 — timed modals beat Tier-B (sharpens the Blokes lesson)

The homepage hero had a "10% off" newsletter modal over the headline+CTA. Per the Blokes retro, this is a *legit* Tier-B trigger — contamination destroying evidence the page depends on (the hero), not a cosmetic stitch artifact. So I escalated to `shoot.py`. It **traded down again**: the modal is a timed first-visit popup, so the fresh render re-fired it — now over the *program cards*, which the cached capture had clean.

**New takeaway:** even a valid Tier-B trigger fails against timed/consent popups, because a fresh load re-arms them. When the cached capture caught the page pre-popup on the tiles that matter, prefer **exclude-the-bad-tile** over re-render. Here the hero's brand treatment was redundantly covered by clean full-bleed heroes on `our_company` / `how_it_works` / `labs`, so excluding one tile cost nothing. Tier-B remains right only for *static* contamination (grey WebGL hero, black media) — not anything time- or interaction-triggered.

## Lesson 2 — "go deep" vs the 8–14 card contract

Fan-out mined 49 → judge accepted 39 (~80% kept, same under-prune ratio as Blokes). Contract target is 8–14. On Blokes I curated down by hand; **this time I kept all 39 on purpose** — a deep run on a priority competitor wants the full audit trail, and the impression carries the 5-second layer above it.

So the tension is real: the judge under-prunes *and* the "typical 8–14" target doesn't fit an explicit deep run. Suggests the count target should be **intent-scaled** (default ~12; deep / N-page runs allow more) rather than a fixed band the judge ignores anyway. Still worth an experiment before touching the prompt.

## Smaller notes

- **Path duality recurred** (now 2/2 runs). Lint wants repo-relative `tile_path`; miner agents run in the *project* cwd and need absolute paths to read PNGs. Passed absolute, rewrote to relative when authoring. This is no longer a one-off — it deserves a line in SKILL.md, or a path-normalize step in the workflow.
- **Cookie banner ≠ exclusion.** Five tiles had a non-blocking corner "We use cookies" strip; the judge correctly kept them (banner in dead space, content legible). The blind layer handled it exactly as designed — no human intervention needed.
- **Quality held** at 76 tiles × 4 Sonnet miners + Opus judge. No taste-word vibes; calibrated strong/mixed/poor spread.

## Net

Output: strong, and the right depth for the ask. Process: the two latent gaps from Blokes (Tier-B judgment, judge ceiling) both resurfaced — neither blocked the run, both now have two data points. Path duality is past "note" and into "fix."
