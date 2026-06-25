# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
learning_tags: [freshness-monitoring, source-rigor, depth-backfill, query-time-grouping-enough, tooling-ergonomics, bounded-live-spend]
```

## 30-second operator read

- **Did the run work?** Yes. Bounded-live re-check of 3 panel brands' captured prices vs
  live; clean gap-probe result. 3 paid credits of 8; 3 outside sources of 5; stop rule
  fired at 3 verifiable brands.
- **What was awkward?** The panel turned out fresher than expected (4/5 captured 06-24,
  1 day old; only Peloton 06-10, 15 days), so this is a freshness *floor* test, not a
  multi-week decay curve. And the Eight Sleep "live" fetch came back as a 06-24 Firecrawl
  cache hit, not a true 06-25 re-check.
- **What should the next agent know?** Decay concentrated entirely at one **expired dated
  promo** (Peloton refurb Bike $695 → reverted to $1,145 after its printed June-15 expiry).
  Everything evergreen matched. The predictive datum (promo end date) is captured in prose
  but unstructured. For a sharper decay study, pick a cohort with 2–4-week-old captures.

## What happened

Read captured price + `captured_at` from store/ for the 5-brand panel first; 4/5 were
captured 06-24 and Peloton 06-10. Fetched 3 live vendor marketing pages as plain markdown
(Oura homepage, Eight Sleep Pod 5 PDP, Peloton exercise-bikes PLP), compared live headline
price to captured value. Stopped at 3 per the contract stop rule (≥3 open-page-verifiable
→ do not add brands). Did not enter any funnel, used no PDF/JSON-extraction, did not mutate
store/. Full detail in `read.md`; live-vs-captured table + claim map in
`receipts/C1-live-price-recheck.md`.

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
| G1 | gap | Of 3 re-checked panel prices, the only one that diverged at re-check was Peloton's refurb Original Bike, where a **dated promo with a printed expiry** ("$695… ends June 15, 2026", captured 06-10) had lapsed by re-check (06-25) and reverted to the struck regular price $1,145. The predictive datum — the promo end date — is captured in `offerings.md` prose / `site_notes` but lives in no frontmatter or price-cell field, so a reader/monitor can't *query* "which captured prices sit on a promo window that has already passed." Empirical, localized instance of the 041/048 "captured State has no change-detection home." | That a structured promo-expiry field should be built — n=1 diverging price, prose carried the expiry every time; only that the decay was promo-bound and the predictive datum is unstructured. | read.md Result(1)/Gap Map; receipts/C1 C3; store/onepeloton-com/offerings.md:7/44/57; runs 041/048 | freshness-monitoring, depth-backfill, query-time-grouping-enough |
| S1 | surprise | Captured *promotional* prices did **not** spontaneously rot at 1-day age, and a captured dated sale stayed valid **inside its own printed window**: Oura's "Flash Sale through June 26th / From $244" (captured 06-24) was still live and still $244/$279 on 06-25. So a captured promo price isn't self-evidently stale — its trustworthiness is bounded by the promo's own end date (often captured verbatim), not by bare `captured_at`. | That promo prices never rot fast — they revert the moment their window passes (see G1); only that within-window they held, so `captured_at` alone over- and under-states staleness depending on the promo window. | read.md Result(2); receipts/C1 C1; store/ouraring-com/offerings.md:32/47 | freshness-monitoring, source-rigor |
| S2 | surprise | The one price that diverged was **already self-flagged in its own capture** — the 06-10 Peloton capture recorded both the struck regular price ($1,145, = today's live price) and the verbatim expiry ("ends June 15, 2026"). So the store held everything needed to predict the rot **without any live fetch**; the live re-check only confirmed what a careful read of `unverified_fields`/`site_notes` already implied. | That the live fetch was unnecessary in general — it falsified the alternative (that the price drifted unpredictably); only that for promo-bound decay the capture's own prose was sufficient to predict it. | read.md Result/Missing-Stale; store/onepeloton-com/offerings.md:44/45 | freshness-monitoring, source-rigor, query-time-grouping-enough |
| G2 | gap | A "live re-check" via `firecrawl_scrape` silently returned a **cached scrape dated 2026-06-24** for Eight Sleep (cacheState `hit`, cachedAt 06-24) — the same day as the original store capture — while Oura returned fresh-today and Peloton was a cache `miss`. A freshness-verification routine that doesn't bust the fetch cache can re-confirm stale data as "still current," defeating the purpose of the check. | That the tool is broken or the price was wrong — Eight Sleep's price matched anyway; only that cache behavior makes "I re-checked it live" unreliable unless cache-busting is explicit (`maxAge:0`). | read.md Result(3)/G2; receipts/C1 S2 metadata (cachedAt 2026-06-24T02:05Z) | tooling-ergonomics, source-rigor, freshness-monitoring |
| S3 | surprise | A vendor-side internal inconsistency was itself **durable** across capture→re-check: Peloton's stale Affirm footnote (refurb Bike+ "based on a price of $1,995" vs displayed $1,395), captured + flagged on 06-10, persisted unchanged on the live 06-25 page. A captured `unverified_fields` discrepancy can be a stable property of the live site, not a capture-time artifact. | That the footnote will never be fixed — only that a flagged on-site inconsistency reproduced live 15 days later, so the 06-10 `unverified_fields` flag is still accurate. | read.md Source Gaps/What-Would-Change; store/onepeloton-com/offerings.md:45; receipts/C1 C4 | source-rigor, freshness-monitoring |

## Inputs and scope

- **Panel (store):** ouraring-com, eightsleep-com, therabody-com, hyperice-com,
  onepeloton-com. Selected for open-marketing-page (non-intake-gated) headline pricing,
  prioritizing the promotional-snapshot captures flagged in runs 043/046.
- **Capture ages at re-check (06-25):** oura/eightsleep/therabody/hyperice = `captured_at
  2026-06-24` (1 day); onepeloton = `captured_at 2026-06-10` (15 days).
- **Re-checked live:** oura (homepage), eightsleep (Pod 5 PDP), onepeloton (exercise-bikes
  PLP). **Not re-checked:** therabody, hyperice — stop rule fired at 3 verifiable brands.
- **Exclusions:** no intake funnels, no login/checkout, no SERP/listicle/third-party, no
  PDF/JSON-extraction, no store/ mutation.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan:
  budget_class: light
  evidence_goal: "Verify, per panel brand, whether the live marketing-page headline price still matches the captured value; record capture date so divergence has a measured age."
  allowed_source_families:
    - "vendor first-party marketing/pricing page (the brand's own site)"
  preferred_first: "Read captured price + captured_at from store/ before any live fetch."
  disallowed_source_families:
    - "SERP / listicle / third-party aggregator / review-forum / PDF / paywalled / private"
  ceilings:
    source_families: 1
    outside_sources_read_or_captured: 5
    paid_capture_credits: 8
  fail_closed_when:
    - "Live price would require intake funnel / login / checkout -> record 'not verifiable on open page', do not enter"
    - "Fetch would need a variable-cost format (PDF/JSON-extraction) -> stop, plain markdown only"
    - "5-source or 8-credit ceiling would be exceeded -> stop as insufficient-evidence"
    - "Question would widen beyond price-match verification -> stop"
  stop_rules:
    - "Stop after at most 5 live vendor-page fetches"
    - "If 3+ panel prices are open-page-verifiable, the divergence read is complete; do not add brands"
# Actuals: 1 source family, 3 outside sources fetched, 3 paid credits. Stop rule fired at 3.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used:
  - source_or_query: "https://ouraring.com/"
    source_family: "vendor first-party marketing page"
    action_taken: scraped
    reason: "Re-check captured Ring 4 'From $244' / Ceramic '$279' + flash-sale window vs live."
    source_grade: primary
    captured_at: "2026-06-25 (Firecrawl cachedAt 2026-06-25T06:55Z, fresh)"
    spend_note: paid-credit
    claim_ids_supported: [C1]
  - source_or_query: "https://www.eightsleep.com/product/pod-cover/"
    source_family: "vendor first-party PDP"
    action_taken: scraped
    reason: "Re-check captured Pod 5 Queen $2,749/$2,999 + 4th July Sale vs live."
    source_grade: primary
    captured_at: "2026-06-24 (Firecrawl CACHE HIT cachedAt 2026-06-24T02:05Z — not an independent 06-25 fetch; see obs G2)"
    spend_note: paid-credit
    claim_ids_supported: [C2]
  - source_or_query: "https://www.onepeloton.com/exercise-bikes"
    source_family: "vendor first-party PLP"
    action_taken: scraped
    reason: "Re-check captured refurb Original Bike '$695 ends June 15' + durable MSRPs vs live."
    source_grade: primary
    captured_at: "2026-06-25 (Firecrawl cacheState miss — fresh live fetch)"
    spend_note: paid-credit
    claim_ids_supported: [C3, C4]
```

## Friction log

Low friction. The one tool surprise (G2: a "live" fetch returning a 06-24 cache hit) is
the only operational snag — it means cache-busting must be explicit for a freshness check.
The panel being freshly captured (1-day age on 4/5) is a sampling limit, not friction.

## Evidence limits

- Capture ages skewed fresh (4/5 at 1 day; 1 at 15 days) → freshness *floor* test, not a
  multi-week decay curve. Organic non-promo price drift is unmeasured (none of the 3
  re-checked evergreen prices moved, but the window was short).
- Eight Sleep "live" cell is a 06-24 cache hit, not an independent 06-25 re-check (G2).
- Therabody + Hyperice not re-checked (stop rule at 3); their Prime-Day-sale persistence
  is unverified — recorded as a coverage limit, not a finding.
- n=1 diverging price (Peloton refurb Bike) — the decay-is-promo-bound pattern is a single
  clean instance, not a proven rate.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass** (bounded-live,
  autonomous_eligible yes, approval_needed no, evidence_mode mirrored)
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (planned bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass** (1 source
  family, 3 sources, 3 credits — all under ceilings; stop rule fired at 3)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (3 logged)
- If `bounded-live`, stop rules and spend notes were recorded: **pass**
- No disallowed action happened: **pass** (no funnel/login/PDF/JSON-extraction/SERP/store-mutation)
- Required citations / receipts present and source-graded: **pass** (receipt C1, all primary)
- No snippet treated as evidence: **pass** (full plain-markdown vendor pages, no snippets)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass**
  (capture dates + live fetch dates + cache state recorded per source)
- Absence language says "not found", not "not true": **pass** (Therabody/Hyperice "not
  re-checked"; Eight Sleep "not an independent re-check"; Peloton "$695 not found live")

## Surprises

The headline surprise: captured pricing State did **not** rot on a clock — it rotted on a
**promo's printed expiry**. A dated sale stayed valid inside its window (Oura) and reverted
the moment it lapsed (Peloton $695 → $1,145). The store had already captured the expiry
date and the post-promo price in prose, so the rot was predictable *without* the live
fetch. Secondary surprise: a "live re-check" silently served a cached scrape (G2).

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

Fired: `freshness-monitoring` (the whole run), `source-rigor` (cache hit, capture dates),
`depth-backfill` (promo-expiry datum unstructured), `query-time-grouping-enough` (prose
carried the expiry; lightest path is a reading/monitor convention, not a field),
`tooling-ergonomics` (cache-busting needed for live re-checks). No new tag coined.

"No new primitive needed" is a valid outcome — and is the landing here: the lightest path
is a freshness reading/monitor convention keyed on already-captured promo-window text, not
a new schema field. A field is unmotivated at n=1 and prose carried the expiry every time.

## Next-run advice

- For a real decay *curve*, pick a panel with 2–4-week-old captures (this store was too
  freshly captured to show organic non-promo drift). Telehealth price captures may be
  older — but their headline price is intake-gated (run-040), so the open-page re-check
  trick won't work there.
- Always set `maxAge: 0` (or otherwise bust cache) on `firecrawl_scrape` when the point is
  to verify *current* state — a default fetch can return a stale cached scrape (G2).
- The promo-expiry signal lives in `offerings.md` `site_notes` / `unverified_fields`; a
  future freshness probe could grep captured promo-window text store-wide to find which
  captured prices are *already* past their printed expiry, with zero live spend.
