# Lead Decision: `/discover-neighbors` verb

Date: 2026-06-24
Decision: **Accept with revision** — approved by Brian.
Packet: `proposal.md` (accepted) · `proposal-review.md` (independent, proposal-mode).

## Decision

Accept the proposal to add a thin `skills/discover-neighbors/` verb. Independent proposal-mode review found the load-bearing claims honest and the verb-over-recipe call sound on category grounds (an outward-reaching, *spending* expansion verb does not belong in the read-only `QUERYING` surface). The review recommended accept-with-one-revision; Brian approved that lean.

## Required revision (must hold at the change-mode gate)

1. **Concrete soft spend ceiling.** The review's one substantive gap: a paid per-query API needs a *checkable* cap, not posture. The SKILL.md names **≤3 query angles per invocation**, **`--num-results 25`**, and **stop-and-ask before a 4th angle or any re-run**.

## Brian's standing build constraints (this packet + future skills)

2. **Keep the skill LIGHT to start.** Thinnest viable SKILL.md; defer optional arms. Started `disable-model-invocation: true` (explicit-only) so a *paid* verb never auto-fires.
3. **Single source of truth — link out, don't duplicate.** The SKILL.md must *reference* the canonical homes (Recipe 9 for diff/output, `exa_search.md`/`.py` for tool mechanics + recall caveats, `store.py` for the diff), never restate them. The change-mode review diffs SKILL.md against Recipe 9 to catch paraphrase-instead-of-link.

## Scope held from the proposal

Never captures (output is a worklist; capture stays `/research-company`). No store writes, no new tool/script, no stored Signal/category, no scheduled job. The fast-capture arm is fenced to a future packet.

## Next

Implementation (done — see `implementation-notes.md`) → independent **change-mode review** (the gate) against this decision. Risk: medium.

## FINAL DECISION (2026-06-24): REJECTED

The accept-with-revision decision above is **reversed**. A post-merge live test — the value check this whole packet lacked — falsified the verb: Exa `/search` surfaced **5 of 32** obvious players in a cohort Brian knows (docs/PM), and had already silently missed the category-definers in telehealth. A prior `2026-06-20-cohort-discovery` bake-off (unread before building) had already ranked feeders (**websearch 0.69 > listicle 0.34 > … ; exa /findSimilar FAILED**) and shipped a `cohort-discovery.workflow.js`. So this verb both **bet on the weakest feeder** and **duplicated existing validated work**.

**Outcome — rejected and unwound:** `skills/discover-neighbors/` deleted; the `QUERYING.md` + `tools/exa_search.md` pointers reverted to HEAD; engine verified clean (`querycheck --strict` OK). Nothing reached the committed tree.

**The problem is still real** (Coverage — "discover companies not in the store"); only this *approach* is rejected.

**revive_if:** restart from the existing `cohort-discovery` bake-off (websearch + listicle **union**, drop exa-as-core), re-run on a SaaS cohort to confirm generalizability, and graduate **only** behind an `acceptance_check` that tests recall against a known cohort — the gate this packet never had.

Lessons logged as observations: `acceptance-criteria-tested-shape-not-value-e7a2`, plus prior-art-unchecked, single-source-vs-union, and value-blind-review sightings this session.
