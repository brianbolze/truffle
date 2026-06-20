# Run Notes

```yaml
run_status: reviewed
evidence_mode: store-only
autonomous_eligible: yes
termination_reason: completed
pressure_lenses_fired: [coverage-caveat, depth-backfill, source-rigor, query-time-grouping-enough, freshness-monitoring]
```

> **Loop 2 (2026-06-20):** Reviewed via 3-pass adversarial workflow (evidence verifier +
> consumer + developer). Verifier = PASS_WITH_FIXES — caught 2 misclassifications
> (hevahealth, niagenplus) now corrected in `read.md` (decision-grade 7→9). Consumer =
> valuable; Developer = submit-candidate. Submitted **MRL-014** (new) + an **MRL-008**
> Evidence Log addend; F1 held at recur-watch. Raw learning appended to
> `discovery-ledger.md`. `Human Notes` untouched.

## 30-second operator read

- **Did it work?** Yes — clean store-only gap-probe on a never-before-read axis
  (geographic / US-state availability). The store cannot answer "can I get this in my
  state?" for any brand, and the reason is **grain mismatch**, not thin coverage.
- **What was awkward?** Availability lives only as prose at four different grains
  (per-SKU / per-line / per-brand / sub-component); there is no structured field to
  query. Took two grep passes (telehealth.md + profile.md) to assemble.
- **Next agent should know:** the decision-grade answer is **product × state**, not
  brand × state — a brand-level field would be false. "All 50 states" is a confound
  (often clinician-licensure or pharmacy reach, not the Rx program). No new primitive
  needed; at most a per-line depth-backfill, human-gated. New candidate item MRL-014.

## What happened

Store-only. Grounded the gap in Scout (8 cohort cuts, no geo field). Loop 1: (1) grepped
all 54 `telehealth.md` bodies for availability/licensing language; (2) grepped 54
`profile.md` files for state exclusions, lists, and "50 states" claims; (3) pulled exact
context for the 9 brands with real limits; (4) categorized into decision-grade exclusions
(7), un-enumerated limits (2), brand-level boilerplate (~8), sub-component "nationwide"
(~8), and silent (~29). Wrote `read.md` with claim IDs C1–C10. No external sources.

## Discovery ledger

Greedy raw learning for this run. Preserve singletons here before triage compresses
anything, then Loop 2 appends the useful rows to `discovery-ledger.md`. Do not merge
rows, dedup into backlog items, or translate wishes into build proposals inside the run.

Use short IDs such as `O1`, `W1`, `F1`, `S1`, or `G1` so reviews can cite them.

| ID | Kind | Raw observation / wish / friction / surprise / gap | Evidence or pointer | Why it matters | Discovery clock |
|---|---|---|---|---|---|
| O1 | observation | "Can I get this in my state?" is a **product × state** question, not brand × state — the same brand is 50-state for one line and 16/25-state-restricted for another (joiandblokes testosterone, vitalityrx Rx vs kit, henrymeds KYZATREX, marek diagnostics). | read.md C2–C5; `store/joiandblokes-com/telehealth.md:26`, `store/vitalityrx-com/profile.md:73` | A brand-level `available_states` field would be false-precise; kills the obvious "just add a field" reflex. | ready-for-triage |
| O2 | surprise | "All 50 states" is a **two-way confound**: (a) brand-claim State, not verified coverage; (b) for ~half the brands saying it, it scopes a sub-component (clinician licensure / pharmacy network / lab draw), not the buyable Rx program. | read.md C8, C9 | A naive tally of "50 states" mentions over-counts national availability and hides undisclosed per-line state limits. | ready-for-triage |
| O3 | observation | "Nationwide" attaches to the wrong noun in ~8 packs — pharmacy fulfillment (ro, directmeds), lab partners (hormonemd, maximustribe, hellopepti), in-clinic locations (niagenplus), clinician licensure (hevahealth, hydramed "13 states"). | read.md C9 | Reading sub-component reach as patient availability is a category error; the cohort body already keeps these distinct, which is the right behavior. | notice-only |
| O4 | surprise | The store **self-flagged the gap**: henrymeds `unverified_fields` says the site "does not enumerate a list" of supported states. Model behavior — record the claim, flag the gap, don't invent a list. | `store/henrymeds-com/profile.md:33` | Evidence the existing absence-discipline already handles this honestly; no schema defect. | notice-only |
| G1 | gap | Geographic/state availability is **not a captured surface** — not among the 8 telehealth cuts, no `available_states`/`service_area` field in SCHEMA/TAXONOMIES; only prose. | read.md C1; `modules/cohort-packs/TELEHEALTH.md` | The structural answer to the gap-probe: a frontier the store cannot currently see at query grain. | ready-for-triage |
| W1 | wish | If anything is captured, the right grain is a **per-offering-line verbatim availability note (dated)** — quote the state list/exclusion on the offering line — never a brand-level field or a stored service-area object. | read.md Market Pattern #3 | Names the only persistence shape that wouldn't rot or lie about multi-line brands. | recur-watch |
| S1 | observation | The **only** hard enumerated state exclusions in the whole store attach to **controlled-substance / compounded lines** (joiandblokes testosterone, henrymeds KYZATREX, trtnation TRT, vitalityrx compounded Rx). | read.md C2–C6 | Suggests availability limits are driven by molecule/Schedule + state pharmacy law, not brand choice — a testable hypothesis for a 2nd cohort. | recur-watch |
| F1 | friction | Assembling the availability picture needed two separate grep passes (telehealth.md body, then profile.md Overview/site_notes/unverified_fields) because availability prose has no canonical home. | this run's bash history | A documented QUERYING note ("availability prose lives in 3 spots, read both files") would save the re-derivation — same shape as MRL-002's price-lives-in-3-surfaces friction. | notice-only |

## Inputs and scope

- Denominator: 54 brands carrying `store/<domain>/telehealth.md` (the telehealth cohort).
- Files read: `telehealth.md` + `profile.md` for the cohort; `SCHEMA.md`,
  `modules/cohort-packs/TELEHEALTH.md` for the field contract.
- Method: grep availability/licensing language → pull exact context for hits → categorize.
- Exclusions: 81 non-cohort store domains (watches, SaaS, energy, etc.) out of scope.
- No external sources, no Firecrawl, no live browsing, no store mutation.

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

One real friction (F1): availability prose has no canonical home, so the read needed two
grep passes (`telehealth.md` body + `profile.md` Overview/`site_notes`/`unverified_fields`).
Mirrors MRL-002's "price lives in 3 surfaces" friction; a QUERYING note would help.

## Evidence limits

- All claims are **captured brand State (claims), not verified truth** — "all 50 states"
  is recorded, never adjudicated.
- The ~29 "silent" brands are **not-found**, not "available everywhere." Absence here
  means the captured pages didn't state geography; a brand could have an undisclosed
  state-gate at checkout the capture never reached.
- Corpus selection bias (MRL-001) bounds generalization: this is the hormone/Rx-commerce
  cohort, not "telehealth" — the controlled-substance-driven exclusion pattern (S1) may
  be a cohort artifact.
- No external verification of any state list (store-only by design); the read maps the
  gap, it does not fill it.

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
- No disallowed action happened: **pass** (no live browsing, no spend, no store mutation, no field creation)
- Required citations / receipts present and source-graded: **pass** (C1–C10, local paths + grade)
- No snippet treated as evidence: **pass** (no external sources at all)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (store clocks; claims labeled as claims, not truth)
- Absence language says "not found", not "not true": **pass** (~29 silent brands framed as not-found)

## Surprises

(S2) The store already handles this gap honestly — henrymeds' `unverified_fields`
explicitly records that the site won't enumerate its states (O4). And the load-bearing
surprise (O1/O2): availability is a *product × state* fact and "all 50 states" is mostly
boilerplate or sub-component reach — so the intuitive "add an `available_states` field"
fix would actively make the store wrong.

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
| `query-time-grouping-enough` | Availability is answerable (where disclosed) by reading existing prose; no durable category/field object is warranted — and a brand-level field would be wrong. | submit triage candidate (new item) |
| `depth-backfill` | The disclosed state lists/exclusions live only as prose; the *right* persistence grain would be a per-offering-line verbatim note, if anything. | watch for recurrence (W1/S1) |
| `coverage-caveat` | ~29/54 brands silent; the cohort is selection-biased (hormone/Rx-commerce), so the controlled-substance exclusion pattern may be a cohort artifact. | watch for recurrence |
| `source-rigor` | "All 50 states" is a two-way confound (unverified claim + sub-component scope) — a clean MRL-008 flavor on a new field. | submit Evidence Log to MRL-008 (Loop 2) |
| `freshness-monitoring` | Any captured state list is point-in-time (struthealth dated "as of Sept 2024"; controlled-substance availability tracks shifting state law). | watch for recurrence |

No new tag needed — existing tags cover it. The novel content is the **product×state grain**
finding and the **"50 states" confound**, both of which fit `query-time-grouping-enough`
+ `source-rigor`.

## Optional triage evidence

This run is more than a raw singleton — it opens a **new axis** (geographic availability)
not previously read, and lands a clean structural finding. Loop 2 should weigh:

- **New candidate MRL-014 — Geographic / state availability is a per-line, point-in-time
  property, not a brand field.** Evidence: O1/O2/G1/W1/S1 above; read.md C1–C10. Proposed
  next step (human-gated, do NOT implement): *hold for a second-cohort sighting of the
  product×state split before any depth-backfill recipe; explicitly do not add an
  `available_states` brand field or a service-area object.* Priority suggestion P3.
- **MRL-008 Evidence Log addend** — the "all 50 states" two-way confound (claim-not-truth
  + sub-component-scope) is a new field-flavor of the confound family (O2/O3). Additive;
  does not move the graduation clock.
- **MRL-002 friction note (optional)** — F1 (availability prose lives in ≥2 files) mirrors
  the price-lives-in-3-surfaces friction; recur-watch only.

Loop 2 decides whether these are mature enough to submit; raw detail stays in the
Discovery ledger / `discovery-ledger.md`.

## Next-run advice

- A second cohort or anchor where availability splits product×state (controlled-substance
  lines limited, everything else national) would harden S1 from a one-cohort Judgment
  into a documented rule. Good candidates: a future read on a cohort with heavy
  controlled-substance lines.
- Do **not** re-run this as a bounded-live "verify the state lists" sweep without human
  approval — that's a 54-brand per-brand live effort, far beyond a light ceiling.
- If geographic availability ever graduates, the grain is **per-offering-line verbatim +
  dated**, never a brand scalar.
