---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: whoop.com
captured_at: 2026-06-24
enumeration: lines-omitted   # membership tiers + Advanced Labs fully rostered; accessories/bands + WHOOP Body apparel (shop.whoop.com) NOT captured — see scope note
site_notes: "Membership prices are annual FLOORS ('Starts at $X/yr') on /membership + each tier page; the real all-in is set at join.whoop.com (not captured). Advanced Labs Comprehensive-Panel prices are on /advanced-labs; its 5 Specialized Panels are PURCHASE-IN-APP ONLY (no web price). Accessories/bands + WHOOP Body apparel live on shop.whoop.com (separate subdomain) — enumerate there next time."
---

## Portfolio overview

WHOOP's catalog is **one product sold three ways plus one add-on**. The flagship is the WHOOP membership — a screen-free wearable bundled into a 12-month subscription — offered in three tiers (**One / Peak / Life**) that differ by device (5.0 vs. medical-grade MG), included accessories, and how deep the health features go. A free 1-month trial (certified pre-owned 5.0) is the funnel entry. The one true companion line is **WHOOP Advanced Labs**, a Quest-powered bloodwork add-on with its own pricing ladder. Bands/apparel (shop.whoop.com) are a real fourth line but sit on a separate subdomain not captured here.

**Prominence** [HIGH]: the three membership tiers are the company's own primary axis — every page leads with the One/Peak/Life comparison table. **Peak** is the most-pushed tier (it's the free-trial default and "Free trial available" badge) [MED]. Within Advanced Labs, the **2-tests/yr Comprehensive Panel** carries WHOOP's own *"MOST POPULAR"* badge [HIGH].

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Membership | family | — | /us/en/membership | — | — | n/a · wearable + 12-mo subscription bundle · DTC, device included |
| WHOOP One | buyable | /us/en/membership | /us/en/one | "Starts at $199/yr" | partial | n/a · WHOOP 5.0 + Basic Charger (wired) + CoreKnit Jet Black band, 12-mo membership · annual floor, all-in at join.whoop.com |
| WHOOP Peak | buyable | /us/en/membership | /us/en/peak | "Starts at $239/yr" | partial | n/a · WHOOP 5.0 + Wireless PowerPack + SuperKnit (Onyx) band, 12-mo membership · adds Healthspan/Stress/Health Monitor |
| WHOOP Life | buyable | /us/en/membership | /us/en/life | "Starts at $359/yr" | partial | n/a · WHOOP **MG** + Wireless PowerPack + SuperKnit Luxe (Titanium) band, 12-mo membership · adds ECG, AFib, BP Insights (beta) |
| Free trial (Peak) | buyable | /us/en/membership | /us/en/whoop-trials | "1-month free trial" | published | n/a · certified pre-owned WHOOP 5.0 + 1-mo Peak membership · free funnel entry |
| WHOOP Advanced Labs | family | — | /us/en/advanced-labs | — | — | blood biomarkers (122+) · Quest in-person draw + clinician review · add-on, requires active membership/trial, US-only |
| Comprehensive Panel — 1 test/yr | buyable | /us/en/advanced-labs | /us/en/advanced-labs | "$199" ("$199 billed annually") | partial | 122+ biomarkers · 1 annual Quest blood test · requires active membership (mandatory separate cost) |
| Comprehensive Panel — 2 tests/yr | buyable | /us/en/advanced-labs | /us/en/advanced-labs | "$349 billed annually" ("$175 per test") | partial | 122+ biomarkers · test every 6 mo · *MOST POPULAR*; requires active membership |
| Comprehensive Panel — 4 tests/yr | buyable | /us/en/advanced-labs | /us/en/advanced-labs | "$599 billed annually" ("$150 per test") | partial | 122+ biomarkers · test every 3 mo · requires active membership |
| Comprehensive Panel — 6 tests/yr | buyable | /us/en/advanced-labs | /us/en/advanced-labs | "$899 billed annually" ("$150 per test") | partial | 122+ biomarkers · most-frequent testing · requires active membership |
| Specialized Panels (×5) | buyable | /us/en/advanced-labs | /us/en/advanced-labs | — | on-request | focused biomarker panels (Heart 81 · Performance 90 · Metabolic 78 · Women's 81 · Men's 77) · *purchase-in-app only*, no web price |

### Verbatim anchors

- **Membership "Starts at" floors** — `/membership` + tier pages: *"Starts at $199/yr"* (One), *"Starts at $239/yr"* (Peak), *"Starts at $359/yr"* (Life). All three → `partial`: the shown number is an annual floor and the checkout all-in is set behind join.whoop.com (not captured). One-page confirms the floor as the real annual figure: *"Professional-grade fitness insights at our best price, at $199/yr… Your purchase includes a 12-month membership."*
- **What's in each tier box** (`/membership` FAQ, verbatim): One = *"WHOOP 5.0 Device, basic charger, and Jet Black CoreKnit band"*; Peak = *"WHOOP 5.0 Device, wireless PowerPack, and an Onyx SuperKnit band"*; Life = *"WHOOP MG Device, wireless PowerPack, and a Titanium SuperKnit Luxe band."*
- **Advanced Labs membership prerequisite** (drives `partial`) — *"WHOOP Advanced Labs is an add-on to your membership"* / *"requires an active WHOOP membership or trial."* The lab fee is fully shown, but using it requires a separate mandatory membership cost → `partial`.
- **Advanced Labs Comprehensive pricing** (`/advanced-labs`, verbatim): 1 test *"$199 / $199 billed annually"*; 2 tests *"$175 per test / $349 billed annually"* (*MOST POPULAR*); 4 tests *"$150 per test / $599 billed annually"*; 6 tests *"$150 per test / $899 billed annually."*
- **Specialized Panels** (`/advanced-labs`) — *"Currently only available for purchase in the WHOOP app"*; biomarker counts per FAQ: Heart 81, Performance 90, Metabolic 78, Women's 81, Men's 77. No web price → `on-request`.
- **Molecule audit:** `not stated` / n/a across the roster — WHOOP sells a wearable + a lab service, not pharmaceuticals; no molecule applies (Advanced Labs measures biomarkers, it does not dispense a drug).

## Deep blocks

None earned — the roster carries this company. The three tiers are a clean feature ladder already captured in the membership comparison; no per-SKU ambiguity needs a verbatim block. (PDP-anatomy block not requested this run.)

## Provenance

- **Pages read:** `/membership`, `/one`, `/peak`, `/life`, `/advanced-labs` (+ homepage for tier framing) — all Firecrawl, /us/en/, captured 2026-06-24 under `captures/2026-06-24/`.
- **Scope note:** Fully enumerated — the 3 membership tiers + free trial, and Advanced Labs (4 Comprehensive cadences + the 5 Specialized Panels as a tier). **Lines omitted (`enumeration: lines-omitted`):** (1) **accessories & bands** + **WHOOP Body Smart Apparel** — sold on **shop.whoop.com**, a separate subdomain not in this capture; (2) **WHOOP Unite / enterprise**, not surfaced on captured marketing pages; (3) **Family Plans / gifting / corporate-gifting** pricing (linked but not captured). Roster count is a **floor**, not WHOOP's full catalog.
- **Gated/unreachable:** live all-in membership checkout (join.whoop.com); Specialized-Panel prices (app-only).
- **Point-in-time caveat:** membership "Starts at" floors and Advanced Labs prices are a 2026-06-24 snapshot; WHOOP runs promos/financing — re-check before quoting.
- **Run profile:** guided — `offerings.md` added to a standard profile capture (membership tiers + Advanced Labs); no emphasis, no hero images, no PDP-anatomy block.
