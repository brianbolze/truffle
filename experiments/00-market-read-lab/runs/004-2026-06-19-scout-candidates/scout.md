# Scout

## Prior Context Read

- `triage.md`: live queue is **system pressure, not a question backlog**. Open pressure:
  denominator reconciliation (MRL-001), reusable query ergonomics (MRL-002), in-cohort
  module gaps (MRL-003), named-counterparty edge + capture grain (MRL-005/006), category-scoped
  exogenous signals (MRL-007), minimal-monitor source rigor (MRL-008), and a standard
  "write-back candidates" section (MRL-009). All held for recurrence; none graduated.
- `scout-context.md`: lead with **plain operator questions**, annotate the system lesson second.
  Go wide on basic archetypes (competitors, current change, crowded categories, pricing,
  offer map, claims, channels, backend, reputation) before narrow recurrence probes. Prefer
  store-only + autonomous-safe for unattended Loop 1.
- Last 3 completed `run-notes.md`:
  - **Run 000 (GLP-1 pricing visibility):** store-only; the store *out-completed* the external
    Notion seed. `Visibility` column is the workhorse for any publish-vs-gate read. Membership
    by `anchor_category` + `value_chain_role`, never raw grep. No new State primitive.
  - **Run 001 (men's-health backend relations):** store-only; parent/ownership already captured
    (`parent`/`owns`); named pharmacy/clinical counterparties too sparse (5/18, 3/18) to typecast.
  - **Run 002 (GLP-1 news monitoring):** external panel load-bearing for *event/freshness*
    questions, but snippets are leads, not evidence. External/current claims need primary URLs +
    capture dates.
- Store census (today): 126 profiles, 54 `telehealth.md` packs, 66 `offerings.md` rosters.
  Telehealth is the deep captured cohort; the rest (watches, energy, SaaS, VC) are sparse.
- Run 003 was a prior Scout-only slate (same slug) that left recommendations open and never
  filled a Selected Run Contract. Mined as a hypothesis source, not copied.

## Candidate Questions

Wide slate of basic archetypes first; the two cleanest store-only picks are recommended below.

| Question | Type | autonomous_eligible | evidence_mode | Why this is worth a run | Trustworthy evidence would require | Failure mode to watch |
|---|---|---:|---|---|---|---|
| Across the captured telehealth store, which product/condition categories are most crowded (most distinct DTC brands competing) and which are thin? | market | yes | store-only | Canonical market-map question a strategist/investor would open with; turns offering rosters + cohort cuts into a category-density view. Tests denominator-build and category grouping with no spend — directly exercises MRL-001/002 pressure. | `telehealth.md` `anchor_category`/categories-served + `offerings.md` roster rows; count **distinct DTC brands** per category gated by `value_chain_role == DTC`; suppliers/infra excluded; "store coverage is a floor" caveat. | Counting SKUs instead of brands; letting pharmacies/infra inflate a category; reading store under-capture as market thinness. |
| Generalize Run 000: across all captured cash-pay categories (not just GLP-1), which are most price-transparent vs most intake-gated? | mixed | yes | store-only | High reuse pressure — proves whether `Visibility` works as a *cross-category* query surface, not a GLP-1 fluke. Operator-recognizable pricing benchmark. | Per-category denominators; `offerings.md` `Visibility` tokens; both brand-weighted and SKU-weighted cuts; clean handling of "branded-retail, brand doesn't set price" vs "brand hides its own price." | Re-running GLP-1 narrowly; conflating not-priced-by-brand with hidden; per-SKU split masking brand-level reality. |
| Who are Hims & Hers' closest true competitors vs adjacent peers across its category footprint? | market | yes | store-only | Clean company-neighborhood archetype on the store's most multi-category brand; tests how Truffle assembles a "competitor set" from audience/category/offer/parent overlap without one universal competitor relation. | Hims profile + offerings/telehealth; comparable multi-category and single-category brands in store; explicit true-substitute vs adjacent criteria. | Generic "other telehealth brands" list; treating category overlap as full substitutability; ignoring single-vertical specialists. |
| Which parent companies/platforms operate multiple front-door brands across health categories (storefront names that hide a rollup)? | market | yes | store-only | Basic market-structure read on fields already proven (`parent`/`owns`); useful for competitor maps where rollups hide behind distinct storefronts. | `profile.md` `parent`/`owns` frontmatter; per-brand category tags; clear ownership vs partnership vs shared-infra distinction. | Collapsing distinct brand strategies into one parent-competitor; overbuilding relation machinery from a simple rollup view. |
| Which cash-pay telehealth products are commonly bundled (TRT, ED, hair, peptides, GLP-1, labs, coaching, supplements) vs sold standalone? | market | yes | store-only | Offer-map question useful for product strategy; pressures whether roster rows can reveal bundles vs standalone SKUs. | `offerings.md` rows + package/bundle prose in telehealth/profile captures; category-normalized product groups. | Treating separate SKUs as intentional bundles; missing bundles described only in prose. |
| Which men's-health / hormone telehealth brands lead with price vs outcomes vs trust/medical-legitimacy vs convenience vs identity? | market | yes | store-only | Straightforward positioning map for a known cohort; tests whether captured page prose supports claim/positioning comparison without new fields. | Profile/telehealth captured claims for a bounded cohort; headline/value-prop evidence per brand. | Turning subjective positioning into false precision; ignoring capture-date/page-depth differences. |
| What changed recently across the major model providers (Claude / OpenAI / Google) — notable launches or announcements this week? | market | no | live-external-needs-approval | Pure current-change-watch archetype an operator asks pre-planning-meeting; deliberately a non-store freshness test. | Approval for live research; official provider pages first, then reputable secondary; exact URLs, dates, source type, snippet-vs-fetched status. | Answering from stale memory/snippets; drifting into broad AI news vs "this week" releases. |
| What do customers complain about most in GLP-1 / men's-health telehealth: price, access, side effects, support, refills, trust, cancellation? | market | no | live-external-needs-approval | Basic reputation/pain archetype; genuinely useful but needs external review/forum surfaces + the unbuilt source-rigor convention (MRL-008). | Approval for live review/forum research; defined source panel; exact URLs + capture dates + source type; small coded complaint sample. | Treating review samples as representative; over-indexing on angry outliers; unattributed snippets. |
| Re-test Run 000's 33/42/25 GLP-1 visibility split directly against current store captures — has it drifted? | system-test | yes | store-only | Cheap reproducibility probe Run 002 explicitly recommended (it only stressed price/legality, not the publish-vs-gate split). Tests whether a store-only read is stable across re-runs. | Same `offerings.md` GLP-1 roster + `Visibility` tokens; same denominator recipe; diff against Run 000's receipt. | Re-deriving the denominator differently and attributing the delta to drift rather than method. |
| Which telehealth categories look least crowded but strategically adjacent to crowded ones (whitespace, store-floor only)? | mixed | yes | store-only | Simple whitespace question; not "build a category ontology," just low density relative to adjacent high density. | Store category counts; adjacency criteria (shared buyer, treatment pathway, molecule/form, brand overlap); explicit "store coverage is a floor" caveat. | Mistaking under-capture for whitespace; opportunity claims without an external denominator. |

## Selected Question(s)

1. **Across the captured telehealth store, which product/condition categories are most crowded
   (most distinct DTC brands competing) and which are thin?** — recommended for Loop 1.
2. Generalize Run 000: across all captured cash-pay categories, which are most price-transparent
   vs most intake-gated? — strong store-only alternative.

These are Scout recommendations; the contract below selects #1 for the unattended Loop 1.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across the captured telehealth store, which product/condition categories are most crowded (most distinct DTC brands competing) and which are thin?"
run_type: market
autonomous_eligible: yes
evidence_mode: store-only
expected_denominator: "Distinct DTC telehealth brands in the store, derived from telehealth.md anchor_category / categories-served unioned with offerings.md roster product categories, gated by value_chain_role == DTC brand. Suppliers (compounding pharmacies), white-label infra, and out-of-cohort profiles excluded. ~54 telehealth packs / 66 offerings rosters are the working set; report it as a captured-floor, not a market census."
likely_source_panel: "None. Internal store only: store/*/telehealth.md (anchor_category + categories-served), store/*/offerings.md (## Roster rows), store/*/profile.md frontmatter (value_chain_role, audience, parent/owns). scripts/store.py resolve only if name reconciliation is needed."
allowed_sources:
  - store/*/telehealth.md
  - store/*/offerings.md
  - store/*/profile.md
  - scripts/store.py
  - QUERYING.md
disallowed_actions:
  - live browsing / WebSearch / Firecrawl scrape or crawl (no spend)
  - writing to store/
  - creating durable category/cohort objects or other engine primitives
  - writing back to Notion or any project KB
  - filling read.md / review files / triage.md (Loop 1 owns read.md only)
approval_needed: no
why_autonomous_safe: "Answerable entirely by grouping existing store evidence (category-density is a query-time count over captured cuts). No live spend, no external claims, no current/news/pricing/policy assertions, no primitive creation. Exercises the open MRL-001/002 denominator + query-ergonomics pressure without touching anything mutable."
loop1_failure_mode: "Counting SKUs instead of distinct brands; letting compounding pharmacies / white-label infra inflate a category; treating store under-capture as genuine market thinness. Mitigation: count distinct DTC brands per category, gate by value_chain_role, and state 'captured floor, not census' on every density claim. Absence language must say 'not captured', not 'not offered'."
```

## Selection Notes

Decision leverage + evidence readiness pick #1: category-density is the most recognizable
market-map question a strategist/investor opens with, and it is fully store-answerable today.
It also lands squarely on the lab's two most-cited open pressures (denominator reconciliation,
query ergonomics) without any spend or mutation — so it is both a useful operator read and a
clean system test.

#2 (cross-category price transparency) is the highest *reuse-pressure* pick: it directly tests
whether Run 000's `Visibility` workhorse generalizes beyond GLP-1. Held as the alternative
rather than the primary because it is closer to a re-run of Run 000's method; #1 is fresher.

The two live-external candidates (model-provider change-watch, customer-complaint reputation)
are deliberately included to keep the freshness/reputation archetypes on the slate, but both are
`approval_needed` and must not be selected for unattended Loop 1 without Brian's sign-off.

Prior run patterns are treated as hypotheses: #1 will test whether the "denominator build is the
expensive part" friction from Runs 000/001 recurs a third time — which would strengthen MRL-002
toward a query helper rather than re-deciding it from one sighting.
