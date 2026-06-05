---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: goodlifemeds.com
captured_at: 2026-06-04
site_notes: "Catalog at /products/<slug> (sexual-health 'ED Mints' is the exception, /ed-mints). The 4 category hubs carry NO prices — pricing is PDP-only. PDP header price widget renders base/promo/compare split across lines ($\\n297\\n$\\n208) but greps fine. TWO pricing models: weight-loss + daily-wellness show a flat monthly price (published); sexual-health + hair show a dose/tier 'Starting at $X' FLOOR with the true price set in the intake quiz (partial). Sitewide SUMMER30 = 30% off every shown price — re-check next run (promo-volatile). Brand-only /products/cialis + /products/viagra exist but aren't in the mega-nav. /products/oral-semaglutide is a dead 404."
---

## Portfolio overview

`Multi-product` — four co-equal lines (Weight Loss · Daily Wellness · Sexual Health · Hair), 26 buyable SKUs. The catalog mixes **compounded** medications (503A/503B-made tirzepatide, semaglutide, peptides, ED/hair blends) with **name-brand FDA** drugs (Wegovy, Ozempic, Zepbound, Mounjaro). Each SKU is an auto-renewing subscription; one bundled price covers consult + medication + shipping.

**Prominence read:**
- **Weight Loss is the lead** `[HIGH]` — line "01", the homepage hero is **Compounded Tirzepatide** tagged "Most Popular," and it's the deepest sub-catalog (9 nav items). Front-door anchor = GLP-1.
- **Compounded GLP-1 over brand** `[MED]` — the three compounded GLP-1s sit first in the weight-loss nav ("Medication") above the "Name Brand" pens; pricing copy pushes the affordability angle ("over 90% less").
- **Daily Wellness #2, Sexual Health + Hair trail** `[MED]` — section order 01→04 and nav depth.
- **Pricing-shape split is the real finding** `[HIGH]` — weight-loss + daily-wellness publish flat monthly prices; sexual-health + hair revert to dose-gated "Starting at" floors (`partial`). What looks like one "transparent pricing" promise is two different models.

A sitewide **SUMMER30** promo (and rotating WELCOME10 / HAPPY2026 coupons) discounts every shown price — the roster carries the **standard (pre-promo)** price; promo figures are in [Verbatim anchors](#verbatim-anchors).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight Loss | family | — | /weight-loss | — | — | The anchor line — compounded + brand GLP-1 for weight management |
| Compounded Tirzepatide | buyable | /weight-loss | /products/tirzepatide | Monthly = $297 (Quarterly = $822; 6 Month = $1494; new-patient JumpStart 3 Month = $599) | published | tirzepatide (GLP-1 + GIP) · subcutaneous injection · quiz→Rx; 503A-compounded, "no additional fees or membership costs" |
| Compounded Semaglutide | buyable | /weight-loss | /products/semaglutide | 1 Month Supply = $199 | published | semaglutide (GLP-1) · injection · quiz→Rx; compounded, "Same Price at Every Dose Level," no membership |
| Microdose GLP-1 | buyable | /weight-loss | /products/microdose-glp-1 | $149 | published | semaglutide *or* tirzepatide · low-dose twice-weekly injection · quiz→Rx; cross-listed under Daily Wellness, no membership |
| Wegovy Pill | buyable | /weight-loss | /products/wegovy-pill | 1.5mg dose: $149/month (4 mg: $199/month; Higher doses: $299/month) + $74 membership | partial | oral GLP-1, "Wegovy pill sourced through Novo Nordisk" (semaglutide not stated verbatim) · oral pill · quiz→Rx; **mandatory $74 platform membership** on top |
| Wegovy | buyable | /weight-loss | /products/wegovy | $499 | published | semaglutide (brand, Novo Nordisk) · injection pen · quiz→Rx; all-in, "No insurance required" |
| Ozempic | buyable | /weight-loss | /products/ozempic | $649 | published | semaglutide (brand; "not FDA-approved for weight loss… prescribed off-label") · pen · quiz→Rx |
| Zepbound | buyable | /weight-loss | /products/zepbound | $1349 | published | tirzepatide (brand, Eli Lilly) · pen · quiz→Rx; FDA-approved for weight loss |
| Mounjaro | buyable | /weight-loss | /products/mounjaro | $1149 | published | tirzepatide (brand, Eli Lilly) · pen · quiz→Rx |
| Daily Wellness | family | — | /daily-wellness | — | — | Injectable longevity + performance shots, flat monthly, no membership |
| NAD+ Injections | buyable | /daily-wellness | /products/nad | $174 | published | NAD+ · injection · quiz→Rx; "boosts cellular health, healthy aging" |
| NAD+ Nasal Spray | buyable | /daily-wellness | /products/nad-nasal-spray | $139 | published | NAD+ · nasal spray (needle-free) · quiz→Rx |
| Sermorelin | buyable | /daily-wellness | /products/sermorelin | $149 | published | sermorelin (synthetic GHRH peptide) · injection · quiz→Rx; "off-label… adult GH deficiency" |
| Glutathione | buyable | /daily-wellness | /products/glutathione | $149 | published | glutathione (antioxidant) · injection · quiz→Rx |
| Slim Shot | buyable | /daily-wellness | /products/slim-shot | $169 | published | Lipo(MIC) + B12 + L-Carnitine · injection · quiz→Rx; "Slim Shot®: Lipo(MIC), B12, L-Carnitine" |
| MIC+B12 | buyable | /daily-wellness | /products/mic-b12 | $129 | published | methionine-inositol-choline + B12 · injection · quiz→Rx |
| Vitamin B12 | buyable | /daily-wellness | /products/vitamin-b12 | $119 | published | vitamin B12 · injection · quiz→Rx |
| Sexual Health | family | — | /sexual-health | — | — | ED + arousal meds for men and women; mostly dose-gated floors |
| Tadalafil (Generic Cialis) | buyable | /sexual-health | /products/tidalafil-generic-cialis | 5mg (30 tablets) = $69; 5mg (90 tablets) = $149; 10mg (30 tablets) = $240; as-needed 10mg = $10 per dose, 20mg = $15 per dose | published | tadalafil (generic Cialis) · oral tablet, daily or as-needed · quiz→Rx; as-needed min order 8 doses |
| Sildenafil (Generic Viagra) | buyable | /sexual-health | /products/generic-viagra | Starting at $5/dose | partial | sildenafil (generic Viagra) · oral tablet · quiz→Rx; floor only, real price dose-gated |
| Cialis | buyable | /sexual-health | /products/cialis | Starting at $15/dose | partial | tadalafil (brand Cialis) · once-daily 5mg tablet · quiz→Rx; floor only |
| Viagra | buyable | /sexual-health | /products/viagra | Starting at $95/dose | partial | sildenafil (brand Viagra) · oral tablet · quiz→Rx; floor only |
| Ignite Strips | buyable | /sexual-health | /products/ignite-strips | Starting at $10/dose | partial | sildenafil + tadalafil + oxytocin · dissolvable oral film · quiz→Rx (men); a benefits blurb says "apomorphine" — see anchors |
| Bliss Strips | buyable | /sexual-health | /products/bliss-strips | Starting at $12/dose | partial | PT-141 / bremelanotide · dissolvable oral film · quiz→Rx (women) |
| ED Mints | buyable | /sexual-health | /ed-mints | — | on-request | tadalafil-/sildenafil-based chewable, multiple formulations · chewable mint · quiz→Rx; no price shown on page |
| Hair | family | — | /hair | — | — | Regrowth for men + women; topical sprays + oral tablets, dose-gated floors |
| Hair Regrowth for Men | buyable | /hair | /products/hair-regrowth-for-men | Starting at $45/month | partial | minoxidil 7% + tretinoin 0.025% + fluocinolone 0.025% + finasteride 0.2% · 3-in-1 topical spray · quiz→Rx |
| Hair Regrowth for Women | buyable | /hair | /products/hair-regrowth-for-women | Starting at $45/month | partial | minoxidil 7% + tretinoin 0.025% + fluocinolone 0.025% + biotin 0.8% + melatonin 0.5% · 3-in-1 topical spray · quiz→Rx (no finasteride) |
| Oral Minoxidil | buyable | /hair | /products/oral-minoxidil | Starting at $30/month | partial | minoxidil · oral tablet · quiz→Rx; off-label, marketed for men + women |
| Finasteride (Generic Propecia) | buyable | /hair | /products/finasteride-generic-propecia | Starting at $20/month | partial | finasteride 1mg · oral tablet · quiz→Rx |

*Not rostered: **Oral Semaglutide** — listed in the weight-loss mega-nav but `/products/oral-semaglutide` returns a thin 404 (no live PDP); a listed-but-unbuilt link, never a priced SKU.*

### Verbatim anchors

- **Tirzepatide pricing tiers** (`/products/tirzepatide`): *"New GL JumpStart Bundle! 3 Month Supply = $599 · Initial 12 Week Supply: 2.5mg → 5mg → 7.5mg… Standard Dose Levels: Monthly = $297 · Quarterly = $822 · 6 Month Supply = $1494."* New-patient bundle is titration-only; the partial token does **not** apply — no separate mandatory cost, so `published`.
- **Wegovy Pill membership** (`/products/wegovy-pill`, the `partial` decider): *"Additional $74 membership fee required which provides access to the Good Life Meds platform, ongoing providers support & prescription management."* — a mandatory cost on top of the $149/$199/$299 dose tiers.
- **Tadalafil as-needed minimum** (`/products/tidalafil-generic-cialis`): *"Quantities for 'as-needed' dosages require a minimum order of 8 doses."* Real per-pack prices shown → `published` despite the "Starting at $3/dose" header.
- **Ignite Strips molecule discrepancy** (`/products/ignite-strips`): product copy twice states *"sildenafil, tadalafil, and oxytocin"* (lines 67, 91); a benefits tile says *"Combines sildenafil, tadalafil, and apomorphine"* (line 128). Roster uses the product-copy molecule; apomorphine is the outlier.
- **SUMMER30 promo** (every Rx PDP): *"30% Off Sitewide… Must use promo code SUMMER30 at checkout."* Captured promo figures (not the rostered standard price): Tirzepatide $208 · Semaglutide $140 · Microdose $105 · NAD+ $122 · Zepbound $1299 · Mounjaro $1099. Prices are a point-in-time snapshot.
- **Molecule-sourcing audit** (the `not stated` cases): **Wegovy Pill** — PDP says "the first FDA-approved oral GLP-1" and "Wegovy pill sourced through Novo Nordisk"; it does **not** print "semaglutide" in product copy (semaglutide is the known Wegovy active, but recorded as brand-attested, not molecule-attested). **ED Mints** — `/ed-mints` lists several formulations (*"Tadalafil + DHEA," "Tadalafil + B vitamins + Oxytocin," "Sildenafil + Tadalafil + Yohimbine + Oxytocin"*) and a *"daily-dose tadalafil with a B-complex blend"* mint; no single molecule and no price.
- **503A compounding disclaimer** (compounded PDPs, verbatim): *"This drug is compounded by a licensed pharmacy in accordance with Section 503A of the Federal Food, Drug & Cosmetic Act… The FDA does not review or approve compounded medications… not affiliated with, endorsed or approved by… Eli Lilly."*

## Deep blocks

Earned only where a roster row can't carry the nuance.

### PDP-template anatomy (portfolio-level — one read teaches the whole catalog)

*Opt-in archetype included for this design/rendering-reference run (see Run profile). Every `/products/*` PDP is the same Webflow shell, so reading one maps all 26:*

```
[trust bar: 100% online · no membership · FDA-regulated pharmacies · transparent pricing · board-certified · US-sourced]
[image gallery — clean product render(s) + chart/testimonial thumbs]   ← hero render lives here
[H1 product name] [price widget: base $ / promo $ / compare $]  [Buy now → app.goodlifemeds.com/start-online-visit/<flow>]
[1-line value prop] · [bullet benefits] · [SUMMER30 promo callout]
### What's Included  (Prescription Medication · Syringes/Pen · Alcohol Pads · Expedited Shipping · Doctor Consultation · Ongoing Doctor Care)
### What is X? · ### Pricing details (tiers OR "Starting at") · [503A/FDA disclaimer]
### Benefits (5 icon tiles) · ### Real Stories (first-name testimonials) · ## Always quality tested (Potency/Sterility/pH/Endotoxicity)
## How it works (01 Questionnaire → 02 Provider Evaluation → 03 Approved & Delivered, 3–5 days)
## Related Products · ## FAQ · footer
```
The price widget is the only structurally variable region: weight-loss/daily-wellness fill a flat monthly tier; sexual-health/hair fill a "Starting at $X" floor.

### Flagship hero renders (captured assets — design reference)

Clean isolated product renders captured for the line flagships (opt-in asset, not a roster column):
- **Compounded Tirzepatide** — olive-green vial → `captures/2026-06-04/images/tirzepatide.png`
- **Compounded Semaglutide** — olive-green vial → `captures/2026-06-04/images/semaglutide.png`
- **NAD+ Injections** — frosted-white vial → `captures/2026-06-04/images/nad.png`
- **Hair Regrowth for Men** — black topical-spray bottle → `captures/2026-06-04/images/hair-regrowth-for-men.png`
- **Ignite Strips** — black single-dose sachet → `captures/2026-06-04/images/ignite-strips.png`

### Wegovy Pill — the one membership-gated SKU

The only catalog SKU with a separate mandatory cost. The dose ladder (1.5mg $149/month → 4mg $199/month → higher $299/month) sits **on top of** a **$74 platform membership** ([anchor](#verbatim-anchors)) — so the shown "$149/month" is never the all-in, hence `partial`. Contrast every other weight-loss SKU, which states "no additional fees or membership costs."

### ED Mints — gated, multi-formulation, no price

`/ed-mints` doubles as the men's sexual-health landing and the ED-Mints PDP. It shows **no price** (only "Medications delivered to your door at an accessible price with no hidden fees") and offers **several chewable formulations** rather than one SKU ([anchor](#verbatim-anchors)) — so molecule is a set (tadalafil/sildenafil + DHEA / B-vitamins / yohimbine / oxytocin), visibility `on-request`.

## Provenance

- **Pages read (cited captures, all `store/goodlifemeds-com/captures/2026-06-04/`):** the 4 category hubs + 27 product PDPs (26 live + the 404 oral-semaglutide stub) + homepage. Prices traced to each PDP's "Pricing details" / header widget; molecules to each PDP's product copy.
- **Scope:** all 26 buyable SKUs enumerated and priced. Microdose GLP-1 cross-listed (Weight Loss + Daily Wellness) is rostered once. Brand-only `/products/cialis` and `/products/viagra` included though absent from the mega-nav. Oral Semaglutide noted, not rostered (dead PDP).
- **Gated/unreachable:** the true all-in price on the 9 `partial` "Starting at" SKUs (sexual-health + hair) is set inside the intake quiz on `app.goodlifemeds.com` — not captured. ED Mints shows no price at all.
- **Snapshot caveat:** prices are point-in-time — a sitewide **SUMMER30** 30%-off promo was active; roster carries standard (pre-promo) figures, promo figures in anchors.
- **Run profile:** non-vanilla — included the opt-in **PDP-template anatomy** block + **flagship hero-render** asset capture (5 renders) for a design/rendering-reference consumer. Standard runs skip both.
