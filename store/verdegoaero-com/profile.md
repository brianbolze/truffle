---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: verdegoaero.com
name: VerdeGo Aero
aliases: []
legal_entity: ""
parent: []
owns: []
socials:
  facebook: https://www.facebook.com/VerdeGoAero/
  x: https://x.com/verdegoaero
  linkedin: https://www.linkedin.com/company/verdego-aero/
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "WordPress/Divi site behind Cloudflare + WP Engine. Map is press/news-heavy but homepage links expose the durable nav and product set. Homepage screenshot captured a mostly blank/teal loader-like state; product-page screenshots rendered fully and are better visual ground truth. Product pricing/order terms are inquiry-gated; product pages carry specs and contact CTAs."
key_pages:
  homepage: /
  hybrid: /hybrid/
  about: /about-verdego/
  vh3: /product/vh3/
  vh4t: /product/250kw-to-500kw-high-performance-hybrids/
  vh5: /product/vh-5/
  aircraft_integration: /product/aircraft-integration/
  defense: /defense/
  investors_partnerships: /investors-partnerships/
unverified_fields:
  - "Published product prices, ordering terms, delivery schedule, and contract structure — not shown; product pages route to contact/inquiry."
  - "Registered legal entity, headcount, revenue, and ownership/cap-table details — not stated in captured pages, JSON-LD, or footer."
  - "Homepage visual impression is limited because the homepage screenshot captured a mostly blank/teal loader-like state; product-page screenshots rendered correctly."

description: "Develops and manufactures hybrid-electric aircraft powerplants and integration services for commercial airframers and defense programs using liquid-fuel engines and generators."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Industrial / Manufacturing, Services / Consulting]
portfolio_shape: Multi-product
business_model: Services / Project-based
primary_industry: Manufacturing & Industrial

# Visual identity
logo_url: "https://verdegoaeropro.wpengine.com/wp-content/uploads/va-logo-white-horizontal.svg"
logos:
  wordmark: { src: "https://verdegoaeropro.wpengine.com/wp-content/uploads/va-logo-white-horizontal.svg", w: 519, h: 85 }
  logomark: { src: "https://www.google.com/s2/favicons?domain=verdegoaero.com&sz=256", px: 256, transparent: false }
  og: { src: "https://verdegoaero.com/wp-content/uploads/share-image_1200x675.jpg", w: 1200, h: 675 }
brand_colors: { primary: "#004962", accent: "#43D49D", secondary: "#F28C00" }
fonts: [Nunito Sans]
color_scheme: dark
design_framework: "wordpress (Divi)"
---

## Overview

VerdeGo Aero develops and manufactures hybrid-electric powerplant systems for high-performance electric aircraft. The site frames its wedge as solving the range, payload, speed, reserve-energy, and infrastructure limits of battery-only electric flight by combining electric propulsion with liquid fuels. Founded in 2017 by three hybrid-electric and battery-electric aircraft veterans, the company positions its technology as dual-use for commercial air mobility, regional cargo, drones, and defense aircraft.

VerdeGo says its products are being developed with U.S. Air Force and NASA support, and the site names commercial airframers, defense leaders, and aerospace innovators as customers or target partners.

## What they offer

- **VH-3 185 kW:** Piston-powered hybrid-electric aircraft powerplant providing "185 kW of continuous electrical power output" in a "650 lb (277 kg) package" with "0.37 lb/HP-hr (225 g/kW-hr)" fuel efficiency; product page uses "Contact us for information" rather than price `[on-request]`
- **VH-4T 400 kW:** Turbine hybrid-electric powerplant for higher-power commercial and military aircraft, providing "up to 400 kW of continuous electrical power"; built around a Pratt & Whitney PW206/PW207 engine, with VH-4T-RD and VH-4T-415 variants listed; page says "Inquire for ordering and delivery schedule" `[on-request]`
- **VH-5 Blended Turbofan:** Electrically convertible turbofan for high-speed VTOL/HSVTOL and high-power onboard electrical loads; the page gives an example of "1.5 MW of electrical output" plus "4,000 lb thrust-class" cruise operation and says architecture scales from "5 kW to 10 MW" `[on-request]`
- **Aircraft integration:** Engineering support for applying VerdeGo powerplants into next-generation aircraft, including modeling/simulation and integration across thermal systems, battery management, noise mitigation, electrical interfaces, communications interfaces, and certification acceleration `[on-request]`

## How it works / model

A VerdeGo hybrid powerplant combines five main components: engine, generator/motor, power electronics, thermal-management system, and hardware/software control system. The engine, either turbine or piston, spins a generator; the system produces electric power for electric aircraft while using Jet-A, JP-8, or sustainable aviation fuel instead of relying on batteries as the primary energy store.

The commercial model is inquiry/project driven. Product pages use contact or inquiry CTAs instead of published pricing, and the integration page describes close work with aircraft customers over multi-year aircraft programs. The site also describes U.S. Air Force, NASA, DARPA, Army DEVCOM, and airframer program work, so the business reads as a mix of powerplant sales, development contracts, and integration services.

## Positioning & audience

VerdeGo targets aircraft manufacturers, advanced air mobility companies, regional cargo and logistics aircraft developers, defense R&D programs, drone/UAS programs, and investors in dual-use aerospace. Its positioning is pragmatic electrification: electric aircraft performance without waiting for battery breakthroughs or new charging infrastructure. The claimed edge is liquid-fuel energy density plus electric-aircraft architecture: greater range, payload, endurance, and mission flexibility while still using existing aviation-fuel infrastructure and, where available, SAF.

## Nav structure

```
- About
  - Hybrid — /hybrid/
  - VerdeGo — /about-verdego/
  - The Team — /team/
- Products
  - VH-3 185 kW — /product/vh3/
  - VH-4T 400 kW — /product/250kw-to-500kw-high-performance-hybrids/
  - VH-5 Blended Turbofan — /product/vh-5/
  - Aircraft Integration — /product/aircraft-integration/
- Defense — /defense/
- News
  - In The News — /news-media/
  - Press Releases — /news-media/#press-releases
  - Technical Papers — /news-media/#technical-papers
- Investors — /investors-partnerships/
- Careers — /careers/
- Contact — /contact/
```

## Credibility & proof

- **Company history:** About page timeline says VerdeGo Aero was founded in 2017; earlier milestones include Anderson flying the "world's first parallel hybrid-electric aircraft" in 2011 and Bartsch/Lindbergh flying battery-electric aircraft in 2013.
- **Program support:** VH-3 page says development is supported by "multiple U.S. Air Force and NASA programs"; VH-4T page says VerdeGo has worked with the U.S. Air Force since 2024 on maturing VH-4T with testing meant to mirror military and FAA civilian certification processes.
- **Defense partnerships:** Defense page says AFWERX awarded VerdeGo multiple development contracts dating back to 2022, and the aircraft-integration page lists U.S. Air Force Agility Prime/Agile Support Prime, DARPA, Army DEVCOM Aviation & Missile Center, and NASA-related work.
- **Performance claims:** Homepage claims hybrid systems can deliver "Reducing Cost Up To 50%" and "Increasing Range 400-1000%"; VH-3 page claims "5-7X higher energy density than batteries" and "Up to 12X faster refuel/recharge"; these are self-reported site claims.
- **Fuel/infrastructure:** VH-3 and VH-4T pages state compatibility with Jet-A and sustainable aviation fuel; VH-4T also names JP-8. Hybrid page claims liquid fuel carries roughly "26 times the energy of the best battery packs available" pound-for-pound.
- **Investors:** Investors page says VerdeGo is backed by RTX Ventures, DiamondStream Partners, Seyer Industries, and the Florida Opportunity Fund, and lists current investors including RTX Ventures, DiamondStream Partners, Seyer Industries, Avfuel, Standish Spring Investments, and The Hatter Angel Network.

## Visual & brand impression

The rendered product pages are dark, technical, and hardware-forward: deep teal backgrounds, lime green product headings, orange CTAs, white spec cards, and large aircraft-powerplant photography or renders. The brand leans into aerospace engineering rather than climate lifestyle imagery. The logo is a stylized bird/aircraft mark with a spaced all-caps wordmark; the logomark candidate is usable but carries a baked white square background, so dark-slide consumers should treat it carefully.

## Strategic read

The site reads as a dual-use aerospace supplier trying to make electric aircraft practical before batteries can carry aviation missions alone. VerdeGo is not just selling a component; it is selling a powertrain architecture and integration expertise for aircraft programs where range, payload, reserve requirements, and fuel infrastructure decide feasibility. Defense credibility is prominent, but the same product family is positioned for commercial air mobility, cargo, and regional missions.

## Provenance

- **Pages:** 9 via Firecrawl (`fc.py`, maxAge:0 + location:US + waitFor) — homepage rich pass, /hybrid/, /about-verdego/, /product/vh3/, /product/250kw-to-500kw-high-performance-hybrids/, /product/vh-5/, /product/aircraft-integration/, /defense/, and /investors-partnerships/, plus the map. Homepage `branding`, `rawHtml`, nav, screenshot, signals, and logos were read from the saved payload.
- **Verify:** all sourceURLs matched; all body md5s unique; no junk soft-404s.
- **Credits:** 10 (1 map, 1 homepage, 8 key pages). Logo helper reused saved homepage payload; no Firecrawl credits.
- **Couldn't get:** public product pricing, ordering terms, delivery schedule, contract structure, legal suffix, headcount/revenue, cap table/ownership, independent verification of self-reported investor/agency/program claims, or a fully rendered homepage screenshot.
- **Run profile:** guided — +logos requested; standard profile otherwise.
- **Structured layer:** ran `fc.py signals` on the persisted homepage rawHtml. JSON-LD Organization provided name, URL, logo candidate, and Facebook/X/LinkedIn sameAs. No JSON-LD legalName was present; homepage nav region matched the captured dropdown structure.
