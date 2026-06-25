# Receipt C4 — prose change-notes (the only change channel)

- **Source:** local; grep over `store/*/profile.md`.
- **Source type / grade:** local / primary. **Spend:** none. **Snippet-only:** no.
- **Claims supported:** C4 (~7/145 profiles carry an explicit prior-capture reference).

## Method
grep -liE 'prior capture|previous capture|resolves the prior|changed since' store/*/profile.md

## Result — 7 profiles
bullish-co, clari-com, getpetermd-com, marekhealth-com, noom-com, nike-com, onemedical-com,
ouraring-com, ro-co, telolife-com (broader pattern grep returns ~10; the strict
change-phrase grep returns 7). Example: onemedical `unverified_fields` —
"On-Demand Care ... Resolves the prior capture's unknown pay-per-visit fee."

This is an ad-hoc, unstructured, prose-only channel — not a queryable change-pulse.
