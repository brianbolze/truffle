# Receipt - signal_delta sweep over all ≥2-capture domains

Supports the whole change-pulse readiness read: which captured signals yield a clean temporal delta, which veto, and why.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7, C8, C9]
```

> **Loop 2 correction:** the first sweep used a company-grain glob (`store/<domain>/signals/<type>/*.json`) and missed Wayback, which is captured at *page* grain one level deeper (`signals/wayback/<page-slug>/*.json`). The adversarial verifier caught it; the Wayback sweep below (S4) is the correction. It adds a second answerable source type and confirms the distinct-domain count is 13.

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/signals/*/` (enumeration of dirs with ≥2 `*.json`) | read 2026-06-20 | local-store | derived | none | no | C1 |
| S2 | `tools/signal_delta.py` first-vs-last pairwise over each ≥2-capture dir | run 2026-06-20 | local-store | derived | none | no | C2,C3,C4,C5,C6,C7 |
| S3 | `tools/signal_delta.md` / `signal_delta.py --help` (tool semantics) | read 2026-06-20 | local-store | primary (tool doc) | none | no | C3,C6 |
| S4 | `tools/signal_delta.py` first-vs-last over each `signals/wayback/<page-slug>/` with ≥2 caps (Loop 2 correction) | run 2026-06-20 | local-store | derived | none | no | C1,C8,C9 |

## Method

1. Enumerated every `store/<domain>/signals/<source_type>/` directory holding ≥2 capture JSONs (company-grain). **Loop 2 correction:** also enumerated `signals/wayback/<page-slug>/` (page-grain, one level deeper) via `find store -path '*/signals/wayback/*' -name '*.json'` — the first pass's company-grain glob missed these.
2. For each, ran `python3 tools/signal_delta.py <first> <last>` (oldest vs newest capture by sorted timestamp).
3. Recorded per-comparison: `read_mode` (delta/level), `gap_days`, metric deltas + `velocity_per_day`, `comparability_flags`, and `vetoes`.

Result set is bounded by what is already on disk — a capture-cadence denominator, not a market census.

## Evidence

**Denominator (S1):** 135 store domains; 49 have a `signals/` dir; the following have ≥2 captures in some source_type (**13 distinct domains**):

- trustpilot ×9 (company-grain): agelessrx, eden-health, hims, honehealth, hydramed, joinamble, joinfridays, maximustribe, sermorelin
- sec_edgar ×4: hims, honehealth, maximustribe, waldo
- serpapi ×2 (multi-subject envelopes): niagenplus, waldo
- wayback ×15 page-subjects across 10 domains (**page-grain, one level deeper** — `signals/wayback/<page-slug>/`): agelessrx, eden-health, hims, honehealth, hydramed, joinamble, maximustribe, niagenplus, onemedical, struthealth

Distinct-domain union across all four types = 13 (wayback contributes onemedical + struthealth beyond the 11 in the other three types).

**Trustpilot — clean deltas (read_mode: delta, real gap ~6.2–6.6 days), ALL flagged `paid_profile`:**

| domain | review_count d0→d7 | Δ | vel/day | reviews_last_12m | gap_days |
|---|---|---|---|---|---|
| honehealth-com | 11579→11645 | +66 | 10.05 | delta=null (rolling) | 6.57 |
| hims-com | 8500→8554 | +54 | 8.68 | delta=null | 6.22 |
| joinamble-com | 3984→4035 | +51 | 7.76 | delta=null | 6.57 |
| agelessrx-com | 2271→2288 | +17 | 2.59 | delta=null | 6.57 |
| joinfridays-com | 4462→4475 | +13 | 1.98 | delta=null | 6.57 |
| maximustribe-com | 975→982 | +7 | 1.07 | delta=null | 6.57 |

`reviews_last_12m` always returns `delta: null` by design — the rolling-12m left edge moves between captures, so the tool refuses a delta (level-read only). `trust_score` is a level metric, not surfaced as a delta in the trustpilot path.

**Trustpilot — vetoes / void (3 of 9):**

- eden-health: `profile_not_found — not a live profile; nothing to level-read` + a separate `tryeden-com` subject (capture resolved a different subject; subject-alignment fence) → `unpaired_capture`, no delta.
- hydramed-com: `profile_empty_between_captures (active at D0) — comparison void, deltas empty`.
- sermorelin-com: `D0_capture_not_ok — comparison void`.

**SEC EDGAR — 0 deltas, 4/4 veto at run time:** every pair returned `no source-aware delta for 'sec_edgar' — add a branch or compare by hand`. The comparator had no sec_edgar delta branch then; the branch shipped 2026-06-22. Independently, the pairs were intra-day (e.g. hims 2026-06-15 04:27→19:03; waldo 2026-06-18 20:18→20:23), so no funding-window change existed to read anyway.

**SERP (serpapi) — 0 deltas, all unpaired:** each `serpapi/` dir holds captures of *different query subjects* (niagenplus: "at home nad+ injection" + "prescription nad+ injection"; waldo: "agentic brand intelligence" + "waldo brand intelligence"), so each subject has only one capture → `unpaired_capture`, level-read only. No repeat capture of the same query to diff.

**Wayback (S4, page-grain) — deltas produced (working branch), 13/15 flat:** 15 page-subjects across 10 domains, each `read_mode: delta` over real gaps (1.1–7.9 days). Metrics: `archive_presence`, `snapshot_count`, `last_seen`, `content_digest`.

| page-subject | snapshot_count d0→d7 | Δ | note |
|---|---|---|---|
| honehealth-com/mens/sermorelin | 0→1 | +1 | archive_presence False→True — page enters archive (last_seen 2026-05-08); the only real content-relevant move |
| onemedical-com (root) | 2517→2516 | −1 | **CONFOUND** — last_seen moves backwards 2026-06-15→2026-06-09, identical digest; CDX nondeterminism, not a real loss |
| hims-com/erectile-dysfunction/hard-mint-chewable | 51→51 | 0 | flat (digest identical) |
| honehealth-com/longevity/nad | 12→12 | 0 | flat |
| maximustribe-com/testosterone/enclomiphene-only | 19→19 | 0 | flat |
| niagenplus-com (root) | 60→60 | 0 | flat |
| agelessrx-com/sermorelin, eden-health root, honehealth/mens-enclomiphene, hydramed/rx-semorelin, joinamble/sermorelin, maximustribe/…cream, struthealth/blog… | unchanged | 0 | flat (archive static between captures) |
| hims-com/testosterone/enclomiphene-supplements, …tadalafil-supplements | 0→0 | 0 | never archived (archive_presence False/False) |

13 of 15 are delta=0 because the Wayback CDX archive only re-crawls on its own (~monthly) cadence; a day/week-spaced re-capture reads the same archived state. The Wayback delta therefore measures *archiver re-crawl*, not *brand page change*.

## Limits

- Cannot prove a brand did *not* change — only that no detectable change exists *between the two captured snapshots*. Two snapshots ≠ continuous monitoring.
- The clean Trustpilot deltas are `review_count` (cumulative, monotone) on `paid_profile` profiles — velocity reflects review-solicitation cadence, not organic sentiment, and says nothing about score or objection mix.
- Denominator is capture-cadence-bound (~13 domains, mostly one source type, one ~1-week window); not a market read.

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Only ~13 domains have ≥2 captures in any one source_type; trustpilot dominant | S1 | Snapshot of disk at 2026-06-20 |
| C2 | 6 trustpilot profiles yield a clean per-day review-velocity delta over a real ~6.5-day gap | S2 | All carry paid_profile |
| C3 | The only delta-able trustpilot metric is cumulative review_count; reviews_last_12m and trust_score are level-only | S2,S3 | Rolling-window + path design |
| C4 | 3 of 9 trustpilot pairs veto (subject realignment, empty-between, D0-not-ok) | S2 | Fail-closed, not silent skip |
| C5 | SEC change-pulse was unsupported at run time: no sec_edgar delta branch then (shipped 2026-06-22), and captures were intra-day | S2 | Cadence gap remains |
| C6 | SERP change-pulse is unsupported: captures are one-per-query (unpaired) | S2,S3 | Need repeat same-subject capture |
| C7 | Every clean trustpilot velocity carries paid_profile — the delta-able metric is the least decision-relevant one | S2 | Temporal flavor of MRL-008 |
| C8 | Wayback diffs cleanly (working branch) but 13/15 page-subjects are delta=0 — captures spaced faster than the archive re-crawls | S4 | Measures archiver re-crawl, not page change |
| C9 | Wayback confound: onemedical snapshot_count −1 with last_seen moving backwards = CDX API nondeterminism | S4 | Second confound flavor, source-mechanics |
