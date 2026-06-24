---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: ouraring.com
captured_at: 2026-06-24
enumeration: indexed-complete
site_notes: "Ring catalog = 3 model/material lines (Ring 5, Ring 4, Ring 4 Ceramic) + Membership; finishes are leaf variants of each ring, priced on the PDP finish picker (client-rendered — the Ring 4 picker didn't render in markdown, so its per-finish prices are uncaptured). Flash-sale pricing throughout (strikethroughs). Ceramic price disagreed $279 (cross-sell modules) vs $399 ~~$499~~ (PDP) same-day — reported, not reconciled. Accessories (chargers, Charging Case) exist but have no priced index page."
---

## Portfolio overview

Oura sells **one product — the smart ring — across three model/material lines**, plus a paid app **Membership** that's required to unlock the full value. The lines are generational/material variants of the same device, not co-equal product families:

- **Oura Ring 5** — the current flagship (newest gen, "world's smallest smart ring"). Prominence **[HIGH]** — homepage hero ("Subtle. Power.", "The world's smallest smart ring is here").
- **Oura Ring 4** — prior generation, kept on as the value option. Prominence **[HIGH]** — dedicated homepage flash-sale banner ("Take up to 44% off Oura Ring 4").
- **Oura Ring 4 Ceramic** — Ring 4 internals in a zirconia-ceramic shell; a style/premium-look play. Prominence **[MED]** — cross-sell module + its own PDP, no hero placement.
- **Oura Membership** — the recurring app subscription. Prominence **[HIGH]** — central to all positioning ("Oura Membership gives your body a voice").

Pricing is flash-sale and **point-in-time** (strikethroughs everywhere). Per-finish prices differ only within Ring 5 ($399 vs $499 by finish); Ring 4's per-finish prices didn't render in capture.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (form · access) |
|---|---|---|---|---|---|---|
| Oura Ring 5 | buyable | — | /store/rings/oura-ring-5 | **$399** (Silver, Black) · **$499** (Gold, Deep Rose, Stealth, Brushed Silver) | published | Titanium smart ring · 6 finishes · flagship; "world's smallest", 40% thinner; 50+ metrics; 6–9 day battery; waterproof 100m/IP68; buy outright |
| Oura Ring 4 | buyable | — | /store/rings/oura-ring-4 | **From $244** † (flash sale) | published | Titanium smart ring · 6 finishes (Silver, Black, Brushed Silver, Stealth, Gold, Rose Gold) · prior gen; 5–8 day battery; per-finish price uncaptured |
| Oura Ring 4 Ceramic | buyable | — | /store/rings/oura-ring-4-ceramic | **$279** ‡ (cross-sell) · **$399 ~~$499~~** (PDP: Midnight, Cloud) | published | Zirconia-ceramic exterior + titanium interior · 4 finishes (Midnight, Cloud, Tide, Petal — only Midnight & Cloud priced on PDP) · 5–8 day battery; incl. polishing pad |
| Oura Membership | buyable | — | /membership | **$5.99 USD/month or $69.99 USD/year** § (first month free, new members) | published | App subscription · monthly or annual · HSA/FSA eligible; unlocks 50+ metrics, Readiness/Sleep/Activity scores & Oura Advisor (AI); requires an Oura Ring |

### Verbatim anchors

- **† Ring 4 "From $244":** homepage — *"Lowest price ever / Take up to 44% off Oura Ring 4"*, *"Oura Ring 4 Flash Sale and free shipping through June 26th"*; cross-sell module reads *"Oura Ring 4 — From $244"*. The Ring 4 PDP itself carried no price (client-rendered).
- **‡ Ring 4 Ceramic price conflict (same-day):** homepage + /membership cross-sell modules read *"Oura Ring 4 Ceramic — $279"*; the /store/rings/oura-ring-4-ceramic PDP finish picker reads *"$399 ~~$499~~"* for both Midnight and Cloud. Reported, not reconciled — likely a flash-sale vs PDP module mismatch.
- **§ Membership pricing footnote (verbatim, international):** *"$5.99 USD/month or $69.99 USD/annually before tax for US members, €5.99/month or €69.99/annually after tax for EU members, A$9.99 AUD/month or A$109.99 AUD/annually after tax for Australian members, CA$7.99 CAD/month or CA$89.99 CAD/annually before tax for Canadian members, ¥999/month or ¥11,800/annually after tax for Japanese members, £5.99/month or £69.99/annually after tax for UK members, CHF5.99/month or CHF69.99/annually after tax for Swiss members, $6.99 USD/month or $79.00 USD/annually after tax for rest of world."*
- **Ring ↔ Membership relationship:** /membership FAQ — *"purchasing, activating, and consistently wearing an Oura Ring is the only way to unlock all of the daily health insights"*; and *"If you choose not to begin or continue your Oura Membership, your Oura Ring and Oura App will still function, but the insights, personal health data, and benefits you receive will be much more limited."* (Membership is required for the value prop but not for basic function — so the ring rows stay `published`, not `partial`.)
- **Molecule:** N/A — hardware/software company, no molecule axis (`not stated` by design).

## Deep blocks

- **Oura Ring 4 Ceramic — price disambiguation (earned: a roster row can't carry the conflict).** Three captured surfaces, two prices, one day: the homepage and /membership cross-sell modules both show **$279**; the product page's own "Choose your finish" picker shows **$399 ~~$499~~** for Midnight and Cloud. Two of four ceramic finishes (Tide, Petal) appear in the page's color story but have **no price** in the picker — possibly out of stock or not-yet-released. Net: a buyer's actual ceramic price is unsettled at capture; quote both and treat as flash-sale-volatile.
- Otherwise **none earned** — the roster carries this company (one product, three transparent ring lines, one membership; no molecule/dose ambiguity to resolve).

## Provenance

- **Pages read (cited captures, all 2026-06-24):** `/store/rings/oura-ring-5`, `/store/rings/oura-ring-4`, `/store/rings/oura-ring-4-ceramic`, `/membership`, plus the homepage cross-sell + flash-sale modules (`captures/2026-06-24/`).
- **Scope note (enumerated vs not):** all 3 ring model lines + the Membership are rostered at model grain (the level Oura indexes its store at, `/store/rings/<model>`) → `indexed-complete`. **Leaf detail not enumerated** (does not set `lines-omitted`): per-finish Ring 4 prices (client-rendered, absent); Ring 4 Ceramic Tide & Petal finishes (shown, unpriced); accessories (chargers/USB-C included; fast-charging **Charging Case** "sold separately", unpriced) — Oura has no accessories index page, and accessories are add-ons to the ring, not a co-equal line.
- **Point-in-time caveat:** every price here is a flash-sale snapshot (strikethroughs, "up to 44% off", "Flash Sale through June 26th") — re-capture for current pricing; do not read as MSRP.

### Run profile

Guided run — `offerings.md` added to a standard `/research-company` capture (per-SKU roster, no flagship hero images, no emphasis).
