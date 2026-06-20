# Developer Review

Question: **What Truffle system behavior does this run pressure?**

Reviewed via a 3-pass adversarial workflow (evidence verifier + consumer + developer, Sonnet).

> **Verifier (zero factual discrepancies):** Independently re-derived all five load-bearing counts
> from `store/*/telehealth.md` (54 files): C1 5/54 insurance-billers (`joinfound, lifemd, nurx,
> onemedical, ro`) ✓; C2 2/54 FDA-brand-only (`nurx, onemedical`) ✓; C3 TRT 0/8 async, 6/8 sync &
> GLP-1 12/19 async, 2/19 sync ✓; C4 access_model per-cohort counts ✓; C5 audience ✓; Nurx+One
> Medical both-axes overlap ✓. **Store-only discipline PASS** (no spend, no live browse, no mutation,
> no snippet-as-evidence). Two **cosmetic** notes only: the read/receipt shorten the enum
> `membership-required` to "membership" (counts correct), and the C3 headline omits the 2/8 TRT
> hybrid slice (receipt records all three; "sharpest contrast" framing defensible). **Fixed below.**

## Capability pressure

| Capability | What did the run expose? | Smallest useful response |
|---|---|---|
| **Query / access** | The MRL-002 State-read recipe generalizes from within-cohort to a **cross-cohort axis** (group by `anchor_category` across all cohorts in one pass) — 5th surface, 1st cross-cohort. | Append to MRL-002 Evidence Log; recipe-level only. |
| **Structure** | The persistence-boundary sub-question: a near-constant cross-cohort mechanic is a *poor* durable-State candidate (low entropy). State/Judgment boundary held cleanly at cross-cohort grain — no new primitive needed. | Document as an MRL-002 sub-heuristic *after a 2nd sighting*; no field/object now. |
| **Synthesis** | "table-stakes ≠ durable-State candidate" is a reusable persistence-boundary heuristic, but one-run. | Watch for recurrence on a different field family. |
| **Guardrails** | Anchored-only denominator under-counts every per-cohort n simultaneously (5th cohort sighting, 1st cross-cohort). | Append to MRL-001 Evidence Log. |

## Lenses

**Steward — is the system still honest?** Yes. State (C1–C5, verbatim frontmatter → receipt S1) is
reported first; the transition into Judgment is fenced under "Judgment (labeled, tied to C1–C5)"; the
three interpretive bullets trace back to quoted cells. C6 (price-publication) is correctly demoted to
prior-run secondary, not promoted to decision-grade. The Nurx/One Medical "coherent outlier" straddles
State and Judgment but is handled as an observation from C1+C2 counts, not a standalone claim. The
boundary labeling works at cross-cohort grain — Truffle should support this boundary, and the run shows
it does so without a new primitive.

**Dev Agent — can repeated toil be removed?** The cross-cohort read is the *same* grep+group+label
recipe with no new toil — one parse pass over 54 files. That's evidence the recipe family is
saturated at recipe level (MRL-002), not evidence for a helper. No new knob wanted.

**Founder — does it compound the warm/cited/cheap asset while staying light?** Yes — the design answer
*is* "don't add ontology": the cohort-agnostic mechanics are the worst durable-State candidates
precisely because they're universal, and the cohort-specific ones group at query time. The run resists
ontology gravity rather than feeding it.

## Recommendation

- **No-op / keep as observation:** the persistence-boundary heuristic is real but one-run; do not
  document it as a rule yet.
- **Watch for recurrence:** a 2nd cross-cohort read finding the same "near-constant ⇒ low-information
  ⇒ don't store" tension on a different field family hardens it into a documented MRL-002 sub-rule.
- **Submit triage candidate:** two additive Evidence Log appends only (MRL-002, MRL-001). No new item,
  no graduation.

## Triage submissions

Append-only Evidence Log entries to existing items (added to `triage.md` this run):

1. **MRL-002** — cross-cohort axis confirmed (5th State-read surface, 1st cross-cohort) + the
   persistence-boundary heuristic ("table-stakes ≠ durable-State candidate"), explicitly flagged as a
   one-run Judgment needing a 2nd sighting to harden.
2. **MRL-001** — 5th-cohort recurrence of the anchored-only under-count, new flavor: cross-cohort reads
   apply the under-count to every per-cohort n simultaneously; agnostic claims strengthened, cohort-
   specific n's are floors.

**Do not graduate, spike, or implement system changes.**
