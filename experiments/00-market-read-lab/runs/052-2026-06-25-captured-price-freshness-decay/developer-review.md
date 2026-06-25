# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Promo-window text (end dates, sale labels) is already captured verbatim in `offerings.md` prose and `site_notes` for every panel brand that had a dated promo. The capture did its job; the structural gap is downstream of it. | G1: "ends June 15, 2026" / "through June 26th" / "4th July Sale" all present in existing captures. | G1 · gap |
| **Structure** | No structured promo-expiry field; the single datum that predicted decay (the printed end date) is prose-only and unqueryable. But it was also already captured in prose every time — so the fillable-cut bar is the deciding question (see Lenses). | G1: promo end date in `site_notes` prose, never in frontmatter or a price cell. | G1 · gap |
| **Query / access** | "Which captured prices sit on a lapsed promo window" is unanswerable from structured fields but answerable by grepping `offerings.md` / `site_notes` for date-looking strings in a promo context. A recipe, not a field. | G1: the exact query that would flag Peloton's $695 without a live fetch requires prose-grep. | G1 · gap |
| **Freshness / automation** | A "live re-check" via `firecrawl_scrape` silently returned a cached 06-24 scrape for Eight Sleep instead of a true 06-25 fetch. For any future freshness-verification build, cache-busting (`maxAge:0`) is load-bearing, not optional. | G2: Eight Sleep `cacheState: hit`, `cachedAt: 2026-06-24T02:05Z` — same day as the original store capture. | G2 · gap |
| **Synthesis** | The store held everything needed to predict the Peloton rot without any live fetch (struck regular price + verbatim expiry both present in the 06-10 capture). A freshness read could start with a prose-grep for lapsed promo windows before spending a credit. | S2: the 06-10 capture recorded "$1,145" struck-through and "ends June 15, 2026" verbatim. | S2 · surprise |
| **Guardrails** | Bounded-live discipline held cleanly: 1 source family, 3 credits of 8, 3 outside sources of 5, stop rule fired at 3, no funnel/PDF/JSON-extraction. The run-040 (PDF) / run-047 (JSON-extraction) breach class was successfully avoided by explicitly naming the class in `fail_closed_when`. | run-notes live_evidence_plan actuals + Loop-1 exit check: all pass. | — |

## Lenses

**Steward** — Honest throughout. Cache state was surfaced and labeled (not suppressed as a clean "match"); Eight Sleep's cell is explicitly marked with the cache caveat in both `receipts/C1` and `read.md`. The finding that the store can predict rot from its own prose without a live re-check is correctly framed as an S2 surprise, not over-stated as a general rule (n=1). Capture dates and source grades are present on every evidence row. Absence language is precise: Therabody/Hyperice are "not re-checked," not "unchanged."

**Dev Agent** — Two concrete, low-cost signals come out of this run:

1. **Prose-grep recipe before any live spend.** A pass over `offerings.md` / `site_notes` for "ends [date]", "through [date]", or "limited-time" strings would surface lapsed promo windows without any paid fetch. It's the cheapest possible freshness check for the promo-bound decay class, and this run proves the data is there to grep.

2. **`maxAge: 0` when the point is to verify current state.** This is a tool-call discipline item, not a schema or recipe. Any future freshness-check routine that uses `firecrawl_scrape` without explicit cache-busting can silently re-confirm stale data. The fix is one argument, grep-verifiable in the plan.

Neither needs a new field or primitive.

**Founder** — The "no new primitive needed" landing is sound. The case for a structured `promo_expiry_date` field fails the fillable-cut bar on two grounds: (a) n=1 diverging price is thin, and (b) a promo-expiry date is a rotting datum by design — it describes an event that, once past, has no continued use to a reader. The warm/cheap/reusable asset already exists (the verbatim expiry in prose); the lightest next step is a reading convention or a grep recipe, not a schema extension. The cache-busting finding (G2) is genuine tooling signal for any future freshness build and cheap to act on.

One ontology-gravity risk to flag: G1 could read as "promo-expiry is a missing field" on first encounter. The counter-argument — prose carried the expiry every time, a field would rot by design, and the run is n=1 — is made clearly in `read.md`, but a future run that finds promo-window text *absent* from a capture would shift the disposition. Hold the landing; watch for that second case.

## Recommendation

- **No-op / keep as observation:** G1 (promo-expiry prose-only). The "no new primitive" landing is correct; hold for a second instance where prose fails to carry the expiry.
- **Watch for recurrence:** G2 (`freshness-monitoring`, `tooling-ergonomics`). Cache-busting is a one-argument fix; any future bounded-live freshness probe should name it explicitly in `fail_closed_when`. Watch for the first re-check run that forgets it.
- **Severe `risk-miss` to surface now:** None. The run correctly identified and disclosed the Eight Sleep cache-hit caveat before asserting the price matched.

## Raw learning to preserve

Already logged in `run-notes.md` Observations (G1, S1, S2, G2, S3). No additional rows needed from the developer lens beyond what is reported to the loop in the final section.
