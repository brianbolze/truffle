# Scout

## Prior Context Read

- `learning/lessons.md` / `learning/observations.md` (context, not a question queue):
  L001 (coverage-radar recipe) **graduated** — but all three source runs (012/022/024)
  were telehealth verticals, so its generalizability to non-telehealth, fuzzy-boundary
  categories is untested. L004 (denominator reconciliation travels with the read), L005
  (query-time grouping; structured-absence ≠ market-absence), L006 (price-visibility
  token scope) all live and saturated. Recurring observation frontiers: cohort-draw /
  `denominator-reconciliation` (n≥5, industry-draw is not a cohort key), single-valued
  `business_model` lossiness, horizontal-relation absence (`relation-pressure`), traction
  level-vs-delta (`traction-readiness`), and the "value lands on builder/Pantry not buyer"
  CR1 frontier (038/039/041/047, partially broken by 043/044 buyer-reads).
- `scout-context.md`: two-test selection (value/reach + design); gap-probes first-class
  with a bounded plan; do not pick store-only because it is easy; name the builder lens.
- Last 3 `run-notes.md` files (050 services-bucket overload, 051 cold-start reliability,
  052 price-freshness decay): all recently exercised schema-fit, cold-start, and
  freshness; the **boundary / membership** design uncertainty (who belongs / who is
  missing) has not been read since the L001 telehealth runs, and never on a consumer
  cohort.
- Current run artifacts: fresh scaffold, temporary slug `scout-candidates`.

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (recommended).** For a buyer choosing a wearable / sleep / recovery tracker, which category members do third-party "best of 2026" listicles + SERPs repeatedly name, and which of those does Truffle's store NOT have captured at all? Does the **graduated L001 coverage-radar recipe** (SERP → ≥2 listicles → token-match store diff) hold on a fuzzy-boundary consumer-hardware category, or does category-boundary blur (smart ring vs smartwatch vs recovery band vs sleep system) break the cross-source intersection? | gap-probe | yes | bounded-live | Real buyer value ("what am I missing"); first test of L001 outside telehealth; the store visibly holds only ~9 of the category (oura/whoop/eightsleep/peloton/apple/therabody/hyperice/nike/casio) and is missing obvious members (Garmin, Fitbit/Google, Samsung, Withings, Ultrahuman, Polar, Coros, Amazfit). | **Boundary / membership.** Tests whether L001's recipe generalizes to a category whose listicle boundary is fuzzier than a crisp telehealth vertical; tests the persistence boundary (membership stays query-time vs earns a stored set). | Reaches past the cached answer to an external named-set the store can be diffed against; probes whether category fuzziness degrades the token-match diff. | 1 SERP query + ≥2 independent editorial listicles (Wirecutter/Tom's Guide/CNET/Verge-class), cross-source intersection, exact URLs + capture dates + source grade; plain-markdown scrapes only. | Category blur inflates the "missing" set with adjacencies (general smartwatches) that aren't true cohort members; vendor-authored listicles biasing the named set (L004). |
| C2 (runner-up). Across a cross-entity sample of captured companies, which back their headline claims with **independently verifiable** proof (named clients, certifications, audited filings, clinical citations) vs **self-reported assertion only** — and can a reader tell proof-grade apart from State alone? | calibration | yes | store-only | Directly serves "make AI safe to delegate to"; cross-cohort cut never done store-wide (021 was telehealth-only proof devices; 038 was GLP-1 delegation grounding). | Confidence / source grain; tests whether proof-grade is legible from State or relay-dependent prose. | Reaches the L002/L003 confound axis across entity types, not one vertical. | The 6–8 sampled `profile.md` lead surfaces + `unverified_fields` + proof prose; reproducible non-cherry-picked sample. | Re-confirming the known "protection lives in prose, relay-dependent" finding without a fresh design payload (repeat risk). |
| C3. For a buyer building an agency shortlist, can the store deliver a **budget anchor** for any of the captured creative/services firms, or is `[on-request]` total across the cohort (follow-on to 045 CR1)? | value-read | yes | store-only | Buyer-facing; sharpens 045 CR1's "4/5 deliver zero price signal." | Pattern extraction (pricing surface on bespoke-scope entities). | Minor reach; mostly re-reads 045 cohort. | The 5 agency profiles' pricing lines. | Pure repeat of 045 with no new design uncertainty. |
| C4. Outside telehealth, which captured brands roll up to a shared corporate parent via `parent`/`owns`, and how concentrated is ownership in the tech/consumer slice (non-telehealth 026)? | gap-probe | yes | store-only | Ownership/consolidation map on a fresh slice. | Relation-pressure (vertical relation; consistency). | Tests vertical-relation consistency outside telehealth. | `parent`/`owns` frontmatter grep across non-telehealth store. | `relation-pressure` is saturated; low marginal learning vs 026/039/047. |
| C5. For a consumer-hardware anchor (Oura), who do buyers actually cross-shop with per external demand-side evidence (Exa neighbors / "X vs Y" / alternatives), and how does that compare to the store's captured neighborhood? | gap-probe | yes | bounded-live | Demand-side neighborhood on a fresh anchor (030 was telehealth+SaaS). | Relation / neighborhood. | Reaches external cross-shop evidence. | Exa/SERP neighbor panel + store diff. | Overlaps 030/047 relation frontier; Exa adds a 3rd source family / broader spend than a clean radar. |
| C6. Can a programmatic downstream consumer rely on `profile.md` frontmatter as a stable typed contract across schema vintages 2.2→2.6, or does version drift (missing `socials`/`legal_entity`/`modules`, single-valued enums) break a build-on-top integration? | calibration | yes | store-only | Serves "build on top without re-capturing"; 051 noted vintage drift leaves peripheral holes. | Persistence boundary / confidence grain. | Tests the Pantry/builder integration surface directly. | Frontmatter survey across the 2.2→2.6 vintage spread. | Builder-only; re-runs the builder-not-buyer frontier; partly answered by 051. |
| C7. Cutting a non-telehealth vertical (consumer hardware), what "table-stakes" offer/acquisition features are becoming normal vs differentiated (cross-cohort table stakes outside telehealth, 015)? | value-read | yes | store-only | Pattern extraction on a fresh vertical. | Pattern extraction. | Mild reach. | Offer/acquisition prose across the hardware cohort. | Thin cohort (~9); risk of a generic "table stakes" read that the store already carries. |

## Selected Question(s)

1. **C1 — Wearable / sleep / recovery tracker coverage radar (L001 generalizability).**
   Recommended. Strongest reader value (a buyer genuinely wants "what am I missing"), it
   exercises the **boundary / membership** design uncertainty unread since the L001
   telehealth runs, and it is the first generalizability test of a *graduated* lesson on
   a fuzzy-boundary consumer-hardware category — a real design payload whether the recipe
   holds or breaks. Bounded-live with a tight light plan.
2. C2 — Cross-entity proof-substantiation grade (store-only runner-up if a zero-spend run
   is preferred). High value-job relevance but higher repeat risk against 021/038.

These are Scout recommendations.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For a buyer choosing a wearable / sleep / recovery tracker, which category members do third-party 'best of 2026' listicles + SERPs repeatedly name, and which of those does Truffle's store not have captured at all — and does the graduated L001 coverage-radar recipe (SERP -> >=2 listicles -> token-match store diff) hold on a fuzzy-boundary consumer-hardware category, or does category blur (smart ring vs smartwatch vs recovery band vs sleep system) degrade the cross-source intersection?"
selected_slug: wearable-coverage-radar-l001-generalizability
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: "Store wearable/recovery brands currently captured (~9: ouraring, whoop, eightsleep, onepeloton, apple, therabody, hyperice, nike, casio) diffed against an externally-named 'best 2026 wearable/sleep/recovery tracker' set from >=2 independent editorial listicles. The cohort boundary is itself a finding to map, not a given."
likely_source_panel: "1 SERP query (firecrawl_search) + 2 independent editorial best-of listicles (Wirecutter / Tom's Guide / CNET / The Verge class), scraped as plain markdown."
builder_lens: "Boundary / membership + persistence boundary: tests whether the graduated L001 coverage-radar recipe generalizes from crisp telehealth verticals to a fuzzy-boundary consumer-hardware category, and whether membership stays a query-time recipe or shows pressure to become a stored set."
reach_reason: "Reaches past the cached store to an external named-set the store can be diffed against, and stresses L001's cross-source intersection on a category whose listicle boundary blurs across smart rings, smartwatches, recovery bands, and sleep systems."
allowed_sources:
  - "store/ (captured wearable/recovery profiles, frontmatter + offerings)"
  - "experiments/00-market-read-lab/learning/ (context only)"
  - "1 SERP query via firecrawl_search (refund the search credit via firecrawl_search_feedback)"
  - ">=2 independent editorial best-of listicles scraped as plain markdown"
disallowed_actions:
  - "PDF parsing (parsers:[pdf]) or JSON-extraction scrapes (formats:[json]) — variable, pre-call-invisible credit cost (run-040 / run-047 spend-breach class)"
  - "entering any purchase funnel, login, or paywall"
  - "treating a vendor-owned listicle as the sole denominator (supplementary only; corroborate across >=2 independent editorial lists)"
  - "adding a 3rd source family or broadening into open-ended browsing/crawl"
  - "mutating store/, writing back, creating durable primitives, or proposing/graduating lessons"
live_evidence_plan:
  evidence_goal: "Verify the externally-named wearable/sleep/recovery tracker set and diff it against the store's captured brands to find which true category members are uncaptured, while watching whether category-boundary blur degrades the L001 cross-source intersection."
  budget_class: light
  allowed_source_families: ["SERP", "editorial best-of listicle"]
  preferred_sources: ["Wirecutter", "Tom's Guide", "CNET", "The Verge", "PCMag", "Rtings"]
  disallowed_source_families: ["vendor-owned listicle as sole denominator", "app-store data", "PDF", "JSON-extraction scrape", "funnel/login/paywalled/private"]
  ceilings:
    source_families: 2
    outside_sources_read_or_captured: 5
    paid_capture_credits: 8
  stop_rules:
    - "Stop after 1 SERP query + at most 3 listicle scrapes, OR once >=2 independent editorial listicles corroborate a stable named set — whichever comes first."
    - "Plain-markdown scrapes only (~1 credit each); refund the SERP search credit via firecrawl_search_feedback."
    - "Fail closed to insufficient-evidence rather than add a 3rd source family, use a variable-cost format, or broaden the question."
  fail_closed_when:
    - "next useful step would exceed 8 paid credits or 5 outside sources"
    - "would require a PDF or JSON-extraction (formats:[json]) scrape"
    - "would add a 3rd source family or enter a funnel/login/paywall"
    - "the named set has no stable cross-source intersection (report 'not found', not 'not there')"
approval_needed: no
why_autonomous_safe: "Standing bounded-live policy; smallest useful panel (2 families, <=5 sources, <=8 credits, plain-markdown only); explicit fail-closed against the run-040/047 variable-cost-format spend-breach class; no funnel, no write-back, no store mutation."
loop1_failure_mode: "Letting category blur inflate the 'missing' set with general smartwatch adjacencies that aren't true cohort members, or treating a single vendor-authored listicle as the denominator (L004); over-claiming completeness from a partial panel ('not found' != 'not there')."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. C1 wins on three counts: (1)
genuine buyer value, (2) it reopens the **boundary / membership** design uncertainty
dormant since the L001 telehealth runs, and (3) it is the first generalizability test of
a graduated lesson on a deliberately harder (fuzzy-boundary) category, so it produces a
design payload whether the recipe holds or breaks. The bounded-live plan is hardened
against the documented spend-breach class (run-040 PDF, run-047 JSON-extraction): plain
markdown only, variable-cost formats explicitly disallowed, search credit refunded.
C2 is the zero-spend runner-up if an unattended store-only run is preferred over any
Firecrawl spend.
