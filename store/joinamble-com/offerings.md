---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: joinamble.com
captured_at: 2026-06-04
site_notes: "Catalog lives entirely in nav (<nav>) — 7 product pages, no /pricing, no storefront subdomain for the census. Every SKU is one Webflow PDP carrying a plan-length table (12-mo cheapest → 1-mo dearest) + a 'same price, every dose' claim. Prices are PDP-only (read off each page, ~1 scrape/SKU). /tesamorelin-injection is in nav but its PDP 404s — depublished. A/B: yes (rotating hero, run-to-run stat flicker) — pricing is a point-in-time snapshot. Hero vial renders are AVIF on the Webflow CDN (browser UA + sips to fetch/convert)."
---

## Portfolio overview

Amble sells **7 live prescription SKUs** across three lines, all **compounded**, all on the same plan-length subscription template (longer commit → lower per-month price), each PDP also claiming "same price, every dose" (terms below). Shape is a clean **Multi-product** roster, not a catalog — every SKU is enumerable at one PDP each.

- **Weight loss (GLP-1)** — `[HIGH]` the company's own flagship: the rotating hero leads with it, the referral program counts **only** Weight Loss sign-ups, and the Amble Cares access program is weight-loss-only. Compounded semaglutide + tirzepatide.
- **Anti aging** — `[MED]` a six-injectable dropdown menu (NAD+, Sermorelin, Glutathione, Lipo-B, Lipo-C — plus a **dead Tesamorelin page**), sharing one PDP template and the purple brand color. Lipo-B and Lipo-C are priced identically.
- **Skin** — `[MED]` one prescription-skincare line, compounded topical actives, the cheapest entry point ("Starting at $55").

**Shape finding:** the catalog is **100% compounded** — even the GLP-1 line is compounded semaglutide/tirzepatide, not branded Wegovy/Zepbound (homepage ISI names both molecules as compounded). The disclaimers' "facilitate both FDA-approved and compounded fulfillment" is generic pharmacy-network language; no FDA-brand SKU is actually sold.

**Product renders (opt-in asset, this run):** clean isolated 3-D vial renders captured for the 6 injectables → `captures/2026-06-04/images/{glp-1,nad,sermorelin,glutathione,lipo-b,lipo-c}.png` (amber for GLP-1, purple for the anti-aging line). Skin has no isolated render (topical — before/after + lifestyle only); Tesamorelin's PDP 404s.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight loss | family | — | /glp-1-injections | — | — | The flagship line; one buyable (GLP-1) |
| GLP-1 injection | buyable | Weight loss | /glp-1-injections | 12-mo **$135** · 6-mo **$145** · 3-mo **$160** · 1-mo **$179** /mo (homepage "From $179") | published | compounded **semaglutide & tirzepatide** · subcutaneous, once weekly · async intake → physician review (live consult where state law requires), 100% online |
| Anti aging | family | — | /glp-1-injections (dropdown; no own page) | — | — | Six-injectable menu; 5 live + 1 dead |
| NAD+ injection | buyable | Anti aging | /nad-injections | 12-mo **$125** · 6-mo **$167** · 3-mo **$183** · 1-mo **$199** /mo | published | compounded **NAD+** (nicotinamide adenine dinucleotide) · subcutaneous, max 0.5 mL/injection · async intake → physician review |
| Sermorelin injection | buyable | Anti aging | /sermorelin-injections | 6-mo **$135** · 3-mo **$149** · 1-mo **$159** /mo (no 12-mo tier) | published | compounded **sermorelin** (synthetic GHRH peptide) · subcutaneous, once daily (evening) · async intake → physician review |
| Glutathione injection | buyable | Anti aging | /glutathione | 12-mo **$75** · 6-mo **$83** · 3-mo **$92** · 1-mo **$100** /mo | published | compounded **glutathione** (antioxidant tripeptide: glutamine, cysteine, glycine) · subQ or IM, 200–800 mg, 1–3×/week · async intake → physician review |
| Lipo-B (MIC+B12) injection | buyable | Anti aging | /lipo-b | 12-mo **$120** · 6-mo **$125** · 3-mo **$133** · 1-mo **$149** /mo | published | compounded **MIC + vitamin B12** (cyanocobalamin; may include L-carnitine, inositol, methionine, choline, B6) · subQ or IM, once weekly, max 1 mL · async intake → physician review |
| Lipo-C injection | buyable | Anti aging | /lipo-c | 12-mo **$120** · 6-mo **$125** · 3-mo **$133** · 1-mo **$149** /mo | published | compounded **MIC + B-complex + vitamin C** (methionine, inositol, choline, pyridoxine/B6) · subcutaneous · async intake → physician review |
| Tesamorelin injection | buyable | Anti aging | /tesamorelin-injection | — (PDP 404s) | on-request | **not stated** (page depublished) — nav label "Naturally boost growth hormone"; molecule appears only in the product NAME, not page-attested. Not a live SKU. |
| Skin (prescription skincare) | buyable | — | /skin | **Starting at $55** /month | published | compounded topical actives — **tretinoin, clindamycin, azelaic acid, niacinamide, GHK-Cu, hydroquinone, tranexamic acid, vitamin B5/E, estriol, caffeine** (personalized per concern: acne, aging, hyperpigmentation, hydration, rosacea) · topical · async intake → physician review |

## Verbatim anchors

- **Plan-table model (all SKUs):** "Per Month" column over four rows — "12 Month / 6 Month / 3 Month / 1 Month" — per the PDPs (e.g. Glutathione: `12 Month $75 · 6 Month $83 · 3 Month $92 · 1 Month $100`). The 1-month rate is the homepage "From $X".
- **"Same price, every dose"** (PDP badge) — with terms: *"Any 'same price at every dose' promotion expires within 24 hours of any price updates. … Introductory or promotional pricing, including 'first month' offers, are not governed by the 'same price per dose' policy."* (NAD+, Sermorelin PDPs). A dose-independence claim, not an extra price — does not change visibility.
- **HSA/FSA (payment, not a price):** *"Yes—HSA and FSA cards are accepted for 3-month or longer plans. We also provide itemized receipts in case you need to self-submit to your benefits provider."* (Glutathione, Lipo-B, Lipo-C PDPs).
- **Molecule sourcing audit:** every molecule above is named in that SKU's PDP body (semaglutide/tirzepatide also on the homepage ISI). The lone `not stated` is **Tesamorelin** — its PDP 404s, so the molecule is attested only by the product name, which the contract forbids treating as a page attestation.

## Deep blocks

- **Tesamorelin — the live-in-nav, dead-on-page SKU.** `/tesamorelin-injection` is linked from both the top nav strip and the Anti-aging dropdown ("Naturally boost growth hormone"), but the page returns **HTTP 404 — "Page Not Found / The page you are looking for doesn't exist or has been moved"** (body is only the trust-badge marquee + a GrowSurf referral widget; no hero, plan table, or ISI). This is a genuine 404, not a §5.6 soft-404-with-content. So the anti-aging menu *advertises* six injectables but *sells* five — a roster row a coarser read would have priced from the nav label.
- **PDP-anatomy:** None earned as a separate block — every live PDP is the same shell (hero vial render → plan-table → "same price every dose" → "What you get with Amble" → "How to take" → side effects → ISI → How-it-works → reviews → referral). The roster's `What` column carries the only cross-SKU variation (molecule/dose), so reading one PDP (e.g. [glutathione](captures/2026-06-04/glutathione.md)) teaches the catalog.

## Provenance

- **Pages read:** the 7 live PDPs + the dead /tesamorelin-injection, all `captures/2026-06-04/` (cited above), cross-checked against the homepage (ISI molecule names, "From $179").
- **Scope:** all 7 live SKUs enumerated and priced; Tesamorelin rostered as a dead-PDP finding (no price). No leaf-level sub-variants (each SKU is a single PDP). Completeness cross-check: nav menu ∩ /map census agree on the 8 product paths (7 live + 1 dead) — no hidden SKUs surfaced.
- **Gated/unreachable:** none gated; Tesamorelin unreachable (404).
- **Point-in-time caveat:** prices run on an A/B-tested site (rotating hero, run-to-run stat flicker) — this is a snapshot, not a fixed truth. "Same price, every dose" promos expire within 24h of any price update (per PDP terms).
- **Run profile:** opt-in flagship **hero product renders** captured this run (6 injectable vial renders → `captures/2026-06-04/images/`), per the user's request; referenced from Portfolio overview. Default offerings runs skip image capture.
