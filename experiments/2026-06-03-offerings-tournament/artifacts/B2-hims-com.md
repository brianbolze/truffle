<!-- design: B2 — molecule-pivoted offerings | company: hims.com | portfolio_shape: Multi-product
     scope: every GLP-1 and TRT/testosterone offering on hims.com's own pages, 2026-06-03 capture.
     anti-Doro: "Molecule" is a per-offering ATTRIBUTE for query-time grouping ONLY (greppable column).
     It is NOT a stored canonical entity. The within-company key is the page Slug (last column).
     No claim is made that a molecule here "is the same product as" any other brand's. -->

# Hims — offerings (molecule-pivoted) · GLP-1 + testosterone

**Scope:** the two prescription lines where Hims runs a molecule-diverse SKU shelf — **weight-loss GLP-1** and **testosterone (TRT-adjacent)**. Built only from hims.com's own `/weight-loss` and `/testosterone` pages (8 captures, fetched 2026-06-03). Sexual-health, hair-loss, mental-health, and labs are out of scope for this doc.

**The one structural fact:** every buyable SKU here is **quiz-gated**. The advertised number is **medication-only** and there is **no path to the all-in price without completing an intake** — GLP-1s route through `/g/i/wm`, testosterone through `/g/i/tt`. So prices read as published teasers, but checkout is gated, and the GLP-1 line carries a **mandatory separate membership** ($39 first month, then $149/mo). Visibility tokens below encode exactly which.

> **Reading the Molecule column:** it is a grouping *attribute*, not an identity claim. "semaglutide" appearing on three Hims rows does not assert those are one product, and says nothing about semaglutide at any other brand. To compare across brands, group on this column at query time — do not treat it as a key. The key is the **Slug**.

---

## Portfolio overview

**Families (summarized; SKU-level detail in the Roster):**

- **GLP-1 / weight loss — the hero shelf.** Six molecule-and-form variants Hims itself lists as its medication menu: *"the Wegovy® Pill, Wegovy® Pen, Zepbound® KwikPen®, Zepbound® Vial, Foundayo™ Pill, and Ozempic® Pill"* [WL-FAQ]. Three molecules across two delivery modes (oral / injectable), spanning branded-only SKUs. Advertised range **From $149/mo† to $299/mo†** for the core menu, with two additional injectables (Mounjaro®, a Zepbound® pen) surfaced **only in on-page modals** at **$1,899/mo\*** and no product page. All medication-only; membership separate.
- **Testosterone — enclomiphene, two blends.** Hims's framing: it *"offers access to a daily oral medication that contains just enclomiphene or combines enclomiphene with tadalafil… offered in 3-, 5-, or 10-month plans"* [TT-FAQ]. Both live SKUs are branded **"Testosterone Rx+"** (compounded, not FDA-approved). One published anchor price for the line: **"starts at $99/month for a 10-month plan paid upfront and in full"** [TT-FAQ]. A daily-pill format only — **Hims states it does not offer TRT injections** today.
- **Announced, not buyable (testosterone).** Two FDA-approved T formats are shown as **"Coming in 2026"** — *testosterone cypionate* (once-weekly injection) and *Kyzatrex® (testosterone undecanoate)* (twice-daily oral pill). No price, no buy path → excluded from the buyable SKU count, listed in the roster's pipeline note.

**Visibility at a glance:** 0 offerings are truly `[published]` (a clean all-in price). The GLP-1 SKUs are best read as **`[partial]`** — a medication price shows, but the real all-in is gated by a mandatory $149/mo membership *and* an intake quiz before checkout. The testosterone SKUs are **`[on-request]`** — only a single line-level "starts at $99/mo" exists, no per-SKU price, and a lab kit + provider review gate the actual cost. The gating *is* the finding.

**Molecules covered (grouping attribute):** semaglutide · tirzepatide · orforglipron · enclomiphene (citrate) · enclomiphene + tadalafil. *(Pipeline-only, not counted: testosterone cypionate, testosterone undecanoate.)*

---

## Deep blocks (flagships only)

Two SKUs carry the line's weight. Everything else is captured fully in the Roster — no block.

### Wegovy® Pill — the homepage hero (semaglutide, oral)

The current front-of-site product (*"The GLP-1 pill is here"* banner; *"Same Wegovy®. New delivery."*). An **FDA-approved semaglutide pill**, once daily, *"clinically proven to help people lose 32 lbs in one year, on average"* [WP]. Priced as the **floor of the branded shelf at From $149/mo†** — deliberately matched to Ozempic® Pill and Foundayo™ to read as the accessible entry point, and undercutting the Wegovy® *Pen* ($199) to push oral.
**Visibility `[partial]`:** "$149/mo" is medication-only; the on-page "How it works" spells out the stack — *"Join the Hims Weight Loss Membership for only $39 in your first month, then $149/mo after that. Medication cost not included."* Real first-month outlay is membership + medication, and you cannot see the medication price confirmed without completing `/g/i/wm`. Slug: `/weight-loss/wegovy-pill`.

### Testosterone Rx+ (enclomiphene + tadalafil + supplements) — the TRT flagship (compounded)

Hims's lead testosterone SKU: a single **daily compounded pill** combining *enclomiphene* (to raise the body's own T), *tadalafil* (sexual performance), and a supplement blend (L-arginine, B6, B12, zinc). Positioned explicitly *against* TRT — *"no synthetic testosterone needed,"* fertility-preserving. **Compounded, not FDA-approved** (stated plainly on-page).
**Visibility `[on-request]`:** the PDP shows **no price at all**. The only number anywhere on the line is the FAQ's *"starts at $99/month for a 10-month plan paid upfront and in full"* — which (a) is line-level, not specific to this 3-in-1 SKU, and (b) describes the enclomiphene anchor. Checkout requires a **mandatory at-home lab kit + provider review** before any price is shown or treatment prescribed. The gate is the product. Slug: `/testosterone/enclomiphene-tadalafil-supplements`.

---

## Roster — buyable SKUs, pivoted by molecule

One row per buyable offering. **Price is verbatim** from the cited page (symbols preserved: `†`, `*`). **Visibility** is per-offering. **Slug** is the within-company key. Rows are grouped by the Molecule attribute (grouping only — not an identity claim).

| Molecule | Form | Branded / Compounded | Brand SKU name | Dose / strength | Price (verbatim) | Visibility | Slug |
|---|---|---|---|---|---|---|---|
| **semaglutide** | Oral (daily pill) | Branded | **Wegovy® Pill** | not stated on PDP (titration by provider) | **From $149/mo†** [WL-grid, WP] | `[partial]` ¹ | `/weight-loss/wegovy-pill` |
| **semaglutide** | Injectable (weekly pen) | Branded | **Wegovy® Pen** | "Range of dosages from 0.25mg–7.2mg" [WPen] | **From $199/mo†** [WL-grid, WPen] | `[partial]` ¹ | `/weight-loss/wegovy-pen` |
| **semaglutide** | Oral (daily pill) | Branded | **Ozempic® Pill** | not stated | **From $149/mo†** [WL-grid] — *also shown* **From $199/mo†** [WL-modal] ² | `[partial]` ¹ | `/weight-loss/ozempic-pill` |
| **tirzepatide** | Injectable (weekly vial) | Branded | **Zepbound® Vial** | not stated | **From $299/mo†** ("Starts at $299/mo") [WL-grid, ZV] | `[partial]` ¹ | `/weight-loss/zepbound-vial` |
| **tirzepatide** | Injectable (weekly pre-filled pen) | Branded | **Zepbound® KwikPen®** | not stated | **From $299/mo†** ("Starts at $299/mo") [WL-grid, ZV-table] | `[partial]` ¹ | `/weight-loss/zepbound-kwikpen` ³ |
| **orforglipron** | Oral (daily pill) | Branded | **Foundayo™ Pill** | not stated | **From $149/mo†** [WL-grid, FP] | `[partial]` ¹ | `/weight-loss/foundayo-pill` |
| **tirzepatide** | Injectable (weekly) | Branded | **Mounjaro®** | not stated | **$1,899/mo\*** [WL-modal] | `[partial]` ¹ ⁴ | *(no product page; modal only)* ⁴ |
| **tirzepatide** | Injectable (weekly pen) | Branded | **Zepbound®** (pen, distinct from Vial/KwikPen rows) | not stated | **$1,899/mo\*** [WL-modal] | `[partial]` ¹ ⁴ | *(no product page; modal only)* ⁴ |
| **enclomiphene** (citrate) + supplement blend | Oral (daily pill) | **Compounded** ⁵ | **Testosterone Rx+** (2-in-1: enclomiphene + supplements) | not stated; sold as 3-, 5-, or 10-month plans [TT-FAQ] | *no price on SKU page*; line anchor **"starts at $99/month for a 10-month plan paid upfront and in full"** [TT-FAQ] | `[on-request]` ⁶ | `/testosterone/enclomiphene-supplements` |
| **enclomiphene + tadalafil** + supplement blend | Oral (daily pill) | **Compounded** ⁵ | **Testosterone Rx+** (3-in-1: enclomiphene + tadalafil + supplements) | not stated; sold as 3-, 5-, or 10-month plans [TT-FAQ] | *no price on SKU page*; line anchor **"starts at $99/month for a 10-month plan paid upfront and in full"** [TT-FAQ] | `[on-request]` ⁶ | `/testosterone/enclomiphene-tadalafil-supplements` |

**Buyable SKU count: 10** (8 GLP-1 + 2 testosterone). The two `$1,899/mo*` GLP-1 SKUs are counted because they are presented as orderable (a "Get started" CTA into the same `/g/i/wm` intake), despite lacking a dedicated product page.

**Pipeline — not buyable, not counted** (testosterone line, both shown "Coming in 2026\*", no price, no buy path) [TT]:
- **testosterone cypionate** — injectable (once-weekly); FDA-approved format.
- **Kyzatrex® (testosterone undecanoate)** — oral (twice-daily pill); FDA-approved; *"Kyzatrex® is the registered trademark of Marius Pharmaceuticals, Inc."*

---

## Footnotes (price & visibility provenance)

¹ **GLP-1 `[partial]` rationale.** Each GLP-1 price is flagged **medication-only** with a mandatory, separately-billed membership, verbatim: *"**Price includes medication only, if prescribed.** An active Hims Weight Loss Membership is required ($39 for the first month, auto-renews at $149/month thereafter). Membership is billed separately and does not include or guarantee a prescription. Medication is not available without a membership. Membership fee is not included."* [WL-category †-note, ZV]. A price shows, but the true all-in (membership + medication) is gated and the medication price itself is only confirmed after the `/g/i/wm` intake quiz → `[partial]`, not `[published]`.

² **Ozempic® Pill — two different prices on one page.** The category product **grid** card reads **"From $149/mo†"** [weight-loss-category, grid]; the category **"Top Treatments" modal** for Ozempic® reads **"From $199/mo†"** with its own footnote *"$199 price includes medication only, if prescribed."* [weight-loss-category, modal]. Both captured verbatim; not reconciled — the discrepancy is the finding. (A separate grid card with no "View details" link also shows "From $199/mo†" with the Ozempic injectable image, consistent with the modal.)

³ **Zepbound® KwikPen® — priced, no captured PDP.** Listed in the medication menu [WL-FAQ], in the nav "Top Treatments" as a live SKU, and priced at **"Starts at $299/mo"** in the Zepbound® Vial PDP's side-by-side comparison table [zepbound-vial]. Its own page (`/weight-loss/zepbound-kwikpen`, linked repeatedly) was **not in this capture set** — price is from the comparison table and category grid, not a dedicated PDP.

⁴ **The two `$1,899/mo*` SKUs (Mounjaro®, a Zepbound® pen).** Appear **only** as on-page cards/modals on `/weight-loss` with a "Get started" CTA but **no "View details" / product-page link** (contrast the six core SKUs, which all link to a `/weight-loss/<slug>` PDP). Mounjaro® modal: *"A weekly GLP-1 injection that's FDA approved to help manage blood sugar levels… commonly prescribed off-label for weight loss,"* priced **$1,899/mo\*** [weight-loss-category, modal]. Slug is intentionally blank — **no within-company page key exists** for these in the capture; do not invent one.

⁵ **Compounded — verbatim, on both testosterone SKU pages:** *"Compounded drug products are not approved or evaluated for safety, effectiveness, or quality by the FDA. Rx required. Testosterone Rx is not available in all 50 states."* [enclomiphene-supplements, enclomiphene-tadalafil-supplements]. FAQ confirms: *"enclomiphene is not FDA-approved… only available through compounding pharmacies or clinical trials."*

⁶ **Testosterone `[on-request]` rationale.** Neither SKU page displays any price. The sole number is the FAQ line *"Pricing for low testosterone treatment with enclomiphene through Hims starts at $99/month for a 10-month plan paid upfront and in full"* [TT-FAQ] — line-level, not per-SKU, and not visible on the product pages themselves. Cost is further gated by a **mandatory at-home lab kit** (*"Lab testing is required to determine eligibility"*) + provider review before prescription. No price without intake + labs → `[on-request]`.

---

## Source pages (within-company; this capture)

All `https://www.hims.com/…`, fetched 2026-06-03 (firecrawl, maxAge:0, location:US); category pages are the 2026-05-30 warm copies.

- `/weight-loss` — **[WL-category / WL-grid / WL-modal / WL-FAQ]** category page: product grid, "Top Treatments" modals (Mounjaro®/Ozempic®/Zepbound®), the `†` medication-only note, and FAQ medication menu.
- `/weight-loss/wegovy-pill` — **[WP]**
- `/weight-loss/wegovy-pen` — **[WPen]** (the 0.25mg–7.2mg dose range)
- `/weight-loss/zepbound-vial` — **[ZV / ZV-table]** (includes the Vial-vs-KwikPen comparison table → KwikPen price)
- `/weight-loss/foundayo-pill` — **[FP]**
- `/testosterone` — **[TT / TT-FAQ]** category page: the two live blends, "Coming in 2026" injectables, and the $99/mo + "no TRT injections" FAQ answers.
- `/testosterone/enclomiphene-supplements` — 2-in-1 Testosterone Rx+ PDP.
- `/testosterone/enclomiphene-tadalafil-supplements` — 3-in-1 Testosterone Rx+ PDP.

**Not in this capture set:** `/weight-loss/zepbound-kwikpen` and `/weight-loss/ozempic-pill` dedicated PDPs (both linked on-site; KwikPen priced via the Vial comparison table, Ozempic via the category grid + modal). The all-in price for any SKU (behind `/g/i/wm` and `/g/i/tt` intakes) was not submitted.
