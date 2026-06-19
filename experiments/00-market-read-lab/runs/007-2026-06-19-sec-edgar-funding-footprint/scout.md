# Scout

## Prior Context Read

- `triage.md`: Open queue MRL-001/002 (denominator + store-query recipe; MRL-002 now P1, 2
  Signals-grain sightings logged after the 3 State-read ones), MRL-003 (depth-backfill),
  MRL-005/006 (relation edge + capture grain, hold), MRL-007 (homeless category-signal, hold),
  MRL-008 (captured-signal confounds travel with the field — **2 sightings: Run 005 reputation,
  Run 006 tenure; flagged as worth a human graduation look**), MRL-009 (write-back receipt section).
- `scout-context.md`: go wide on basic operator archetypes; prefer store-only / autonomous-safe;
  the Signals layer is named as the richest under-exercised territory.
- Last 3 `run-notes.md` (004 category-crowdedness, 005 Trustpilot, 006 Wayback): Signals reads
  (005/006) both hand-rolled the same latest-per-dir + field-extract loop; Run 006 said a **3rd**
  Signals-consumption read re-handrolling that loop is the MRL-002 trigger, and a tenure/reputation
  pattern is now 2 sightings on MRL-008. Run 006 next-run advice explicitly nominates
  **SEC-presence** as the next distinct signal grain.
- Current run artifacts: fresh scaffold, nothing to resume.

## Store grounding (for candidate realism)

135 profiles / 54 telehealth packs / 66 offerings. Captured signal grains by count:
**wayback 47, trustpilot 20, sec_edgar 20, trends 5, serpapi 2, exa_similar 2, ads 1.**
Trustpilot (005) and Wayback (006) are consumed; **sec_edgar (20 brands, Form-D rich) is the
largest unconsumed signal grain.** No `pricing.md` module exists — pricing lives inside
`offerings.md` roster cells.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| Among captured DTC telehealth brands, which show an SEC/Form-D funding footprint, and what does that footprint (form type, date, name-match quality) actually tell you vs. not tell you about company maturity? | mixed | yes | store-only | 3rd Signals-consumption read; SEC is the largest unconsumed grain; directly hits the MRL-002 (3rd latest-per-dir hand-roll) and MRL-008 (3rd captured-signal-confound) recurrence gates the last two runs named. Real strategist Q: who's institutionally funded vs bootstrapped. | Latest `signals/sec_edgar/*.json` per domain; report `form_d.match`, `is_vehicle`, `flags:[existence_only]`, `amount:null` alongside any funding claim; join `value_chain_role`. | Reading Form-D presence as "raised $X" — amounts are null and name-match can be a false positive (`is_vehicle`, ambiguous CIK). |
| Cross-signal maturity: which brands carry BOTH a funding signal (sec_edgar) and a reputation signal (trustpilot), and where do the two disagree (funded-but-low-regard / unfunded-but-trusted)? | mixed | yes | store-only | Tests whether two captured Signal grains compose at query time without a built join; a genuinely useful 2x2 for an investor/operator. | Latest per dir for both signal types, inner-join on domain, carry each signal's confounds. | Treating a 2-axis grid built on two thin captured floors as market truth; tiny overlap N. |
| Across the captured telehealth cohort, what access/channel model does each brand use — cash-pay, membership/subscription, insurance, pharmacy-direct — and which is becoming table stakes? | market | yes | store-only | Channel/access map is a named scout archetype not yet run; pure State read from telehealth.md / offerings.md. | `pharmacy_model`/role frontmatter + roster/subscription cues; label inference vs stated. | Channel cues are prose-scattered; whole-file grep inflates (the Run 004 trap). |
| What does each telehealth brand *lead with* in positioning — price, speed/convenience, clinical authority, outcomes, or identity — and what's the dominant claim archetype per category? | market | yes | store-only | Positioning/claims archetype not yet run; exercises whether claim posture is query-able from captured copy. | Hero/positioning lines in telehealth.md/profile.md; quote the claim, label as Judgment. | Claim classification is subjective; risks persona-performance over evidence. |
| Per-brand Wayback **trend diff**: for brands with ≥2 Wayback captures, has offer-page tenure/snapshot motion changed between captures (new offer pages appearing)? | system-test | yes | store-only | Run 006 only used latest; multiple captures exist per domain. Tests the Signals *trend/diff* path (signal_delta) rather than latest-snapshot. | ≥2 captures per (domain,keyword); use the diff comparator, not a hand re-walk. | Most domains may have only 1 usable capture → thin/again no-trend. |
| Who are the closest neighbors/substitutes for the cohort's anchor brands, per captured `exa_similar`? | market | no | live-external-needs-approval | Neighborhood archetype; but only 2 exa_similar captured — too thin to read store-only, would need fresh capture. | Captured exa_similar JSON; honestly only 2 exist. | Over-claiming a neighborhood from 2 captures; needs spend to be real. |
| Branded search-interest read from captured Google Trends — who has demand momentum? | market | no | live-external-needs-approval | Demand-signal archetype; only 5 trends captured — below a readable floor. | ≥1 trends JSON per brand; only 5 exist. | 5/54 is not a cohort; would mislead. |

## Selected Question(s)

1. **SEC/Form-D funding-footprint read** (primary) — largest unconsumed signal grain, directly
   advances two live recurrence gates, and a recognizable strategist question.
2. *(runner-up)* Cross-signal maturity (sec_edgar × trustpilot) — strong, but depends on a thin
   two-way overlap; better once the SEC grain is characterized on its own first.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Among captured DTC telehealth brands, which show an SEC / Form-D funding footprint, and what does that footprint (form type, filing date, name-match quality, existence-only flags) actually tell you — and not tell you — about company funding/maturity?"
selected_slug: sec-edgar-funding-footprint
run_type: mixed
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store domains with a captured store/<domain>/signals/sec_edgar/ dir (~20), framed against the 54 captured telehealth packs as the captured floor — not the market."
likely_source_panel: "Latest store/<domain>/signals/sec_edgar/<captured_at>.json per domain; store/<domain>/telehealth.md frontmatter (value_chain_role, anchor_category) for the join."
allowed_sources:
  - "store/*/signals/sec_edgar/"
  - "store/*/telehealth.md"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / SEC re-fetch (efts.sec.gov, data.sec.gov)"
  - "Firecrawl or any paid capture"
  - "store/ mutation or KB write-back"
  - "durable primitive / category creation"
  - "triage graduation"
approval_needed: no
why_autonomous_safe: "Answerable entirely from already-captured local signal JSON + existing store frontmatter; no spend, no live fetch, no mutation."
loop1_failure_mode: "Reading Form-D *presence* as a funded-amount or maturity claim — amounts are null, name-match can be a false positive (is_vehicle / ambiguous CIK), and existence_only flags must travel with every funding statement. Also the whole-file grep trap and overstating completeness from a ~20-domain captured floor."
```

## Selection Notes

The SEC read wins on three axes at once: (1) decision leverage — funding footprint is a question a
strategist/investor actually asks; (2) system-test value — it is the **3rd** Signals-consumption
read, the threshold both MRL-002 (latest-per-dir hand-roll) and MRL-008 (captured-signal confound)
explicitly named as their recurrence trigger, so the run will either fire or fail those gates with
real evidence; (3) evidence readiness — the grain is the largest unconsumed one and query-ready off
disk. Per scout-context, treat the prior Signals-read methods (005/006) as hypotheses to re-test for
recurrence, not as a recipe to copy. The cross-signal runner-up is deferred because characterizing
SEC alone first makes the eventual 2x2 honest about each axis's confounds.
