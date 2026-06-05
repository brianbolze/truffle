---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: brellohealth.com     # company key; each offering's slug (its relative url) is its key *within* Brello
captured_at: 2026-06-04      # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "WordPress + WooCommerce + Elementor. Catalog census = /product-sitemap.xml → exactly 7 products (4 single compounded meds + 3 bundles), and the mega-nav + homepage grid agree (blind-source agreement → complete). Prices are PDP-shown but PROMOTIONAL/point-in-time: a struck-through 'Original price was $749 → $499' under a Deadline Funnel countdown ([deadlinefunnel] shortcode) — re-check next run. '$X/Month' = the 3-month plan total ÷ 3; real billing is the 3-month total charged upfront, auto-renewing 'every 10 weeks' (sermorelin: 'every 11 weeks'). BUY-FIRST: you pay before intake, so no dose ladder is shown pre-checkout. Bundle PDPs each carry TWO GLP-1 variants (semaglutide vs tirzepatide), each its own price. The sermorelin PDP FAQ has a copy-paste bug naming 'Semaglutide' (see Verbatim anchors). Clean hero vial renders live at 2026/02 'Bottle-1' paths (open with a Referer); 2025/01 thumbnail paths 403 to bare fetch."
---

## Portfolio overview

Brello is **Flagship + companions**: **GLP-1 weight loss is the flagship** (it leads the homepage, owns every testimonial, and sits inside all three bundles), with **NAD+** and **sermorelin** as longevity/vitality companions, then **three bundles** that stack them. The catalog is small and fully enumerable — **7 products, all compounded, all injectable, all sold as 3-month cash-pay plans** that include the consult, medication, injection supplies, the Brello app, Brello Rise classes, and a Facebook community.

**Visibility rule (stated once, applied to every row).**
- **`published`** — the displayed 3-month price is the complete, self-contained cost to start (medication included, no separate membership). Six of seven rows.
- **`partial`** — a further mandatory cost sits on top. Only **The Metabolic Compass**: after the included 90-day Lumen trial, the **Lumen app auto-renews at $19.90/mo** (a separate ongoing fee beyond the plan).
- **`on-request`** — none. Every SKU shows a price on its card/PDP (the buy-first model surfaces price *before* intake, not after).

**One pricing shape, two framings.** Every SKU is a **3-month plan charged upfront** then auto-renewing "every 10 weeks" (sermorelin: "every 11 weeks"). The "$X/Month" headline is that 3-month total ÷ 3. Prices are **promotional** (struck-through "original price" + countdown), so treat the exact numbers as a snapshot.

**Prominence (calibrated).**
- **GLP-1 weight loss is the lead line [HIGH]** — the homepage hero, every testimonial ("down 108 pounds"), the first two product cards, and a GLP-1 inside all three bundles.
- **Company-stamped badges [HIGH]:** **Tirzepatide** = "Most Requested," **Semaglutide** = "Most Popular" (homepage plan grid); **The Longevity Stack** = "Most Complete."
- **"New Arrival" tags [MED]** on Sermorelin + the bundles — recency, not depth.
- Card order within the grid left **[LOW]** — not used for ranking.

## Roster

Complete at the indexed level (Brello's 7 WooCommerce products; census confirmed against /product-sitemap.xml). Price quoted verbatim with on-page markers; molecule/form page-attested only (every PDP lists "Syringes with Needles & Injection Instructions" → injectable; molecule audit under Verbatim anchors). Every slug is an attested URL from a captured page.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Compounded Tirzepatide | buyable | — | /product/tirzepatide-b6 | ~~$749.00~~ **$499.00** every 3 months ("$166 Per Month"); Billed $499 today, then $499 Every 10 Weeks | published | tirzepatide + B6 (pyridoxine) · injectable vial · 3-mo all-in plan, med incl.; "Most Requested" |
| Compounded Semaglutide | buyable | — | /product/semaglutide-b6 | ~~$599.00~~ **$399.00** every 3 months ("$133 Per Month"); Billed $399 today, then $399 Every 10 Weeks | published | semaglutide + B6 (pyridoxine) · injectable vial · 3-mo all-in plan; "Most Popular" |
| Compounded NAD+ | buyable | — | /product/compounded-nad | **$239.00** every 3 months ("$79 Per Month"); Billed $239 today, then $239 Every 10 Weeks | published | NAD+ (nicotinamide adenine dinucleotide) · injectable, "minimum (3) 1,000mg vials" · 3-mo all-in plan |
| Compounded Sermorelin | buyable | — | /product/compounded-sermorelin | ~~$599.00~~ **$349.00** every 3 months ("$116 Per Month"); Billed $349 today, then $349 Every 11 Weeks | published | sermorelin (GH-secretagogue peptide) · injectable vial · 3-mo all-in plan |
| Empowered+ — GLP-1 + NAD+ | buyable | — | /product/empowered-longevity-lifestyle-plan | "From $199/month": Semaglutide+NAD+ **$598.00**/3mo ($598 today, then $598 every 10 wks); Tirzepatide+NAD+ **$698.00**/3mo | published | semaglutide \| tirzepatide + NAD+ · injectable · 3-mo all-in bundle |
| The Longevity Stack — GLP-1 + NAD+ + Sermorelin | buyable | — | /product/thrive-forward-longevity-lifestyle-plan | "From $299/month": Sema variant ~~$997.00~~ **$897.00**/3mo ($897 today); Tirz variant ~~$1,099.00~~ **$997.00**/3mo ($997 today) | published | semaglutide \| tirzepatide + NAD+ + sermorelin · injectable · 3-mo all-in bundle; "Most Complete" |
| The Metabolic Compass — GLP-1 + Lumen Tracker | buyable | — | /product/the-metabolic-compass-plan | "From $166/month": Semaglutide+Lumen Billed **$499** today ($499 sign-up + $399/3mo after a 3-mo free trial); Tirzepatide+Lumen Billed **$599** today ($599 sign-up) | partial | GLP-1 + Lumen Metabolism Tracker (hardware) · injectable + device · Lumen app renews **$19.90/mo** after 90-day incl. trial |

## Verbatim anchors

Price + molecule footnotes the roster points at, quoted exactly from the cited PDP captures:

- **Tirzepatide** (`/product/tirzepatide-b6`): title "**Compounded Tirzepatide With B6 (Pyridoxine)**"; "**The compounded GLP-1 medication included in this plan is tirzepatide.**"; "~~$749.00~~ Original price was: $749.00. $499.00 Current price is: $499.00. every 3 months … Billed **$499** Today … Then **$499** Every 10 Weeks … Cancel anytime"; FAQ "You will be charged **$499** for the 3-month plan that includes Tirzepatide, if approved."
- **Semaglutide** (`/product/semaglutide-b6`): title "**Compounded Semaglutide With B6 (Pyridoxine)**"; "**The compounded GLP-1 medication included in this plan is semaglutide.**"; "~~$599.00~~ … $399.00 … every 3 months … Billed **$399** Today … Then **$399** Every 10 Weeks."
- **NAD+** (`/product/compounded-nad`): "**Includes minimum (3) 1,000mg vials of NAD+ Medication (If Approved)**"; "NAD+ (Nicotinamide Adenine Dinucleotide) is a natural coenzyme…"; "**$239.00** every 3 months … Billed $239 Today … Then $239 Every 10 Weeks."
- **Sermorelin** (`/product/compounded-sermorelin`): title "**Compounded Sermorelin**"; "~~$599.00~~ … $349.00 … every 3 months … Billed _$349_ Today … Then $349 Every **11 Weeks**." **⚠ FAQ template bug:** the page's own FAQ reads "You will be charged $349 for the 3-month plan that includes **Semaglutide**, if approved" — a copy-paste error; the product is Sermorelin (title, gallery, and "Sermorelin Medication" line all confirm).
- **Empowered+** (`/product/empowered-longevity-lifestyle-plan`): "**3 Month Plan with Tirzepatide & NAD+:** You will be charged **$698** today … renew for $698 every 10 weeks."; "**3 Month Plan with Semaglutide & NAD+:** … **$598** today … $598 every 10 weeks."
- **The Longevity Stack** (`/product/thrive-forward-longevity-lifestyle-plan`): "~~$997.00~~ … **$897.00** every 3 months … Billed **$897** Today" (Semaglutide variant); "~~$1,099.00~~ … **$997.00** every 3 months … Billed **$997** Today" (Tirzepatide variant).
- **The Metabolic Compass** (`/product/the-metabolic-compass-plan`): "Tirzepatide (3 month plan) & Lumen Metabolism Tracker Device — **$499 every 3 months with a 3-month free trial and a $599 sign-up fee** … Billed **$599** Today"; "Semaglutide … **$399 every 3 months with a 3-month free trial and a $499 sign-up fee** … Billed **$499** Today"; "After 90 days, the Lumen app renews at **$19.90/month**, or save with an annual plan at **$9.90/month ($119/year**, billed annually). Cancel anytime and keep your device." (A stray, conflicting "renews at $29/" also appears on the page — flagged as point-in-time noise.)

*Molecule audit:* every molecule is page-attested (the GLP-1 SKUs name tirzepatide/semaglutide in body text + "with B6 (Pyridoxine)" in the title; NAD+ and sermorelin are named in their titles + "What's Included"). None inferred from a brand name. Form = injectable for all (each "What's Included" lists syringes/needles).

## Deep blocks

### PDP-template anatomy (opt-in — one block teaches all 7)

Every Brello PDP is the **same WooCommerce/Elementor shell**, so reading one maps the catalog. Spine, in order:
1. **H1** `Compounded <Molecule>` + an `## $<X> Per Month Special` sub-head (the ÷3 framing of the 3-month total).
2. **Trustpilot TrustBox** (4.1/5, 3,860 reviews) — repeated 3× per page.
3. **Gallery** — a clean isolated vial render (purple-cap compounding vial, "Compounded <Molecule>" label) + a shared "image-brello" infographic + "EXCLUSIVE MEMBERS ONLY ACCESS" promo cards (the brello app, the Thrive Facebook community "12,000+ members").
4. **"What's Included"** — identical 6–7 bullet list (medication if approved · syringes+needles · Brello app · Brello Rise classes · private FB community · provider review · fast shipping).
5. **Plan selector** — struck-through "Original price" → current price → "Billed $X Today / Then $X Every 10 Weeks / Cancel anytime," wrapped in a **`[deadlinefunnel]` countdown**.
6. **"No Intake Form Required Before You Pay"** — the buy-first disclosure ("purchase your plan … then complete an online intake … full refund" if not approved).
7. **"A Deeper Look Inside <Molecule>"** — mechanism prose with cited journal references (e.g., tirzepatide → Diabetologia, JAMA, SURPASS).
8. **"A Straightforward Path to Care"** (4 steps) → FAQ (approval, inclusion, timeline, refund/replacement).

**Flagship hero renders captured** (clean isolated vial product shots, badge-free, white background — for a design/rendering-reference consumer; assets in `captures/2026-06-04/images/`):
- **Tirzepatide** → `captures/2026-06-04/images/tirzepatide.png` (Tirzepatide-Bottle-1)
- **Semaglutide** → `captures/2026-06-04/images/semaglutide.png` (Semaglutide-Bottle-1)
- **NAD+** → `captures/2026-06-04/images/nad.png` (NAD-Bottle-1)
- **Sermorelin** → `captures/2026-06-04/images/sermorelin.webp` (sermorelin-thumb)

*(The on-PDP gallery variants carry baked "$166 / $79 Per Month" sunburst badges + "Slide for details"; the promoted renders above are the badge-free homepage "Bottle-1" assets. Bundle PDPs have no single clean render — their gallery leads with composite/lifestyle cards.)*

### The Metabolic Compass — why `partial` (the one non-self-contained plan)

The only SKU whose all-in isn't the shown number. Structure: a **GLP-1 plan ($399 sema / $499 tirz per 3 mo) + a Lumen Metabolism Tracker device with a $499/$599 sign-up fee**, and a **3-month free Lumen-app trial**. After 90 days the **Lumen app auto-renews at $19.90/mo** (or $9.90/mo annually, $119/yr) — a recurring cost on top of the GLP-1 plan, which is why this row is `partial` while the other six are `published`. "Cancel anytime and keep your device for lifetime breath measurements."

## Provenance

- **Pages read:** the 7 product PDPs (tirzepatide, semaglutide, nad, sermorelin, empowered-plan, thrive-forward-plan, metabolic-compass-plan) + the homepage plan grid + /faq — all in `captures/2026-06-04/`. Census cross-checked against /product-sitemap.xml.
- **Scope:** all 7 indexed products enumerated (complete — blind-source agreement: sitemap ∩ nav ∩ homepage grid). Bundle GLP-1 variants (sema/tirz) captured as price variants within the bundle row, not as separate SKUs.
- **Gated/unreachable:** none for price (buy-first surfaces price pre-intake); exact per-SKU dose ladders are not shown before checkout.
- **Point-in-time caveat:** prices are promotional — struck-through "original price" + a Deadline Funnel countdown; the exact numbers can flicker run-to-run. Member count is self-reported and inconsistent (80k vs 70k).
- **Credits:** rode the profile.md capture (the 7 PDPs were scraped once, serving both files) — 0 additional credits for offerings.
- **Run profile:** guided — `offerings.md` requested with **flagship hero product images** (4 single-med vial renders captured + promoted) and an **opt-in PDP-template-anatomy** deep block (design/rendering-reference consumer).
