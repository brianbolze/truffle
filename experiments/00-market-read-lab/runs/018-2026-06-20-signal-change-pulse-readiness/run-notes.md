# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [freshness-monitoring, tooling-ergonomics, source-rigor, denominator-reconciliation, coverage-caveat]
```

## 30-second operator read

- **Did the run work?** Yes. First temporal/diff read in the lab; `signal_delta.py` ran clean over every ≥2-capture dir and gave an honest readiness verdict.
- **What was awkward?** Nothing in execution — the tool's veto-not-skip behavior made the "what can't we diff" answer fall out for free. The substantive friction is in the *store*, not the run: SEC had no delta branch at run time (shipped 2026-06-22), SERP captures are one-per-query, and only Trustpilot has a real time-gapped second capture.
- **What should the next agent know?** "Trust the cache over time" is operable today on two surfaces — Trustpilot review-velocity (~6 brands) and Wayback archive-presence (~10 domains) — but **both readable deltas are noisy proxies** (solicitation cadence; archiver re-crawl cadence) for the change a consumer wants. The verdict is **no new primitive needed — freshness is a capture-cadence-matched-to-refresh-rate + small tooling gap, not a schema gap.** Note the Loop 2 correction below: the page-grain Wayback signal was missed on the first pass.

## What happened

Enumerated every `store/<domain>/signals/<source_type>/` dir with ≥2 capture JSONs (~13 domains), ran `signal_delta.py` first-vs-last on each, and classified each result as clean-delta / level-only / veto. Wrote the readiness verdict from the pattern. Pure local; no fetch, no spend.

## Inputs and scope

- **Store slice:** all `signals/` dirs with ≥2 captures — trustpilot ×9 + sec_edgar ×4 + serpapi ×2 (company-grain) + **wayback ×15 page-subjects across 10 domains (page-grain)** = **13 distinct domains**.
- **Tool:** `tools/signal_delta.py` (read-only consumer), semantics from `signal_delta.md` / `--help`.
- **Exclusions:** 86/135 domains have no `signals/`; single-capture signal dirs (no second snapshot to diff) excluded by construction.
- **Loop 2 correction:** the first pass's company-grain glob missed Wayback (captured a level deeper at page grain); the adversarial evidence verifier caught it and the Wayback sweep is folded into `read.md`/receipt.
- **Receipts:** `receipts/signal-delta-sweep-2026-06-20.md` (C1–C9).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

- **Grain-dependent enumeration is a real footgun (Loop 2 catch).** A `store/*/signals/*/` company-grain glob silently misses Wayback, whose envelopes live a level deeper at page grain (`signals/wayback/<page-slug>/`). The zsh "no matches" noise on `signals/wayback/*.json` was the tell, and the first pass dismissed it. "What's diffable" is grain-dependent; any future `signal_delta` enumeration helper must walk to the envelope, not assume `<domain>/signals/<type>/*.json`. This is concrete `tooling-ergonomics` evidence.
- The other system friction surfaced by the tool: `signal_delta.py` had no `sec_edgar` branch, so SEC pairs returned a veto string instead of a diff. Correct fail-closed behavior; the branch shipped 2026-06-22, leaving cadence and subject pinning as the live SEC change-pulse constraints.

## Evidence limits

- **Thin, lopsided temporal substrate:** ~13 domains with a second capture, 6 with a usable delta, one source type (Trustpilot), one ~1-week window. Not a market census.
- **The clean signal is the confounded one:** every readable velocity is `review_count` on a `paid_profile` profile — solicitation cadence, not organic sentiment. The decision-grade surfaces (trust_score trend, review bodies) are not delta-tracked.
- **Two snapshots ≠ monitoring:** "no detected change" means *not found between these two captures*, not *no change occurred*. SEC/SERP "no change" is really "mis-spaced/unpaired captures," not stability.
- **Risky inference avoided:** drew no market/momentum conclusion from the velocity spread; the payload is the readiness verdict.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no fetch, no spend, no store mutation, no primitive)
- Required citations / receipts present and source-graded: **pass** (`receipts/signal-delta-sweep-2026-06-20.md`, derived/local-store)
- No snippet treated as evidence: **pass** (all evidence is local diff output)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (capture timestamps + gap_days on every delta)
- Absence language says "not found", not "not true": **pass** (SEC/SERP framed as "unsupported/unpaired," not "no change")

## Surprises

- **The delta-able metric is the least useful one.** I expected Trustpilot to be the strong source — it is, but only for cumulative `review_count`, which is `paid_profile`-confounded; `trust_score` and `reviews_last_12m` don't diff. The temporal axis inherits MRL-008's "headline metric misleads without its confound sibling" almost verbatim.
- **SEC and SERP have second captures but they're useless for change-pulse for *structural* reasons, not coverage** — SEC pairs are intra-day, SERP "pairs" are different queries. The bottleneck is capture *cadence/identity*, not capture *count*.
- The tool's veto-not-skip discipline made "what can't we answer" the cheapest part of the read.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

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

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `freshness-monitoring` | First temporal/diff read; the whole run is about whether change-pulse is operable. Verdict: yes for ~6 Trustpilot brands/one metric, no for SEC/SERP — bounded by capture cadence, not schema. | submit triage candidate (new item: change-pulse readiness = cadence + tooling gap, not a primitive) |
| `tooling-ergonomics` | `signal_delta.py` had no `sec_edgar` delta branch at run time; SEC pairs vetoed instead of diffing. Narrow, concrete tool gap; shipped 2026-06-22. | resolved for the code branch; cadence/subject pinning remain in MRL-012 |
| `source-rigor` | The only delta-able Trustpilot metric (`review_count`) is `paid_profile`-confounded; decision-grade surfaces (score trend, bodies) don't diff. Temporal flavor of MRL-008. | append Evidence Log to MRL-008 |
| `denominator-reconciliation` | The "denominator" here is a *capture-cadence* set (subjects captured ≥2× same-source/same-subject with a real gap), not a market-membership set — a new flavor of MRL-001's denominator pressure. | append Evidence Log to MRL-001 (temporal-denominator flavor) |
| `coverage-caveat` | 86/135 domains have no `signals/`; only 6 yield a usable delta. | reinforces, no-op |

## Triage submissions

Proposed (human-gated; not implemented here):

- **New item (suggest P2, `Submitted`, area: freshness/signals-cadence):** *Change-pulse readiness is a capture-cadence-matched-to-refresh-rate + tooling gap, not a new primitive.* Evidence: this run. The append-only `signals/` layer + `signal_delta.py` are the right shape and need no schema change; what blocks a real "trust the cache over time" read is (a) capture cadence not matched to each signal's own refresh rate — SEC pairs are intra-day, SERP "pairs" are different queries, Trustpilot counts move daily (gapped repeats work), and Wayback re-captures are days apart while the archive re-crawls ~monthly so 13/15 read delta=0; and (b) one narrow tool gap — `signal_delta.py` had no `sec_edgar` delta branch at run time. Proposed next step (human-gated): decide whether a light re-capture cadence (tuned per source) for a small subject set is worth standing up. The `sec_edgar` branch shipped 2026-06-22. Explicitly do **not** build a monitor service, a stored diff/change object, or a non-company signal entity from one run.
- **Evidence Log → MRL-008:** *two* temporal confound flavors. (1) The delta-able Trustpilot metric (`review_count` velocity) is `paid_profile`-confounded and the decision-grade surfaces (trust_score trend, review bodies per MRL-010) are not delta-tracked. (2) Wayback's onemedical `snapshot_count` moved −1 with `last_seen` going *backwards* — a CDX API-nondeterminism confound that a naive read would report as a lost archived snapshot. The confound convention must travel onto the *change* axis, not just the level read, and now spans two source families (review-score and archive-state).
- **Evidence Log → MRL-001:** new *temporal-denominator* flavor — for change-pulse reads the denominator is "subjects with ≥2 comparable same-subject captures and a real gap," distinct from market-membership denominators; here ~6 of ~13 ≥2-capture domains, dominated by one source type.

(Loop 2 should decide whether these add new evidence before writing them; do not auto-graduate.)

## Next-run advice

- If freshness/change-pulse recurs, the highest-value variant is **after** a deliberate re-capture cadence exists — re-running this exact sweep then would show whether the substrate widened. Until then, a repeat is calibration only.
- A cheap adjacent run: a **staleness/decay audit** (oldest `captured_at` per load-bearing field) — the decay side of freshness, complementary to this delta side, and answerable store-only.
- Avoid drawing market/momentum conclusions from review-velocity on `paid_profile` profiles.
