# Market Read

## Question

For a shopper comparing premium DTC brands that sell **one-time catalog products**
(Warby Parker, Nike, Therabody, Hyperice), how does the captured store represent a
**transactional** purchase — catalog breadth, price visibility, and offer structure — and
does Truffle's telehealth-subscription-shaped State frame leave a physical-retail buyer
able to comparison-shop, or blind?

Value-read (mixed). Builder lens: whether durable State built around subscription-DTC
telehealth generalizes to one-time physical-retail commerce. Store-only.

## Result

**The frame carries the transactional buyer for *price and breadth*, but goes silent on
the rest of a retail purchase decision — returns, warranty, channel, FSA/HSA — which is
captured richly in prose and nowhere in a structured field a buyer can diff across brands.
"No new primitive needed" holds; the shortfall is a fielding gap, not a frame break.**

**(1) Where the frame works cleanly (price + revenue shape).**
- `business_model: Transactional / One-time` is accurate and discriminating for all four
  (C1) — it correctly separates these from the subscription telehealth default and from
  the hybrid wearables (Oura/Peloton, run 037/043). No strain on any of the four.
- **Per-SKU price is reachable and `[published]`** for the core consumer-hardware lines.
  All four have an active `offerings.md` roster (the telehealth-cohort opt-in has been
  extended to consumer goods), so a buyer gets verbatim prices per SKU, not just a family
  floor: Therabody Theragun Relief `$99.99`, PRO Plus `$549.99`; Hyperice Hypervolt Go 2
  `$109`, Normatec 3 Full Body `$1,349`; Warby frames `$95`; Nike Hyperboot `$699.97`
  (C2). The price-visibility token does its job at the line/SKU grain.
- **The token correctly flags the non-buyable legs.** Every one of the four has a
  secondary `[on-request]` leg — Warby eye exams + Rx contacts, Therabody *Reset*
  in-person services + *Coach* app + corporate gifting, Nike (free) Membership, Hyperice
  team/B2B sales. The per-line token marks each as un-priceable without inventing a
  misleading company-level "transparency" scalar. This **corroborates the per-line-token,
  not-company-scalar principle** (cousin to L006) on a fresh entity type.

**(2) Where the buyer goes blind (the retail decision beyond price).** A catalog shopper
weighs more than price: return window, warranty, shipping threshold, payment options
(FSA/HSA, Klarna/Afterpay), and channel (online vs in-store vs Best Buy pickup). **All
four profiles capture these — but only in `How it works / model` and `Credibility & proof`
prose, never in a structured field.** Concretely, the buyer who wants to compare
purchase-protection across the four must read four prose blocks to assemble:
  - **Returns:** Warby 30-day free · Therabody returns (footer link, window not quoted) ·
    Nike 60-day for Members · Hyperice 30-day.
  - **Warranty:** Hyperice 1-year (stated) · others not quoted in the captured prose.
  - **Free-shipping threshold:** Warby free · Nike $50+ (Members) · Hyperice $49+ ·
    Therabody not quoted.
  - **FSA/HSA:** Warby yes · Therabody yes (Flex) · Hyperice yes · Nike not surfaced.

  There is **no structured handle** for any of these, so a 4-brand purchase-protection
  table cannot be drawn from frontmatter or `offerings.md` — only hand-assembled from
  prose, unevenly (several cells are "not quoted"). This is the consumer-goods analog of
  run 045's agency finding: *the body carries the decision, the structured spine does
  not.* It recurs here on a cohort whose price the spine **does** carry, which sharpens it
  — the gap is specifically the **non-price retail factors**, not pricing.

**(3) Catalog-breadth comparison is uneven by construction.** `portfolio_shape` is the
only structured breadth handle, and `Catalog` explicitly means *un-enumerable* — so
breadth lives in `offerings.md`, whose enumeration scope **varies across the four**:
Hyperice rostered all 65 Shopify handles (`Multi-product`); Therabody rostered the full
indexed storefront; **Nike's `offerings.md` enumerated only its recovery/wellness line**
(the rest of the catalog is parked in `unverified_fields`); Warby is `Catalog` (shape +
exemplars, hundreds of styles un-enumerated). A buyer asking "who has the widest line"
gets a **coverage artifact, not a market fact** — Nike looks narrow only because the
capture scoped to recovery. Per L005's corollary: structured/rostered absence ≠ market
absence.

## Gap Map

| Buyer need | Structured handle? | Where it actually lives | Verdict |
|---|---|---|---|
| Revenue shape (one-time vs subscription) | **Yes** — `business_model` | frontmatter | Clean, discriminating |
| Per-SKU price | **Yes** — `offerings.md` + `[published]` token | offerings roster / body | Reachable for the consumer line |
| Can I even get a price (per line) | **Yes** — price-visibility token | body lines | Works; flags `[on-request]` legs |
| Catalog breadth | Partial — `portfolio_shape` (coarse) | offerings.md (uneven scope) | Comparable only where enumeration matches |
| Returns / warranty / shipping threshold | **No** | prose only | Buyer must hand-read 4 blocks; cells often "not quoted" |
| Payment (FSA/HSA, BNPL) | **No** | prose only | Same |
| Channel (online / in-store / retail pickup) | **No** (omnichannel in prose) | prose only | Same |
| Current vs sale price | **No freshness flag in frontmatter** | offerings note | Therabody/Hyperice captured mid-sale; trap |

## Evidence Used

All store-only; no external/current claims. Store clocks govern: Warby `captured_at:
2026-06-04`; Nike / Therabody / Hyperice `captured_at: 2026-06-24`.

- **C1** — `business_model: Transactional / One-time` present in all four `profile.md`
  frontmatter (`store/{warbyparker-com,nike-com,therabody-com,hyperice-com}/profile.md`).
- **C2** — per-SKU `[published]` prices: `store/therabody-com/offerings.md` Roster (Theragun
  $99.99–$549.99); `store/hyperice-com/offerings.md` / profile.md (Hypervolt $109–$299,
  Normatec to $1,349); `store/warbyparker-com/profile.md` ($95 frames); `store/nike-com/
  offerings.md` (Hyperboot $699.97).
- **C3** — `[on-request]` secondary legs: Warby exams/contacts (profile.md "What they
  offer"); Therabody Reset/Coach/corporate (profile.md + offerings.md `on-request` rows);
  Nike free Membership (profile.md "How it works"); Hyperice team sales (profile.md).
- **C4** — retail factors in prose only: returns/warranty/shipping/FSA-HSA quoted in each
  profile's "How it works / model" + "Credibility & proof"; no frontmatter or offerings
  field carries them (grep: no `warranty`/`returns`/`shipping` schema key).
- **C5** — uneven enumeration: `store/nike-com/profile.md` `unverified_fields` ("only the
  Recovery/Wellness line was enumerated this run"); `store/hyperice-com/offerings.md`
  (65 handles); `store/therabody-com/offerings.md` `enumeration: indexed-complete`.
- **C6** — sale-snapshot pricing: `store/therabody-com/offerings.md` + profile.md
  site_notes ("Prime Day sale… re-check before ranking"); `store/hyperice-com/profile.md`
  unverified_fields ("Prime Day sale… point-in-time snapshot").

## Companies Seen

warbyparker.com, nike.com, therabody.com, hyperice.com (the seed Transactional cohort).
Other store `business_model: Transactional` brands noted but out of scope: apple, ford,
casio, swatch, rolex, patek, audemarspiguet, alange-soehne, cartier (luxury watches
covered in run 033), plus several telehealth/pharmacy one-off-purchase entities
(anazaohealth, hallandalerx, millspharmacy, prohealth, defymedical, etc. — a different,
clinical-supply shape, not consumer catalog retail).

## Missing / Stale Coverage

- **Nike** catalog is enumerated only for the recovery/wellness line; the broad
  footwear/apparel catalog price grid is `unverified` (lives on `/t/` PDPs). Breadth
  reads understate Nike.
- **Therabody / Hyperice** prices are a **Prime Day sale snapshot** (captured 2026-06-24)
  with strike-through regular prices on many cards — stale-by-design for any post-sale
  read; the offerings note says re-check before ranking.
- **Warby** national store count, per-box contacts price, and eye-exam fee are
  selection/booking-gated (`unverified_fields`).

## Source Gaps

- No structured field for **purchase-protection / fulfillment** retail factors (returns,
  warranty, shipping threshold, payment methods, channel). These are real, recurring,
  cross-brand-comparable consumer-retail decision inputs that currently live only in prose.
- No frontmatter signal that a capture's prices were taken during a **promotional sale**;
  `captured_at` dates the capture but not the merchandising state. A returning buyer can't
  tell a sale snapshot from a regular-price one without reading the offerings note.

## Raw Learning to Preserve

See `run-notes.md` Observations: **W1** (no structured handle for non-price retail
factors), **G1** (uneven offerings enumeration → breadth is a coverage artifact), **S1**
(per-line price-visibility token cleanly handled the consumer-vs-services split — a
strength), **G2** (sale-snapshot pricing has no freshness flag in frontmatter).

## External Completeness Check

Not run — completeness is not load-bearing for this read (the question is frame-fit on a
named seed cohort, not "who are all the transactional brands"). The seed set is explicitly
partial; the `business_model: Transactional` grep (28 hits) is named as the wider, mostly
out-of-scope pool. Say "not found," not "not there" for any brand-level absence.

## Market Pattern

Premium DTC physical-goods brands converge on a common transactional shape the store
**does** capture well at the price layer: one-time purchase, a published per-SKU catalog,
a free loyalty/app layer that is *not* a paid subscription (Nike Membership, Therabody
Coach, Warby Advisor), and an FSA/HSA + BNPL checkout. The recovery-hardware pair
(Therabody/Hyperice) even shares the **Nike × Hyperice Hyperboot** as a literal co-branded
SKU across two of the four profiles — a relation the store records in prose but not as a
structured link. Where the brands genuinely differentiate for a buyer — return window,
warranty length, channel, mission — the store carries it in prose, not fields.

## What Would Change This Answer

- A structured purchase-protection/fulfillment block (returns/warranty/shipping/payment)
  would flip the "buyer goes blind on non-price factors" verdict — but four brands is too
  thin to justify minting one; this is a sighting, not a mandate.
- Re-capturing Nike's full catalog (not just recovery) would make catalog-breadth
  comparison even, removing the coverage artifact.
- A post-sale re-capture of Therabody/Hyperice would test whether the sale-snapshot prices
  were transient and whether a freshness flag is warranted.
