# Scout

## Prior Context Read

- `triage.md`: Most-recurrent unresolved theme is **relations/neighborhood** — MRL-005 (named-counterparty edge), MRL-006 (capture-grain split), MRL-011 (competitive/substitute as a buyer-relative Judgment). Every relation read to date (001/014/016/017/026) used store-prose or store frontmatter; none reached outside for **demand-side** evidence of who buyers actually cross-shop. MRL-011 is explicitly a *single sighting* (Hone, run 017) held for a second.
- `scout-context.md`: Select for value + reach + source-family diversity, not store-answerability. Gap-probes are first-class. Bounded-live needs a filled plan with light ceilings + fail-closed rules. Name the builder lens.
- Last 3 `run-notes.md` files (027/028/029): 027 + 028 opened the cross-vertical frontier (taxonomy + read recipes generalize off telehealth); 029 mapped traction-readiness (plumbing yes, substance thin). All three were store-only. The lab has now run ~26 store-only reads and **only 4 bounded-live reads, exercising just 2 external source families** (Trustpilot review bodies once; listicle/SERP coverage-radar 3×). Three live tools — `exa_similar.py`, `trends.py`, `ads_transparency.py` — have **never been driven by a market read**.
- Current run artifacts: fresh scaffold; no prior scout.md/receipts.

## Candidate Questions

Slate generated for value + reach + source-family diversity. Selection driver this round: **bring in fresh external data on an under-probed axis** (Brian's explicit ask — get more ambitious, probe what we haven't). Candidate A was green-lit by Brian 2026-06-20.

| Question | Mode | Autonomous eligible? | Evidence mode | Why this is worth a run | Builder lens / design test | What it reaches / probes | Trustworthy evidence would require | Failure mode to watch |
|---|---|---|---|---|---|---|---|---|
| **A (SELECTED).** For Hone Health as anchor, who do buyers actually cross-shop, per external demand-side evidence (Exa neighbors + owned/third-party comparison pages) — and does that confirm or overturn run 017's store-only substitute/adjacent tiering? | gap-probe | yes | bounded-live | First demand-side relation probe in the lab; directly tests MRL-011's buyer-relative Judgment against outside evidence; first use of the dormant `exa_similar.py`. A/B against an existing store-only read (017). | relation-pressure: does external demand-side evidence (a) move the substitute-vs-adjacent line set store-only, and (b) surface neighbors the anchored-only `anchor_category` grep missed (the MRL-001 under-count)? | Exa neighbor-graph + real comparison/relationship pages — outside the store's prose-only relation substrate. | Treating an Exa rank or a single "alternatives to" listicle as truth; conflating co-mention with substitution; letting the panel sprawl past 2 families. |
| B. True GLP-1/TRT price floor incl. manufacturer-direct (NovoCare, LillyDirect) + retail/cash-pay (Walmart, GoodRx) vs the DTC premium. | gap-probe | yes | bounded-live | DTC-only corpus is blind to the cheapest access path by construction; maximally brief-worthy. | source-panel + denominator: a category/reference-level price signal with no company home (MRL-007 cousin). | Manufacturer/retail pricing pages outside the DTC set. | Stale/promotional reference prices read as steady-state; scope creep across retailers. |
| C. Current regulatory status of the compounded-GLP-1 model (FDA 503A/503B, shortage list, warning letters) — is this a homeless category-level signal? | gap-probe | yes | bounded-live | The parked MRL-007 homeless-signal, never revisited since run 002; timely. | persistence boundary / non-company entity: where does a cohort-governing signal live? | FDA shortage DB + warning-letter search. | Regulatory surfaces sprawl; snippet-grade legal claims. |
| D. Live-ad positioning vs owned-page positioning + branded search demand on the GLP-1 cohort. | value-read | yes | bounded-live | First use of `ads_transparency.py` + `trends.py`; ads are an untouched ingredient family. | source-panel: does the acquisition surface reveal claims owned pages hide? Neutral attention denominator for run 029's thin traction map. | Google Ads Transparency + Google Trends. | Trends relativity/noise; ad copy over-read. |
| E. Cross-vertical variant of A — run the cross-shop map on a SaaS anchor (PostHog/Notion) instead. | gap-probe | yes | bounded-live | Tests whether the demand-side recipe generalizes off telehealth (extends 027/028 to the external layer). | relation-pressure × generalizability. | Exa + "alternatives to X" + G2/`/vs` pages. | Over-generalizing from one SaaS anchor. |

## Selected Question(s)

1. **A** — For Hone Health as anchor, who do buyers actually cross-shop (per Exa neighbors + owned/third-party comparison pages), and does external demand-side evidence confirm or overturn run 017's store-only substitute/adjacent tiering? *(Green-lit by Brian, 2026-06-20.)*

## Selected Run Contract

This is the canonical handoff to Loop 1. If this block and the candidate table disagree,
Loop 1 should trust this block.

```yaml
selected_question: "Across a multi-anchor set of captured companies (~15-20 telehealth brands + 3-5 SaaS brands, with Hone Health as the calibration anchor), who do buyers actually cross-shop with per external demand-side evidence (Exa /findSimilar neighbors + owned and third-party comparison pages) — which neighbors recur as cross-shop HUBS across anchors, which are store-absent (the selection-bias under-count), and does the external set confirm or overturn run 017's store-only Hone substitute/adjacent tiering? Does the recipe generalize off telehealth to SaaS?"
selected_slug: external-cross-shop-neighbor-map
run_type: market
question_mode: gap-probe
autonomous_eligible: yes
evidence_mode: bounded-live   # EXPANDED budget, operator-approved (see approval_note) — exceeds the default light envelope
expected_denominator: "Per anchor: the store's anchored-only cohort (anchor_category grep) as the baseline, plus run 017's 16-brand tiering specifically for Hone. The external demand-side neighbor graph is the comparison set; the delta (store-absent neighbors, cross-anchor hubs) IS the finding."
likely_source_panel: "Exa /findSimilar across ~15-20 telehealth anchors + 3-5 SaaS anchors (tools/exa_similar.py); SERP 'alternatives to X' / 'X vs' direction-finding; owned + third-party comparison pages scraped for Hone + the top recurring hubs (not every anchor)."
builder_lens: "relation-pressure — does external demand-side evidence (a) move run 017's store-only substitute/adjacent line, (b) surface cross-shopped neighbors the anchored-only anchor_category grep cannot see (MRL-001 selection-bias, now quantified across MANY anchors at once), and (c) reveal cross-anchor HUBS that a single-company relation read can't? Plus a generalizability probe: does the external demand-side recipe run off-telehealth on SaaS (extends 027/028 to the external layer)? Tests whether MRL-011's competitive/substitute surface needs outside evidence to be trustworthy."
reach_reason: "Every prior relation read (001/014/016/017/026) used store-internal prose/frontmatter on a single cohort. This is the first MULTI-anchor demand-side graph, the first read to drive exa_similar.py, the first to score cross-anchor neighbor recurrence, and the first cross-vertical external read. It calibrates a specific prior store-only judgment (017) AND maps an under-count the store cannot see by construction."
allowed_sources:
  - "tools/exa_similar.py output (Exa /findSimilar, neighbor-graph family) across the selected anchor set"
  - "store/ (run 017 read.md + per-anchor profiles/telehealth.md + the Technology slice, for baselines and store-match joins)"
  - "owned + third-party comparison/relationship pages (/vs, /compare; third-party 'alternatives to X' pages), reached via SERP direction-finding"
  - "SERP queries ('alternatives to X', 'X vs') as direction-finding + cross-shop corroboration"
  - "experiments/00-market-read-lab/ artifacts (017 prior read)"
disallowed_actions:
  - "Do not mutate store/ or write back to any project system"
  - "Do not add a competitors:/similar_to: field, edge table, or any durable primitive"
  - "Do not capture review/forum bodies, ads, or regulatory surfaces (out-of-family for this run)"
  - "Do not use login-gated, paywalled, or private sources; no open-ended crawl; no recursion into neighbors-of-neighbors beyond depth 1"
  - "Do not treat an Exa rank, a SERP snippet, or a single comparison page as truth; require cross-source/cross-anchor corroboration before confident language"
live_evidence_plan:
  evidence_goal: "Build a multi-anchor demand-side neighbor graph: score cross-anchor recurrence (hubs), match neighbors against the store (store-absent under-count worklist), calibrate Hone vs run 017, and test whether the recipe generalizes to SaaS."
  budget_class: expanded   # operator-approved; NOT the default light envelope
  allowed_source_families:
    - "neighbor-graph (Exa /findSimilar via tools/exa_similar.py)"
    - "comparison/relationship pages (owned /vs + /compare and third-party 'alternatives to' pages)"
    - "SERP (serpapi/firecrawl_search) — direction-finding to locate comparison pages + 'alternatives to X' corroboration"
  preferred_signal: "cross-ANCHOR recurrence (a neighbor surfacing for many anchors = a hub) AND cross-SOURCE recurrence (a neighbor in BOTH Exa and a comparison/SERP page = high-signal cross-shop nominee). Single-source, single-anchor names are weak nominees."
  disallowed_source_families:
    - "review/forum bodies, ads transparency, regulatory surfaces, listicle leaderboards (reserved for other candidate runs)"
  ceilings:
    source_families_max: 3
    exa_calls_max: 30          # ~25 anchors x 1 call (25 neighbors each); ~$0.30-0.60 total
    serp_queries_max: 20       # focused on Hone + top hubs, not every anchor
    firecrawl_scrapes_max: 25  # comparison pages for Hone + top recurring hubs only
  stop_rules:
    - "Fail closed to insufficient-evidence before exceeding ANY ceiling (exa 30 / serp 20 / firecrawl 25 / families 3)."
    - "Fail closed if a 4th source family (reviews/ads/regulatory/listicle) becomes necessary — note it as a finding, do not add it."
    - "Do NOT scrape comparison pages for every anchor — restrict the comparison-page family to Hone (calibration) + the top recurring hubs."
    - "Do NOT recurse into neighbors-of-neighbors (depth-1 only); no open-ended crawl; no multi-hop graph expansion."
    - "Fail closed if a comparison page requires login/paywall/private access."
approval_needed: no
approval_note: "Brian green-lit an EXPANDED bounded-live budget + the cross-vertical SaaS add-on in-session 2026-06-20, deliberately exceeding the default light ceiling (2 families / 6 sources / 20 credits). This is an operator-supervised run, not standing unattended policy; the light envelope remains the default for autonomous runs."
why_autonomous_safe: "Operator-approved expanded bounded-live: every outside source logged in live_evidence_used, hard per-tool ceilings, depth-1-only, fail-closed stop rules, no write-back, no durable-primitive creation. Exa metered in cents; SERP/Firecrawl bounded by explicit caps."
loop1_failure_mode: "Budget sprawl across 25 anchors (over-scraping comparison pages for every anchor instead of focusing on Hone + hubs); over-claiming substitution from Exa proximity or co-mention (Exa rank is similarity, not a cross-shop fact); reading a store-absent neighbor as 'not in the market' rather than 'not captured'. Mirror of MRL-011: substitute-vs-adjacent is buyer-relative — label it Judgment, not derive it as fact."
```

## Selection Notes

Question-selection policy lives in `scout-context.md`. Candidate A was chosen from a 5-candidate slate (A–E above) because it scores highest on the round's driver — fresh external data on an under-probed axis — while attacking the single most-recurrent unresolved triage theme (relations, MRL-005/006/011) and exercising a built-but-dormant tool (`exa_similar.py`). Hone is the anchor specifically because run 017 already produced a store-only substitute/adjacent map for it, making this a clean A/B calibration of MRL-011 rather than a standalone read. Candidates B–E remain valid future scouts; B and C were also recommended but not green-lit this round.
