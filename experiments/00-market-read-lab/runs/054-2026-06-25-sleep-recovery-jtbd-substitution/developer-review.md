# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients, capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence | Logged observation |
|---|---|---|---|
| **Capture** | No gap — per-member State is rich and decision-grade. | read.md Gap Map ("answered cleanly") | — |
| **Structure** | `primary_industry`/`offering_category` are producer-shaped; cannot recover a buyer-goal cohort. Real but not new — reconfirms 036/037/039/042 at a new grain. | read.md Result(2); G2 | G2 |
| **Query / access** | **Strongest pressure.** No cross-cohort buyer-goal query path; prose `description`+body is the only substrate, and its reliability has a hidden gradient (vocabulary scatter, capture vintage). | read.md C5, Missing/Stale Coverage | DR1 |
| **Freshness / automation** | No pressure (store-only, no current claims). | — | — |
| **Synthesis** | State/Signals/Judgment kept clean — the substitute set is correctly labeled Judgment, consistent with 039 CR1 / 047. | read.md Result; run-notes Evidence Limits | (G1) |
| **Guardrails** | Source-rigor handled correctly — "not found ≠ not there", method bound named (L004 self-applied). | read.md S3 / Missing coverage | S3 |

## Lenses

- **Steward:** Honest. Provenance, per-profile clocks, State/Judgment separation, and visible uncertainty all present. The substitute set is labeled the agent's Judgment, not store fact — correct.
- **Dev Agent:** The repeated toil (hand-assembling a buyer-goal set) points at a **query-time recipe**, not a field. But the recipe carries a silent-partiality risk (DR1): "grep description+body for the goal" is reliable for conventional-vocabulary goals and silently partial for jargon-fragmented ones or sparse older captures.
- **Founder:** "No new primitive needed" keeps the asset light. A JTBD field would be open-ended, buyer-framed, and unfillable-reliably (fails engine-dev's fillable-cut bar); a substitute relation would be mostly empty/dangling (039 W1 logic). No filter/sort consumer has appeared. Holding is correct.

## Recommendation

- **No-op / keep as observation:** G1/W1 (no JTBD field; query-time recipe is the lightest path). "No new primitive needed" is the honest call in both adversarial directions — the recurrence strengthens the case for a *recipe*, not a field.
- **Watch for recurrence:** **G2 — `denominator-reconciliation` is now n=5** (036 G3, 037 G2, 039 DR1, 042 G3, 054 G2). Genuinely strengthened, not restated: the first four were **supply-side** cohort draws (group by what a company *is*); 054 is the first **demand-side** draw (group by what a buyer *wants*). Spanning both sides hardens the claim that `primary_industry` is producer-shaped *by construction*. Strong candidate for the next out-of-band learning pass to weigh a consolidated lesson — route cohort queries (either side) around the industry field. (Not a run action.)
- **Severe `risk-miss` to surface now:** None. Source-rigor and absence-language are correct.

## Raw learning to preserve

New rows appended to `run-notes.md` Observations and lifted to `learning/observations.md`:
**DR1** (the query-time recipe has a silent reliability gradient — vocabulary scatter + capture-vintage/prose-density) and **DR2** (the telehealth double-burial is a structural *inversion* of L005's corollary: not absent but **tag-correct-and-therefore-invisible** / misrouted — a mechanism L004/L005 don't cover). Everything else is covered by G1/G2/S1/G3/S2/W1/S3.

**Did not** propose, graduate, spike, or implement system changes.
