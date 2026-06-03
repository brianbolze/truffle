<!--
design: B1 — roster-first offerings.md (incumbent 2026-06-01 design)
company: ro.co (Ro)
portfolio_shape: Multi-product
scope: every GLP-1 and TRT/testosterone offering on Ro's own site
within-company key = page slug · NO cross-company canonical key · price_visibility is per-offering
sources (this company only):
  - /pricing/                → captures/ro-co/pricing-all-conditions.md
  - /weight-loss/            → captures/ro-co/weight-loss-hub.md
  - /weight-loss/pricing/    → captures/ro-co/weight-loss-pricing.md
  - /weight-loss/wegovy/     → captures/ro-co/weight-loss-wegovy-pen.md
  - /weight-loss/wegovy-pill/→ captures/ro-co/weight-loss-wegovy-pill.md
captured_at: 2026-06-01 (warm) / 2026-06-03 (weight-loss/pricing + per-product, fetched)
-->

# Ro — Offerings (GLP-1 + Testosterone)

## Portfolio overview

**Two very different shapes sit under the words "GLP-1" and "testosterone" at Ro.** The GLP-1 line is a real, deep, six-SKU prescription roster wrapped in a paid membership. "Testosterone," by contrast, is **not a prescription TRT product at all** — Ro's only testosterone offering is an OTC daily supplement. The gap is the headline finding.

**GLP-1 (weight loss) — a membership wrapping a med roster.** The buyable thing Ro sells you first is the **Ro Body membership** (a flat cash-pay fee: `$39 first month`, then `$74/mo` annual / `$149/mo` monthly). The GLP-1 medication is billed *separately* and is gated behind an online visit + provider Rx + a dose ladder. So the line is two layers:
- **Layer 1 — membership** (`Ro Body`): price fully published.
- **Layer 2 — the med SKUs** (six of them): each has a published *starting* "from $X first month" cash price on `/weight-loss/pricing/`, but the real all-in is membership + a per-dose ladder that escalates ("$199–$299 thereafter", etc.), and the medication only ships after Rx. Each med SKU is therefore **[partial]** — a price shows, but the true ongoing cost is dose- and Rx-gated. The lone exception is **Ozempic**, quoted as a flat cash range with no Prepay/ladder.

The six med SKUs split by molecule and form:
- **Semaglutide** — Wegovy pill (oral), Wegovy pen (injection), Ozempic (injection, off-label).
- **Tirzepatide** — Zepbound KwikPen (the cash variant), Zepbound pen (the insurance variant).
- **Orforglipron** — Foundayo pill (oral, newest).

Cash vs. insurance is a stocking/access axis Ro foregrounds: Wegovy pill, Zepbound KwikPen, Foundayo pill are tagged **"Cash-pay only"**; Wegovy pen, Zepbound pen, Ozempic are **"Insurance or cash-pay."** Same molecule appears on both sides (semaglutide as both a cash-only pill and an insurance-eligible pen) — a within-Ro distinction by *form + brand + access*, keyed by slug, not a canonical "semaglutide" entity.

**Testosterone — supplement, not TRT.** Ro lists **Testosterone Support**, a "daily supplement" at `$35/mo` (monthly) / `$29/mo` (quarterly), fully published on `/pricing/`. There is no prescription testosterone, no TRT gel/injection, no testosterone lab-and-treat path on the captured pages. (Ro does sell a separate **Fertility Hormone Test** elsewhere, but that is not a testosterone-replacement offering and is out of this roster.)

**Breadth-first hierarchy (GLP-1 + testosterone slice only):**
```
Weight loss  /weight-loss/
  └─ Ro Body membership  /weight-loss/   [the paid wrapper; med billed separately]
       ├─ Wegovy pill        /weight-loss/wegovy-pill/   semaglutide · oral · cash-only
       ├─ Wegovy pen         /weight-loss/wegovy/        semaglutide · injection · insurance|cash
       ├─ Foundayo pill      /weight-loss/foundayo/      orforglipron · oral · cash-only
       ├─ Zepbound KwikPen   /weight-loss/zepbound/      tirzepatide · pen · cash-only
       ├─ Zepbound pen       /weight-loss/zepbound/      tirzepatide · pen · insurance|cash
       └─ Ozempic            /weight-loss/ozempic/       semaglutide · injection · off-label
Daily Health (supplements)
  └─ Testosterone Support  /supplements/testosterone-support/   OTC supplement — NOT TRT
```
(Ro's full catalog also spans ED, premature ejaculation, hair, skin/derm, fertility, and a men's multivitamin — all out of scope here.)

---

## Deep blocks

The four most-compared / flagship offerings in this slice: the membership wrapper, the two Wegovy forms (semaglutide, the line's hero), and the testosterone supplement (because it is the surprising non-TRT). Spine first, then verbatim gold.

### Ro Body membership — the paid GLP-1 wrapper
- **Parent:** Weight loss · **url:** `/weight-loss/` · **kind:** family/membership
- **Price:** `$39 first month, $74/mo thereafter prepaid on annual plan` (monthly: `$149/month`)
- **price_visibility:** **[published]** — the membership fee itself is fully shown. (The *medication* under it is separate and gated — see each med SKU.)

Verbatim, page H1 (`/weight-loss/`):
> # Get access to prescription weight loss medication online

Exact price string, FAQ "How much does the Ro Body membership cost?" (`/weight-loss/`, restated identically on `/weight-loss/pricing/`):
> "The Ro Body membership costs **$39 for the first month** and **as low as $74/month when you prepay for an annual plan**. If you stay on a monthly plan, the ongoing cost is **$149/month**.
> Please note that the cost of GLP-1 medication is not included in the membership cost. Medication cost will depend on your treatment and insurance coverage."

`/pricing/` tile, verbatim:
> ### Ro Body — Weight loss medication
> Monthly membership **$39 first month, $74/mo thereafter prepaid on annual plan**

What's included (verbatim, `/weight-loss/`):
> - Access to FDA-approved GLP-1 medications
> - Dedicated insurance concierge
> - Unlimited provider messaging
> - Side effect management and titration support
> - Weight tracking and dose logging
> - 1:1 health coaching

Membership is **cash-pay only** and does not accept insurance for the fee itself (`/weight-loss/pricing/` FAQ: "this medication is paid for separately from your Ro Body membership, which is only available by cash pay only and does not accept insurance"). Audience: adults qualifying for GLP-1s ("See if you qualify for Zepbound, Wegovy pill, or other GLP-1s").

### Wegovy pill (semaglutide) — oral, cash-pay-only
- **Parent:** Ro Body / Weight loss · **url:** `/weight-loss/wegovy-pill/` · **kind:** buyable (med SKU)
- **Price:** `$149 first month`, `$199-$299 thereafter` (cash; + membership)
- **price_visibility:** **[partial]** — a starting cash price shows, but ongoing cost rides a dose ladder + the separate mandatory membership; medication only ships after an online visit + Rx.

Verbatim, page H1 (`/weight-loss/wegovy-pill/`):
> # Wegovy® pill prescription online for weight loss

Exact price string, "How much does the Wegovy pill cost?" (`/weight-loss/wegovy-pill/`):
> "The Wegovy pill is **only available as a cash-pay option**. For a limited time, new patients can start on the lower doses of Wegovy pill for **$149/mo**. The price of Wegovy increases for higher doses, but Prepay & Save on Ro unlocks even more savings."

Per-SKU tile, verbatim (`/weight-loss/pricing/`):
> ### Wegovy® pill — semaglutide
> - First FDA-approved GLP-1 pill for weight loss
> - Prepay & Save $50/mo with an annual plan
> - Shipped directly to your door
> **$149 first month**
> **$199-$299 thereafter**
> (See pricing details)

Footnote always attached: "**Additional Ro Body membership fee required.** The Ro Body membership fee is as low as $74/month when you prepay for an annual plan." Form/dose facts (verbatim): "taken by mouth once daily upon waking"; "Highest-dose 1-year avg weight loss: 14% (pill) vs 19% (pen)." The full dose-by-dose ladder is behind a client-side "See pricing details" expander that did not render.

### Wegovy pen (semaglutide) — injection, insurance-or-cash
- **Parent:** Ro Body / Weight loss · **url:** `/weight-loss/wegovy/` · **kind:** buyable (med SKU)
- **Price:** `$199 first month`, `$199-$399 thereafter` (cash; + membership) — or insurance copay
- **price_visibility:** **[partial]** — starting cash price shown; ongoing is dose-laddered + membership-gated; insurance route is "copays vary."

Verbatim, page H1 (`/weight-loss/wegovy/`):
> # Wegovy® pen prescription online for weight loss

Exact price string, "How much does the Wegovy pen cost?" (`/weight-loss/wegovy/`):
> "**Paying cash?** For a limited time, new patients can start on the lower doses of Wegovy pen for **$199/mo**. The price of Wegovy increases for higher doses, but Prepay & Save on Ro unlocks even more savings.
> **Using insurance?** Wegovy pen may be covered by insurance. If you'd like to use insurance, our insurance concierge will fight for coverage and handle all of your paperwork."

Per-SKU tile, verbatim (`/weight-loss/pricing/`):
> ### Wegovy® pen — semaglutide
> - Wegovy at half the retail price when paying cash
> - Prepay & Save up to $150/mo with an annual plan
> - Shipped directly to your door
> **$199 first month**
> **$199-$399 thereafter**
> (See pricing details)

Form (verbatim): "a prefilled injection pen used once weekly." Dose note: "Wegovy HD … contains **7.2 mg of semaglutide**"; maintenance dose 2.4 mg. Savings mechanic (verbatim, `/weight-loss/pricing/`): "Save $100/mo on the Wegovy pen and $50/mo on the Wegovy pill with an annual plan."

### Testosterone Support — OTC supplement (NOT prescription TRT)
- **Parent:** Daily Health / supplements · **url:** `/supplements/testosterone-support/` · **kind:** buyable (OTC supplement)
- **Price:** `$35 / mo` (monthly) · `$29 / mo` (quarterly, 3-mo supply); `$15 off your first order`
- **price_visibility:** **[published]** — both plan prices shown outright on `/pricing/`.

Verbatim, `/pricing/` section + tile:
> ### Testosterone support
> Created by doctors, backed by science. You can't get this blend anywhere else. Every active ingredient is backed by studies showing improvement in at least one area of male virility.
> Get $15 off your first order
> Available monthly ($35/mo.) and quarterly ($87/3 mo.)
> ### Testosterone Support — Daily supplement
> Monthly plan **$35 / mo**
> Quarterly plan (3 mo supply) **$29 / mo**

This is a daily *supplement*, not testosterone-replacement therapy: no prescription, no testosterone hormone, no gel/injection/lab-and-treat path appears anywhere in the captured pages. Treat any "Ro does TRT" read as **unsupported** by this capture.

---

## Roster (complete at the indexed level — GLP-1 + testosterone slice)

Within-company key = **Slug**. Prices verbatim from the cited pages; med SKUs carry a mandatory separate membership fee (see footnotes). NO cross-company canonical key — molecule lives in "What", not as an identity.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (one line) |
|---|---|---|---|---|---|---|
| **Ro Body membership** | family/membership | Weight loss | `/weight-loss/` | `$39 first month, $74/mo thereafter prepaid on annual plan` (monthly `$149/month`) | [published] | Cash-pay GLP-1 access wrapper: provider Rx, insurance concierge, coaching, labs; **med billed separately**. [^mem] |
| **Wegovy pill** | buyable | Ro Body / Weight loss | `/weight-loss/wegovy-pill/` | `$149 first month` · `$199-$299 thereafter` | [partial] | Semaglutide · oral, once-daily · **cash-pay only**; dose ladder + membership gate cost. [^memreq] |
| **Wegovy pen** | buyable | Ro Body / Weight loss | `/weight-loss/wegovy/` | `$199 first month` · `$199-$399 thereafter` | [partial] | Semaglutide · weekly injection pen · insurance-or-cash; HD dose = 7.2 mg. [^memreq] |
| **Foundayo pill** | buyable | Ro Body / Weight loss | `/weight-loss/foundayo/` | `$149 first month` · `$199-$299 thereafter` | [partial] | Orforglipron · oral · newest FDA-approved GLP-1 pill · **cash-pay only**. [^memreq] |
| **Zepbound KwikPen** | buyable | Ro Body / Weight loss | `/weight-loss/zepbound/` | `$299/mo` 2.5mg · `$399/mo` 5mg · `$449/mo` 7.5–15mg (w/ mfr offer) | [partial] | Tirzepatide · pen · **cash-pay only**; "fastest-working GLP-1"; full dose ladder below. [^kwik][^memreq] |
| **Zepbound pen** | buyable | Ro Body / Weight loss | `/weight-loss/zepbound/` | `Copays vary` (insurance route); cash via KwikPen | [partial] | Tirzepatide · pen · insurance-or-cash; cash buyers routed to the KwikPen variant. [^memreq] |
| **Ozempic** | buyable | Ro Body / Weight loss | `/weight-loss/ozempic/` | `$900-$1100 a month without insurance` | [partial] | Semaglutide · weekly injection · FDA-approved for T2D, **off-label** for weight loss; pay at pharmacy. [^memreq] |
| **Testosterone Support** | buyable | Daily Health / supplements | `/supplements/testosterone-support/` | `$35 / mo` (monthly) · `$29 / mo` (quarterly) | [published] | **OTC daily supplement — NOT prescription TRT**; "$15 off your first order." |

[^mem]: Membership fee is fully published and **[published]**; the *medications* underneath it are separately billed, Rx-gated, and dose-laddered, hence each med SKU is **[partial]** on its own row. Membership is cash-pay only and "does not accept insurance" for the fee.

[^memreq]: Every GLP-1 med SKU footnotes, verbatim: "**Additional Ro Body membership fee required.** The Ro Body membership fee is as low as $74/month when you prepay on an annual plan." Med ships only after an online visit → provider Rx. "Eligible GLP-1s — through insurance" (Zepbound pen, Ozempic, Wegovy pen): "**Copays vary** depending on your insurance."

[^kwik]: Zepbound KwikPen full cash ladder, verbatim (`/weight-loss/pricing/` FAQ): "$299/mo for 2.5 mg dose; $399/mo for 5 mg dose; $449/mo for 7.5 mg, 10 mg, 12.5 mg, and 15 mg doses (with manufacturer offer)." Miss the 45-day refill window and "you'll be charged the full price": "$499 for a 7.5 mg refill; $699 for 10 mg, 12.5 mg, and 15 mg refills." Tile summary: "**$299 first month** / **$399-$449/mo thereafter**."

### Cross-cutting price framing (verbatim, `/weight-loss/pricing/`)
- "**Lowest medication prices**—the same as LillyDirect®, NovoCare®, and TrumpRx."
- "Options start at **$149/month**\* and increases for higher doses." (\*"new patients can start on the lower doses of Wegovy pill for $149/mo.")
- "**Prepay & Save** unlocks up to **$150 per month** on GLP-1s" / "$150/mo savings apply to the highest dose of Wegovy pen on an annual plan."
- Metabolic test: "testing at any Quest location is **included** in the cost of the Ro Body membership. Or you can purchase an **at-home blood collection kit through Ro for $75**."

### Notes on gating / what the capture can't see
- **GLP-1 med all-in is fundamentally [partial], not [published].** Each med shows a promotional "from $X first month," but the true ongoing price is a dose ladder ("$199–$299 thereafter") **plus** the mandatory, separately-billed membership — and the medication only ships after intake + provider Rx. The "from" price is real but not the all-in. (Ozempic is quoted as a flat cash range, still membership-gated.)
- **Per-dose ladders are mostly behind a client-side "See pricing details" expander** that did not render into markdown — captured only for **Zepbound KwikPen** (via the page's FAQ). Wegovy pill/pen, Foundayo dose-by-dose ladders are unrendered (only the "first month" + "thereafter" range tiles are visible).
- **Zepbound pen** has no standalone cash price tile; cash buyers are routed to the **Zepbound KwikPen**. Its row is the insurance-access face of tirzepatide ("Copays vary").
- **Foundayo** has a price tile on `/weight-loss/pricing/` but its dedicated `/weight-loss/foundayo/` per-product page was not captured; the price shown is from the pricing-page tile.
- **No prescription TRT exists on the captured pages.** The only testosterone offering is the OTC **Testosterone Support** supplement. Absence of a TRT product here = **not found in this capture** (5 pages: `/pricing/`, `/weight-loss/`, `/weight-loss/pricing/`, `/weight-loss/wegovy/`, `/weight-loss/wegovy-pill/`); a testosterone-treatment line elsewhere on ro.co cannot be ruled out by this sample.
- **Prices are a point-in-time snapshot.** Ro runs its own A/B engine and promo-driven offers (TrumpRx pricing, limited-time "$149/mo" starts); "for a limited time" appears on every Wegovy/Foundayo starting price.
