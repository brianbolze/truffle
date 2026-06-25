# Market Read

## Question

A buyer wants to improve **sleep & recovery** and is open to any solution type. Can
Truffle assemble the cross-category option set — connected hardware (Oura / Whoop /
Eight Sleep / Apple Watch), recovery devices (Therabody / Hyperice), and any
supplement / longevity / telehealth entrants — from captured State alone, or do
`primary_industry` / `offering_category` tags scatter the substitutes so the buyer's
"what are my options?" question is structurally unanswerable?

## Result

**Lead (gap-probe):** Truffle holds rich, well-captured State on each individual
member of the sleep/recovery option set, but **no structured field recovers the set as
a set.** The cross-industry substitute neighborhood is *reader-assemblable by hand*
(full-text reading of `description` + body across cohorts) but **not queryable** — a
run Judgment, not store State. This is the "diagnosable but not queryable / map-not-
ingredient" frontier (cousin of run-039 CR1 and run-043 CR1), now at the **buyer-goal
grain** rather than the relations or price axis.

**(1) No JTBD/use-case cut exists.** Grep over all 145 profiles for any
`use_case` / `job_to_be_done` / `jtbd` / `condition` / `vertical` frontmatter field
returns nothing (C1). The store has no field that says "serves the sleep/recovery
job." The only way to find the set is to read prose.

**(2) `primary_industry` scatters the core device set across three industries** (C2):

| Member | primary_industry | offering_category | How it serves the sleep/recovery job |
|---|---|---|---|
| eightsleep.com | **Technology** | Physical Products / Hardware | Pod: heats/cools/tracks sleep |
| ouraring.com | **Healthcare & Life Sciences** | Hardware, Software / SaaS | Ring: 50+ sleep/recovery metrics |
| whoop.com | **Healthcare & Life Sciences** | Hardware, Software / SaaS | Band: sleep + recovery coaching |
| apple.com (Watch) | **Technology** | Hardware, Media, SaaS, Fintech | Apple Watch sleep tracking (catalog-grain) |
| therabody.com | **Healthcare & Life Sciences** | Hardware, Services / Consulting | Recovery + sleep (Theragun, masks) |
| hyperice.com | **Sports & Recreation** | Physical Products / Hardware | Recovery devices |
| nike.com | **Sports & Recreation** | Physical Products / Hardware | Electronic recovery (minor line) |
| onepeloton.com | **Sports & Recreation** | Hardware, Media / Content | Fitness→recovery framing (weak) |

A naive `primary_industry` draw recovers none of this cohort; it scatters across
Technology / Healthcare & Life Sciences / Sports & Recreation **for the device members
alone.**

**(3) The only shared structured tag is too coarse and still incomplete.** Every
device member carries `offering_category: [Physical Products / Hardware]`, but that
value spans **19 profiles** store-wide (C3) — it also pulls in Casio, watch brands,
and Apple's whole catalog, which are not sleep/recovery substitutes — *and* it misses
the telehealth entrants entirely (next point). So even "draw all Hardware" is both
over- and under-inclusive for the JTBD.

**(4) The telehealth Rx-sleep entrants are doubly buried** (C4). `rexmd`, `rugiet`,
and `malemd` each sell a prescription **sleep** treatment line, but: (a) their
`offering_category` is `[Services / Consulting, Biotech / Pharma Products]` and
`primary_industry: Healthcare & Life Sciences` — no overlap with the device members'
tags; and (b) "sleep" is one minor line buried among ED / TRT / GLP-1 / hair, visible
only by grepping the `description`. No device/wearable draw would ever surface them as
substitutes for the sleep buyer.

**(5) No horizontal substitute relation exists.** Oura, Whoop, and Eight Sleep are
mutual substitutes for the sleep buyer, yet the store carries **zero** edges between
them. Relation support is vertical-only (`parent` / `owns`); the competes-with /
substitute axis is structurally absent (re-confirms run-039 S1, run-047), so the
neighborhood cannot be traversed even one hop.

**Net:** the buyer's "what are my options for sleep & recovery?" is answerable **only
by a human reading prose across the store and exercising substitution judgment.** The
store is an excellent per-member fact base and a poor JTBD-neighborhood index.

## Gap Map

- **Answered cleanly:** every individual member's offering, price posture, and
  business model is captured well (consistent with runs 037/043). The *ingredients* are
  present and decision-grade per company.
- **Fell short:** assembling the cross-industry substitute **set** from structured
  fields. No JTBD field; `primary_industry` scatters; `offering_category`'s shared
  value is over-inclusive and misses telehealth; no horizontal relation. The set is a
  reader Judgment, not queryable State.
- **What would have changed the answer:** a `use_case` / JTBD tag, or a horizontal
  substitute relation, or a consistent "conditions served" body block grep-able across
  cohorts. None exists. (See *What Would Change* for why none clears the build bar
  today.)

## Evidence Used

All local store-only; store clock = each profile's `captured_at`. Receipts:
[`receipts/C1-no-jtbd-field.md`](receipts/C1-no-jtbd-field.md),
[`receipts/C2-industry-scatter.md`](receipts/C2-industry-scatter.md).

- **C1** — No `use_case`/`jtbd`/`condition`/`vertical` frontmatter field exists across
  any of 145 profiles (empty grep).
- **C2** — The 8 device/recovery members scatter across 3 `primary_industry` values.
- **C3** — `offering_category: [Physical Products / Hardware]` spans 19 profiles
  (over-inclusive; includes watches/Casio/Apple catalog).
- **C4** — `rexmd` / `rugiet` / `malemd` carry a prescription "sleep" line in
  `description`, tagged `Services / Consulting` + `Biotech / Pharma` (no device overlap).
- **C5** — Supplement/compounding adjacency (`anazaohealth`, `keeps`, plus the above)
  surfaces only by grepping `melatonin|magnesium|sleep aid|circadian` — fuzzy edge,
  full-text-dependent.

## Companies Seen

Core device/recovery: eightsleep, ouraring, whoop, apple (Watch, catalog-grain),
therabody, hyperice, nike (minor), onepeloton (weak). Telehealth Rx-sleep: rexmd,
rugiet, malemd. Supplement/compounding adjacency (fuzzy): anazaohealth, keeps.

## Missing / Stale Coverage

The set is **partial by construction**: it was assembled by full-text grep on a small
keyword set (`sleep`, `recovery`, `melatonin`, `magnesium`, `circadian`). A brand
serving the sleep job through, e.g., a supplement named without those tokens, or a
mattress/CPAP/app category the store holds none of, would be missed. **"Not found" via
this method is not "not there."** No external denominator was consulted (store-only by
contract); a "best sleep tech 2026" coverage radar (parked candidate C4 in `scout.md`)
would be the bounded-live way to test whether whole solution types are absent.

## Source Gaps

- **No JTBD / conditions-served surface.** The single missing cut that would make this
  queryable; today it lives only in scattered `description`/body prose.
- **No horizontal substitute relation** (vertical-only relation support).
- **External demand-side panel** (SERP / listicles / "people also bought") would be
  needed to validate the substitute set's completeness — out of scope for store-only.

## Raw Learning to Preserve

See `run-notes.md` Observations: **G1** (no JTBD field; set is a Judgment not State),
**G2** (5th sighting industry≠cohort, now buyer-goal grain), **S1** (telehealth
entrants doubly buried), **G3** (horizontal relation absent — re-confirm), **S2**
(only-shared tag over- and under-inclusive), **W1** (lightest path = query-time recipe,
held).

## External Completeness Check

Not performed — store-only by contract. Completeness is explicitly caveated as
method-bounded (Missing / Stale Coverage). Flagged as the parked bounded-live follow-up.

## Market Pattern

For a consumer goal that spans industries — "sleep & recovery" — the *market* is a
cross-category substitute set (hardware + wearables + recovery devices + Rx +
supplements), but the *store's* organizing axes (`primary_industry`,
`offering_category`) are **producer-shaped, not buyer-goal-shaped.** They answer "what
kind of company is this?" cleanly and "what options serve my goal?" not at all. The
mismatch is structural, not a coverage gap: even with every member captured perfectly,
the JTBD neighborhood remains unqueryable.

## What Would Change This Answer

A reader who needs to **filter/sort** by buyer goal (not just read) — e.g. a
comparison-shopping consumer surface or a delegated "find my options" agent — plus a
**second JTBD** showing the same cross-industry scatter, would raise the question of a
`use_case`/JTBD tag or a horizontal substitute relation. Both fail engine-dev's
fillable-cut bar **today**: JTBD is open-ended and buyer-framed (the company rarely
declares it), a substitute relation would be mostly empty and dangling (run-039 W1
logic), and no cross-JTBD consumer has appeared. **"No new primitive needed" stays
live.** Lightest path if anything ever graduates: a **query-time recipe** — "grep
`description` + body for the buyer goal across all cohorts; ignore `primary_industry`
and `offering_category` as keys" — not a new field or relation. Mirrors the
anti-sprawl W1 landings of runs 036 / 037 / 039 / 042 / 043.
