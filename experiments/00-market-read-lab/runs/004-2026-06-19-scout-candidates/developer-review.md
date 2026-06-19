# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Do not default to "capture more data." Ask whether the run exposed a reusable system need: capture, structure, query, freshness, automation, access, or guardrails.

Market reads may make judgments. When they do, ask whether the read clearly crossed from State or Signals into Judgment, and whether Truffle should support that boundary or leave the judgment downstream.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Query / access** | **Third sighting** of the same wall: the answer needed a grouping the store doesn't hold (no per-SKU category), so the breadth count was hand-built in-run from molecule strings. Distinct shape from Run 000 (entity-set union) and Run 001 (relation-edge grep). | Append to MRL-002 as a third-sighting recipe candidate — a documented QUERYING "group the cohort by category at query time" recipe (inputs, roster-cell molecule match, the whole-file-grep anti-pattern, captured-floor language). Pattern-level, human-gated. |
| **Structure** | The tempting fix — a normalized per-SKU category field/taxonomy — is the wrong one. That is exactly the ontology gravity / datapoint-reconciliation weight the anti-Doro line refuses. | Keep category grouping as a *query-time recipe*, NOT a stored per-SKU taxonomy. The front-door `anchor_category` (one-per-brand) is the right grain of stored state; finer is downstream's job. |
| **Guardrails** | The whole-file-grep trap is the sharpest evidence yet of a known failure: full-body grep returned TRT 53/53 and labs 53/53 (prose/FAQ/negation), confidently wrong. The run caught and discarded it. | No new guardrail — reinforce existing QUERYING guidance "match molecules inside the roster cell, never the file body." The recipe (above) should carry this anti-pattern with these concrete numbers. |
| **Synthesis** | Read labeled every State→Judgment crossing inline (`[State]` / `[Judgment]`) and kept "thin = few captured brands" distinct from "thin market." This is the boundary working as intended. | No-op. This is the labeling discipline the developer review is supposed to check for — it held. |

## Lenses

**Steward** — System stayed honest. Provenance (receipt `derived`, claim map, capture
clocks), uncertainty (mid-band ranks flagged soft; GLP-1 lead + mental-health floor
flagged robust), and the State/Signals/Judgment split were all visible. The one structural
honesty point: the breadth cut is presented as a count but is *derived, not stored* — the
read says so explicitly, so it's honest, but it means the cohort cannot be re-queried on
category without re-deriving.

**Dev Agent** — Repeated toil is real and now thrice-seen, but the response is a
**convention/recipe, not a helper or a field**. A committed molecule→category map or a
per-SKU tag would be premature infrastructure (and would need maintaining as molecules
change). The grep-verifiable contract here is "roster-cell match + named anti-pattern in
QUERYING," which removes the toil without standing infrastructure.

**Founder** — Compounds the warm asset (the receipt's regexes + anti-pattern are directly
reusable) while staying light. The discipline to *not* graduate a category object on the
third sighting is the right founder instinct: recurrence earns a documented recipe, not an
ontology.

## Recommendation

- **No-op / keep as observation:** Synthesis labeling (held), the whole-file-grep guardrail
  (reinforces existing guidance, no new gate), source rigor.
- **Watch for recurrence:** A *fourth* category-grouping wall would be the signal to
  actually graduate the QUERYING recipe (MRL-002). Still a human call.
- **Submit triage candidate:** Append a dated third-sighting Evidence Log entry to
  **MRL-002**. No new item, no priority change, no graduation.

## Triage submissions

**Append to MRL-002 Evidence Log (third sighting):** Run 004 hit the same query-machinery
wall in a new shape — a missing per-SKU category dimension forcing query-time molecule
classification over roster cells. Recurrence now crosses three distinct query shapes
(union / relation-grep / category-grouping), strengthening the case for a *documented
QUERYING recipe layer* over per-query helpers — and explicitly **against** a stored per-SKU
category taxonomy (anti-Doro). The run also produced the cleanest evidence of the
whole-file-grep anti-pattern (TRT/labs 53/53), which the recipe should carry.

MRL-001 (denominator reconciliation) is *touched* but not strengthened: the DTC gating by
`value_chain_role` was a clean 1:1 join this run, not the hard part. Logging the sighting
on MRL-002 only, to avoid double-counting one run as two sightings.

**Do not graduate, spike, or implement system changes.**
