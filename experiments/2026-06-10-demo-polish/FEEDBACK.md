# Demo-polish ledger — render.py briefs for the 2026-06-12 Scott demo

Yardstick: "lands with a creative director in 5 seconds." Three test briefs:
parlance-cc (sparsest capture — degradation test) · onepeloton-com (shared
reference brand) · marquelongevitylab-com (Scott did the brand — identity-fidelity test).

Triage buckets: **done** · **this-round** (queued for the current fix batch) ·
**post-Scott** (deliberately deferred — let his live reaction decide, per BACKLOG
"tune for a brand-strategy reader").

## Round 1 — 2026-06-10

Rendered all three from current master, no changes yet. Pre-render state notes:

- Parlance has no offerings.md / no assets/ — Offer architecture tab falls back to
  family-level prose + "no per-SKU roster" note; hero wordmark fetched remotely (PNG
  on paper plate). Profile prose is complete (all five sections + extras present).
- Marque is missing a "Strategic read" section → renders a "not captured" placeholder.
- Switzer (Parlance) and Nb Architekt (Marque) aren't on Google Fonts → typography
  tab shows "substituted" and the display face falls back to the sans stack.

### Raw notes → triage

| # | Note (Brian, verbatim-ish) | Triage | Resolution |
|---|---------------------------|--------|------------|
| 1 | Classification rows (Entity, Industry…) eat room; generic by design, not Scott-useful | **done** (f92f8d0) | Demoted to one quiet chip strip; "sells to" leads; default `entity: Company` dropped |
| 2 | Hero descriptions run 5-6 lines — feels wrong for a hero headline; idea: Haiku/Sonnet drafts a short headline for this layer | **done (interim)** (3203089) + **post-Scott** | Type size now steps down with length. Agent-drafted headline **parked by Brian** (round 2) — first generated copy in a verbatim surface; revisit after the meeting |
| 3 | Too much long prose generally; maybe lightweight post-processing — but keep the layer dumb/faithful | **post-Scott** | Condensation parked with #2; deeper restructuring waits on Scott's reactions |
| 4 | Positioning + target audience not prominent enough for a brand strategist | **done** (b1d8ddc) | "Positioning & audience" promoted to slot 2, open by default |
| 5 | Wife demo: 20+ s to answer "tell me about Parlance" + render | **done (renderer's share)** (b17f0af) | `--all` pre-warm flag; remaining latency is agent synthesis, not render.py — demo choreography: pre-render before the meeting |
| 6 | Wife demo: "so what / what can't Claude do alone" — built a presentation layer? | **done** (259ec68) | Brian called the gate → `render.py --index` built: 101 companies, per-layer clocks, stat band, links to briefs. The demo opener |
| 7 | Immersion-phase + comparison value didn't come across | **post-Scott / parked** | Comparison view stays parked per BACKLOG rule-of-two; wife demo ≠ second human ask |

## Deferred until after the meeting (post-Scott)

- (per BACKLOG) Reorder for a brand-strategy reader — voice/positioning *leading the
  whole brief*, language-extraction surfaces. Let Scott's reactions pick the changes.
- Cross-company comparison artifact — parked in BACKLOG on the rule of two.
- Agent-drafted hero headline + prose condensation (Brian parked it round 2 — keep the
  layer verbatim through the demo; Scott's reaction to the long descriptions decides).
