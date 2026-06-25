# Run Notes

```yaml
run_status: reviewed
evidence_mode: local-existing
autonomous_eligible: yes
termination_reason: completed
learning_tags: [source-rigor, tooling-ergonomics, query-time-grouping-enough, schema-edge-entity-type]
```

## 30-second operator read

- Did the run work? Yes — local-existing, zero spend, clean. Rendered 6 flag-heavy briefs
  with `render.py … --no-fetch` and audited the renderer source + output.
- What was awkward? Nothing operationally. The interesting twist is that the naive hypothesis
  ("render launders the flags") was **falsified** — the brief carries every flag — and the
  real finding moved to salience/ordering, which took reading `brief.py` in full to nail.
- What should the next agent know? This audited only the single-company HTML brief
  (`scripts/present/brief.py`). The comparison sheet, the index, and direct `profile.md`
  consumption were **not** audited — don't generalize "preserve-but-bury" past the brief.

## What happened

Scout selected a gap-probe testing the recurring relay-risk thread (flag protection is
"prose-grade, relay-dependent") against the actual relay Truffle ships: `scripts/render.py`.
Loop 1 rendered 6 profiles chosen to span the flag types from runs 038/042/046/048, diffed
the generated HTML against source `profile.md`, and read `model.py`/`brief.py`. Result:
content fidelity is good (no flag dropped), but the flags render at the lowest salience
(tab 4 / collapsed `<details>`) while the over-claim-prone `description` renders at the
highest (hero), so the 5-second handoff path is flag-free. See `read.md`.

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
| S1 | surprise | **The laundering hypothesis is falsified at the artifact level.** `render.py` preserves every source-rigor flag: all 6 briefs render their full `unverified_fields` list ("What we couldn't verify": 3/3, 3/3, 2/2, 2/2, 4/4, 4/4 vs source), plus `site_notes` ("Field notes — read before trusting a number"), the self-reported proof prose, and the price-vis token as roster chips (therabody 57 `published`, remedymeds 3 `published`+3 `on-request`). The one relay Truffle ships does **not** drop flag content — a positive for the engine against the 038/042/048 R-row worry. | That the brief is safe — content fidelity ≠ salience fidelity (see G1); only that no flag is dropped from the file. | read.md Result(1)/C1-C4; receipts/C1; brief.py:93-96,190-222 | source-rigor, query-time-grouping-enough |
| G1 | gap | **The recurring "relay-dependent" risk is a *salience* property of the structured flags, not a content one.** The structured trust surfaces (`unverified_fields`/`site_notes` → tab 4; price-vis chips → tab 2) are uniformly off the default path (hero + tab-1 auto-open Overview/Strategic read); the "self-reported" proof bullets render collapsed. The structured layer is preserve-but-bury. [Scoped per VR1: the default path is NOT flag-free — captor prose in the auto-open sections often carries the caveat; see VR1.] | That tab-4 placement is wrong — may be working-as-designed (flags = "limits," filed under Provenance); only that the *structured* flag surfaces are off the default path. n=1 relay (the HTML brief). | read.md Result(2)/Gap Map; brief.py:259-263,326-348; C2/C3 | source-rigor, query-time-grouping-enough, tooling-ergonomics |
| S2 | surprise | **The hero renders the most over-claim-prone field at peak salience with no flag of its own.** `description` is the single most prominent element (`hero-desc`, 21-29px); sorafuel's hero = "**Produces** sustainable aviation fuel…" (present-tense, the run-042 G1 maturity over-claim) while its *structured* guard ("captured pages describe a *planned* pilot… future production") is in tab-4 `unverified_fields`. The relay puts the field that most needs a structural flag furthest from one. | That `description` is wrong to feature — it's the right lead field; only that featuring it without an adjacent structured maturity/self-reported flag reproduces 042's over-claim at peak salience (captor prose below may still rescue it — VR1). | read.md Result(2)/C1; sorafuel profile.md:96-98; brief.py:381 | source-rigor, schema-edge-entity-type |
| VR1 | risk-miss | **(Evidence verifier) The read's first framing — "the 5-second path contains zero flags" — was false and is corrected.** remedymeds' **auto-open** Strategic read carries "Scale and outcome figures are *self-reported and internally inconsistent… treat as marketing, not audited metrics*"; sorafuel's auto-open Overview/Strategic read carry "*venture-stage… moving toward pilot production… not a sales storefront… pre-commercial/pilot-stage.*" So the default path DOES carry a caveat **when the captor wrote one** — a captor-prose-dependent, unreliable second channel (run-037 DR2 shape), not the structural absence the read first asserted. Core finding survives, sharpened: the *structured* flags are tab-gated; the *default-path* protection is captor-prose-dependent. Same verifier-catches-a-precision-slip value as run-042/045/048 VR1. | That the salience-inversion finding is wrong — the structured-flag burial holds; only that "5-second path is flag-free" overstated it by ignoring captor prose in the auto-open sections. | read.md Result(2) pre/post correction; remedymeds profile.md:120 (## Strategic read, open); sorafuel profile.md:51-53/118-120; brief.py:259-263 | source-rigor, schema-edge-entity-type |
| G2 | gap | **The renderer's stated intent and its salience disagree.** `brief.py`'s module docstring says the engine's trust surface (capture clocks, unverified fields, enumeration floors) is "rendered visibly **as the product**" — but in practice that surface is tab-gated (tab 4) and the proof section is collapsed. A reader taking the docstring at face value would over-trust the brief's default-view honesty. | That the docstring is false — clocks *do* render in the hero eyebrow; only that "as the product" overstates the salience of the limits surface specifically. | brief.py:1-7 (docstring) vs brief.py:190-222,259-263 | source-rigor, tooling-ergonomics |
| W1 | wish | If anything ever graduates from G1/S2, the lightest path is a **salience tweak in `brief.py`** — surface one flag token at hero grain (a "pre-revenue / pilot" or "figures self-reported" eyebrow beside `description`) or auto-open the limits section — **NOT** a new field or schema change (the data already renders). Load-bearing reason: this is a presentation-layer Judgment owned by the present-layer owner, and the failure is ordering, not capture. Held: n=6, single relay; "no new primitive needed" stays live. | That it should graduate or that the brief should change now — only the lightest path *if* a real 5-second consumer (Scott Witt) is shown to mis-trust the default view AND the present-layer owner agrees tab-4 placement is the bug. | read.md Gap Map / What Would Change; _design/2026-06-12-presentation-layer.md | query-time-grouping-enough, tooling-ergonomics |
| CR1 | gap | (Consumer review) **Value lands on the builder/Steward, not the end reader — map-not-ingredient on the presentation surface.** The deliverable is "here is where the shipped brief buries the structured trust flags," which the present-layer owner consumes; a buyer reading one brief gets no new company fact. Same builder-not-buyer frontier as 038/041/047/048 CR1, here on the brief renderer itself. | That the read failed — it's a gap-probe that lands its builder payload; only that the strongest value is not buyer-facing. | consumer-review.md Verdict; read.md Result | query-time-grouping-enough, tooling-ergonomics |
| DR1 | surprise | (Developer review) **The fix-shape, if any ever graduates, is one-file and grep-verifiable — not a primitive.** The salience finding lives entirely in `scripts/present/brief.py` ordering (hero `description` vs tab-gated structured flags); the lightest response is a layout tweak, no field/schema/module. The anti-pattern to refuse is treating salience as a capture or schema problem, or adding a "flag-salience" config knob — it's a single presentation Judgment downstream of State. Pairs S2/W1 with engine-dev's least-complexity bar. | That a fix is due — out-of-band/Brian's call; only that the disposition is "one-file ordering Judgment," not "new primitive." | developer-review.md Dev Agent/Founder; brief.py:259-263,381; .claude/rules/engine-dev.md | tooling-ergonomics, query-time-grouping-enough |

## Inputs and scope

- **Renderer:** `scripts/render.py` → `scripts/present/{model,brief}.py` (read in full).
- **Command:** `python scripts/render.py remedymeds henrymeds sorafuel etsy euclidpower therabody --no-fetch` → `_out/briefs/<slug>.html`.
- **Panel (6, purposive — flag-type coverage, not a census):** remedymeds-com, henrymeds-com,
  sorafuel-com, euclidpower-com, therabody-com, etsy-com. 3 carry `offerings.md` (remedymeds,
  henrymeds, therabody).
- **Flag contracts referenced:** SCHEMA.md price-visibility token; `unverified_fields`,
  `site_notes`, STRAIN conventions.
- **Exclusions:** comparison sheet (`compare.py`), corpus index (`index.py`), direct
  `profile.md` agent consumption — not audited. No external network; `--no-fetch` used.

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

Repeated manual steps, took a long time, confusing paths, missing helpers, schema mismatches.
Summarize the operational friction here after preserving concrete sightings in the
Observations section.

## Evidence limits

- **n=1 relay, n=6 profiles.** Audits only the single-company HTML brief (`brief.py`).
  The comparison sheet, index, and direct `profile.md` consumption could relay flags with
  different salience — untested.
- **"5-second path" is an analytic proxy, not observed behavior.** It is the default-open DOM
  path (hero + auto-open Overview/Strategic read), not a measured reader study. The flags are
  one click away; whether a real reader clicks before acting is unmeasured.
- **Salience is a Judgment surface.** Whether tab-4 placement is a "bug" or correct-by-design
  (limits filed under Provenance) is the present-layer owner's call; the run only shows the
  default path is flag-free, not that the layout is wrong.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass** (`local-existing`, `autonomous_eligible: yes`, `approval_needed: no`)
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (`local-existing`)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (not bounded-live)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no network/Firecrawl/SERP, no `store/` mutation, no script edits, briefs written only to `_out/`)
- Required citations / receipts present and source-graded: **pass** (`receipts/C1-render-structure-audit.md`, derived/local-store, claims C1–C4)
- No snippet treated as evidence: **pass** (no snippets; all evidence is local code + generated HTML)
- Current/news/pricing/policy claims carry capture dates and source grade: **n/a** (no external/current claims; profile prices read only as rendered, not re-verified)
- Absence language says "not found", not "not true": **pass** (read says "off the default path"/"not audited," not "absent")

## Surprises

The framing flipped mid-run: the run was designed expecting `render.py` to drop flags
(launder them), and instead found the brief preserves every flag faithfully — the real
finding is a salience inversion (flags buried in tab 4 / collapsed; the over-claim-prone
`description` in the hero). A cleaner, more useful result than the hypothesis: the relay-risk
thread is a *preserve-but-bury* ordering property, not a content-drop. See S1/G1/S2.

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

Fired: `source-rigor` (the flags are the source-rigor surface, and salience defeats them on
the default path), `tooling-ergonomics` (the fix, if any, is a presentation-layer ordering
tweak), `query-time-grouping-enough` (no new field/primitive — the data already renders),
`schema-edge-entity-type` (the hero `description` over-claim is sharpest on pre-revenue
deep-tech, the run-042 entity type). No new tag needed — `source-rigor` + `tooling-ergonomics`
cover "the relay preserves but buries." "No new primitive needed" holds.

"No new primitive needed" is a valid outcome.

## Next-run advice

- To generalize "preserve-but-bury" past n=1 relay, audit the comparison sheet (`compare.py`)
  and the index (`index.py`) for the same salience inversion — does the comparison view also
  bury `unverified_fields` / feature `description`?
- A complementary read: take a real delegated-agent consumption path (a prompt that hands an
  agent `profile.md`) and check whether *it* carries the flags — the other half of the
  relay-risk thread that the HTML brief doesn't cover.
- Don't re-run this as a build proposal. The lightest path (W1) is a present-layer Judgment;
  graduation is out-of-band and Brian's call.
