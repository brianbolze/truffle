# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Partly — strongly for the builder/Steward, marginally for an end buyer.**
- **Why:** This is a gap-probe on the store's most-loaded classification token, and it lands its builder payload cleanly: it proves `Services / Consulting`-as-primary is a residual catch-all (≥6 non-comparable jobs across ~56% of the store), and — sharpened by the evidence verifier (VR1) — shows the offering_category pair + entity_type peel the telehealth mass off the residual but cannot discriminate *within* the 9-firm professional-services tail. The actionable ingredient (the 52/9 Biotech-secondary split, 100% clean in-sample) is real and usable today.
- **Where Truffle added value:** A correct, falsifiable diagnosis of a reader hazard affecting 82/145 profiles, plus a strong positive ingredient (the clean telehealth-vs-professional pair-key) a Pantry consumer can use to build a telehealth roster or strip non-telehealth firms now.
- **Where Truffle added little or fell short:** No end-buyer deliverable. A Strategist asking "show me all services companies" or "find me a brand agency" still trips on the over-merge — the run surfaces the hazard but the recipe to avoid it (read the pair, not the lead token) is not persisted in QUERYING.md. The within-residual ambiguity (IDEO vs onemedical vs Red Antler share a pair) means even the corrected recipe doesn't fully separate the tail.
- **What the consumer can do now:** Build a clean telehealth cohort (Services-primary + Biotech-secondary = 52) or a clean "non-telehealth professional services" set (Services-primary, no Biotech = 9) — but must then read prose to sub-sort the 9.
- **What made it safer / better than generic Claude + web search:** Grounded entirely in 145 cited local profiles with a reproducible denominator receipt; a web search could not have audited the store's own classification grain at all.
- **Biggest limit:** Latent value — the fix is named (one-line reading convention) but explicitly deferred; the consumer still needs the recipe the run discovered.
- **Human follow-up needed:** A Steward call on whether to persist the pair-reading convention in QUERYING.md/TAXONOMIES.md, ideally after the DR4 audit (does an existing recipe already over-merge?).

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Decision aid, not just summary. | Yes for the builder: a precise hazard map + a usable pair-key. Partial for a buyer (recipe not persisted). |
| **Judgment-ready** | Cited ingredients to reason from. | Strong — 52/9 split is cited, reproducible (receipt C1), and corrected for scope (VR1). |
| **Sourced & cited** | Traces to dated captures/receipts. | Yes — receipt C1 with method; per-profile `captured_at`; Overview prose cited for all 9. |
| **Deep enough** | Covers the intended set. | Yes — all 61 primaries + ~21 secondary holders; not just examples. |
| **Fresh enough** | Freshness visible where it matters. | N/A — schema-grain read, no current claims; capture clocks noted. |
| **Kept / reusable** | Warm files for the next ask. | Yes — receipt C1 + the pair-key recipe are reusable. |
| **Shortfall mapped** | Names where Truffle couldn't support. | Yes — the within-residual gap (VR1), the denominator method-sensitivity, and the deferred-fix gap are all named. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Build on top without re-capturing** | Strong — the pair-key gives a downstream system a clean telehealth/non-telehealth filter from existing State. | Persist the recipe so the system doesn't have to re-derive it. |
| **Compare a whole field** | Partial — clean for "telehealth vs professional"; fails within the 9-firm residual. | Prose/cohort tag needed to sub-sort the residual. |
| **Five-second brief input** | Weak — a buyer gets no new company fact; the value is a map, not an ingredient. | This is the recurring map-not-ingredient frontier (see CR rows). |

## Lens check

- **Strategist:** lands plainly and is novel (the dominant token is residual is a non-obvious, hard-to-get-elsewhere insight) — but it's an insight *about the store*, not about a market.
- **The Pantry / downstream system:** the 52/9 pair-key is genuinely high-quality ingredient — stable, cited, trivially queryable once known. The gap is recipe persistence, not data quality.
- **First Contact:** would trust it — the run shows its work, reconciles its denominator, and visibly corrected its own overreach (VR1).

## Raw learning to preserve

Appended to `learning/observations.md`: CR1 (value lands on builder/Steward — map-not-ingredient, now 8+ runs but first *inward fold* onto the dominant existing token), CR2 (the 52/9 pair-key is a strong, buy-ready ingredient — gap is persistence not quality). Evidence-verifier VR1 (the "clean discriminator" overreach, corrected in read.md) is logged from the run Observations.

**Did not propose lessons, graduate anything, or implement system changes.**
