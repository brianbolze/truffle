---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "2.5"

# Identity
domain: airbnb.com
name: Airbnb
aliases: []
parent: []
owns: []
socials: { instagram: "https://instagram.com/airbnb", x: "https://twitter.com/airbnb", facebook: "https://www.facebook.com/airbnb" }   # from footer anchors (no JSON-LD sameAs); handle "airbnb" verified
external: {}

# Capture meta
captured_at: 2026-06-04
capture_method: firecrawl
site_notes: "Custom React SPA (no Next/Gatsby/Webflow markers, hashed assets). /v2/map returns ~470 URLs but ~95% are /rooms/<id> listings + /help/article + /users/show + /s/<loc> search — near-zero structural signal; derive structure from homepage links (top nav = Homes/Experiences/Services; footer carries Support/Hosting/Airbnb nav + social anchors instagram/twitter/facebook). Homepage + each vertical render geolocated, point-in-time listing/price carousels (US capture localizes to the DC–Manassas–Leesburg metro); listing prices, 'X available' counts, AND which Services show 'live' vs 'Coming soon' all flicker by location/run — treat as a snapshot. The Services TYPE taxonomy itself (Photography/Chefs/Prepared meals/Training/Catering/Massage/Makeup/Hair/Spa treatments) is stable; only availability is geolocated. Logo is an inline data-URI SVG WORDMARK in branding.images.logo (Bélo + 'airbnb', viewBox 3490×1080) → decode to assets/wordmark.svg. Favicon/og come off a0.muscache.com, a CDN that content-negotiates modern formats (the og:image .jpg URL served AVIF to the fetcher). Feature announcements live off-site at news.airbnb.com (homepage links it as /release) — the richest 'what's new' source. Homepage markdown tail repeats the 'Now you'll see one price for your trip, all fees included' banner — strip as noise. A coral login/price-banner modal overlays the homepage screenshot."
key_pages:
  homes: /homes
  experiences: /experiences
  services: /services
  host_homes: /host/homes
  aircover: /aircover
  aircover_hosts: /aircover-for-hosts
  release: /release
unverified_fields:
  - "Scale claims ('8 million vacation rentals', '2 million Guest Favorites', '220+ countries and regions') are homepage meta-description copy; 'over one billion guest and host reviews' and Experiences '4.93 out of 5 average' are 2026 Summer-Release marketing copy — self-reported, not independently verified."
  - "Exact fee percentages (host service fee, guest service fee) are not stated on captured pages — only 'one price for your trip, all fees included' (guest) and AirCover-as-free framing (host)."
  - "Listing/experience/service prices, 'X available' counts, the host-earnings estimate ('make $854'), and which Services read 'live' vs 'Coming soon' are a point-in-time, geolocated snapshot, not fixed — DC-metro localization, flicker run-to-run."

# Description — one sentence: [what they do] + [how] + [focus/differentiator].
description: "A global travel marketplace where independent hosts list short-term stays, local experiences, and on-demand services; hosts set their own prices, Airbnb takes a per-booking fee and backs both sides with AirCover protection."

# Classification — closed sets (see TAXONOMIES.md).
entity_type: Company
target_market: [B2C, B2B2C]
offering_category: [Marketplace / Platform]
portfolio_shape: Multi-product
business_model: Marketplace / Commission
primary_industry: Hospitality & Tourism

# Visual identity — branding payload is a hint; confirmed against screenshot + rawHtml.
logo_url: assets/wordmark.svg
logos:
  wordmark: { src: assets/wordmark.svg, w: 102, h: 32 }                                                          # inline data-URI SVG from branding.images.logo — Bélo + "airbnb", viewBox 0 0 3490 1080
  logomark: { src: "https://www.google.com/s2/favicons?domain=airbnb.com&sz=256", px: 240, transparent: false } # white Bélo on a BAKED coral square (JPG, no alpha) — flag for dark slides
  og:       { src: "https://a0.muscache.com/im/pictures/fe7217ff-0b24-438d-880d-b94722c75bf5.jpg", w: 1200, h: 600 }  # declared og:image (CDN serves AVIF); clean lifestyle cover (glowing dome stay)
brand_colors: { primary: "#FF385C", text: "#222222", background: "#FFFFFF" }   # STRAIN: branding 'accent' #224CA4 is the link blue, not the brand hue; coral #FF385C is the verified identity color
fonts: [Airbnb Cereal, Circular]
color_scheme: light
design_framework: react (custom SPA)   # STRAIN: rawHtml shows no Next/Gatsby/Webflow markers — Airbnb's own front-end stack
---

## Overview

Airbnb is a two-sided online marketplace for travel. Guests search and book; independent **hosts** supply the inventory, set their own prices, and pay Airbnb a fee per booking. Airbnb owns no inventory — its product is the marketplace, the booking/payments rails, and the trust layer (reviews, Guest Favorites, AirCover) that lets strangers transact. As of the **2026 Summer Release** the platform is visibly expanding from "book a stay" toward "book the whole trip": three co-equal verticals lead the top nav — **Homes** (the original, still-dominant short-term-rental business), **Experiences**, and **Services** (the latter two relaunched and pushed hard) — now wrapped in a layer of trip logistics (grocery, airport pickup, luggage, car rental), boutique hotels, and AI planning/support tools.

## What they offer

Three marketplace verticals, each an un-enumerable catalog of host-supplied listings, plus a newer trip-logistics + AI layer. Breadth + shape here; per-line/feature detail in `offerings.md`.

- **Homes:** short-term stays — entire homes, private rooms, condos, cabins, villas — plus newly added **boutique & independent hotels** (launching across 20 destinations). Host-set nightly pricing, displayed all-fees-included (captured DC-metro examples ~$103–$198/night; 2-night totals $206–$1,375). `[published]`
- **Experiences ("NEW"):** host-led local activities, including curated **Airbnb Originals** and the categories Airbnb is scaling — **Landmarks** ("more than 3,000"), **Food culture** ("more than 2,500"), and **FIFA World Cup 2026** tie-ins across six host cities. Per-guest pricing (captured: From $28–$250/guest). `[published]`
- **Services ("NEW"):** on-demand professional services booked to a location. Live in the captured metro: **Photography, Chefs, Prepared meals, Training, Catering**; **Massage, Makeup, Hair, Spa treatments** shown "Coming soon" (the live-vs-coming-soon split is geolocated, not global). Priced per guest or per group, often with booking minimums (captured: From $20–$295/guest, "Minimum $60–$600 to book"). `[published]`
- **Trip services (2026 Summer Release, partner-powered):** booked in-app, fulfilled and priced by partners with Airbnb-guest perks — **Grocery delivery** (Instacart, "$0 delivery and $10 off an order of $50 or more", 25+ US cities), **Airport pickups** (Welcome Pickups, "20% off", 160+ cities), **Luggage storage** (Bounce, "15% off", 15,000+ locations / 175 cities), **Car rentals** (in-app, "20% credit back" on first rental). `[partial]`
- **AirCover for guests:** bundled free on every home booking — rebooking help or a full/partial refund for serious issues (host cancels, unreachable host, listing "significantly different"), plus a 24-hour safety line. Explicitly "not an insurance policy." `[published]`
- **AirCover for Hosts:** "Always included, always free. Only on Airbnb." — guest identity verification, reservation screening, **$3M USD** host damage protection (art & valuables, auto & boat, pet damage, income loss, deep cleaning), **$1M** liability insurance, **$1M** Experiences liability insurance, and a 24-hour safety line. `[published]`
- **Hosting platform:** list a home / experience / service; **Airbnb Setup** (hands-on onboarding from a Superhost), the **Co-Host Network** (hire a local co-host to run your listing), and an earnings estimator ("Your home could make $854" — geolocated). Free to list; Airbnb earns its fee per booking. `[published]`
- **AI & planning layer (Summer Release, rolling out):** AI review highlights (synthesizing "over one billion" reviews), AI-powered wishlist comparison, shared group itinerary, a connections/travel map, and an AI customer-support assistant ("11 languages," billed "the best AI support assistant in travel"). Platform features, not separately priced.

## How it works / model

**Two-sided marketplace on commission.** Guests browse free, book a stay/experience/service, and pay a single all-in price ("one price for your trip, all fees included"); hosts set prices and list for free. Airbnb makes money by taking a **fee per booking** (host- and guest-side service fees — percentages not disclosed on captured pages) and, increasingly, via partner/affiliate economics on the new trip services (Instacart, Welcome Pickups, Bounce, car rentals) and a credit-back loop that recycles spend into future Airbnb stays. The trust layer is the enabling product: identity verification, reviews, **Guest Favorites**, and **AirCover** (free protection on both sides) are what make stranger-to-stranger transactions work. Host acquisition runs through self-serve listing + Airbnb Setup + the Co-Host Network.

## Positioning & audience

Targets leisure and increasingly longer-stay travelers (B2C) and the hosts who supply inventory (B2B2C — individuals, co-hosts, and now boutique hoteliers). Positions against hotels and OTAs (Booking/Expedia) on *uniqueness and locality* — "Experiences you can only get on Airbnb," hotels "with no big chains" — and against pure-stay rivals (Vrbo) on *breadth*: the 2026 Summer Release reframes Airbnb from a stays marketplace toward an end-to-end trip platform. Claimed edge: the two-sided trust layer (AirCover, reviews, Guest Favorites) and a host network no competitor matches.

## Nav structure

Header nav (verified from rawHtml `<header>` + screenshot):

```
- Airbnb homepage (logo) — /
- Search tabs (the primary IA):
  - Homes — /homes
  - Experiences  [NEW] — /experiences
  - Services  [NEW] — /services
- Search bar: Where · When (Add dates) · Who (Add guests)
- Become a host — /become-a-host
- Language & currency selector
- Profile / main navigation menu (account, login/signup — client-rendered)
```

Footer / global links (destinations from the homepage link inventory; group labels follow Airbnb's standard footer — the mega-footer is client-rendered, not in captured markdown):

```
- Support: Help Center /help · AirCover /aircover · Anti-discrimination /against-discrimination ·
  Accessibility /accessibility · Travel insurance /travelinsurance · Community Center /t5/Community-Center ·
  Report neighborhood concern /neighbors
- Hosting: Airbnb your home /host/homes · Host an Experience /host/experiences ·
  Host a Service /host/services · AirCover for Hosts /aircover-for-hosts · Co-Host Network /host/co-hosts ·
  Airbnb-friendly apartments /airbnb-friendly · Hosting resources /resources
- Airbnb: Newsroom /press/news · 2026 Summer Release /release · Careers /careers ·
  Gift cards /giftcards · Refer a host /refer
```

## Credibility & proof

All figures are **self-reported** (homepage meta + Summer-Release marketing copy) — recorded verbatim, not endorsed:

- **Scale:** "8 million vacation rentals," "2 million Guest Favorites," "220+ countries and regions worldwide" (homepage meta); "over one billion guest and host reviews," "millions of hosts."
- **Quality / ratings:** Experiences "4.93 out of 5 stars on average"; per-listing ratings shown across captures cluster 4.7–5.0 (snapshot); the **Guest Favorite** badge and **Superhost** program as on-platform trust marks.
- **AI support:** "the best AI support assistant in travel," "available in 11 languages."
- **Host protection (concrete guarantees):** AirCover for Hosts — "$3M USD" damage protection, "$1M" liability insurance, "$1M" Experiences liability insurance, guest identity verification, reservation screening, 24-hour safety line. Hotels carry a "Price match guarantee" (difference back as Airbnb credit).
- **Partnerships (named):** Instacart, Welcome Pickups, Bounce (trip services); Chef's Table, Grand Central Market (food experiences); FIFA World Cup 2026.

## Visual & brand impression

Mature, confident consumer design. The homepage is a **storefront/app-shell** — a dense grid of rounded-corner listing cards (Popular homes, Featured hotels, then city-by-city carousels), wishlist hearts, and "Guest favorite" badges, carrying little positioning prose (the self-description lives on the vertical and release pages). The palette is restrained white/near-black (#222) with the signature **coral #FF385C** ("Rausch") as the single accent — search button, the Bélo, CTAs. Airbnb Cereal typography, generous whitespace, photography-forward. The top nav animates the Homes/Experiences/Services tabs with small looping videos. A coral modal (the white Bélo + "Now you'll see one price for your trip, all fees included") overlays the capture — a UX nudge toward the all-in pricing change.

## Strategic read

The capture caught Airbnb mid-pivot. For its first ~17 years the product was *stays*; the **2026 Summer Release** is a deliberate widening into a full-trip platform — Experiences and Services elevated to co-equal nav verticals, a new trip-logistics layer (grocery/airport/luggage/car) stitched in via partners rather than built, boutique hotels added to inventory, and an AI layer (review synthesis, comparison, multilingual support) wrapped around the booking flow. The throughline is **owning more of the trip without owning more assets** — Airbnb keeps its asset-light, two-sided-marketplace model and monetizes adjacency through partnerships and a credit-back flywheel that recycles every service purchase into another stay. The defensible core remains the trust layer (AirCover, reviews, Guest Favorites) and the host supply; the open question the release bets on is whether guests will treat Airbnb as a trip *super-app* rather than just a place to book a room.

## Provenance

- **Pages:** 8 analyzed (Firecrawl, 2026-06-04) — homepage + /homes, /experiences, /services, /host/homes, /aircover, /aircover-for-hosts, /release (the news.airbnb.com 2026 Summer Release).
- **Verify:** all 8 sourceURLs matched; all body md5s unique — no geo/cache contamination this run.
- **Credits:** 9 (1 map + 1 homepage rich pass + 7 key pages; logos module reused the cached homepage payload, no new credits).
- **Couldn't get:** exact host/guest fee percentages (not on captured pages); the mega-footer hierarchy (client-rendered, reconstructed from link destinations); founding/company history + financials (off-site, deep-research scope).
- **Run profile:** guided — emphasis "platform features / services taxonomy"; +offerings (platform-feature/service grain, not listing SKUs); +logos. Forced refresh over a still-warm 2026-05-30 capture (prior archived to captures/_archive/).
