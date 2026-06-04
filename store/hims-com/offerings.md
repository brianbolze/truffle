---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: hims.com            # company key; each offering's slug (its relative url) is its key *within* hims
captured_at: 2026-06-03     # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Hims (Hims & Hers, NYSE: HIMS) is **Multi-product** and **broader than its own "six lines" framing** — this
capture enumerates **seven** co-equal storefronts at SKU grain: **weight loss, sexual health (ED + PE + OTC
sexual wellness), hair loss, testosterone, mental health, labs, and skin care.** Skin care (a full Apostrophe-
powered derm line) and the OTC sexual-wellness shelf (rings, vibrators, condoms, lube) were absent from the
warm `profile.md` and are first surfaced here. Every Rx line sells the same way: a condition *family* gates a
roster of SKUs through an intake quiz (`/g/i/*`, `/c/*`); medication ships on a subscription that **bundles the
consult, shipping, check-ins and messaging** — *except* weight loss, which charges a **separate** membership.

**Visibility rule (stated once, applied to every row).**
- **`published`** — the displayed number is a complete, self-contained price you can actually subscribe at for
  the entry configuration: no mandatory separate fee, no drug bought elsewhere. A *"Starting at $X/mo"* or
  *"from $X/use"* floor still counts as published when that entry tier is itself purchasable (the floor is
  quoted verbatim so a comparison can see it move with dose/quantity).
- **`partial`** — the headline number **excludes a mandatory separate cost** (a membership), or the med is
  bought elsewhere, so the real all-in is materially higher than shown. **Every weight-loss GLP-1 SKU is
  `partial`**: the price is *medication only*, with a **Weight Loss Membership ($39 first month → $149/mo)**
  stacked on top ("Medication is not available without a membership").
- **`on-request`** — **no price on the card/hero**; you must finish intake (± a required lab) to see it, or the
  only figure is buried in FAQ prose. Hits testosterone (enclomiphene `$99/mo` lives *only* in FAQ + is
  lab-gated), the two "Coming in 2026" TRT SKUs, the Rx custom skin creams, the Galleri add-on, and valacyclovir.

So the shape is **two pricing patterns**: weight loss is the one `partial` line (membership wedge); every other
Rx/OTC line is **self-contained `published`** at a per-month or per-use floor, with a handful of lab-/intake-
gated `on-request` exceptions. The headline cheap floors hide real spread — ED runs **$1.63/use (Hard Mints) →
$958/mo (brand Cialis® daily)**; brand Viagra® is **$543/mo**.

**Prominence (calibrated).**
- **Weight loss is the lead line [HIGH]** — the hero ("Lose weight *the way you want*"), every GLP-1 card
  badged **`RxNew`**, the widest lineup (2 molecules, 9 drug SKUs across pill/pen/vial + a meal-replacement),
  and it owns the cross-site "Top Treatments" rail's first three slots (Wegovy Pill, Wegovy Pen, Zepbound
  KwikPen).
- **Company-stamped "Most popular" badges [HIGH] (within-line):** **3-in-1 Hard Mints** (sexual health),
  **Finasteride & Minoxidil + Supplement Chew** (hair), **Sildenafil** (its own PDP).
- **The "Top Treatments" nav rail [MED]** (every page footer): Wegovy Pill · Wegovy Pen · Zepbound KwikPen ·
  Hard Mints · Generic Viagra (Sildenafil) · Viagra® · Finasteride & Minoxidil Spray · Generic Lexapro
  (Escitalopram) — hims's own curated cross-line set. Site "Explore" nav order (WL · Labs · Sexual · Testosterone
  · Hair · Mental · Skin) puts **Labs second [MED]**, a louder push than its 2-SKU depth implies.
- Card order within a grid and the rotating ATF heroes left **[LOW]** — not used for ranking.

**Form column** = the page-attested delivery mechanism mapped to the Notion **Delivery Mechanisms** slug *by
route*: swallowed orals → `pill`, self-injection → `injection`, creams/gels/serums → `topical-gel`. Where the
vocab has **no slug for the page's form**, the page word carries a **`[new?]`** flag — `chewable`, `spray`,
`foam`, `shampoo`, `wipe` are all genuine gaps (DTC men's-health is full of chewables/sprays; the list has only
`sublingual-troche`/`nasal-spray`/`topical-gel`). Non-drug items (labs draws, sex-toy devices, meal replacement)
have **no** delivery mechanism → `not stated`.

**Category column** = the SKU's best-fit Notion **Product Category**, slugified, grounded in hims's own grouping.
`[?]` marks a forced fit: OTC skin "basics" (Notion's *aesthetics-dermatology* explicitly *excludes* OTC beauty),
the meal-replacement (a food in a drug category), and the dandruff shampoo (OTC scalp care shelved under hair).

## Roster

Complete at the indexed level (hims's product cards) across all seven lines, deduped: marketing-URL variants
(`hair-power-pack-shopping-*`, `finasteride-gs-holiday`) collapse to the canonical slug; a SKU shown on several
storefronts is listed once. Price quoted verbatim with its on-page markers; molecule/form page-attested only
(never inferred from a brand name — see the molecule audit under Verbatim anchors). A slug here is never asserted
equal to another brand's.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | Form | Category | What (molecule · access) |
|---|---|---|---|---|---|---|---|---|
| **Weight Loss** | family | — | `/weight-loss` | — | — | — | — | GLP-1 line; "holistic program" gating a SKU roster behind a separate membership. |
| Weight Loss Membership | buyable | Weight Loss | `/weight-loss/membership` | `$39 for the first month, auto-renews at $149/month thereafter` | published | not stated | glp-1-medical-weight-loss | — · the recurring fee that gates every WL SKU; billed separately from medication. |
| Wegovy® Pill | buyable | Weight Loss | `/weight-loss/wegovy-pill` | `From $149/mo†` | partial | pill | glp-1-medical-weight-loss | semaglutide · oral, once-daily · membership-gated; med-only price. |
| Wegovy® Pen | buyable | Weight Loss | `/weight-loss/wegovy-pen` | `From $199/mo†` | partial | injection | glp-1-medical-weight-loss | semaglutide · once-weekly inj., doses 0.25–7.2mg · membership-gated; FSA/HSA eligible. |
| Zepbound® Vial | buyable | Weight Loss | `/weight-loss/zepbound-vial` | `From $299/mo†` | partial | injection | glp-1-medical-weight-loss | tirzepatide · once-weekly inj. (vial) · membership-gated; med-only price. |
| Zepbound® KwikPen® | buyable | Weight Loss | `/weight-loss/zepbound-kwikpen` | `From $299/mo†` | partial | injection | glp-1-medical-weight-loss | tirzepatide · once-weekly pre-filled pen · membership-gated; now its own PDP. |
| Foundayo™ Pill | buyable | Weight Loss | `/weight-loss/foundayo-pill` | `From $149/mo†` | partial | pill | glp-1-medical-weight-loss | orforglipron · oral, once-daily · membership-gated; "no rules around food, water, timing." |
| Ozempic® Pill | buyable | Weight Loss | `/weight-loss/ozempic-pill` | `From $149/mo†` | partial | pill | glp-1-medical-weight-loss | semaglutide · oral · membership-gated; FDA-approved T2D, off-label weight loss. |
| Ozempic® (injection) | buyable | Weight Loss | `/weight-loss/ozempic-pen` | `From $199/mo†` | partial | injection | glp-1-medical-weight-loss | semaglutide · weekly inj. · membership-gated; off-label weight loss. |
| Mounjaro® | buyable | Weight Loss | (no PDP — category modal) | `$1,899/mo†` / `$1,899/mo*` | partial | injection | glp-1-medical-weight-loss | not stated · weekly inj. · membership-gated; full-price brand card, "a weekly GLP-1 injection." |
| Zepbound® (brand entry) | buyable | Weight Loss | (no PDP — category modal) | `$1,899/mo†` / `$1,899/mo*` | partial | injection | glp-1-medical-weight-loss | tirzepatide · weekly inj. · membership-gated; full-price brand card, distinct from the $299 Vial/KwikPen. |
| Meal Replacements | buyable | Weight Loss | `/weight-loss/meal-replacement` | `Starting at $110/mo*` | published | not stated | glp-1-medical-weight-loss [?] | not stated · shakes (chocolate/vanilla) + bars · non-Rx food adjunct; [?] food in a drug category. |
| **Sexual Health** | family | — | `/sexual-health` | — | — | — | — | ED + premature-ejaculation Rx + an OTC sexual-wellness shelf; self-contained subs (no membership). |
| Generic for Viagra® (Sildenafil) | buyable | Sexual Health | `/erectile-dysfunction/sildenafil` | `Starting at $22/mo` / `From $4 per use` | published | pill | ed | sildenafil · as-needed PDE5i · "Most popular"; dose 25/50/100mg, "5% of the cost" of Viagra®. |
| Viagra® (brand) | buyable | Sexual Health | `/erectile-dysfunction/viagra` | `Starting at $543/mo` / `From $135 per use` | published | pill | ed | sildenafil · as-needed · FDA-approved brand ("the little blue pill"). |
| Generic for Cialis® (Tadalafil) | buyable | Sexual Health | `/erectile-dysfunction/tadalafil` | `Starting at $24/mo` / daily `From $40 per month` | published | pill | ed | tadalafil · as-needed or daily PDE5i. |
| Cialis® (brand) | buyable | Sexual Health | `/erectile-dysfunction/cialis` | `$958 per month` | published | pill | ed | tadalafil · daily · FDA-approved brand. |
| 3-in-1 Hard Mints™ | buyable | Sexual Health | `/erectile-dysfunction/hard-mint-chewable` | `Starting at $30/mo` / `From $1.63 per use` | published | chewable [new?] | ed | sildenafil + tadalafil + vitamin B12 · as-needed mint · "Most popular." |
| Sildenafil Chews | buyable | Sexual Health | `/erectile-dysfunction/sildenafil-chew` | `Starting at $30/mo` | published | chewable [new?] | ed | sildenafil · as-needed berry chew. |
| Tadalafil Chews | buyable | Sexual Health | `/erectile-dysfunction/tadalafil-chew` | `Starting at $30/mo` | published | chewable [new?] | ed | tadalafil · as-needed lemon chew. |
| 3-in-1 Pill | buyable | Sexual Health | (no PDP — ED storefront card) | `Starting at $39/mo` | published | pill | ed | sildenafil + tadalafil · as-needed multi-benefit pill. |
| Sex Rx + Hair Health | buyable | Sexual Health | (no PDP — ED storefront card) | `Starting at $39/mo` | published | pill | ed | not stated · daily 2-in-1 (ED + finasteride for hair). |
| Sex Rx + Testosterone Support | buyable | Sexual Health | (no PDP — ED storefront card) | `Starting at $39/mo` | published | pill | ed | not stated · daily 2-in-1 (ED + T support). |
| Sex Rx + Multivitamin | buyable | Sexual Health | (no PDP — ED storefront card) | `Starting at $39/mo` | published | pill | ed | not stated · daily (ED + multivitamin). |
| Sex Rx + Climax Control | buyable | Sexual Health | (no PDP — ED/PE card) | `Starting at $39/mo` / `from $39/month` | published | pill | ed | tadalafil + fluoxetine · daily (ED + PE control). |
| Sex Rx + Vitality Pro | buyable | Sexual Health | (no PDP — ED storefront card) | `Starting at $39/mo` | published | pill | ed | not stated · daily 2-in-1 (ED + cholesterol support). |
| Sertraline for PE | buyable | Sexual Health | `/premature-ejaculation/sertraline-for-pe` | (no price on page — line floor `from $39/month`) | on-request | pill | ed | sertraline · daily, off-label for PE. |
| Sildenafil for PE | buyable | Sexual Health | `/premature-ejaculation/sildenafil-for-pe` | `from $4/use` | published | pill | ed | sildenafil · as-needed, off-label PE endurance. |
| Tadalafil for PE | buyable | Sexual Health | (no PDP — PE storefront card) | `from $6/use` | published | pill | ed | tadalafil · as-needed, off-label PE endurance. |
| Clockstopper Climax Delay Wipes | buyable | Sexual Health | `/premature-ejaculation/benzocaine-wipes` | `from $19/use` / `Starting at $19/mo` | published | wipe [new?] | ed | benzocaine · topical anesthetic wipe (off-label PE). |
| Climax Control Condoms | buyable | Sexual Health | `/premature-ejaculation/climax-control-condoms` | (price not shown on captured pages) | on-request | not stated | other | — · device, climax-control condoms. |
| Standing O Penis Rings | buyable | Sexual Health | `/sexual-health/penis-rings` | `$30` | published | not stated | other | — · OTC device. |
| Thrill Ride Prostate Massager | buyable | Sexual Health | `/sexual-health/prostate-massager` | `$74` | published | not stated | other | — · OTC device. |
| OMG Ring Vibrator | buyable | Sexual Health | `/sexual-health/male-vibrator` | `$74` | published | not stated | other | — · OTC device. |
| Condoms & Lube Kit | buyable | Sexual Health | `/sexual-health/sex-kit` | `$35` | published | not stated | other | — · OTC accessory kit. |
| Ultra Thin Condoms | buyable | Sexual Health | `/sexual-health/ultra-thin-condoms` | `$35 / 12 Pack` | published | not stated | other | — · OTC accessory. |
| Glide Water-based Lube | buyable | Sexual Health | `/sexual-health/water-based-lube` | `$15` | published | not stated | other | — · OTC accessory. |
| Valacyclovir | buyable | Sexual Health | `/sexual-health/valacyclovir` | (no price on page) | on-request | pill | other | valacyclovir · oral antiviral, genital herpes (also a cold-sore PDP at `/skin-care/valacyclovir`). |
| **Hair Loss** | family | — | `/hair-loss` | — | — | — | — | "Hair Hybrids" — finasteride/minoxidil singles + multi-active sprays/serums/chews; published subs, no membership. |
| Finasteride & Minoxidil + Supplement Blend Pill | buyable | Hair Loss | `/hair-loss/finasteride-minoxidil-supplement-pill` | `Starting at $29 per month` | published | pill | hair-loss | finasteride + minoxidil + supplement blend · oral · badge "New." |
| Finasteride & Minoxidil + Supplement Blend Chew | buyable | Hair Loss | `/hair-loss/finasteride-minox-chew-week` | `Starting at $29 per month` | published | chewable [new?] | hair-loss | finasteride + minoxidil + supplements · 3-in-1 citrus chew · "Most popular." |
| Rx Hair Loss Spray (Finasteride & Minoxidil) | buyable | Hair Loss | `/hair-loss/topical-finasteride` | `Starting at $29 per month` | published | spray [new?] | hair-loss | finasteride + minoxidil · once-daily quick-dry spray. |
| Rx Hair Loss Spray + Ketoconazole + Biotin | buyable | Hair Loss | `/hair-loss/hair-loss-spray` | `Starting at $33 per month` | published | spray [new?] | hair-loss | finasteride + minoxidil + ketoconazole + biotin · spray. |
| Rx Hair Loss Serum | buyable | Hair Loss | `/hair-loss/serum` | `Starting at $29 per month` | published | topical-gel | hair-loss | finasteride + minoxidil · once-daily dropper serum. |
| Minoxidil + Supplement Blend Chew | buyable | Hair Loss | `/hair-loss/minox-chew` | `Starting at $29 per month` | published | chewable [new?] | hair-loss | minoxidil + supplements · once-daily orange chew. |
| Finasteride | buyable | Hair Loss | `/hair-loss/finasteride` | `Starting at $22 per month` | published | pill | hair-loss | finasteride · oral, FDA-approved (generic Propecia®). |
| Hair Power Pack | buyable | Hair Loss | `/hair-loss/hair-power-pack` | `Starting at $60 per month` | published | pill | hair-loss | finasteride + minoxidil (kit) · "complete hair growth routine." |
| Minoxidil Foam | buyable | Hair Loss | `/hair-loss/minoxidil-foam` | `Starting at $19 per month` | published | foam [new?] | hair-loss | minoxidil · OTC topical foam. |
| Minoxidil Serum | buyable | Hair Loss | `/hair-loss/minoxidil` | `Starting at $15 per month` | published | topical-gel | hair-loss | minoxidil · OTC topical solution/serum, FDA-approved. |
| Dandruff Detox Shampoo | buyable | Hair Loss | `/hair-loss/zinc-pyrithione-shampoo` | `Starting at $18 per month` | published | shampoo [new?] | hair-loss [?] | zinc pyrithione · OTC anti-dandruff; [?] OTC scalp care shelved under hair. |
| **Testosterone** | family | — | `/testosterone` | — | — | — | — | "Testosterone Rx+" (enclomiphene, *not* synthetic TRT) live now; real TRT "Coming in 2026." |
| Testosterone Rx+ (enclomiphene + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-supplements` | none on page; FAQ `starts at $99/month for a 10-month plan paid upfront and in full` | on-request | pill | fertility-preserving-hormone-optimization | enclomiphene + supplements (zinc, B6, B12, L-arginine) · oral, daily · lab + intake gated. |
| Testosterone Rx+ (enclomiphene + tadalafil + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil-supplements` | none on page; FAQ `$99/month for a 10-month plan paid upfront and in full` | on-request | pill | fertility-preserving-hormone-optimization | enclomiphene + tadalafil + supplements · oral, daily · the marquee card; lab + intake gated. |
| Injectable TRT | buyable (roadmap) | Testosterone | (no PDP — category card) | `Coming in 2026*` | on-request | injection | trt | testosterone cypionate · once-weekly inj. · FDA-approved; not yet offered. |
| Oral TRT | buyable (roadmap) | Testosterone | (no PDP — category card) | `Coming in 2026*` | on-request | pill | trt | testosterone undecanoate (Kyzatrex®) · twice-daily oral · FDA-approved; not yet offered. |
| **Mental Health** | family | — | `/mental-health` | — | — | — | — | Async psychiatry for anxiety/depression; SSRIs/SNRIs + adjuncts, line floor `from $49/mo`. No controlled substances. |
| Sertraline | buyable | Mental Health | `/psychiatry/sertraline` | `Starting at $49/mo` | published | pill | mental-health | sertraline · oral (generic Zoloft®). |
| Escitalopram | buyable | Mental Health | `/psychiatry/escitalopram` | line floor `from $49/mo` | published | pill | mental-health | escitalopram · oral (generic Lexapro®). |
| Citalopram | buyable | Mental Health | `/psychiatry/citalopram` | line floor `from $49/mo` | published | pill | mental-health | citalopram · oral (generic Celexa®). |
| Fluoxetine | buyable | Mental Health | `/psychiatry/fluoxetine` | line floor `from $49/mo` | published | pill | mental-health | fluoxetine · oral (generic Prozac®). |
| Duloxetine | buyable | Mental Health | `/psychiatry/duloxetine` | line floor `from $49/mo` | published | pill | mental-health | duloxetine · oral (generic Cymbalta®). |
| Venlafaxine | buyable | Mental Health | `/psychiatry/venlafaxine` | line floor `from $49/mo` | published | pill | mental-health | venlafaxine · oral (generic Effexor®). |
| Bupropion XL | buyable | Mental Health | `/psychiatry/bupropion` | line floor `from $49/mo` | published | pill | mental-health | bupropion · oral (generic Wellbutrin XL®). |
| Buspirone HCl | buyable | Mental Health | `/psychiatry/buspirone` | line floor `from $49/mo` | published | pill | mental-health | buspirone · oral (generic Buspar®). |
| Propranolol | buyable | Mental Health | `/psychiatry/propranolol` | line floor `from $49/mo` | published | pill | mental-health | propranolol · oral beta-blocker (off-label performance anxiety). |
| **Labs** | family | — | `/labs` | — | — | — | — | At-home blood testing via Quest + a doctor-built "Action Plan"; Galleri cancer add-on. |
| Labs by Hims (biomarker panel) | buyable | Labs | `/labs/biomarkers` | `~~$499~~ $349 per year` ("less than $1/day") | published | not stated | labs-diagnostics | not stated · 130+ biomarkers / "1,000+ conditions" across 10 areas; Quest blood draw + Action Plan. |
| Hims Multi-Cancer Test by Galleri® | buyable | Labs | `/labs/cancer-test` | (no price — "add it to your Labs plan") | on-request | not stated | labs-diagnostics | not stated · annual MCED blood screen, 50+ cancer types; add-on to the Labs plan. |
| **Skin Care** | family | — | `/skin-care` | — | — | — | — | Men's derm in partnership with Apostrophe — Rx custom creams (gated) + OTC basics (published). |
| Custom Anti-Aging Cream | buyable | Skin Care | `/skin-care/anti-aging` | (no price — "Prescription," intake-gated) | on-request | topical-gel | aesthetics-dermatology | tretinoin + azelaic acid + niacinamide · custom Rx cream. |
| Custom Acne Cream | buyable | Skin Care | `/skin-care/acne-treatment` | (no price — "Prescription," intake-gated) | on-request | topical-gel | aesthetics-dermatology | tretinoin / clindamycin / niacinamide / azelaic acid / zinc pyrithione (custom mix) · Rx cream. |
| Goodnight Wrinkle Cream | buyable | Skin Care | `/skin-care/night-cream-men` | `$24` | published | topical-gel | aesthetics-dermatology [?] | not stated · OTC night cream; [?] Notion aesthetics-derm excludes OTC beauty. |
| High Tide Cleanser | buyable | Skin Care | `/skin-care/face-cleanser-men` | `$15` | published | topical-gel | aesthetics-dermatology [?] | not stated · OTC face cleanser; [?] OTC beauty. |
| Everyday Moisturizer | buyable | Skin Care | `/skin-care/moisturizer-men` | `$18` | published | topical-gel | aesthetics-dermatology [?] | not stated · OTC moisturizer; [?] OTC beauty. |
| Vitamin C Serum | buyable | Skin Care | `/skin-care/vitamin-c-serum-men` | `$33` | published | topical-gel | aesthetics-dermatology [?] | vitamin C · OTC serum; [?] OTC beauty. |

### Verbatim anchors

The footnotes the Price column points at — what decides `partial`/`published`/`on-request`, plus the molecule
and form audit. Quoted exactly from the captured pages.

- **† (weight-loss membership):** *"Price includes medication only, if prescribed. An active Hims Weight Loss
  Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is billed
  separately and does not include or guarantee a prescription. Medication is not available without a membership.
  Membership fee is not included."* (`weight-loss-category` + every WL PDP) → the WL number is real but med-only;
  all-in = membership + medication, hence **`partial`** for all WL SKUs.
- **\* (Mounjaro / generic Zepbound $1,899):** the same membership footnote keyed to `*` on the "Our brands"
  modals (`weight-loss-category`).
- **\* (Meal Replacements $110):** *"Starting at $110/mo"* with a `*` (`weight-loss-meal-replacement`); a non-Rx
  food, self-contained → `published`, but `[?]` on category (a food in a drug-defined vertical).
- **\* (testosterone "Coming in 2026"):** *"Such expected launch is subject to certain assumptions and factors,
  some of which may be outside of our control, and as such may be subject to change."* (`testosterone-category`).
- **Testosterone $99 is FAQ-only + lab-gated → `on-request`:** the only figure on the entire line is in FAQ prose
  — *"Pricing for low testosterone treatment with enclomiphene through Hims starts at $99/month for a 10-month
  plan paid upfront and in full"* — no price on any card/hero, and the path is gated behind intake **plus** a
  required at-home lab. And it is **not synthetic TRT**: enclomiphene works on the body's own T production ("no
  synthetic testosterone needed"); hims's real injectable TRT (cypionate) is "Coming in 2026," not buyable today.
- **ED self-contained → `published`:** *"What's included in my subscription: ED medication, Free shipping, Free
  assessment by a licensed medical provider, Periodic check-ins, Unlimited messaging, App"* (`ed-category`,
  `sexual-health-category`, `pe-category` FAQs) — no separate membership, so the per-mo/per-use floor is the real
  entry price. *"Treatments start as low as $2/dose"* / *"less than $2/chew."*
- **The ED price spread (verbatim, all in `ed-sildenafil`/`ed-cialis` cross-sell):** Hard Mints *"From $1.63 per
  use"* · Generic Viagra *"From $4 per use"* · brand Viagra *"From $135 per use"* (and *"Starting at $543/mo"* on
  `sexual-health-category`) · daily generic Tadalafil *"From $40 per month"* · **brand Cialis daily *"$958 per
  month."*** Same molecule, wildly different prices — kept verbatim, never normalized.
- **Labs is `published`:** *"Check for signals of 1,000+ conditions for just ~~$499~~ $349 per year"* /
  *"in-depth lab testing for less than $1/day"* (`labs-biomarkers`). Galleri carries **no** on-page price —
  *"You'll be able to add the Hims Multi-Cancer Test by Galleri® onto your Labs by Hims plan"* → `on-request`.
- **Psychiatry line floor:** *"Clinically proven psychiatry medications from $49/mo"* (`mental-health-category`)
  and on the SKU PDP *"Starting at $49/mo"* (`psychiatry-sertraline`). No per-drug card prices; the $49/mo floor
  is line-wide and self-contained → `published`. *"Controlled substances such as Xanax and Adderall are not
  available."*
- **Molecule sourcing (page-attested-only, audited):** Wegovy Pen → **semaglutide** (*"Wegovy® Pen with
  semaglutide"*, *"Contains semaglutide… also in Ozempic®"*). Zepbound (vial/kwikpen/brand) → **tirzepatide**
  (attested on `weight-loss-zepbound-vial`: *"Both contain tirzepatide"*). Ozempic → **semaglutide**. Foundayo →
  **orforglipron** (`weight-loss-foundayo-pill`). **Mounjaro → "not stated"** (no captured page names its
  molecule — only *"a weekly GLP-1 injection"*; recorded "not stated", not inferred from the brand). Hard Mints →
  **sildenafil + tadalafil + B12** (*"Sildenafil and Tadalafil — plus Vitamin B12… in a 3-in-1 mint"*). Cialis →
  **tadalafil** (*"Cialis® is the brand name of… tadalafil"*). Injectable TRT → **testosterone cypionate**, Oral
  TRT → **testosterone undecanoate (Kyzatrex®)** (both attested on the testosterone cards). The four bundle SKUs
  whose cards don't name a molecule (Sex Rx + Hair Health / Testosterone Support / Multivitamin / Vitality Pro)
  are **"not stated"** — only Sex Rx + Climax Control is attested (*"Tadalafil and Fluoxetine"*).
- **`[new?]` form gaps:** the Delivery Mechanisms vocab has no slug for **chewable/ODT** (Hard Mints, the
  sildenafil/tadalafil chews, the hair chews), **topical spray** (the two Rx Hair Loss Sprays), **foam**
  (Minoxidil Foam), **shampoo** (Dandruff Detox), or **wipe** (Clockstopper benzocaine wipes). All five are
  common in DTC men's health — a real vocab gap, flagged rather than force-fit to `topical-gel`/`pill`.
- **`[?]` category forces:** `meal-replacement` (food → glp-1 vertical), `dandruff-shampoo` (OTC scalp → hair),
  and the four OTC skin basics (Notion *aesthetics-dermatology* is defined as Rx skincare, *"distinct from
  over-the-counter beauty products"* — so cleanser/moisturizer/wrinkle-cream/vit-C don't cleanly fit any category).

## Deep blocks

Three earned blocks span the brand's three structural PDP shapes — a **membership-gated GLP-1 injection**
(flagship, `partial`), a **self-contained ED oral** (`published`, the original franchise), and a **diagnostic
panel** (`published`, no drug at all). They teach how a hims PDP is laid out; the rest of the lineup answers from
the roster.

### Wegovy® Pen — the flagship, membership-gated GLP-1 (`/weight-loss/wegovy-pen`)

- **Parent:** Weight Loss · **price:** `From $199/mo†` (med-only) · **visibility:** `partial` · **form:** injection

Page anatomy in order — **hero carousel → H1 + molecule subhead → benefit bullets → "About the ingredients" →
"How to take" → benefit grid → "How it works" (the membership reveal) → ISI/footnotes.**

> **H1:** "Wegovy® Pen"  ·  **subhead:** "with semaglutide"
> **Hero badges:** "High dose available" · "FSA & HSA eligible"
> **Bullets:** "An FDA-approved GLP-1 injection" · "Clinically proven to help people lose 35 lbs in one year, on
> average" · "Range of dosages from 0.25mg–7.2mg"
> **About the ingredients (verbatim):** "Contains semaglutide, a clinically-proven ingredient that's also in
> Ozempic®… Semaglutide mimics a naturally-occurring hormone in the body (GLP-1) released after eating to signal
> fullness."
> **How to take:** "Inject once weekly, same day each week… Inject under the skin (stomach, thigh, or upper arm)."
> **The membership reveal (verbatim, step 1 of "How it works"):** "Join the Hims Weight Loss Membership for only
> $39 in your first month, then $149/mo after that."

**Why it earns a block:** the `$199/mo†` on the card is *medication only* — the load-bearing fact is buried two
sections down in "How it works," where the **separate** $39→$149/mo membership appears. A roster cell flags
`partial`; the block shows *where* the all-in actually lives, which is exactly the misattribution a cross-brand
GLP-1 comparison must recover. Molecule is page-attested (semaglutide), not inferred.

### Sildenafil — the original franchise, self-contained ED oral (`/erectile-dysfunction/sildenafil`)

- **Parent:** Sexual Health · **price:** `Starting at $22/mo` / `From $4 per use` · **visibility:** `published` · **form:** pill

Page anatomy — **"Most popular" badge → H1 + "Generic for Viagra®" → value pitch → "Meet sildenafil" specs →
how-to/side-effects → price disclaimer → "Why sildenafil?" → FAQ → cross-sell rail.**

> **Badge:** "Most popular"  ·  **H1:** "Sildenafil" / "Generic for Viagra®"
> **Pitch (verbatim):** "sildenafil has the same active ingredient as Viagra® at 5% of the cost. Better sex at a
> lower price—what's not to love?"
> **Specs:** "Flexible dosage options (25mg, 50mg, or 100mg)" · "Sildenafil is an as-needed ED treatment."
> **Pricing mechanic (verbatim):** "Actual price to customer will depend on product and subscription plan
> purchased." And in FAQ: "generally costs anywhere from about $4 to $10 per dose, compared to $50 to $70 per
> dose for brand-name Viagra®."
> **Mechanism:** "Oral ED medications work by suppressing an enzyme in the body called PDE5… blood is able to
> flow more freely."

**Why it earns a block:** it shows hims's *published* pattern — a per-use floor (`$4/use` → `$22/mo`) that is
self-contained (no membership; the subscription bundles consult/shipping/messaging) but **moves with dose**
(25–100mg) and plan, which is why the price cell quotes both the per-mo and per-use floors verbatim. The cross-
sell rail on this same page is also where the brand prices surface (Cialis daily **$958/mo**, Viagra **$135/use**)
— the spread the roster's per-row floors would otherwise hide.

### Labs by Hims — the diagnostic panel, a drug-less `published` SKU (`/labs/biomarkers`)

- **Parent:** Labs · **price:** `~~$499~~ $349 per year` · **visibility:** `published` · **form:** not stated (a blood draw)

Page anatomy — **value hero (price) → 10 "vital area" accordions, each listing its biomarkers with a "Learn more
about <marker>" leaf link → Action Plan → Galleri upsell.**

> **Hero (verbatim):** "Get in-depth lab testing for less than $1/day →" · "Check for signals of 1,000+
> conditions for just ~~$499~~ $349 per year."
> **The 10 areas:** Heart Health · Metabolic Health · Hormone Health · Inflammation & Stress · Thyroid Health ·
> Kidney Health · Liver Health · Immune Defense · Nutrients · (+ the cancer add-on). Each expands to its markers
> (e.g. Hormone Health → Total/Free Testosterone, LH, FSH, SHBG, Estradiol, PSA, IGF-1).
> **Galleri upsell (verbatim):** "You'll be able to add the Hims Multi-Cancer Test by Galleri® onto your Labs by
> Hims plan after answering a few questions… book your blood draw appointment at a Quest Diagnostics location."

**Why it earns a block:** it's the structural outlier — **no molecule, no delivery mechanism, no Rx gating**, and
the *only* line whose price is a flat annual number (`$349/yr`, struck from `$499`) rather than a per-mo floor.
The 70+ `/labs/biomarkers/<marker>` leaf pages are **sub-indexed content, not SKUs** — the indexed level is the
one panel + the Galleri add-on, which is why the roster carries two rows, not seventy. It also anchors why Labs
sits second in the site's "Explore" nav despite its thin SKU count — a deliberate push.

## Provenance

- **Sources reconciled (this run, all `captures/2026-06-03/`, 19 fresh scrapes + maps):**
  - **Census/backbone:** `robots.txt` → single `sitemap.xml`; Firecrawl `/v2/map` no-search census (163 URLs,
    blog-dominated) + **12 `site:hims.com/<path>` map passes** (hair-loss, erectile-dysfunction,
    premature-ejaculation, sexual-health, mental-health, psychiatry, labs, weight-loss, testosterone, skin,
    anxiety, depression) — these surfaced the PDPs the grids hide and the **skin-care** + **sexual-wellness
    device** lines absent from `profile.md`. Direct CMS backends (`/products.json`, `/wp-json`) **don't exist** —
    hims is a custom React SPA; the sitemap-fed `/map` is the only backend census, and it 403s to plain curl.
  - **Category/index pages (10, `--homepage` for prominence + card grids):** weight-loss, testosterone,
    hair-loss, ed (erectile-dysfunction), pe (premature-ejaculation), sexual-health, mental-health, psychiatry,
    labs, skin-care.
  - **Deep PDPs (9):** ed-sildenafil, ed-cialis, pe-sertraline, labs-biomarkers, labs-cancer-test,
    weight-loss-meal-replacement, valacyclovir, psychiatry-sertraline, hair-loss-finasteride — plus the four
    tournament WL PDPs reused (wegovy-pill/pen, zepbound-vial, foundayo-pill) and the two enclomiphene PDPs.
  - **Verify:** `fc.py verify` — all 19 sourceURLs match, all bodies md5-unique (no §5.1 geo/cache contamination).
- **Completeness verdict — HIGH confidence the roster is complete at the indexed level.** Every category grid
  was captured with its rendered cards, and each `site:` map pass cross-checked for unlinked PDPs; the two agree.
  ~75 rows across 7 lines. The residual risk is *marketing-funnel slugs* (`/hair-loss/non-prescription-hair-kit`,
  `/erectile-dysfunction/chewable-ed-meds` roll-up, `/hair-loss/finasteride-gs-holiday`) that are A/B/landing
  variants, not distinct catalog SKUs — collapsed to canonical slugs, not enumerated separately.
- **Couldn't reach / not enumerated:** all-in weight-loss cost (med + membership + dose titration); per-drug
  psychiatry prices (only the `$49/mo` line floor is public); per-SKU prices for the six "Sex Rx +" bundles and
  3-in-1 Pill (only the `$39/mo` floor, no standalone PDP captured); Climax Control Condoms + valacyclovir +
  the two Rx skin creams + Galleri (all `on-request`, price behind intake); the 70+ `/labs/biomarkers/*` leaf
  pages (sub-indexed content, intentionally not SKUs); brand-Cialis/Viagra "per use" vs "per month" units kept
  verbatim, not reconciled.
- **Credit spend:** `fc.py spend` = **20** (1 census map + 19 scrapes, manifest-attributed). Add **~12** for the
  `site:` map passes (run via direct `/v2/map`, billed but outside the manifest) and **up to ~9** likely billed
  by an aborted `fc.py map` batch (a `--search` containing `/` crashed the payload-filename step *after* the API
  call — unattributable, shared-key, so counted as a ceiling). **Run total ≈ 32–41 Firecrawl credits**, ~9
  uncertain. *(Note: `fc.py map` mis-handles a slash in `--search`; the `site:` passes were done via the raw map
  API to avoid it — worth a one-line fix to the script.)*
- **[new?] / [?] flags raised** (for the Notion vocab owners): **Form `[new?]`** — `chewable`, `spray`, `foam`,
  `shampoo`, `wipe` (Delivery Mechanisms has none of these). **Category `[?]`** — `meal-replacement`,
  `dandruff-shampoo`, and the four OTC skin basics (no clean Product Category; aesthetics-dermatology is Rx-only
  by definition).
- **Point-in-time snapshot, not fixed:** hims runs promo + A/B pricing (struck-through `$499→$349` labs, "for a
  limited time" WL heroes, reCAPTCHA/Stripe/Transcend instrumentation in the markdown). This module's own
  `captured_at` + a short TTL are the guard — re-capture before trusting a price as current.
