# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
learning_tags: [denominator-reconciliation, coverage-caveat, source-panel, source-rigor, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes — clean bounded-live gap-probe, both halves landed. The store
  holds 4 of the externally-named tracker brands (Oura/Whoop/Apple/Eight Sleep) and lacks
  the mainstream-volume majority (Fitbit, Garmin, Withings, Samsung, Amazfit, Google). The
  graduated L001 coverage-radar recipe **mechanically generalized** to a non-telehealth
  vertical AND exposed two telehealth-shaped assumptions it carries. 3 net credits / 8;
  3 outside sources / 5; 2 source families; stop rule fired after the 2nd editorial list.
- **What was awkward?** PCMag (the planned fitness-axis list) is unsupported by Firecrawl
  ("we do not support this site"); substituted wareable.com — an in-plan source-family
  swap, logged. And the category is genuinely fuzzy: the sleep-axis and fitness-axis lists
  barely overlap, so the named-set depends on which sub-axis list you pick.
- **What should the next agent know?** L001 holds outside telehealth but its load-bearing
  assumption (a category maps to one overlapping listicle population) is telehealth-shaped:
  on consumer hardware the category splits into near-disjoint sub-axis listicles (G1) AND
  the store's own cohort boundary doesn't match the editorial category (G2 — Peloton/
  Therabody/Hyperice/Nike are in the store's "wearable" set but in neither tracker list).
  "No new primitive needed"; membership stays a query-time recipe with a documented
  generalization caveat.

## What happened

Bounded-live coverage radar. (1) Grepped `ls store/` for the captured wearable/recovery
cohort (8 dedicated makers + Casio watches) and confirmed via frontmatter. (2) Ran 1 SERP
query (firecrawl_search, plain web), refunded 1 of 2 credits via firecrawl_search_feedback.
(3) Scraped 2 independent editorial best-of lists as plain markdown — Sleep Foundation
(sleep axis) and Wareable (fitness axis); PCMag failed (unsupported), substituted Wareable
already in plan. (4) Built the cross-source intersection and token-matched the named brands
against `ls store/`. No JSON/PDF formats, no funnel, no store mutation. Full detail in
`read.md`; named-set + diff in `receipts/C1-external-named-set-and-store-diff.md`.

## Observations

Greedy raw learning for this run. Preserve singletons here, then Loop 2 appends the
useful rows to `learning/observations.md`. Do not merge rows, dedup into backlog items,
or translate wishes into build proposals inside the run.

Use short IDs such as `F1`, `S1`, `W1`, `G1` so reviews can cite them. Kinds are the
closed set: `friction` · `surprise` · `wish` · `gap` · `risk-miss` · `brian-correction`.
Record the symptom in `Saw`; put the boundary you are deliberately not asserting in
`Not claiming` (no fix, no build proposal).

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| S1 | surprise | **L001's coverage-radar recipe mechanically generalizes outside telehealth.** First non-telehealth test of the *graduated* L001 recipe (all 3 source runs 012/022/024 were telehealth verticals): 1 SERP + 2 independent editorial listicles + a token-match store diff produced a clean, corroborated missing-set (Fitbit/Garmin/Withings/Samsung/Amazfit/Google) on consumer wearables. The mechanism is source-family-portable, not telehealth-specific. | That L001 is fully general — G1/G2 show its *assumptions* are telehealth-shaped; only that the recipe's mechanics produced a real answer on a fresh vertical. | read.md Result(2)/Verdict; receipt C1 table | query-time-grouping-enough, source-panel |
| G1 | gap | **Category blur splits the denominator into near-disjoint sub-axis listicles — a sharper `denominator-reconciliation` than telehealth.** The sleep-axis list (Oura, Eight Sleep, Bía, Muse, RISE) and the fitness-axis list (Hume, Fitbit, Huawei, Amazfit, Garmin) intersect on almost nothing but Oura/Whoop. In L001's telehealth runs "best GLP-1" lists overlapped, so "≥2 listicles corroborate" was robust; here *which two lists you pick drives the named-set*, so a naïve single-list radar misleads. L001 as written names no sub-category step. | That L001 is broken — it holds (S1); only that its "one category → one listicle population" assumption is telehealth-shaped and needs an explicit sub-axis step on fuzzy categories. | read.md Result(2)/C2; receipt C1 (S2 vs S3) | denominator-reconciliation, source-panel, coverage-caveat |
| G2 | gap | **The store's own cohort boundary doesn't match the editorial category, so the diff denominator is contested before any matching.** The store's "wearable/recovery" set includes Peloton (connected fitness equipment), Therabody + Hyperice (percussive/recovery hardware), Nike (apparel + recovery partnership) — and **none of the four appears in either tracker list**. "What counts as in the category" is the question the radar cannot derive; a human must fix the boundary first. New flavor of `denominator-reconciliation`: contamination is on the *store* side of the diff, not (only) the external draw. | That the store tags are wrong — each is individually defensible; only that an entity-shape cohort ("trackers") can't be drawn from the store's broader "wearable/recovery" grouping without a human boundary call. | read.md Result(2)/C3; profile.md descriptions for onepeloton/therabody/hyperice/nike | denominator-reconciliation, coverage-caveat |
| S2 | surprise | **The missing-set is the market's volume center; the store skews premium.** The 6 high-confidence missing brands (Fitbit/Garmin/Withings/Samsung/Amazfit/Google) are the mainstream $50–400 fitness-band/smartwatch tier; the store's captured 4 (Oura/Whoop/Eight Sleep/Apple) are the premium recovery/optimization tier. The store's wearable coverage is mode-skewed, not random. | That the store *should* capture the volume tier — "not captured" ≠ "not a competitor" (L005 corollary); only that the coverage gap is systematically on one market mode. | read.md Market Pattern; receipt C1 | coverage-caveat, source-panel |
| R1 | risk-miss | **Listicle rankings carry vendor/affiliate bias even where the named set corroborates (L004 instance).** Wareable ranks **Hume Band #1–2** while running "Buy 1 Hume Band, Get 1 free" + "50% OFF code WRBL20" + affiliate links (Hume is an advertiser on the page); the Circular SERP listicle ranks its own Circular Ring #1. The recovered *set* survives cross-source corroboration, but *rank and inclusion* are self-serving. A radar that trusted rank, not just membership, would launder advertiser placement into "best." | That the lists are useless — the corroborated set is reliable; only that vendor-authored/affiliate rankings are a biased denominator for *ranking*, not membership. Mirrors run-047 S2. | read.md C4; receipt C1 (S3 Hume advertiser, S1 Circular self-#1) | source-rigor, source-panel |
| R2 | surprise | **Bounded-live source-substitution worked cleanly when a planned list was unscrapeable.** PCMag (the planned fitness-axis list) returned Firecrawl "we do not support this site"; substituting wareable.com (same source family, in-plan) kept the run in-contract with no ceiling breach and no broadening. Contrast the run-040/047 spend-*breach* class — here the plan's "≥2 independent editorial listicles" framing (family, not named URL) absorbed a dead source gracefully. | That source substitution is always safe — it stayed safe because the swap was same-family and in-ceiling; only that family-level (not URL-level) plans degrade gracefully when a source dies. | run-notes live_evidence_used; receipt C1 (PCMag failed, not billed) | tooling-ergonomics, source-panel |

## Inputs and scope

- **Store cohort (denominator A):** `ls store/` + frontmatter grep → 8 dedicated
  wearable/recovery makers (ouraring, whoop, eightsleep, onepeloton, apple, therabody,
  hyperice, nike) + casio (watches, excluded as non-tracker). Store total 145 dirs.
- **External named-set (denominator B):** 1 SERP query + 2 independent editorial best-of
  listicles (Sleep Foundation sleep axis; Wareable fitness axis) + SERP snippet leads
  (Consumer Reports, Wired, PCMag, Circular, Wirecutter) as direction-finding only.
- **Diff:** token-match each externally-named brand against `ls store/`.
- **Exclusions:** single-source tail brands treated as leads, not corroborated gaps;
  Casio excluded; rankings excluded from the membership claim (R1 bias).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
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
  outcome: "Stop rule fired after the 2nd independent editorial listicle corroborated a stable named set. Net spend 3 credits / 8; 3 outside sources read / 5; 2 source families. No fail-closed condition hit; PCMag substitution stayed in-family and in-ceiling."
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: 'firecrawl_search "best fitness and sleep tracker 2026 wearable buying guide" (searchId 019efe3f-7ef2-7149-a6d1-2153698dd6b6)'
    source_family: SERP
    action_taken: searched
    reason: "Find independent editorial best-of listicles spanning the category's sleep and fitness sub-axes; harvest snippet leads."
    source_grade: direction-finding
    captured_at: 2026-06-25
    spend_note: paid-credit (2 charged, 1 refunded via firecrawl_search_feedback -> net 1)
    claim_ids_supported: [C1, C4]
  - source_or_query: https://www.sleepfoundation.org/best-sleep-trackers
    source_family: editorial best-of listicle (sleep axis)
    action_taken: scraped
    reason: "Independent editorial sleep-tracker named-set for the cross-source intersection."
    source_grade: secondary
    captured_at: 2026-06-25 (page modified 2026-04-22)
    spend_note: paid-credit (1)
    claim_ids_supported: [C1, C2, C3]
  - source_or_query: https://www.pcmag.com/picks/the-best-fitness-trackers
    source_family: editorial best-of listicle (fitness axis)
    action_taken: scrape-attempted-failed
    reason: "Planned fitness-axis list; Firecrawl returned 'we do not support this site' — not billed, not counted as a read. Substituted wareable.com (same family, in plan)."
    source_grade: n/a
    captured_at: 2026-06-25
    spend_note: none (failed, not billed)
    claim_ids_supported: []
  - source_or_query: https://www.wareable.com/fitness-trackers/the-best-fitness-tracker
    source_family: editorial best-of listicle (fitness axis)
    action_taken: scraped
    reason: "Independent editorial fitness-tracker named-set; second corroborating list (PCMag substitute)."
    source_grade: secondary
    captured_at: 2026-06-25 (Firecrawl cache 2026-06-23; page modified 2026-06-02)
    spend_note: paid-credit (1, cache hit)
    claim_ids_supported: [C1, C2, C3, C4]
```

## Friction log

PCMag (planned fitness-axis list) unscrapeable — Firecrawl "we do not support this site."
Resolved by same-family substitution (wareable.com), no broadening (see R2). No other
operational friction; the radar mechanics (grep store → SERP → 2 scrapes → diff) were
fast.

## Evidence limits

Light panel (2 editorial lists + SERP leads), not a census. High-confidence missing-set
limited to brands named by ≥2 sources (Fitbit/Garmin/Withings/Samsung/Amazfit/Google);
single-source tail (Huawei/Xiaomi/Hume/Ultrahuman/Muse/Bía) is leads-only. SERP rows are
snippet-grade direction-finding. "Missing" = not captured as of 2026-06-25 in this panel,
not "not a category member." Listicle rankings are vendor/affiliate-biased (R1).

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass** (3/8 credits, 3/5 sources, 2 families, stop rule fired)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (incl. the failed PCMag attempt)
- If `bounded-live`, stop rules and spend notes were recorded: **pass**
- No disallowed action happened: **pass** (no JSON/PDF format, no funnel, no store mutation, no 3rd family)
- Required citations / receipts present and source-graded: **pass** (receipt C1)
- No snippet treated as evidence: **pass** (SERP rows labeled direction-finding; claims rest on dated scrapes + store diff)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass**
- Absence language says "not found", not "not true": **pass**

## Surprises

L001 generalized mechanically (S1) but the category's fuzziness surfaced two failure modes
the crisp telehealth verticals never could (G1 sub-axis listicle disjointness; G2 store
cohort boundary ≠ editorial category). The store's wearable coverage turned out
mode-skewed toward premium recovery, blind to the volume fitness-band tier (S2). Vendor/
affiliate ranking bias was overt (R1). Family-level source planning absorbed a dead
source gracefully (R2).

## Learning tags

Short `kebab-case` recurrence handles for system pressure this run exposed. They mirror
the run header's `learning_tags`. These are not a fixed taxonomy and not permission to
build — a learning pass decides what, if anything, recurs into a lesson.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag? Mirror them into the
header `learning_tags`.

Fired: `denominator-reconciliation` (G1 sub-axis disjointness, G2 store-side boundary
contamination), `coverage-caveat` (S2 mode-skewed coverage), `source-panel` (S1/R2 the
listicle panel and its substitution behavior), `source-rigor` (R1 vendor/affiliate
ranking bias), `query-time-grouping-enough` (membership stays a query-time recipe). No new
tag coined — existing handles fit.

"No new primitive needed" is the honest outcome: membership stays a query-time recipe;
L001 holds with a documented generalization caveat.

## Next-run advice

- If anyone wants to settle G1, re-run with a 3rd *category-spanning* editorial list to
  test whether the sleep-vs-fitness listicle disjointness is a 2-list artifact or a real
  category property.
- Do **not** treat this as a capture worklist for the 6 missing brands without a real
  downstream consumer — the gap is mode-skew, not an error (S2 / L005 corollary).
- Reusable for the next bounded-live scout: family-level source plans (not named URLs)
  degrade gracefully when a source dies (R2); keep that framing.
- Loop 2 should weigh whether G1/G2 are an out-of-band L001 *scope* note (the recipe needs
  an explicit sub-category + cohort-boundary step on fuzzy categories) — but only as an
  observation; do not edit L001.
