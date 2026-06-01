---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.2"

# Identity
domain: cartier.com
name: Cartier
aliases: []
parent: [richemont.com]               # footer links Richemont group governance docs; Cartier is a Richemont Maison (inferred, see unverified_fields)
owns: []

# Capture meta
captured_at: 2026-05-31
capture_method: firecrawl
site_notes: "Salesforce Commerce Cloud (Demandware) storefront — /on/demandware.store/Sites-CartierUS-Site/ + demandware.static favicon are the fingerprint. cartier.com → www.cartier.com/en-us/home; /en-us/ locale prefix is the US canonical path. Map only ever returns the ~100-URL home-&-stationery subtree even with --search — useless for IA; the full mega-nav renders into the HOMEPAGE markdown (278 links), so discover the catalog from homepage links, not map. Prices appear on category LISTING pages (e.g. /jewelry/bracelets/love), not just PDPs. reCAPTCHA Enterprise + lazy-loaded hero leak noise into markdown/screenshots."
key_pages:
  heritage: /la-maison/the-story/living-heritage
  jewelry: /jewelry/cartier-jewelry
  high_jewelry: /high-jewelry/know-how
  watches: /watches/cartier-watchmaking
  love_bracelets: /jewelry/bracelets/love
  fragrances: /fragrances/signatures
  services: /services/jewelry/our-jewelry-services
  la_maison: /la-maison
unverified_fields:
  - "Watch pricing — no watch product/category page captured; watches are largely 'request appointment' online. Only jewelry ($2,130–$38,520, Love line) and fragrance ($49–$355) prices verified."
  - "parent: richemont.com — inferred from a footer link to Richemont's group human-rights statement, not an explicit on-site ownership statement."
  - "Headcount / revenue / boutique count — not stated on the marketing site (deep-research job, not capture)."

description: "The French luxury Maison, a jeweler and watchmaker since 1847, designing and selling fine jewelry, watches, high jewelry, fragrances, and leather goods direct to consumers online and through its global boutique network."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company                 # runs its own commerce/P&L and sells DTC, though owned by Richemont (AWS→Amazon precedent)
target_market: [B2C]
offering_category: [Physical Products / Hardware]   # maker of jewelry/watches/leather goods; sold DTC but classified by product, not as a reseller (maker-vs-reseller rule)
portfolio_shape: Catalog             # category × iconic-collection; hundreds of SKUs, un-enumerable
business_model: Transactional / One-time
primary_industry: Consumer Goods

# Visual identity
logo_url: https://www.cartier.com/on/demandware.static/Sites-CartierUS-Site/-/default/dwfa1db89c/images/favicons/favicon-196x196.png   # branding.images.logo is an inline data-URI SVG wordmark → favicon fallback
brand_colors: { primary: "#D50032", text: "#1D1C1C" }   # the iconic "Cartier red" (confirmed: footer band in screenshot); near-black wordmark/body
fonts: [Brilliant Cut, Fancy Cut, Helvetica]            # Cartier's proprietary display/heading faces; Helvetica/Arial as system fallback
color_scheme: light
design_framework: Salesforce Commerce Cloud (Demandware)   # demandware.store / Sites-CartierUS-Site / demandware.static in rawHtml + favicon
---

## Overview

Cartier is a French high-luxury Maison — "Jeweler and Watchmaker since 1847" (the site's own title tag) — selling fine jewelry, watches, high jewelry (haute joaillerie), fragrances, leather goods, eyewear, and home objects. The site is a full transactional e-commerce storefront (cart, wishlist, account, boutique locator) layered over heavy editorial/heritage content. Positioning is built almost entirely on heritage, savoir-faire, and a small set of globally-recognized icon collections (Love, Trinity, Panthère, Santos, Tank) rather than on price or feature comparison.

## What they offer

A luxury catalog organized as **category × iconic collection** (per-SKU depth defers to `offerings.md` if a project enables it):

- **Jewelry:** bracelets, rings, necklaces, earrings, engagement rings, wedding bands — organized by ~19 named collections (Love, Trinity, Juste un Clou, Panthère de Cartier, Clash de Cartier, Écrou, Grain de Café, Cartier d'Amour, etc.). Love bracelets verified at **$2,130–$38,520** on the listing page (most common: $5,300 / $7,950 / $11,000).
- **Watches:** collections Tank, Santos, Ballon Bleu, Panthère, Baignoire, Tortue, Roadster (the homepage hero: "INTRODUCING THE NEW ROADSTER"); plus Fine Watchmaking. No online price captured — watches skew to boutique/appointment.
- **High Jewelry (haute joaillerie):** one-of-a-kind creations grouped by theme (Flora & Fauna, Architecture & Purity, Geometry & Contrasts, Panther, Indomptables); positioned via savoir-faire, not price.
- **Fragrances:** signature lines (Baiser Volé, Déclaration, La Panthère, Must, Pasha, Rivières), plus high perfumery and gift/discovery sets. Verified **$49–$355**.
- **Bags & Accessories:** women's/men's bags, small leather goods, sunglasses, belts, scarves, cufflinks, lighters — by collection (Panthère, C de Cartier, Trinity, Losange, Must).
- **Home & Stationery:** pens, decorative objects, tableware, textiles, games, baby gifts — the only subtree the sitemap/map exposes.

## How it works / model

Direct-to-consumer **transactional** retail — one-time luxury purchases, no subscription. Online journey: browse by category/collection → product page → add to cart / wishlist → checkout, **or** book a boutique appointment (`/rdv-bookings`, "Find a Boutique"). Commerce runs on Salesforce Commerce Cloud (Demandware); account/auth via a separate `auth.cartier.com` OAuth flow. Purchase is wrapped in concierge-style service: complimentary delivery, easy return/exchange, free gift wrapping, fragrance sampling, and engraving/personalization. Post-purchase is a distinct revenue/retention surface — adjustments, care & repair, personalization, and a dedicated `cartiercare.cartier.com` service-request portal with published "service costs."

## Positioning & audience

Targets affluent luxury consumers (Firecrawl's branding read: "luxury consumers," tone "professional"). The claimed edge is **heritage + integrated savoir-faire**: "Since 1847"; "one of the only Maisons in the world to bring together every profession under the roof of their High Jewelry workshops" (stone experts, sculptors, jewelers, gem-setters, lapidaries, glypticians, lacquerers…). Differentiation is craft and icon-collection recognition, not specs or price. Competes with other luxury maisons (Van Cleef & Arpels, Tiffany, Bvlgari) and high watchmaking houses (Rolex, Patek Philippe — both pending in this store).

## Nav structure

Full mega-nav, reconstructed from homepage links (`/en-us/` prefix omitted):

```
- High Jewelry — /high-jewelry
  - All Creations — /high-jewelry/all-creations  (Architecture & Purity, Flora & Fauna, Geometry & Contrasts, Indomptables, Panther)
  - Latest Collections — /high-jewelry/latest-collections  (En Équilibre)
  - Markers of Style — /high-jewelry/markers-of-style  (Architecture & Purity, Cultural Dialogues, Flora & Fauna, Geometry & Contrasts)
  - Iconic Panthère — /high-jewelry/iconic-panthere
  - Living Legacy — /high-jewelry/living-legacy
  - Exceptional Stones — /high-jewelry/exceptional-stones
  - Know-How — /high-jewelry/know-how
- Jewelry — /jewelry
  - All Collections — /jewelry/all-collections  (Agrafe, C de Cartier, Cartier d'Amour, Fauna & Flora, Cartier Libre, Clash, Diamond, Écrou, Grain de Café, Juste un Clou, Les Berlingots, Love, Maillon Panthère, Panthère, Precious Colored Stones, Santos, Symbols & Logos, Trinity, Tutti Frutti)
  - Bracelets — /jewelry/bracelets  (Cartier d'Amour, Clash, Diamond, Écrou, Juste un Clou, Love, Panthère, Trinity)
  - Rings — /jewelry/rings  (Clash, Diamond, Écrou, Grain de Café, Juste un Clou, Love, Maillon Panthère, Panthère, Trinity; Rings Virtual Try-On)
  - Necklaces — /jewelry/necklaces  (C de Cartier, Cartier d'Amour, Fauna & Flora, Clash, Diamond, Écrou, Grain de Café, Juste un Clou, Love, Panthère, Trinity)
  - Earrings — /jewelry/earrings  (C de Cartier, Cartier d'Amour, Fauna & Flora, Clash, Diamond, Écrou, Grain de Café, Juste un Clou, Love, Panthère, Trinity)
  - Engagement Rings — /jewelry/engagement-rings  (Destinée, Étincelle, Love, Precious Colored Stones, Solitaire 1895, Trinity Ruban)
  - Wedding Bands — /jewelry/wedding-bands  (1895, Broderie, C de Cartier, Cartier d'Amour, Destinée, Étincelle, Love, Maillon Panthère, Trinity Ruban, Vendôme Louis Cartier)
  - Cartier Jewelry (editorial) — /jewelry/cartier-jewelry  (Creative Vision, Timeless Creations, Innovation & Savoir-Faire)
  - Advice & Services — /jewelry/advice-and-services
- Watches — /watches
  - Collections — /watches/collections  (Baignoire, Ballon de Cartier, Panthère, Roadster, Santos, Tank, Tortue)
  - Choose Your Watch — /watches/choose-your-watch  (by bracelet/strap, by material)
  - Cartier Watchmaking — /watches/cartier-watchmaking
  - Exceptional Watches / Fine Watchmaking — /watches/exceptional-watches/fine-watchmaking
  - Advice & Services — /watches/advice-and-services
- Fragrances — /fragrances
  - Signatures — /fragrances/signatures  (Baiser Volé, Déclaration, La Panthère, Must, Pasha, Rivières)
  - High Perfumery — /fragrances/high-perfumery  (Les Heures de Parfum, Les Épures, Les Heures Voyageuses, Les Nécessaires, Les Bases à Parfumer)
  - Sets — /fragrances/sets  (Discovery Sets, Gift Sets)
- Bags & Accessories — /bags-and-accessories
  - Women's Bags — /bags-and-accessories/womens-bags  (evening, mini, shoulder, top-handle, tote)
  - Men's Bags — /bags-and-accessories/mens-bags  (business, lifestyle)
  - Small Leather Goods — /bags-and-accessories/small-leather-goods  (card holders & key cases, purses & wallets)
  - Collections — /bags-and-accessories/collections  (C de Cartier, Losange, Must, Panthère C, Panthère Double, Panthère Graphique, Trinity)
  - Sunglasses — /bags-and-accessories/sunglasses  (C de Cartier, Clash, Décor C, Panthère, Première, Santos, Signature C)
  - Accessories — /bags-and-accessories/accessories  (belts, cufflinks & dress accessories, key rings, lighters, scarves, travel)
- Home & Stationery — /home-&-stationery
  - Home — /home-&-stationery/home  (baby gifts & toys, decorative objects, games, tableware, textiles)
  - Pens & Stationery — /home-&-stationery/pens-&-stationery  (pens, pen refills, notebooks, desk & office)
  - Accessories — /home-&-stationery/accessories  (key rings, money clips)
- La Maison — /la-maison
  - The Story — /la-maison/the-story  (Living Heritage, L'Odyssée de Cartier)
  - Savoir-Faire & Transmission — /la-maison/savoir-faire-&-transmission  (Savoir-Faire, Métiers d'Art, Cartier Institutes)
  - Cartier's Commitments — /la-maison/cartiers-commitments  (Art & Culture, Society & Communities)
- Services — /services  (Jewelry: day-to-day advice, services, size guide · Watches: advice, warranties, watchmaking services)
- Utility — Find a Boutique (stores.cartier.com) · Book Appointment (/rdv-bookings) · Contact (/contact-customer-care) · FAQ (/faq) · Check Order (/check-order) · My Cartier (auth.cartier.com) · Wishlist · Cart · Change Country
```

## Credibility & proof

- **Heritage:** "Since 1847" stated throughout; The Cartier Collection (museum-grade archive), exhibitions worldwide, and a published bibliography.
- **Savoir-faire:** in-house High Jewelry workshops spanning every craft profession; the Cartier Jewelry Institute (est. 2002, Paris); 150+ year partnership with the Haute École de Joaillerie; principal sponsor (since 2019) of the Association des Maîtres d'Art.
- **Service guarantees:** complimentary delivery, easy return/exchange, free gift wrapping, engraving/personalization, dedicated care & repair portal, and anti-theft registration via Enquirus.
- **Corporate governance:** footer links to Richemont group documents (human-rights statement), signaling parent-group oversight.

## Visual & brand impression

Restrained, editorial luxury. Centered serif **Cartier wordmark** on a white/cream field, generous whitespace, and large full-bleed product/heritage imagery (homepage hero: a steel Roadster watch on a brushed-metal ground). The signature **"Cartier red" (#D50032)** is used sparingly — a deep red footer band and CTAs — against near-black (#1D1C1C) type. Typography leans on Cartier's proprietary display faces (Brilliant Cut / Fancy Cut). The screenshot is largely lazy-loaded (heavy SPA-style storefront), but the rendered chrome reads unmistakably high-end: minimal, confident, heritage-forward, no discounting or urgency cues.

## Provenance

- **Pages:** 8 analyzed via Firecrawl (`maxAge:0`, `location:US`, `waitFor`) — homepage (all formats) + heritage, jewelry, high-jewelry know-how, Love bracelets (pricing), watchmaking, fragrances, jewelry services. IA reconstructed from 278 homepage links (map was useless — see site_notes). Plus 2 map calls (base + "love bracelet" search, both subtree-locked).
- **Verify:** all 8 sourceURLs matched; all 8 body md5s unique — no §5.1 geo/cache contamination.
- **Credits:** 10 (1 map + 1 map-search + 1 homepage + 7 key pages).
- **Couldn't get:** watch pricing (not sold online / appointment-gated); per-SKU catalog depth (Catalog shape — `offerings.md` territory); explicit Richemont ownership statement (inferred from footer link); headcount/revenue.
- **Migrations:** 2026-06-01 v1→v2.0 — offering_category remapped by rule (not re-captured): [Apparel & Footwear, Retail / E-Commerce] → Physical Products / Hardware (maker-vs-reseller).
- **Structured layer (schema 2.2):** ran `fc.py signals` on the persisted 2026-05-31 homepage rawHtml — JSON-LD present but no `sameAs`/`logo`/`alternateName`, so no new structured-layer fields. Re-stamped 2.0→2.2.
