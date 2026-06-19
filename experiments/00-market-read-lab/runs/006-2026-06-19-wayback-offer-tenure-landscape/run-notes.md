# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [source-rigor, coverage-caveat, tooling-ergonomics, query-time-grouping-enough]
```

## 30-second operator read

- **Did the run work?** Yes. Store-only, no spend, no mutation. **Second read ever to consume the
  Signals layer** (Run 005 = Trustpilot; this = Wayback), and the first to hit Wayback tenure.
- **What was awkward / the actual finding:** the captured `tenure_days` field is a *trap*. Read
  naively it crowns 20-year incumbents (noom 27y, rexmd/bluechew ~25y, telolife/ivyrx/remedymeds
  22y) — but those are *domain* ages on reused/recycled domains, not brand age. The honest brand-era
  signal is the sparse offer-page captures (e.g. honehealth `/mens/sermorelin/` 38d), not the clean
  root number. The read's value is the caveat, not a ranking.
- **What the next agent should know:** the discriminator that makes tenure trustworthy (snapshot
  density / `status_trail` gaps) is *in the JSON* but not surfaced as a field, so a consumer reading
  only `tenure_days` gets the trap with no warning. Same latest-per-dir + extract loop as Run 005 had
  to be hand-rolled (2nd Signals-consumption sighting of that friction).

## What happened

Gated on the contract (scout-only → store-only → autonomous → approval:no, all pass). Globbed every
`store/*/signals/wayback/<keyword>/*.json`, kept latest per (domain,keyword) by `captured_at`
(74 raw → 55 distinct / 47 domains), split root vs offer/blog URL, joined `anchor_category` +
`value_chain_role` from `telehealth.md`. Built a snapshot-density reuse diagnostic (pre-2020 vs
2024+ snapshot counts) to test whether old `first_seen` reflects the current brand. One derived
receipt. Kept State (captured archive facts) / Signal (tenure values) / Judgment ("age-credible?",
"revival candidate") explicitly separated. No external fetch, no `store.py` (join was 1:1), no
`store/` write.

## Inputs and scope

- Working set: **47 domains with a captured Wayback signal** (46 telehealth), **55 distinct
  (domain,keyword) captures**, 49 scorable (48 `measured`, 1 `provisional`, 6 `insufficient`).
- Files: `store/*/signals/wayback/<keyword>/<latest>.json`, `store/*/telehealth.md` frontmatter.
- Capture clock: 2026-06-15 / -16 (3–4 days old).
- Exclusions: prior captures per (domain,keyword) (no trend diff — out of scope); the 8 captured
  telehealth packs with no Wayback signal; all non-Wayback signal types; the wider 135-profile store.

## Friction log

- **No reusable signal-aggregation surface — 2nd Signals-consumption sighting.** Same shape as
  Run 005's Trustpilot friction: hand-wrote a loop over signal JSON, picked latest-per-dir, pulled
  fields. Run 005 explicitly said *"if a second Signals-consumption read also has to hand-roll the
  latest-per-dir + extract loop, that recurrence is the signal."* This is that second read.
  (`tooling-ergonomics`)
- **The trustworthiness discriminator isn't a field.** `tenure_days` is top-level and easy to grep;
  the thing that tells you whether to believe it (snapshot density / `status_trail` gaps) had to be
  recomputed from the `snapshots` array. (`source-rigor`)
- Nested `wayback/<keyword>/` layout (vs Trustpilot's flat dir) meant a 2-level glob; minor.

## Evidence limits

- **Captured floor:** 47/135 store profiles, 46/54 telehealth. "Oldest/newest" is within this slice.
  (`coverage-caveat`)
- **`first_seen` ≠ brand age** for reused domains; the reuse diagnostic is a *derived heuristic*
  (snapshot density), not proof of an ownership change. It flags unreliability; it does not
  establish true founding dates (would need WHOIS/registration — out of scope, store-only).
- **Mostly one URL per domain** — root *or* an offer page, rarely both — so brand-vs-offer tenure
  can't be compared within the same brand for most of the cohort.
- `snapshots_truncated: true` on ivyrx/noom/onemedical → their snapshot counts are floors.
- The category-anachronism argument (C5) uses category-emergence timing (GLP-1 ~2021+, online-ED
  ~2017+) as internal consistency, **not** an external founding-date claim — no receipt needed and
  none asserted.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only` or `local-existing`: **pass** (store-only)
- `approval_needed: no`: **pass**
- No disallowed action happened: **pass** (no browse/CDX re-fetch, no spend, no `store/` write, no
  primitive creation, no write-back; only `read.md` + receipt + run-notes touched)
- Required citations / receipts present and source-graded: **pass** (receipt graded `derived`;
  C1–C6 mapped)
- No snippet treated as evidence: **pass** (no external/snippet sources; all from captured JSON +
  frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (no
  pricing/policy/news claims; every tenure carries its `first_seen` + capture date; category-timing
  used as internal consistency, flagged as such)
- Absence language says "not found", not "not true": **pass** (8 telehealth packs framed as "no
  Wayback signal captured"; `insufficient` captures framed as "no first_seen", not "no history";
  revival flagged as "candidate", not asserted reuse)

All items pass → `run_status: read-done`, `termination_reason: completed`.

## Surprises

- **The cleanest-looking number is the most wrong.** Big `snapshot_count` + old `first_seen` +
  `measured` confidence reads as "established incumbent" — yet ivyrx (750 snaps, first 2004) has
  only 7 pre-2020 snapshots and 482 from 2024+. High confidence on the *archive fact*, near-zero
  reliability for the *brand-age inference*.
- **`snapshot_count` is not popularity.** It tracks archival frequency; reused domains can carry
  huge counts from a prior occupant.
- **Offer-page captures invert the hierarchy.** The thinnest, youngest-looking captures
  (sermorelin/enclomiphene pages, 38–630d) are the *most* honest brand-era markers, because the URL
  only exists once the current brand built that offer.

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
| `source-rigor` | Captured `tenure_days` reads as decision-grade but is brand-age-misleading for reused domains; the trustworthiness discriminator (snapshot density / status-trail gaps) lives in the JSON but isn't a field. | **Append to MRL-008** — 2nd captured-signal-interpretation sighting (Run 005 Trustpilot was 1st). Same family: a captured Signal field carries a built-in confound that must travel with it. Watch; do not build. |
| `tooling-ergonomics` | 2nd Signals-consumption read to hand-roll latest-per-dir + extract; Run 005 named exactly this recurrence as the trigger to consider a tiny signals-read recipe. | **Append to MRL-002 evidence log** — now 2 sightings at the *Signals* grain (distinct from the 3 State-read sightings). Still a documented-recipe candidate, not a built helper; human call. |
| `coverage-caveat` | 47/135 profiles (46/54 telehealth) have a Wayback signal; mostly one URL per domain, so brand-vs-offer tenure rarely comparable within a brand. | No-op / watch. Standard captured-floor caveat for an opt-in signal. |
| `query-time-grouping-enough` | The whole read was answerable by grouping captured signals at query time; no durable tenure/age object needed. Age stays a labeled, caveated Judgment. | No-op / watch. Reinforces no-new-primitive posture. |

## Triage submissions

**Do not implement, spike, or recommend immediate graduation from inside the run.**

- **MRL-008 — append evidence (2nd captured-signal-interpretation sighting).** Run 005 generalized
  MRL-008 from external-monitoring rigor to captured-signal interpretation rigor (Trustpilot score
  conflates regard with solicitation posture). This run is the 2nd sighting at that grain, different
  signal: the Wayback `tenure_days` field reads as decision-grade but conflates *domain history*
  with *brand age* whenever the domain was reused — and the corroborating discriminator (snapshot
  density / `status_trail` gaps) sits in the same JSON unsurfaced. Candidate rule (pattern-level,
  NOT a build): when a read consumes a tenure/age Signal, report the snapshot-density/continuity
  context alongside `tenure_days` and keep "established/new" a labeled Judgment. **2nd sighting in
  this family — the recurrence is now consistent (reputation Run 005, tenure Run 006); worth a human
  look at whether MRL-008 should graduate to a documented "captured-signal confounds travel with the
  field" convention. Not a build.**
- **MRL-002 — append evidence (2nd Signals-grain sighting).** Second consecutive Signals-consumption
  read to hand-roll the latest-per-dir + field-extract loop (Run 005 was the first; this is the
  recurrence Run 005 flagged as the trigger). Strengthens the case for a *documented QUERYING
  signals-read recipe* (latest-per-dir, field extraction, confound fields to always pull) — pattern
  level, alongside the 3 State-read sightings. Still a human graduation call.
- **No new State or Signals primitive.** Tenure is cleanly Signal (captured `first_seen`/snapshots) +
  downstream Judgment ("how established"). The engine captures the right fields; the gap is purely
  interpretive (surfacing the confound), not a missing primitive.
- **Possible no-op note for MRL-007:** like Run 005, this signal is per-domain and attached cleanly
  (no homeless category-level signal), so it gives MRL-007 no new evidence — recorded as the
  per-domain signal path working fine again.

## Next-run advice

- **The Signals layer remains the richest under-exercised territory.** Trustpilot (005) and Wayback
  (006) are done; SEC-presence, branded Trends (only 5 captured — too thin), and **per-brand Wayback
  trend diffs** (multiple captures exist per domain) are the next distinct grains.
- **For any tenure re-read: never trust `tenure_days` alone.** Pull the snapshot-year distribution
  and `status_trail`; treat sparse-pre-2020 / dense-2024+ as a brand-age red flag. Treat
  `snapshot_count` as archival frequency, not popularity.
- **A cheap high-value follow-up:** for the ~10 brands with offer-page captures, capture the root too
  (or vice-versa) so brand-vs-offer tenure is comparable head-to-head — currently it's inferred
  across brands.
- **If a 3rd Signals-consumption read also hand-rolls latest-per-dir + extract**, that crosses Run
  005's "watch for recurrence" into a concrete QUERYING signals-recipe candidate (MRL-002).
