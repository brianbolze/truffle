# Remedy Meds — offerings

> Design **B1 — roster-first** (incumbent, 2026-06-01). Source: captured pages under `captures/remedymeds-com/` only. Prices verbatim; visibility token per offering. Within-company key = page slug. No cross-company canonical key, no cross-brand equivalence asserted.

## Portfolio overview

**One vertical — medical weight loss via compounded GLP-1 — sold as four plan variants of a single month-to-month membership.** No TRT/testosterone or any non-weight-loss line appears on any captured page; this is a single-funnel site where every CTA points to `/quiz`. Pricing is marketed all-in (medication + unlimited clinician care + free labs + shipping + community), and the homepage strip reads "No Memberships or Hidden Fees" — even though the patient manual repeatedly calls the recurring charge a "membership" billed automatically every 28 days.

The four variants form a single titration ladder, sorted by dose intensity / entry friction:

```
Medical weight loss (GLP-1)  — membership, billed every 28 days
├─ Microdose Plan        "Easiest Entry"     — same molecule, half-dose 2×/week   [on-request]
├─ Semaglutide           "Best First Step"   — $299/mo                            [published]
├─ Tirzepatide           "64% of members"    — from $399/mo                       [published]
└─ Branded (Ozempic® / Zepbound®)  "Retail Pricing" — name-brand option           [on-request]
```

**The split that matters for this roster: which variants have a real, greppable price and which gate it.** Only the two compounded injectables get their own product page with a published monthly price (Semaglutide $299, Tirzepatide $399). The two "edge" variants — Microdose and Branded — appear *only* as homepage cards with no price string at all; their price is reachable only by completing the quiz. The gating is itself the finding: the catalog the site *shows* is two-priced; the catalog it *sells* is four, two of them price-opaque.

## Deep blocks

The two flagship offerings — the only ones with a dedicated product page and a published price, and the two most-compared (sema = "Best First Step," tirz = "64% of members use this").

---

### Semaglutide — compounded GLP-1 injectable

- **Parent:** Medical weight loss (GLP-1 membership)
- **URL (slug):** `/medication/comp-sema-inj`
- **Price:** **$299/month** · `[published]`
- **Kind:** buyable

**Page H1:** "Semaglutide" — subhead "Compounded GLP-1"

**Exact price strings (verbatim):**
> "Monthly1 Month" → "**$299/month**"

On its own product page the plan-comparison block also states:
> "Starting at**$299/mo.**" / "Less than $9/day."

**What it is (verbatim):**
> "1 Month supply of injections for weight loss with proven GLP-1 results"
> "Your first step. A once-weekly injection that quiets food noise, reduces cravings, and supports steady weight loss from day one."
> Type label: "GLP-1 receptor agonist"

**Best for (verbatim):** "You've never tried GLP-1s before" · "You want steady, consistent progress"

**Header claim on page:** "America's #1 GLP-1 care platform, 200,000+ users, 400,000+ prescriptions." · badge "In-Stock"

**Member-result claims (self-reported, flagged on page):** "Remedy members lose **45 lbs** in their first 6 months"; "Top responders lose **65 lbs** in 12 months." Footnote: "Results are based on self-reported data from ~300,000 Remedy Meds members … Individual results may vary."

---

### Tirzepatide — compounded GLP-1 injectable

- **Parent:** Medical weight loss (GLP-1 membership)
- **URL (slug):** `/medication/comp-tirz-inj`
- **Price:** **$399/month** (product page) / "Starting at $399/mo." (card) · `[published]`
- **Kind:** buyable

**Page H1:** "Tirzepatide" — subhead "Compounded GLP-1"

**Exact price strings (verbatim):**
> "Monthly1 Month" → "**$399/month**"

Plan-comparison block (appears on homepage and on the sema page):
> "Starting at**$399/mo.**" / "Less than $13/day."

**What it is (verbatim):**
> "1 Month supply of injections for weight loss with dual power and greater results"
> "Our strongest compounded option. Targets both hunger and insulin pathways for faster and more effective results when your body needs more."
> Type label: "Dual GIP + GLP-1 agonist"

**Positioning flag (verbatim):** "On GLP-1 or hit a plateau?64% of members use this" · "Designed for less side effects"

**Best for (verbatim):** "Breaking through weight loss plateaus" · "Need stronger appetite control"

**Member-result claims (self-reported, flagged on page):** "Remedy members lose **50 lbs** in their first 6 months"; "Top responders lose nearly **76 lbs** in 12 months." Same ~300,000-member self-reported-data footnote.

---

## Roster

Complete at the indexed level — every GLP-1 offering surfaced on the captured pages. No TRT/testosterone offering exists on this site.

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (one line) |
|---|---|---|---|---|---|---|
| **Medical weight loss (GLP-1)** | family | — (root) | `/` | — (membership, "charged automatically every 28 days") | `[partial]` | The single vertical: compounded-GLP-1 weight-loss membership, all-in (med + unlimited care + free labs + shipping); marketed "No Memberships or Hidden Fees." |
| **Semaglutide** | buyable | Medical weight loss (GLP-1) | `/medication/comp-sema-inj` | "$299/month"; "Starting at $299/mo." / "Less than $9/day." | `[published]` | Once-weekly compounded GLP-1 receptor agonist injection; "Best First Step" for GLP-1-naïve members. |
| **Tirzepatide** | buyable | Medical weight loss (GLP-1) | `/medication/comp-tirz-inj` | "$399/month"; "Starting at $399/mo." / "Less than $13/day." | `[published]` | Once-weekly compounded dual GIP + GLP-1 agonist injection; "strongest compounded option," "64% of members use this." |
| **Microdose Plan** | buyable | Medical weight loss (GLP-1) | (no own page; homepage card → `/quiz`) | *no price shown* | `[on-request]` | "Same medication — half the dose, twice a week"; GLP-1 receptor agonist micro-titration, "Easiest Entry" for injectable-naïve / side-effect-sensitive users. Price quiz-gated. |
| **Branded (Ozempic® / Zepbound®)** | buyable | Medical weight loss (GLP-1) | (no own page; homepage card → `/quiz`) | *no price shown* — labeled "Retail Pricing" | `[on-request]` | Name-brand GLP-1 option ("Want a name brand?"); single card lists Ozempic® and Zepbound®, one "Start name brand" CTA. Price quiz-gated. |

**Notes on the roster:**
- **Slug key.** Only Semaglutide and Tirzepatide have real `/medication/*` slugs in the capture. Microdose and Branded have no dedicated page — they exist solely as homepage plan-cards routing to `/quiz`. Their parenthetical "slug" records that absence, not an invented path.
- **Family-row visibility = `[partial]`** by the per-offering rule: the membership is the all-in unit, two of its variants publish a monthly price while the real all-in for the other two is gated behind the quiz — a price shows for the line, but the full picture is not uniformly published.
- **Branded as one row.** The site presents Ozempic® + Zepbound® as a single "name brand" card with one CTA and one "Retail Pricing" label; it is recorded as one buyable with both molecules noted, rather than split into two SKUs the page does not itemize.
- **Molecule/form** lives in the What column: semaglutide and tirzepatide are the two compounded molecules; Microdose is the same compounded molecule(s) at a split half-dose; Branded is the name-brand forms (semaglutide-as-Ozempic®, tirzepatide-as-Zepbound®). No cross-brand equivalence is asserted as stored fact.
- **Add-ons / bundle (not separate buyables; "all-in," no stated extra cost):** medication, syringes + alcohol pads (injectables), free shipping, free lab work (TSH, A1C, CMP, lipid panel via Quest/LabCorp/Bioreference), unlimited clinician + nursing-line access (video + chat), monthly live expert sessions, recipes/meal plans, a 10,000+-member community, and a "365-Day Money-Back Guarantee" / "Weight Loss Warranty."
- **Billing reality (patient manual, verbatim):** "Your membership is charged automatically every 28 days"; "entirely month-to-month with no minimum contracts"; **"once a prescription has been written, we are unable to issue a refund."**
