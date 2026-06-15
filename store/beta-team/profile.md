---
# Query contract for this store: ../../QUERYING.md - parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.6"

# Identity
domain: beta.team
name: BETA Technologies
aliases: [BETA]
legal_entity: "BETA Technologies, Inc."
parent: []
owns: []
socials:
  instagram: "https://www.instagram.com/beta.aircraft/"
  linkedin: "https://www.linkedin.com/company/beta-air-llc"
  facebook: "https://www.facebook.com/BetaElectricAviation/"
  x: "https://x.com/BETA_aircraft"
  youtube: "https://www.youtube.com/@beta.technologies"
external: {}

# Capture meta
captured_at: 2026-06-14
capture_method: firecrawl
site_notes: "HubSpot CMS site. Homepage nav is the clean IA; map is noisy with stories/open-positions. Investor page starts with hCaptcha/language-list noise before the useful About BETA block. Product prices are not public; most sales paths are contact forms."
key_pages:
  homepage: /
  aircraft: /aircraft
  charge: /charge
  motor: /motor
  battery: /battery
  flight_controls: /flight-control-computers
  training: /flight-training
  defense: /defense
  team: /team
  timeline: /timeline
  investors: "https://investors.beta.team/"
unverified_fields:
  - "Product purchase prices and contract terms - no prices published; sales/contact forms gate aircraft, charging, motor, battery, flight-control, training, and defense inquiries."
  - "Exact production-facility size - homepage says 188,000 square feet; timeline says 188,500 square feet."
  - "Detailed financials, current share price, and market cap - investor landing page was captured, but filings/PDFs were not scraped."

# Description
description: "Designs, manufactures, and sells electric aircraft, propulsion, batteries, flight controls, chargers, and training for cargo, defense, passenger, and medical aviation operators."

# Classification
entity_type: Company
target_market: [B2B, B2G]
offering_category: [Physical Products / Hardware, Services / Consulting]
portfolio_shape: Multi-product
business_model: Transactional / One-time
primary_industry: Manufacturing & Industrial

# Visual identity
logo_url: "https://beta.team/hubfs/Brand/BETA_Logo_Gray_Updated.png"
logos:
  wordmark: { src: "https://beta.team/hubfs/Brand/BETA_Logo_Gray_Updated.png", w: 248, h: 68 }
  logomark: { src: "https://beta.team/hubfs/Logos/BETA_B_bolt.WHITE.png", px: 300, transparent: true }
  og:       { src: "https://beta.team/hubfs/3%20Ship%20CX300%2020250814_0060%20(1).jpg", w: 1200, h: 800 }
brand_colors: { primary: "#09090B", accent: "#6C757D", background: "#FFFFFF" }
fonts: [Titillium Web, JetBrains Mono]
color_scheme: light
design_framework: hubspot cms
---

## Overview

BETA Technologies is an electric-aviation manufacturer whose site describes it as "an aerospace company manufacturing electric flight." It builds the ALIA aircraft family in CTOL and VTOL configurations, plus the propulsion, battery, flight-control, charging, and training systems needed to operate that aircraft ecosystem. The investor page states BETA designs, manufactures, and sells electric aircraft, propulsion systems, components, and charging systems to operators worldwide, serving cargo/logistics, defense, passenger, and medical end markets.

The company is public-company shaped in this capture: the investor site carries SEC filing links and the timeline says BETA IPOed on the New York Stock Exchange under ticker "BETA" in 2025. The site-derived legal name is "BETA Technologies, Inc." from the investor contacts block.

## What they offer

- **ALIA aircraft:** CTOL and VTOL all-electric aircraft configurations; captured specs include "336 nm" max demonstrated range, "200 ft3" cargo capacity, "5 Passengers," "1 hr" charge time, and "153 kts" max speed; no aircraft price published `[on-request]`.
- **Charging systems and network:** Charge Cube, Mini Cube, and Thermal Management Cube; Charge page says the network has "over 60 sites online" and supports operators building charging networks; no charger or network pricing published `[on-request]`.
- **Electric propulsion systems:** H500B pusher engine and V600A lift engine; motor page says the systems are "Designed, produced and sold by BETA Technologies" and power vehicles across platforms and propulsion needs; no motor price published `[on-request]`.
- **Energy storage systems:** Battery packs for electric propulsion platforms; captured specs include "45 kWh," "832 V max," "400+ kW" peak power, and "255 kg (176 Wh/kg)"; no pack price published `[on-request]`.
- **Flight control computer:** FCC for fly-by-wire aircraft integration, described as proven on CX300 and designed for Part 23 and Part 25 applications; no FCC price published `[on-request]`.
- **Training and simulation:** Permanent Thunderdome simulators, trailer-borne Microdome units, and mobile VR training; no training price published `[on-request]`.
- **Defense ALIA MV250:** Autonomous hybrid VTOL aircraft for contested logistics; defense page lists "250+ nm" range with 2,000 lbs payload and "150+ KIAS" max airspeed; no defense program pricing published `[on-request]`.

## How it works / model

BETA sells high-value aerospace hardware and related training/support directly to operators, with most commercial paths ending in "Contact Sales" or inquiry forms rather than checkout. Homepage funding language cites military contracts, firm deposits, charging sales, EXIM financing, and equity investment; the investor page adds that enabling technologies create aftermarket revenue opportunity over each aircraft's life. The operating model is vertically integrated: aircraft, motors, batteries, FCCs, chargers, simulators, flight training, customer support, and charge-network access reinforce each other.

## Positioning & audience

BETA targets aviation operators rather than consumers: logistics carriers, medical transport, passenger operators, defense customers, airports/FBOs, training organizations, and aircraft/OEM partners. The site positions BETA as pragmatic electric aviation for real missions, foregrounding lower operating cost, safety validation, quiet/zero-emissions flight, and the ability to deploy the whole ecosystem around the aircraft. Defense is not a side note: it has its own top-level page, advisory board, and ALIA MV250 logistics framing.

## Nav structure

- Products & Services
  - Aircraft - /aircraft
  - Charge - /charge
  - Motor - /motor
  - Battery - /battery
  - Flight Controls - /flight-control-computers
  - Training - /flight-training
- Defense - /defense
- Company
  - Careers - /careers
  - Team - /team
  - Timeline - /timeline
- Resources
  - Stories - /stories
  - eIPP - /eipp
  - Glossary - /glossary
  - Videos - /video-library
  - Photos - /brand-assets/photos
- Investors - https://investors.beta.team/
- Shop - https://shop.beta.team/
- Support footer
  - Brand Assets - /brand-assets
  - Privacy Policy - /privacy-policy
  - Ethics and Compliance Line - https://irdirect.net/BETA/whistleblower
  - Contact BETA - /contact

## Credibility & proof

- **Flight record:** homepage flight counter showed "150,435.06" NM flown at capture time; investor page says the ALIA family has flown "more than 120,000 nautical miles."
- **Backlog:** homepage says BETA has "more than 800 aircraft in the backlog" and is funded by military contracts, firm deposits, charging sales, EXIM financing, and equity investment.
- **Manufacturing:** homepage says advanced technologies are built in a "188,000-square-foot, net-zero manufacturing and production space"; timeline separately says the final assembly and production facility is "188,500-square-foot" with capacity up to "300 aircraft per year."
- **Customers/partners:** homepage logo wall and timeline cite United Therapeutics, UPS, Air New Zealand, Bristow, U.S. Air Force, U.S. Army, EXIM, Fidelity, TPG, Qatar Investment Authority, Helijet, New Zealand Air Ambulance Service, GE Aerospace, UrbanLink, Ryan Air, and others.
- **Certifications and validation:** homepage says Charge Cubes are "UL-listed"; timeline says Charge Cube received "UL Certification"; battery and FCC pages cite DO-160G testing/qualification; FCC page cites ARP4754 and DO-254; timeline records FAA test-pilot evaluation, a Hartzell electric-propeller FAA certification with BETA, and DoD/USAF/Army flight exercises.
- **Public-company signals:** investor page links Q1 2026 financial results, a 10-Q, SEC filing alerts, and governance pages; timeline says the 2025 IPO raised over "$1 billion" and debuted on NYSE under ticker "BETA."

## Visual & brand impression

The rendered site is aerospace-industrial and restrained: black/white/gray UI, large aircraft photography, small uppercase navigation, and hard-edged CTAs. It feels more like an engineering/manufacturing company than a consumer EV brand - lots of certification, testing, operations, facility, and partner proof, with Vermont/manufacturing pride threaded through the imagery. The HubSpot implementation is visible in the captured payloads and CTA links, but the front-end presentation is polished and photography-led.

## Strategic read

BETA is not positioning as a single-aircraft startup; it is selling an integrated electric-aviation stack. The captured site uses the aircraft as the hero, but the deeper pages show the real scope: batteries, propulsion, FCCs, charging infrastructure, training/simulation, field support, and aftermarket/MRO concepts. The strategic bet is that electric aviation adoption needs the whole operating environment, not only an aircraft.

## Provenance

- **Pages:** 11 analyzed via Firecrawl (`maxAge:0`, US location, full-format homepage): homepage, aircraft, charge, motor, battery, flight_control_computers, flight_training, defense, team, timeline, investors; plus `/map` inventory of 318 URLs.
- **Verify:** `fc.py verify --slug beta-team` passed before writing: all sourceURLs matched, all bodies md5-unique, no junk soft-404s.
- **Structured layer:** homepage JSON-LD was only a `VideoObject`; no Company JSON-LD legalName/sameAs. Nav recovered from the captured `<nav>` and checked against homepage markdown/screenshot.
- **Credits:** 12 Firecrawl credits spent: 1 map + 11 scrapes. Logos were downloaded from homepage-declared asset URLs and measured locally with `sips`/ImageMagick; no additional Firecrawl spend.
- **Couldn't get:** product purchase prices, contract terms, current market data, and filing-level financials; investor page captured links to filings/PDFs but those documents were not scraped.
- **Run profile:** guided - standard profile + `logos:{}` module.
