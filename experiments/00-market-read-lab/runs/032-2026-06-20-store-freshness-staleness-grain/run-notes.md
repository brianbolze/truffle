# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [freshness-monitoring, query-time-grouping-enough, source-rigor, coverage-caveat]
```

## 30-second operator read

- **Did it work?** Yes — first dedicated **State-axis** freshness/staleness calibration
  (freshness has fired 6× as a tag but only ever on the Signals axis, 018/MRL-012). Store-only,
  no spend. Verdict: a reader **can** risk-rank staleness, but only by crossing **two** already-
  greppable surfaces — `captured_at` age × the literal `point-in-time snapshot, not fixed` token —
  and **neither alone works**. **No new primitive:** `query-time-grouping-enough` fires TRUE for
  risk-ranking, FALSE only for actual *drift*, which no store-only surface can answer by design.
- **What was awkward?** I reproduced the contracted failure mode twice and caught both: (1) a loose
  keyword grep over-flagged the high-risk set to 57 incl. stable watch/SaaS brands (real set = 34
  via the literal token); (2) my first `captured_at` parser silently dropped 4 **quoted**-date
  profiles as "undated" (format hazard G3). Both folded into the read as V1.
- **Next agent (Loop 2) should know:** the load-bearing counts are C1 130/130 dated (median 16d),
  C2 57 token (47 literal), C3 34 high-risk, C5 0/49 signals-fresher. Pressure-test C3 and C5 and
  the "token = volatility not staleness" framing — that distinction is the whole result.

## What happened

Parsed `captured_at` across all 130 profiles (age 0–21d, median 16d; 79 ≥15d). Censused the literal
`point-in-time snapshot, not fixed` token (47 literal + 10 loose ≈ 57; SCHEMA.md:112) and cross-
tabbed by vertical (health 36/69 vs non-health 11/61). Crossed age≥14d × literal token → 34 high-
risk profiles. Checked signals recency: 49 `signals/` dirs, **0** with a clock newer than the
profile capture → signals don't refresh State. Read SCHEMA-112 to fix what the point-in-time token
is *meant* to mark (capture-volatility, not staleness). Concluded staleness-RISK is a query-time
cross of two existing surfaces; actual drift is unobservable store-only (→ MRL-012). One receipt (S1–S3).

## Discovery ledger

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | The store carries **two** freshness surfaces answering different questions: `captured_at` ("how old", 130/130, median 16d) and the `point-in-time snapshot, not fixed` token ("how volatile at capture", 57). Staleness-**risk** is their **cross** (34 old+volatile); neither alone works. | read.md Result/Gap Map; receipt C1–C3 | First explicit model of the engine's State-freshness layer; tells a "trust the cache" reader exactly what's knowable. | ready-for-triage |
| O2 | observation | **Signals never refresh the State clock:** 49 profiles have `signals/`, **0** carry a signal clock newer than `captured_at` — co-captured, not re-run. So "signals recency" is NOT a State-freshness re-read today. | read.md G1; receipt C5 | Kills the intuitive "signals tell me what changed" assumption for State; drift needs re-capture (MRL-012), not the existing signals layer. | ready-for-triage |
| O3 | observation | The point-in-time token marks capture-**volatility** (A/B/promo/rotation, SCHEMA-112), not staleness-since-capture, and is **vertical-shaped**: health/telehealth 36/69 vs non-health 11/61 (telehealth promo/intake pricing). | read.md C2; SCHEMA.md:112 | Volatility-of-content, not age, is the real staleness axis — and it's a telehealth phenomenon; ranking by age alone inverts the truth for stable brands. | ready-for-triage |
| S1 | surprise | **Query-time cross is enough — no new marker.** Both staleness-risk inputs (`captured_at`, point-in-time token) already exist and are greppable; the persistence boundary holds at query-time. The only real gaps are drift-detection (MRL-012) and a format lint (G3). | read.md What Would Change | A clean `query-time-grouping-enough` TRUE for risk-ranking on the freshness axis; sibling to 031's "no per-fact confidence field" verdict on the trust-metadata layer. | ready-for-triage |
| G1 | gap | **Actual drift is unobservable store-only:** no surface says a fact *changed* since capture, only "how old × how volatile." Closing it = the parked re-capture+diff cadence (MRL-012), spend-gated. | read.md G1; run-018/MRL-012 | Bounds the value-job honestly: "trust the cache over time" is answerable as *risk*, not as *change*, without spend. | ready-for-triage |
| G3 | gap/friction | **`captured_at` format inconsistency**: 4 profiles quote the date (anazaohealth, goinfusive, jinfiniti, millspharmacy), 126 bare. A naive `captured_at:\s*\d` grep silently drops the 4. | receipt Evidence/G3; my Loop-1 parser | A concrete MRL-008 "parse-hazard / bare field isn't self-describing" sighting on the freshness field; one-line normalization or `querycheck` lint fixes it. | ready-for-triage |
| W1 | wish | If anything graduates it is **not a freshness marker** — it's (a) the MRL-012 re-capture cadence (drift) and (b) a `captured_at` format-normalization lint (G3). Prefer a documented **query recipe** ("staleness-risk = age × point-in-time token") over any new field. | read.md What Would Change | Names the anti-sprawl path consistent with "spend on conventions, not infra"; zero migration blast-radius. | recur-watch |
| F1 | friction | Crossing age × volatility needed a hand-rolled Python pass (parse `captured_at` robustly, grep the literal token, signals-clock walk); no MRL-002 recipe covers a "freshness-risk" cross-company read. | run-notes friction log | Mirrors the recurring MRL-002 query-machinery friction, now on the freshness grain; recur-watch. | recur-watch |
| V1 | value-miss | I reproduced the contracted failure mode **twice** and caught both: a loose keyword grep over-flagged high-risk to 57 (incl. stable Casio/Cartier/Nike/AWS/Datadog) vs the disciplined 34 via the literal token; and a non-quote-aware parser mislabeled 4 quoted-date profiles "undated." Both corrected before exit. | read.md C4; receipt G3 | The exact `loop1_failure_mode` Scout named (age≠staleness over-claim; point-in-time-as-staleness). Demonstrates age≠staleness concretely; a self-audit catch, not a clean run. | ready-for-triage |

## Inputs and scope

- **Slice:** all 130 `store/*/profile.md` (cross-vertical) + 49 `store/*/signals/` dirs.
- **Fields:** `captured_at`, `primary_industry`, `site_notes`/`unverified_fields` point-in-time token.
- **Contract:** SCHEMA.md:112 (point-in-time / A/B), :23 (volatile-fact discipline).
- **Exclusions:** 9 capture-only stubs (no profile.md, run-027 list) — outside the freshness denominator.
- **No external sources.** Scripts: `/tmp/freshness.py`, `/tmp/fresh4.py` (method recorded in receipt).

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
# Default light ceilings: 2 source families, 6 outside sources read/captured,
# 20 paid capture credits. Lower if Scout set a tighter plan.
# Fail closed before exceeding the ceiling, adding an unplanned source family,
# broadening into search/crawl, or using login/paywalled/private sources.
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

## Friction log

- Crossing freshness surfaces required a bespoke Python pass each time (robust `captured_at` parse +
  literal-token grep + signals-clock walk); no MRL-002 recipe covers a cross-company freshness-risk
  read (F1). One sighting on this grain.
- The `captured_at` quoted/bare inconsistency forced a parser re-write mid-run (G3/V1).

## Evidence limits

- The 57/34 sets depend on the point-in-time token being *applied at capture*; an unflagged volatile
  profile would be under-counted. Token **coverage** (how often the flag is correctly applied) was not
  measured here — a capture-discipline question distinct from this read.
- The volatility token is a *correlate* of staleness risk, not a drift measure; nothing here proves a
  specific fact changed since capture (G1, by design store-only).
- The health/non-health vertical cut is a coarse keyword bucket on `primary_industry` (derived).

## Loop 1 exit check

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a**
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation)
- Required citations / receipts present and source-graded: **pass** (receipt S1–S3, grade derived/primary)
- No snippet treated as evidence: **pass** (store-only, no snippets)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no live current claims; freshness *of* the store is the subject, dated per-profile)
- Absence language says "not found", not "not true": **pass** (G1 framed as "unobservable store-only", not "no drift exists")

## Surprises

- **Signals never refresh State (0/49)** — the intuitive "signals tell me what changed" assumption
  is false today; signals are co-captured with the profile, not re-run (O2/S1).
- **Query-time cross is enough** — the staleness-risk answer fell out of two *existing* greppable
  surfaces with no new field; the persistence boundary held (S1).
- I reproduced the exact failure mode Scout named, twice, and the discipline (literal token + quote-
  aware parse) caught both (V1) — a useful demonstration that age ≠ staleness.

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
| `freshness-monitoring` | First dedicated State-axis freshness calibration; staleness-risk is rankable but actual drift is unobservable store-only (needs MRL-012 re-capture cadence). | submit Evidence Log to **MRL-012** (generalizes change-pulse from Signals to State; names the two-surface model + signals-don't-refresh finding) |
| `query-time-grouping-enough` | Staleness-risk = query-time cross of `captured_at` × point-in-time token; no durable freshness marker earns its keep. | no-op (a clean TRUE; reinforces the no-new-primitive posture, sibling to 029/031) |
| `source-rigor` | `captured_at` quoted/bare format inconsistency silently drops 4 profiles from a naive freshness grep (G3); reproduced by my own parser. | watch for recurrence; candidate Evidence Log to **MRL-008** (parse-hazard / bare-field family) on 2nd sighting |
| `coverage-caveat` | Point-in-time token coverage (is the volatility flag actually applied at capture?) is unmeasured; under-flagged volatile profiles would be missed. | no-op; capture-discipline note, not a build |

## Optional triage evidence

Normally none. Add only concrete backlog evidence, with priority/status suggestions,
when the run has more than a raw singleton or when review adds evidence to an existing
item. Keep this to 1-3 backlog-ready bullets plus pointers to the Discovery ledger,
`discovery-ledger.md`, or run artifacts.

**Do not implement, spike, or recommend immediate graduation from inside the run.**
Raw learning belongs in the run Discovery ledger and `discovery-ledger.md`. Submit
triage only when the run adds enough evidence for a stewarded backlog item or Evidence
Log entry.

## Next-run advice

- **Re-check (Loop 2):** verify C3 (34 = age≥14d × literal token), C5 (0/49 signals-fresher), and the
  47-vs-57 literal-vs-loose token split. Pressure-test the "token = volatility, not staleness" framing —
  that distinction carries the whole result.
- **Try later:** a **token-coverage** read (how often is the point-in-time flag correctly applied vs
  missed on visibly volatile pricing?) — this run measured the flag's *meaning*, not its *recall*.
- **Avoid:** ranking staleness by `captured_at` age alone (inverts the truth for stable MSRP/rate-card
  brands), and reading the point-in-time token as "this is stale."
- **Note:** the runner-up Scout candidate C (offerings roster completeness) remains untested; revisit if
  a completeness-grain calibration is wanted next.
