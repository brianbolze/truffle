---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: nike.com
captured_at: 2026-06-24
enumeration: lines-omitted   # the Recovery/Wellness line is rostered complete at SKU grain; the rest of Nike's Catalog is OUT OF SCOPE by request (see Provenance scope note)
site_notes: "SCOPED ROSTER — recovery/wellness hardware only, by request; Nike overall is portfolio_shape: Catalog and is NOT enumerable per-SKU. The recovery line is small + fully enumerable: the whole roster + prices render on the collection grid /w/performance-recovery-collection-3k7dgz8hfx3z90poyzw274 (one scrape = every SKU, no per-PDP needed for price). PDP adds specs (Hyperboot scraped). Prices are promo-discounted (code SUMMER; sale + struck original both shown) — point-in-time, re-check next run. Style id rides the slug tail (…/65000-001)."
---

## Portfolio overview

A by-request **recovery & wellness** slice of Nike's catalog — *not* a Nike census. Nike's overall
shape is `Catalog` (un-enumerable per-SKU); this one line is small and fully enumerable, so it gets a
real SKU roster. It splits three ways:

- **Nike × Hyperice (co-branded electronic hardware)** — the headline. Seven powered devices Nike
  fronts but co-brands with **Hyperice** (massage guns, dynamic-air-compression boots/hips, a heated
  massage wrap, and the wearable **Hyperboot**). Warranty/service runs *through Hyperice*, not Nike —
  Nike is the storefront + brand, Hyperice the device maker. Price band **$119.97 → $999.97**.
- **Nike Recovery (own-brand passive tools)** — four cheap non-powered SKUs (recovery ball, two
  rollers, a training mat). Price band **$30 → $75**.
- **Nike ReactX Rejuven8 (recovery footwear)** — a recovery-specific cushioning shoe + slide.

**Prominence (calibrated):** "Best Seller" is Nike's *own* badge on the **NormaTec Elite Legs**
($999.97 — the priciest item) and the **ReactX Rejuven8 men's shoe** `[HIGH]` (own label). The
**Hyperboot** is the collaboration's flagship by editorial salience — its own size-fit guide and a
release article (`/a/nike-hyperice-boot-release-info`) `[MED]` (nav/editorial cues, not a badge).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (form · access) |
|---|---|---|---|---|---|---|
| Performance Recovery Collection | family | — | /w/performance-recovery-collection-3k7dgz8hfx3z90poyzw274 | — | — | the recovery line: Hyperice co-branded hardware + Nike own-brand tools + recovery footwear |
| Hyperice Hypervolt Go 3 | buyable | Nike × Hyperice | /t/hyperice-hypervolt-go-3-massage-gun-yhM8ZuwV | $119.97 ($149, 19% off) | published | percussive massage gun, compact/travel · cordless · DTC + store pickup |
| Hyperice Hypervolt 3 | buyable | Nike × Hyperice | /t/hyperice-hypervolt-3-massage-gun-sNqZiTTw | $209.97 ($249, 15% off) | published | percussive massage gun · cordless · DTC + store pickup |
| Hyperice Hypervolt 3 Pro | buyable | Nike × Hyperice | /t/hyperice-hypervolt-3-pro-massage-gun-jF8dYopA | $299.97 ($349, 14% off) | published | percussive massage gun, pro tier · cordless · DTC + store pickup |
| Nike x Hyperice Hyperboot | buyable | Nike × Hyperice | /t/hyperice-hyperboot-shoes-0v8aYsXz | $699.97 ($799, 12% off) | published | wearable heated + NormaTec air-compression recovery boot · battery/Bluetooth/app · DTC (see deep block) |
| Hyperice Venom 2 Back | buyable | Nike × Hyperice | /t/hyperice-venom-2-back-heated-massage-wrap-z1FKF4TL | $215.97 ($269, 19% off) | published | heated + vibration back massage wrap · battery · DTC + store pickup |
| Hyperice Normatec Elite Hips | buyable | Nike × Hyperice | /t/hyperice-normatec-elite-hips-dynamic-air-compression-massage-mk1iBmbR | $549.97 ($599) | published | dynamic air-compression hip wrap · battery · DTC |
| Hyperice Normatec Elite Legs | buyable | Nike × Hyperice | /t/hyperice-normatec-elite-legs-dynamic-air-compression-boots-itzr47im | $999.97 ($1,099) | published | dynamic air-compression leg boots ("Best Seller") · battery · DTC |
| Nike Recovery Ball | buyable | Nike Recovery | /t/recovery-ball-ZpXWFx | $30 | published | massage/trigger-point ball · passive · DTC |
| Nike Recovery Small Roller Bar | buyable | Nike Recovery | /t/recovery-small-roller-bar-SMPCr6 | $35 | published | handheld roller bar · passive · DTC |
| Nike Recovery Foam Roller | buyable | Nike Recovery | /t/recovery-foam-roller-w8Qdk7 | $50 | published | 13in foam roller · passive · DTC |
| Nike Training Mat 2.0 | buyable | Nike Recovery | /t/training-mat-2-72NdDg | $75 | published | training/stretching/yoga mat · passive · DTC |
| Nike ReactX Rejuven8 (Men's) | buyable | Nike ReactX Rejuven8 | /t/reactx-rejuven8-mens-shoes-kUTSf6kL | $75 | published | recovery cushioning shoe ("Best Seller") · footwear · DTC |
| Nike ReactX Rejuven8 (Women's) | buyable | Nike ReactX Rejuven8 | /t/reactx-rejuven8-womens-slides-9B7S52 | $65 | published | recovery cushioning slide · footwear · DTC |

*All prices are member/promo-discounted snapshots (code SUMMER); the struck original is quoted in
parens. Visibility is `published` throughout — the full self-contained price shows on the grid + PDP;
the SUMMER code is an optional promo, not a hidden mandatory cost.*

### Verbatim anchors

- **"Best Seller"** — Nike's own badge, shown on *Hyperice Normatec Elite Legs* and *Nike ReactX
  Rejuven8 Men's Shoes* (recovery_collection grid).
- **"Extra 20% w/ SUMMER"** — promo flag on the *ReactX Rejuven8 Women's Slides* tile; *"Extra 20% Off
  Select Styles: Use code SUMMER"* banner sitewide.
- **Hyperboot service:** *"Nike return policy is 60 days. One year warranty is through Hyperice only."*
  and *"FSA/HSA eligible"* (hyperboot PDP) — the device-maker-vs-storefront split, verbatim.
- **Form caveat:** the Hyperboot is filed under **"Shoes"** on-site (it's wearable), but it is a
  powered recovery device, not athletic footwear — see deep block.

## Deep blocks

**Nike x Hyperice Hyperboot — `/t/hyperice-hyperboot-shoes-0v8aYsXz` — $699.97 ($799, 12% off).**
Earned: a $699.97 item filed under "Shoes" that is actually a battery-powered recovery appliance — the
roster row can't carry the disambiguation or the spec depth a hardware consumer wants. Verbatim from
the PDP:

> *"Optimize your warm-up and recovery routines with the Hyperboot, a Nike x Hyperice collaboration.
> The wearable technology offers heat and Normatec dynamic air compression for feet and ankles that
> you can customize on the go."*

- **Mechanism:** *"A system of dual-air Normatec bladders bonded to warming elements evenly
  distributes heat throughout the upper… helps drive heat deep into the muscle and tissue in the feet
  and ankles."* Designed for *"standing, walking, sitting or traveling, the battery-powered shoes work
  while your feet relax."*
- **Control:** *"Buttons on the shoe or a Bluetooth connection to the Hyperice app let you choose from
  three levels of heat and Normatec dynamic air compression."*
- **Specs (verbatim):** Heat — *"Level 1 = 111°F (44°C)/Level 2 = 118°F (48°C)/Level 3 = 125°F
  (52°C)."* Compression — *"Level 1 = 50 mmHg/Level 2 = 130 mmHg/Level 3 = 210 mmHg."* Battery —
  *"1–1.5 hours on max heat/compression."* Plus *"USB-C charger," "TSA friendly," "FSA/HSA eligible,"
  "Spot clean," "Imported,"* Style *65000-001*.
- **Service:** *"Nike return policy is 60 days. One year warranty is through Hyperice only."*

*No other SKU earns a deep block — the grid roster carries the rest; the powered Hyperice devices
share the same "Hyperice makes it, Nike sells it" pattern this one establishes.*

## Provenance

- **Pages read:** `/w/performance-recovery-collection-3k7dgz8hfx3z90poyzw274` (the grid — every SKU,
  name + sub-type + sale/original price + style id, in one scrape) and the Hyperboot PDP
  (`/t/hyperice-hyperboot-shoes-0v8aYsXz/65000-001`, for the deep block). Discovery via homepage nav
  + `map --search hyperice` and `map --search recovery`. All under `captures/2026-06-24/`.
- **Scope note (`enumeration: lines-omitted`):** this file rosters **only** the Performance Recovery
  Collection (13 buyable SKUs across Nike × Hyperice hardware, Nike own-brand tools, ReactX Rejuven8
  footwear). **Intentionally omitted — the entire rest of Nike's catalog:** all sport footwear,
  apparel, and equipment across every sport; Jordan; NikeSKIMS; Converse; Nike By You; the app
  ecosystem. Those are `Catalog`-scale and not enumerable per-SKU — see `profile.md`'s *What they
  offer*. The 13-SKU count is the recovery line's size, **not** any measure of Nike's breadth.
- **Adjacent-but-excluded:** Nike Mind is footwear technology (sensation amplification), **not** a
  recovery/wellness device — excluded from this roster (noted in `profile.md`). Yoga gear and the Nike
  Well Festival are wellness-adjacent but apparel/event, not the hardware line; left to the catalog.
- **Snapshot caveat:** prices are promo (code SUMMER) + member-discounted — a point-in-time snapshot,
  not fixed; the struck original is carried in each Price cell. Re-check next run.
- **Run profile:** guided — emphasis "wellness/recovery, esp. consumer hardware." This file is the
  scoped roster that emphasis produced; vanilla Nike would write **no** offerings.md (Catalog shape).
