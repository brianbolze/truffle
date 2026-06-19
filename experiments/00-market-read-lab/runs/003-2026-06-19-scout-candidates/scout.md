# Scout

## Prior Context Read

- `triage.md`: live queue is system pressure, not a question backlog. Open pressure
  includes denominator reconciliation, query ergonomics, module gaps, named counterparties,
  category-scoped external signals, source-rigor, and surfacing write-back candidates.
- `scout-context.md`: updated calibration is to start with normal operator questions and
  only then annotate what each teaches Truffle. Go wide on basic question archetypes before
  narrow recurrence probes.
- Last 3 completed `run-notes.md` files:
  - Run 000: GLP-1 pricing visibility worked store-only, but denominator building and
    membership cleanup were awkward. Store data beat the external Notion seed.
  - Run 001: relation questions were useful, but parent/ownership is already captured and
    named pharmacy/clinical counterparties were sparse.
  - Run 002: freshness/event questions need external source panels, but snippets are leads,
    not evidence.
- Current run artifacts, if resuming: Run 003 Scout was recalibrated from a system-pressure
  slate to a broader basic-question slate. No target receipts found.

## Candidate Questions

| Question | Type | autonomous_eligible | evidence_mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---:|---|---|---|---|
| Who are Hone Health's closest competitors, and which are true substitutes vs adjacent peers? | market | yes | store-only | Straightforward company-neighborhood question; useful to a strategist and pressures how Truffle builds competitor sets from audience, category, offers, claims, and parent/partner context. | Hone profile/telehealth/offering data; comparable men's health, TRT, longevity, sexual-health, and hormone-care brands in the store; explicit criteria for true competitor vs adjacent peer. | Producing a generic list of men's health brands without explaining the basis of similarity; treating category overlap as full substitutability. |
| In compounded Rx telehealth, which product categories are most crowded? | market | yes | store-only | Simple market-map question that turns the store's offering rosters into a category-density view. Good test of category/cohort grouping without live spend. | Store `offerings.md` rows and `telehealth.md` anchor/category fields for compounded-Rx sellers; count by product/condition category; exclusions for suppliers/infra; caveats for missing modules. | Counting every SKU as equal market presence; mixing DTC brands, pharmacies, and infrastructure providers; overstating completeness. |
| Which cash-pay telehealth categories are most price-transparent vs most intake-gated? | mixed | yes | store-only | Practical benchmark that generalizes Run 000 beyond GLP-1 while staying readable to an operator. Also tests whether `Visibility` works as a cross-category query surface. | Category denominators; `offerings.md` `Visibility` values; brand-weighted and SKU-weighted cuts; clear handling of partial/branded-retail rows. | Re-running GLP-1 too narrowly; confusing "brand does not set retail price" with "brand hides its own price." |
| Any new releases or notable announcements from Claude or OpenAI this week? | market | no | live-external-needs-approval | Basic current-change watch archetype. It intentionally tests a non-store, freshness-heavy question like an operator might ask before a planning meeting. | Approval for live external research; official Anthropic/OpenAI pages first, then reputable secondary coverage; exact URLs, dates, source type, and snippet-vs-fetched status. | Answering from stale memory or snippets; drifting into broad AI news instead of "this week" release/announcement evidence. |
| Which men's health telehealth brands lead with price, outcomes, trust/medical legitimacy, convenience, or identity? | market | yes | store-only | Straightforward positioning map for a known cohort. It tests whether profile and page-capture prose can support claim/positioning comparisons without inventing new fields. | Store profile/telehealth summaries and captured claims; a bounded men's health cohort; examples of headline/value-prop evidence by brand. | Turning subjective positioning into false precision; ignoring capture-date differences or page-depth differences. |
| Which products are commonly bundled together in cash-pay telehealth: TRT, ED meds, hair loss, peptides, GLP-1, labs, coaching, or supplements? | market | yes | store-only | Offer-map question that is easy to understand and useful for product strategy. It pressures whether offering rows can reveal bundles vs standalone SKUs. | `offerings.md` roster rows; package/bundle descriptions in telehealth/profile captures; category-normalized product groups. | Treating separate SKUs as intentional bundles; missing bundles described only in prose. |
| Which telehealth brands depend on the same pharmacies, provider groups, parents, or infrastructure platforms? | mixed | yes | store-only | Basic backend-dependency question, expressed in operator language rather than relation-primitive language. It can still test named-counterparty recurrence. | Parent/owns frontmatter; `telehealth.md` Fulfillment/Provider lines; named counterparty grep; separation of named vs generic/unnamed relationships. | Reading "our pharmacy/providers" as a named dependency; implying absence when the brand simply does not publish the counterparty. |
| What are customers complaining about most in GLP-1 or men's health telehealth: price, access, side effects, support, refills, trust, or cancellation? | market | no | live-external-needs-approval | Basic reputation/pain question. Useful market read, but it needs external review/forum surfaces and a source-rigor convention. | Approval for live external review/forum research; defined source panel; exact URLs and capture dates; source type; small coded complaint sample. | Treating review samples as representative; over-indexing on angry outliers; using unattributed snippets. |
| Which telehealth categories look least crowded but strategically adjacent to crowded ones? | mixed | yes | store-only | Simple whitespace question: not "build a category ontology," just ask where offer density is low relative to adjacent high-density categories. | Store category counts; adjacency criteria such as shared buyer, treatment pathway, molecule/form factor, or brand overlap; explicit caveat that store coverage is a floor. | Mistaking store under-capture for market whitespace; making opportunity claims without external denominator checks. |
| Which parent companies or platforms operate multiple front-door brands across health categories? | market | yes | store-only | Basic market-structure question using fields already shown to work. Useful for competitor maps where storefront names hide rollups. | `profile.md` parent/owns frontmatter; category tags and offer rows for each brand; clear distinction between ownership, partnership, and shared infrastructure. | Collapsing distinct brand strategies into one parent-level competitor; overbuilding relation machinery from a simple rollup view. |

## Selected Question(s)

1. Who are Hone Health's closest competitors, and which are true substitutes vs adjacent peers?
2. In compounded Rx telehealth, which product categories are most crowded?

These are Scout recommendations until Brian or the operator confirms one.

## Selection Notes

These are intentionally basic. They are still useful system tests, but the operator-facing question
comes first.

Question 1 is the cleanest company-neighborhood starter: concrete company, recognizable output,
store-only evidence, and a good test of how Truffle handles "competitor" without pretending there is
one universal competitor relation.

Question 2 is the cleanest category-density starter: simple, store-only, and likely to surface the
membership/counting caveats that matter without dragging the run into live external source work.

There is no shared question queue yet. Candidate questions live in Scout files; `triage.md` remains
for system pressure only. Operator should choose or refine one question, then start Loop 1 in a
fresh session.
