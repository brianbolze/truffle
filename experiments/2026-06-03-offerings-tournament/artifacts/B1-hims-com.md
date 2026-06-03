<!-- design: B1 roster-first offerings.md (incumbent 2026-06-01) | company: hims.com | portfolio_shape: Multi-product -->
<!-- scope: GLP-1 (weight-loss) + TRT (testosterone) lines only. Sexual-health / hair-loss / mental-health / labs noted but not enumerated — no captures for them in this tournament. -->
<!-- key = page slug WITHIN hims.com. No cross-company canonical key. price_visibility per-offering. -->

# Hims — Offerings (GLP-1 + Testosterone)

Captured 2026-06-03 from hims.com's own pages (weight-loss + testosterone category pages, 4 weight-loss PDPs, 2 testosterone PDPs). Prices are quoted verbatim with their on-page footnotes. Within-company key is the **page slug**; an offering here is never asserted equal to a same-molecule offering at another brand.

## Portfolio overview

Hims is **Multi-product** — six co-equal condition lines (weight loss, sexual health, hair loss, testosterone, mental health, labs). This doc covers the two captured for the tournament: **weight loss (GLP-1)** and **testosterone (TRT)**. Both are sold the same way: a condition *family* gates a roster of buyable medication SKUs, each reached through an intake quiz, all wrapped in a recurring membership/plan.

The breadth-first hierarchy is two real levels plus a pricing wrapper:

```
Weight Loss  (family — /weight-loss)
└─ Weight Loss Membership  (the recurring fee that gates every SKU: $39 first month → $149/mo)
   ├─ Wegovy® Pill            semaglutide, oral daily      /weight-loss/wegovy-pill
   ├─ Wegovy® Pen             semaglutide, weekly inj      /weight-loss/wegovy-pen
   ├─ Zepbound® Vial          tirzepatide, weekly inj      /weight-loss/zepbound-vial
   ├─ Zepbound® KwikPen®      tirzepatide, weekly inj      /weight-loss/zepbound-kwikpen
   ├─ Foundayo™ Pill          orforglipron, oral daily     /weight-loss/foundayo-pill
   ├─ Ozempic® Pill           semaglutide, oral            /weight-loss/ozempic-pill
   ├─ Ozempic® (injection)    semaglutide, weekly inj      (no PDP — category card/modal)
   ├─ Mounjaro®               tirzepatide, weekly inj      (no PDP — category modal)
   └─ Zepbound® (generic)     tirzepatide                  (no PDP — category card/modal)

Testosterone  (family — /testosterone, "Testosterone Rx" / "Testosterone Rx+")
   ├─ Testosterone Rx+  (enclomiphene + supplements)            /testosterone/enclomiphene-supplements
   ├─ Testosterone Rx+  (enclomiphene + tadalafil + supplements) /testosterone/enclomiphene-tadalafil-supplements
   ├─ Enclomiphene                                              /testosterone/enclomiphene          (linked, not captured)
   ├─ Enclomiphene & Tadalafil                                  /testosterone/enclomiphene-tadalafil (linked, not captured)
   ├─ Testosterone cypionate (injection)   — "Coming in 2026*"  (roadmap, no PDP)
   └─ Kyzatrex® (testosterone undecanoate, oral) — "Coming in 2026*"  (roadmap, no PDP)
```

**Two pricing patterns, two visibility tokens.**
- **Weight-loss SKUs are `[partial]`.** A number always shows ("From $149/mo"), but it is *medication only* and a separate, mandatory **Weight Loss Membership** ($39 first month, then $149/mo) is billed on top — "Medication is not available without a membership." The advertised price is real but is never the all-in cost.
- **Testosterone SKUs are `[on-request]`.** No price appears on the product cards or PDP heroes at all; the only figure on the whole line — "starts at $99/month for a 10-month plan paid upfront and in full" — is buried in FAQ prose, and the buy path is gated behind an intake **plus** a required at-home lab test. The two "Coming in 2026" injectables aren't buyable yet.

**How the lines relate.** Weight loss is the hero (homepage banner: "The GLP-1 pill is here"), spanning FDA-approved branded GLP-1s across both molecules (semaglutide, tirzepatide) and the new oral orforglipron, in pill/pen/vial forms. Testosterone is a newer line built on compounded enclomiphene (explicitly *not* synthetic TRT — "no synthetic testosterone needed"), leaning on the same at-home-labs wedge that also feeds the wider Labs line. Both run on the membership/subscription model the parent (Hims & Hers, NYSE: HIMS) is built on.

---

## Deep blocks — flagship / most-compared offerings

The five most-compared SKUs: the three weight-loss heroes carried in the site's own comparison tables (Wegovy Pill, Wegovy Pen, Zepbound Vial), plus Foundayo (the new orforglipron pill the homepage banner leads with), plus the testosterone flagship (Testosterone Rx+).

### Wegovy® Pill — semaglutide, oral

- **Parent:** Weight Loss · **url:** `/weight-loss/wegovy-pill` · **price:** From $149/mo† (medication only) · **price_visibility:** `[partial]`

> **H1:** "Wegovy® Pill"
> Sub-bullets: "Wegovy® is an FDA-approved semaglutide pill for weight loss" · "Clinically proven to help people lose 32 lbs in one year, on average*"

Exact price string (PDP comparison table): "Starts at **_$149/mo_** / billed monthly, / membership required\*" — "Taken **_Once daily_**", "Semaglutide active ingredient", "FDA approved for weight loss". Category-page card reads "From $149/mo†".

The gating, verbatim (How-it-works step 1): *"Join the Hims Weight Loss Membership for only $39 in your first month, then $149/mo after that. **Medication cost not included.**"* And the price footnote: *"† **Price includes medication only, if prescribed.** An active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is billed separately and does not include or guarantee a prescription. Medication is not available without a membership."* → the $149/mo is real but med-only; all-in = membership + medication, hence `[partial]`.

### Wegovy® Pen — semaglutide, weekly injection

- **Parent:** Weight Loss · **url:** `/weight-loss/wegovy-pen` · **price:** From $199/mo† (medication only) · **price_visibility:** `[partial]`

> **H1:** "Wegovy® Pen" (sub: "with semaglutide")
> Sub-bullets: "An FDA-approved GLP-1 injection" · "Clinically proven to help people lose 35 lbs in one year, on average1" · "Range of dosages from 0.25mg–7.2mg"

Exact price string (PDP comparison table): "Starts at **_$199/mo_** / billed monthly, / membership required\*" — "Taken **_Once weekly_**". Badge on page: "High dose available" · "FSA & HSA eligible". Same membership footnote and "Medication cost not included" gating as the Pill → `[partial]`.

### Zepbound® Vial — tirzepatide, weekly injection

- **Parent:** Weight Loss · **url:** `/weight-loss/zepbound-vial` · **price:** From $299/mo† (medication only) · **price_visibility:** `[partial]`

> **H1:** "Zepbound® Vial"
> Sub-bullets: "FDA-approved GLP-1 for weight loss" · "Lose up to 21% of your body weight1" · "Take once a week"

Exact price string (PDP comparison table): "Starts at **_$299/mo_** / billed monthly, / membership required\*" — "Taken **_Once weekly_**", "Tirzepatide active ingredient". Footnote: *"**\*Price includes medication only, if prescribed.** An active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is billed separately..."* Same-page comparison shows Zepbound® KwikPen® also at "$299/mo". → `[partial]`.

### Foundayo™ Pill — orforglipron, oral

- **Parent:** Weight Loss · **url:** `/weight-loss/foundayo-pill` · **price:** From $149/mo† (medication only) · **price_visibility:** `[partial]`

> **H1:** "Foundayo™ Pill" (sub: "Orforglipron")
> Sub-bullets: "FDA-approved GLP-1 for weight loss" · "Lose 11% body weight on average in over a year1" · "Greater flexibility with no food, water, or timing restrictions"

Category-page card: "From $149/mo†". The PDP itself shows **no** price card — only the membership-gating step ("Join the Hims Weight Loss Membership for only $39 in your first month, then $149/mo after that. **Medication cost not included.**"). Pitched as "The only GLP-1 pill with no rules around food, water, and when to take it." → `[partial]` (price comes from the category teaser + the mandatory membership).

### Testosterone Rx+ — enclomiphene + supplements (the TRT flagship)

- **Parent:** Testosterone · **url:** `/testosterone/enclomiphene-supplements` · **price:** none on product page; FAQ "starts at $99/month for a 10-month plan paid upfront and in full" · **price_visibility:** `[on-request]`

> **H1:** "Testosterone Rx+"  (eyebrow above it: "Now with supplements")
> Sub: "Get your edge back with one daily pill, with enclomiphene to boost testosterone levels and supplements for energy metabolism & circulation support."

No price anywhere in the hero, card, or buy area — every CTA is "Get started" / "See if treatment is right for me" routing to the intake at `/g/i/tt`. The only number on the line, quoted from the FAQ verbatim: *"Pricing for low testosterone treatment with enclomiphene through Hims starts at $99/month for a 10-month plan paid upfront and in full."* Buy path is gated twice — intake **and** a required at-home lab: *"Lab testing is required to determine eligibility. After checkout, you'll be sent an initial lab kit..."* Ingredients (verbatim): "enclomiphene and supplements" — "L-arginine supports circulation, vitamins B6 & B12 support energy metabolism, and zinc supports healthy T levels." Compliance line: *"Compounded drug products are not approved or evaluated for safety, effectiveness, or quality by the FDA. Rx required."* → price is FAQ-prose-only and the real path is lab+intake-gated, hence `[on-request]`.

(Note: the sibling SKU `/testosterone/enclomiphene-tadalafil-supplements` carries the **identical H1 "Testosterone Rx+"** and the same $99/mo FAQ figure — its differentiator is the added tadalafil "to boost sexual performance." Kept as a distinct row below, keyed by its own slug.)

---

## Roster — complete at the indexed level

Every GLP-1 and testosterone offering visible on the captured pages. Within-company key = **Slug**. Price quoted verbatim. Molecule/form is in **What**.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (one line) |
|---|---|---|---|---|---|---|
| Weight Loss | family | — | `/weight-loss` | — | — | GLP-1 weight-loss line; "a holistic program" (nutrition + app + meds) gating a SKU roster. |
| Weight Loss Membership | buyable | Weight Loss | `/weight-loss/membership` | "$39 for the first month, auto-renews at $149/month thereafter" | published | Recurring fee that gates every weight-loss SKU; billed separately from medication. |
| Wegovy® Pill | buyable | Weight Loss | `/weight-loss/wegovy-pill` | "From $149/mo†" / "Starts at **$149/mo**" | partial | Semaglutide, once-daily oral GLP-1; med-only price + mandatory membership. |
| Wegovy® Pen | buyable | Weight Loss | `/weight-loss/wegovy-pen` | "From $199/mo†" / "Starts at **$199/mo**" | partial | Semaglutide, once-weekly injection; dosages 0.25–7.2mg; med-only + membership. |
| Zepbound® Vial | buyable | Weight Loss | `/weight-loss/zepbound-vial` | "From $299/mo†" / "Starts at **$299/mo**" | partial | Tirzepatide, once-weekly injection (vial); med-only + membership. |
| Zepbound® KwikPen® | buyable | Weight Loss | `/weight-loss/zepbound-kwikpen` | "From $299/mo†" / "Starts at **$299/mo**" | partial | Tirzepatide, once-weekly injection (pre-filled pen); price from category card + Vial-page comparison table (own PDP not captured). |
| Foundayo™ Pill | buyable | Weight Loss | `/weight-loss/foundayo-pill` | "From $149/mo†" | partial | Orforglipron, once-daily oral GLP-1; "no rules around food, water, timing"; med-only + membership. |
| Ozempic® Pill | buyable | Weight Loss | `/weight-loss/ozempic-pill` | "From $149/mo†" | partial | Semaglutide oral; FDA-approved for type-2 diabetes, off-label for weight loss (own PDP not captured). |
| Ozempic® (injection) | buyable | Weight Loss | (no PDP — category card/modal) | "From $199/mo†" | partial | Semaglutide weekly injectable; footer modal "Ozempic®" = "Weekly injectable GLP-1... commonly used off-label for weight loss." See note [a]. |
| Mounjaro® | buyable | Weight Loss | (no PDP — category modal) | "$1,899/mo†" / "$1,899/mo\*" | partial | Tirzepatide weekly injection; FDA-approved for type-2 diabetes, "commonly prescribed off-label for weight loss." |
| Zepbound® (generic) | buyable | Weight Loss | (no PDP — category card/modal) | "$1,899/mo†" / "$1,899/mo\*" | partial | Tirzepatide, weekly GLP-1 injection "FDA approved for chronic weight management." Brand-line Zepbound card distinct from the $299 Vial/KwikPen SKUs. See note [b]. |
| Testosterone | family | — | `/testosterone` | — | — | "Testosterone Rx" / "Testosterone Rx+" line; enclomiphene-based, at-home-labs-gated. |
| Testosterone Rx+ (enclomiphene + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-supplements` | none on page; FAQ "starts at $99/month for a 10-month plan paid upfront and in full" | on-request | Compounded enclomiphene + L-arginine/B6/B12/zinc, daily pill; lab + intake gated. |
| Testosterone Rx+ (enclomiphene + tadalafil + supplements) | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil-supplements` | none on page; FAQ "starts at $99/month for a 10-month plan paid upfront and in full" | on-request | Same as above + tadalafil "to boost sexual performance"; identical H1 "Testosterone Rx+"; lab + intake gated. |
| Enclomiphene | buyable | Testosterone | `/testosterone/enclomiphene` | — (not captured) | on-request | Enclomiphene-only variant; linked from category "Featured" + breadcrumb; page not captured this run. |
| Enclomiphene & Tadalafil | buyable | Testosterone | `/testosterone/enclomiphene-tadalafil` | — (not captured) | on-request | Enclomiphene + tadalafil variant; linked from category "Featured" + breadcrumb; page not captured this run. |
| Testosterone cypionate (injection) | buyable (roadmap) | Testosterone | (no PDP — category card) | "Coming in 2026*" | on-request | "Once-weekly injection"; "FDA approved"; explicitly not yet offered — FAQ: "Hims does not currently offer access to TRT injections." |
| Kyzatrex® (testosterone undecanoate) | buyable (roadmap) | Testosterone | (no PDP — category card) | "Coming in 2026*" | on-request | "Twice-daily oral pill," FDA-approved testosterone undecanoate; not yet offered. |

**Footnotes / verbatim anchors**

- **† (weight loss):** *"Price includes medication only, if prescribed. An active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is billed separately and does not include or guarantee a prescription. Medication is not available without a membership. Membership fee is not included."* (weight-loss category + every WL PDP)
- **\* (Mounjaro / generic Zepbound):** *"$1,899 price includes medication only, if prescribed. An active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter)..."* (weight-loss category footer modals)
- **\* (testosterone "Coming in 2026"):** *"Such expected launch is subject to certain assumptions and factors, some of which may be outside of our control, and as such may be subject to change."*
- **[a] Ozempic split:** the weight-loss category grid shows two Ozempic cards — one at "From $149/mo†" linking to `/weight-loss/ozempic-pill`, and one at "From $199/mo†" (image `ozempic-product-4_3`, no working "View details"). The footer modal titled "Ozempic®" shows "From $199/mo†" and describes a "Weekly injectable." Read as: oral pill = $149, weekly injectable = $199. Both quoted verbatim; not reconciled.
- **[b] Zepbound naming:** the brand carries three price points on the captured pages — Vial **and** KwikPen at "From $299/mo†" (the Hims weight-loss SKUs, with PDPs/comparison rows), and a separate generic "Zepbound®" card/modal at "$1,899/mo\*" framed as the off-label/full-price brand entry. Kept as distinct rows; no claim about which dose maps to which price.

## Provenance

- **Pages read (8, all this experiment's captures dir):** `weight-loss-category.md` (/weight-loss), `weight-loss-wegovy-pill.md`, `weight-loss-wegovy-pen.md`, `weight-loss-zepbound-vial.md`, `weight-loss-foundayo-pill.md`, `testosterone-category.md` (/testosterone), `testosterone-enclomiphene.md` (/testosterone/enclomiphene-supplements), `testosterone-enclomiphene-tadalafil.md` (/testosterone/enclomiphene-tadalafil-supplements). Context: `store/hims-com/profile.md`.
- **Gated / unreachable:** all-in weight-loss cost (med price + membership, before dose-titration variance — "Pricing may vary by dosage"); all testosterone pricing beyond the $99/mo FAQ teaser (intake + required lab); PDPs for Zepbound KwikPen, Ozempic Pill, Ozempic injection, Mounjaro, generic Zepbound, and both bare enclomiphene variants (priced/described only via category cards/modals or not captured). Out of tournament scope (no captures): sexual-health, hair-loss, mental-health, and Labs lines.
