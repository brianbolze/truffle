# Developer Review

Question: **What Truffle system behavior does this run pressure?**

**Overall:** Well-executed, correctly disciplined, builds nothing. Two proposed triage nuggets — one earns a submit-candidate (MRL-001 selection-bias flavor), one is downgraded to watch (MRL-002 orthogonal axis). Reviewed via a 3-pass adversarial shape (evidence verifier + consumer + developer, Sonnet).

## Capability pressure

| Capability | What fired | Smallest useful response |
|---|---|---|
| **Query / access** | Two-enum cross-tab (`audience` × `anchor_category`) fell out of one parse pass; `query-time-grouping-enough` confirmed for a *second* clean enum serving as the primary axis. | **Watch** — Evidence Log on MRL-002; no recipe addition until a second two-enum/audience-axis sighting. |
| **Synthesis / guardrails** | Whitespace/asymmetry reads are **doubly bounded** — selection-bias in corpus construction AND anchored-only grep-exclusion — and fixing one bound does not fix the other. | **Submit** — name the compound-caveat in MRL-001; flag as a first-class rule for any future QUERYING whitespace recipe, not a footnote. |
| **Structure** | `audience` confirmed as a durable frontmatter enum usable as a primary query axis without any persisted cohort object; State/Judgment boundary held. | No change. |

## Lenses

**Steward** — State (the cross-tab, verbatim frontmatter) vs Judgment ("male-coded vertical," whitespace hypothesis) kept rigorously separated and labeled. Absence language correct throughout ("not captured," not "not there"); coverage limits stated early and loudly. The verifier reproduced every count with zero discrepancies. Cosmetic catch (fixed): a blank duplicate Loop-1-exit-check block was left in `run-notes.md` from the template — removed.

**Dev Agent** — No toil removed, none created; the clean-enum cross-tab is a one-liner, no helper warranted. The one recipe-level artifact that pays forward is the **compound-caveat**: if a QUERYING recipe for whitespace reads ever graduates, *both* bounds must be in the template.

**Founder** — Compounds the warm/cited asset cheaply (store-only, zero spend) and produces a *testable hypothesis* rather than a finding, with the bounded-live corroboration path clearly named. No ontology added.

## Adversarial assessment of the two nuggets

**Nugget #1 (MRL-002, orthogonal axis) — downgrade to WATCH.** Real but thin. Every prior State-read organized *by* `anchor_category`; this is the first where the group-by and the secondary dimension are two different enums. Genuine generalization signal (the MRL-002 family is "clean-enum-primary-axis reads," not "category-reads only") — but one sighting of a two-enum cross-tab does not earn a sub-recipe. Log it; do **not** brand it a "7th surface" milestone (a count that rots). Call it: first time an orthogonal enum served as the primary axis. Hold for a 2nd sighting.

**Nugget #2 (MRL-001, selection-bias denominator) — SUBMIT-CANDIDATE.** The stronger nugget; the distinction holds under pressure:
- *Anchored-only under-count* (runs 008–017): a brand *in the store* falls out of a per-category grep because it's `multi/none`. Bias enters at **query time**; fix = wider grep / tier annotation.
- *Selection-bias denominator* (run 020): the captured cohort was seeded men's-hormone-heavy (runs 001/008/014/016), so the 15-vs-5 asymmetry is bounded *before any grep runs*. Bias enters at **corpus-construction time**; no query-time fix touches it — needs a different capture campaign or an external denominator.

A reader could correctly apply the anchored-only fix (widen to multi/none) and *still* get a misleading men/women ratio. So a QUERYING recipe for this read shape must carry **both** caveats — that is a synthesis/guardrails need, not a restatement of the coverage-caveat.

## Recommendation

- **No-op / keep as observation:** the State/Judgment boundary win and the `audience`-as-clean-enum confirmation.
- **Watch for recurrence:** MRL-002 orthogonal-axis flavor (hold for a 2nd audience-axis or two-enum cross-tab read).
- **Submit triage candidate:** MRL-001 Evidence Log — the selection-bias denominator flavor + the compound-caveat (both bounds must travel together in any future whitespace QUERYING recipe).

## Triage submissions

1. **MRL-001 (Evidence Log) — submit.** Name the selection-bias denominator flavor and distinguish it from the anchored-only under-count (corpus-construction-time vs query-time bias); record the compound-caveat implication.
2. **MRL-002 (Evidence Log) — submit as a *watch* note.** First orthogonal-enum primary axis; clean two-enum cross-tab with no new toil; not a surface-count milestone; hold for a 2nd sighting before any recipe addition.

No graduation. No `store/` mutation. No `Human Notes` touched.
