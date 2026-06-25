# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001–L006 read. Heavy recent run streak (036–047) is **schema-fit / entity-type** on
  non-telehealth slices, dominated by tags `schema-edge-entity-type`,
  `denominator-reconciliation` (n=4 industry-draw), `query-time-grouping-enough` (every
  run lands "no new primitive needed"), `relation-pressure` (039/047, now twice-anchored),
  and `bounded-live-spend` (040/047 both breached/near-breached the variable-cost-format
  ceiling). `traction-readiness` appears **once** (run 029) — genuinely under-tested.
- `scout-context.md`: two-test selection (value/reach + design); start from a reader's
  question, name the builder lens, do not optimize for store-answerability; gap-probes
  first-class when bounded.
- Last 3 `run-notes.md` files (045 agencies, 046 consumer-goods, 047 saas-competitor-edge):
  045/046 confirm prose carries the buyer while the structured spine can't; 047 confirms
  horizontal relation absent + bounded-live JSON-extraction spend breach. All three are
  schema-fit/relation reads — the slate should diversify off that axis.
- Current run artifacts: fresh scaffold (048), Scout-only.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **[RECOMMENDED]** For an investor/partner sizing up the captured **pre-revenue deep-tech cohort** (electra-aero, verdegoaero, blueenergy, cfs-energy, evoloh, sorafuel, beta-team; euclidpower as a commercial foil), can the store support a "**who has momentum / is gaining ground**" triage from captured State — capital raised, milestone cadence, hiring/partnership motion — or is traction a Signals/time-axis fact the static profiles structurally can't carry? | gap-probe / calibration | yes | store-only | Momentum is the *literal* question an investor asks of pre-revenue deep-tech, and run-042 already proved the cohort's **maturity** (a State fact) is legible — so this isolates the adjacent, harder axis: **traction** (Signals, time-axis, comparative). Directly tests the traction frame's deferred **cohort roll-up (#4)** and whether it can start from existing State. | Traction cohort aggregation layer; the **State-vs-Signals boundary**; whether momentum is assemblable from static profiles or needs the deferred comparability + durable-home machinery. Confirmed: **0/8 of this cohort has any `signals/` capture** — so the read rests entirely on static prose. | Reaches past the comfortable maturity read (042) into the time-axis/comparative frontier the engine flags first-class-future but hasn't built; controlled cohort (same as 042) isolates axis, not denominator. | Captured `description`/funding lines + `unverified_fields`; milestone blocks; SEC/`signals/` absence noted as **not-captured**, not not-true. | Laundering a **level** ("raised $X", "operational 2027") into a **delta/momentum** claim ("gaining ground") — the frame's #1 grain trap; and over-claiming a snapshot as a time-series. |
| For a B2B buyer doing **vendor-durability / staying-power** diligence on the captured SaaS slice (Datadog, Snowflake, Stripe, Twilio, PostHog, etc.), can the store ground "will this vendor still be here / is it winning" from captured State (scale claims, funding, tenure)? | gap-probe | yes | store-only | Procurement's real question behind any SaaS shortlist. | Traction/durability lens on a mature cohort; the "easy first-party signal" (ticker, big round) the frame says capture-cheap. | Reaches the per-company **competitor-triage** consumer (frame). | Scale/funding prose + any SEC signal; tenure via Wayback signal where present. | Overlaps the 039/044/047 SaaS reads (cohort fatigue); momentum still likely prose-laundered. |
| For the **telehealth slice that has 2+ `signals/` captures**, can captured **Signals deltas** (Trustpilot review velocity, SERP visibility, SEC/Form-D) rank brand momentum — testing whether *captured Signals* (not just State) carry a comparative read? | gap-probe | yes | store-only | The only slice with real time-axis substrate; tests frame **#2 (comparability)** head-on. | Whether the `signals/` append layer + `signal_delta.py` already supports a crude cohort momentum roll-up. | Reaches the comparability machinery directly. | Two dated signal captures per brand + delta tooling output. | Close to run-018 (signal change-pulse readiness) — repeat unless the *cohort roll-up* framing is genuinely new. |
| Across the **whole captured store**, which companies expose an **easy first-party traction anchor** (stock ticker / public filer, or a dated big announced funding round in prose/SEC) — i.e., what is the cheap-to-capture traction floor the frame says to grab? | calibration | yes | store-only | Sizes the cheap-signal denominator before any traction build. | The frame's "capture easy, obvious signals; refuse the paid-data swamp" boundary. | Reaches the build-scoping question for the traction layer. | Frontmatter + SEC signal + prose round mentions. | Census-shaped, lower standalone reader value; risks being a coverage table not a market read. |
| For a **women's-health telehealth** buyer, how do captured brands differ on access model (async vs hybrid, insurance vs cash, compounded vs FDA-brand) and offer structure? | value-read | yes | store-only | Recognizable buyer comparison on a slice less-read recently. | Pattern-extraction; likely re-confirms `query-time-grouping-enough`. | Modest reach (comfortable cached answer). | Store offer/access prose. | Adds little new design learning — another grouping-enough confirmation. |
| Can a delegated agent tell a **confident** captured traction/scale claim from a **self-reported/unverified** one across a cohort — testing whether the prose `unverified_fields`/self-reported flags survive relay on the *traction* axis? | calibration | yes | store-only | Maps the #1 value job (safe delegation) on a new axis. | Relay-discipline / confidence-grain (L002/L004/038-R1). | Reaches the delegation-grounding frontier on traction. | `unverified_fields` + self-reported flags across cohort. | Repeat of 038's grounding shape on a thin new axis. |

## Selected Question(s)

1. **[RECOMMENDED]** For an investor/partner sizing up the captured pre-revenue deep-tech
   cohort (electra-aero, verdegoaero, blueenergy, cfs-energy, evoloh, sorafuel, beta-team;
   euclidpower as a commercial foil), can the store support a "who has momentum / is gaining
   ground" triage from captured State, or is traction a Signals/time-axis fact the static
   profiles structurally can't carry?

Runner-up: the telehealth-Signals-delta momentum read (candidate 3) is the natural
follow-on *if* this run confirms static State can't carry momentum — it tests the one slice
that has a real time-axis substrate. Held off this cycle to avoid run-018 overlap and to
keep the cohort diversified from the recent telehealth-light streak.

These are Scout recommendations until Brian or the operator confirms one.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For an investor/partner sizing up the captured pre-revenue deep-tech cohort (electra-aero, verdegoaero, blueenergy, cfs-energy, evoloh, sorafuel, beta-team; euclidpower as a commercial foil), can Truffle's captured State support a 'who has momentum / is gaining ground' triage — capital raised, milestone cadence, hiring/partnership motion — or is traction a Signals/time-axis, comparative fact the static profiles structurally cannot carry?"
selected_slug: deep-tech-cohort-traction-momentum
run_type: system-test
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "The 8 captured pre-revenue/early-commercial deep-tech profiles from run-042's cohort (electra-aero, verdegoaero, blueenergy, cfs-energy, euclidpower, evoloh, sorafuel, beta-team). euclidpower is the commercial foil; beta-team the early-commercial boundary case. Treat the set as partial: an industry draw does not recover this entity-shape cohort (run-042 G3), so membership is the named-8, not a primary_industry grep."
likely_source_panel: "store/<domain>/profile.md (description, funding/capital prose, milestone blocks, unverified_fields) for the 8; store/<domain>/signals/ presence check (confirmed 0/8 captured). No external sources."
builder_lens: "Tests the traction cohort roll-up (traction-frame #4, deferred) and the State-vs-Signals boundary: can a comparative 'momentum' read be assembled from static captured State, or does it require the frame's deferred comparability (repeat-capture deltas) and durable time-series home? Probes whether the traction aggregation layer can start on existing substrate."
reach_reason: "Reaches past run-042's maturity read (a State 'is it shipping' fact) into the adjacent traction axis (a Signals 'how is it doing / who's gaining' fact) the engine flags first-class-future but hasn't built. Same cohort isolates the axis, not the denominator. Diversifies off the 036–047 schema-fit/relation streak onto the once-tested traction-readiness lens."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/learning/"
  - "_design/2026-06-14-traction-frame.md (design context for the builder lens only, not evidence)"
disallowed_actions:
  - "No live browsing, WebSearch, or Firecrawl capture."
  - "No store/ mutation, write-back, or signal capture."
  - "No durable primitive, field, or category creation."
  - "No lesson proposal or graduation."
  - "No treating funding/milestone levels as momentum deltas without flagging the grain gap."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files plus existing lab/design artifacts; no spend, no external evidence, no write-back. Standing store-only policy."
loop1_failure_mode: "Laundering a level (capital raised, 'operational 2027') into a delta/momentum claim ('gaining ground'); over-claiming static State as a time-series; or overstating cohort completeness from a partial/named denominator."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Chosen for: (1) reader value —
"who has momentum" is the literal investor question for pre-revenue deep-tech; (2) reach —
it crosses from the well-tested maturity/State axis into the time-axis/comparative
**traction** frontier the engine defers; (3) diversity — breaks the 036–047
schema-fit/relation cohort streak and revisits the once-tested `traction-readiness` lens;
(4) safety — pure store-only, no spend. The controlled re-use of run-042's cohort is
deliberate: it isolates the State-vs-Signals axis rather than re-deriving a denominator.
Expect the honest result to be "static State names funding/milestone **levels** but cannot
answer momentum/who's-gaining without a Signals delta layer" — a `gap-probe` whose payload
is a roadmap finding for the traction frame, with "no new primitive needed *now*" still
live.
