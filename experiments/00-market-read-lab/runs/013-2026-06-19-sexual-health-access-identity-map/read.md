# Market Read

## Question

In the ED / sexual-health telehealth cohort the store has captured, what access and offer
models do brands use (cash-pay vs insurance, async vs hybrid, compounded vs FDA-brand,
subscription vs one-off, membership wedge), and which buyer identity does each brand speak to?

## Direct Answer

Reading the store's **6 ED-identity brands** on their structural frontmatter cuts
(`pay_model` / `modality` / `compounding_posture` / `access_model` / `audience`), three
patterns hold and one is a coverage hole:

1. **Access model tracks anchor position.** The three brands *anchored* in sexual-health
   (rugiet, rexmd, bluechew) all run **`access_model: all-in`** — consult + meds bundled
   into one price, no membership wedge. The three brands where ED is a *secondary* line
   (hims, keeps, ro) all run **`access_model: à-la-carte/both`**, where the membership
   wedge sits on their *front-door growth* category (GLP-1 for hims/ro, hair for keeps)
   and ED is a standalone per-product subscription. **The membership wedge lives on the
   growth category, not on ED.** *(Judgment — a clean correlation across 6 brands, not a law.)*
2. **Modality splits on controlled substances, not on ED.** Single-vertical ED is **async**
   (bluechew). Brands that bolt TRT onto the ED line go **hybrid** — video is required for
   testosterone (rugiet, rexmd; hims is hybrid for its own breadth). ro stays **async**
   because it routes GLP-1, not TRT. ED itself is async everywhere; sync appears only where
   a controlled hormone is added.
3. **Pay model is both the differentiator and the coverage hole.** rexmd is **`cash-pay only`**
   ("does not accept insurance"), rugiet/hims are **`HSA/FSA eligible`** (cash rail, not
   insurance-billed), and ro **`bills insurance`** — the lone insurance-integrated brand, and
   the only `all-genders` one. But `pay_model` is **`unclear` for bluechew and keeps** — the
   store has no captured pay statement for 2 of 6. The access read is confident for 4 of 6.

**Buyer identity** (verbatim hero/positioning, `audience` field): all **men-only** except
**ro (all-genders)**. The ED-anchored three split the men's market by *tone* — rugiet =
**performance/optimization** ("Performance Medicine For Men" / "RUGIET FOR SEX"); rexmd =
**mainstream value access** ("Telemedicine for Men"; "475,000 men… take charge of their
sexual health"; persistent "$2 per tablet" ED sale); bluechew = **casual lifestyle
convenience** (the chewable; "HAVE BETTER SEX!"). The companion three lead elsewhere: hims =
lifestyle brand pivoted to weight; keeps = hair-first; ro = clinical/insurance-integrated,
GLP-1-led. **White space (Judgment):** no captured brand owns a *premium-clinical,
sexual-health-first* identity for men — ro is clinical but all-genders and GLP-1-led, while
the three ED-anchored brands all sit in value / performance / convenience.

## Evidence Used

All from cached store State (`telehealth.md` frontmatter, quoted verbatim — not re-derived
from prose). No external sources, no spend. Capture clocks per row.

| Brand | captured_at | anchor_category | ED-tier | audience | pay_model | modality | compounding_posture | access_model |
|---|---|---|---|---|---|---|---|---|
| rugiet.com | 2026-06-07 | sexual-health | anchored | men-only | HSA/FSA eligible | hybrid | both | all-in |
| rexmd.com | 2026-06-04 | sexual-health | anchored | men-only | cash-pay only | hybrid | both | all-in |
| bluechew.com | 2026-06-04 | sexual-health | anchored | men-only | **unclear** | async | compounded-only | all-in |
| hims.com | 2026-06-18 | GLP-1 | ED origin | men-only | HSA/FSA eligible | hybrid | both | à-la-carte/both |
| keeps.com | 2026-06-04 | hair | ED companion | men-only | **unclear** | async | both | à-la-carte/both |
| ro.co | 2026-06-18 | GLP-1 | Roman ED origin | all-genders | bills insurance | async | both | à-la-carte/both |

The structural cells — `anchor_category`, `audience`, `pay_model`, `modality`,
`compounding_posture`, `access_model` — are frontmatter values quoted verbatim from each
brand's `telehealth.md` (value + inline `#` justification). `unclear` is the store's own
captured value (no pay statement on captured pages), not an inference. **The `ED-tier` column
is a hand-drawn Judgment** (which tier of the cohort a brand sits in), sourced from each
brand's *body* prose (hims body: "Sexual health is the origin franchise"; keeps body: ED "the
newer companion"; ro body: men-origin / began as Roman) — **not** from the `anchor_category`
field or its `#` comment. It is the run's cohort-boundary call, not a captured field.

## Companies Seen

- **Cohort — ED-identity (6, scored above):** 3 anchored (`anchor_category: sexual-health`:
  rugiet, rexmd, bluechew) + 3 ED-as-named-franchise anchored elsewhere (hims = ED origin;
  keeps = ED companion to hair; ro = Roman ED origin, now GLP-1 front door).
- **Straddler tail (sell ED, no ED identity — named, not scored):** a grep for ED terms
  (`erectile|sexual health|sildenafil|tadalafil`) across `store/*/telehealth.md` returns
  **24 brands**. The 18 beyond the cohort are TRT shops (getopt, vitalityrx, trtnation,
  marekhealth, defymedical, getpetermd) and GLP-1 / `multi/none` generalists (lifemd,
  joiandblokes, malemd, mydrhank, hydramed, goodlifemeds, struthealth, invigormedical,
  agelessrx, eden, henrymeds, home-medvi) that list a sildenafil/tadalafil line without an
  ED front-door identity.

## Missing / Stale Coverage

- **`pay_model: unclear` for bluechew + keeps** (2 of 6 cohort brands). A structural field
  that's only ~67% populated can't carry a confident cohort-wide access claim. Concrete
  depth-backfill: capture each brand's billing/insurance statement.
- Captures span 2026-06-04 → 2026-06-18; rexmd/bluechew/keeps are the oldest (06-04). All
  carry point-in-time hero caveats (A/B-rotating front doors), but the *structural* cuts
  read here are the durable ones, less A/B-volatile than the hero.

## Source Gaps

- The read is **structural State only.** It does not touch price levels, offer-ladder rungs,
  or trust/objection content — the buyer-*identity* read leans on hero copy, not on what
  buyers actually say (the MRL-010 reviews-as-bodies gap; out of scope for a store-only run).

## External Completeness Check

Not run — store-only by contract. The cohort boundary is hand-drawn (see Market Pattern);
no external denominator was consulted. Treat the 6-brand cohort as the *ED-identity* set, not
the *ED-selling* set (24 in store, certainly more in market).

## Market Pattern

- **The structural cut held up as a load-bearing read** — the first lab run whose answer
  rests on `pay_model`/`modality`/`compounding_posture`/`access_model` rather than the
  well-worn `Visibility`/pricing/`Credibility` cuts. The fields were populated and verbatim-
  quotable for 5 of 6 brands (pay_model the lone gap).
- **Anchored-only grep silently under-counts the ED market** — `anchor_category: sexual-health`
  returns 3; the ED-selling set is 24. Same anchored-vs-all-offerers under-count MRL-001 named
  on GLP-1 (run 012), now recurring on the sexual-health cohort. The cohort had to be
  hand-drawn into 3 tiers (anchored / ED-franchise / straddler).
- **Access model correlates with anchor position** (all-in for ED-anchored; à-la-carte/both
  for ED-companion). Interesting State pattern in a 6-brand sample — labeled a Judgment, not a
  durable rule.

## What Would Change This Answer

- Capturing pay statements for bluechew + keeps (closes the 2/6 hole; could break or confirm
  the "ED-anchored = cash/HSA, never insurance" read).
- A re-capture flipping an A/B front door (e.g. hims/ro rotating ED back to the hero) would
  re-sort the anchored-vs-companion split this read depends on.
- Pulling the straddler tail into scope (24 ED-sellers) would test whether the all-in vs
  à-la-carte correlation survives outside the 6 ED-identity brands.
