# Developer Review

Question: **What did this run reveal about Truffle's missing or weak ingredients,
capabilities, and guardrails?**

## Capability pressure

| Capability | Observed gap or strength | Evidence from this run | Logged observation (ID · kind) |
|---|---|---|---|
| **Capture** | Strength: required scalar contract is genuinely 100% captured; `unverified_fields` never degrades to empty. Gap: relation fields (`parent`/`owns`) captured on only 11–13% — too thin to partition on. | C1 census; C5 counts | S4 · surprise; G1 · gap |
| **Structure** | Strength: subtractive emptiness is perfectly `entity_type`-gated, so the State boundary holds (a blank *encodes* shape, not missing data). Gap: no structured field separates a true-negative relation (`parent: []`, none exists) from a not-captured one. | C3 (all empties = Investor/Holding); C5 | S2 · surprise; G1 · gap |
| **Query / access** | The read crosses into Judgment (the four-tier map is the run's synthesis, not store State) — correctly labeled. Pressure: a downstream consumer needs fill-rate + concentration + entity-gating + the comment convention together to choose a key; "is it filled" alone misleads. | read.md Result framing; S3 | S1 · surprise; S3 · surprise |
| **Freshness / automation** | Out of scope by design; the census is a point-in-time baseline that will drift as the corpus grows. Noted, not chased. | run-notes Next-run advice | — (no-op) |
| **Synthesis** | The read kept State (the counts) and Judgment (the tiers) distinguishable, and held "coverage fact ≠ market fact" throughout — the run's own discipline worked. | read.md Market Pattern / What Would Change | S1 · surprise |
| **Guardrails** | **Live finding: a guardrail (fail-loud-by-comment) is anti-machine-readable.** The inline `# empty — …` convention protects a human but feeds comment text to a naive parser as data. A read-side parsing hazard, not a schema defect. | C7 (first-pass vs comment-stripped counts) | R1 · risk-miss |

## Lenses

**Steward** — The system stayed honest. Provenance (`captured_at` 100%), the
State/Judgment split, and visible uncertainty (`unverified_fields` 136/136) are all intact.
The one honesty wrinkle is internal-facing: the structured-emptiness channel (R1) is honest
to humans but misleading to machines — worth a Steward note because the store advertises
grep-verifiable contracts, and R1 shows a naive grep over-reads fill.

**Dev Agent** — The repeated toil this run exposes is the comment-stripping every frontmatter
parser must do (R1). That is the single most recipe-able finding — but it is a *reading
convention*, not a helper, and naming it is an out-of-band learning-pass call, not a run
action. Everything else (the tiers) is a one-shot census, not recurring toil.

**Founder** — The run compounds the warm asset without adding ontology gravity: its entire
payload is "here is what you can already rely on," and its explicit conclusion is *no new
primitive*. It resists the additive reflex — relations are thin, but the read declines to
propose a relation field, correctly (a field you cannot fill reliably fails engine-dev's
fillable-cut bar — the very thing G1 measures).

## Recommendation

- **No-op / keep as observation:** all of S1–S4, G1, G2 — calibration findings, no build.
  The whole run is a "no new primitive needed" outcome with a dependability map as payload.
- **Watch for recurrence:** `denominator-reconciliation` is now n=6 (036/037/039/042/054 +
  this run's S3, the first *store-wide* and *concentration-flavored* sighting that a
  high-fill field can still be a lopsided partition key). `relation-pressure` recurs (G1 ≈
  039 S1, now sized). `R1` (comment-masking) is a cousin of run-037 DR2 (unreliable second
  channel) — if a pass clusters them, route to docs/recipe.
- **Severe `risk-miss` to surface now:** **none severe.** R1 is a real risk-miss but
  conditional — it only bites a *naive* (non-comment-stripping) downstream parser, and no
  such consumer is live today. Surface it as a watch item, not an alarm.
- **Evidence-verify nuance (logged as DR1):** read.md Tier-2 lists 7 investor entities as
  "the empties," but `business_model` is empty for only 6 (the VCs); the 7th, blueowl, carries
  `business_model: Other` and is empty only for `portfolio_shape`. The core claim ("every
  subtractive empty is an `Investor / Holding`") survives and is in fact *strengthened* —
  blueowl, an asset manager, gets the closed-set-misfit `Other` rather than a blank — but the
  read's "7 empties" phrasing slightly overstates the `business_model` count. A precision slip
  the adversarial pass caught (cousin of run-042 VR1).

## Raw learning to preserve

Logged to `run-notes.md` Observations: **DR1** (the 6-vs-7 business_model-empty precision
nuance + blueowl's `Other`-not-blank, which sharpens S2's entity-gating story). S1–S4/G1/G2/R1
already carry the substantive builder findings.

**No lessons proposed, nothing graduated, no spike, no system change.**
