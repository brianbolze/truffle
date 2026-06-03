---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.0"
domain: ro.co               # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-03     # own freshness; captures/2026-06-03/ holds the source pages
---

## Portfolio overview

Ro (Ro/Roman, private) is **Multi-product** — six condition lines (weight loss, sexual health, hair, skin,
fertility, daily supplements). This doc enumerates the **weight-loss (GLP-1)** line at SKU grain plus the one
**testosterone** offering, the two with a live per-SKU consumer; the other lines are real but not enumerated
here (no per-SKU capture this run). The two captured slices sell in **opposite shapes**: weight loss is a deep
six-SKU prescription roster wrapped in a paid membership; "testosterone" is a single OTC supplement.

**The shape finding — "testosterone" at Ro is *not* TRT.** Ro's only testosterone offering on the captured
pages is **Testosterone Support**, a "Daily supplement" (`$35/mo` monthly / `$29/mo` quarterly), shelved under
the pricing page's supplement tiles next to the men's multivitamin — not a condition line. No prescription
testosterone, no TRT gel/injection, no lab-and-treat path appears anywhere captured; the page never names an
active molecule ("you can't get this blend anywhere else"). Treat any "Ro does TRT" read as **unsupported by
this capture**.

**The weight-loss shape — a membership over a med roster, two visibility tokens:**
- **Ro Body membership is `[published]`** — the flat cash fee is shown outright ("`$39 first month, $74/mo
  thereafter prepaid on annual plan`"; monthly `$149/month`). It is the buyable wrapper; **medication is
  billed separately** and gated behind an online visit + provider Rx.
- **Every GLP-1 med SKU is `[partial]`** — a promotional starting price always shows ("`$149 first month`"),
  but the true ongoing cost rides a dose ladder ("`$199-$299 thereafter`") **plus** the mandatory, separately
  billed membership, and the med only ships after intake + Rx. The starting number is real but never the
  all-in. (Ozempic is the one quoted as a flat cash *range*, `$900-$1100`, still membership-gated.)

**Prominence (calibrated).** Weight loss is the deep, fully-built line **[HIGH]** — it is the only slice with
a dedicated `/weight-loss/pricing/` page, carries the widest lineup (three molecules, 6 med SKUs across
pill/pen, cash + insurance faces), and the hub's own H1 is "Get access to prescription weight loss medication
online" leading with "*See if you qualify* for Zepbound, Wegovy pill, or other GLP-1s." Testosterone reads as
a **thin supplement, not a line [HIGH]** — one SKU, sitting among OTC supplement tiles, no condition page in
this capture. Within the GLP-1 roster, **no SKU carries a "Most popular" badge** (those appear only on
ED/hair/PE/derm cards) — so no own-label hero. The hub card *order* leads with the three "Cash-pay only" pills
(Wegovy pill, Zepbound KwikPen, Foundayo pill) ahead of the insurance-or-cash pens, but card order + the
"New"/"In stock"/"Supply available" stock tags are left **[LOW]** — not used for ranking (stock tags are not
emphasis).

## Roster

Complete at the indexed level for the two captured slices. Within-company key = **Slug**. Price quoted verbatim
with its on-page markers; molecule/form is page-attested (never inferred from the brand — see the molecule note
under Verbatim anchors). The two Zepbound rows **share one slug** (`/weight-loss/zepbound/`) — they are the
cash and insurance access faces of the same tirzepatide PDP, kept as distinct rows by access. An offering here
is never asserted equal to a same-molecule offering at another brand.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Weight loss | family | — | `/weight-loss/` | — | — | GLP-1 weight-loss line; the Ro Body membership gates a med SKU roster behind an online visit + Rx, med billed separately. |
| Ro Body membership | buyable | Weight loss | `/weight-loss/` | `$39 first month, $74/mo thereafter prepaid on annual plan` (monthly `$149/month`) | published | — · subscription · the recurring cash-pay wrapper (GLP-1 access + insurance concierge + coaching/labs); **medication billed separately**. [^mem] |
| Wegovy pill | buyable | Weight loss / Ro Body | `/weight-loss/wegovy-pill/` | `$149 first month` · `$199-$299 thereafter` | partial | semaglutide · oral, once-daily upon waking · **cash-pay only**; dose ladder + mandatory membership gate the all-in. [^memreq] |
| Wegovy pen | buyable | Weight loss / Ro Body | `/weight-loss/wegovy/` | `$199 first month` · `$199-$399 thereafter` | partial | semaglutide · weekly injection pen · insurance-or-cash; HD dose = 7.2 mg, maintenance 2.4 mg; dose ladder + membership gated. [^memreq] |
| Foundayo pill | buyable | Weight loss / Ro Body | `/weight-loss/foundayo/` | `$149 first month` · `$199-$299 thereafter` | partial | orforglipron · oral · **cash-pay only**; "the newest FDA-approved GLP-1 pill"; price from `/weight-loss/pricing/` tile (own PDP not captured). [^memreq] |
| Zepbound KwikPen | buyable | Weight loss / Ro Body | `/weight-loss/zepbound/` | `$299 first month` · `$399-$449/mo thereafter` | partial | tirzepatide · pen · **cash-pay only**; "the fastest-working GLP-1"; full dose ladder + refill penalty in the anchor. [^kwik][^memreq] |
| Zepbound pen | buyable | Weight loss / Ro Body | `/weight-loss/zepbound/` | `Copays vary` (insurance); cash via KwikPen | partial | tirzepatide · pen · insurance-or-cash; the insurance face — cash buyers routed to the KwikPen variant. [^memreq] |
| Ozempic | buyable | Weight loss / Ro Body | `/weight-loss/ozempic/` | `$900-$1100 a month without insurance` | partial | semaglutide · weekly injection · FDA-approved for T2D, **off-label** for weight loss; pick up + pay at pharmacy; also listed insurance-eligible ("Copays vary"). [^memreq] |
| Testosterone Support | buyable | Daily health / supplements | `/supplements/testosterone-support/` | `$35 / mo` (monthly) · `$29 / mo` (quarterly, 3-mo supply) | published | **not stated** · OTC daily supplement · **NOT prescription TRT**; "$15 off your first order"; quarterly billed `$87/3 mo`. |

### Verbatim anchors

The footnotes the roster's Price column points at — they are what decide `[partial]` vs `[published]`, plus the
molecule-sourcing audit trail. Quoted exactly from the captured pages.

- **[^mem] Ro Body membership (the wrapper, `[published]`):** the `/pricing/` tile reads *"Ro Body — Weight
  loss medication · Monthly membership **$39 first month, $74/mo thereafter prepaid on annual plan**"*; the
  weight-loss FAQ restates *"The Ro Body membership costs **$39 for the first month** and as low as
  **$74/month** when you prepay for an annual plan. If you stay on a monthly plan, the ongoing cost is
  **$149/month**. … the cost of GLP-1 medication is not included in the membership cost."* (weight-loss-hub +
  weight-loss-pricing + pricing-all-conditions). The fee is fully shown; the **medication** under it is what is
  gated. Membership is **cash-pay only** ("only available by cash pay only and does not accept insurance").
- **[^memreq] every GLP-1 med SKU (the `[partial]` driver):** each med tile footnotes, verbatim: *"**Additional
  Ro Body membership fee required.** The Ro Body membership fee is as low as $74/month when you prepay on an
  annual plan."* (weight-loss-pricing). Cross-cutting cash framing: *"Options start at **$149/month**\* and
  increases for higher doses"* (\* *"new patients can start on the lower doses of Wegovy pill for $149/mo"*).
  Insurance-eligible SKUs (Zepbound pen, Ozempic, Wegovy pen): *"**Copays vary** depending on your insurance."*
  → a starting number shows, but the all-in = membership + dose ladder + Rx, hence `[partial]`.
- **[^kwik] Zepbound KwikPen full cash dose ladder + refill penalty (weight-loss-pricing FAQ):** *"$299/mo for
  2.5 mg dose; $399/mo for 5 mg dose; $449/mo for 7.5 mg, 10 mg, 12.5 mg, and 15 mg doses (with manufacturer
  offer)."* Miss the 45-day refill check-in and *"You'll be charged the full price for your refill: **$499** for
  a 7.5 mg refill; **$699** for 10 mg, 12.5 mg, and 15 mg refills."* The tile summary is the roster's `$299
  first month / $399-$449/mo thereafter`. (Wegovy pill/pen and Foundayo dose-by-dose ladders sit behind a
  client-side "See pricing details" expander that did not render — only their "first month" + "thereafter"
  ranges are visible.)
- **Molecule sourcing (the page-attested-only rule, audited):**
  - **semaglutide** → Wegovy pill, Wegovy pen, Ozempic — attested on the `/weight-loss/pricing/` tiles
    (*"Wegovy® pill — semaglutide"*, *"Wegovy® pen — semaglutide"*, *"Ozempic® — semaglutide"*), the hub cards
    ("Semaglutide"), and the wegovy-pill page (*"Active ingredient: semaglutide (same as Wegovy pen and
    Ozempic)"*).
  - **tirzepatide** → Zepbound KwikPen + Zepbound pen — attested on the pricing tile (*"Zepbound® KwikPen® —
    tirzepatide"*) and both hub Zepbound cards ("Tirzepatide").
  - **orforglipron** → Foundayo pill — attested (*"Foundayo™ pill — orforglipron"*; hub card "Orforglipron").
  - **Testosterone Support → "not stated."** No captured page names a molecule — the `/pricing/` block calls it
    a *"Daily supplement"* and *"this blend"* (*"You can't get this blend anywhere else"*), never an active
    ingredient. Recorded "not stated" rather than inferred from the "testosterone" name — it is a supplement
    blend, not a hormone.

## Deep blocks

One block earns its place — the not-TRT disambiguation a roster cell can't carry. The weight-loss molecules and
their per-SKU prices live in the roster (+ the Zepbound ladder in its anchor); reproducing them as blocks would
only restate roster/footnote cells.

### Testosterone Support — an OTC supplement, *not* prescription TRT

- **Parent:** Daily health / supplements · **slug:** `/supplements/testosterone-support/` · **price:** `$35 /
  mo` (monthly) · `$29 / mo` (quarterly, 3-mo supply) · **visibility:** `[published]`

> **Section + tile (verbatim, `/pricing/`):** "Created by doctors, backed by science. You can't get this blend
> anywhere else. Every active ingredient is backed by studies showing improvement in at least one area of male
> virility. Get $15 off your first order · Available monthly ($35/mo.) and quarterly ($87/3 mo.)"
> **Tile (verbatim):** "Testosterone Support · Daily supplement · Monthly plan **$35 / mo** · Quarterly plan
> (3 mo supply) **$29 / mo**"
> **Molecule:** *not named on any captured page* — "this blend," "every active ingredient," no hormone or
> compound stated.

**Why this block earns its place** (and the others don't): the single most likely cross-brand mis-grouping
against a telehealth roster is "Ro testosterone = TRT." It isn't. Ro's only testosterone offering on these
pages is an **OTC daily supplement** at `$35/mo` — no prescription, no testosterone hormone, no gel/injection,
no lab-and-treat path appears anywhere in the 5 captured pages. The roster row flags this, but the block carries
the verbatim proof and the **absence finding** a cell can't: a TRT line elsewhere on ro.co cannot be ruled out
by this sample, but within this capture it is **not found**. (Contrast Hims, whose testosterone line *is* a
prescription enclomiphene product — same word, different shape.) The GLP-1 line, by contrast, answers fully
from the roster + anchors, so it earns no block.

## Provenance

- **Pages read (5, all `captures/2026-06-03/`):** `pricing-all-conditions.md` (/pricing/),
  `weight-loss-hub.md` (/weight-loss/), `weight-loss-pricing.md` (/weight-loss/pricing/),
  `weight-loss-wegovy-pen.md` (/weight-loss/wegovy/), `weight-loss-wegovy-pill.md` (/weight-loss/wegovy-pill/).
  Context: `store/ro-co/profile.md`. `/pricing/` + `/weight-loss/` were warm-reused from the 2026-06-01 store
  capture; `/weight-loss/pricing/` + the two per-product pages were fetched 2026-06-03 (3 credits).
- **Scope:** weight-loss (GLP-1) at SKU grain + the single testosterone offering — the two slices with a live
  per-SKU consumer. Ro's other lines (ED/sexual health, premature ejaculation, hair, skin/derm, fertility, the
  men's multivitamin) are priced on `/pricing/` but **not enumerated** here — out of this run's scope.
- **Gated / unreachable:** GLP-1 medication all-in cash cost (dose-laddered + provider-titrated + separately
  billed membership — the "thereafter" ranges are floors, not totals); per-dose ladders for Wegovy pill, Wegovy
  pen, and Foundayo (behind an unrendered client-side "See pricing details" expander — captured only for
  Zepbound KwikPen via its FAQ); own PDPs for Foundayo, Zepbound, and Ozempic (priced via the
  `/weight-loss/pricing/` tiles, not their dedicated pages); Testosterone Support's active-ingredient list
  (a "blend," unnamed); the Zepbound **pen** has no standalone cash price (cash buyers routed to the KwikPen).
- **Point-in-time snapshot, not fixed:** Ro runs its own A/B engine (`ro-experiments`) and promo-driven offers
  ("for a limited time" recurs on every Wegovy/Foundayo starting price; TrumpRx-matched cash pricing) — this
  module's `captured_at` + a short freshness TTL are the guard; re-capture before trusting a price as current.
