# Retro — capture facts vs. model memory (2026-05-31)

From the `/research-company etsy` run. When Brian questioned a stale-looking claim, I over-corrected and scrubbed *every* non-verbatim fact from the profile in the name of "never use priors." That's too blunt. This is where the line actually sits.

## What happened

The profile had three kinds of "memory," and I wrongly lumped them together:

- **The real error:** "the `/about` figures are an *older, Etsy.com-only* snapshot." The page is undated and says no such thing — I invented a *reason* two captured numbers disagreed, with an "older" guess from training data. This deserved cutting.
- **Over-scrubbed #1:** captured "publicly traded" → "NASDAQ: ETSY." A stable, one-search-away fact anchored to the page. Safe — I just hadn't *labelled* it as priors.
- **Over-scrubbed #2:** captured brand name "Reverb" → `reverb.com`. A lookup, not a claim. Safe.

## The line

It isn't capture-vs-memory. A memory-derived fact is probably safe to land if it's:

1. **Stable** — won't change between captures (ticker, HQ city, founding year, an owned brand's domain). *Not* prices, counts, headcount, dates, "current X."
2. **Anchored** — tied to something actually captured, not floating in from priors.
3. **Marked** — a reader can tell it came from model knowledge, not the page.

| Verdict | Examples |
|---|---|
| **Land it, page-cited** | captured facts + synthesis across pages (already the job) |
| **Land it, *marked* as priors** | stable + anchored: `ETSY` ticker, `Reverb`→`reverb.com` |
| **Never** | volatile facts from memory, or a causal/temporal claim asserted as observation |

The bright line is between the last two rows — not between "page" and "memory." This fits what we already believe: reasoning is free, and we already want provenance on every fact. So the fix is a *label*, not a ban.

## Recommendations (proposals, not applied)

1. **Soften the SCHEMA rule** from "never infer from prior knowledge" → "captured, synthesized, or *stable-anchored-and-marked*; volatile and causal claims are capture-only."
2. **Add an enrichment marker** — a Provenance line like `Enriched (model knowledge): ETSY ticker; Reverb→reverb.com`. Distinct from `unverified_fields`, which means "couldn't get it," not "got it from priors." (Dumping the ticker into `unverified_fields`, as I did, loses that difference.)
3. **Keep the OpenAI-retro's "grep-it-or-unverified" — just scope it to volatile facts** (prices, counts, dates). That's what catches fabricated pricing; it shouldn't block a stable ticker. Split that way, the two retros agree.

Open question for later: whether enrichment needs an explicit confidence floor ("would one search confirm it?"). Not worth deciding until it bites.
</content>
