# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Strength: `offerings.md` per-SKU rosters were already warm for all 4, so the price read cost zero new capture. Weakness: Nike's roster scoped to one line, so capture *scope* (not capability) bounds breadth comparison. | C2 (warm prices); C5 (Nike recovery-only) | G1 · gap |
| **Structure** | The gap: no structured field for non-price retail decision factors (returns/warranty/shipping/payment/channel) — confirmed absent from SCHEMA and all 4 frontmatters. They live in prose. Strength: `business_model` + price-visibility token express price/revenue shape cleanly with **no strain**. | W1 (prose-only factors); S1 (token handled consumer-vs-services split); `SCHEMA.md` has no warranty/return field | W1 · wish; S1 · surprise |
| **Query / access** | A buyer's purchase-protection question is not greppable — it requires reading 4 prose blocks; price questions are greppable via offerings rosters. | read.md Gap Map | W1 · wish |
| **Freshness / automation** | `captured_at` dates the capture but carries no flag that pricing was promotional; Therabody/Hyperice were mid-Prime-Day. A price read off the clock alone misleads. | C6; offerings/site_notes | G2 · gap |
| **Synthesis** | Strength: the read held the State (prices, business_model) vs Judgment (buyer "goes blind") line cleanly and labeled the verdict. | read.md Result/Gap Map | — |
| **Guardrails** | Store-only stayed store-only; no spend, no live browse, no mutation; loop1_failure_mode (over-generalizing from price-publishers) was explicitly guarded. | run-notes exit check (all pass) | — |

## Lenses

**Steward** — Honest. Provenance is per-claim with store clocks; the sale-snapshot freshness
risk is surfaced (G2); the State/Judgment boundary held; absences read as "not found." The
one integrity watch is G2 — a clean-looking captured price that is silently a sale price is
exactly the "fail loud before silently wrong" case, and the read caught it.

**Dev Agent** — No new helper is warranted from n=4. The toil observed (hand-assembling a
4-brand purchase-protection table from prose) is a *fielding* question, not a tooling one;
converting it to a field is a learning-pass call, not a run's. Prefer leaving it as a
grep-verifiable observation (W1) until it recurs.

**Founder** — "No new primitive needed" holds and keeps the engine light. The W1 fielding
want is real but must clear the anti-sprawl bar (what would a returns/warranty field
*replace*? nothing yet) before earning a place — resist ontology gravity at n=1 entity type.

## Recommendation

- **No-op / keep as observation:** Yes. The frame fits transactional retail at the price
  layer; the non-price-factor want stays an observation, not a field.
- **Watch for recurrence:** `depth-backfill` + `schema-edge-entity-type` (W1) — the
  "body carries the decision, structured spine doesn't" shape now has two sightings (045
  agencies, 046 consumer goods); a pass should judge whether it clusters with L006 or forms
  its own lesson. `denominator-reconciliation` (G1, uneven enumeration) and
  `freshness-monitoring` (G2, sale-snapshot) also recur.
- **Severe `risk-miss` to surface now:** None. G2 (sale-price-as-current) is a real but
  caveated freshness risk, not a shipped error.

## Raw learning to preserve

Observations W1, G1, S1, G2 in `run-notes.md` — appended to `learning/observations.md` this
Loop 2. No developer-side sighting beyond those four.

**No lessons proposed, nothing graduated, no spike, no system change implemented.**
