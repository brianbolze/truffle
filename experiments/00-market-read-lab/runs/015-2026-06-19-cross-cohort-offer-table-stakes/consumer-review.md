# Consumer Review

Question: **Was the read itself valuable enough for a human or agent to trust, reuse, or act on?**

## Verdict

- **Valuable? Yes.**
- **Why:** The read answered a question a strategist actually cares about — what's DTC-telehealth
  table-stakes vs cohort-specific — and produced two non-obvious, briefing-ready findings: (1) the
  agnostic mechanics (cash-pay rail 49/54; compounding-capable 52/54) are near-constant *because*
  they're the lowest-information cuts, which inverts the "table-stakes → store it" instinct into a
  documented persistence-boundary heuristic; (2) the two exceptions on *both* agnostic axes are the
  same two brands (Nurx, One Medical) — a coherent "real clinic" cluster a strategist can name. The
  modality-as-cohort-property finding (TRT 0/8 async vs GLP-1 12/19 async) was a genuine surprise
  not pre-loaded by the question. Every finding is tied to verbatim cell counts; the denominator
  caveat is named and graded (MRL-001, 5th sighting); price-publication was scoped out, not fudged.
- **What the consumer can do now:** Lift the two agnostic-axis claims directly into a brief
  ("DTC telehealth defaults to cash-pay + compounding-capable across every condition; the only
  both-axis deviants are Nurx and One Medical, the insurance-accepting FDA-brand-only outliers").
  Use the modality finding operationally: a brand's modality is largely constrained by the
  *condition* it treats, not brand taste. The design answer (no new cross-cohort primitive) is also
  actionable — no schema work needed.
- **What made it safer / better than generic Claude + web search:** Generic Claude can't reproduce
  the 54-brand cross-cohort matrix — it would hallucinate counts or require manually classifying 54
  sites. The numerical spine (5/54 insurance, 2/54 FDA-brand-only, TRT 0/8 async) is derived from
  already-captured, dated, field-structured store State. The "same two brands on both axes" coherence
  is only visible because both fields were extracted from one corpus simultaneously — a web search
  would never surface it.
- **Biggest limit:** The denominator. 54 of 135 store companies have structured `telehealth.md`, and
  each cohort's n is anchored-only (generalists fall into `multi/none`). The agnostic claims are
  robust to this (generalists reinforce them); the cohort-specific proportions — especially
  sexual-health (n=3) — are floors. Treat direction as strong, exact percentages as indicative.
- **Human follow-up needed:** Price-publication (5th mechanic) is deliberately on prior-run secondary
  footing; a dedicated bounded run (66-file `offerings.md` Visibility extract, MRL-009/010 guard)
  would resolve it. The highest-value lab follow-on is a *second* cross-cohort read on a different
  field family — if it finds the same "near-constant ⇒ low-information ⇒ don't store" tension, the
  persistence-boundary heuristic hardens from one-run Judgment into a documented design rule.

## Value diagnostics

| Signal | What to look for | Evidence / gap |
|---|---|---|
| **Useful** | Clear answer / decision aid, not just a summary. | Yes — agnostic-vs-specific verdict + the "table-stakes ≠ durable-State candidate" design call. |
| **Judgment-ready** | Fresh, rare, cited ingredients to reason from. | Yes — 5 verbatim cross-cohort distributions + the Nurx/One Medical coherence finding. |
| **Sourced & cited** | Claims trace to dated captures; uncertainty visible. | Yes — C1–C5 → receipt S1 (store clock 06-04→06-18); C6 demoted to secondary; denominator caveat named. |
| **Deep enough** | Covers the intended set. | Partial-by-design — 54/135 companies, anchored-only n's, framed as floors. Agnostic claims robust; cohort-specific indicative. |
| **Fresh enough** | Capture dates / stale risk visible. | Yes — store clock cited; A/B-volatility of front doors flagged. |
| **Kept / reusable** | Warm files for the next ask. | Yes — `cross-cohort-structural-matrix.md` receipt + reusable cross-cohort grep recipe. |

## Job fit

| Job | Did the read help? | Missing / next step |
|---|---|---|
| **Compare a whole field** | Yes — first cross-cohort synthesis collating 54 brands' mechanics no single tab gives. | Price-publication dimension still single-cohort/secondary. |
| **Five-second brief input** | Yes — the two agnostic-axis claims + Nurx/One Medical outlier are brief-ready verbatim. | Exact cohort-specific percentages are floors, not laws. |
| **Build on top without re-capturing** | Yes — proved the MRL-002 grep recipe generalizes to the cross-cohort axis for downstream agents. | — |

## Lens check

- **Strategist:** Lands plainly and fast; the "table-stakes are the *worst* things to store" inversion
  is a genuinely novel, hard-to-get-elsewhere insight.
- **The Pantry / downstream system:** Can reuse the cross-cohort grep + the labeled State cells as
  ingredients without re-browsing; Judgments are clearly fenced off.
- **First Contact:** Would trust it — counts are reproducible (Loop 2 verifier re-derived all five
  with zero discrepancies), caveats are visible, no spend or live browse.

## Triage submissions

No new consumer-originated item. The persistence-boundary heuristic and the cross-cohort denominator
flavor are captured as additive Evidence Log appends to MRL-002 and MRL-001 (see developer review +
`triage.md`). No graduation.
