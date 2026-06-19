# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [source-rigor, tooling-ergonomics, denominator-reconciliation, coverage-caveat, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. **3rd read ever to consume the
  Signals layer** (Trustpilot 005, Wayback 006, SEC-EDGAR 007) — and the first to hit SEC. This is
  the 3rd Signals-consumption read that hand-rolled the same latest-per-dir loop, which is the exact
  recurrence trigger Run 006 named for MRL-002.
- **What was awkward / the actual finding:** the captured `total_hits` is a trap (maximustribe shows
  45 hits / 19 CIKs but **zero real filings** — name collision). The signal is only trustworthy
  *because* it ships a `form_d.match` quality grade + `is_vehicle`/`distinct_ciks`. And the sharpest
  fact in the whole read isn't a leaderboard — it's that **niagenplus-com and truniagen-com are one
  CIK** (Niagen Bioscience), invisible to a domain-keyed store.
- **What the next agent should know:** SEC presence is a *minority, lumpy* signal here — ~6 distinct
  issuers across 20 captured brands. Amounts are always null (`existence_only`); never read Form-D
  presence as a raise size. This is the **3rd captured-signal-confound sighting** for MRL-008.

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Globbed every
`store/*/signals/sec_edgar/*.json` (24 raw → 20 distinct domains, latest per domain by `captured_at`),
extracted `state.{is_public,cik,registered_name}`, `form_d.{match,total_hits,distinct_ciks,is_vehicle}`,
`filings[].{form,date}`, `funding_signals[].{amount,flags}`, and joined `value_chain_role` +
`anchor_category` from `telehealth.md`. Classified into 4 buckets by match quality, spotted the shared
CIK by eye. One derived receipt. State (captured filing facts) / Signal (footprint existence + dates) /
Judgment ("maturity tier", "funded") kept explicitly separated. No external fetch, no `store.py` (join
1:1), no `store/` write.

## Inputs and scope

- Working set: **20 domains with a captured `sec_edgar` signal** (19 telehealth packs + waldo-fyi,
  which has no telehealth pack), framed against 54 captured telehealth packs as the captured floor.
- Files: `store/*/signals/sec_edgar/<latest>.json`, `store/*/telehealth.md` frontmatter.
- Capture clock: 2026-06-15 (19), 2026-06-18 (waldo) — 1–4 days old.
- Exclusions: prior captures per domain (no trend diff — out of scope); the ~34 captured telehealth
  packs with no SEC signal; all non-SEC signal types; Form-D primary-doc bodies (amounts — out of scope).

## Friction log

- **No reusable signal-aggregation surface — 3rd Signals-consumption sighting.** Identical shape to
  Run 005 (Trustpilot) and Run 006 (Wayback): hand-wrote a loop over signal JSON, picked latest-per-dir,
  pulled fields, joined frontmatter. Run 006 explicitly said the **3rd** such read crosses
  "watch for recurrence" into a concrete QUERYING signals-recipe candidate. **This is that third read.**
  (`tooling-ergonomics`)
- **The trustworthiness discriminator is, again, not the headline field.** `total_hits` is the
  greppable number and it's the *wrong* one; the thing that tells you whether to believe it
  (`form_d.match` + `distinct_ciks` + `is_vehicle` + `flags`) had to be pulled deliberately.
  (`source-rigor`)
- **Entity dedup is a hand step.** Two domains sharing CIK …6570 was caught by eye, not by any
  CIK-keyed join; a domain-keyed store has no native way to collapse them. (`denominator-reconciliation`)

## Evidence limits

- **Captured floor:** 20/54 telehealth packs have a SEC signal. "Who's funded" is within this slice;
  the other ~34 are *no signal captured*, not *no filing*. (`coverage-caveat`)
- **`no_match` ≠ "never raised."** It means no EDGAR filing was found under the resolved name — a
  brand could be bootstrapped, have raised without a Form D, or filed under a different legal name.
- **`existence_only` / `amount: null` everywhere** — the signal is a presence map, not a sizing read.
- **Filing dates = entity raise, not brand/product age** (Eden's 2017 Form D predates its current
  GLP-1 line) — same domain-history-≠-brand-history caution as Run 006.
- **Public `filings[]` capped at 10** → filing counts for hims/Niagen are floors.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no SEC re-fetch, no browse/spend, no `store/` write, no
  primitive creation, no write-back; only `read.md` + receipt + run-notes touched)
- Required citations / receipts present and source-graded: **pass** (receipt graded `derived`; C1–C6 mapped)
- No snippet treated as evidence: **pass** (no external/snippet sources; all from captured JSON + frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no pricing/policy/news
  claims; every footprint carries its filing dates + capture date; funding framed as existence-only)
- Absence language says "not found", not "not true": **pass** (`no_match` framed as "no filing found
  under the resolved name"; `name_match_unconfirmed` framed as "no usable signal", not "not funded")

All items pass → `run_status: read-done`, `termination_reason: completed`.

## Surprises

- **The biggest `total_hits` number is the most worthless.** maximustribe (45 hits) and joinamble
  (34) top a raw count and have *zero* attached filings — pure common-name collisions. Confidence in
  the *signal* is high precisely because it self-grades the match and flags vehicles.
- **One issuer hides behind two brands.** niagenplus + truniagen → CIK …6570 "Niagen Bioscience" — a
  parent/shared-entity fact the store can't see from domains. A "count of public telehealth companies"
  built naively would double-count.
- **hims' `no_issuer_form_d` is a *correct* read, not a gap** — public-market issuers raise via
  registered offerings, not exempt Form Ds.

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
| `tooling-ergonomics` | 3rd consecutive Signals-consumption read to hand-roll latest-per-dir + field-extract + frontmatter join. Run 006 named the 3rd such read as the trigger to consider a documented QUERYING signals-read recipe. | **Append to MRL-002** — recurrence at the *Signals* grain now = 3 sightings (005/006/007). Crosses Run 006's stated trigger; worth a human look at graduating a *documented* QUERYING signals-read recipe (NOT a built helper). |
| `source-rigor` | `total_hits` reads as the headline but is collision-inflated; the read is only honest because `form_d.match`/`is_vehicle`/`distinct_ciks`/`flags:[existence_only]` travel with it. | **Append to MRL-008** — **3rd captured-signal-confound sighting** (005 reputation, 006 tenure, 007 funding/match-quality). Same family: a captured Signal's headline field carries a built-in confound that must travel with it. Strengthens the graduation case; still a human call. |
| `denominator-reconciliation` | Two brand domains = one CIK (Niagen Bioscience); dedup/entity-resolution was a manual eyeball. The real entity key is CIK, not domain. | Watch. Distinct from the State-read denominator sightings — this is an *entity-resolution-via-CIK* angle. New-ish; note for recurrence, don't build (a CIK entity table would be the anti-Doro reconciliation swamp). |
| `coverage-caveat` | 20/54 telehealth packs have a SEC signal; cohort funding claims are over this slice. | No-op / watch. Standard captured-floor caveat for an opt-in signal. |
| `query-time-grouping-enough` | Whole read was answerable by grouping captured signals at query time; "funded/mature" stays a labeled Judgment. No durable funding/maturity object needed. | No-op / watch. Reinforces no-new-primitive posture. |

## Triage submissions

**Do not implement, spike, or recommend immediate graduation from inside the run.**

- **MRL-002 — append evidence (3rd Signals-grain sighting).** Third consecutive Signals-consumption
  read (Trustpilot 005, Wayback 006, SEC 007) to hand-roll the latest-per-dir + field-extract +
  frontmatter-join loop. Run 006 explicitly set the 3rd such read as the recurrence trigger. The
  recurrence is now consistent across three distinct signal types — a *documented QUERYING
  signals-read recipe* (latest-per-dir, field extraction, and which confound fields to always pull
  alongside the headline value) looks earned. Pattern-level only, NOT a built helper; human graduation call.
- **MRL-008 — append evidence (3rd captured-signal-confound sighting).** 005 (reputation: score
  conflates regard with solicitation), 006 (tenure: domain history ≠ brand age), now 007 (funding:
  `total_hits` is collision-inflated; `existence_only` ≠ amount; match-quality must travel with the
  footprint). Three signal types, same family: **a captured Signal's headline field carries a built-in
  confound that must travel with it.** Note the root-cause spread the item already tracks — SEC adds a
  *third* flavor (the confound is a name-match-integrity grade, captured *correctly* by the tool; the
  risk is purely a naive consumer reading `total_hits`/`tenure_days`/`trust_score` without its
  siblings). Now 3 sightings — recurrence strong; human call on graduating a "captured-signal confounds
  travel with the field" convention. Not a build.
- **MRL-007 (no-op note):** like 005/006, every SEC signal is per-domain and attached cleanly; no
  homeless category-level signal surfaced. No new evidence for MRL-007; recurrence gate unmoved.
- **No new State or Signals primitive.** Funding footprint is cleanly Signal (captured filing
  existence + dates + match grade) + downstream Judgment ("funded / mature tier"). The engine captures
  the right fields. The only *new-ish* observation is the CIK-as-entity-key dedup (relation/entity
  angle) — logged under MRL-002's denominator note as a watch item, explicitly NOT a build (a CIK
  entity-resolution table is the anti-Doro swamp).

## Next-run advice

- **The Signals layer's latest-per-dir loop is now a 3-sighting recurrence — Loop 2 should weigh
  whether MRL-002's signals-read recipe is ready for a human graduation look.** All three reads were
  store-only, query-ready, and re-invented the same scaffold.
- **For any SEC re-read: never rank by `total_hits`.** Filter on `form_d.match == confirmed` (or
  public), and always carry `is_vehicle`/`distinct_ciks`/`existence_only`. Treat `no_match` as "not
  found," not "unfunded."
- **Cheap high-value follow-ups (all store-only):** (a) the **cross-signal 2x2** (sec_edgar × trustpilot
  overlap — funded-but-low-regard / unfunded-but-trusted), the Scout runner-up; (b) a CIK-collision
  sweep across *all* captured `sec_edgar` to see how many other brand pairs share an issuer.
- **To attach raise *amounts*** would need live Form-D primary-doc fetching (approval-gated) — would
  convert this existence map into a sizing read.
