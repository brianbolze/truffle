---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: truniagen.com         # company key; each offering's slug (its relative url) is its key within the company
captured_at: 2026-06-16       # own freshness; captures/2026-06-16/ holds the source pages
enumeration: indexed-complete  # full Shopify /products.json registry (14 buyable products) rostered, cross-checked vs homepage mega-nav; only sub-SKU dose/count tiers collapse into a row
site_notes: "Catalog backbone = Shopify /products.json (saved to captures/products_json_registry.json) — authoritative for the SKU list + ONE-TIME prices; cross-checks 1:1 with the homepage mega-nav. The PDP/collections grid renders Subscribe & Save 'From' prices (~10% off the one-time), so a price shows TWO ways (e.g. $49 one-time / 'From $44.10' S&S). NanoCloud's 2-pack price is registry-only (not rendered on any captured .md page) — kept out of the roster $-tokens to stay lint-clean; see Provenance. Prices/prominence are a point-in-time snapshot (Father's-Day promo + a NanoCloud skincare-launch hero rotating the collections grid order)."
---

## Portfolio overview

**One molecule, many forms.** Every Tru Niagen SKU is the parent's patented **Niagen®** — *nicotinamide riboside (NR)* / nicotinamide riboside chloride (NRCl), an NAD⁺ precursor — varied by **dose** (150 / 300 / 1,000 mg), **format** (vegetarian capsule · powder stick pack · topical sachet), and a couple of **actives-added companions** (Beauty, Immune). It is a `Flagship + companions` portfolio, not a multi-molecule catalog: there is no second active ingredient family, so "what's the molecule?" is the same answer for all 14 products. The dose ladders straight to the efficacy claim — **300 mg → "+50% NAD⁺," 1,000 mg → "up to 150% in three weeks."**

**Prominence (calibrated).** The hero **Tru Niagen® 300mg** is the foundational anchor `[MED]` — listed first under "Foundational," called "the original — our minimum daily recommended serving," and carrying by far the most on-site reviews (591). **Pro 1,000mg** leads the homepage product grid as the "clinical-strength" / "superior" serving `[MED]`. **Niagen NanoCloud™** is currently foregrounded out of proportion to its catalog weight `[LOW]` — a top-of-grid slot + a persistent homepage banner — because it's a **new skincare launch** (rotating promo, not durable rank). Bundles and the actives companions (Beauty, Immune) sit lower.

## Roster

14 buyable products (8 single + 6 bundles); dose/count tiers collapse into their product row. One-time price is the verbatim anchor; Subscribe & Save (~10% off) shown where it renders.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Niagen® NR (oral) family** | family | — | — | — | — | Niagen® / nicotinamide riboside · veg capsule & powder · OTC daily supplement |
| Tru Niagen® 300mg | buyable | (oral family) | /products/tru-niagen-300mg | **$49.00 / $127.00 / $244.00** (30/90/180 ct; S&S "From $44.10") | published | NR · veg capsule · "the original," "minimum daily serving"; "increase NAD+ … over 50%" |
| Tru Niagen® Pro 1,000mg | buyable | (oral family) | /products/tru-niagen-1000mg | **$116.00** (60 ct = 30-day @ 2 caps; S&S "From $104.40") | published | NR · two 500 mg veg capsules · "clinical-strength"; "up to 150%" in "three weeks"; NSF Certified for Sport® |
| Tru Niagen® 150mg | buyable | (oral family) | /products/tru-niagen-150mg | **$94.00** (120 ct; S&S "From $84.60") | published | NR · smaller veg capsule · "lowest starter serving" |
| Tru Niagen® 300mg Stick Packs | buyable | (oral family) | /products/tru-niagen-300mg-stick-packs | **$58.00** (30 ct; S&S "From $52.20") | published | NR · powder stick pack · "on the go, plus daily prebiotic support"; NSF Certified for Sport® |
| Tru Niagen® 300mg Stick Packs — 7-pack | buyable | tru-niagen-300mg-stick-packs | /products/tru-niagen-300mg-stick-packs-7-day-supply | **$15.00** (7 ct) | published | NR · powder stick pack · trial size (also given free w/ $50+) |
| Tru Niagen® Beauty | buyable | (oral family) | /products/tru-niagen-beauty | **$49.00** (30 ct) | published | NR (100 mg) + "targeted beauty actives" · veg capsule · once-daily |
| Tru Niagen® Immune | buyable | (oral family) | /products/tru-niagen-immune | **$41.00** (30 ct) | published | NR + immune actives (Vitamin C + Curcumin, per /quality COA names) · capsule |
| Niagen NanoCloud™ | buyable | — | /products/niagen-nanocloud | **$59.00** (1-pack / 30 ct; S&S "From $53.10"); a 2-pack (60 ct) is also offered | published | NR + low-mol-weight hyaluronic acid · waterless water-activated **topical** sachet · skincare; Limited Release, Final Sale |
| Tru Niagen® Whole-Body Benefits Bundle | buyable | — | /products/tru-niagen-whole-body-benefits-bundle | **$130.00** (30/30/30) | published | NR · 300mg + Beauty + Immune capsules · bundle |
| Tru Niagen® Pro Whole-Body Benefits Bundle | buyable | — | /products/tru-niagen-pro-whole-body-benefits-bundle | **$194.00** (30/60/30) | published | NR · Pro 1,000mg + Beauty + Immune · bundle |
| Tru Niagen® 300mg 30ct + Beauty Bundle | buyable | — | /products/tru-niagen-300mg-30ct-beauty-bundle | **$93.00** (30/30) | published | NR · 300mg + Beauty · bundle |
| Tru Niagen® Pro 1,000mg + Beauty Bundle | buyable | — | /products/tru-niagen-1000mg-beauty-bundle | **$156.00** (60/30) | published | NR · Pro 1,000mg + Beauty · bundle |
| Tru Niagen® 300mg 30ct + Immune Bundle | buyable | — | /products/tru-niagen-300mg-30ct-immune-bundle | **$85.00** (30/30) | published | NR · 300mg + Immune · bundle |
| Tru Niagen® Pro 1,000mg + Immune Bundle | buyable | — | /products/tru-niagen-pro-1000mg-immune-bundle | **$148.00** (60/30) | published | NR · Pro 1,000mg + Immune · bundle |

## Verbatim anchors

- **Molecule (uniform, page-attested):** "Niagen®, our patented nicotinamide riboside (NR)" (PDPs); "Niagen® (nicotinamide riboside chloride, or NRCl)" (/pages/quality). No SKU names a second active molecule; Beauty/Immune add unnamed/under-detailed "actives" on top of NR — molecule for those rides as **NR + actives**, not a different molecule.
- **300mg claim:** "Our foundational 300mg daily serving is clinically shown to increase NAD+ levels by over 50% in most individuals." (/products/tru-niagen-300mg)
- **1,000mg claim:** "1,000mg of Niagen® is clinically shown to increase NAD+ levels by up to 150% in as little as three weeks." (/products/tru-niagen-1000mg)
- **Subscribe & Save:** "Your price stays the same, whether you subscribe for a month or 6 months" — the grid "From" price (e.g. "From $44.10 ~~$49.00~~") is the S&S price, ~10% under the one-time. (PDPs / collections)
- **NanoCloud (topical, category departure):** "delivering the same patented NAD+ precursor trusted in Tru Niagen supplements at peak potency … now topically, for the first time"; "Limited Release. Final Sale." Tagged `truemed-ineligible` + `onetime-purchase-only` in the registry (no S&S, no HSA/FSA on this one). (/products/niagen-nanocloud)

## Deep blocks

- **Niagen NanoCloud™ — the only non-oral, non-supplement SKU (earned: a real category + form departure a roster row flattens).** Spine: `/products/niagen-nanocloud`, $59 (1-pack). It is **skincare, not a supplement** — a waterless, "precision-dosed" sachet of Niagen® + low-molecular-weight hyaluronic acid that the user **activates with water at the moment of application** ("With dry hands, place one … sachet in your palm. Apply a dime-sized amount of your favorite water-based serum or moisturizer … onto the sachet"). The verbatim gold is the *why-waterless* mechanism: "NAD+ precursors degrade in water-based formulas, breaking down before they ever reach your skin … Each … sachet keeps Niagen® stable and protected until the moment you activate it." Consumer-test claim: "visibly smoother texture, more even tone … in as few as 2 weeks, with continued improvement through 6 weeks." Commercial posture differs from the supplements: **Limited Release, Final Sale, one-time-purchase-only, HSA/FSA-ineligible** — a small-batch launch from the "Niagen Skincare Innovation Lab," not a staple SKU. Frequency: "1–2x daily."
- **Others:** none earned — the roster + overview carry the oral line (uniform molecule, dose-laddered claims, all prices published).

## Provenance

- **Pages:** /collections/all (rich — prominence read), PDPs tru-niagen-300mg / tru-niagen-1000mg / niagen-nanocloud (molecule · form · claims attestation), homepage + /pages/quality (companion actives, NSF/Alkemist split) — Firecrawl, 2026-06-16. Full SKU list + one-time prices from the Shopify **/products.json** registry (captures/products_json_registry.json).
- **Scope:** `indexed-complete` — all **14** buyable products (8 single + 6 bundles) rostered, the registry cross-checking 1:1 with the homepage mega-nav (two blind sources agree). Sub-SKU dose/count tiers (e.g. 300mg 30/90/180 ct) collapse into their product row by design — leaf detail, not an omitted line.
- **Prices:** one-time/regular prices (registry + struck-through grid price) are the verbatim anchors, all grep-verifiable in captured `.md`. Subscribe & Save "From" prices cited where rendered. **NanoCloud 2-pack price is registry-only** (not on any captured `.md` page) → kept out of the roster as a `$`-token to satisfy the grep-verifiable-price lint; the 60-ct 2-pack exists, priced in products_json_registry.json.
- **Point-in-time:** prices/prominence are a snapshot — a Father's-Day promo (free 7-day Stick Pack w/ $50+) and a NanoCloud skincare launch are rotating the hero/grid; re-check next run.
- **Run profile:** express — `offerings.md` requested explicitly in the invocation ("including offerings.md"), a `deep` override of the project relevance gate (Companies row "Different audience / Low" would otherwise baseline this brand). Vanilla roster otherwise (no images, no PDP-anatomy block).
