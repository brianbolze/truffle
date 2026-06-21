# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable? Yes** — for the "trust the cache over time" reader, this is the first read that
  says plainly *what you can and cannot know about staleness from the store alone*, with the
  exact query to risk-rank what to re-check.
- **Why:** The headline is decision-useful and non-obvious: staleness-*risk* is rankable today
  (cross `captured_at` age × the point-in-time token → 34 high-risk profiles), but actual
  *drift* is unobservable store-only. A delegating reader now knows to re-verify the 34
  promo-priced telehealth profiles before quoting their prices, and to *not* waste a re-capture
  on the old-but-stable watch/SaaS brands.
- **Where Truffle added value:** It turned a vague worry ("is the cache stale?") into a concrete,
  reproducible filter, and corrected the naive instinct (rank by age) that would have flagged the
  wrong companies. The age≠staleness demonstration (stable Casio at 20d vs volatile GLP-1 at 16d)
  is exactly the calibration a fast reader needs.
- **Where it added little / fell short:** It cannot tell the reader whether any specific fact has
  *actually* moved — only how old + how volatile-by-nature it is. For "did Ro change its GLP-1
  price last week?" the read correctly says: store can't answer, that needs a re-capture. So the
  most valuable version of "trust the cache" (change detection) is out of reach store-only.
- **What the consumer can do now:** Run the documented cross to get a re-check worklist; trust
  the 96 non-high-risk profiles' market facts more; treat the 34 high-risk ones as quote-at-your-
  own-risk until re-captured.
- **Safer than generic Claude + web search?** Yes on provenance — every profile carries a dated
  capture clock and a contracted volatility flag, so the staleness read is grounded, not guessed.
  Generic web search has no notion of "when was this last verified and is it the kind of thing
  that flickers."
- **Biggest limit:** No drift surface (G1). The read is honest about it, but it caps the value job
  at *risk-ranking*, not *change-detection*.
- **Human follow-up needed:** Decide whether the staleness-risk cross deserves a documented query
  recipe (W1) and whether the `captured_at` format lint (G3) is worth a one-liner. Both are human-
  gated; neither is urgent.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer + next step | Strong: a reproducible 34-profile re-check worklist, not a summary. |
| **Judgment-ready** | Cited ingredients | Strong: every count traces to dated frontmatter + the SCHEMA-112 token; verifier re-derived C1/C2/C3/C5 clean. |
| **Sourced & cited** | Uncertainty visible | Strong: G1/G2/G3 name exactly what the read can't prove; "unobservable store-only" not "no drift." |
| **Deep enough** | Whole set | Strong: all 130 profiled cos, cross-vertical, not sampled. |
| **Fresh enough** | Stale assumptions visible | This *is* the freshness read; capture dates surfaced per-profile. |
| **Kept / reusable** | Warm files | Receipt + the cross-query are reusable; next freshness ask is cheaper. |
| **Shortfall mapped** | Names the gap | Strong: drift (G1), token-coverage (unmeasured), format hazard (G3) all named. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Yes — an agent can now avoid quoting stale promo prices by checking the high-risk filter first. | Drift detection would make it airtight; not store-only. |
| **Trust the cache over time** | Partly — risk is rankable; change is not detectable. | Re-capture + diff cadence (MRL-012). |
| **Build on top without re-capturing** | Yes — downstream systems get a dated, volatility-flagged State they can risk-weight. | A documented recipe would lower the build cost (W1). |

## Lens check

- **Strategist:** Lands fast — "rank by volatility×age, not age; 34 to re-check; store can't see drift."
  The age≠staleness inversion is the novel, hard-to-get-elsewhere insight.
- **The Pantry / downstream system:** Usable as ingredients — `captured_at` + the greppable token are
  stable, dated inputs a downstream monitor could risk-weight without re-browsing. The one caveat it
  must respect: the token is *volatility*, not *drift* (clearly labeled as a Truffle-side judgment).
- **First Contact:** Trustworthy — the run reproduced its own contracted failure mode twice and caught
  both (V1); a new reader sees the self-correction in the open, which builds rather than erodes trust.

## Optional triage evidence

No new consumer-side triage item. The value ceiling (risk-rankable, drift-blind) is evidence for the
existing **MRL-012** (re-capture cadence), appended via the developer review. No-op here.
