# Scout

## Prior Context Read

- `triage.md`: Open queue is dominated by two acknowledged P1 conventions — MRL-002 (query
  recipes for State *and* Signals reads) and MRL-008 (captured-signal source-rigor / confound
  rule). MRL-001 (denominator reconciliation) and MRL-003 (depth-backfill: altRx, Marque) sit at
  P2. Relation items MRL-005/006 are held for a backend-naming-dense cohort. MRL-007 (homeless
  category-level signal) is held pending recurrence. Graduation is human-gated.
- `scout-context.md`: Go *wide* on basic operator archetypes before narrow pressure probes.
  Prefer store-only for unattended Loop 1. System learning is the second layer, not the headline.
  Avoid false completeness from a partial denominator; don't turn a query-time grouping into a
  durable category.
- Last 3 `run-notes.md` (005/006/007): All three were **Signals** reads (Trustpilot, Wayback,
  SEC-EDGAR). Each repeated the same raw "latest-per-dir + field-extract + confound-sibling"
  loop, which is what pushed MRL-002 and MRL-008 to Acknowledged. None touched the **State** layer
  or the **visual** module. A State read is the natural next swing of the pendulum.
- Current run artifacts: fresh scaffold, nothing to resume.

Store census (read for grounding, not a claim): 126 `profile.md`, 66 `offerings.md`,
54 `telehealth.md`, 44 `visual.md`, 49 with `signals/`. Telehealth is the deepest cohort
(GLP-1, men's-health/TRT/hormone, longevity); also watches, aero, VC, SaaS.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| In the men's-health / TRT / hormone telehealth cohort, who **publishes price** vs gates it behind intake, and what offer structures (membership, labs-included, compounded vs brand) are table stakes? | market | yes | store-only | Direct recurrence test of run 000's GLP-1 price-visibility pattern on a *different, already-enumerated* cohort (run 001 mapped these brands). Tells a strategist where price is a weapon vs a secret outside GLP-1. | `offerings.md` / `telehealth.md` per brand with captured pricing fields; explicit "price not shown / intake-gated" where absent; capture clocks surfaced. | Reading "no price in store" as "price hidden by company" when it's a capture gap. Partial cohort denominator. |
| Across the telehealth corpus, **who leads with what** — price, clinical outcomes, trust/safety, convenience, or identity — and which positioning is crowded vs rare? | market | yes | store-only | Classic positioning map a strategist recognizes; tests whether `profile.md`/`telehealth.md` carry claims at a grain you can group without re-browsing. | Verbatim positioning language per brand from captured pages, tagged to a small claim-axis set; judgments labeled. | Soft "vibes" synthesis that crosses from State into unlabeled Judgment; over-reading marketing copy. |
| Which **offer / product areas are most saturated** across the `offerings.md` corpus (GLP-1, sermorelin/peptides, testosterone, NAD+, ED, hair)? | market | yes | store-only | Crowdedness read names where the field is a commodity vs thin; feeds where differentiation is hard. | A grouping pass over `offerings.md` rosters with per-area brand counts; denominator named as partial. | Treating a query-time grouping as a durable category (scout-context anti-pattern). |
| Who are henrymeds' (or hims') **closest competitors / substitutes** purely from what the store already holds — overlapping offers, cohort, price band? | market | yes | store-only | Company-neighborhood archetype; tests whether relation/peer reads are answerable from State alone or need the `exa_similar` signal. | Offer + cohort overlap from `offerings.md`/`telehealth.md`; any `signals/exa_similar` used as a *lead*, not proof. | Asserting "closest competitor" as fact from store overlap; only 2 brands have `exa_similar`. |
| First-ever consumption of the **visual layer**: across the 44 `visual.md` companies, what brand-impression archetypes cluster, and is the visual evidence judgment-ready as an ingredient? | mixed | yes | store-only | No run has read `visual.md`. Tests whether that module produces reusable ingredients or just opinions, and where its State/Judgment line sits. | The blind cards + "Visual & brand impression" lines already in `visual.md`; treat impressions as labeled Judgments. | Producing broad brand opinions (scout-context "Avoid"); mistaking impression for measurable State. |
| Corpus census: of 126 profiles, **which cohorts are deep vs thin** on the module cuts (telehealth/offerings/visual/signals) a market read needs? | system-test | yes | store-only | Names denominator/coverage health before the next reads over-claim completeness; directly serves MRL-001/MRL-003. | A file-presence census per cohort with explicit gaps; framed as corpus-health, not a new primitive. | Census theater — counting files without saying what it blocks. |
| In the **compounding-heavy GLP-1** cohort, do brands name their **pharmacy / clinical backend** densely enough to join as a relation edge? | market | partly | store-only | The exact "backend-naming-dense cohort" MRL-005/006 are *held for*. A clean recurrence test, not a new build. | `telehealth.md` bodies + frontmatter for named counterparties; explicit absence; no possessive-language entities. | Re-litigating MRL-005 without new evidence; contaminated possessive claims ("our pharmacy"). |
| What **launched or changed** in GLP-1 telehealth in the last ~30 days (offers, pricing, entrants)? | market | no | live-external-needs-approval | Current-change archetype; would expose a freshness/monitoring source ingredient. | Primary URLs, capture dates, source grade per event (snippets are leads only). | Snippet-grade evidence treated as decision-grade; needs approval + spend. |

## Selected Question(s)

1. **Primary (selected):** In the men's-health / TRT / hormone telehealth cohort, who publishes
   price vs gates it behind intake, and what offer structures are table stakes? *(store-only,
   autonomous-safe)*
2. **Secondary (not run):** Telehealth positioning map — who leads with price / outcomes / trust /
   convenience / identity. Hold as the next State read if the price-visibility recurrence is thin.

Rationale: 005/006/007 were all Signals reads, so a State read rebalances coverage. The TRT/hormone
cohort is *already enumerated* (run 001's men-led/hormone brands), which removes most denominator-
build cost and makes this a sharp recurrence test of run 000's price-visibility pattern on a
different category — exactly the "does the same pressure recur?" probe the lab wants, with
falsifiable `offerings.md` evidence and a small judgment surface. The visual-layer and positioning
candidates are more novel but lean judgment-soft; they're better once a clean State recurrence is
banked.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "In the men's-health / TRT / hormone telehealth cohort already in the store, which brands publish price vs gate it behind intake, and what offer structures (membership, labs-included, compounded vs brand) are becoming table stakes?"
selected_slug: trt-mens-health-price-visibility
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store companies whose profile.md/telehealth.md place them in the men's-health / TRT / hormone-optimization cohort (run 001 enumerated a men-led/hormone set; treat as a partial seed, re-derive from store, do not assume complete)."
likely_source_panel: "store/<domain>/offerings.md and telehealth.md for pricing + offer structure; profile.md for cohort membership; signals/ only as dated context, never as the price source."
allowed_sources:
  - "store/ (offerings.md, telehealth.md, profile.md, and signals/ as dated context only)"
  - "experiments/00-market-read-lab/ (triage.md, scout-context.md, prior run-notes as evidence)"
disallowed_actions:
  - "live browsing / Firecrawl / any external fetch"
  - "store/ mutation or write-back"
  - "treating absence of a captured price as company-gated pricing"
  - "presenting a partial cohort denominator as complete"
  - "durable category/primitive creation or triage graduation"
approval_needed: no
why_autonomous_safe: "Fully answerable from already-captured local store files; the cohort is pre-enumerated; no current/news/policy claims, no spend, no mutation. Price-visibility is captured STATE, not a live signal."
loop1_failure_mode: "Overstating completeness from a partial denominator, or conflating 'price not in our capture' with 'price hidden by the company' — must distinguish capture-gap from intake-gating explicitly."
```

## Selection Notes

- **Decision leverage:** A strategist gets a same-question read on a second cohort — does price
  transparency behave like GLP-1 or differently? That comparison is the payoff.
- **Evidence readiness:** High. `offerings.md` exists for 66 brands; the TRT/hormone cohort is
  well represented (marek, hone, maximus, trtnation, hormonemd, malemd, defy, etc.).
- **Freshness pressure:** Low — price-visibility is durable State; capture clocks should still be
  surfaced so a stale capture is visible.
- **Reuse pressure:** Likely fires MRL-002 (a *State* price-grouping recipe) and MRL-001
  (denominator naming). This is a recurrence test, not a new convention.
- **Surprise potential:** Whether the price-gate split inverts outside GLP-1 (TRT/labs may gate
  more by clinical necessity) is a genuine unknown.
- **System-test value:** Tests the capture-gap vs intake-gate distinction — the load-bearing
  honesty move for any price-visibility read.
- **Artifact pressure:** Low; no new template needed.

Prior price-visibility method (run 000) is a hypothesis here, not a default — Loop 1 should
re-derive the cohort and the capture-gap/intake-gate split from scratch rather than porting 000's
exact table.
