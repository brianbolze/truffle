# Scout

## Prior Context Read

- `triage.md`: 9 live items. The relations cluster (**MRL-005** named-counterparty edge,
  **MRL-006** capture-grain gap) is parked at P3 awaiting a recurrence test *outside*
  compounded GLP-1. **MRL-002** (State-read query recipe) is `Acknowledged` and
  **saturated at recipe level** across 5 single-cohort + 1 cross-cohort State surfaces —
  another single-cohort price/offer/positioning read adds nothing. **MRL-010**
  (reviews/forums bodies) already crossed its 3rd-sighting bar (run 011) and is
  graduation-decision-ready — do not re-run. **MRL-008** (signal confounds) matured over
  Trustpilot/Wayback/SEC.
- `scout-context.md`: two-test selection (value + design); persist runs not ontology;
  store-only when cached State is genuinely enough; avoid candidates that *merely execute*
  a parked next step (triage annotates, it does not originate).
- Last 3 `run-notes.md` (013, 014, 015): 013 = sexual-health access map; 014 = GLP-1
  backend-counterparty (found OpenLoop Health behind 2 brands — first joinable cross-brand
  edge); 015 = first cross-cohort read (table-stakes ⇒ poor durable-State candidate).
  **Both 014 and 015 explicitly name the same highest-value next test: run the relation
  read on a non-GLP-1 cohort to decide whether shared-clinical-backend concentration is a
  GLP-1-compounding artifact or a telehealth-wide market structure.** That is the open
  design edge (relations/neighborhood) with no store-frontmatter support yet.
- `question_history.py` map: 000–015. Saturated shapes = single-cohort State price/offer
  reads (008/009/010/013), per-domain Signals reads (005/006/007). Under-tested =
  relations beyond GLP-1, persistence-boundary hardening, cross-cohort axes.

## Candidate Questions

| # | Question | Type | Auton.? | Evidence mode | Why worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|
| C1 | Outside compounded GLP-1, do DTC telehealth brands share **named** clinical-provider or pharmacy backends — i.e., is the OpenLoop-style backend concentration a GLP-1 artifact or a telehealth-wide market structure? | mixed | yes | store-only | Decides (not just reinforces) the parked MRL-005/006 relations question; real reader value as a cross-market backend-dependency map | Per-brand `parent`/`owns` frontmatter + `telehealth.md` Fulfillment/Clinical prose across the ~35 non-GLP-1 structured brands; every named entity resolved against `store/` | Possessive "our pharmacy" prose read as a named entity (run-001 trap); calling 2-brand recurrence "concentration" |
| C2 | Across all cohorts, which offer mechanics actually **differ** (high-entropy, cohort-distinguishing) vs are universal table-stakes — i.e., which cuts would make *useful* durable-State filters? | system-test | yes | store-only | Hardens run-015's persistence-boundary heuristic (near-constant ⇒ don't store) by testing its *other* side on a different field family | `telehealth.md` enum fields across 54 brands; entropy/variance per field per cohort | Re-running 015's shape; mistaking sampling sparsity for low entropy |
| C3 | In the captured store, which cohorts carry the **stalest** capture clocks, and does any prior lab read rest on State old enough to plausibly mislead today? | system-test | yes | store-only | Tests the "trust the cache over time" value job, never the primary subject; freshness has only ever been a watch tag | `captured_at`/store-clock frontmatter across cohorts; map against load-bearing claims in runs 008–015 | Treating clock age as truth-decay without a change mechanism; meta-navel-gazing with no market read |
| C4 | Across cohorts, which brands publish a **named 503A/503B compounding pharmacy** vs route to an unnamed "partner pharmacy," and does any 503B recur across brands (supply concentration)? | mixed | yes | store-only | Sharper supply-side cut of C1; 503B recurrence would be a genuine concentration signal | `telehealth.md` Fulfillment prose; entity-resolution of each named pharmacy against `store/` | Pharmacy names dangle (no profiles) → un-joinable, as run 014 found; thin yield |
| C5 | In the TRT/hormone cohort, what positioning wedge does each brand anchor on (TRT-replacement vs enclomiphene-reboot vs concierge-longevity vs labs-first), and where is the whitespace? | market | yes | store-only | Reader-valued whitespace map | `anchor_category`/`Credibility`/`Notes` per TRT brand | Re-runs run-009 positioning shape on a new cohort; MRL-002 already saturated |
| C6 | Which captured brands' Trustpilot **score** most diverges from what their review **bodies** say, and does the gap track invitation/paid-profile posture? | market | no | bounded-live | High reader value (trust map) | Trustpilot bodies for divergent brands | Duplicates MRL-010/run-011, already graduation-ready; bounded-live spend not needed when store-only candidates win |

## Selected Question(s)

1. **C1** — non-GLP-1 backend-relation read. Best value+design combination: store-only and
   autonomous-safe; directly answers a question two consecutive runs flagged as the
   highest-value next test; can *close* (not just reinforce) the parked MRL-005/006 relations
   decision; reader-valued as a cross-market backend-dependency map.

Rejected: C2/C5 are MRL-002-saturated shape risk; C3 is meta with weak market value; C4 is a
narrower slice of C1 (fold pharmacy-vs-clinical *into* C1); C6 duplicates graduation-ready
MRL-010 and needs spend.

## Selected Run Contract

```yaml
selected_question: "Outside compounded GLP-1, do DTC telehealth brands share named clinical-provider or pharmacy backends — is the OpenLoop-style backend concentration a GLP-1-compounding artifact or a telehealth-wide market structure?"
selected_slug:          non-glp1-backend-relations
run_type:               mixed
autonomous_eligible:    yes
evidence_mode:          store-only
expected_denominator:   "The ~35 non-GLP-1 brands with structured telehealth.md (TRT 8, longevity/NAD 8, multi/none 10, sexual-health 3, peptides 2, singletons). Partial: anchor-only grep under-counts offerers (MRL-001); a brand can use a backend without naming it. Report as a floor."
likely_source_panel:    "store/*/telehealth.md (Fulfillment + Clinical-entity prose), store/*/profile.md (parent/owns/pharmacy_model/value_chain_role frontmatter), ls store/* for entity resolution."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
disallowed_actions:
  - "live browsing / WebSearch / Firecrawl"
  - "any spend"
  - "store/ mutation or write-back"
  - "creating a durable relation edge, table, or frontmatter field"
  - "treating possessive 'our pharmacy' language as a named entity"
  - "calling a 2-brand co-occurrence 'concentration'"
live_evidence_plan: null
approval_needed:        no
why_autonomous_safe:    "Answerable entirely from already-captured store files + lab artifacts; no live evidence, no spend, no write-back. Mirrors the safe store-only shape of runs 013/014/015."
loop1_failure_mode:     "Overstating concentration from sparse co-occurrence; mistaking unnamed/possessive backends for absence-of-relationship; counting anchored-only brands as the full denominator."
```

## Selection Notes

C1 carries reader value in its own right (a backend-dependency map a strategist would
recognize), so it is not *merely* executing a triage next-step — triage only sharpened its
evidence bar (named-vs-possessive guard, floor framing, anchored-only caveat). The design
payoff is decisive: a non-GLP-1 recurrence of a shared clinical/pharmacy backend would move
MRL-005 toward graduation; broad *absence* would help *close* it as a GLP-1-compounding
artifact. Either outcome advances a parked decision rather than re-confirming a saturated one.
