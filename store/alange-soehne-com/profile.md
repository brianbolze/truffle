---
schema_version: "2.2"

# Identity
domain: alange-soehne.com
name: A. Lange & Söhne
aliases: ["Lange", "A. Lange und Söhne"]
parent: [richemont.com]      # STRAIN: inferred from footer governance links (Richemont Human Rights Statement on richemont.com + EthicsPoint compliance portal), not an explicit "part of the Richemont Group" statement on captured pages
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Richemont-group maison. Locale-prefixed paths (/us-en, /eu-de, /cn-zh, /gb-en) — scrape /us-en only; map sample is locale-skewed (4 us-en of 500), use homepage links as the discovery surface. Geo-detects visitor (banner offers /gb-en) but serves correct /us-en content under location:US. Custom Vite SPA served from /als/dist/assets/*; no public prices anywhere — every model is 'Price upon request' (boutique-led sales). Repair price schedule + overhaul pricelist live at separate /customer-service/* URLs (not in main nav). Press at press.alange-soehne.com (separate host)."
key_pages:
  timepieces: /us-en/timepieces
  all_timepieces: /us-en/timepieces/all-timepieces
  manufacture: /us-en/manufacture
  art_of_watchmaking: /us-en/manufacture/art-of-watchmaking
  heritage: /us-en/manufacture/heritage
  company: /us-en/manufacture/company
  services: /us-en/services
  boutiques: /us-en/boutiques
unverified_fields:
  - "Pricing — none public; every model reads 'Price upon request' (boutique-led). Repair/overhaul price schedule referenced but lives at /customer-service/* URLs not captured."
  - "parent: richemont.com is inferred from footer corporate-governance links, not an explicit ownership statement on captured pages."
  - "Founding/ownership financials (headcount, revenue, exact annual production) — not on the marketing site; a deep-research job."

description: "A German haute-horlogerie manufacture in Glashütte that hand-crafts mechanical luxury watches — six collections led by the LANGE 1 — all powered by in-house movements, sold price-on-request through boutiques and authorised dealers."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware]
portfolio_shape: Multi-product
business_model: Transactional / One-time
primary_industry: Consumer Goods

# Visual identity
logo_url: https://www.alange-soehne.com/als/favicon.ico   # STRAIN: branding.images.logo is an inline data-URI SVG; favicon fallback used
brand_colors: { primary: "#000000", background: "#FFFFFF", accent: "#B58B4C" }   # STRAIN: branding payload reports #0038FF (UI link chrome, not the brand). True identity is monochrome black-on-white/cream; warm "honeygold"/metal tone (~#B58B4C) read off product imagery
fonts: [ALangeUndSoehne-Headline, UniversforALS]   # bespoke brand faces (heading + body); Arial/Times are fallbacks
color_scheme: light
design_framework: custom   # hashed Vite bundle at /als/dist/assets/main-2ONFfoO3.js, no CMS markers; branding.designSystem said "custom" (ignored per rule, rawHtml agrees)
---

## Overview

A. Lange & Söhne is a Saxon haute-horlogerie *manufacture* — it develops, finishes, and assembles every movement by hand in Glashütte, Germany. The house makes only mechanical luxury wristwatches, organised into six watch families spanning two-hand classics to grand complications. There is no e-commerce checkout for watches: each model is listed "Price upon request" and sold through Lange boutiques and authorised dealers, with the website acting as catalogue, heritage archive, and after-sales service hub. The brand trades almost entirely on craftsmanship, in-house calibres, and a 180-year origin story.

## What they offer

Six watch families (LANGE 1 is the flagship-among-equals; all mechanical, all in-house movements, all "Price upon request"):

- **LANGE 1:** the signature family — asymmetric dial, outsize date, twin sub-dials; sub-lines incl. Little LANGE 1, Grand LANGE 1, LANGE 1 Moon Phase, Time Zone, Perpetual Calendar, Tourbillon Perpetual Calendar (incl. "Lumen")
- **SAXONIA:** the purist, minimalist dress line — incl. Saxonia Thin, Saxonia Annual Calendar, DATOGRAPH UP/DOWN
- **1815:** classically-styled homage to founder Ferdinand Adolph Lange (b. 1815), railway-track minute scale, Arabic numerals
- **RICHARD LANGE:** scientific / observation-watch line named for the patent-prolific son
- **ZEITWERK:** mechanically-driven *digital* (jumping-numerals) display watch — a signature technical statement
- **ODYSSEUS:** the modern sports line — steel, integrated bracelet, 12-bar water resistance (showering/swimming-rated)

Complication & finissage tiers used as cross-family selections: **Lange classics, Outsize date, Chronographs, Perpetual calendar, Tourbillon watches, Grand complications, HANDWERKSKUNST editions** (since 2011, top-tier hand-finishing), and **Flagship exclusive**. The all-timepieces grid surfaced **~96 individual references**. Catalogue depth (per-SKU case metal / reference / specs) defers to `offerings.md`.

Adjacent: **Straps and buckles** (the one openly shoppable category), and paid **after-sales** — Complete Service & Restoration, overhauls (recommended every 5–7 years).

## How it works / model

One-time luxury purchase, not subscription. Watches carry no online price and no add-to-cart — the journey is *discover online → enquire / "Contact our experts" → buy at a boutique or authorised dealer*. A shopping bag exists in the UI but is effectively for accessories. Revenue is the watch sale plus a lifetime after-sales tail (overhauls, restoration — "every Lange watch built since 1990 is accepted for repair"). Every timepiece ships with **"The History of Your Watch"** booklet that doubles as guarantee document and maintenance log.

## Positioning & audience

Targets the top tier of mechanical-watch collectors, competing with the haute-horlogerie elite (Patek Philippe, Vacheron Constantin). The claimed edge is *manufacture* integrity and Saxon craft, not Swiss heritage: in-house calibres, hand-engraved balance cocks (each engraver's style unique), **twofold assembly** (every movement built, disassembled, and rebuilt), German precision, and revival-from-near-extinction provenance. Walter Lange's motto — *"There is something one should expect not only of a watch but also of oneself: to never stand still"* — anchors the voice.

## Nav structure

```
- Timepieces — /us-en/timepieces
  - Explore our collection — /us-en/timepieces
    - Lange classics — /us-en/timepieces/selections/classics
    - Outsize date — /us-en/timepieces/selections/outsize-date
    - Chronograph — /us-en/timepieces/selections/chronographs
    - Perpetual calendar — /us-en/timepieces/selections/perpetual-calendar-watches
    - Tourbillon watches — /us-en/timepieces/selections/tourbillon-watches
    - Grand complications — /us-en/timepieces/selections/grand-complications
    - See all timepieces — /us-en/timepieces/all-timepieces
  - Families: LANGE 1 — /us-en/timepieces/lange-1 · SAXONIA — /saxonia · 1815 — /1815 ·
    RICHARD LANGE — /richard-lange · ZEITWERK — /zeitwerk · ODYSSEUS — /odysseus
  - Manufacture movements — /us-en/manufacture/art-of-watchmaking/manufacture-movements
  - Straps and buckles — /us-en/services/straps-and-buckles
- Manufacture — /us-en/manufacture
  - The art of watchmaking — /us-en/manufacture/art-of-watchmaking
  - Heritage — /us-en/manufacture/heritage
  - Company — /us-en/manufacture/company
    - Sustainability — /manufacture/company/sustainability
    - Corporate social responsibility — /manufacture/company/corporate-social-responsibility
    - Careers — /manufacture/company/careers (+ Apprenticeships)
  - News and events — /us-en/manufacture/news-and-events
  - Press — https://press.alange-soehne.com/ (separate host)
- Services — /us-en/services
  - Watch Registration — /services/watch-registration
  - Care and handling — /services/care-and-handling
  - Complete service and restoration — /complete-service-and-restoration
  - Guarantee information — /services/guarantee-information
  - FAQ — /services/faq
  - Service request — /services/contact-service
- Contact us — /us-en/contact (+ Newsletter; Find a boutique — /us-en/boutiques)
```

## Credibility & proof

- **Provenance:** founded 1845 by Ferdinand Adolph Lange ("the foundations for German fine watchmaking"); forcibly nationalised after WWII; **re-founded 1990 by Walter Lange** (great-grandson) with Günter Blümlein, first collection 1994.
- **Patents / pedigree:** son Richard Lange contributed to **27 patents**, some still used today; Emil Lange's "Century Tourbillon" won fame at the **1900 Paris World Exhibition** (Knight's Cross, Legion of Honour).
- **Technical firsts:** **TRIPLE SPLIT** — "the world's first mechanical rattrapante chronograph" measuring over several hours to 1/6 second; ZEITWERK mechanical digital display; fusée-and-chain transmission.
- **Craft claims:** all calibres developed/finished/assembled in-house in Glashütte; hand-engraved balance cocks; twofold assembly; HANDWERKSKUNST top-finish line since 2011; chronographs "flagship products since 1999."
- **Guarantee:** 24 months from purchase; **+1 year** when bought from a Lange boutique and registered; new 24-month guarantee after any out-of-warranty service. "The History of Your Watch" booklet per timepiece.
- **Retail presence:** global boutique network (e.g. Dresden, Berlin, Zurich salon) + authorised dealers; US Client Relations +1 800 408 8147.

## Visual & brand impression

High-luxury restraint: a near-monochrome black-on-white/cream gallery with generous negative space, centred serif display type (bespoke ALangeUndSoehne headline face), and large editorial product photography on plain grounds. The hero is a macro of a ZEITWERK-style jumping-numerals date over "GLASHÜTTE I/SA". Warm metal tones (pink/yellow/honeygold cases, brown alligator straps) supply the only colour; the dark editorial footer closes it. The design reads mature, museum-like, and deliberately un-commercial — no badges, no urgency, no prices — signalling exclusivity through quiet confidence.

## Strategic read

The whole site is engineered to *not* sell online — price-on-request and a vestigial cart push every serious buyer into a boutique relationship, protecting both margin and the high-touch clienteling that defines this tier. The narrative weight sits on "manufacture" (vertical, in-house, hand-finished) and a literal resurrection story (lost to nationalisation, reborn 1990) — differentiating a *German* house against the Swiss establishment on craft-authenticity rather than legacy alone. Within the Richemont watch stable it occupies the connoisseur/grail slot above the group's larger-volume maisons. The after-sales architecture (lifetime repair back to 1990, the History booklet) is itself a moat: it reinforces multi-generational ownership and a controlled secondary narrative.

## Provenance

- **Pages:** 7 analyzed via Firecrawl (markdown + full-page screenshots) — homepage, /manufacture, /manufacture/art-of-watchmaking, /manufacture/heritage, /manufacture/company, /timepieces/all-timepieces, /services. Map (500 URLs, locale-skewed) used for inventory; homepage links drove key-page selection.
- **Verify:** all 7 sourceURLs matched; all 7 body md5s unique — no geo/cache contamination. Served under location:US despite a UK geo-detect banner.
- **Credits:** 8 (1 map + 7 scrapes, all base 1cr; no enhanced proxy, no PDFs).
- **Couldn't get:** any actual prices (all "Price upon request"); repair/overhaul price schedule (lives at /customer-service/* URLs, not in main nav); per-SKU catalogue depth (deferred to offerings.md).
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): Hardware / Physical Products → Physical Products / Hardware.
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-31 homepage rawHtml — no `application/ld+json` present, so no JSON-LD structured-layer fields (Nav already captured). Re-stamped 2.0→2.2.
