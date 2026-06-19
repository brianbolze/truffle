# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Reviewed via the 3-pass adversarial workflow. Headline: **clean MRL-002 recurrence, no new primitive.** The
State/Judgment boundary held; the two verifier errors were query-accuracy (misread fields), not structural
failures; the reviews/forums source gap reaches a second sighting and earns a named (P3/Submitted) candidate.

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Capture** | No new capture need — the positioning read ran entirely off existing `telehealth.md`/`profile.md` State. | None. |
| **Structure** | State→Judgment crossing in two places (axis labels, whitespace). Both correctly labeled `[J]`; Judgments stayed out of `store/`. The convention held. | None — adding a `judgments/` module or schema guard would be living infrastructure over a working convention. |
| **Query / access** | **The two verifier errors both originate at the field-read layer** (gogeviti TRT count; gethealthspan `access_model`/`Labs` re-derived from prose, not read verbatim from frontmatter). | A recipe-level guard, not a helper: *read `access_model` frontmatter and `Labs:` lines verbatim before writing a panel summary; never re-derive from prose.* Belongs in MRL-002's recipe language. |
| **Freshness / automation** | None — positioning is durable enough at ≤19-day captures. | None. |
| **Synthesis** | The read template carried a positioning/proof read cleanly; `[J]` labeling + dated receipts worked. | None. |
| **Guardrails** | The **adversarial verifier pass** is what caught both errors — evidence that the Loop-2 verify step is doing real work, as in run 008. | Keep the verifier pass as standard Loop 2 shape. |

## Lenses

**Steward** — The system stayed honest. Provenance is intact (every claim → dated capture), freshness is
visible, and State/Signals/Judgments separation held: the axis and whitespace are labeled `[J]` and live in
the read, not in `store/`. The two errors were *factual field-reads* (one an internal inconsistency the
read's own evidence table already contradicted), not leaked judgments — and the adversarial pass caught and
corrected both. That is the boundary working as designed, not failing.

**Dev Agent** — The repeated toil here is **not** machinery (the cohort grep + section read was trivial) —
it's **field-read fidelity**. The gethealthspan miss is the tell: a panel summary should quote the
frontmatter `access_model`/`Labs` fields verbatim rather than paraphrase from the prose `Notes`. That is a
one-line addition to the MRL-002 recipe guidance (a grep-verifiable contract: panel cells must match
frontmatter), not a new helper or knob. No schema change.

**Founder** — The run compounds the warm/cited/cheap-to-reask asset (a reusable positioning panel over a
captured cohort) while staying light — no new surface, no ontology gravity. The one place to resist gravity:
the reviews/forums gap is real and now twice-sighted, but it should be *named and watched*, not built — one
sprint's evidence justifies a P3 candidate with a natural home (`profile.md` Credibility or a `signals/`
capture grain), not a schema commitment.

## Recommendation

- **No-op / keep as observation:** No new primitive. State/Judgment boundary and the read template both held.
- **Watch for recurrence:** MRL-001 gets a *positive contrast* point — clean `anchor_category` frontmatter
  made the denominator a single grep (only 2 straddlers hand-called), the opposite of run 008's TRT-boundary
  toil. Worth tracking when frontmatter cuts are clean vs fuzzy.
- **Submit triage candidate:** (1) MRL-002 Evidence Log — positioning-read recurrence + the verbatim-field
  guard the errors expose; (2) a **new P3/Submitted candidate** for reviews/forums **body content** as a
  source ingredient (second sighting across two different read questions).

## Triage submissions

Append-only evidence + one new candidate (statuses are suggestions; graduation stays human-gated):

- **MRL-002 (query recipes)** — Evidence Log: *State positioning-read recurrence (run 009).* Extends the
  recipe family from `Visibility`-column pricing reads (000/008) to a positioning/credibility surface
  (`anchor_category` grep → `Credibility & access` + `Notes` read → supply↔diagnostic axis labeling) — same
  latest-capture + field-extract + group/label idiom, different captured surface. **Adds a needed guard:**
  the two verifier errors (gogeviti count; gethealthspan `access_model`/`Labs` overstated) trace to
  re-deriving fields from prose; panel cells should quote frontmatter (`access_model`, `Labs:`) verbatim.

- **MRL-001 (denominator reconciliation)** — Evidence Log: *contrast data point (run 009).* A clean
  `anchor_category` frontmatter cut reduced the cohort boundary to a single grep + 2 hand-called straddlers
  (getopt, joinfridays) — useful contrast to run 008's harder TRT boundary; reinforces that when a clean
  frontmatter cut exists, denominator labor nearly vanishes.

- **MRL-010 (new candidate, P3 / Submitted)** — *Reviews/forums body content as a source ingredient.*
  Second sighting: run 008 fired `source-panel` for customer-pain/trust reads; run 009 fires it again for
  longevity trust/whitespace reads. Both needed review *body* content (objection mining, distrust of
  compounded NAD, churn) absent from the store. Ratings already land in `profile.md` Credibility blocks;
  bodies do not — the delta is concrete. Two sightings across two different read questions on adjacent runs
  is enough to **name** it, not enough to prescribe a schema change. Hold for a third sighting before any
  graduation discussion; natural home would be `profile.md` or a `signals/` capture grain.

No graduation, no implementation, no spike. `reviewed` reflects review completion only.
