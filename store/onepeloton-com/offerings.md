---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: onepeloton.com
captured_at: 2026-06-10
enumeration: indexed-complete
site_notes: "Hardware roster reads cleanly off the marketing PLPs (/exercise-bikes, /treadmills, /row-plus) — each carries its lineup's verbatim prices + the financing footnote; no per-SKU PDP scrape needed for the new lineup. Buy-flow lives at /shop/<sku>. Subscriptions on /membership (compare table) + /app-membership. Apparel is a separate subdomain (apparel.onepeloton.com) — not rostered. Accessories are a long-tail SKU set under /shop/accessories/<id> — noted as a line, not enumerated to leaf. Refurb/promo prices are point-in-time (homepage: $695 refurb Bike ends June 15, 2026)."
---

## Portfolio overview

Peloton's roster splits into **hardware** (one-time purchase) and **memberships** (recurring, and required to use the hardware). Hardware is two series:

- **Cross Training Series** — the current *new* lineup (Bike, Bike+, Tread, Tread+, Row+), all "Powered by Peloton IQ" to varying degrees; the `+` models add the camera/Sonos/fan/hands-free tier. `[HIGH]` prominence — it's the entire new-unit catalog and the homepage hero "latest lineup."
- **Original Series** — the older Bike / Bike+, now sold **refurbished or rental only** (no new units). `[HIGH]` that it's refurb/rental-only — stated explicitly on /exercise-bikes ("Buy refurbished / Rent" is the only option).

Memberships gate everything: **All-Access** ($49.99/mo) for equipment owners; **App One / App+ / Strength+** for the equipment-free funnel. Apparel + accessories are adjacent lines (apparel on its own subdomain). Every hardware price is `[partial]` because the All-Access Membership is a mandatory separate recurring cost; memberships themselves are `[published]`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Cross Training Series | family | — | /exercise-bikes | — | — | New connected bikes/treads/row, Peloton IQ |
| Cross Training Bike | buyable | Cross Training Series | /bike | "Starting at $1,695" | partial | Exercise bike · new · All-Access Membership separate (21.5" tilting screen, manual resistance) |
| Cross Training Bike+ | buyable | Cross Training Series | /bike-plus | "Starting at $2,695" | partial | Exercise bike · new · membership separate (23.8" swivel screen, auto-resistance, camera, Sonos) |
| Cross Training Tread | buyable | Cross Training Series | /tread | "From $3,295" | partial | Treadmill · new · membership separate (21.5" swivel, belt to 12.5% incline) |
| Cross Training Tread+ | buyable | Cross Training Series | /tread-plus | "From $6,695" | partial | Treadmill · new · membership separate (23.8" swivel, slat belt, Free Mode, camera, Sonos) |
| Cross Training Row+ | buyable | Cross Training Series | /row-plus | "As low as $3,495" | partial | Rower · new · membership separate (23.8" swivel, Form Assist, magnetic resistance) |
| Original Series | family | — | /exercise-bikes | — | — | Older bikes, refurbished / rental only |
| Original Bike (refurbished) | buyable | Original Series | /shop/refurbished/bike | "Refurbished from $695" (~~$1,145~~) | partial | Exercise bike · refurbished · membership separate; limited-time, ends June 15, 2026 |
| Original Bike+ (refurbished) | buyable | Original Series | /shop/refurbished/bike-plus | "Refurbished from $1,395 or rent for $124.99/mo" | partial | Exercise bike · refurbished or monthly rental · rental membership included in rental |
| All-Access Membership | buyable | — | /membership | "$49.99/mo" | published | Subscription · required for Bike/Tread/Row owners; all hardware content + household profiles |
| Peloton App+ | buyable | App Membership | /app-membership | "$28.99/mo" or "$289/yr (save $58)" | published | Subscription · no equipment · unlimited classes incl. cardio-equipment + Strength+ |
| Peloton App One | buyable | App Membership | /app-membership | "$12.99/mo" or "$129/yr (save $26)" | published | Subscription · no equipment · full library, 3 cardio-equipment classes/mo |
| Peloton Strength+ | buyable | App Membership | /strength-plus-app | "$9.99/mo" | published | Subscription · standalone gym/strength app, audio-guided, workout generator |
| Apparel | family | — | https://apparel.onepeloton.com/ | — | on-request | Branded performance apparel — separate subdomain, not enumerated |
| Accessories | family | — | /shop/accessories | — | on-request | Shoes, weights, mats, heart-rate bands — long-tail SKUs, not enumerated to leaf |

### Verbatim anchors

- **Membership-separate footnote (decides `partial` on all hardware):** "¹Peloton All-Access Membership required to access all Peloton content and applicable features on your Peloton hardware" (/exercise-bikes, /treadmills, /row-plus, homepage).
- **All-Access price:** "You need an All-Access Membership instead. App+ and Strength+ access is included in your membership for your Bike, Tread, or Row ($49.99/mo)." (/app-membership).
- **App tiers:** "$12.99/mo … or $129/yr (save $26)" (App One); "$28.99/mo … or $289/yr (save $58)" (App+); "$9.99/mo" (Strength+) — /membership compare table.
- **Refurb Bike promo (point-in-time):** "Refurbished from _$695_ ~~$1,145~~" (/exercise-bikes); homepage: "$450 off Refurbished Original Bike … Limited time offer ends June 15, 2026."
- **Refurb Bike+ price discrepancy:** card shows "Refurbished from $1,395 or rent for $124.99/mo" (/exercise-bikes), but the same page's financing footnote ² still bases the refurb Bike+ on "$1,995" ("$166.25/mo … Based on a price of $1,995") — a stale footnote vs. the displayed $1,395 card price. Recorded the displayed price; flagged in `profile.md` `unverified_fields`.
- **Rental:** "Refurbished from $1,395 or rent for $124.99/mo … Membership included in monthly rental³" (/exercise-bikes).
- **Molecule/form note:** N/A — physical fitness equipment + content subscriptions, no molecule axis.

## Deep blocks

None earned — the roster carries this company. Pricing is consistent across the PLPs and the financing footnote (one stale-footnote discrepancy on refurb Bike+, captured in Verbatim anchors); no gated price needs an FAQ-figure rescue, and no disambiguation a roster row can't hold.

## Provenance

- **Pages read:** captures/2026-06-10/ — exercise_bikes.md (Bike/Bike+ new + Original refurb), treadmills.md (Tread/Tread+), row_plus.md (Row+), membership.md (App tiers compare), app_membership.md (All-Access $49.99 + App+/App One), homepage.md (lineup tiles + promo). Every `$` price above is grep-verifiable in a cited capture.
- **Scope note:** `indexed-complete` — all hardware lines (Cross Training ×5 + Original ×2 refurb/rental) and all membership tiers (×4) rostered at SKU grain. **Leaf-omitted by design (not `lines-omitted`):** individual Apparel SKUs (separate subdomain) and the Accessories long-tail (/shop/accessories/<id>) are recorded as lines, not enumerated to leaf — neither is a priced, separately-positioned SKU line the consumer would rank.
- **Point-in-time caveat:** refurbished/promo pricing runs on dated offers ($695 refurb Bike ends June 15, 2026); the new-lineup MSRPs are the durable figures. Re-capture for current promo state.
- **Run profile:** guided — emphasis "logos and offerings"; offerings module added to a standard profile capture. No hero-image capture, no PDP-anatomy block.
