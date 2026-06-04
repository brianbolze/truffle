---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: airbnb.com
captured_at: 2026-06-04
site_notes: "Platform-feature taxonomy, NOT listing SKUs — Airbnb's real catalog is millions of un-enumerable host listings (a Catalog shape); this roster captures the MARKETED service/feature taxonomy, the layer above the listings. Service TYPES (Photography/Chefs/Prepared meals/Training/Catering/Massage/Makeup/Hair/Spa) live on /services as a type-carousel with stable `service_type_tag` IDs (Tag:89xx), but have NO clean per-type canonical URL — only geolocated /s/<loc>/services?service_type_tag= search refinements; key on the tag, never construct a URL. Which types read 'live' vs 'Coming soon', the 'X available' counts, and all host-set prices are geolocated point-in-time (DC–Leesburg metro this run) — snapshot, re-check next run. New trip-services + AI features are announced off-site at news.airbnb.com/release (linked /release), app-only, no web PDP. Prices are host-set 'From $X' floors + booking minimums (per guest | per group)."
---

## Portfolio overview

**Shape: a `Catalog`-shape marketplace — this roster is the *marketed feature/service taxonomy*, not the inventory.** Airbnb sells access to millions of un-enumerable host listings; what *is* enumerable, and what Airbnb markets, is the platform taxonomy below: three booking verticals, a partner-powered trip-services layer, the AirCover trust programs, the hosting toolset, and a new AI layer. Per the run emphasis, this file captures that taxonomy (the listings themselves are out of scope — they're the un-enumerable leaf).

**Prominence (calibrated):**
- **Homes is the flagship — `[HIGH]`.** It leads the nav, and the entire homepage is a Homes listing grid; Experiences/Services get tabs but the homepage is stays.
- **Experiences & Services are the active push — `[HIGH]`** (own "NEW" badges on both nav tabs; the 2026 Summer Release is largely about them).
- **Trip services + AI features are Summer-Release headliners — `[HIGH]`** (the /release page leads with them), but most are "rolling out later this summer/year" — marketed ahead of full availability.
- **AirCover is the marquee trust feature — `[HIGH]`** ("Only on Airbnb," repeated across guest + host pages).
- **Within Services, Photography leads the type-carousel — `[MED]`** (carousel order, and it had the most "available" in this metro; both are geolocated, so low stability).

## Roster

Two levels: the seven marketed families (Kind `family`), then their leaf types/features (Kind `buyable` = a leaf the guest/host books or switches on; some leaves are bundled-free platform features, priced `Free`). Slugs are attested paths or `(no PDP — …)` where a marketed type has only a geolocated search URL or an in-app surface.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What |
|---|---|---|---|---|---|---|
| Homes | family | — | /homes | — | — | Short-term stays + boutique hotels; host-set nightly price, shown all-fees-included |
| ⤷ Stays | buyable | homes | /homes | $206–$1,375 / 2 nights | published | Entire homes, private rooms, condos, cabins, villas; "Guest favorite" badge; snapshot prices |
| ⤷ Boutique & independent hotels | buyable | homes | (no PDP — /homes; 20 destinations) | $400–$735 / 2 nights | published | "Each hotel is selected by Airbnb, with no big chains"; Price match guarantee; up to 15% Airbnb credit |
| Experiences | family | — | /experiences | — | — | Host-led local activities, per guest; rated "4.93 out of 5" (self-reported) |
| ⤷ Landmarks | buyable | experiences | (no PDP — /experiences category) | From $54 (e.g. Tower of London) | published | "more than 3,000 landmark experiences" with local experts |
| ⤷ Food culture | buyable | experiences | (no PDP — /experiences category) | per guest (host-set) | published | "more than 2,500"; Chef's Table & Grand Central Market partnerships |
| ⤷ FIFA World Cup 2026 | buyable | experiences | (no PDP — /experiences category) | per guest (host-set) | published | Once-in-a-lifetime events across six host cities |
| Services | family | — | /services | — | — | On-demand professional services booked to a location; per guest/group, booking minimums |
| ⤷ Photography | buyable | services | (no PDP — Tag:8949) | From $60–$295 | published | LIVE in metro (24 available). Per guest/group; "Minimum $120–$250 to book" on some |
| ⤷ Chefs | buyable | services | (no PDP — Tag:8950) | From $20–$285 | published | LIVE (13 available). Private chefs; "Minimum $60–$600 to book" on some |
| ⤷ Prepared meals | buyable | services | (no PDP — Tag:8939) | per guest/group | published | LIVE (6 available) |
| ⤷ Training | buyable | services | (no PDP — Tag:8941) | per guest/group | published | LIVE (3 available) |
| ⤷ Catering | buyable | services | (no PDP — Tag:8951) | per guest/group | published | LIVE in metro (1 available) — was "Coming soon" in the 2026-05-30 capture |
| ⤷ Massage | buyable | services | (no PDP — Tag:8942) | — | on-request | "Coming soon" in this metro (live in others — geolocated) |
| ⤷ Makeup | buyable | services | (no PDP — Tag:8952) | — | on-request | "Coming soon" |
| ⤷ Hair | buyable | services | (no PDP — Tag:8944) | — | on-request | "Coming soon" |
| ⤷ Spa treatments | buyable | services | (no PDP — Tag:8943) | — | on-request | "Coming soon" |
| Trip services | family | — | (no PDP — /release, in-app) | — | — | 2026 Summer Release; partner-fulfilled, booked in-app with Airbnb-guest perks |
| ⤷ Grocery delivery | buyable | trip-services | (no PDP — Instacart, in-app) | $0 delivery; $10 off $50+ | partial | Instacart partnership, 25+ US cities; item price is partner-side |
| ⤷ Airport pickups | buyable | trip-services | (no PDP — Welcome Pickups) | 20% off every ride | partial | Welcome Pickups, 160+ cities; driver tracks your flight |
| ⤷ Luggage storage | buyable | trip-services | (no PDP — Bounce) | 15% off | partial | Bounce, 15,000+ locations / 175 cities |
| ⤷ Car rentals | buyable | trip-services | (no PDP — in-app) | 20% credit back (first rental) | partial | In-app discovery; "rolling out later this summer" |
| AirCover | family | — | /aircover | — | — | Free two-sided protection; "Only on Airbnb" |
| ⤷ AirCover for guests | buyable | aircover | /aircover | Free | published | Rebooking or full/partial refund for serious issues; 24-hr safety line; "not an insurance policy" |
| ⤷ AirCover for Hosts | buyable | aircover | /aircover-for-hosts | Free ($3M / $1M cover) | published | Guest ID verification, reservation screening, $3M damage protection, $1M liability, $1M Experiences liability, 24-hr safety line |
| Hosting | family | — | /host/homes | — | — | Supply-side: list + run a home / experience / service |
| ⤷ Airbnb Setup | buyable | hosting | /host/homes | Free onboarding | published | "Hands-on help from a Superhost from your first question to your first guest" |
| ⤷ Co-Host Network | buyable | hosting | /host/co-hosts | host pays co-host | partial | Hire a vetted local co-host to manage a listing |
| AI & planning | family | — | (no PDP — /release, in-app) | — | — | 2026 Summer Release AI layer across the app; bundled, free |
| ⤷ AI review highlights | buyable | ai-planning | (no PDP — /release) | Free feature | published | Synthesizes "over one billion" reviews into what you care about |
| ⤷ AI customer support | buyable | ai-planning | (no PDP — /release) | Free feature | published | "11 languages"; billed "the best AI support assistant in travel"; voice coming |
| ⤷ Shared itinerary + travel map | buyable | ai-planning | (no PDP — /release) | Free feature | published | Group trip planning in the Trips tab; connections/travel map; "later this summer" |

## Verbatim anchors

The footnotes and claims the roster points at (quoted exactly; all self-reported — recorded, not endorsed):

- **Services availability (geolocated, this run = DC–Leesburg metro), with stable type tags:** Photography "24 available" (`Tag:8949`), Chefs "13 available" (`Tag:8950`), Prepared meals "6 available" (`Tag:8939`), Training "3 available" (`Tag:8941`), Catering "1 available" (`Tag:8951`); Massage (`Tag:8942`), Makeup (`Tag:8952`), Hair (`Tag:8944`), Spa treatments (`Tag:8943`) all "Coming soon." *The tag IDs are stable; the live/coming-soon split and counts are not.*
- **Services pricing form:** "From $75/ group," "From $60/ guest" + "Minimum $120 to book," "From $20/ group," "From $285/ guest" + "Minimum $570 to book" — host-set floors with per-listing booking minimums.
- **Trip services (Summer Release):** Grocery — "$0 delivery and $10 off an order of $50 or more … Available in over 25 US cities in partnership with Instacart." Airport — "20% off every ride … Now available in over 160 cities worldwide" (Welcome Pickups). Luggage — "15% off and access to over 15,000 locations in 175 cities" (Bounce). Car rentals — "the first time you rent a car on Airbnb, you'll get 20% credit back."
- **AirCover for Hosts:** "$3M USD" host damage protection, "$1M" liability insurance, plus "$1M Experiences liability insurance," guest identity verification, reservation screening, 24-hour safety line — "Always included, always free."
- **Experiences:** "rating them 4.93 out of 5 stars on average," "more than 3,000 landmark experiences," "more than 2,500 food culture experiences"; Tower of London listed "for $54."
- **Hotels:** "Find a lower price for the same hotel anywhere else, and we'll give you the difference as Airbnb credit"; "Book a featured hotel and you can receive up to 15% credit."
- **Hosting:** earnings estimator "Your home could make $854 on Airbnb" (geolocated).

## Deep blocks

**None earned.** The roster + the geolocated-availability caveat in `site_notes`/anchors carry this company. There's no per-type price ambiguity an FAQ figure resolves (prices are host-set and openly shown), and no PDP-template anatomy was requested for this run.

## Provenance

- **Pages read:** /services (the service-type taxonomy + pricing form), /experiences, /homes, /host/homes, /aircover, /aircover-for-hosts, /release (the 2026 Summer Release — trip services, hotels, AI), homepage — all `store/airbnb-com/captures/2026-06-04/`.
- **Scope:** enumerated = the marketed family/leaf taxonomy (3 verticals + 9 service types + 3 experience categories + 4 trip services + AirCover ×2 + hosting tools + AI features). NOT enumerated = the millions of individual host listings (the un-enumerable `Catalog` leaf — out of scope by design).
- **Gated / unreachable:** host & guest service-fee percentages (not stated on any captured page); per-type canonical URLs (service types exist only as geolocated search refinements — keyed on `service_type_tag`).
- **Point-in-time caveat:** prices, "X available" counts, and the Services live/coming-soon split are a **geolocated snapshot, not fixed** (DC–Leesburg metro, 2026-06-04) — they flicker by location and run.
- **Run profile:** non-vanilla — opt-in `offerings.md` reframed to **platform-feature/service taxonomy** (per the guided emphasis "platform features / services taxonomy"), not listing-SKU grain. `Kind` reads as family/leaf; bundled-free features (AirCover, AI, Airbnb Setup) carry `Free`/`—` prices with `published` visibility. No hero-image capture (a marketplace has no product renders).
