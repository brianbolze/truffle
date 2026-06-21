# Scout

## Prior Context Read

- `triage.md`: MRL-002 (read-recipe family, P1, Acknowledged) now has 8 telehealth read
  surfaces logged; MRL-001 (denominator) and MRL-008 (source-rigor) both Acknowledged
  with the anchored-only / selection-bias / confound flavors mature. Run 027 added a
  `directory-vs-profiled` denominator flavor and a `schema-edge-entity-type` lens.
- `scout-context.md`: select for value + reach + roadmap learning, not store-answerability;
  gap-probes are first-class with a bounded plan; name the builder lens.
- Last 3 `run-notes.md` (025 geo-availability, 026 ownership-consolidation, 027
  cross-vertical taxonomy): 025/026 telehealth-internal; **027 was the first read outside
  the telehealth vertical** — but it audited *classification* (closed-set taxonomy fit),
  not a *market read*. Every MRL-002 read surface (008–026) ran on telehealth.
- Current run artifacts: fresh scaffold (028).

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **[SELECTED] Across the captured SaaS/Technology slice (~24 cos), what is the pricing-visibility + business-model landscape (subscription vs usage-based vs transactional/marketplace; published price vs "contact sales"/enterprise-quote gating; free-tier/trial entry offers) — and can the read recipes that worked on telehealth even run on this substrate?** | calibration (value-read + gap-probe) | yes | store-only | Pricing-model + price-visibility is the lab's most-run reader surface (000, 008); re-running it on a *non-telehealth* cohort is the cleanest possible calibration of whether the MRL-002 recipe family generalizes off-vertical or is telehealth-substrate-bound. "Contact sales" gating is the direct SaaS analog of telehealth intake-gating. | **Recipe generalizability**, the question 027 left open. 027 proved the *closed-set classification taxonomy* isn't telehealth-overfit; it did NOT test whether the *read recipes* (offerings.md `Visibility` column, `telehealth.md` cohort cuts, `anchor_category` grep) generalize. Builder lens: which read-recipe ingredients are universal vs telehealth-only. | Reaches the first non-telehealth *market read*; probes whether `business_model` is a usable primary axis (like `audience` in 020) and whether price-visibility is even capturable without offerings.md. | `business_model` frontmatter verbatim; `pricing`/`offerings.md` presence per co; profile.md Overview/pricing prose; explicit "not found" where price surface is absent. | Importing the telehealth recipe and reporting "no price visibility" when the real finding is *the substrate (offerings.md) is absent for 19/24* — a depth-backfill gap, not a market fact. |
| Across the SaaS slice, what is the entry offer — free tier vs free trial vs demo/contact-sales-gated — and is "free tier" becoming table stakes? | value-read | yes | store-only | Concrete reader value (the freemium-vs-sales-gated wedge is the defining SaaS GTM question). | Tests whether entry-offer structure is capturable off telehealth without offerings.md. | Non-telehealth offer-structure read. | offerings.md / pricing prose per co. | Folds into the selected candidate; standalone it's thinner (overlaps offer-structure run 010). |
| Among the captured non-telehealth companies, which have ≥2 comparable captures or any `signals/`, i.e. is change-pulse even possible off telehealth? | gap-probe | yes | store-only | Tests the least-run design uncertainty (change-pulse, only run 018) on a new slice. | Freshness/temporal-denominator off telehealth. | Reaches the freshness frontier cross-vertical. | `signals/` dir walk + capture-date diff per co. | Run 018 already showed the temporal denominator is tiny (≈6 usable of 135); this is likely a near-empty confirm — low marginal learning. |
| For the 7 `Investor / Holding` allocators (027's structural break), can the store map any portfolio/relation among them or to operating cos? | gap-probe | yes | store-only | Follows 027's one structural finding. | Relation traversal on the entity-type edge. | Reaches relation off telehealth. | `owns`/`parent` frontmatter on allocators. | 026 just mapped ownership and found it dangles 18/21; allocators almost certainly have empty `owns` → near-certain repeat of MRL-006 with no new flavor. |
| Do non-telehealth companies disclose competitors/partners/integrations the store can read as relations? | gap-probe | yes | store-only | Tests relation surfaces off telehealth. | Relation-neighborhood off-vertical. | Reaches relation frontier. | frontmatter relation fields + prose. | High overlap with 026 ownership finding (relations dangle); SaaS "integrations" may be a new flavor but thin without offerings.md. |
| Bounded-live coverage-radar on a non-telehealth category (e.g. "best survey tools 2026") vs the store's survey/feedback cos (typeform, qualtrics, delighted, dovetail...). | gap-probe | yes | bounded-live | Would test selection-bias denominator off telehealth. | Coverage-radar off-vertical. | Reaches selection-bias cross-vertical. | 2 authoritative listicles, cross-source intersection, token-diff. | The coverage-radar recipe is already **named with 3 sightings** (012/022/024); a 4th in a new vertical adds little beyond "it still works" and spends credits — defer in favor of the store-only recipe-generalizability gap, which is the higher-information reach this cycle. |

## Selected Question(s)

1. **Across the captured SaaS/Technology slice, what is the pricing-visibility + business-model landscape, and can the telehealth read recipes even run on this substrate?**

Rationale: this is the natural, higher-information successor to run 027. 027 settled
*taxonomy* generalizability; this settles *read-recipe* generalizability — the other half
of the engine's "universal fields + reusable cuts" claim. It carries real reader value
(SaaS pricing-model/visibility landscape) and a clean builder lens (which read-recipe
ingredients are universal vs telehealth-substrate-bound). Store-only and autonomous-safe.
A bounded-live coverage-radar (candidate 6) is deferred: that recipe is already named
with three sightings, so its marginal learning is lower than the store-only reach here.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured SaaS/Technology slice (~24 companies), what is the pricing-visibility and business-model landscape — business model (subscription vs usage-based vs transactional/marketplace), price visibility (published price vs 'contact sales'/enterprise-quote gating), and entry offer (free tier vs trial vs demo/sales-gated) — and can the read recipes that worked on the telehealth cohort actually run on this substrate?"
selected_slug: saas-pricing-visibility-recipe-generalizability
run_type: mixed
question_mode: calibration
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Store companies whose primary_industry is Technology (~24, profiled). Treat as partial: a directory/industry-grep denominator (per MRL-001 run-027) over-counts stubs and may miss tech-adjacent cos filed under other industries. Count profile.md existence, not directories."
likely_source_panel: "store/<tech-co>/profile.md (business_model, pricing, Overview/pricing prose), store/<tech-co>/offerings.md where present (only ~5 of 24), TAXONOMIES.md for the business_model closed set."
builder_lens: "Read-recipe generalizability off telehealth: which MRL-002 read-recipe ingredients are universal (business_model enum grep, profile.md prose) vs telehealth-substrate-bound (offerings.md `Visibility` column, telehealth.md cohort cuts, anchor_category grep). Tests whether price-visibility is capturable without the telehealth-specific modules."
reach_reason: "First non-telehealth *market read* (027 was a classification audit, not a market read). Probes whether the lab's most-run surface — price-visibility — survives a substrate that lacks the telehealth-only modules every prior read leaned on."
allowed_sources:
  - "store/"
  - "experiments/00-market-read-lab/triage.md"
  - "experiments/00-market-read-lab/discovery-ledger.md"
  - "TAXONOMIES.md"
  - "SCHEMA.md"
disallowed_actions:
  - "No Firecrawl / live web / scraping / SERP."
  - "No store/ mutation or write-back."
  - "No durable primitive / field / category creation."
  - "No triage graduation."
live_evidence_plan: null
approval_needed: no
why_autonomous_safe: "Answerable entirely from local store files and existing lab artifacts; no spend, no live browsing, no write-back."
loop1_failure_mode: "Reporting 'SaaS has no price visibility' when the real finding is that the offerings.md/telehealth.md substrate the telehealth recipe assumes is absent for ~19/24 — a depth-backfill/substrate gap, not a market fact. Must separate 'price is gated' (market State) from 'the store has no price surface captured' (coverage gap), and say 'not found', not 'not there'."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. This run is deliberately a
calibration/gap-probe hybrid: the value-read layer (SaaS pricing-model + visibility +
entry-offer landscape) is real reader value, and the gap-probe layer (does the read
recipe generalize off telehealth?) is the roadmap learning. The contracted failure mode
is the load-bearing guardrail — do not let an absent capture substrate masquerade as a
market finding.
