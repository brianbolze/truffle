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
| 2 | Hero descriptions run 5-6 lines — feels wrong for a hero headline; idea: Haiku/Sonnet drafts a short headline for this layer | **done (interim)** (3203089) + **this-round?** | Type size now steps down with length. Agent-drafted headline = open fork, Brian to call |
| 3 | Too much long prose generally; maybe lightweight post-processing — but keep the layer dumb/faithful | **this-round?** | Hangs on the same fork as #2 (how far condensation goes). Deeper restructuring → post-Scott |
| 4 | Positioning + target audience not prominent enough for a brand strategist | **done** (b1d8ddc) | "Positioning & audience" promoted to slot 2, open by default |
| 5 | Wife demo: 20+ s to answer "tell me about Parlance" + render | **done (renderer's share)** (b17f0af) | `--all` pre-warm flag; remaining latency is agent synthesis, not render.py — demo choreography: pre-render before the meeting |
| 6 | Wife demo: "so what / what can't Claude do alone" — built a presentation layer? | **this-round?** | This is the `--index` corpus page's exact job; gated on Brian calling it |
| 7 | Immersion-phase + comparison value didn't come across | **post-Scott / parked** | Comparison view stays parked per BACKLOG rule-of-two; wife demo ≠ second human ask |

## Deferred until after the meeting (post-Scott)

- (per BACKLOG) Reorder for a brand-strategy reader — voice/positioning *leading the
  whole brief*, language-extraction surfaces. Let Scott's reactions pick the changes.
- Cross-company comparison artifact — parked in BACKLOG on the rule of two.
- Prose condensation beyond the hero (if the agent-headline fork opens at all).
