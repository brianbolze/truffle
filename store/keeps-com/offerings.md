---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: keeps.com           # company key; each offering's slug (its relative url) is its key *within* Keeps
captured_at: 2026-06-04     # own freshness; captures/2026-06-04/ holds the source pages
enumeration: indexed-complete   # all /our-products index cards rostered w/ verbatim prices + both ED PDPs; only un-priced LEAVES noted (shampoo+conditioner bundle PDP, quiz-gated ED compounds) — see Provenance
site_notes: "One catalog, on the WordPress-free Next.js marketing site. The /our-products index card grid carries per-SKU prices VERBATIM as 'list promo' (e.g. '$50 $33.33' = the 'up to 1 month FREE with a 3-month plan' offer), so the hair roster comes off ONE rich --homepage scrape of /our-products — no per-SKU PDP needed for price. EXCEPT: (1) ED prices are PDP-only ('starting from $X/dose'), not on /condition/ed; (2) the homepage 'Half the cost' table gives a parallel per-MONTH framing (finasteride $25/mo, minoxidil $10/mo) that doesn't fully reconcile with the per-shipment card prices — quote both, normalize neither; (3) the 4 NEW Chew/Drop 'X-in-1' compounds + chew-3-in-1 + daily-hair-defense are homepage/nav-linked but ABSENT from the /map (pull from homepage links). Compounded 'Powerhouse 3-in-1'/'Triple-action' ED are homepage-featured but quiz-gated (no public slug/price). Prices billed every 3/6/12 mo; 'price not guaranteed'; possible SPA personalization → treat order/promo as point-in-time."
---

## Portfolio overview

Keeps (keeps.com; a **Thirty Madison** company) is a **men's hair-loss-first** DTC telehealth brand with a smaller
**sexual-health (ED)** companion line, an OTC styling range, and a supplement — a `Multi-product` shape dominated by
one franchise. Every line sells the same way: a **provider-gated online consultation** confirms the plan, then
treatment ships on a **3/6/12-month subscription** "at half the cost of your local pharmacy." This roster enumerates
the full **/our-products** catalog (prices read verbatim off the index cards) plus the two ED PDPs; the only un-priced
leaves are the shampoo+conditioner bundle (PDP not scraped) and the quiz-gated compounded ED options.

**Shape finding #1 — two co-existing price framings, both real.** The same med is quoted two ways: a **per-shipment
card price** on /our-products as `list promo` (the promo = the "up to 1 month FREE with a 3-month plan" discount; e.g.
Finasteride `$80 $53.33`, Minoxidil Foam `$50 $33.33`) **and** a **per-month** figure in the homepage "Half the cost"
table (Finasteride **$25/mo**, Minoxidil **$10/mo**). They don't cleanly reconcile (cadence + promo math), so both are
quoted verbatim and neither is normalized. All shown prices are `published`; medications are then billed every 3/6/12
months and "price not guaranteed."

**Shape finding #2 — the up-market move is compounded "X-in-1" formulas.** On top of the cheap commodity generics
(finasteride, minoxidil), Keeps now leads the catalog with **four new proprietary multi-ingredient prescription
compounds** — **Chew+ 5-in-1 `$149`**, **Chew 3-in-1 `$129.99`**, **Drop+ 11-in-1 `$174.99`**, **Drop 4-in-1
`$159.99`** (dutasteride or finasteride + minoxidil + "supporting ingredients") — plus a compounded **Minoxidil+ Spray
`$135 $108`** (minoxidil + caffeine + tretinoin + melatonin). These are 3–7× the price of the single generics and are
the grid's and the nav's lead items.

**Shape finding #3 — compounding is page-attested on the spray, inferred-but-not-worded on the combos.** Only the
**Minoxidil+ Spray** PDP/card uses the word *"compounded"* verbatim. The Chew/Drop "X-in-1" products are described as
*"prescription chew/drop combining [actives]"* — de-facto compounded combination Rx, but the card copy doesn't say
"compounded." Molecules are page-attested throughout (dutasteride, finasteride, minoxidil, biotin); the ED compounds'
molecules are **not stated**.

**Shape finding #4 — a thin, $5 provider layer, not a membership.** There is **no membership wrapper** (unlike Hone).
Each product is bought à la carte on its own cadence; the only recurring service charge is the consult: **"first visit
free, $5 per visit thereafter,"** plus "unlimited medical provider messaging for one year."

**Prominence (calibrated).** **Hair loss is the flagship [HIGH]** — the hero ("Keep your hair. Regrow what you lost."),
the page title ("Hair Loss Treatment for Men | Keeps"), the first nav category, and the founding mission are all
hair-loss. **The new Chew/Drop "X-in-1" compounds lead the catalog [HIGH]** — they occupy the top 4 cards of both the
/our-products grid and the Hair Loss mega-dropdown, plus a dedicated homepage "Hair loss treatment got an upgrade"
band. **Sexual health/ED is a secondary companion [MED]** — branded "New to Keeps," the second nav category, no
homepage hero dominance. **Cosmetics + supplement are the tail [LOW]**. **Exact card order is [LOW]** — Next.js SPA,
possible personalization; treat ordering + the promo prices as a point-in-time snapshot.

## Roster

Complete at the indexed (card) level. Within-company key = **Slug** (the relative URL, quoted exactly). Price quoted
verbatim as shown on the card (`list promo`) or PDP; the per-month homepage figure is added where the "Half the cost"
table gives one. Molecule/form is **page-attested only** (card copy or PDP), never inferred from the product name. An
offering here is never asserted equal to a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| **Hair Loss — single-agent** | family | — | `/hair-loss` | — | — | The FDA-approved commodity molecules + the prescription shampoo. |
| Finasteride | buyable | Hair Loss — single-agent | `/our-products/finasteride` | `$80 $53.33` (homepage: `$25/mo`) | published | **finasteride** ("generic Propecia®") · oral tablet (90 tablets) · Rx, provider-gated. "FDA-approved to prevent hair loss and boost regrowth." |
| Minoxidil Foam, 5% | buyable | Hair Loss — single-agent | `/our-products/minoxidil-foam` | `$50 $33.33` (homepage: `$10/mo`) | published | **minoxidil 5%** ("generic Rogaine®") · topical foam · **OTC** (no Rx label). Regrowth at the crown. |
| Minoxidil Solution, 5% | buyable | Hair Loss — single-agent | `/our-products/minoxidil-solution` | `$33 $22` | published | minoxidil 5% · topical liquid solution · **OTC**. Equally effective alternative to the foam. |
| Minoxidil+ Spray | buyable | Hair Loss — single-agent | `/our-products/minoxidil-spray` | `$135 $108` | published | **minoxidil + caffeine + tretinoin + melatonin** — "an all-in-one **compounded** spray" · once-daily topical spray · Rx, provider-gated. [anchor: compounded] |
| Ketoconazole Shampoo, 2% | buyable | Hair Loss — single-agent | `/our-products/ketoconazole` | `$33 $22` | published | **ketoconazole 2%** · Rx shampoo, used 2–3×/week · provider-gated. Dandruff, itchiness, flaking. |
| **Hair Loss — compounded "X-in-1"** | family | — | `/our-products` | — | — | The up-market multi-ingredient prescription combos — the catalog's lead items (all flagged "New"). |
| Chew+ 5-In-1: Dutasteride & Minoxidil | buyable | Hair Loss — compounded "X-in-1" | `/our-products/chew-plus-5-in-1-dutasteride-and-minoxidil` | `$149` | published | **dutasteride + minoxidil + "essential hair nutrients"** · oral chew · Rx, provider-gated. "5-in-1 prescription chew." [New] |
| Chew 3-In-1: Finasteride & Minoxidil | buyable | Hair Loss — compounded "X-in-1" | `/our-products/chew-3-in-1-finasteride-and-minoxidil` | `$129.99` | published | **finasteride + minoxidil + biotin** · oral chew · Rx, provider-gated. "3-in-1 prescription chew." [New] |
| Drop+ 11-In-1: Dutasteride & Minoxidil | buyable | Hair Loss — compounded "X-in-1" | `/our-products/drop-plus-11-in-1-dutasteride-and-minoxidil` | `$174.99` | published | **dutasteride + minoxidil + "supporting ingredients"** · topical drop · Rx, provider-gated. "11-in-1 topical drop." [New] The catalog's priciest SKU. |
| Drop 4-In-1: Finasteride & Minoxidil | buyable | Hair Loss — compounded "X-in-1" | `/our-products/drop-4-in-1-finasteride-and-minoxidil` | `$159.99` | published | **finasteride + minoxidil + "supporting ingredients"** · topical drop · Rx, provider-gated. "4-in-1 topical drop." [New] |
| Topical Finasteride and Minoxidil Gel | buyable | Hair Loss — compounded "X-in-1" | `/our-products/topical-finasteride-and-minoxidil` | `$180 $120` | published | **finasteride + minoxidil** · two-in-one topical gel · Rx, provider-gated. "Stimulates regrowth and reduces hair loss." |
| Finasteride & Minoxidil (combo) | buyable | Hair Loss — compounded "X-in-1" | `/our-products/finasteride-minoxidil-foam` · `/our-products/finasteride-minoxidil-solution` | `$130 $86.66` (plan-builder widget) | published | **finasteride (oral) + minoxidil (foam or solution)** · combined plan · Rx, provider-gated. The "Overall Thinning" popular plan; minoxidil type selectable. |
| **Hair — OTC cosmetics & supplement** | family | — | `/our-products` | — | — | Non-Rx styling/care + a hair supplement; ungated. |
| Keeps Thickening Shampoo | buyable | Hair — OTC cosmetics & supplement | `/our-products/thickening-shampoo` | `$22 $17.60` | published | OTC shampoo · "keep follicles clean and help hair look fuller." Ungated. |
| Keeps Thickening Conditioner | buyable | Hair — OTC cosmetics & supplement | `/our-products/thickening-conditioner` | `$22 $17.60` | published | OTC conditioner · "strengthen hair cuticles." Ungated. |
| Thickening Pomade | buyable | Hair — OTC cosmetics & supplement | `/our-products/thickening-pomade` | `$25 $20` | published | OTC styling pomade · "thicker, fuller-looking hair." Ungated. |
| Thickening Shampoo + Conditioner (bundle) | buyable | Hair — OTC cosmetics & supplement | `/our-products/thickening-shampoo-conditioner` | — (PDP not captured) | published | OTC bundle of the two thickening items · price on its PDP (not scraped this run). |
| Daily Hair Defense Supplement | buyable | Hair — OTC cosmetics & supplement | `/our-products/daily-hair-defense-supplement` | `$81` | published | **daily vitamins + saw palmetto** ("doctor-formulated mega mix") · oral supplement · OTC, ungated. |
| **Sexual Health (ED) — "New to Keeps"** | family | — | `/condition/ed` | — | — | The companion men's-health line; two FDA-approved generics + quiz-gated compounded options. |
| Sildenafil Citrate | buyable | Sexual Health (ED) | `/our-products/sildenafil-citrate` | `starting from $3.20/dose` | partial | **sildenafil citrate** ("generic Viagra®", 25/50/100 mg) · oral, as-needed (30 min–4 hr before) · Rx, quiz-gated. Per-dose floor → real price set by dose/plan at consult. [anchor: ed-dose] |
| Tadalafil | buyable | Sexual Health (ED) | `/our-products/tadalafil` | `starting from $4.80/dose` | partial | **tadalafil** ("generic Cialis®", 2.5/5/10/20 mg) · oral, daily or as-needed · Rx, quiz-gated. Per-dose floor → real price at consult. [anchor: ed-dose] |
| Powerhouse 3-In-1 | buyable | Sexual Health (ED) | (no PDP — quiz-gated; homepage-featured) | — | on-request | molecule **not stated** ("our most powerful ED treatment, in one daily dose"; compounded) · daily · behind /sh-condition-routing. |
| Triple-action by design | buyable | Sexual Health (ED) | (no PDP — quiz-gated; homepage-featured) | — | on-request | molecule **not stated** ("Brain, body, and blood flow — covered in one daily dose"; compounded) · daily · behind /sh-condition-routing. |
| **Provider care** | family | — | — | — | — | The thin service layer that gates every Rx SKU (no membership). |
| Provider Consultation | buyable | Provider care | (no PDP — funnel: `/quiz`) | `First visit free` · `$5 per visit` thereafter | published | provider review of the online consultation + "unlimited medical provider messaging for one year." Gates all Rx; not a membership. |

**Buyable count (in scope): 21** — 5 hair single-agent (3 Rx + 2 OTC) + 6 compounded "X-in-1" combos + 5 OTC
cosmetics/supplement (incl. the un-priced bundle) + 4 ED (2 priced PDPs + 2 quiz-gated compounds) + 1 provider
consult. `family` rows are non-buyable groupings, not counted.

### Verbatim anchors

The footnotes the Price/Visibility columns point at — quoted exactly from the cited captures.

- **[anchor: half-the-cost] The homepage per-month framing (verbatim, homepage "Half the cost" table):**
  *FINASTERIDE (Rx) Generic Propecia® — Other guys $65/mo — Keeps $25/mo* · *MINOXIDIL (OTC) Generic Rogaine® —
  Other guys $18/mo — Keeps $10/mo* · *PROVIDER CONSULTATION — Other guys $100+ per visit — Keeps First visit free,
  $5 per visit thereafter.* This is the only per-month framing; the /our-products cards use per-shipment `list promo`
  pricing instead.
- **[anchor: promo] The card price model (verbatim):** the site-wide banner reads *"Get up to 1 month FREE with a
  3-month plan,"* and each card shows a struck list price + a discounted price (e.g. *"$50 $33.33," "$180 $120," "$135
  $108"*) under *"DELIVER EVERY: 3 months / 6 months / 12 months."* The our-products footnote: *"Medication cost may
  vary based on prescribed treatment, **price not guaranteed**. Medications shipped and billed every 3, 6 or 12
  months… Additional costs apply."* → all shown numbers are `published` but promo-dependent and a point-in-time snapshot.
- **[anchor: compounded] Compounded attestation (verbatim):** only **Minoxidil+ Spray** is worded "compounded" —
  *"An all-in-one compounded spray with clinically-backed minoxidil, caffeine, tretinoin, and melatonin."* The
  Chew/Drop "X-in-1" products read *"prescription chew/drop combining [dutasteride/finasteride], minoxidil, and
  [biotin / essential hair nutrients / supporting ingredients]"* — combination Rx, but the word "compounded" is **not**
  on those cards (recorded as combination, not asserted "compounded").
- **[anchor: ed-dose] ED dose + price (verbatim, the PDPs):** Sildenafil — *"starting from $3.20/dose"*; tablets
  *"25mg, 50mg, & 100mg, Rx only,"* "take as needed… 30 minutes to 4 hours before." Tadalafil — *"starting from
  $4.80/dose"*; tablets *"2.5mg, 5mg, 10mg, & 20mg, Rx only,"* "daily or as needed." Both are per-dose floors with the
  real total set by dose/plan at the (quiz-gated) consult → `partial`. No price appears on /condition/ed.
- **Molecule sourcing (page-attested only):** finasteride ("generic Propecia®"), minoxidil ("generic Rogaine®"),
  dutasteride (named in the Chew+/Drop+ titles), biotin (Chew 3-in-1), ketoconazole, sildenafil citrate ("generic
  Viagra®"), tadalafil ("generic Cialis®"), saw palmetto (supplement) — all attested in card/PDP copy. **Powerhouse
  3-in-1 and Triple-action molecules are NOT stated** (compounded, ingredients not public) → recorded "not stated."
- **Gating (verbatim):** *"A licensed medical provider will confirm it's everything you need"* (hair); *"Your private
  online consultation is reviewed by a licensed medical provider to see if treatment is medically appropriate"* (ED);
  *"Services not offered in every state. Medications prescribed only if clinically appropriate, based on completion of
  the required consultation."*

## Deep blocks

*None earned — the roster carries this company.* The catalog is shallow and the per-SKU facts (molecule, form, price,
Rx/OTC, New) all fit a roster cell; no verbatim H1 / price-footnote / disambiguation resolves an ambiguity a row can't.
(The PDP-anatomy archetype is opt-in and wasn't requested this run.)

## Provenance

- **Pages read (all `captures/2026-06-04/`):** `/our-products` (rich `--homepage` pass — the price-bearing index +
  prominence), homepage (the "Half the cost" per-month table + the new-compounds band), `/condition/ed` (ED line +
  doses), `/about-us` (model), `/hair-loss` (line framing), and 2 ED PDPs `pdp_sildenafil-citrate`, `pdp_tadalafil`
  (the "starting from $X/dose" floors). Context: `store/keeps-com/profile.md`. All verified — sourceURLs match, bodies
  md5-unique. **8 credits** (shared with the profile capture — same pages).
- **Scope — enumerated:** the full `/our-products` catalog at card grain (every card rostered with its verbatim price)
  + both ED PDPs. **Un-priced leaves (noted, not whole lines → `indexed-complete` holds):** (1) the
  **Thickening Shampoo + Conditioner bundle** (`/our-products/thickening-shampoo-conditioner`) — its PDP wasn't scraped,
  so price is uncaptured; (2) the **quiz-gated compounded ED** ("Powerhouse 3-in-1," "Triple-action") — homepage-featured
  but no public slug or price (behind `/sh-condition-routing`), rostered `on-request`. Hair-loss condition sub-pages
  (`/hair-loss/receding-hairline`, `/balding-at-crown`, `/male-pattern-baldness`) are SEO/condition content, not SKUs —
  not rostered.
- **Gated / unreachable:** the actual prescribed price for any Rx (set at the provider-reviewed consult / quiz); the
  ED compound molecules + prices; the all-in for a given cadence (3/6/12-mo billing, "price not guaranteed").
- **Point-in-time snapshot, not fixed:** card prices are promo prices (the "1 month free on a 3-month plan" offer) and
  "price not guaranteed"; the Next.js SPA may personalize ordering. Re-capture before trusting a price as current —
  `captured_at` + a short freshness TTL are the guard.

### Run profile

Express `/research-company` invocation (intent carried; step-2.5 batch skipped) with `+offerings.md` enabled alongside
`+telehealth.md` and `+logos`. Roster built off the single price-bearing `/our-products` index (no per-hair-SKU PDP
needed — prices are on the cards) plus the two ED PDPs for their per-dose floors. No opt-in PDP-anatomy block or hero
images requested.
