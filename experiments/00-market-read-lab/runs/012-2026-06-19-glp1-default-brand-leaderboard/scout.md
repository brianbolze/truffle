# Scout

## Prior Context Read

- `triage.md`: Active queue. Graduation-decision-ready item **MRL-010** (review/forum *bodies* as a
  source ingredient — 3rd sighting + first actual use in run 011). **MRL-002** (P1, query-recipe layer
  for State/Signals reads — confirmed across 6+ runs). **MRL-008** (P1, captured-signal source-rigor /
  confound convention). **MRL-001** (P2, market-denominator reconciliation convention — *named sources
  checked, inclusion/exclusion rules, known gaps*; flagged that external SERP/listicle panels should be
  *fallback* denominator sources, not the default). MRL-003/005/006/007/009 are lower-priority holds.
- `scout-context.md`: Bias toward **Strategist** questions and **archetypes not yet tried**. Prefer
  questions that (1) a strategist would ask, (2) need evidence the store alone lacks, (3) answerable with
  a light bounded panel, (4) teach Truffle about source ingredients / read shape. Choose `bounded-live`
  when a small public panel materially improves the read. Avoid reusing prior methods as defaults.
- Last 3 `run-notes.md`: **009** longevity positioning whitespace (store-only); **010** GLP-1 offer-ladder
  (store-only, *third* State-read field surface); **011** GLP-1 trust-gap reviews (**first bounded-live**,
  used Trustpilot review bodies, 5 credits, clean — review_after clock 1/3). Run 011's next-run advice:
  re-run the trust-gap shape on a *different cohort* (TRT/longevity) for a 4th MRL-010 sighting.
- Current run artifacts: fresh scaffold only.

## Candidate Questions

| Question | Type | Autonomous eligible? | Evidence mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|
| **C-A. Default-brand / leaderboard read:** Which GLP-1 telehealth brands do third-party "best of 2026" listicles and SERPs repeatedly name as the *default / best*, and how does that named set compare to Truffle's captured GLP-1 universe (19 anchored brands)? | mixed | yes | bounded-live | Untried archetype ("who's considered the default?") + **untried source ingredient** (SERP/listicle as a *named-set* source, vs 011's review bodies). Directly pressures **MRL-001** (membership/denominator) and tests whether a third-party named-set surfaces store gaps or store over-coverage. Strategist-native: "who does the market think leads?" | 3-4 listicle/SERP pages captured with exact URLs + dates; named brands extracted verbatim; set-vs-set comparison to the store cohort. Label affiliate/SEO confound explicitly. | Treating listicle *inclusion* or *order* as objective ranking (it is affiliate/SEO-driven); sprawl beyond a light panel; snippet-grade naming used as evidence. |
| **C-B. Trust-gap on a second cohort:** In TRT / men's-health telehealth, what objections cluster in customer review bodies, and are they answered on owned pages? Does the dominant cluster differ from GLP-1's billing-after-cancel (run 011)? | market | yes | bounded-live | Run 011's explicit next-run advice; a clean **4th MRL-010 sighting** on a *different* cohort tests category-specific vs subscription-wide trust gap, sharpening the human graduation decision. | Trustpilot 1-2★ bodies for 3 TRT brands + 1 forum triangulation; confound siblings (paid-sub/invited) surfaced; "in this sampled panel" language. | Method *reuse as default* (scout-context Avoid) rather than a fresh archetype; prevalence overclaim from a low-star cut. |
| **C-C. Audience / identity ownership:** Across GLP-1 (or TRT), which buyer identity does each brand claim — optimization, shame-free access, clinical seriousness, masculinity, affordability, luxury? Where is an identity underserved? | market | yes | store-only | Strategist seed ("who owns which buyer identity"). Tests whether positioning State (run 009 surface) answers an *identity-map* cut, not just a credibility cut. | `profile.md`/`telehealth.md` positioning + `site_notes` read across the cohort, grouped by claimed identity. | Overlaps run 009's positioning surface; risks repeating method without new system learning. Identity is a Judgment over captured prose — easy to overstate. |
| **C-D. Channel story vs website story:** What do paid ads / affiliates / creator content emphasize for a GLP-1 brand that its owned site does not? | market | no | live-external-needs-approval | Genuinely untried archetype with high strategist value. | Ad-library + affiliate-page capture across several brands — broad, login-ish, sprawl-prone. | Needs a broad, unclear panel (ad libraries, affiliate networks); not a *light* bounded plan — fails the autonomy bar. |
| **C-E. Cheapest-vs-gated benchmark refresh:** Re-quantify the "$X/month ≠ what you pay" pattern (run 010) as a number: what share of headline GLP-1 monthly prices are upfront-÷-N vs med-only-plus-membership vs dose-floor? | market | yes | store-only | Run 010's next-run advice; turns a qualitative finding into a count. | `offerings.md` `site_notes`/Visibility-rule read across 19 brands, classified and counted. | Pure recurrence on the run-010 surface — low new system learning; mostly re-confirms MRL-002. |
| **C-F. Competitor neighborhood:** Who are the 5 closest substitutes/peers for a named GLP-1 brand, by offer shape and audience — and does the store hold them? | mixed | yes | store-only | Tests relation/neighborhood pressure + membership coverage. | Cohort grep + per-brand offer/audience similarity grouping; flag any named peer missing from store. | "Closest" is a Judgment with no captured similarity field; risks thin, hand-waved neighborhoods. |

## Selected Question(s)

1. **C-A — Default-brand / leaderboard read** (selected). Untried archetype *and* untried source
   ingredient (SERP/listicle as a named-set source), bounded-live, directly pressures MRL-001
   (denominator/membership) and keeps the bounded-live convention exercised (review_after clock 1/3 → 2/3).
   Chosen over C-B because scout-context biases toward *untried* archetypes/source-ingredients over
   reusing run 011's review-body method as a default; C-A tests a different source family on a different
   question shape. C-B remains the strongest *next* candidate if a 4th MRL-010 sighting is wanted.

These are Scout recommendations until the operator confirms.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Which GLP-1 telehealth brands do third-party 'best of 2026' listicles and SERPs repeatedly name as the default/best, and how does that third-party named set compare to Truffle's captured GLP-1 universe (the ~19 anchor_category: GLP-1 brands)? Does the comparison reveal store coverage gaps, store over-coverage, or a mismatch between market-default perception and the captured set?"
selected_slug:          glp1-default-brand-leaderboard
run_type:              mixed
autonomous_eligible:   yes
evidence_mode:         bounded-live
expected_denominator: "Store side: the ~19 store domains carrying anchor_category: GLP-1 in telehealth.md (closed, greppable). Third-party side: the union of brands named across 3-4 captured 'best GLP-1 telehealth 2026' listicles/SERP pages — explicitly a partial, affiliate-confounded named set, not a census."
likely_source_panel: "3-4 third-party 'best of' listicle pages + 1-2 SERP queries (e.g. 'best GLP-1 telehealth 2026', 'best online semaglutide'), captured with URLs and dates; compared against a store-only GLP-1 cohort grep."
allowed_sources:
  - "store/ (telehealth.md anchor_category grep; profile.md/offerings.md for any named-but-uncaptured brand check)"
  - "SERP/listicle pages from the bounded-live panel (firecrawl_search + light scrape of 'best of' pages)"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "write-back to store/"
  - "code, schema, or template changes"
  - "durable primitive creation (no stored leaderboard/category object)"
  - "triage graduation"
  - "broad crawling beyond the 3-4 listicle panel"
  - "treating listicle order as an objective ranking"
live_evidence_plan:
  approved_by: Brian
  approval_scope: autonomous Market Read Lab runs
  budget_class: light
  review_after: 3 bounded-live runs
  evidence_goal: "Establish which GLP-1 telehealth brands the third-party 'best of' / SERP surface repeatedly names as default/best, and whether that named set matches, exceeds, or under-covers Truffle's captured GLP-1 universe — testing SERP/listicle as a named-set (membership/denominator) source ingredient."
  source_families_allowed:
    - SERP/listicle ('best GLP-1 telehealth 2026' listicles, comparison pages, SERP result sets)
    - owned/official pages (only to confirm a named brand's identity/domain when ambiguous)
    - local-store (cohort grep + checking whether a named brand is already captured)
  source_families_preferred:
    - SERP/listicle
  source_families_disallowed:
    - login-only or paywalled sources
    - broad crawling beyond the listicle panel
    - private / non-public data
    - ad libraries / affiliate-network dashboards
    - review/forum body mining (that is run 011's surface, out of scope here)
  stop_when:
    - 3-4 listicles + 1-2 SERP queries yield a stable repeatedly-named set (new pages stop adding new top names)
    - the next source would widen into ad libraries, reviews, or a full crawl
    - the remaining uncertainty is a framing judgment (affiliate confound), not a sourcing gap
    - listicles conflict in a way that needs human interpretation
  disallowed_actions:
    - write-back to store/
    - code, schema, or template changes
    - durable primitive creation
    - triage graduation
approval_needed:       no
why_autonomous_safe: "Standing bounded-live policy (budget_class: light); panel is 3-4 public 'best of' pages + 1-2 SERP queries, well inside allowed SERP/listicle families; store comparison is store-only; no write-back, no schema, no graduation. Spend ~3-6 Firecrawl credits, comparable to run 011's 5. Stop rules cap sprawl."
loop1_failure_mode: "Broadening from a light listicle check into open-ended browsing; OR treating listicle inclusion/order as an objective market ranking rather than an affiliate/SEO-confounded named set; OR overclaiming store gaps from a partial third-party panel."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C-A wins on the scout-context bias toward
*untried archetypes and untried source ingredients*: it tests SERP/listicle as a **named-set / membership**
source (new), where run 011 tested review/forum bodies as a **trust** source. It pressures MRL-001's
denominator-reconciliation convention with a concrete fallback-source experiment (the triage note that
external SERP/listicle panels should be *fallback* denominator sources, not default, is exactly the thing
to test). C-B (trust-gap on a second cohort) is held as the strongest follow-up but was deprioritized to
avoid reusing run 011's method as a default this cycle.
