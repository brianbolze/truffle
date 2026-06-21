# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [source-panel, depth-backfill, coverage-caveat, source-rigor, tooling-ergonomics]
```

## 30-second operator read

- **Did the run work?** Yes. First lab read on the **ads / paid-acquisition** source
  family. 6 GLP-1 domains captured via `ads_transparency.py` (6 SerpAPI credits, at the
  planned ceiling). Clean three-state result: 2 active (hims, ro), 2 ran-but-quiet
  (henrymeds, lifemd), 2 zero-on-surface (remedymeds, eden).
- **What was awkward?** Nothing in execution — the tool is well-documented and bounded.
  The interpretive discipline is the whole game: it is a push/budget signal, not demand.
- **What should the next agent know?** The store sees **1/130** ads signals (waldo only),
  **0** GLP-1 — the gap is coverage, not architecture (mirrors run-029). The four
  false-confidence traps (push!=demand, first-page!=volume, legal-name!=brand,
  zero!=not-advertising) are all live; the read avoided each by name.

## What happened

Gated on `run_status: scout-only` + a complete `bounded-live` Selected Run Contract
(1 source family, <=6 captures). Resolved 6 GLP-1 panel domains from `store/<dir>/profile.md`
`domain:` lines -> ran `tools/ads_transparency.py <domain> --region US` once each
(6 credits) -> parsed `ad_creatives[]` for recency/tenure/format -> checked store ads
coverage (`ls -d store/*/signals/ads_transparency`). Receipts saved under
`receipts/ads/*.json` + summarized in `receipts/ads-transparency-panel-2026-06-20.md`.
No Firecrawl, no scrape, no store write-back. Stayed at the 6-credit ceiling exactly.

## Discovery ledger

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | First lab read on the **ads / paid-acquisition** source family. A 6-brand GLP-1 panel splits cleanly into 3 readable states: active (hims, ro — last_shown 2026-06-20), ran-but-quiet (henrymeds ~209d, lifemd ~309d), zero-on-surface (remedymeds, eden). 1 SerpAPI credit each. | read.md Result; receipt Evidence table | The ads tool delivers a real, discriminating push-signal cheaply — a source family none of the 33 prior reads touched. | ready-for-triage |
| O2 | observation | The signal is **push/resourcing, not demand**: presence/recency/tenure/format are informative about *budget + acquisition motion* and silent about conversion/outcome. Cleanest single illustration of run-029's push-vs-demand traction split. | read.md Result, Market Pattern #3; tool doc | Pins exactly what an ads signal can and cannot contribute to a traction read — the boundary the traction frame must encode. | ready-for-triage |
| O3 | observation | **Advertiser legal-name != brand**: ro->"Roman Health Ventures Inc.", henrymeds->"ADONIS HEALTH INC.", lifemd->"LifeMD, Inc.". Domain-keyed search (not name) avoided mis-attribution. | receipt Evidence table | A real entity-resolution surface the store lacks; a name-keyed read would silently mis-attribute. Mirrors tool doc's Hone->TIME THERAPEUTICS. | ready-for-triage |
| O4 | observation | **Tenure != current activity**: lifemd has 2nd-longest tenure (since 2022) but went quiet on Google ~10 months ago. Recency and tenure are independent axes. | read.md Market Pattern #2; receipt | A naive "long tenure = active advertiser" read inverts lifemd; both axes must travel together. | recur-watch |
| O5 | observation | **first-page count != ad volume**: ro.co's `n_creatives_first_page: 40` is the page cap, not "ro runs 40 ads"; hims 14, henrymeds 2, lifemd 1 are also first-page-only. | read.md Gap Map trap #2; tool doc | The count field is the most tempting and least safe number on the surface; only presence/recency/tenure/format are decision-grade. | ready-for-triage |
| S1 | surprise | **Zero != not advertising**: remedymeds + eden returned clean zero = not visible on Google Transparency for that exact `target_domain`; they may run Meta ads or land on a different domain (`eden.health` is itself an uncertain ad-landing key). | read.md trap #4; receipt Limits | A structured zero is a coverage/channel signal, not a market fact — a direct recurrence of the MRL-008 run-028/033 "empty structured surface != market absence" branch, now on an *external* source. | ready-for-triage |
| G1 | gap | **Ads source family is essentially uncaptured: 1/130 store-wide (waldo-fyi), 0 GLP-1.** Tool exists + `ads_transparency` source_type resolves, but coverage ~= 0. | read.md Gap Map; `ls -d store/*/signals/ads_transparency` | The structural gap-probe answer: a cheap, working push-signal the store cannot see — coverage, not architecture (mirrors run-029 "machinery ahead of coverage"). | ready-for-triage |
| W1 | wish | If anything graduates it is **capture coverage** (run the tool across a real cohort) + a **`signal_delta.py` ads branch** for time-deltas — NOT a new primitive. Both spend/approval-gated. | read.md What Would Change | Names the lightest path (consistent with run-029 W1: coverage + comparator branch, no new primitive). | recur-watch |
| F1 | friction | Per-domain brand->`domain:` resolution + per-domain JSON parse was hand-rolled; no MRL-002 recipe covers "enumerate ads-presence across a panel." | this run | Mirrors the recurring MRL-002 query-machinery friction (now on the ads grain); one sighting, recur-watch. | recur-watch |

## Inputs and scope

- **Cohort/denominator:** `grep -rl 'anchor_category:.*GLP-1' store/*/telehealth.md` -> 25
  brands (loose; ~19 strict per run-029). Panel = 6 of these, reported as a sample.
- **Panel domains** (resolved from `store/<dir>/profile.md`): hims.com, ro.co,
  henrymeds.com, remedymeds.com, eden.health, lifemd.com.
- **Tool:** `tools/ads_transparency.py <domain> --region US`, one call per domain.
- **Exclusions:** the other ~19 cohort brands (not sampled); non-Google channels
  (Meta/Apify, disallowed); no time-delta (single capture).

## Live evidence plan

```yaml
live_evidence_plan:
  budget_class: light
  evidence_goal: "Verify running-now-vs-ran-only, advertising tenure, creative format for a bounded GLP-1 panel; test whether ads-transparency is a cheap, real acquisition-motion Signal the store lacks, and map where it misleads."
  source_families_allowed: ["Google Ads Transparency Center (tools/ads_transparency.py / SerpAPI)"]
  ceilings: {source_families: 1, outside_sources_captured: 6, paid_capture_credits: 6}
  recency_rule: "active = last_shown within ~35 days of captured_at"
  fail_closed_conditions:
    - "tool error persists after one retry on a domain -> log as tool-error, no family substitution"
    - "need would require a 2nd family / Meta-Apify / login / >6 domains"
    - "temptation to expand to the whole cohort"
    - "schema_drift / exit 3 -> stop that domain insufficient-evidence"
  stop_rules:
    - "stop at 6 domains; report rest as not sampled"
    - "if unreadable after <=6 captures, stop insufficient-evidence not broaden"
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "ads_transparency.py hims.com --region US"
    source_family: ads/social (Google Ads Transparency Center)
    action_taken: captured
    reason: "panel member — recency/tenure/format"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C2, C3, C5]
  - source_or_query: "ads_transparency.py ro.co --region US"
    source_family: ads/social
    action_taken: captured
    reason: "panel member"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C2, C3, C4, C5]
  - source_or_query: "ads_transparency.py henrymeds.com --region US"
    source_family: ads/social
    action_taken: captured
    reason: "panel member"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C2, C5, C6]
  - source_or_query: "ads_transparency.py remedymeds.com --region US"
    source_family: ads/social
    action_taken: captured
    reason: "panel member (clean zero)"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C7]
  - source_or_query: "ads_transparency.py eden.health --region US"
    source_family: ads/social
    action_taken: captured
    reason: "panel member (clean zero)"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C7]
  - source_or_query: "ads_transparency.py lifemd.com --region US"
    source_family: ads/social
    action_taken: captured
    reason: "panel member"
    source_grade: primary
    captured_at: 2026-06-21
    spend_note: paid-credit
    claim_ids_supported: [C1, C2, C6]
```

Total: 1 source family, 6 outside captures, 6 paid SerpAPI credits — exactly at the planned
light ceiling, 0 over. `store/*/signals` coverage check is a local-store query, not an
outside source.

## Friction log

Brand->domain resolution and per-domain creative parsing were hand-rolled (F1) — one
sighting of the recurring MRL-002 query-machinery friction on a new (ads) grain. Not a
tooling ask yet.

## Evidence limits

- **Panel, not census** (6 of ~19–25); the read is a source-family probe, not a cohort map.
- **Single point, single region (US).** No time-delta; tenure is first/last bookends only.
- **Two zeros unresolved** — could be domain-keying/channel artifacts, not true absence.
- **Push/budget only** — no demand, conversion, or performance is observable.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **pass** (1 family / 6 captures / 6 credits, at ceiling)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **pass** (6/6)
- If `bounded-live`, stop rules and spend notes were recorded: **pass**
- No disallowed action happened: **pass** (no Firecrawl, no Meta/Apify, no >6 domains, no write-back)
- Required citations / receipts present and source-graded: **pass** (receipt + 6 JSON captures, primary)
- No snippet treated as evidence: **pass** (primary SerpAPI captures, not snippets)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (2026-06-21, primary)
- Absence language says "not found", not "not true": **pass** (zeros framed as "not visible on this surface")

All items pass -> `run_status: read-done`.

## Surprises

The strongest single surprise is **zero != not advertising** (S1): a clean structured zero
on an *external* source is a coverage/channel signal, not a market fact — the MRL-008
run-028/033 "empty structured surface != market absence" branch recurring outside the store,
on a live source. Secondary: advertiser legal-names diverge sharply from brand (O3).

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `source-panel` | First use of the ads/social source family; a repeatable per-cohort ads-presence panel shape emerged. | watch for recurrence (2nd ads read would name the recipe) |
| `depth-backfill` | Ads signal captured for 1/130 (0 GLP-1) despite a working tool + resolving source_type. | submit triage evidence (coverage gap, MRL-029-adjacent) |
| `coverage-caveat` | Panel of 6, two unresolved zeros, no time-delta. | no-op (inherent to a bounded probe) |
| `source-rigor` | Four live false-confidence traps (push!=demand, first-page!=volume, legal-name!=brand, zero!=not-advertising). | submit MRL-008 evidence (external-source confound flavor) |
| `tooling-ergonomics` | Hand-rolled brand->domain + parse (F1). | watch for recurrence |

"No new primitive needed" to *consume* the signal — the gap is coverage + a delta branch.

## Optional triage evidence

Deferred to Loop 2 per the operator contract. Candidate shapes (for Loop 2 to weigh, not
to graduate):
- **MRL-008 external-source branch:** ads-transparency adds 4 confound flavors — push!=demand,
  first-page!=volume, legal-name!=brand, structured-zero!=absence (the last is a direct
  recurrence of the run-028/033 branch on a *live external* source). See O2/O3/O5/S1.
- **MRL-029 / traction-coverage:** ads is a real push-side traction ingredient captured for
  1/130; widening it is coverage + a `signal_delta.py` ads branch, not a new primitive (G1/W1).

## Next-run advice

- A **2nd ads read** (different cohort, or a Meta/Apify route if approved) would (a) name the
  ads-presence panel recipe and (b) resolve whether the Google-zeros advertise off-Google.
- If repeating, consider **ad-landing-domain resolution** (a brand may target `try<brand>.com`,
  not its store `domain:` key) before calling a zero a zero.
- Keep it bounded: 1 credit/domain makes a 6–10 brand panel cheap, but the interpretive
  discipline (push, not demand) is the load-bearing part, not the coverage.
