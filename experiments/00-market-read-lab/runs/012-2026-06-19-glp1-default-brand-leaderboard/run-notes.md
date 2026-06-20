# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         bounded-live
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [denominator-reconciliation, source-panel, coverage-caveat, source-rigor]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer, Sonnet). The **verifier caught two internal counting errors** — both fixed in
> `read.md` + the receipt: C4 said "8" but listed 9 store-anchored-unranked brands (→ **9**); C2 said
> "~9 absent" but the true store-absent count excl. the GoodRx aggregator is **11** (SkinnyRX had been
> silently dropped; single-source nominees now distinguished from the double-sourced Mochi gap). Verifier:
> C1/C3/C5 **CONFIRMED**; C1/C2/C4 partials were **count-presentation only, not membership errors**;
> bounded-live discipline **PASS** (4 sources logged, ~7 credits, stopped at plan boundary, snippet-only
> S3/S4 constrained to direction-finding). Consumer verdict: **valuable**. Developer verdict: both triage
> attributions **justified** (MRL-001 internal under-count is real + generalizable; MRL-008 listicle flavor
> additive-but-modest); **"no new primitive needed"** is honest. Triage: appended Evidence Logs to
> **MRL-001** (external-panel radar-not-denominator + internal anchored-vs-all-offerers under-count) and
> **MRL-008** (listicle-inclusion confound flavor). `bounded-live` review_after-3-runs clock: **2/3**.

## 30-second operator read

- **Did the run work?** Yes. Second `bounded-live` run (review_after clock now **2/3**). A light
  SERP/listicle panel — 1 SERP query + 2 high-authority listicles fully scraped + 2 affiliate pages
  read as snippets — answered "who's the market default, and does the store hold them?" cleanly. ~7
  Firecrawl credits.
- **What was awkward?** Two things. (1) The U.S. News JSON extraction cost **5 credits**, not the ~1–2
  I expected for a scrape — JSON-with-schema is priced like an extract; markdown for Forbes was ~1. (2)
  Forbes' award→brand mapping isn't a clean field — I recovered it by locating the brand card immediately
  before each "Best …" badge in the markdown; defensible but not verbatim-structured.
- **What should the next agent know?** A third-party listicle panel is a usable **coverage radar, not a
  denominator** — exactly the MRL-001 "SERP/listicle as fallback, not default" note, now tested. It
  nominates concrete capture candidates (**Mochi** is named by *both* authoritative listicles and is
  captured nowhere) and confirms the store is deep on the compounding tail but blind on the big-brand /
  insurance tier. The named set is **head-stable / tail-divergent**: trust cross-source recurrence, never
  one listicle's order (affiliate-confounded).

## What happened

Gated on the contract (scout-only → bounded-live with filled `live_evidence_plan` → autonomous →
approval:no, all pass). Derived the store cohort with `grep -l "anchor_category: GLP-1" store/*/telehealth.md`
(19 brands) and spot-checked 4 GLP-1-offering-but-not-anchored store brands. Ran one SERP query, refunded
1 credit via `firecrawl_search_feedback`, then scraped the two highest-authority listicles (U.S. News 23
providers; Forbes 6 affordable). Computed third-party-named vs store-anchored set membership three ways.
Wrote `read.md` + one panel receipt. Stopped at the plan boundary (head stable after two authoritative
sources; next source would widen into low-authority affiliate tail or a crawl).

## Inputs and scope

- **Store (free):** `anchor_category: GLP-1` grep → 19 brands; `anchor_category` spot-check on
  lifemd/altrx/nurx/hellowisp (GLP-1 offered but not anchored).
- **Live panel (paid/secondary):** U.S. News + Forbes Health "best GLP-1" listicles (fully scraped);
  1 SERP query (8 results); HealingMaps + VaccineAlliance affiliate pages (SERP-snippet only).
- **Exclusions:** GoodRx/Amazon treated as aggregator/marketplace, not telehealth brands, for the
  membership math; low-authority listicle tails kept as direction-finding only; no review/forum bodies
  (run 011's surface, out of scope per plan).

## Live evidence plan

```yaml
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
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "firecrawl_search — best GLP-1 telehealth providers 2026 online semaglutide (8 web results)"
    source_family: SERP/listicle
    action_taken: searched
    reason: "Rank candidate 'best of' listicles by authority; pick the panel"
    source_grade: direction-finding
    captured_at: 2026-06-19
    spend_note: paid-credit   # 2 credits, 1 refunded via firecrawl_search_feedback → 1 net
    claim_ids_supported: [C2, C5]
  - source_or_query: "https://health.usnews.com/best-diet/medication/top-glp-1-weight-loss-medication-providers"
    source_family: SERP/listicle
    action_taken: scraped
    reason: "Authoritative 23-provider named set (page updated 2026-06-12) — JSON extraction of every named brand + headline price"
    source_grade: secondary
    captured_at: 2026-06-19
    spend_note: paid-credit   # 5 credits (JSON-schema extraction priced like extract)
    claim_ids_supported: [C1, C2, C3, C4]
  - source_or_query: "https://www.forbes.com/health/weight-loss/best-affordable-online-glp1-providers/"
    source_family: SERP/listicle
    action_taken: scraped
    reason: "Authoritative affordable cut (audited 2026-06-10); award→brand mapping for the 6 winners"
    source_grade: secondary
    captured_at: 2026-06-19
    spend_note: paid-credit   # ~1 credit (markdown, onlyMainContent)
    claim_ids_supported: [C1, C2, C3]
  - source_or_query: "https://healingmaps.com/best-glp1-telehealth-programs-2026/ ; https://www.vaccinealliance.org/semaglutide/cheapest-online/"
    source_family: SERP/listicle
    action_taken: searched
    reason: "Low-authority affiliate tails — used snippet-only to show cross-source tail divergence"
    source_grade: direction-finding
    captured_at: 2026-06-19
    spend_note: free   # SERP snippets only, not scraped
    claim_ids_supported: [C5]
```

Total spend: **~7 Firecrawl credits** (1 net search + 5 JSON scrape + ~1 markdown scrape). Above run 011's
5; the overage is entirely the JSON-extraction premium on one page (see Friction log). Stopped at plan
boundary.

## Friction log

- **JSON scrape cost 5 credits, not ~1.** `firecrawl_scrape` with `formats:[json]` + schema is billed like
  an extract, not a plain scrape. For named-set capture, **prefer markdown + local parse** (Forbes route,
  ~1 credit) and reserve JSON extraction for when verbatim structured fields are load-bearing. A cheap
  recurrence note, not a system gap.
- **Award→brand mapping is prose, not a field.** Forbes' "Best X" badges had to be matched to the brand
  card preceding them in markdown. Faithful but not greppable — same prose-surface flavor MRL-002 already
  notes for offer-structure (run 010), now on a third-party listicle.
- The store-side comparison was trivial: one `grep` + four spot-checks. The labor was all on the messy
  third-party side — which is the point of the read.

## Evidence limits

- **Affiliate/SEO confound is load-bearing.** Both authoritative listicles carry commission disclosures;
  inclusion/order ≠ objective ranking. Only the head (Ro, Hims/Hers, Mochi, Remedy Meds, Found) is stable
  across them. Conclusions rest on cross-source *recurrence*, not any single page's list.
- **Partial third-party panel** (2 authoritative listicles + SERP titles). A wider panel would add tail
  names; head-stability suggests it would not move the head. Framed as "named by this panel", not "the
  market's complete default set".
- **Store side is the queryable cohort, not all GLP-1 offerers.** LifeMD/Nurx/Wisp offer GLP-1 but are
  `multi/none`-anchored, and altRx lacks `telehealth.md` — so the anchor grep *under*-counts store GLP-1
  presence. The "store gap" is relative to the *anchored* set; some apparent absentees are partial-presence.
- **Snippet-only S3/S4** support only the tail-divergence framing (C5), never a membership conclusion.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (planned bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (4 entries)
- If `bounded-live`, stop rules and spend notes were recorded: **pass** (~7 credits itemized; stopped at plan boundary)
- No disallowed action happened: **pass** (no store write-back, no schema/code/template change, no graduation, no broad crawl, no listicle-order-as-ranking)
- Required citations / receipts present and source-graded: **pass** (one panel receipt, S1–S7 graded)
- No snippet treated as evidence: **pass** (C1–C4 rest on fully-scraped authoritative listicles + store grep; S3/S4 snippets labeled direction-finding, support only C5)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (listicles dated 2026-06-12 / 2026-06-10, scraped 2026-06-19, graded secondary)
- Absence language says "not found", not "not true": **pass** ("absent from store", "captured nowhere", "not GLP-1-queryable" — never "doesn't exist")

## Surprises

- **The store's gap and over-coverage point in opposite directions.** I expected either "store is thin" or
  "store is complete". Instead the store *under*-covers the brand-name/insurance head (Mochi, PlushCare,
  WeightWatchers) and *over*-covers the compounding long-tail (8 anchored brands no listicle ranks). The
  store and the listicles are measuring two different markets.
- **Mochi is the one clean signal in a noisy panel.** Almost everything else diverges by source, but Mochi
  is named by *both* authoritative listicles and is the highest-mention store-absent brand — the rare case
  where the affiliate noise cancels and a real capture candidate falls out.
- **The store accidentally already "knows" some absentees** — LifeMD, Nurx, Wisp all offer GLP-1 but
  aren't anchored to it, so a naive cohort grep calls them missing when they're partially present. The
  denominator bug is on *our* side as much as the panel's.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `denominator-reconciliation` | The whole read was store-set vs third-party-named-set reconciliation; the answer depends entirely on how the GLP-1 set is drawn (anchored-only vs all-GLP-1-offerers) and on the affiliate confound in the external set. | append MRL-001 evidence — first run to *test* the SERP/listicle-as-fallback-denominator note; confirms radar-not-denominator |
| `source-panel` | A SERP/listicle named-set panel was the load-bearing external source — a *different* bounded-live source family than run 011's review bodies. First use of listicles as a membership/coverage radar. | watch — pairs with MRL-001; distinct from MRL-010 (reviews) |
| `coverage-caveat` | Concrete store gaps surfaced (Mochi, PlushCare, WeightWatchers, LifeMD-as-GLP-1) + the anchored-grep under-count of multi/none GLP-1 offerers. | append MRL-001; Mochi is a concrete capture candidate (relates to MRL-003 depth-backfill family) |
| `source-rigor` | Listicles are affiliate/SEO-confounded; head-stable/tail-divergent; one JSON scrape mis-priced. Confident claims kept to cross-source recurrence only. | reinforces MRL-008's "headline signal needs its confound sibling" — listicle *inclusion* needs an *affiliate-disclosure / cross-source-recurrence* sibling |

No new tag needed. **"No new primitive needed"** holds: this is denominator/coverage-radar evidence
(MRL-001) plus a confound-flavor note (MRL-008), not a call for a stored leaderboard object, a scraper, or
a monitor. A third-party-default *Signal* is named as a one-sighting curiosity, explicitly not proposed.

## Triage submissions

1. **MRL-001 (Market denominator reconciliation) — append Evidence Log.** First run to *operationalize*
   the standing note that "external SERP/listicle panels should be fallback denominator sources, not the
   default." Tested it: a 2-authoritative-listicle panel is a usable **coverage radar** (nominated Mochi +
   PlushCare + WeightWatchers + LifeMD-as-GLP-1 as concrete capture candidates; confirmed store depth on
   the compounding tail) but **not a clean denominator** (affiliate-confounded, head-stable/tail-divergent).
   Also surfaced an *internal* denominator bug: the `anchor_category: GLP-1` grep under-counts store GLP-1
   presence because multi/none brands (LifeMD, Nurx, Wisp) and module-thin brands (altRx) offer GLP-1
   without being anchored to it. Recommendation: the MRL-001 convention should name *both* the external
   inclusion rule (cross-source recurrence, affiliate caveat) *and* the internal "anchored vs all-offerers"
   cut. Human-gated; no graduation.
2. **MRL-008 (source-rigor / confound convention) — append Evidence Log (new flavor).** Listicle
   *inclusion* is a headline signal that misleads without its confound sibling: a single affiliate listicle
   reads as a ranking, but inclusion/order is partner/SEO-driven. The integrity sibling here is
   **affiliate-disclosure + cross-source recurrence**. Same family as the Trustpilot score→body flavor
   (run 011), different signal grain (listicle naming).
3. **Concrete capture candidate (note, not a new item): Mochi.** Named by both authoritative listicles,
   absent from the store. Pairs with the MRL-003 depth-backfill family. Propose-don't-write; do not capture
   from inside the run.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- **Close the named head-gap, then re-test:** capture Mochi (+ PlushCare, WeightWatchers, LifeMD's GLP-1
  line) and re-run this comparison — does the store then become a superset of market-default, or do new
  listicle names keep appearing? That tells you whether the head is finite or a moving target.
- **Fix the internal denominator first:** decide whether "GLP-1 cohort" means anchored-only or
  all-GLP-1-offerers; the multi/none brands (LifeMD, Nurx, Wisp) sit in the seam and quietly distort every
  GLP-1 cohort read, not just this one.
- **Keep listicle reads to recurrence, not rank.** Never trust one page's order; require a name on ≥2
  authoritative sources before calling it "default." Use markdown+parse, not JSON extraction, to keep
  named-set capture at ~1 credit.
- If a 4th MRL-010 sighting is still wanted, run 011's trust-gap shape on a *different* cohort (TRT/longevity)
  — held over from this cycle to test a fresh source family instead.

---

**Loop 1 complete — `run_status: read-done`.** Start Loop 2 for review.
