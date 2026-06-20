# Developer Review

Question: **What Truffle system behavior does this run pressure?**

The "no new primitive needed" verdict holds under stress-testing. The run's real contribution is naming **three separable gaps** the existing schema doesn't distinguish — and the adversarial evidence pass (which caught the page-grain Wayback omission) is itself a finding about enumeration grain.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | **Subject-identity is not pinned at capture time.** SERP "pairs" are unpaired not because a second capture wasn't taken, but because it was a *different query* under the same `domain/serpapi/` dir. "Same domain + same source_type" ≠ a diffable pair. This is a capture-*contract* gap, not a cadence gap. | When re-capture targeting matters, pin a canonical subject (query string for SERP, issuer for SEC) so a delta has a guaranteed pair. No new entity. |
| **Structure** | A **capture-cadence denominator** is structurally distinct from a market-membership denominator (MRL-001): "which subjects were re-captured with a real gap *and stable identity*," not "which brands are in a category." Different validity checks, different failure language. | Name it as a first-class denominator note in any future QUERYING signals-read recipe — including the subject-identity requirement, not just cadence thinness. |
| **Query / access** | Enumerating "what's diffable" is **grain-dependent and easy to get wrong** — a company-grain glob silently dropped all page-grain Wayback subjects (the Loop-1 miss). | Any `signal_delta` enumeration helper must walk to the envelope (`find … -name '*.json'`), never assume `<domain>/signals/<type>/*.json`. |
| **Freshness / automation** | Change-pulse readiness is **bounded by cadence matched to each signal's refresh rate**, not schema. Trustpilot counts move daily (weekly gap fine); Wayback re-crawls ~monthly (weekly re-capture → 13/15 delta=0); SEC pairs intra-day. | A light, per-source-tuned re-capture cadence for a small fixed subject set — ops, not a monitor service. |
| **Synthesis** | The read stayed cleanly in Signals and refused Judgment: no brand ranked by velocity, `paid_profile` labeled as solicitation cadence, the onemedical −1 labeled as API artifact. The "Market Pattern" section names the 10× spread then parks it. | None — this is the model for a change-pulse read template. |
| **Guardrails** | `signal_delta.py`'s veto-not-skip discipline made "what can't we diff" cheap and honest (SEC veto, eden subject-realignment, hydramed empty-between). The one buildable tool gap: no `sec_edgar` delta branch. | Add the `sec_edgar` branch (~one function); keep everything else fail-closed. |

## Lenses

**Steward** — System stayed honest. Provenance/freshness/grain are visible; State/Signals/Judgment separation held; the adversarial pass caught the one real integrity miss (Wayback omission) and it was folded in with the correction logged. The two confound flavors (paid_profile velocity; CDX −1 nondeterminism) are labeled, not laundered.

**Dev Agent** — No over-building: no monitor, no stored diff object, no persistent artifact. The two repeated toils worth a convention (grain-aware enumeration; per-source cadence) are flagged, not escalated. Prefer the grep-verifiable contract (subject-identity field) over a new edge/object.

**Founder** — Conservatively correct, but **don't over-soften the cheap fixes**. Bundling "no re-capture cadence" (an ops/scheduling decision) with "no `sec_edgar` branch" (a ~30-min code change) as one human-gated item adds friction. If SEC funding-pulse matters to a consumer like Scott Witt, the branch is near-zero cost — sequence it independently.

## Recommendation

- **Submit triage candidate** (the new freshness/cadence item is genuine first evidence — no prior run touched the change-pulse axis).
- Watch for recurrence on subject-identity: a second temporal read hitting the SERP/SEC unpaired wall would harden "pin subject-identity at capture" from a one-run observation into a capture-contract recommendation.

## Triage submissions

Submitted to `triage.md` as a new item + two Evidence Logs (framing per the corrections below). Human-gated; nothing implemented.

1. **New P2 item — change-pulse readiness = cadence + tooling, not a primitive** — but labeled as **two separable gaps**: (a) per-source re-capture cadence (ops) and (b) `sec_edgar` delta branch (~30-min code), so the steward can sequence them independently.
2. **Evidence Log → MRL-008** — lead with the *new fact* (only `review_count` diffs; decision-grade Trustpilot surfaces aren't temporal-tracked; Wayback's onemedical −1 is a second confound flavor), not "the convention must travel to the change axis" (which reads as restatement).
3. **Evidence Log → MRL-001** — name the **subject-identity** problem explicitly: "same domain + same source_type" is insufficient for a temporal pair; SERP/SEC need a pinned canonical subject. Not just "the temporal denominator is thinner."

**Do not graduate, spike, or implement system changes.**
