# Remedy Meds — offerings (B2: molecule-pivoted)

**Domain:** remedymeds.com · **Portfolio shape:** Single (one vertical — medical weight loss via GLP-1) · **Captured:** 2026-06-01
**Design B2** — molecule-grouped price comparison. `Molecule` is a per-offering **attribute** for query-time grouping (greppable), **not** a stored canonical entity; the within-company key is the page **Slug**. No cross-brand equivalence is asserted.

> **Scope finding:** This site is GLP-1 weight-loss **only**. There is **no TRT / testosterone / men's-health line** anywhere in the captured pages — the entire site is a single female-skewed weight-loss funnel. TRT rows are therefore absent because the offering does not exist here, not because pricing was gated. See Notes.

---

## Portfolio overview

One vertical, sold as four plan variants of a single all-in subscription (medication + unlimited clinician/care-team access + free labs + free shipping + community, auto-billed every 28 days). All CTAs route to `/quiz`.

- **Two families have published prices**, each on its own product page:
  - **Compounded Semaglutide** — once-weekly GLP-1, "Best First Step" — **$299/month** `[published]`
  - **Compounded Tirzepatide** — dual GIP+GLP-1, "Our strongest compounded option," "64% of members use this" — **$399/month** `[published]`
- **Two variants are price-gated** (homepage cards only, no product page, no number anywhere — CTA goes straight to the quiz):
  - **Microdose Plan** — "same medication — half the dose, twice a week," micro-titration entry — **price not shown** `[on-request]`
  - **Branded name-brand** (Ozempic®, Zepbound®) — card labeled "Retail Pricing" — **price not shown** `[on-request]`

**Molecules covered (attribute, for grouping):** semaglutide, tirzepatide. (Branded cards name Ozempic® = semaglutide-class and Zepbound® = tirzepatide-class by their manufacturer labeling, but the site states no molecule and no price for them — treated as their own gated SKUs below, not merged into the compounded rows.)

**Pricing posture:** all-in, cash-pay, HSA/FSA eligible, month-to-month. The site markets "No Memberships or Hidden Fees," yet the patient manual calls the recurring charge a "membership" billed "automatically every 28 days" and states **"once a prescription has been written, we are unable to issue a refund."** Compounded-only ("the FDA has not evaluated the medications for safety, quality, or efficacy").

---

## Deep blocks (flagships only)

Only the two published-price compounded plans get a block; the gated variants are roster rows (the gating is the whole finding).

### Compounded Semaglutide — `[published]`
- **Slug:** `/medication/comp-sema-inj` · **Molecule:** semaglutide · **Form:** injection (once-weekly) · **Branded/Compounded:** Compounded
- **Price (verbatim):** page header — **"$299/month"** (label "Monthly / 1 Month," "1 Month supply of injections"). Cross-sell card — **"Starting at $299/mo."**, **"Less than $9/day."**
- **Positioning (verbatim):** "Compounded GLP-1"; "GLP-1 receptor agonist"; "Best First Step"; "New to GLP-1s? → Start here." "A once-weekly injection that quiets food noise, reduces cravings, and supports steady weight loss from day one."
- **Member-results claims (self-reported, flagged):** "Remedy members lose **45 lbs** in their first 6 months"; "Top responders lose **65 lbs** in 12 months." Based on self-reported data from ~300,000 members; "Individual results may vary."

### Compounded Tirzepatide — `[published]`
- **Slug:** `/medication/comp-tirz-inj` · **Molecule:** tirzepatide · **Form:** injection (once-weekly) · **Branded/Compounded:** Compounded
- **Price (verbatim):** page header — **"$399/month"** (label "Monthly / 1 Month," "1 Month supply of injections"). Cross-sell card — **"Starting at $399/mo."**, **"Less than $13/day."**
- **Positioning (verbatim):** "Compounded GLP-1"; "Dual GIP + GLP-1 agonist"; "Our strongest compounded option. Targets both hunger and insulin pathways…"; "On GLP-1 or hit a plateau? **64% of members use this**."
- **Member-results claims (self-reported, flagged):** "Remedy members lose **50 lbs** in their first 6 months"; "Top responders lose nearly **76 lbs** in 12 months"; "Designed for less side effects." Same ~300,000-member self-reported basis.

---

## Roster — molecule-pivoted (one row per buyable SKU)

Sorted by molecule, then by visibility (published first). `Price` is verbatim from the captured page. `Slug` is the within-company key; where no product page exists, the buyable locator is the quiz route and is flagged `(no product page; → /quiz)`.

| Molecule | Form | Branded/Compounded | Brand SKU name | Dose/strength | Price (verbatim) | Visibility | Slug |
|---|---|---|---|---|---|---|---|
| semaglutide | injection, once-weekly | Compounded | Semaglutide ("Best First Step") | not specified (clinician-titrated; "1 Month supply") | **"$299/month"** (card: "Starting at $299/mo." / "Less than $9/day.") | `[published]` | `/medication/comp-sema-inj` |
| semaglutide | not specified | Branded | Ozempic® ("Retail Pricing") | not specified | — (no price shown) | `[on-request]` | `(no product page; → /quiz)` |
| tirzepatide | injection, once-weekly | Compounded | Tirzepatide ("strongest compounded option") | not specified (clinician-titrated; "1 Month supply") | **"$399/month"** (card: "Starting at $399/mo." / "Less than $13/day.") | `[published]` | `/medication/comp-tirz-inj` |
| tirzepatide | not specified | Branded | Zepbound® ("Retail Pricing") | not specified | — (no price shown) | `[on-request]` | `(no product page; → /quiz)` |
| semaglutide *or* tirzepatide (unstated) | injection, twice-weekly | Compounded | Microdose Plan ("Easiest Entry") | "half the dose, twice a week" (micro-titration) | — (no price shown) | `[on-request]` | `(no product page; → /quiz)` |

**Row-count note (5 SKU rows):** the homepage presents Microdose as one card and "Want a name brand?" as **one** card naming **two** drugs (Ozempic®, Zepbound®). I split the branded card into two rows because they are distinct brand SKUs with distinct molecules; if you prefer to count buyable *cards*, that collapses to 4 (sema, tirz, microdose, branded). I report **5 distinct buyable SKUs**.

Molecule assignment for the branded rows reflects each drug's manufacturer labeling **as a query-time attribute only** — the Remedy Meds pages state no molecule for these cards. This is not a claim that Remedy's branded SKU "is the same product as" any other brand's.

---

## Notes (gated / unreachable / caveats)

- **No TRT/testosterone offering exists on this site.** Every captured page (homepage, both medication pages, quiz shell, patient manual) is GLP-1 weight loss. The brief asked for "every GLP-1 and TRT/testosterone offering"; the TRT half returns **zero** — a genuine absence, not a capture gap.
- **Microdose Plan — `[on-request]`:** appears only as a homepage card (and a "New!" banner). No price is shown anywhere in the capture; CTA "Start Microdose" → `/quiz`. The molecule is left unstated by the site ("same medication" — ambiguous as to sema vs tirz). The gating *is* the finding.
- **Branded Ozempic® / Zepbound® — `[on-request]`:** one homepage card labeled "Want a name brand? → Retail Pricing." No price shown; CTA "Start name brand" → `/quiz`. Captured as two SKU rows.
- **Dose/strength not published** for any SKU. Dosing is clinician-titrated post-quiz; product pages say only "1 Month supply of injections." No mg/mL strengths anywhere in the capture.
- **`/quiz` is a thin SPA shell** (captured body is a 4-option intake screen, no static pricing) — confirms the gated prices live behind the quiz/app and were not reachable in a static scrape.
- **"From"/floor language:** the cross-sell cards say "Starting at $299/mo." / "Starting at $399/mo.", but each med's own product page shows a flat "$299/month" / "$399/month" header for a 1-month supply. Both kept verbatim; treated as `[published]` (a real number is shown, all-in by the brand's own "everything included" claim) rather than `[partial]`, since there is no separate mandatory add-on fee disclosed — the med price is the membership.
- **Self-reported metrics:** all weight-loss figures (45/50/65/76 lbs, "94.6%", "2x faster", "-14 lbs") are member-reported per the on-page disclaimers; testimonial members "were compensated." Not independent data.
- **Source pages (within-company, this capture):** `/` (homepage), `/medication/comp-sema-inj`, `/medication/comp-tirz-inj`, `/quiz`, `/documents/getting-started` (patient manual). All prices above trace to the homepage and the two medication pages.
