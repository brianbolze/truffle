---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: ford.com
name: Ford
aliases: [Ford Motor Company]
parent: []
owns: [fordpro.com]                  # Ford Pro — the commercial/fleet division, footer-linked, on its own site
socials:
  facebook: https://www.facebook.com/ford
  x: https://www.twitter.com/ford
  instagram: https://www.instagram.com/ford
  youtube: https://www.youtube.com/user/ford
  tiktok: https://www.tiktok.com/@ford
  threads: https://www.threads.net/@ford
external: {}                         # no third-party records (crunchbase/wikipedia/…) declared on the consumer site

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Built on Adobe Experience Manager (AEM) — /content/, /acslibs/, /etc.clientlibs/ paths. Top nav (Vehicles/Shop/Ownership Support/For Business) is client-rendered flyouts — empty in HTML+markdown; rebuild from footer + screenshot + /showroom. Company/about pages (/about, /about-us, /our-story, /history) are SSO/redirect stubs (~585 chars) → corporate info lives at corporate.ford.com; the consumer site is product-only. Full priced lineup lives on /showroom (every model + starting MSRP); per-model pricing under /<category>/<model>/pricing-and-incentives. Map is ~57% /local dealer pages + /support & /finance/customer-support FAQ noise — select from /showroom + /new-* + footer, not the map. Image CDN split: www.assets.ford.com (Adobe DAM) is fetchable with full browser headers (UA+Referer+Sec-Fetch); www.ford.com/acslibs + build.ford.com hard-block bare fetches (http=000) → clean configurator/'jellybean' renders ungettable. Pricing is time-stamped ('Pricing for June 4, 2026') with a rotating 'Employee Pricing for All' promo."
key_pages:
  showroom: /showroom                # full priced lineup — the roster backbone
  trucks: /new-trucks
  suvs: /suvs
  evs_hybrids: /new-hybrids-evs
  commercial: /new-commercial-trucks
  f150: /trucks/f150
  mustang: /cars/mustang
  bronco: /suvs/bronco
  mach_e: /suvs/mach-e
  explorer: /suvs/explorer
  bluecruise: /technology/bluecruise
  ford_credit: /finance/why-ford-credit
  ford_pro: https://www.fordpro.com   # commercial / fleet — separate site
unverified_fields:
  - "Vehicle MSRPs are a point-in-time snapshot, not fixed — page reads 'Pricing for June 4, 2026' under an active 'Employee Pricing for All' promo; dealer-set final price (dealer adjustment, destination/delivery, fees) is not shown."
  - "Most trim-level MSRPs are gated behind Build & Price — only base + halo-trim starting prices show on-page (e.g. F-150 Raptor $79,005, Mustang halo $106,490, Bronco Raptor $79,995)."
  - "Company facts (founding year, HQ, headcount, revenue) — not on the consumer site; /about, /about-us, /our-story, /history all redirect-stub to corporate.ford.com."
  - "logos og slot omitted — declared og:image (Ford_OG_1200x630.jpg) and apple-touch-icon were CDN-blocked from measurement (http=000)."

# Description — one sentence (~160-220 chars).
description: "The US consumer site of Ford Motor Company: trucks, SUVs, cars, EVs and commercial vans it designs and builds in-house and sells through a franchised dealer network, backed by captive Ford Credit financing and BlueCruise hands-free driving."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2C, B2B]            # consumer vehicle site first; Ford Pro / commercial / fleet is the B2B side
offering_category: [Physical Products / Hardware, Financial / Fintech Products]   # vehicles (maker), + Ford Credit captive lending
portfolio_shape: Multi-product       # enumerable model lines (showroom indexes ~22 models across SUVs/Trucks/Cars/Commercial/Performance)
business_model: Transactional / One-time   # core = vehicle sales via dealers; financing (Ford Credit) + subscription (BlueCruise/FordPass) layered on — see body
primary_industry: Automotive & Mobility

# Visual identity — branding payload is a hint; confirmed against screenshot + rawHtml.
logo_url: assets/wordmark.svg        # canonicalized to the wordmark (the blue oval, extracted from inline branding SVG)
logos:
  wordmark: { src: assets/wordmark.svg, w: 80, h: 30 }                                                             # the Ford blue oval (mark+script), transparent SVG — fill #00095B
  logomark: { src: "https://www.google.com/s2/favicons?domain=ford.com&sz=256", px: 180, transparent: false }     # white "Ford" script on a baked navy square (JPEG, no alpha)
  # og: omitted — declared Ford_OG_1200x630.jpg CDN-blocked from actual-width verification (see unverified_fields)
brand_colors: { primary: "#066FEF", accent: "#00095B" }   # bright UI/CTA "Ford blue" + the heritage navy oval; confirmed on screenshot
fonts: [FordFont, Arial]             # FordFont = the custom corporate typeface (branding.fonts[0])
color_scheme: light
design_framework: adobe experience manager (aem)   # from rawHtml — /etc.clientlibs/, /content/dam/, /acslibs/ (not the branding payload)
---

## Overview

Ford.com is the United States consumer storefront for **Ford Motor Company** — the marketing and shopping surface for its full vehicle lineup. It merchandises trucks, SUVs/crossovers, cars, electrified vehicles and commercial vans, lets a shopper Build & Price and search local inventory, then routes them to a **franchised dealer** to buy or lease. It is not a direct-sale site: pricing is shown as starting MSRP and the transaction completes at the dealer. Wrapped around the vehicles are Ford's recurring-revenue services — **Ford Credit** financing, the **BlueCruise** hands-free-driving subscription, **FordPass** connected services, and accessories/parts. Corporate identity, careers and investor material are firewalled off to `corporate.ford.com`; this site is purely the consumer brand.

## What they offer

Family-grain lines (per-SKU model roster + per-trim pricing in [`offerings.md`](offerings.md)); starting MSRPs shown on `/showroom`, verbatim:

- **Trucks & Vans:** Maverick, Ranger, F-150, Super Duty, Transit — **from $28,145** (Maverick) `[published]`
- **SUVs & Crossovers:** Escape, Bronco Sport, Bronco, Explorer, Expedition — **from $30,350** (Escape) `[published]`
- **Cars:** Mustang (the only remaining car line) — **from $32,640** `[published]`
- **Electric & Hybrid:** Mustang Mach-E (**$37,795**), F-150 Lightning (**$54,780**), Escape Hybrid (**$33,890**) / Plug-In Hybrid (**$35,400**) `[published]`
- **Commercial (Ford Pro):** E-Transit (**$48,150**), Transit, E-Series & F-Series chassis cabs/cutaways, F-650/F-750 — **from $38,135** `[published]`; fleet/upfit sold via `fordpro.com`
- **Performance / halo:** Mustang Dark Horse (**to $106,490**), Bronco Raptor (**$79,995**), F-150 Raptor (**$79,005**), Explorer ST (**$54,905**), Ford GT `[published]`
- **Ford Credit (financing):** buy / lease, GAP, Ford Protect extended service plans, WearCare, Ford Insure — rates via prequalify `[on-request]`
- **BlueCruise (hands-free highway driving):** **$495.00/Year** subscription `[published]`
- **Also:** FordPass app + Ford Rewards, connected services, Accessories Store, Ford Parts, Ford Blue Advantage (certified used)

## How it works / model

- **Merchandise → lead → dealer.** The site is a configurator + lead-gen funnel: Build & Price or Search Inventory, then "Locate Dealer" / "Order Through Dealer." Ford books revenue wholesale to its independent franchised dealers; the dealer sets the final transaction price (MSRP is a floor — "dealer adjustment, destination/delivery, taxes, title" excluded).
- **Recurring revenue layered on the metal:** captive financing (Ford Credit, "since 1959"), a paid ADAS subscription (BlueCruise, $495/yr), connected services (FordPass), and accessories/parts.
- **Incentives are the demand lever** — a sitewide "Employee Pricing for All" promo + $1,000 retail cash were live at capture, time-stamped to the day.

## Positioning & audience

Mass-market American automaker spanning entry trucks ($28K Maverick) to six-figure halos (GT, Dark Horse, Raptor). The tagline running across model pages — **"American Value. For American Values."** — and partnerships (MLB "America's Vehicle Drives America's Pastime," a Formula 1 return, Ford Racing) lean hard on heritage and a patriotic, work-and-play identity. Consumers are the primary audience; **Ford Pro** addresses commercial/fleet buyers (largely off-site at fordpro.com). Sibling luxury brand **Lincoln** is referenced only in shared-dealer pricing disclaimers, not merchandised here.

## Nav structure

Top-level nav buttons are client-rendered flyouts (empty in HTML); the tree below is reconstructed from the footer, the homepage screenshot, and `/showroom` categories.

```
- Vehicles
  - SUVs & Crossovers — Escape, Bronco Sport, Mustang Mach-E, Explorer, Bronco, Expedition
  - Trucks & Vans — Maverick, Ranger, F-150, Super Duty, F-150 Lightning, Transit
  - Cars — Mustang (/cars/mustang)
  - Electric & Hybrid — /new-hybrids-evs
  - Performance — /new-performance-vehicles · Ford Racing (performance.ford.com)
  - Commercial — /new-commercial-trucks
  - Future Vehicles — /future-vehicles
  - All Vehicles / Showroom — /showroom
- Shop
  - Build & Price · Search Inventory · Special Offers / Incentives
  - Trade-In Value · Towing Guides · Certified Used (Ford Blue Advantage)
  - Accessories Store · Ford Merchandise · Ford Parts
  - First Responder · Employee Pricing
- Ownership Support
  - Support Home · Service & Maintenance · Technology Support · EV Support
  - Owner Manuals & Warranty · Maintenance Schedule · Recalls
  - Roadside Assistance · Collision Assistance
  - FordPass / Ford Rewards · Vehicle Dashboard · Vehicle Health Report
- For Business
  - Ford Pro (fordpro.com) · Commercial Vehicles · Fleet · Ford Credit financing
- Finance (Ford Credit) — Why Ford Credit · Finance Options · Payment Calculator · Prequalify · Ford Insure · Investor Center
- Experience Ford (footer) — Corporate (corporate.ford.com) · Careers · Investors · Ford Pro · Ford Racing · Ford Philanthropy · Heritage Vault · FordPass · Co-Pilot360 · Going Electric
```

## Credibility & proof

Self-reported / marketing claims — recorded verbatim, **not** endorsed:

- **Ford Credit:** "Since 1959, millions of Americans have financed their Ford vehicle through Ford Credit." (NMLS #3018)
- **BlueCruise:** hands-free "Blue Zones" covering "over 130,000 miles of North American roads"; driver-facing camera eye-tracking.
- **Ford Co-Pilot360** driver-assist suite; 360 Viewer / Build & Price configurators on each model.
- **Brand / culture proof:** MLB partnership ("America's Vehicle Drives America's Pastime"), return to Formula 1, Ford Racing, an `/awards` page, Ford Philanthropy, Heritage Vault.
- **Owner programs:** FordPass Rewards, special incentives for military / first responders / medical / students.

## Visual & brand impression

Polished, modern, photography-forward — the screenshot reads as a confident mass-market automaker, not a boutique. Large cinematic lifestyle/beauty imagery (Bronco on a lakeshore, trucks on a hillside) over a clean white canvas, organized into clear merchandising bands ("Find Your Ford" category tiles, Featured Offers cards, Build & Price). The palette is **bright Ford blue (#066FEF)** for CTAs/section fills against the heritage **navy blue oval (#00095B)**; pill-shaped buttons (border-radius ~400px) and the custom **FordFont** typeface give it a current, corporate-systematic feel. Tone is plainspoken and patriotic ("American Value. For American Values."). Strong configurator integration signals a shop-online-buy-at-dealer model.

## Strategic read

- **It's a merchandising + lead funnel, not a store.** Every path ends at "Locate Dealer." The wholesale/franchise model is intact; ford.com optimizes desire and configuration, the dealer closes.
- **Services are the margin story grafted onto the metal** — captive lending (Ford Credit), a metered ADAS subscription (BlueCruise $495/yr), connected services, parts/accessories. This is where recurring revenue and software-style monetization live.
- **EV is a distinct pillar but a minority of the lineup** — Mach-E, F-150 Lightning, E-Transit get their own "Electric & Hybrid" merchandising, yet the roster is overwhelmingly ICE/hybrid, and a 2025/26 across-the-board "Employee Pricing for All" promo reads as demand stimulus.
- **Commercial is deliberately walled off** to Ford Pro (fordpro.com); the consumer site only lightly surfaces it.
- **Corporate self is firewalled** to corporate.ford.com — a clean separation of "shop for a Ford" from "Ford Motor Company the public company."

## Provenance

- **Pages:** 16 captured via Firecrawl (location US, maxAge 0): homepage (rich: rawHtml+branding+images+screenshot), `/showroom` (rich roster backbone), 4 category landings (`/new-trucks`, `/suvs`, `/new-hybrids-evs`, `/new-commercial-trucks`), 5 flagship PDPs (`/trucks/f150`, `/cars/mustang`, `/suvs/bronco`, `/suvs/mach-e`, `/suvs/explorer`, with `--images`), `/technology/bluecruise`, `/finance/why-ford-credit`. The 3 company pages (`/about`, `/our-story`, `/about-us`) returned ~585-char redirect stubs.
- **Verify:** 16/16 sourceURLs matched; all body md5s unique — no geo/cache contamination.
- **Credits:** 18 (1 map + 17 scrapes).
- **Couldn't get:** company/corporate facts (founding, HQ, financials) — consumer site redirect-stubs to corporate.ford.com; og:image + apple-touch-icon measurement (Ford CDN http=000); clean isolated configurator/"jellybean" renders (acslibs/build.ford.com hard-blocked) — flagship heroes instead sourced from the fetchable assets.ford.com DAM (marketing beauty shots, not isolated-on-white).
- **Run profile:** guided — +logos; +offerings (per-SKU roster + flagship hero images); no emphasis.
- **Enriched (model knowledge):** F (NYSE) ticker; Ford Motor Company is the corporate parent entity behind this consumer brand.
