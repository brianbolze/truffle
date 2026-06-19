# Store-Derived GLP-1 / Medical Weight Loss List

Date: 2026-06-19
Method: local store parse (no scraping, no spend). Captures span 2026-05-30..2026-06-18.

## How it was built

Three store layers, unioned on slug, then filtered by value-chain role:

1. **Telehealth cohort packs** (`store/*/telehealth.md`) — `anchor_category: GLP-1`
   (front-door / leads-with) and the body `Categories served` line including GLP-1.
2. **Offerings rosters** (`store/*/offerings.md`) — any SKU row whose molecule/form
   cell names `semaglutide|tirzepatide|liraglutide|wegovy|ozempic|mounjaro|zepbound|
   retatrutide|GLP-1`.
3. **Profile bodies** (`store/*/profile.md`) — same molecule regex.

Raw union: **53 slugs**. After cleaning (below): **48 DTC sellers + 3 compounding-pharmacy
suppliers + 1 white-label infra**.

### Cleaning (keyword membership over-counts)

- **bluechew-com — removed.** The `Categories served` line reads *"No TRT, **GLP-1**, hair…"* —
  the keyword matched inside a **negation**. A naive grep counts it as a GLP-1 brand; it isn't.
- **onemedical-com — not GLP-1.** Resolves from Notion "One Medical (Amazon)" but the profile
  has **0** GLP-1 mentions; it's membership primary care.
- **onepeloton-com, truniagen-com — false positives** from a looser `weight` term in the
  aggregate pass only; not in the molecule-based union.

Lesson: build the denominator from `telehealth.anchor_category` + roster molecule cells +
`value_chain_role`, **not** a raw body grep.

## DTC GLP-1 sellers (48)

GLP-1 is the front door (`anchor_category: GLP-1`) — leads-with weight loss (20):

`altrx-com`*, `brellohealth-com`, `directmeds-com`, `eden-health`, `effecty-com`,
`goodlifemeds-com`, `henrymeds-com`, `hims-com`, `home-medvi-org`, `ivimhealth-com`,
`ivyrx-com`, `joinamble-com`, `joinfound-com`, `joinfridays-com`, `mydrhank-com`,
`noom-com`, `remedymeds-com`, `ro-co`, `telolife-com`, `tryshed-com`

\* altrx-com is a profiled DTC GLP-1 brand ("the cheapest GLP-1 program") but has **no**
`telehealth.md`/`offerings.md` module layer — so it's GLP-1-led by its profile, not by an
`anchor_category` field. Module-backfill candidate.

GLP-1 as a line inside a broader TRT / longevity / sexual-health / multi menu (28):

`agelessrx-com`, `defymedical-com`, `gethealthspan-com`, `getopt-com`, `getpetermd-com`,
`gogeviti-com`, `hellopepti-com`, `hellowisp-com`, `hevahealth-com`, `honehealth-com`,
`hormonemd-com`, `hydramed-com`, `invigormedical-com`, `joiandblokes-com`,
`kingsbergmedical-com`, `lifemd-com`, `malemd-com`, `marekhealth-com`,
`marquelongevitylab-com`, `maximustribe-com`, `mylifeforce-com`, `nurx-com`,
`prohealth-com`, `rexmd-com`, `rugiet-com`, `sermorelin-com`, `struthealth-com`,
`trtnation-com`

## Supply-side / infra (not DTC sellers, surfaced by the same grep)

- **Compounding-pharmacy suppliers (3):** `hallandalerx-com` (503A, B2B),
  `millspharmacy-com`, `strivepharmacy-com` (503A). They *make* GLP-1; they don't sell a
  consumer program.
- **White-label infra (1):** `openloophealth-com` (B2B telehealth backbone; sells GLP-1
  supply to partners). Notion correctly parked this as context-only.

## Reconciliation vs Notion denominator seed (34 primary rows)

`scripts/store.py resolve` folded each Notion name to a slug.

### In both (24 confirmed GLP-1 sellers)

AgelessRx, Alt Rx, Blokes (`joiandblokes-com`), Defy Medical, Dr Hank (`mydrhank-com`),
Effecty, Fridays (`joinfridays-com`), Henry Meds, Hims & Hers, Hone Health, HormoneMD,
Invigor Medical, Ivy Rx, Kingsberg Medical, LifeMD, Lifeforce (`mylifeforce-com`),
Maximus Tribe, Medvi (`home-medvi-org`), Noom Med (`noom-com`), ProHealth, Remedy Meds,
Ro, Shed Rx (`tryshed-com`), TRT Nation.
*(Plus "Mens" → `malemd-com` as a probable-but-uncertain fuzzy match — counted separately.)*

### Notion-only (10): in the seed, not a confirmed store GLP-1 seller

- **Absent from store (8):** Citizen Meds, Gala, GoodRx, Klarity Health, Max Life, omzo,
  TMates, Trim Rx.
- **Profiled but not GLP-1 (1):** One Medical (Amazon) — primary care, 0 GLP-1 SKUs.
- **Uncertain match (1):** "Mens" → `malemd-com` (fuzzy; could be another brand).

### Store-only (~24): GLP-1 sellers the Notion primary list omits

`brellohealth-com`, `directmeds-com`, `eden-health`, `gethealthspan-com`, `getopt-com`,
`getpetermd-com`, `gogeviti-com`, `goodlifemeds-com`, `hellopepti-com`, `hellowisp-com`,
`hevahealth-com`, `hydramed-com`, `ivimhealth-com`, `joinamble-com`, `joinfound-com`,
`malemd-com`, `marekhealth-com`, `marquelongevitylab-com`, `nurx-com`, `rexmd-com`,
`rugiet-com`, `sermorelin-com`, `struthealth-com`, `telolife-com`.
*(joinfound-com is Found; Eucalyptus was a Notion context-only row but is a different entity.)*

### Headline

- Notion → store hit rate: **24/34 = 71%** confirmed GLP-1 sellers (26/34 = 76% profiled at all).
- Store adds **~24** GLP-1 sellers Notion's primary list misses.
- Overlap ≈ 24; symmetric difference is large on **both** sides. **Neither list is exhaustive;
  union ≈ 48 + the 8 unprofiled Notion names = ~56 known, and that's still a floor.**

## Per-SKU price-visibility aggregate (the read's core)

229 buyable GLP-1 SKU rows across ~45 rosters (family/no-price rows excluded):

| Visibility token | SKUs | Share |
|---|---|---|
| `published` (self-contained number on page) | 75 | 33% |
| `partial` ("from / starting at" floor; real price set in gated intake) | 97 | 42% |
| `on-request` (no price until consult / quiz) | 57 | 25% |

Company-dominant mode splits roughly evenly three ways (~17 publish-led, ~17 floor-led,
~11 gate-led). Source: `offerings.md` `Visibility` column, per QUERYING Recipe 4.
