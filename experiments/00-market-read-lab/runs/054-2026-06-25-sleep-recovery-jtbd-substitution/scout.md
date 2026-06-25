# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue): L001 (coverage radar), L004 (denominator travels with the read), L005 (query-time grouping only when corpus carries the cut), L006 (price-visibility grain). Heavy recent recurrence: `denominator-reconciliation` — `primary_industry` is **not** an entity-shape cohort key (n≥4: runs 036 G3, 037 G2, 039 DR1/S2, 042 G3). `relation-pressure` — store has structured **vertical** relations (`parent`/`owns`) but **zero horizontal** competes-with/substitute relation (039 S1, 047). Recurring "value lands on builder/Pantry not buyer" CR streak (038/039/041).
- `scout-context.md`: two-test selection (value+reach / design). Don't optimize for store-answerability. Gap-probes first-class.
- Last 3 `run-notes.md` files: 051 (cold-start profile reliability, store-only), 052 (captured-price freshness decay, bounded-live), 053 (wearable coverage radar / L001 generalizability, bounded-live). Recent slate is store-only schema/cohort reads + a few bounded-live freshness/coverage probes.
- Current run artifacts, if resuming: none (fresh scaffold 054).

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (SELECTED).** A buyer wants to improve **sleep & recovery** and is open to any solution type. Can Truffle assemble the cross-category option set — connected hardware (Oura/Whoop/Eight Sleep/Nike), recovery devices (Therabody/Hyperice), plus any supplement/longevity/telehealth entrants — from captured State alone, or do `primary_industry`/`offering_category` tags scatter substitutes so the buyer's "what are my options?" is structurally unanswerable? | gap-probe | yes | store-only | "What are my options for X" is a top buyer job; tests whether the store serves a **cross-industry job-to-be-done substitute set**, not a within-industry cohort. | JTBD-substitution as a horizontal relation at the **buyer-goal grain** — is it recoverable from existing State (description/offering_category/target_market) or does it need a new cut? Joins `relation-pressure` (no horizontal relation) + `denominator-reconciliation` (industry ≠ cohort). | Reaches past the comfortable within-cohort read (043/053 stayed inside "wearables"): substitution that **crosses** industry tags at a buyer goal. | The store's substitute set, assembled by hand-judgment; whether industry/category fields recover it; "not captured" vs "not a substitute". | Claiming a substitute set is complete when tags don't carry the JTBD cut; calling a thin slice "the market" (say "not found", not "not there"). |
| C2. Across subscription-model brands store-wide (not one vertical), what cancellation / commitment / auto-renew terms are disclosed vs silent, and can a buyer compare lock-in across cohorts? | value-read | yes | store-only | Lock-in is a real buyer worry; cross-cohort cut. | Tests whether commitment terms are a fillable structured cut or prose-only. | Cross-cohort, but offer-ladder runs (010/043) partly covered it. | Per-brand terms with capture clocks. | Re-running the offer-ladder shape; thin reach. |
| C3. Do non-telehealth cohorts (deep-tech, SaaS, agencies, consumer goods) use the **same trust/proof devices** as telehealth (run 021), or are proof-device vocabularies cohort-specific? | calibration | yes | store-only | Tests generalizability of the proof-device read across verticals. | Whether a proof-device taxonomy is telehealth-overfit. | Cross-vertical calibration. | Body-prose proof devices across cohorts. | Soft, descriptive; weak design payload. |
| C4. For the sleep/recovery JTBD set, do third-party "best sleep tech 2026" roundups name **solution types the store holds none of** (sleep supplements, CPAP, apps, mattresses)? | gap-probe | yes | bounded-live | Coverage radar (L001) at the **JTBD** level, not category level. | Whether L001's missing-member recipe generalizes from a named category to a buyer goal that spans categories. | External demand-side panel. | SERP + ≥2 listicles, cross-source intersection, store diff. | L001 already graduated; risk of mere re-confirmation. Held as bounded alt to C1. |
| C5. Across the store, which companies expose a fundraising/round Signal (SEC Form-D) and what is the cross-store funding footprint by cohort? | value-read | yes | store-only | Investor-facing cross-store cut. | Funding-signal coverage + grain. | Cross-store. | signals/ + frontmatter. | Heavily covered (007/029/048); repeat. |
| C6. Extending run 025 (telehealth geographic availability) to the **non-telehealth** slice: do hardware/SaaS/consumer brands disclose geographic/shipping availability, and can the store answer "can I get this where I am?" | value-read | yes | store-only | Real buyer fact; extends a telehealth-only read cross-vertical. | Whether availability is an ingredient-type gap store-wide (038 G1 found it intake-gated for telehealth). | Cross-vertical availability. | Per-brand availability lines + clocks. | Medium reach; availability may simply be "ships everywhere" for hardware (thin). |

## Selected Question(s)

1. **C1 — Cross-vertical sleep/recovery JTBD substitution neighborhood (store-only).** Strongest reader value (a top buyer job), genuine reach (crosses industry tags at a buyer-goal grain, where every prior cohort read stayed within one industry), and a fresh builder lens that sits exactly on the two recurring frontiers — horizontal relation absence (`relation-pressure`) and `primary_industry` ≠ cohort key (`denominator-reconciliation`) — without re-running either. Fully store-only, so autonomous-safe.
   - C4 is the bounded-live sibling if C1 shows the store holds the hardware/recovery options but is blind to whole adjacent solution types; left for a future run to keep this cycle store-only.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "A buyer wants to improve sleep & recovery and is open to any solution type. Can Truffle assemble the cross-category option set — connected hardware (Oura/Whoop/Eight Sleep/Nike), recovery devices (Therabody/Hyperice), and any supplement/longevity/telehealth entrants — from captured State alone, or do primary_industry/offering_category tags scatter the substitutes so the buyer's 'what are my options?' question is structurally unanswerable?"
selected_slug: sleep-recovery-jtbd-substitution
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Captured companies whose offering plausibly serves the sleep/recovery buyer goal, assembled by reading descriptions/offering_category/body across cohorts — NOT a single primary_industry or offering_category draw. Treat as partial: the JTBD cut is reader-assembled, not a store field."
likely_source_panel: "store/<domain>/profile.md (description, frontmatter, body), grep over primary_industry / offering_category / target_market; no external sources."
builder_lens: "Whether a cross-industry job-to-be-done substitute set is recoverable from existing State, or whether the buyer-goal substitution neighborhood needs a cut the store does not carry (horizontal relation / JTBD tag). Tests relation-pressure (no horizontal relation) and denominator-reconciliation (industry != cohort key) at the buyer-goal grain."
reach_reason: "Every prior cohort read stayed inside one industry (wearables, SaaS, deep-tech). This reaches the cross-industry substitution a real buyer faces, where industry/category tags are expected to scatter the option set."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/learning/"
disallowed_actions:
  - "No live browsing, WebSearch, or Firecrawl spend."
  - "No store/ mutation or write-back."
  - "No durable primitive / category / relation creation."
  - "No lesson proposal or graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable/mappable entirely from local store files and lab artifacts; store-only; no spend, no write-back."
loop1_failure_mode: "Overstating the substitute set as complete (telehealth-heavy corpus may hide whole solution types), or treating an industry/category draw as if it recovered the JTBD cohort. Say 'not found', not 'not there'."
```

## Selection Notes

C1 is a gap-probe whose payload may well be "no new primitive needed" — the honest
likely outcome is that the cross-industry substitute set is reader-assemblable from
prose but not queryable from any field, the same "diagnosable but not queryable /
map-not-ingredient" frontier seen in 039 CR1 and 043 CR1, now at the buyer-goal grain.
That is still a valuable calibration: it tells the roadmap whether JTBD-substitution is
a real persistence-boundary candidate or stays query-time. Evidence mode is store-only
by deliberate choice for autonomous safety; the bounded-live reach (C4) is parked.
