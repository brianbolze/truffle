# Market Read

## Question

Cutting the captured telehealth store by **audience** (men-only/men-first,
women-only/women-first, all-genders) rather than by category, how does brand supply
distribute across the audience × `anchor_category` grid — where is the gender market thin
or empty per condition, and is the apparent men-leaning vs women-leaning asymmetry a real
captured pattern or a store-coverage artifact?

## Direct Answer

Among the **54 captured telehealth brands** (all 54 carry both `audience` and
`anchor_category` verbatim), supply is **strongly men-tilted and category-polarized — but
the tilt is a store-coverage artifact, not a market finding** (see caveats; this is the
load-bearing limit of the whole read).

Captured supply by audience lean (State, verbatim from frontmatter):

| Lean | n | Frontmatter values |
|---|---|---|
| All-genders | 34 | `all-genders` |
| Men-leaning | 15 | `men-only` (7) + `men-first` (8) |
| Women-leaning | 5 | `women-only` (3) + `women-first` (2) |

The **audience × category grid** (counts are captured brands; rows are `anchor_category`
verbatim):

| category | MEN | WOMEN | ALL | total |
|---|---:|---:|---:|---:|
| GLP-1 | 2 | 3 | 14 | 19 |
| TRT | 7 | 0 | 1 | 8 |
| longevity/NAD | 0 | 0 | 8 | 8 |
| multi/none | 1 | 1 | 8 | 10 |
| sexual-health | 3 | 0 | 0 | 3 |
| peptides | 1 | 0 | 1 | 2 |
| womens-HRT | 0 | 1 | 0 | 1 |
| hair | 1 | 0 | 0 | 1 |
| labs | 0 | 0 | 1 | 1 |
| primary-care | 0 | 0 | 1 | 1 |

**Three captured patterns (State + labeled Judgment):**

1. **TRT and sexual-health are the male-coded verticals.** TRT is the most polarized cell
   in the grid — **7 men-leaning, 0 women-leaning, 1 all-genders** (hormonemd). All 3
   captured sexual-health (ED) brands are `men-only`. Men-leaning supply concentrates
   almost entirely in these two lanes (10 of 15). *(State: the cells. Judgment: "male-coded
   vertical" — a positioning read of where men-anchored brands cluster.)*

2. **Women-leaning supply is tiny and lives in two lanes — GLP-1 and HRT.** All 5
   women-leaning brands are: 3 in GLP-1 (`brellohealth`, `effecty`, `remedymeds`),
   1 womens-HRT (`innerbalance`), 1 generalist (`nurx`). **Zero women-anchored brands in
   TRT, longevity/NAD, sexual-health, peptides, hair, labs.** *(State.)*

3. **Longevity/NAD is fully gender-neutral.** All 8 captured longevity brands are
   `all-genders` — no gendered front door at all in that lane (the largest single
   audience-homogeneous cell). GLP-1 is the most audience-balanced category (the only one
   with women-leaning supply present alongside men- and all-genders). *(State.)*

**The whitespace, stated honestly:** the empty cells (e.g. "no women-anchored TRT/hormone-
optimization brand," "no women-anchored longevity brand") are **store-coverage absences,
not proven market whitespace.** Two independent coverage mechanisms bound every cell —
see *What Would Change This Answer*. The honest payload is **a map of where the *captured*
store is thin by gender, plus a candidate whitespace hypothesis a human could test
live** — not a market whitespace claim.

## Evidence Used

All evidence is local store frontmatter (`store-only`); no external/current claims, no
snippets, no spend. Receipt: `receipts/audience-category-crosstab-2026-06-20.md`.

- **C1** — 54 brands have a `telehealth.md`; all 54 carry both `audience` and
  `anchor_category`. (S1, derived from local store.)
- **C2** — Audience buckets: all-genders 34 / men-first 8 / men-only 7 / women-only 3 /
  women-first 2. (S1.)
- **C3** — The audience × `anchor_category` cross-tab above, taken with `audience` value
  read **verbatim from the frontmatter field** (not inferred from brand name), the comment
  stripped. (S1.)
- **C4** — The 5 women-leaning brands and the all-male TRT/sexual-health cells, by domain.
  (S1.)

## Companies Seen

54 telehealth domains. Load-bearing named sets:

- **Women-leaning (5):** brellohealth-com (women-only/GLP-1), effecty-com
  (women-first/GLP-1), innerbalance-com (women-only/womens-HRT), nurx-com
  (women-only/multi-none), remedymeds-com (women-first/GLP-1).
- **TRT (8):** defymedical, getopt, getpetermd, marekhealth, maximustribe, trtnation
  (men-first); vitalityrx (men-only); hormonemd (all-genders).
- **Sexual-health (3):** bluechew, rexmd, rugiet (all men-only).
- **Longevity/NAD (8):** agelessrx, gethealthspan, gogeviti, honehealth, mylifeforce,
  niagenplus, prohealth, truniagen (all all-genders).
- **multi/none generalists (10):** hellowisp, hevahealth, hydramed, invigormedical,
  joiandblokes, kingsbergmedical, lifemd, struthealth (all-genders); malemd (men-only);
  nurx (women-only).

## Missing / Stale Coverage

- **20 of the 135 store domains** are telehealth-but-not-in-this-cut? No — the cut is the
  54 with `telehealth.md`; the other 81 store domains are non-telehealth or un-moduled and
  out of scope by construction.
- **The cohort is intentionally men's-health/hormone-tilted** (per prior lab runs
  001/008/014/016, which seeded TRT/men's-hormone captures). This is the single biggest
  coverage caveat and it directly produces the 15-vs-5 asymmetry.

## Source Gaps

- No demand-side evidence (traffic, market share, revenue) — "thin supply" ≠ "small
  market." A category can be all-genders in supply yet have a large women's sub-segment
  served by those same all-genders brands.
- `audience` is a supply-side *positioning* field (who the front door addresses), not a
  customer-mix measurement. A `men-first` brand may serve many women (the field comments
  flag several straddlers, e.g. `men-first` brands whose weight-loss/labs lines are not
  gender-gated).

## External Completeness Check

Not run (store-only by contract). A bounded-live corroboration is the natural next step
(see *What Would Change This Answer*) — but the read deliberately makes **no** external
completeness claim. The 54 is a floor.

## Market Pattern

*(All below are labeled Judgments built on the State cross-tab.)*

- The captured store mirrors the **legacy gendering of telehealth verticals**: TRT and ED
  are male-coded front doors; menopause/HRT is the one female-coded front door; GLP-1 and
  longevity are the gender-neutral "new" categories where supply doesn't pick a side.
- **GLP-1 is where women-anchored brands actually exist** — the only category that drew
  dedicated women-first/only entrants (brello, effecty, remedymeds). Plausibly because GLP-1
  is a large, gender-balanced, newly-DTC market where a women-framed wedge is viable; the
  established hormone lanes (TRT) were colonized men-first long before.
- **Candidate whitespace hypothesis (NOT a finding):** a *dedicated women's hormone-
  optimization / longevity* front door is absent from the captured store. Whether that is a
  real market gap or just absent from this cohort is **exactly what this store-only read
  cannot answer** — it is a live-evidence question.

## What Would Change This Answer

1. **The coverage tilt is the answer's ceiling.** The 15-vs-5 men/women asymmetry is
   **bounded by intentional cohort selection** — the lab's telehealth captures were seeded
   men's-hormone-heavy. A representative recapture (or a neutral external denominator) could
   move the ratio sharply. *Treat the asymmetry as a captured-supply count, not a market
   fact.*
2. **The anchored-only under-count (MRL-001) makes every per-category cell a floor.** The
   10 `multi/none` generalists (8 all-genders) sell into TRT/HRT/longevity/sexual-health
   *without anchoring there*, so a "0 women in TRT" cell means "no women-**anchored** TRT
   brand captured," **not** "women can't get TRT" — all-genders generalists serve them. Any
   per-category audience cell undercounts actual gendered service.
3. **`audience` is positioning, not customer mix.** Field comments flag straddlers
   (`men-first` brands with non-gender-gated weight-loss/labs lines). A demand-side read
   could show the gendered front doors serve far less gendered customer bases.
4. A **bounded-live** check — a "best women's telehealth 2026" listicle panel + a few owned
   women's-health sites — would test whether the dedicated-women's-hormone whitespace is
   real market or just store-absent (mirrors run 012's listicle-as-coverage-radar).
