---
schema_version: 1

# Identity
domain: airbnb.com
name: Airbnb
aliases: []
parent: []
owns: []

# Capture meta
captured_at: 2026-05-30
capture_method: firecrawl
site_notes: "Custom React SPA. /v2/map returns ~470 URLs but ~95% are /rooms/<id> listings + /help/article/<n> — near-zero structural signal; derive the offering structure from homepage links instead (top nav = Homes/Experiences/Services; footer carries the full Support/Hosting/company nav). Homepage + each vertical page render geolocated, point-in-time listing/price carousels (US capture localized to the DC–Manassas metro and Wichita, KS); listing prices and 'X available' counts flicker run-to-run — treat as a snapshot, not stable data. Logo is an inline data-URI SVG (the Bélo) → use favicon for logo_url. Homepage markdown tail repeats 'Now you'll see one price for your trip, all fees included' hundreds of times (a total-price-display banner animation) — strip as noise. A login modal overlays the homepage screenshot."
key_pages:
  homes: /homes
  experiences: /experiences
  services: /services
  host: /host/homes
  become_host: /become-a-host
  aircover: /aircover
  aircover_hosts: /aircover-for-hosts
  airbnb_friendly: /airbnb-friendly
unverified_fields:
  - "Scale claims ('8 million vacation rentals', '2 million Guest Favorites', '220+ countries and regions') are homepage meta copy, not independently verified."
  - "Exact fee percentages (host service fee, guest service fee) are not stated on captured pages — only 'we only collect a fee after you've gotten paid' (host) and 'one price, all fees included' (guest)."
  - "All listing/experience/service prices shown are geolocated and point-in-time (a US-metro snapshot); they are not stable values."

description: "A global travel marketplace connecting guests with independent hosts who offer short-term home stays, local experiences, and on-demand services; hosts set their own prices and Airbnb earns a fee on each booking, backing both sides with AirCover protection."

# Classification
entity_type: Company
target_market: [B2C, B2B2C]
offering_category: [Marketplace / Platform]
portfolio_shape: Multi-product
business_model: Marketplace / Commission
primary_industry: Hospitality & Tourism

# Visual identity
logo_url: https://a0.muscache.com/im/pictures/airbnb-platform-assets/AirbnbPlatformAssets-Favicons/original/0d189acb-3f82-4b2c-b95f-ad1d6a803d13.png?im_w=240
brand_colors: { primary: "#FF385C", text: "#222222", background: "#FFFFFF" }   # STRAIN: branding 'accent' #224CA4 is a link blue, not the brand hue; coral #FF385C is the verified identity color
fonts: [Airbnb Cereal, Circular]
color_scheme: light
design_framework: react (custom SPA)   # STRAIN: rawHtml shows React but no Next/Gatsby/Webflow markers — Airbnb's own front-end stack
---

## Overview

Airbnb is a two-sided online marketplace for travel. Guests search and book accommodations and activities; independent **hosts** supply the inventory, set their own prices, and pay Airbnb a fee per booking. As of the 2026 Summer Release the site presents three co-equal verticals in the top nav — **Homes** (the original and still-dominant short-term-rental business), **Experiences**, and **Services** — the latter two newly relaunched and pushed hard. Airbnb itself owns no inventory; its product is the marketplace, the booking/payments rails, and the trust layer (reviews, Guest Favorites, AirCover) that lets strangers transact.

## What they offer

Three marketplace lines, each an un-enumerable catalog of host-supplied listings:

- **Homes** — short-term stays in entire homes, private rooms, condos, cabins, villas, and (newer) partner hotels. The flagship: homepage meta claims "8 million vacation rentals" and "2 million Guest Favorites" across "220+ countries and regions." Priced per night by the host (captured examples: Ocean City homes $530–$889 for 2 nights).
- **Experiences** ("NEW") — host-led activities, including a curated **Airbnb Originals** tier "hosted by the world's most interesting people" (e.g. soccer-pro sessions, FIFA World Cup 26 tie-ins). Per-guest pricing (captured: $12–$250/guest).
- **Services** ("NEW") — on-demand professional services booked to a location: **Photography, Chefs, Massage, Prepared meals, Training** live, with **Makeup, Hair, Spa treatments, Catering** "Coming soon." Priced per guest or per group (captured: chefs from $20–$350/guest, often with a booking minimum; massage from $70/guest).

Per-offering detail belongs in `offerings.md` (not captured at Tier-0).

## How it works / model

**Marketplace / commission.** Hosts list for free, set their own price, and Airbnb collects a service fee — host page: *"Getting started is free. You set your price, and we only collect a fee after you've gotten paid."* Guests now see *"one price for your trip, all fees included"* (a recent shift to total-price-upfront display). The host journey is explicitly de-risked: a free listing flow with 1-1 mentor support, and a new **co-host** marketplace where an owner can hire a "high-quality, local co-host" to create the listing or run hosting entirely.

Adjacent programs widen the host funnel:
- **Airbnb-friendly apartments** — a partnership with US/UK apartment-building owners so renters can host part-time in approved buildings ("Rent a place to live. Airbnb it part-time."). Airbnb does not own or operate the buildings; it's a B2B2C lead-gen partnership (testimonial cites a host earning avg "$13,799 per year").
- An earnings estimator on the host page ("Your home could make $854… 7 nights · $122/night") converts intent.

## Positioning & audience

Two audiences, one platform. **Guests** are pitched on breadth and trust ("an Airbnb for every kind of trip"); **hosts** on low-friction, low-risk income. The 2025–26 expansion from Homes into Experiences and Services reframes Airbnb from "where you stay" toward "what you do on the trip" — competing less with hotels alone and more with activity/booking platforms (Viator, GetYourGuide) and local-services apps. The co-host marketplace and Airbnb-friendly program attack the supply side, lowering the bar to becoming a host.

## Nav structure

```
- [Top nav]
  - Homes — /homes
  - Experiences (NEW) — /experiences
  - Services (NEW) — /services
- Support (footer)
  - Help Center — /help/home
  - Get help with a safety issue — /help/contact-us
  - AirCover — /aircover
  - Travel insurance — /travelinsurance
  - Anti-discrimination — /against-discrimination
  - Disability support — /accessibility
  - Cancellation options — /help/article/2701
  - Report neighborhood concern — /neighbors
- Hosting (footer)
  - Airbnb your home — /host/homes
  - Airbnb your experience — /host/experiences
  - Airbnb your service — /host/services
  - AirCover for Hosts — /aircover-for-hosts
  - Hosting resources — /resources
  - Hosting responsibly — /help/responsible-hosting
  - Airbnb-friendly apartments — /airbnb-friendly
  - Join a free hosting class — /e/intro-to-hosting
  - Find a co-host — /host/co-hosts
  - Refer a host — /refer
- Airbnb (footer)
  - 2026 Summer Release — /release
  - Newsroom — /press/news
  - Careers — /careers
  - Gift cards — /giftcards
```

## Credibility & proof

- **AirCover** — the headline trust layer, dual-sided. *AirCover for guests* (free on every home booking) promises rebooking or full/partial refund if a host cancels, is unreachable, or the listing is "significantly different than advertised," plus a 24-hour safety line; *AirCover for Hosts* covers the supply side.
- **Reviews + Guest Favorites** — near-ubiquitous star ratings (4.7–5.0 on captured cards) and a "Guest favorite" / "2 million Guest Favorites" badge program signal vetted quality.
- **Scale as proof** — "8 million vacation rentals," "220+ countries and regions," "Join millions of hosts."
- Publicly traded (investors.airbnb.com / SEC filings surfaced in the map), reinforcing institutional credibility.

## Visual & brand impression

Polished, photography-forward, and unmistakably mature. The homepage is a clean white canvas filled with dense, region-grouped grids of rounded-corner listing photos — the imagery (the homes, the food, the experiences) *is* the brand; chrome is minimal. The signature **Rausch coral (#FF385C)** anchors the search bar, the heart/Bélo logo, and primary CTAs against near-black (#222222) text. Typography is the proprietary **Airbnb Cereal** (a Circular derivative), reinforcing a friendly-but-premium, design-led identity. The captured shot has a coral-buttoned login modal overlaid mid-page.

## Strategic read

The capture catches Airbnb mid-pivot. For its entire history "Airbnb" meant Homes; the 2026 Summer Release elevates **Experiences** and **Services** to co-equal nav tabs — a deliberate bet to monetize the whole trip, not just the bed, and to turn its host base and guest demand into a broader local-commerce platform. Two supply-side plays reinforce it: the **co-host marketplace** (removes the effort barrier) and **Airbnb-friendly apartments** (removes the ownership barrier). The simultaneous move to all-in total pricing is a direct response to years of "hidden cleaning fee" backlash. Watch whether Experiences/Services gain real liquidity or stay thin (several Services categories are still "Coming soon," and Experiences leans on subsidized Originals).

## Provenance

- **Pages analyzed (7, all Firecrawl, `maxAge:0` + US geo, 2026-05-30):** homepage, `/homes`, `/experiences`, `/services`, `/host/homes`, `/aircover`, `/airbnb-friendly`. All 7 verified: sourceURL-matched and body-md5-unique (no geo/cache contamination).
- **Discovery:** map returned ~470 URLs but ~95% were `/rooms/<id>` + `/help/article/<n>` noise; offering structure came from homepage top-nav + footer links.
- **Not captured:** exact fee percentages, host onboarding flow behind `/become-a-host`, and the full Experiences/Services catalogs (geolocated, point-in-time). Financials/funding are a deep-research job, not Tier-0.
