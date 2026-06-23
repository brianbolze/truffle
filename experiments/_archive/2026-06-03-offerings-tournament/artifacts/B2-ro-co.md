<!--
artifact: B2 — molecule-pivoted offerings
company: Ro (ro.co)
portfolio_shape: Multi-product
scope: GLP-1 (weight-loss) + TRT/testosterone offerings only, per task. Other Ro lines (ED, hair, PE, cold sores/herpes, skin, fertility, multivitamin) exist and are priced on /pricing/ but are OUT of scope for this artifact.
built_from: captures/ro-co/{pricing-all-conditions, weight-loss-hub, weight-loss-pricing, weight-loss-wegovy-pen, weight-loss-wegovy-pill}.md (firecrawl, 2026-06-01/03)
anti-Doro: "Molecule" is a per-offering attribute for query-time grouping — greppable, NOT a stored canonical entity. Within-company key = page slug (Slug column). No cross-brand equivalence asserted: Ro's "semaglutide" is NOT claimed to be "the same product as" any other brand's.
-->

# Ro (ro.co) — Offerings, molecule-pivoted — GLP-1 + testosterone

Scope: the **GLP-1 (weight-loss)** and **TRT/testosterone** lines only. Ro is Multi-product (six condition lines); the rest are priced on `/pricing/` but excluded here per task.

## Portfolio overview

**Two molecule families in scope, and they could not be more different in shape:**

- **GLP-1s (weight loss)** — 6 buyable SKUs across 3 molecules (semaglutide, tirzepatide, orforglipron), all sold *through* one cash-pay **Ro Body membership** ($39 first month, then $74/mo prepaid annually, or $149/mo monthly[^body]). **The membership price is published; every GLP-1 medication price is structurally separate** ("billed separately—no hidden fees"[^pricepage]). Cash SKUs show real verbatim ladders on `/weight-loss/pricing/`; insurance SKUs are copay-gated.
- **Testosterone — one SKU, and it is NOT TRT.** Ro has **no prescription testosterone / TRT product.** The only testosterone offering is **Testosterone Support**, an **OTC daily supplement** ($35/mo monthly, $29/mo quarterly[^tsupport]) — a botanical/nutrient blend, not testosterone. Listed for completeness; see [Roster](#roster).

**Price-visibility at a glance (per offering, never a company scalar):**

| Family | SKUs in scope | Dominant visibility | Why |
|---|---|---|---|
| GLP-1 — cash-pay | Wegovy pill, Wegovy pen, Foundayo pill, Zepbound KwikPen, Ozempic | `[partial]` | Med price shown ("from $X") **but** mandatory Ro Body membership fee is separate + additive — real all-in is gated |
| GLP-1 — insurance route | Zepbound pen, Ozempic, Wegovy pen (insurance) | `[on-request]` | "Copays vary depending on your insurance"[^copay] — no price |
| Testosterone (OTC) | Testosterone Support | `[published]` | Full price on `/pricing/`, no Rx, no membership |

**Two structural findings worth stating plainly:**
1. **No GLP-1 is truly `[published]`.** Even the most transparent tile (a Wegovy pill "from $149/mo") is `[partial]`: the headline med price never includes the compulsory membership, which Ro itself bills and discloses separately. The all-in floor for any cash GLP-1 = med price **+** $74–$149/mo membership.
2. **Same molecule, different prices by form & route.** Semaglutide appears as a pill, a pen (cash), and a pen (insurance) at three different price structures — and tirzepatide as KwikPen (cash, laddered) vs pen (insurance, copay). This is exactly what the molecule pivot surfaces; the Slug column keeps each a distinct within-company offering.

## Deep blocks

Only the two genuine flagships. (Per-product pages exist for each GLP-1 but mostly restate the starting price and point back to `/weight-loss/pricing/`; their dose ladders sit behind a client-rendered "See pricing details" expander that did not capture — see [notes](#capture-notes--gated--unreachable).)

### Wegovy pill (semaglutide) — the foregrounded cash GLP-1 flagship

Slug: `/weight-loss/wegovy-pill/` · Molecule: **semaglutide** · Form: oral pill · Branded · Route: **cash-pay only**

> "The Wegovy pill is **only available as a cash-pay option**. For a limited time, new patients can start on the lower doses of Wegovy pill for **$149/mo**. The price of Wegovy increases for higher doses, but Prepay & Save on Ro unlocks even more savings."[^wpill]

- Pricing tile (`/weight-loss/pricing/`): **"$149 first month"**, **"$199-$299 thereafter"**[^pricepage]
- "First FDA-approved GLP-1 pill for weight loss"; "Prepay & Save $50/mo with an annual plan"[^pricepage]
- Visibility **`[partial]`** — a real "from" price shows, but the mandatory Ro Body membership ($74–$149/mo[^body]) is separate and additive; full dose ladder ($199–$299 band) is not itemized in captured markdown.

### Zepbound KwikPen (tirzepatide) — the only fully-laddered cash GLP-1

Slug: `/weight-loss/zepbound/` · Molecule: **tirzepatide** · Form: injection pen (KwikPen) · Branded · Route: **cash-pay only**

This is the one GLP-1 where the **complete dose-by-dose cash ladder captured** (via the pricing-page FAQ), so the structure is fully legible[^zepladder]:

| Dose | Cash price | Note |
|---|---|---|
| 2.5 mg | **$299/mo** | first-month tile: "$299 first month"[^pricepage] |
| 5 mg | **$399/mo** | |
| 7.5 mg | **$449/mo** | with manufacturer offer; **$499** if 45-day refill window missed[^zepladder] |
| 10 mg / 12.5 mg / 15 mg | **$449/mo** | with manufacturer offer; **$699** if window missed[^zepladder] |

- Pricing tile headline: **"$299 first month"**, **"$399-$449/mo thereafter"**[^pricepage]; "The fastest-working GLP-1"; "Same price as LillyDirect®"
- Visibility **`[partial]`** — full ladder is published, but the all-in still requires the separate Ro Body membership; the discounted $449 tier is conditional on a 45-day refill check-in.

## Roster

One row per **buyable SKU**. Molecule is a greppable per-offering attribute (group on it at query time); the **Slug** is the within-company key. Prices are **verbatim** from the captured pages — quoted, never recomputed. Membership is its own row (it is the gate every GLP-1 med price sits behind), not a med SKU.

| Molecule | Form | Branded/Compounded | Brand SKU name | Dose/strength | Price (verbatim) | Visibility | Slug |
|---|---|---|---|---|---|---|---|
| _(none — service)_ | membership | n/a | **Ro Body membership** | n/a | "$39 first month, $74/mo thereafter prepaid on annual plan"[^pricepage]; "$149/month" if monthly[^body] | `[published]` | `/weight-loss/` |
| **semaglutide** | oral pill | Branded | **Wegovy pill** | "lower doses" start (ladder not itemized) | "$149 first month" / "$199-$299 thereafter"[^pricepage] | `[partial]` | `/weight-loss/wegovy-pill/` |
| **semaglutide** | injection pen | Branded | **Wegovy pen** (cash) | "lower doses" start; HD = 7.2 mg[^wpen] | "$199 first month" / "$199-$399 thereafter"[^pricepage] | `[partial]` | `/weight-loss/wegovy/` |
| **semaglutide** | injection pen | Branded | **Wegovy pen** (insurance route) | maintenance 2.4 mg / HD 7.2 mg[^wpen] | "Copays vary depending on your insurance"[^copay] | `[on-request]` | `/weight-loss/wegovy/` |
| **orforglipron** | oral pill | Branded | **Foundayo pill** | "lower doses" start (ladder not itemized) | "$149 first month" / "$199-$299 thereafter"[^pricepage] | `[partial]` | `/weight-loss/foundayo/` |
| **tirzepatide** | injection pen (KwikPen) | Branded | **Zepbound KwikPen** (cash) | 2.5 / 5 / 7.5 / 10 / 12.5 / 15 mg[^zepladder] | "$299 first month" / "$399-$449/mo thereafter"[^pricepage]; ladder $299→$449 ($499/$699 off-window)[^zepladder] | `[partial]` | `/weight-loss/zepbound/` |
| **tirzepatide** | injection pen | Branded | **Zepbound pen** (insurance route) | (not itemized) | "Copays vary depending on your insurance"[^copay] | `[on-request]` | `/weight-loss/zepbound/` |
| **semaglutide** | injection pen | Branded | **Ozempic** | (not itemized) | "$900-$1100 a month without insurance"[^pricepage]; insurance: "Copays vary"[^copay] | `[partial]` | `/weight-loss/ozempic/` |
| _(not testosterone — supplement)_ | oral supplement | OTC blend | **Testosterone Support** | "Daily supplement"[^tsupport] | "Monthly plan $35 / mo" · "Quarterly plan (3 mo supply) $29 / mo"[^tsupport] | `[published]` | `/supplements/testosterone-support/` |

**Buyable SKU count in scope: 9** (1 membership + 7 GLP-1 medication offerings + 1 testosterone supplement). The two Zepbound rows and the two Wegovy-pen rows share a slug each (one within-company offering, two purchase routes) — counted as distinct buyable lines because each is a separately-buyable cash-vs-insurance path with its own price token.

Molecule grouping (query-time view, NOT a stored key):
- **semaglutide** → Wegovy pill, Wegovy pen (cash), Wegovy pen (insurance), Ozempic — 4 offerings, 3 slugs
- **tirzepatide** → Zepbound KwikPen (cash), Zepbound pen (insurance) — 2 offerings, 1 slug
- **orforglipron** → Foundayo pill — 1 offering, 1 slug
- _testosterone:_ no Rx molecule; Testosterone Support is an OTC blend (no single active drug named on captured pages)

## Capture notes — gated / unreachable

- **No GLP-1 all-in price is published anywhere.** Every cash GLP-1 med price is explicitly "billed separately" from the mandatory Ro Body membership[^pricepage]; insurance-route prices are "Copays vary"[^copay]. The gating *is* the finding — hence `[partial]` (a med "from" price shows) or `[on-request]` (insurance copay), never `[published]`, for medications.
- **Per-SKU dose ladders are behind a client-rendered expander.** On `/weight-loss/pricing/` each tile has a "(See pricing details)" control that did not render into the captured markdown[^pricepage]; per-product pages (Wegovy pen/pill) restate only the starting price and link back. **Only Zepbound's full ladder captured**, via the pricing-page FAQ[^zepladder]. So Wegovy pill/pen, Foundayo, and Ozempic show their verbatim *banded* tiles ("$199-$299 thereafter") but not the per-dose breakdown.
- **Saxenda is excluded.** It appears in the site nav (`/weight-loss/saxenda/`, per the store profile) but on **none** of the captured pages — no price, no captured page, so no row. Not-found in this sample, not asserted absent from the site.
- **No prescription TRT.** Confirmed across captures: Ro markets no testosterone-replacement Rx. "Testosterone Support" is an OTC supplement (`/pricing/` "Testosterone support" section); included as the sole testosterone-named SKU, flagged as not-TRT.
- **Point-in-time.** Ro runs its own A/B engine (`ro-experiments`) and promo pricing (limited-time "$149/mo" Wegovy starts, TrumpRx-matched cash prices); these tiles are a 2026-06-01/03 snapshot, not fixed list prices.

---

[^body]: `/weight-loss/` FAQ "How much does the Ro Body membership cost?": "The Ro Body membership costs $39 for the first month and as low as $74/month when you prepay for an annual plan. If you stay on a monthly plan, the ongoing cost is $149/month." (captures/ro-co/weight-loss-hub.md)
[^pricepage]: `/weight-loss/pricing/` — per-SKU cash tiles + membership ("billed separately—no hidden fees"); verbatim tile prices for Wegovy pill ("$149 first month" / "$199-$299 thereafter"), Foundayo pill (same), Zepbound KwikPen ("$299 first month" / "$399-$449/mo thereafter"), Wegovy pen ("$199 first month" / "$199-$399 thereafter"), Ozempic ("$900-$1100 a month without insurance"); Ro Body tile ("$39 first month, $74/mo thereafter prepaid on annual plan" — verbatim from /pricing/). (captures/ro-co/weight-loss-pricing.md; Ro Body tile also captures/ro-co/pricing-all-conditions.md)
[^copay]: `/weight-loss/pricing/` "Eligible GLP-1s — through insurance … Includes Zepbound® pen, Ozempic®, or Wegovy® pen … **Copays vary** depending on your insurance." (captures/ro-co/weight-loss-pricing.md)
[^wpill]: `/weight-loss/wegovy-pill/` "How much does the Wegovy pill cost?" — "only available as a cash-pay option … start on the lower doses … for $149/mo. The price of Wegovy increases for higher doses." (captures/ro-co/weight-loss-wegovy-pill.md)
[^wpen]: `/weight-loss/wegovy/` — cash start "$199/mo"; "Wegovy HD … contains 7.2 mg of semaglutide"; maintenance dose 2.4 mg; "Wegovy pen may be covered by insurance." (captures/ro-co/weight-loss-wegovy-pen.md)
[^zepladder]: `/weight-loss/pricing/` FAQ "How much does Zepbound cost?" — "The Zepbound KwikPen is available as a cash pay-only offering on Ro: $299/mo for 2.5 mg dose; $399/mo for 5 mg dose; $449/mo for 7.5 mg, 10 mg, 12.5 mg, and 15 mg doses (with manufacturer offer)." Off-window full price: "$499 for a 7.5 mg refill; $699 for 10 mg, 12.5 mg, and 15 mg refills" if next refill check-in not completed within 45 days. (captures/ro-co/weight-loss-pricing.md)
[^tsupport]: `/pricing/` "Testosterone support" — "Testosterone Support / Daily supplement / Monthly plan $35 / mo / Quarterly plan (3 mo supply) $29 / mo"; "Available monthly ($35/mo.) and quarterly ($87/3 mo.)". Not a prescription / not TRT — an OTC supplement. (captures/ro-co/pricing-all-conditions.md)
