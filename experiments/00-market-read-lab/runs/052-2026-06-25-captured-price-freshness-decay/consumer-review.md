# Consumer Review

Question: **Where did Truffle create reader value, and where did it fall short?**

## Verdict

- **Valuable?** Partly — strongly on the builder side, not at all for the end buyer.
- **Why:** The run's payload is a clean empirical result about *when* captured pricing State rots (on a promo's printed expiry, not on a clock), and the discovery that the capture already holds the predictive datum. A builder/Steward learns the store needs a promo-expiry reading convention, not a new schema field. A buyer wanting a current price gets nothing useful — the run explicitly didn't update any store data and the one diverging price was already stale before the run started.
- **Where Truffle added value:** The store held exactly the right evidence to pre-diagnose the decay without a live fetch — captured expiry text ("ends June 15, 2026"), struck-through regular price ($1,145), and capture date (06-10) together predicted the $695 promo had already lapsed. That's a positive result: the capture was honest and self-sufficient for identifying its own risk. (S2, C3/C4)
- **Where Truffle added little or fell short:** The promo-expiry datum lives in prose, not a queryable field, so a staleness monitor can't ask "which captured prices are sitting on an expired promo window" without reading every offerings file. (G1) The Eight Sleep "live" verification was silently a cached re-scrape of the capture-day data, making the "unchanged" cell trivially same-day — not a genuine independent check. (G2)
- **What the consumer can do now:** The builder/Steward can act on the reading convention: grep `offerings.md` prose for dated promo-window text store-wide and flag prices where the printed end date has passed — zero live spend needed, the information is already captured. (read.md Market Pattern / What Would Change)
- **What made it safer / better than generic Claude + web search:** The capture had already recorded the expiry date and the post-promo regular price verbatim. So the rot was predictable from the store alone — generic web search in June 2025 would have fetched the live $1,145 but wouldn't know the $695 was ever captured, so it couldn't measure the divergence. Truffle's dated snapshot made the gap visible.
- **Biggest limit:** The panel was too freshly captured (4/5 brands at 1 day old) to show organic non-promo drift, so the run answers a freshness *floor* question, not a decay curve. n=1 diverging price is a clean instance, not a proven rate. Eight Sleep's "live" cell is not independently verified. (run-notes Evidence limits)
- **Human follow-up needed:** None for the finding. If the promo-expiry reading convention is worth persisting, it belongs in QUERYING.md — but that's a builder lane call, not a buyer deliverable.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer, decision aid, or next step. | Yes for the builder: "captured pricing rots on the promo's own end date, not the clock; the datum to predict it is already in the store." Not useful for a buyer wanting current prices. |
| **Judgment-ready** | Fresh, cited ingredients a human or downstream system could reason from. | The Peloton case (C3/C4) is fully cited, dated, and clean. Oura (C1) is fresh-verified. Eight Sleep (C2) is a cache caveat — not judgment-ready as an independent check. |
| **Sourced & cited** | Claims trace to dated captures, receipts; uncertainty visible. | Receipt C1, three live vendor pages, capture dates per source, cache-state metadata recorded. The Eight Sleep cache-hit is surfaced honestly, not buried. (G2) |
| **Deep enough** | Covers the intended set. | 3/5 panel brands live-checked (stop rule at 3); Therabody and Hyperice unverified. Coverage limit named, not claimed as finding. |
| **Fresh enough** | Capture dates and stale assumptions visible. | Yes — capture age is the explicit independent variable. The one stale price (Peloton $695) is named as stale in Missing/Stale. |
| **Kept / reusable** | Leaves behind warm files, state, or receipts. | Receipt `C1-live-price-recheck.md` persists. No store mutation (by contract). The reading convention is surfaced but not yet persisted. |
| **Shortfall mapped** | Names structural frontiers. | G1 (unstructured promo-expiry datum) and G2 (Firecrawl cache-hit silently defeats a freshness check) are both named cleanly and bounded. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Make AI safe to delegate to** | Indirectly — it established that delegating a "what's the current price" query against the store is safe for evergreen prices but unsafe for dated promos without a staleness check. Not actionable yet. | A reading/delegation convention that flags promo-windowed prices before returning them. |
| **Trust the cache over time** | Yes — this is the job the run was selected to serve, and it answers it: trust the cache for evergreen prices; for promo prices, trust it only within the promo's own printed window, which the capture usually records. (S1, S2) | The promo-expiry grep recipe in QUERYING.md would make this actionable without live spend. |
| **Build on top without re-capturing** | Partly — the evergreen-price finding is positive. The promo case requires either a reading convention or live re-check to be trustworthy downstream. | Persisting the reading convention would close this. |

## Lens check

**Strategist:** The run's headline is clean and quotable: "captured pricing rots on a promo's printed expiry, not on the clock — and the expiry is already in the store." A strategist can use that to calibrate how much to trust the store's pricing State without re-fetching. The Peloton $695→$1,145 example is concrete. What the strategist can't get here: a current price for any brand.

**Pantry / downstream system:** The Oura and Peloton evergreen prices (C1 partial, C4) are stable ingredients a downstream system can use. The promo-windowed prices (Peloton $695, Oura flash sale, Eight Sleep 4th July) require a promo-window staleness check before relaying — the check is feasible from existing prose but not yet encoded. A Pantry consumer using the Peloton offerings.md today would silently relay the stale $695 if they read only the headline. (read.md Missing/Stale)

**First Contact:** The run is well-evidenced and honest about its limits — the cache caveat for Eight Sleep, the stop rule at 3, the "floor test not a decay curve" framing. A first-contact reader can trust the documented claims and calibrate the ones labeled as limits.

## CR1 frontier note

This run lands squarely on the recurring "value lands on builder not buyer" frontier (038/039/041/047/048/049/050 CR1). The consumer here is the Steward who learns the store needs a freshness reading convention — not the buyer wanting a current price. The distinction from prior CR1 instances: this run *closes* the gap for a specific, actionable scope (promo-expiry text in existing prose, zero live spend), rather than just naming a structural absence. That makes the builder-value more concrete than usual, but it is still builder-facing.
