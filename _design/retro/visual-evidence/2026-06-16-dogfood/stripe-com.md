# 2026-06-16 dogfood — stripe-com

**Mode:** tricky (no prior visual.md — not in the regression set)
**Pages tiled:** homepage, payments, pricing, connect, enterprise (71 tiles)
**Tier-B fired:** homepage (`--dismiss` y), enterprise (`--dismiss` y) · connect / pricing / payments kept Tier-A
**WARNINGs fired:** none (no `scroll_locked`, no missing-overview on either run; stderr empty both times)
**Manifest verdict:** homepage + enterprise → `dismissed=true`, `scroll_locked=false`, `overview=overview-480w.png`, `source=shoot`
**Result:** `qa_status: recapture-used` · 37 cards (24 strong / 9 mixed / 4 poor) · lint exit 0

## What happened
Every page's hero tile carried the same **site-wide Intercom sales-chat overlay** — the expanded "N sales reps available… Chat now" proactive bubble on homepage/connect/enterprise/pricing, a collapsed launcher on payments. Re-rendered the two pages where the bubble covered real evidence (homepage: "Flexible solutions" intro + a product card; enterprise: the customer-logos band). On both, `--dismiss` cleared the proactive message via its own close control and collapsed it to the persistent "Chat with Stripe sales" launcher — no WARNINGs, both manifests cleanly labeled. The three remaining pages stayed Tier-A: the chat widget there sits over gradient/empty corner (low-harm faithful capture-fact), so re-rendering would have manufactured Tier-B for nothing. All gradients/photos otherwise rendered; the 4 `poor` cards spot-checked as genuine design (dense footer, untreated Squire photo), not artifacts.

## Surprising
- **First live confirmation of the Intercom edge the approach doc flagged (open call #2).** The doc dropped the chat-specific hide and bet the generic ×/close-affordance match would catch dismissable proactive bubbles while the persistent launcher stays as a faithful capture-fact. Dogfood confirms it exactly: `--dismiss` collapsed the proactive bubble, launcher remained. The probe's 8 sites were cookie banners / modals / a splash — **none was a chat widget**, so this was unmeasured until now.
- **`--dismiss → clean` isn't binary on a persistent launcher.** `shoot.py` screenshots each viewport live, so a `position:fixed` launcher repeats in the bottom-right of **every** Tier-B tile — vs Tier-A `tile.py`, which crops one full-page PNG and shows a fixed element only once (tile-00). So `--dismiss` removes the content-covering proactive layer but the residual launcher becomes *ubiquitous* across the Tier-B set. Miners correctly treated it as a caveat (no card cites it), so no harm here — but it's a real difference from the probe, which only looked at the first viewport.
- **QA can miss WebGL-incompleteness when the broken state looks intentional.** Enterprise's cached hero rendered its animated amber-gold→violet gradient **flat-dark**; I read that as a deliberate dark hero and classed the page overlay-only. The `--dismiss` render revealed it was actually the *combined* WebGL+overlay case (approach doc #2's dual-render trigger). The render restored the gradient and directly enriched 3 cards (`color_02 / color_04 / typography_05`). Takeaway: the dual-render trigger leans on QA spotting WebGL-incompleteness — the exact case that hides as plausible design. I shipped a single `--dismiss` render as the active tiles (most faithful clean view) with the cached `.payloads` kept as the as-captured baseline, rather than a sibling dual-render.

## For regression only: vs the prior visual.md
N/A — tricky mode, no prior `visual.md` to diff.

## Open follow-ups → BACKLOG.md
- Tier-B persistent-fixed-element repetition: a chat launcher / fixed bar repeats in every `shoot.py` tile (it's clean per-viewport, dirty in aggregate). `--dismiss` clears the dismissable proactive layer but not a persistent launcher. Worth a note on whether Tier-B should flag residual fixed-element coverage — not a patch (held per instructions).
