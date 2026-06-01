---
schema_version: "2.2"

# Identity
domain: audemarspiguet.com
name: Audemars Piguet
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Adobe Experience Manager (AEM) site — /etc.clientlibs/ + clientlib markers in rawHtml. URL structure is /com/<locale>/ (EN = /com/en/...home.html); map is dominated by locale variants (fr/de/es/it/ja/ru/zh-hans/zh-hant) — filter to /com/en/. Homepage links are the reliable EN discovery surface (map is a 114-URL sample). No e-commerce/cart and no public watch prices on .com — it's a brand-showcase site that drives to boutique appointments; a maintenance 'Service Price list' page exists (/com/en/services/pricelist.html, not captured). Stores page is a Google-Maps embed (~29k chars of map-tile noise, no textual store list). Collections page is thin (client-rendered) but does list the 6 living families. Brand content also lives on separate hosts: 150years.audemarspiguet.com, apchronicles.audemarspiguet.com (AP Chronicles archive), aplb.ch (AP Lab / 150-year timeline)."
key_pages:
  collections: /com/en/collections.html
  royal_oak: /com/en/collections/royal-oak-collection.html
  origins: /com/en/about/origins.html
  commitments: /com/en/about/commitments.html
  services: /com/en/services/all-services.html
  stores: /com/en/stores.html
  novelties_2026: /com/en/watch/2026-novelties.html
unverified_fields:
  - "Watch prices — not published on .com (no e-commerce; sold via boutiques / AP Houses)."
  - "Maintenance-service pricing — behind /com/en/services/pricelist.html, not captured."
  - "Headcount / revenue / annual production volume — not on the marketing site (only public statement is that 'annual production and distribution remains limited')."

description: "A Swiss haute-horlogerie manufacture, founded 1875 in Le Brassus and still owned by its founding families, that designs and crafts high-complication mechanical watches — led by the iconic Royal Oak — sold through its own boutiques and AP Houses."

# Classification
entity_type: Company
target_market: [B2C]
offering_category: [Physical Products / Hardware]
portfolio_shape: Flagship + companions   # STRAIN: Royal Oak (+ Offshore + Concept) is the overwhelming hero; Code 11.59 / Neo Frame / Établisseurs are companions. Underlying reference count is catalog-scale.
business_model: Transactional / One-time
primary_industry: Consumer Goods

# Visual identity
logo_url: https://www.audemarspiguet.com/etc.clientlibs/ap-com/ui/clientlibs/publish/resources/static/audemars-piguet-logo.svg
brand_colors: { primary: "#000000", accent: "#FFFFFF" }   # STRAIN: identity is monochrome black-on-white (screenshot-confirmed); branding payload's #2B4F4F teal / #B02828 red are UI chrome, not brand colors
fonts: [Helvetica Neue]   # branding payload (body); display headings pair it with an italic serif for emphasis words — not separately fingerprinted
color_scheme: light   # white page chrome + black text; hero photography is dark/editorial (see Visual)
design_framework: Adobe Experience Manager (AEM)
---

## Overview

Audemars Piguet is one of the "big three" Swiss luxury watch *manufactures*, founded in 1875 by Jules Louis Audemars and Edward Auguste Piguet in Le Brassus, in the Vallée de Joux. It designs, manufactures, and services high-complication mechanical timepieces, and is "the oldest watchmaking manufacturer still in the hands of its founding families" — a point of independence it positions as central to its identity. Production is vertically integrated across sites in Le Brassus, Le Locle, and Meyrin, with deliberately limited annual volume. The `.com` is a brand-showcase and service portal, not a store: it presents the collections, the heritage, and after-sales care, and routes buyers to boutiques / AP Houses by appointment.

## What they offer

Mechanical wristwatches, organized into six living collections (plus heritage/pocket lines). No public prices on `.com`; Royal Oak and its two extensions dominate the catalog.

- **Royal Oak:** "From avant-garde to icon." The flagship — the 1972 stainless-steel luxury sports watch (octagonal bezel, integrated bracelet) that defines the brand. — /com/en/collections/royal-oak-collection.html
- **Royal Oak Offshore:** "A daring and sportier take on the Royal Oak." Larger, bolder sports line. — /com/en/collections/royal-oak-offshore-collection.html
- **Royal Oak Concept:** "A high-tech approach to Haute Horlogerie." Experimental materials and complications. — /com/en/collections/royal-oak-concept-collection.html
- **Code 11.59 by Audemars Piguet:** "Classic by nature, unconventional by design." The round-case contemporary line. — /com/en/collections/code-11-59-collection.html
- **Neo Frame:** "Vintage elegance meets modern innovation" (e.g. Neo Frame Jumping Hour). — /com/en/collections/neo-frame-collection.html
- **Établisseurs:** "A Sanctuary for Rare Craftsmanship" — Métiers d'Art / high-craft pieces (e.g. Établisseurs Galets). — /com/en/collections/les-etablisseurs.html
- **Heritage / historical lines:** Millenary, Jules Audemars, Classique, Remaster, Starwheel, and ultra-complicated pocket watches (e.g. "150 Heritage" Universal Calendar) surface in the catalog and AP Chronicles archive.

Complications span perpetual calendar, flying tourbillon, chronograph, minute repeater, openworked/skeleton, and quartz (Royal Oak Mini). Per-reference depth defers to `offerings.md`.

## How it works / model

One-time luxury purchase, not subscription. The `.com` carries no cart or price list for watches — it functions as catalog + heritage storytelling + appointment funnel. Buyers book an appointment or visit a boutique / **AP House** (the brand's hospitality-led mono-brand spaces) or an authorized retailer; a store-locator map fronts distribution. Revenue is the manufacture-and-sell-timepieces model, deliberately volume-constrained to protect quality and scarcity. A substantial **after-sales / maintenance** business wraps the product (see below), and brand-experience properties (Masterclasses, AP Lab Geneva, the Musée Atelier) deepen engagement.

## Positioning & audience

Targets affluent collectors and luxury consumers (B2C). Claimed edge is the combination of **independence + founding-family ownership + Vallée de Joux savoir-faire** — framed against larger group-owned maisons. Language leans on heritage ("150 years," "cradle of Haute Horlogerie," the *établissage* tradition), craft, and the icon status of the Royal Oak. Brand-world activations (Montreux Jazz Festival, music collaborations, art partnerships) extend a cultural, design-forward positioning beyond watchmaking. Deep voice work defers to `brand.md`.

## After-sales services

A core, separately-merchandised offering — the ownership relationship is explicitly marketed.

- **Periodical check-ups:** Complimentary annual boutique check of chronometric performance, water-resistance, and magnetization (not warrantied).
- **Complete maintenance service:** A secure 10-step protocol (registration/diagnosis → disassembly → component replacement → washing → lubrication → rate adjustment → optional polishing → casing-up → final QC) with a **2-year service warranty** valid across the global authorized network.
- **Water-resistance service:** Case disassembly/cleaning, movement check, component + (for quartz) battery replacement; warranty limited to replaced components.
- **Polishing service** and **Strap & Buckle service** (incl. retrofit on legacy models, handcrafted straps).
- **Restoration Workshop:** for vintage / legacy pieces.
- **Documents — Extract from the archives:** electronic certificate confirming a watch's unique case/movement numbers appear in AP's registers (records its existence, *not* a warranty of authenticity).
- **HI-Care Programme / AP Coverage:** ownership/coverage programs; plus online service request, warranty extension, and pick-up request flows (account-gated).

## Nav structure

```
- Watches — /com/en/watch-collection.html (search) ; /com/en/collections.html
  - Royal Oak — /com/en/collections/royal-oak-collection.html
  - Royal Oak Offshore — /com/en/collections/royal-oak-offshore-collection.html
  - Royal Oak Concept — /com/en/collections/royal-oak-concept-collection.html
  - Code 11.59 — /com/en/collections/code-11-59-collection.html
  - Neo Frame — /com/en/collections/neo-frame-collection.html
  - Établisseurs — /com/en/collections/les-etablisseurs.html
  - 2026 Novelties — /com/en/watch/2026-novelties.html
- Our World
  - Origins — /com/en/about/origins.html
  - Sustainability / Commitments — /com/en/about/commitments.html
  - Masterclasses — /com/en/masterclasses.html
- Stories (news) — /com/en/news.html
- Services — /com/en/services/all-services.html
  - AP Coverage — /com/en/services/ap-coverage.html
  - HI-Care Programme — /com/en/services/hi-care-programme.html
  - FAQ — /com/en/services/faq.html
  - AP Line — /com/en/services/line.html
- Stores (locator) — /com/en/stores.html
- Account / Appointment — /com/en/secure/account.html ; /com/en/form/appointment.html
```

## Credibility & proof

- **150-year heritage (1875):** Founding-family independence across four generations (Audemars & Piguet families; Olivier Audemars, Vice Chairman; Jasmine Audemars).
- **Manufacture provenance:** Le Brassus (oldest building 1868; first atelier 1907; Manufacture des Forges 2008), Le Locle, Meyrin.
- **Royal Oak:** Industry-defining 1972 luxury sports watch — the brand's enduring icon and primary proof point.
- **Sustainability transparency:** "3/6 Sustainability Framework" (Environment / People & Communities / Governance); published ESG annual reports (2023, 2024); AP SpeakUp whistleblowing line.
- **Brand-world / cultural credibility:** Musée Atelier, AP Lab Geneva, Masterclasses; Montreux Jazz Festival and music/art collaborations.

## Visual & brand impression

A high-maturity, editorial luxury aesthetic. The page chrome is light (white ground, black text, thin sans-serif nav with the AP wordmark and "150 years" logotype), but the body is carried by large, full-bleed **dark** photography and video — macro shots of watch mechanisms, hands at work, raw materials (the blue gemset/stone close-ups), and the Vallée de Joux landscape. Generous negative space, sharp zero-radius rectangles, restrained monochrome palette, and italic-serif emphasis words against the Helvetica-style sans give a measured, gallery-like, design-forward feel — closer to a craft/art house than a retailer. No promotional clutter, no prices, no urgency: the design itself signals exclusivity.

## Strategic read

The site's deliberate *refusal* to transact is the strategy: no cart, no prices, scarcity-by-design ("annual production remains limited"). It sells the manufacture, the family-owned independence, and the Royal Oak icon, then funnels to human, appointment-based, boutique/AP-House sale — a luxury model that treats the website as a brand cathedral and after-sales relationship as a durable, recurring revenue layer wrapped around an otherwise one-time purchase.

## Provenance

- **Pages:** 6 analyzed (firecrawl, /com/en/) — homepage, collections, about/origins, about/commitments, services/all-services, stores. Plus map (114 URLs, locale-filtered) + homepage links (45 EN paths) for discovery.
- **Verify:** All 6 sourceURLs matched; all 6 body md5s unique — no §5.1 geo/cache contamination.
- **Credits:** 7 (1 map + 1 homepage all-formats + 5 key pages, 1 each; no enhanced-proxy retries).
- **Couldn't get:** Watch prices (none on .com — no e-commerce); maintenance price list (separate page, not scraped); headcount/revenue/production volume (not on a marketing site); textual store list (Stores page is a Google-Maps embed).
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): Hardware / Physical Products → Physical Products / Hardware.
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-31 homepage rawHtml — no `application/ld+json` present, so no JSON-LD structured-layer fields (Nav already captured). Re-stamped 2.0→2.2.
