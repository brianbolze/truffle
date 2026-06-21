# Scout

## Prior Context Read

- `triage.md`: Acknowledged items MRL-001 (denominator reconciliation), MRL-002 (query
  recipes for State/Signals reads), MRL-008 (source-rigor/confound convention — now with
  four branches), plus referenced MRL-005/006/009/010/011/012/014. Used only to annotate
  design pressure, not to source candidates.
- `scout-context.md`: two-test selection (value/reach + design); prefer source-family
  diversity and frontier gap-probes; bounded-live is first-class when stop rules are clear.
- Last 3 `run-notes.md` files (031 confidence-grain, 032 freshness-grain, 033 watch
  price-visibility): all `store-only`, all landed on the same anti-sprawl family
  (`query-time-grouping-enough` / "no new primitive" / structured-surface-absence). A
  fourth store-meta calibration read would have low marginal design learning.
- `discovery-ledger.md`: 029 established the *traction* axis substrate is thin (20/126
  carry a genuine traction signal; the binding constraint is capture coverage, not
  architecture). 030 found Exa `/findSimilar` is a weak demand-side signal. No lab read
  has ever used the **ads / paid-acquisition** source family, and `tools/ads_transparency.py`
  got a region fix today (2026-06-20).

## Candidate Questions

Scout should select for reader value, reach, source-family diversity, and roadmap
learning. Do not prefer a candidate merely because the store can already answer it.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **C1 (RECOMMENDED).** For a bounded panel of ~6 captured GLP-1 telehealth brands, what does the Google Ads Transparency Center show about active paid-acquisition motion (running now vs ran-only, advertising tenure, creative format), and is ads-presence a cheap, real signal the store's current toolkit can't see — or too biased/push-only to trust? | gap-probe | yes | bounded-live | First lab read on the **ads / paid-acquisition** source family; extends 029's "traction substrate is thin" by testing whether an external *push* signal fills part of the gap. A reader genuinely wants "who's spending to acquire right now." | source-family: does `ads_transparency.py` (Google Ads Transparency) add a cheap, real acquisition-motion Signal absent from the store, and what is its false-confidence boundary? | A source family never used in a read; the paid-acquisition surface; the push-vs-demand distinction the traction frame must respect. | One SerpAPI ads_transparency capture per domain (≤6), domain-keyed to avoid name collisions; recency rule (active = last_shown within ~35d of capture); store cohort as denominator. | Reading ads-presence as **demand/success** (it is budget/push only); `n_creatives_first_page` as total volume; advertiser legal-name ≠ brand mis-attribution; zero-creatives as "not advertising" vs "not visible on Google". |
| C2. Across a cohort, can the store support an apples-to-apples **catalog/offerings comparison** ("what does each brand actually sell"), or does `offerings.md` coverage/grain break the join? | gap-probe | yes | store-only | Tests the under-probed offerings *content* layer (vs pricing in 023). | depth-backfill: is `offerings.md` coverage/grain consistent enough to compare catalogs cross-brand? | The offerings layer as a comparable surface. | `ls offerings.md` coverage count + grain audit across a cohort. | Likely re-confirms the known 028/033 coverage gap (offerings.md sparse) → low novelty. |
| C3. Pick a captured-but-unfamiliar company: does its `profile.md` alone support a 5-second **cold-start** (who/what/how-priced/credible) without re-capture? | calibration | yes | store-only | Tests the never-probed "cold-start a company" + "hand off in 5s" value jobs. | synthesis: is single-profile State sufficient for the cold-start job? | The synthesis/presentation pillar at single-company grain. | Read N profiles against a fixed 5-second rubric. | Single-company + introspective; weak *market-read* reach. |
| C4. Does the **trust/proof-device** pattern-extraction recipe (run 021, telehealth) generalize to a non-telehealth cohort (SaaS or watches)? | gap-probe | yes | store-only | Completes the 027/028/033 cross-vertical generalizability thread on a new recipe. | pattern-extraction: is the proof-device recipe telehealth-overfit? | Cross-vertical recipe portability. | Per-profile credibility-prose read across a non-telehealth cohort. | Generalizability thread is saturated; likely lands "it generalizes, one caveat" again. |
| C5. Using **SERP intent panel** (`serp_intent_panel.py`), what does branded vs category search intent look like for a GLP-1 panel, and does it add a demand-side signal the store lacks? | gap-probe | yes | bounded-live | A second untested-in-a-read source family (intent/SERP). | source-family: does SERP-intent add a usable demand signal? | The intent/SERP demand surface. | ≤6 serp_intent captures + store cohort. | Overlaps 012/022/024 listicle reads; intent-panel parsing unvalidated; demand-vs-visibility confound. |
| C6. **Meta/Instagram** ads presence for a cohort — who runs social ads? | gap-probe | no | live-external-needs-approval | Demand/push on a different channel. | source-family: social-ads channel. | The non-Google ad surface. | Apify route (deferred per tools/BACKLOG.md). | Out of bounded scope — Apify route deferred; not autonomous-safe. Rejected. |
| C7. Cross-store **audience × vertical** whitespace beyond telehealth — does the run-020 audience cut generalize off telehealth? | value-read | yes | store-only | Reuses a clean enum cut on a new vertical. | persistence-boundary: is `audience` a clean primary axis cross-vertical? | The audience-axis generalization. | Two-enum cross-tab over the non-telehealth slice. | `audience` is likely telehealth-shaped (sparse off-vertical); thin result. |

## Selected Question(s)

1. **C1 — GLP-1 ads-transparency presence panel (bounded-live).** Recommended. Highest
   novelty (first ads source family), real reader value, directly extends the 029
   traction thread, and is autonomous-safe under a complete light bounded-live plan with
   one source family and a ≤6-capture ceiling.
2. (Runner-up) **C4 — trust-proof-device cross-vertical generalizability (store-only)** if
   a fully store-only run is preferred; lower novelty.

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "For a bounded panel of up to 6 captured GLP-1 telehealth brands, what does the Google Ads Transparency Center show about active paid-acquisition motion (running-now vs ran-only, advertising tenure, creative format), and is ads-presence a cheap, real Signal the store's current toolkit can't see — or too push-biased to trust as traction?"
selected_slug: glp1-ads-transparency-presence-panel
run_type: mixed
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live
expected_denominator: "Store GLP-1-anchored cohort (~25 brands by loose anchor_category grep; ~19 strict per run-029). The read panel is a bounded subset of up to 6 high-recognition DTC GLP-1 domains, NOT the whole cohort; report the panel as a sample, not a census."
likely_source_panel: "Google Ads Transparency Center via tools/ads_transparency.py (SerpAPI engine=google_ads_transparency_center), domain-keyed. Store telehealth.md / profile.md for the cohort denominator and brand->domain resolution (local, not an outside source)."
builder_lens: "source-family — does Google Ads Transparency presence/recency/tenure add a cheap, real acquisition-motion Signal absent from the store's signal toolkit, and what is its false-confidence boundary (push!=demand, first-page!=volume, legal-name!=brand, zero!=not-advertising)?"
reach_reason: "First lab read using ads_transparency.py and the first paid-acquisition source family of any kind; tests whether an external push-signal partially fills the thin-traction gap run-029 mapped — a frontier the store cannot see today."
allowed_sources:
  - "store/ (telehealth.md, profile.md, signals/ for the cohort + brand->domain)"
  - "tools/ads_transparency.py via SerpAPI (Google Ads Transparency Center), one capture per domain"
  - "experiments/00-market-read-lab/ (lab artifacts, discovery-ledger, triage)"
disallowed_actions:
  - "Firecrawl scrape/crawl/search or any web browsing beyond the ads_transparency tool"
  - "Meta/Instagram/Apify social-ads route (deferred)"
  - "Capturing more than 6 domains, or exceeding 6 SerpAPI credits"
  - "store/ mutation, signals/ write-back via scripts/signals.py, or any persistence"
  - "Treating ads-presence as demand/success, or reporting first-page creative count as total ad volume"
live_evidence_plan:
  budget_class: light
  evidence_goal: "Verify running-now-vs-ran-only, advertising tenure (first_shown), and creative format for a bounded GLP-1 panel; test whether ads-transparency is a cheap, real acquisition-motion Signal the store lacks, and map where it misleads."
  source_families_allowed:
    - "Google Ads Transparency Center (tools/ads_transparency.py / SerpAPI)"
  source_families_preferred:
    - "Google Ads Transparency Center (domain-keyed search — collision-proof per tool doc)"
  source_families_disallowed:
    - "Firecrawl web search/scrape/crawl"
    - "Meta/Apify social-ads route"
    - "review/forum, listicle/SERP, or any second outside family"
  ceilings:
    source_families: 1
    outside_sources_captured: 6
    paid_capture_credits: 6
  panel_selection_rule: "From the store GLP-1-anchored cohort, pick up to 6 high-recognition DTC GLP-1 domains (e.g. hims.com, ro.co, henrymeds.com, remedymeds.com, eden, lifemd.com), domain-keyed to avoid name collisions. Resolve each brand's domain from the store dir before the call."
  recency_rule: "Treat 'active' as any creative last_shown within ~35 days of captured_at; older-only = 'ran ads, not currently visible' (per tool doc)."
  fail_closed_conditions:
    - "ads_transparency.py errors persist after one retry on a domain -> log the domain as tool-error, do not substitute another family"
    - "Need would require a second source family, Meta/Apify, login/paywall, or >6 domains"
    - "Temptation to expand the panel to the whole cohort to 'complete' the census"
    - "Tool returns schema_drift / exit 3 (missing both creatives and advertisers) -> stop that domain as insufficient-evidence"
  stop_rules:
    - "Stop at 6 domains regardless of cohort size; report remaining cohort as 'not sampled'."
    - "If the panel-level pattern is unreadable after <=6 captures, stop with termination_reason: insufficient-evidence rather than broadening."
approval_needed: no
why_autonomous_safe: "Standing bounded-live policy; a single, well-documented source family (Google Ads Transparency via SerpAPI); <=6 paid SerpAPI credits (well under the 20 ceiling and 6-source ceiling); no Firecrawl, no scrape, no store write-back; zero-creatives is a clean documented result; clear fail-closed and stop rules."
loop1_failure_mode: "Overclaiming traction/demand from a push-only signal: reading ads-presence as 'doing well', reporting first-page creative count as total ad volume, mis-attributing via advertiser legal-name != brand, or reading a zero/Google-only result as 'not advertising' rather than 'not visible on this surface'. Secondary: panel-as-census overclaim (treating <=6 sampled brands as the whole cohort)."
```

## Selection Notes

C1 wins on the two-test bar: real reader value ("who's actively spending to acquire in
GLP-1?") **and** the strongest design learning available right now — it is the first lab
read on any paid-acquisition source family, it diversifies away from four consecutive
store-only meta-reads (031/032/033 + the 027/028 generalizability thread), and it puts a
concrete, bounded test under run-029's open question of whether the thin traction
substrate can be widened with a cheap external push-signal. The bounded-live plan is
deliberately one source family / <=6 captures so the run isolates exactly what
ads-transparency adds, with documented fail-closed behavior. C6 (Meta/Apify) is the only
rejected candidate — its route is deferred and not autonomous-safe.
