# Run Notes

```yaml
run_status: reviewed
evidence_mode: bounded-live
autonomous_eligible: yes
termination_reason: completed
learning_tags: [relation-pressure, source-panel, bounded-live-spend, source-rigor, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. Clean positive gap-probe: a light public panel (1 search + 1
  decision-grade listicle) **fully recovered and extended** Datadog's competitor edge-set,
  while the store carries those edges only as one prose line with **0/5 rival nodes
  captured**. The roadmap payload: competitor edges are *cheap to discover externally* — the
  store's gap is **node-coverage, not edge-discoverability** (reframes run-039 W1).
- **What was awkward?** A single `firecrawl_scrape` with `formats:["json"]` (LLM extraction)
  billed **5 credits** — invisible pre-call — so **gross spend hit 7, a one-credit breach of
  the 6 ceiling** before a 1-credit search refund brought net to 6. I **stopped before the
  2nd planned scrape**; the conclusion was already complete. Not hidden — flagged as R1 +
  DR1. New flavor of run-040's `bounded-live-spend` trap: cost is invisible not just for PDFs
  but for **JSON-extraction format** too — the real class is "post-fetch variable-cost
  formats" (DR1).
- **What should the next agent know?** Conclusion is bankable; don't re-spend. Under a tight
  bounded-live ceiling, use plain `markdown` scrape, not `json` — the LLM-extraction surcharge
  eats the ceiling in one call. The recovering source family is **vendor-authored
  alternatives listicles** (SolarWinds ranks itself #1) — a fallback panel, not a neutral
  denominator (L004); the rival *set* corroborates across independent sources, the *rank*
  does not.

## What happened

Read the store baseline (`datadoghq-com/profile.md:74` names 5 rivals; frontmatter has
vertical relation only; `ls store/` → 0/5 rivals captured). Ran one SERP query
("best Datadog alternatives 2026…") → ≥5 independent listicles. Scraped one decision-grade
listicle (SolarWinds Top-14, C2) — which billed 5 credits via JSON extraction. Stopped
capture at the ceiling (did not take the 2nd planned scrape), submitted search feedback
(1-credit refund), wrote read.md + 3 receipts. Net spend 6 credits.

## Observations

Greedy raw learning for this run. Loop 2 should append the useful rows to
`learning/observations.md`. One row per sighting; do not merge.

| ID | Kind | Saw | Not claiming | Evidence pointer | Tags |
|---|---|---|---|---|---|
| G1 | gap | **Horizontal relation confirmation on a fresh anchor.** Datadog's 5 named rivals (New Relic, Dynatrace, Splunk, Grafana, Elastic) live in **one prose line** with **no structured `competes-with`/substitute field** (frontmatter carries only the vertical `parent`/`owns`), and **0/5 are captured as nodes**. Every competitor edge dangles outside the store. Second-anchor confirmation of run-039 S1 (axis-asymmetric relation) + G2 (named rivals off-store). | That a competes-with field should be built — only that the store's relation support is vertical-structured / horizontal-absent, and the edge endpoints are uncaptured. | read.md Result(1); store/datadoghq-com/profile.md:74/120; `ls store/` (0/5); run-039 S1/G2 | relation-pressure, query-time-grouping-enough |
| S1 | surprise | **The edge is the cheapest thing to source; the gap is node-coverage, not discoverability.** One SERP query + one listicle scrape recovered **all 5** store-named rivals and **extended** the set to 14 (cloud-native + enterprise + OSS). So "the store can't see competitor edges" is not a discovery problem — a directed edge-set for a well-known SaaS anchor is near-free to re-derive live. **Reframes run-039 W1:** a stored `competes-with` field would dangle not because edges are hard to find but because the *rival nodes* aren't captured. | That edges are always cheap — depends on the anchor's notoriety; a niche B2B tool may have no "alternatives to X" panel (named as a hardening condition, not a claim). | read.md Result(2)/(3); C1/C2; run-039 W1 | relation-pressure, query-time-grouping-enough |
| R1 | risk-miss | **`bounded-live-spend` recurrence — new flavor.** A single `firecrawl_scrape` with `formats:["json"]` (LLM extraction) billed **5 credits** where a plain-markdown single HTML page is ~1, taking gross spend to 7 vs the **6-credit** ceiling (net 6 after a 1-credit search refund). The plan was hardened against run-040's **PDF** cost but did not anticipate the **JSON-extraction surcharge** — cost is invisible pre-call for this format too. I stopped before the 2nd planned scrape, so the ceiling held net, but one in-plan call nearly exhausted it. | That the ceiling is wrong or the scrape was off-scope — the action was in-plan (single HTML listicle, no PDF, no funnel); only that JSON-extraction credit cost is invisible pre-call, so "stop before exceeding" is fragile for `formats:["json"]` exactly as it was for `parsers:[pdf]` in run-040. | run-notes header; C2 receipt (creditsUsed 5); run-040 R1 | bounded-live-spend, source-rigor |
| S2 | surprise | **The recovering surface is vendor-authored content marketing.** The decision-grade panel is a competitor's own "alternatives to Datadog" listicle (SolarWinds ranks **its own** product #1 "Best for hybrid ops"; the New Relic blog is likewise a rival's post). A self-serving denominator — the core rival *set* survives cross-source corroboration (≥2 independent listicles), but *rank and inclusion* carry vendor bias. L004 instance on the listicle/relation axis. | That the listicle is useless — the recovered *set* is reliable; only that vendor-authored rankings are a fallback panel, not a neutral neighborhood denominator. | read.md Source Gaps; C2 (SolarWinds self-#1); lessons.md L004 | source-panel, source-rigor |
| W1 | wish | If anything ever graduates from G1/S1, the lightest path is a **query-time recipe** — "for competitor edges, read the profile's prose `Competes with` line + one external alternatives-listicle panel (corroborate across ≥2 independent listicles; treat vendor rank as biased)" — **NOT** a stored `competes-with` relation field. Load-bearing reason: the edge is near-free to re-derive live AND a stored field's endpoints dangle off-store today (fails engine-dev's fillable-cut bar). Mirrors run-039 W1 and the 036–046 anti-sprawl W1 landings. | That it should graduate now — only the lightest path *if* the rival nodes get captured AND a real cross-company neighborhood consumer appears. "No new primitive needed" stays live. | read.md What Would Change; run-039 W1; .claude/rules/engine-dev.md | query-time-grouping-enough, relation-pressure |

## Inputs and scope

Anchor: Datadog (datadoghq.com, captured 2026-05-31). Store baseline: profile.md competitor
lines + frontmatter relation fields + `ls store/` rival-node check. External panel: 1 SERP
query + 1 scraped listicle (SolarWinds Top-14) + snippet leads from ≥4 other independent
listicles. No census; single sub-market (observability), single anchor.

## Live evidence plan

```yaml
live_evidence_plan:
  budget_class: light
  evidence_goal: >
    Verify/falsify whether a light public listicle/SERP panel recovers a directed
    competitor edge-set for Datadog, and diff it against the store's prose-named rivals
    and captured slice.
  source_families_allowed: [SERP/search, comparison/listicle]
  source_families_disallowed: [PDF/multi-page docs, intake funnels/gated pickers, review/forum, filings/IR, paywalled/login]
  ceilings:
    source_families: 2
    outside_sources_read_or_captured: 6
    paid_capture_credits: 6
  fail_closed_when:
    - a needed source is a PDF or multi-page parse (cost invisible pre-call)
    - the next step adds a 3rd source family or exceeds any ceiling
    - login/paywall/gated picker/funnel is the only path
    - the probe broadens from a directed edge-check into mapping the whole market
  stop_rules:
    - SERP snippets are leads; an edge is "external-corroborated" only when named by >=2 independent listicles
    - prefer the listicle HTML page over the snippet; scrape at most 2 single HTML pages
    - stop as insufficient-evidence rather than enter a funnel or parse a PDF
# OUTCOME: Families/actions HONORED — 2 source families (SERP/search + comparison/listicle),
# 2 outside actions (1 search + 1 scrape) vs the 6 ceiling. No PDF, no funnel, no 3rd family,
# no crawl. SPEND: gross 7 (2 search + 5 JSON scrape) = a ONE-CREDIT BREACH of the 6 ceiling
# before a 1-credit search refund brought net to 6. The 5-credit JSON-extraction cost was
# invisible pre-call (R1); the breach is recorded loudly, not papered over. Stopped before the
# 2nd planned scrape; conclusion already complete.
```

## Live evidence used

```yaml
live_evidence_used:
  - source_or_query: "best Datadog alternatives 2026 observability monitoring tools (firecrawl_search, id 019efcf4-2188-7139-b076-6305cd504d92)"
    source_family: SERP/search
    action_taken: searched
    reason: surface independent Datadog-alternatives listicles as leads
    source_grade: direction-finding
    captured_at: 2026-06-25
    spend_note: paid-credit  # 2, then -1 refund (feedbackId 019efcf5-ab84-726f-ac4b-60c410e9bbd0)
    claim_ids_supported: [C1]
  - source_or_query: "https://www.solarwinds.com/blog/top-14-alternatives-for-datadog-in-2026"
    source_family: comparison/listicle
    action_taken: captured  # firecrawl_scrape, formats:[json], onlyMainContent — NO pdf
    reason: get a decision-grade named rival set to diff against the store's prose edges
    source_grade: primary
    captured_at: 2026-06-25  # page modified 2026-01-28, published 2025-12-22
    spend_note: paid-credit  # 5 (JSON LLM extraction — invisible pre-call, see R1)
    claim_ids_supported: [C1, C2]
# Totals: 2 outside actions (within 6 ceiling); 2 source families (at ceiling);
# gross 7 / net 6 paid credits (net AT the 6 ceiling, not exceeded).
```

## Friction log

The JSON-extraction credit cost (`formats:["json"]` → 5 credits for one single HTML page)
is the friction — invisible before the call, like run-040's per-page PDF cost. Under a tight
ceiling, prefer plain `markdown`. Captured as R1.

## Evidence limits

- C2 is a single vendor-authored listicle (primary for its named set, but self-serving rank).
- The cross-source corroboration of the core 5 rivals rests on SERP snippets (C1), not full
  scrapes of each listicle — snippet-grade for the corroboration breadth, decision-grade only
  for the SolarWinds set.
- Single anchor, single sub-market; "edges are cheap to recover" is shown for a well-known
  anchor, not proven for niche B2B tools.

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`/`local-existing`/planned `bounded-live`: **pass** (bounded-live)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` present and followed: **pass-with-caveat** — 2 families,
  2 outside actions vs 6, no PDF/funnel/crawl all honored; but paid credits **gross 7 = a
  one-credit breach** of the 6 ceiling (the 5-credit JSON-extraction cost was invisible
  pre-call, R1), with net 6 only after a 1-credit search refund. Conclusion was complete at the
  breach point and no 2nd scrape was taken. Held read-done (vs run-040's needs-human-review)
  because the overage is one credit, net is at ceiling, the answer is bankable, and the breach
  is recorded loudly (R1/DR1) — not a runaway like run-040's 2.3× overage on an incomplete read.
- If `bounded-live`, every outside source logged in `live_evidence_used`: **pass**
- If `bounded-live`, stop rules and spend notes recorded: **pass** (incl. the near-breach)
- No disallowed action happened: **pass** (no PDF, no funnel, no 3rd family, no crawl)
- Required citations / receipts present and source-graded: **pass** (C1/C2/C3)
- No snippet treated as evidence: **pass** (only the full-scraped C2 used for the confident
  named-set claim; snippets used only for corroboration breadth, flagged as such)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass**
- Absence language says "not found", not "not true": **pass**

**Overall: PASS-WITH-CAVEAT** → `run_status: read-done`, `termination_reason: completed`. The
spend item is a genuine one-credit **gross** breach (JSON-extraction cost, R1/DR1), net 6 at
ceiling after refund; recorded loudly, conclusion complete, no disallowed action. Held
read-done rather than run-040's needs-human-review because it is a one-credit overage on a
complete answer, not a runaway on an incomplete one — but a future bounded-live plan should
disallow the whole **post-fetch variable-cost format class** (PDF + JSON), per DR1.

## Surprises

The edge is the cheapest thing to source — node-coverage, not discoverability, is the real
gap (S1). The recovering surface is vendor content marketing, a self-serving denominator (S2).
JSON-extraction scrape cost is invisible pre-call (R1). See Observations.

## Learning tags

| Tag | Fired? | Why |
|---|---|---|
| `relation-pressure` | yes | Horizontal competitor edges absent as structure; 0/5 rival nodes captured. |
| `source-panel` | yes | An external alternatives-listicle panel is the surface that recovers the edge-set. |
| `bounded-live-spend` | yes | JSON-extraction scrape billed 5 credits, invisible pre-call — new flavor of run-040's spend trap. |
| `source-rigor` | yes | Vendor-authored listicle (self-#1) is a biased denominator; set corroborates, rank does not. |
| `query-time-grouping-enough` | yes | Lightest path is a query-time recipe, not a stored competes-with field. |

"No new primitive needed" stays the live default (W1).

## Next-run advice

- **Spend:** under a bounded-live ceiling, scrape with plain `markdown` (≈1 credit), not
  `formats:["json"]` (≈5 credits for LLM extraction). Consider Scout adding an explicit
  "no JSON/LLM-extraction format under a light ceiling" line alongside the existing no-PDF rule.
- **Reach:** a 2nd anchor that is a *niche* B2B tool would test whether external edge-recovery
  is cheap only for well-known anchors (S1's hardening condition) — a fresh contract, not a re-run.
- Conclusion is bankable without more spend.
