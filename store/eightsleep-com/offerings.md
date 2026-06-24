---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: eightsleep.com       # company key; each offering's slug (its relative url) is its key *within* Eight Sleep
captured_at: 2026-06-24      # own freshness; captures/2026-06-24/ holds the source pages
enumeration: indexed-complete   # every product line rostered at SKU grain off /accessories + /product/pod-cover; only leaf gaps (Pod 5 Ultra price, per-size pricing) skipped
site_notes: "Whole catalog lives at /accessories (every companion SKU as a card with slug + price) + the /product/pod-cover configurator (Pod 5 hardware price, sizes, and the 3 Autopilot tiers). No CMS REST backend exposed — accessories page is the authoritative index, and it carries verbatim prices, so no per-SKU PDP sweep was needed. Prices ran a '4th July Sale' (up to $500 off) — both sale and struck-through regular prices captured; re-check next run. Pod 5 has a Core and an Ultra Cover variant; the configurator rendered only the Core price."
---

## Portfolio overview

Eight Sleep is **Flagship + companions**: one hero — **the Pod** (a smart mattress *Cover*, not a mattress) — plus a companion catalog that mostly "Requires Pod." The shape finding worth flagging: the Pod is sold as **hardware + a mandatory software subscription** — **Autopilot is required for the first 12 months**, so the real entry price is the Cover *plus* an annual plan ($199–$399/yr), not the hardware alone. The companions split into four groups: **temperature hardware** (Base, Blanket, Pillow Cover), a **Premium Mattress**, **supplements** (Sleep Elixir / Plus, Jet Lag), and **bedding** (sheets, pillow, protector, duvet cover, a bundle).

**Prominence (calibrated):**
- **The Pod (Cover) is the unambiguous lead [HIGH]** — the only nav CTA ("Shop the Pod"), the homepage hero, and the PDP every page routes to.
- **Base → Blanket → Pillow Cover are the primary add-ons [HIGH]** — that exact order is the PDP's "Add on and save" section and the top of the `/accessories` grid.
- **Supplements + bedding are tail accessories [MED]** — lower in the `/accessories` grid, no hero placement.
- **Autopilot is mandatory infrastructure, not a merchandised "product" [HIGH]** — required, recurring, and the strategic core (the Elite tier reframes the bed as a health device).

**Visibility:** every line is **`published`** — Eight Sleep shows a verbatim price for all hardware, supplements, bedding, and all three Autopilot tiers; nothing is quiz- or consult-gated. (The Pod's all-in *requires* Autopilot, but that price is openly shown too, so the Pod row stays `published`, not `partial`.)

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (form · access) |
|---|---|---|---|---|---|---|
| Pod 5 (the Cover) | buyable | — | /product/pod-cover | $2,749 (~~$2,999~~, Queen) | published | smart mattress cover · the Cover + Hub · dual-zone cooling/heating 55–110°F, sleep & health tracking, vibration/thermal alarms; **requires Autopilot**. *(Higher Pod 5 Ultra variant adds auto-elevation + snore mitigation — price not captured.)* |
| Autopilot | family | — | /autopilot | — | — | required AI software subscription · annual billing · covers 2 users/Pod · required first 12 months |
| · Autopilot Standard | buyable | /autopilot | (no PDP — tier on /product/pod-cover) | $199 billed annually ($17/mo) | published | dynamic temperature, vibration/thermal alarm, sleep & health tracking, snore detection + mitigation, 2-year warranty |
| · Autopilot Enhanced | buyable | /autopilot | (no PDP — tier on /product/pod-cover) | $299 billed annually ($25/mo) | published | everything in Standard + **5-year warranty** (the "most members choose" tier) |
| · Autopilot Elite | buyable | /autopilot | (no PDP — tier on /product/pod-cover) | $399 billed annually ($33/mo) | published | everything in Enhanced + Health Check: advanced cardiovascular + respiratory monitoring ("New") |
| The Base | buyable | — | /product/the-base | $1,899 (~~$1,999~~) | published | adjustable bed base · slides under mattress · elevation, automatic snore mitigation, integrated speaker; requires Pod 4 or 5 |
| The Blanket | buyable | — | /product/the-blanket | $949 (~~$999~~) | published | hydro-powered duvet insert · doubles cooling/heating coverage; requires Pod 5 |
| Pod Pillow Cover | buyable | — | /product/the-pillow-cover | $949 (~~$999~~) | published | cooling/heating cover for any pillow · runs on its own Hub; requires Pod |
| Premium Mattress | buyable | — | /product/premium-mattress | $1,899 (~~$1,999~~) | published | breathable, supportive mattress · pairs with the Pod Cover |
| Sleep Elixir | buyable | — | /product/sleep-elixir | $59 (~~$79~~, Subscribe & save) | published | daily sleep supplement |
| Sleep Elixir Plus | buyable | — | /product/sleep-elixir-plus | $59 (~~$79~~, Subscribe & save) | published | daily sleep supplement **+ melatonin** |
| Jet Lag | buyable | — | /product/jet-lag | $99 | published | supplement to help beat jet lag |
| The Air Pillow | buyable | — | /product/the-air-pillow | $199 | published | premium pillow made to dissipate heat |
| Pod Sheet Set | buyable | — | /product/the-pod-sheet-set | $189 | published | sheet set designed to fit the Pod |
| Pod Protector | buyable | — | /product/waterproof-protector | $119 | published | waterproof protector for the Pod |
| Duvet Cover | buyable | — | /product/duvet-cover | $199 | published | custom-fit cover made for the Pod Blanket |
| The Sleep Essentials Bundle | buyable | — | /product/the-sleep-essentials-bundle | $415 (Bundle & Save $200) | published | bundle · one Pod Sheet Set + one Pod Protector + two Air Pillows |

*Also offered (not a SKU): **Rent the Pod** — a Pod 5 Core/Ultra + Autopilot for **from $169/mo**, cancel anytime (a rental, not rent-to-own). Financing via **Affirm** 0% APR (up to 36 mo, "as low as $77/mo") + **Klarna**; HSA/FSA-eligible.*

### Verbatim anchors

- **Sale (point-in-time):** "4th July Sale: Get up to $500 off*" — sale prices above; struck-through values are regular price (e.g. Pod 5 "$2,749 / $2,999 / $250 off"; Base "$1,999 / $1,899 / -$100").
- **Mandatory subscription:** "An Autopilot Plan is required for the first 12 months (cancel any time), and covers two separate users per Pod." / "Autopilot comes in annual plans and is billed once yearly."
- **Warranty tie:** "**Autopilot Enhanced or Autopilot Elite required for 5-year warranty.**" Standard = 2-year.
- **Supplement pricing:** Sleep Elixir / Sleep Elixir Plus list "$59 ~~$79~~ Subscribe & save" — $59 is the subscribe price, $79 the struck one-time.

## Deep blocks

*None earned — the roster + the `/accessories` index carry this catalog. Every SKU is a single published price on one index page; no gated line, FAQ-only figure, or molecule disambiguation needs a block.*

## Provenance

- **Pages read:** `/accessories` (the authoritative SKU index — slug + price per card) and `/product/pod-cover` (Pod 5 hardware price, sizes, the 3 Autopilot tiers, rent + financing), cross-checked against `/product/the-base` and `/autopilot`. Captures under `captures/2026-06-24/`.
- **Scope:** `indexed-complete` — all product lines rostered at SKU grain. **Leaf gaps (not omitted lines):** Pod 5 **Ultra** Cover-variant price (configurator showed only Core/Queen), and per-size pricing (Full / King / Cali King — only Queen rendered).
- **Snapshot caveat:** prices ran a "4th July Sale" (up to $500 off) — a point-in-time promo snapshot, not fixed; regular prices captured struck-through for every discounted line.
- **Run profile:** guided — `offerings.md` requested alongside the standard profile. No emphasis, no hero images, no added columns.
