# Scout

## Prior Context Read

- `triage.md`: Live queue — MRL-002 (query recipes, P1, State *and* Signals reads recurring), MRL-008 (source-rigor/confound, P1), MRL-001 (denominator reconciliation, P2), MRL-003 (depth-backfill altRx/Marque, P2), MRL-009 (write-back receipt section, P2), MRL-005/006/007/010 (P3 holds: relation edge, capture-grain, category-signal anchor, reviews/forums bodies as a source ingredient — MRL-010 now at 2 sightings). Graduation is human-gated; no auto-build.
- `scout-context.md`: Temporary **Strategist-first blind** bias — ask what a senior strategist would want before knowing the system shape; mark source gaps honestly; prefer `store-only` for unattended runs but don't treat it as inherently better; don't reuse prior run methods as defaults (prefer recurrence *tests* over copying).
- Last 3 `run-notes.md` files: **007** SEC-EDGAR funding footprint (Signals); **008** TRT price-visibility (store-only; price-posture tracks **business model, not molecule**; denominator labor was the only toil); **009** longevity/NAD positioning whitespace (store-only; one supply↔diagnostic axis; "longevity clinic" often = hormone-optimization in a longevity coat; **nobody leads with outcome proof**). Both 008 and 009 teed up: test these patterns on a *third* cohort, and quantify the longevity-coat share.
- Current run artifacts: none (fresh scaffold).

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C1. GLP-1 offer ladder & continuity mechanics** — across store GLP-1 brands, what is the entry offer, what gets bundled, and which commitment/continuity terms (upfront multi-month charge, auto-renew cadence, membership floor, buy-first vs intake-gated) are becoming table stakes? | market (offer-packaging) | **yes** | store-only | Strategist-native "what am I really buying / where's the lock-in" read. Exercises a **new `offerings.md` field surface** (bundle structure, billing cadence, what's-included, commitment terms) distinct from the price-Visibility column (000/008) and positioning Notes (009) — tests whether captured State answers an offer-*packaging* question, not just a price-posture one. ~18 GLP-1 brands carry `offerings.md`. | `offerings.md` Roster + `site_notes` per brand: verbatim plan price, billing cadence, bundle composition, what's-included, buy-first/intake-gate flag — all tied to dated captures. | Reading promotional/A/B point-in-time prices as durable; conflating "monthly headline" with the real upfront multi-month charge; treating bundle variants as separate SKUs. |
| C2. ED / sexual-health positioning recurrence test — does 009's "everyone sells mechanism / measurement / access, nobody sells outcome proof" hold in sexual-health? | market (positioning) | yes | store-only | Clean recurrence test of 009's whitespace finding on a third lever. | telehealth.md Notes/Credibility for the 3 dedicated ED anchors + ED lines inside generalists. | Thin dedicated cohort (only 3 `sexual-health` anchors) → denominator-heavy; ED-inside-generalists boundary call dominates. |
| C3. Longevity-coat quantification — across all `longevity/NAD` + `TRT` brands, what share of "longevity"-anchored brands sell Schedule-III testosterone? | market (positioning) | yes | store-only | Sharpens 009's qualitative "longevity coat" tell into a number; combines two well-captured cohorts. | Page-attested Rx/molecule lines per brand, dated. | Risks merely re-confirming 009 rather than learning something new; app-walled Rx grain (gogeviti) caps completeness. |
| C4. Category crowdedness map — across the 54-pack corpus, which verticals lead as a *front door* vs appear only as co-equal grid items? | system-test / market (membership) | yes | store-only | Membership/coverage read; tests `anchor_category` + `multi/none` as a saturation lens. | `anchor_category` frontmatter census + grid-vs-frontdoor note read. | Conflating store-capture bias with real market saturation; `multi/none` swallows nuance. |
| C5. Buyer-identity ownership — which brands own masculinity vs optimization vs shame-free access vs affordability vs luxury vs longevity status? | market (positioning) | yes | store-only | Strategist identity map; reuses `audience` + Notes. | telehealth.md `audience` + positioning Notes per brand. | Overlaps 009's positioning surface; identity labels drift into unanchored Judgment. |
| C6. Channel / access map — cash-pay vs membership vs insurance vs marketplace across the corpus. | market (channel) | yes | store-only | Tests `access_model` frontmatter as a channel lens. | `access_model` frontmatter census + site_notes. | `access_model` grain may be coarse; "membership" means different things across brands. |
| C7. Trust-device benchmark — who earns a skeptical buyer's trust fastest, and what objections stay unhandled? | market (trust) | no | live-external-needs-approval | High strategist value; but the load-bearing half (objections, regret, distrust) needs **review/forum bodies** the store doesn't hold — exactly MRL-010. Surfacing it honestly exposes the recurring source gap. | Review/forum body content (Trustpilot/Reddit) with primary URLs + capture dates — beyond store State; no bounded plan drafted. | Answering the trust half from owned-site copy only → false completeness; this is why it's not autonomous-safe. |

## Selected Question(s)

1. **C1 — GLP-1 offer ladder & continuity mechanics** (recommended; autonomous-safe, store-only, fresh field surface).
2. Runner-up: C4 (category crowdedness map) — cheapest pure membership read if C1's `offerings.md` surface proves too sparse.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the store's GLP-1 cohort, what is the entry offer, what gets bundled, and which commitment/continuity terms (upfront multi-month charge, auto-renew cadence, membership floor, buy-first vs intake-gated) are becoming table stakes — and where is there still real differentiation?"
selected_slug:          glp1-offer-ladder-continuity
run_type:              market
autonomous_eligible:   yes
evidence_mode:         store-only
expected_denominator:  "Store companies with anchor_category: GLP-1 that carry an offerings.md (~18 brands); generalist GLP-1 lines inside multi/none brands inspected as a cross-check, not scored in the core cohort. Treat as a partial denominator, not a census."
likely_source_panel:   "store/<domain>/offerings.md Roster + Visibility + site_notes + Verbatim anchors; store/<domain>/telehealth.md frontmatter (cohort derivation via anchor_category)."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/ (prior run-notes as evidence, not templates)"
disallowed_actions:
  - "no live browsing / WebSearch / Firecrawl spend"
  - "no store/ mutation or write-back"
  - "no durable category/primitive creation"
  - "no triage graduation"
live_evidence_plan: null
approval_needed:       no
why_autonomous_safe:   "Answerable entirely from captured offerings.md + telehealth.md State; no current/news/policy claims; prices read as captured-floor snapshots with dates; no external fetch or spend."
loop1_failure_mode:    "Reading promotional/A-B point-in-time prices as durable; conflating the '$X/month' headline with the real upfront multi-month charge; treating bundle variants as separate SKUs; overstating completeness from a partial denominator."
```

## Selection Notes

- **Decision leverage:** C1 answers the strategist question 008/009 didn't — *offer packaging and continuity lock-in*, the "what would a buyer think they're buying" lens from scout-context. Highest reuse for a real positioning/market-entry call.
- **Evidence readiness:** confirmed during Scout — `brellohealth-com/offerings.md` already carries bundle composition, billing cadence (3-mo upfront, auto-renew every 10 wks), what's-included, and a buy-first disclosure. The surface is there.
- **System-test value:** exercises whether `offerings.md` answers an *offer-structure* read, a surface the lab hasn't probed (000/008 read the Visibility column; 009 read positioning Notes). Likely strengthens MRL-002's "State reads beyond pricing" scope without reusing its exact method.
- **Surprise potential:** continuity mechanics (upfront multi-month charges dressed as "$X/month", auto-renew cadences, mandatory membership floors) are a plausible table-stakes finding a price-visibility read would miss.
- **Why not C3:** tempting (009 teed it up) but risks merely re-confirming the longevity-coat tell rather than learning a new surface.
- **Why C7 is parked:** genuinely the highest-value strategist question, but its trust half needs review/forum bodies (MRL-010, now 2 sightings) — not store-answerable unattended. Logged as `live-external-needs-approval` to keep the source gap visible rather than downgrading it into a false store-only read.
- Treat prior run patterns as hypotheses, not defaults: C1 is deliberately a *new field surface*, not a third price-posture grouping.

**Next step:** `run_status: scout-only` — start Loop 1 in a fresh session against this run after renaming to the selected slug.
