# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [relation-pressure, source-rigor, source-panel, coverage-caveat, tooling-ergonomics]
```

## 30-second operator read

- **Did the run work?** Yes — first multi-anchor demand-side graph, first use of `exa_similar.py`,
  first cross-vertical external read. Clean, decisive, on-budget.
- **Headline:** neither external demand-side source gives a trustworthy cross-shop map. Exa
  `/findSimilar` is **name/semantic similarity, not cross-shop** (1/16 recall vs run 017);
  "alternatives to X" pages are better (4/16) but **owned-`/vs` SEO-self-selected**. Run 017's
  store-only read is **partially corroborated, not overturned** → vindicates MRL-011's no-`competitors:`-field.
- **What was awkward:** had to hand-write `analyze.py` for the cross-anchor orchestration (Exa is
  match-free by design). Firecrawl search outputs were too big for context (delegated extraction to
  Sonnet subagents).
- **Next agent (Loop 2):** verify the 1/16 and 4/16 recall counts against the receipts; pressure-test
  the "Exa ≠ cross-shop" claim and the owned-`/vs` self-selection confound; append discovery rows.

## What happened

Scout selected candidate A (green-lit by Brian, expanded to multi-anchor + cross-vertical with
operator-approved budget). Loop 1: (1) picked 18 telehealth anchors spread across cohorts (deep on
Hone's run-017 universe = longevity/NAD + TRT + labs) + 5 SaaS anchors; (2) ran Exa `/findSimilar` ×
24 (incl. 1 Hone smoke test), 25 neighbors each → `receipts/exa/`; (3) wrote `receipts/analyze.py`
to apex-fold, dedupe, score cross-anchor hubs, match against the store, and calibrate Hone vs run 017
→ `receipts/analysis-output.txt`; (4) tested the comparison-page family via `firecrawl_search` on
Hone (calibration), Ro (GLP-1), Notion (common-name SaaS), extraction via 2 Sonnet subagents →
`receipts/comparison-pages-2026-06-20.md`; (5) wrote `read.md`. No store mutation, no primitive, no
write-back; depth-1 only; 2 source families.

## Discovery ledger

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | Exa `/findSimilar` recall vs run 017's 16 store-only Hone neighbors = **1/16** (`hormonemd` only); all 4 Tier-1 substitutes missed. Exa similarity ≈ page/name/embedding match, not cross-shop. | read.md C2; `analysis-output.txt` | First use of the dormant tool by a market read shows it does **not** deliver the demand-side relation signal MRL-005/006/011 needs. | ready-for-triage |
| O2 | source-idea | Store-absent cross-shop nominees surfaced by comparison pages: **Numan, Male Excel, Fountain TRT, Viking Alternative Medicine** (Hone/TRT), **Sesame** (Ro/GLP-1). | read.md C8; `comparison-pages-2026-06-20.md` Q1,Q2 | A small, real `/research-company` capture worklist (MRL-009) — the run's actionable corpus-growth output. | ready-for-triage |
| O3 | observation | Comparison-page recall = **4/16** (Defy Medical, Peter MD, Maximus, Lifeforce, incl. 2/4 Tier-1) — 4× Exa — but only **1 of 5 result pages was a neutral third-party listicle** (3 owned `/vs`, 1 competitor-intel, 1 affiliate). | read.md C6,C7 | Demand-side "alternatives" sets are biased toward who-wrote-the-page (SEO self-selection); cross-source recurrence is the only usable filter. | ready-for-triage |
| O4 | observation | GoodRx "alternatives to Ro" page named **drugs** (Qsymia/Contrave/Orlistat/Phentermine), not telehealth platforms. | read.md C9; `comparison-pages-2026-06-20.md` Q2 | A category-extraction confound mirroring run-024's payers-not-platforms (MRL-008 family) — corrupts set membership at extraction. | ready-for-triage |
| S1 | surprise | Exa quality tracks **anchor-name distinctiveness**: `posthog`→real rivals (Plausible/Matomo/Statsig/Clickhouse); `hims`→bit.ly/mailchi.mp/HMS-Holdings; `notion`→notion.so/Notion-Wave/OneNote; `ro`→Roon/ro.am/Rvo. | read.md C3,C4; `receipts/exa/*.json` | The tool's usefulness is name-bound, not vertical-bound — a sharp, generalizable boundary on `exa_similar.py`. | recur-watch |
| S2 | surprise | The captured GLP-1 leaders (ro/hims/henrymeds/remedymeds) barely surface **each other** in Exa despite all being in-store; only `honehealth` + `hormonemd` recur as STORE hubs. | `analysis-output.txt` (hubs) | Confirms Exa ≠ competitive map even inside a tight, well-captured cohort — the strongest single disproof. | recur-watch |
| G1 | gap | No source in the panel converts the substitute/adjacent judgment into a **joinable fact**; demand-side inputs are too noisy/biased. | read.md Gap Map | Reinforces MRL-011 with demand-side evidence: the `competitors:`-field inputs are unreliable → don't build it. | ready-for-triage |
| W1 | wish/source-idea | The cleanest demand-side cross-shop signal observed is the **owned `/vs` page read as a directed edge** ("who did brand X choose to attack") — biased but self-declared, cheap, capturable. | read.md Source Gaps; Market Pattern | A different, lighter relation primitive than a listicle named-set or an Exa list — worth a future probe. | recur-watch |
| W2 | wish | A **review-platform "people also viewed" / search co-occurrence** panel (untested here) may be the cleaner cross-shop source than either family tried. | read.md What Would Change | Names the next demand-side source to test before concluding "no good external cross-shop signal exists." | notice-only |
| F1 | friction | Cross-anchor orchestration (apex-fold, dedupe, store-match, hub-score) had to be **hand-written** (`analyze.py`); `exa_similar.py` is match-free by design, so every caller rebuilds this. | `receipts/analyze.py` | Mirrors the recurring MRL-002 query-machinery friction, now on the *external-neighbor* grain; one sighting. | recur-watch |
| V1 | trap-avoided | The per-anchor store-absent-neighbor rate (0–3/25) **looks** like a selection-bias measurement but isn't — the denominator (Exa neighbors) is mostly noise the store correctly skips. | read.md Missing/Stale Coverage | Avoided over-claiming a coverage gap from a junk denominator (contrast the clean listicle-based selection-bias reads 022/024). | notice-only |

## Inputs and scope

- **Anchors (23):** 18 telehealth (honehealth + mylifeforce/gethealthspan/gogeviti/agelessrx,
  defymedical/marekhealth/maximustribe/hormonemd, functionhealth, ro/hims/henrymeds/remedymeds,
  rexmd/bluechew, lifemd/nurx) + 5 SaaS (posthog/notion/linear/airtable/snowflake).
- **Store baseline:** 126 profiled domains; run 017's 16-brand Hone tiering for calibration.
- **Exclusions:** depth-1 only (no neighbors-of-neighbors); comparison-page family run only for
  Hone + Ro + Notion (not every anchor), per the contract's hub-focus stop rule.

## Live evidence plan

```yaml
live_evidence_plan:
  evidence_goal: "Multi-anchor demand-side neighbor graph: score cross-anchor hubs, match vs store, calibrate Hone vs run 017, test SaaS generalization."
  budget_class: expanded   # operator-approved (Brian 2026-06-20); exceeds default light envelope
  allowed_source_families: [exa-neighbor-graph, comparison/relationship-pages, SERP-direction-finding]
  ceilings: { source_families_max: 3, exa_calls_max: 30, serp_queries_max: 20, firecrawl_scrapes_max: 25 }
  stop_rules: "fail closed before any ceiling; no 4th family; comparison pages for Hone+hubs only; depth-1; no login/paywall."
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "Exa /findSimilar on 23 anchors (24 calls incl. honehealth smoke test), 25 neighbors each"
    source_family: exa-neighbor-graph
    action_taken: captured
    reason: "Build the demand-side neighbor graph + Hone calibration (C1-C5, S1-S2)."
    source_grade: secondary   # similarity signal, not adjudicated cross-shop
    captured_at: 2026-06-20
    spend_note: paid-credit   # ~$0.022/call x 24 ≈ $0.53 (Exa meters USD); under exa_calls_max 30
    claim_ids_supported: [C1, C2, C3, C4, C5]
  - source_or_query: "firecrawl_search 'Hone Health alternatives competitors' (limit 5, markdown)"
    source_family: comparison/relationship-pages
    action_taken: scraped
    reason: "Calibration: does the comparison-page family recover 017's Hone neighbors? (C6, C7)"
    source_grade: secondary   # owned-/vs + affiliate + competitor-intel; demand-side leads
    captured_at: 2026-06-20
    spend_note: paid-credit   # ~6 Firecrawl credits
    claim_ids_supported: [C6, C7, C8]
  - source_or_query: "firecrawl_search 'best alternatives to Ro telehealth weight loss GLP-1' (limit 5, markdown)"
    source_family: comparison/relationship-pages
    action_taken: scraped
    reason: "Second-anchor (GLP-1) test of the comparison-page family (C9)."
    source_grade: secondary
    captured_at: 2026-06-20
    spend_note: paid-credit   # ~6 Firecrawl credits
    claim_ids_supported: [C8, C9]
  - source_or_query: "firecrawl_search 'Notion alternatives competitors' (limit 5, summary)"
    source_family: comparison/relationship-pages
    action_taken: scraped
    reason: "Cross-vertical common-name test: do comparison pages rescue the case Exa fails? (C10)"
    source_grade: secondary
    captured_at: 2026-06-20
    spend_note: paid-credit   # 6 Firecrawl credits
    claim_ids_supported: [C10]
# Totals: Exa 24 calls (~$0.53) / 3 firecrawl searches (~18 credits) / 2 source families used (3rd allowed, unused).
# All under ceilings (exa 30, serp 20, firecrawl 25, families 3). No ceiling breach.
```

## Friction log

- `exa_similar.py` is deliberately match-free, so the entire discovery layer (apex-fold mirrors,
  dedupe across anchors, score cross-anchor recurrence, match neighbors to the store) was hand-built
  in `analyze.py` (F1). Reasonable for one run; a recurring external-neighbor read would want a
  documented recipe, not a helper, per the engine's "conventions not infra" line.
- `firecrawl_search` with `scrapeOptions` returns full page markdown that blew the context cap; the
  fix (Sonnet subagents reading the tool-result files) worked and kept bulk text out of context.

## Evidence limits

- Named sets from comparison pages are **secondary/direction-finding** — affiliate, owned-`/vs`, and
  competitor-intel confounded. Used as leads (capture nominees, recall calibration), never as truth.
- Comparison-page family tested on 3 anchors only (Hone/Ro/Notion), not all 23 — a budget-scoped
  choice, so the 4/16 recall is a single calibration point, not a distribution.
- Exa `score` intentionally dropped (rank only, per tool doc); ranks used ordinally.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was planned `bounded-live`: **pass**
- `approval_needed: no` (operator-approved expanded budget): **pass**
- `live_evidence_plan` present and followed: **pass**
- Every outside source logged in `live_evidence_used`: **pass**
- Stop rules and spend notes recorded: **pass** (no ceiling breached; 2 of 3 families used; depth-1)
- No disallowed action happened: **pass** (no store mutation, no primitive, no write-back)
- Required citations / receipts present and source-graded: **pass** (C1–C10 → receipts)
- No snippet treated as evidence: **pass** (named sets labeled secondary leads)
- Current/pricing/policy claims carry capture dates and source grade: **pass** (Exa `captured_at`; search date 2026-06-20)
- Absence language says "not found", not "not true": **pass**

## Surprises

- Exa quality is **name-distinctiveness-bound, not vertical-bound** (S1) — the cleanest cross-vertical
  finding, and the opposite of what "exercise the dormant tool" assumed (we expected a usable
  neighbor signal; got a name-matcher).
- The store's own GLP-1 leaders don't surface each other in Exa (S2) — the most direct disproof that
  `/findSimilar` is a competitive-map source.

## Pressure tags

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `relation-pressure` | First demand-side relation probe; neither external source gives a joinable cross-shop fact (G1) | submit triage candidate — reinforces MRL-011 with demand-side evidence (don't build `competitors:`) |
| `source-rigor` | Exa similarity≠cross-shop (O1/S1), owned-`/vs` self-selection (O3), drugs-not-platforms extraction confound (O4) | submit triage candidate — new MRL-008 flavors (external-similarity + demand-side-source confounds) |
| `source-panel` | Tested which external source serves cross-shop; neither graduation-grade; named the untested cleaner ones (W1/W2) | watch for recurrence — pairs with MRL-011 |
| `coverage-caveat` | Store-absent nominees (O2) + the not-a-clean-selection-bias caveat (V1) | watch — small MRL-009 capture worklist; no over-claim |
| `tooling-ergonomics` | Cross-anchor orchestration hand-built (F1) | watch for recurrence — recipe, not helper |

## Optional triage evidence

For Loop 2 to weigh (do not graduate):

- **MRL-011 (competitive/substitute relation as Judgment):** Second sighting, now with *demand-side*
  evidence. Run 017 was store-only supply-side; run 030 reached outside and found the demand-side
  sources that would populate a `competitors:` field (Exa, "alternatives" listicles) are unreliable
  (Exa 1/16, comparison 4/16-but-SEO-biased). Strengthens "hold, do not build the field." Pointer:
  read.md Result/Gap Map; discovery O1/O3/G1.
- **MRL-008 (source-rigor/confound family):** Two new external-source flavors — (a) Exa
  `/findSimilar` similarity is name-distinctiveness-bound and ≠ cross-shop (a neighbor-graph confound);
  (b) owned-`/vs` SEO self-selection biases "alternatives to X" named sets; plus a recurrence of the
  run-024 category-extraction confound (drugs-not-platforms). Pointer: discovery O1/O3/O4/S1.
- **MRL-009 (write-back/capture worklist):** Tiered store-absent cross-shop nominees — Numan, Male
  Excel, Fountain TRT, Viking Alternative Medicine (Hone/TRT); Sesame (Ro). Propose-only; NOT
  autonomous (Firecrawl capture spend). Pointer: read.md C8; discovery O2.

## Next-run advice

- If pursuing demand-side cross-shop further, **test W2 first** (review-platform "people also viewed"
  / search co-occurrence) before concluding no clean external source exists — both families tried here
  were the weakest two.
- The **owned-`/vs`-as-directed-edge** idea (W1) is the most promising lighter primitive; a focused
  probe that scrapes brands' own `/vs` and `/compare` pages and reads them as directed edges would
  test it cheaply.
- Use `exa_similar.py` only for **distinctive-name** anchors, and always corroborate; do not use it as
  a cohort/competitor enumerator.
- For Loop 2: re-derive the 1/16 (Exa) and 4/16 (comparison) recall against the receipts; confirm the
  owned-`/vs` 4-of-5 count; check the store-absent nominee list against the store before it becomes an
  MRL-009 worklist.
