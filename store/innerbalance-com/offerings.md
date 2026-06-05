---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: innerbalance.com       # company key; each offering's slug (its relative url) is its key *within* the company
captured_at: 2026-06-04        # own freshness; captures/2026-06-04/ holds the source pages
site_notes: "Four flagship compounded products, each with its own product page + a `/quiz/<x>` intake funnel. Prices are PUBLISHED as 'From $X/mo' floors on the product pages (the skincare /pqp page + the Oestra /p/treatment/hrt page show full plan tiers; NAD+ & Libida show a single floor only — dose/plan tiers sit behind the quiz). Molecules are page-attested on each product page. A/B: Optimizely → prices/promos (20%/15% off) are point-in-time. ⚠ On /pqp/anti-aging-face-cream the $60–$120, $30–$60, $100–$300, and $250–$500 figures are COMPETITOR/DIY comparison anchors ('what women typically spend'), NOT Inner Balance prices — IB's price is $199/mo or $249/3-mo ($83/mo), +$20 finasteride."
---

## Portfolio overview

**Flagship + companions.** **Oestra®** (bioidentical HRT cream) is the hero — tagged "Bestseller" on /science, the homepage hero, and the brand-namesake intake (`/quiz/hormone-imbalance`) **[HIGH]** (the company's own label + corroborated hero). Three companions sit one rung down in the "Our Products" grid and carry standing promo badges: **Libida™** (20% off), **NAD+** (15% off), **BodyMatched™** anti-aging skincare **[MED]** (nav-grid order + promo badges; A/B-rotating). All four are **compounded prescription** products on a monthly **subscription**, and all four **publish a price floor** on their product page — unusual for compounded telehealth, where intake-gating is the norm. The "conditions" in the nav (menopause, perimenopause, PCOS, endometriosis, postpartum) are **Oestra applications, not separate SKUs**.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Oestra® | buyable | — | /p/treatment/hrt | "$199/month = $7/day for the first 6 months" → "$99.50/month = $3/day" ongoing | published | estradiol + micronized progesterone (bioidentical) · vaginal cream, one daily pump · Rx via /quiz/hormone-imbalance; 90-day supply every 90 days, billed monthly; **no added testosterone** |
| Libida™ | buyable | — | /p/sexual-wellness/libida | "From $99.70/mo" (20% off) | published | bremelanotide + oxytocin · sublingual tablet, on-demand · Rx via /quiz/libida; non-hormonal; onset 30–60 min, ≤1 tablet / 72h |
| NAD+ | buyable | — | /p/longevity/nad | "From $183/mo" (15% off) | published | NAD+ (nicotinamide adenine dinucleotide) 200mg/serving · sublingual tablet, daily · Rx via /quiz/nad; needle-free |
| BodyMatched™ Anti-Aging Face Cream | buyable | — | /pqp/anti-aging-face-cream | "$199 every month" ($199/mo) · "$249 every 3 months" ($83/mo, "Most Savings") | published | estriol + tretinoin + niacinamide (compounded) · face cream, once daily · Rx via /quiz/anti-aging-face-cream; vegan, fragrance-free |
| BodyMatched™ + Finasteride | buyable | BodyMatched™ Anti-Aging Face Cream | /pqp/anti-aging-face-cream | "Include Finasteride (+$20)" | published | + topical finasteride (DHT-modulating; targets facial hair, oil, acne) · optional "Clinical Strength Upgrade" add-on on the base cream |

### Verbatim anchors

- **Oestra price (/p/treatment/hrt):** "$199/month = $7/day for the first 6 months" · "Then $99.50/month = $3/day" · "90-day supply shipped every 90 days, billed monthly. Cancel anytime." · "Your membership includes treatment, pharmacy processing, shipping, and unlimited clinical support."
- **Oestra molecule (/p/treatment/hrt):** "Bioidentical Estradiol + Micronized Progesterone"; "Oestra® delivers bioidentical estradiol and progesterone in one balanced cream"; "Oestra® does not contain added testosterone… restores progesterone — which serves as a precursor."
- **Libida price + molecule (/p/sexual-wellness/libida):** "From $99.70/mo" · "20% off" · "A brain-boosting libido peptide – enhanced with Oxytocin"; "bremelanotide (Libida's active ingredient)"; "Libida™ contains no estrogen, progesterone, or testosterone."
- **NAD+ price + molecule (/p/longevity/nad):** "From $183/mo" · "NAD+ 200mg per serving, sublingual for optimal absorption"; "NAD+ (nicotinamide adenine dinucleotide)."
- **BodyMatched price + molecule (/pqp/anti-aging-face-cream):** "Monthly Plan — $199 every month — $199/mo" · "3-Month Plan — $249 every 3 months — $83/mo — Most Savings" · "Include Finasteride (+$20)" · "From $83/mo" · "Estriol. Tretinoin. Niacinamide. Finasteride."
- **⚠ Competitor/DIY anchors (NOT IB prices), /pqp/anti-aging-face-cream:** "Prescription tretinoin $60–$120/month," "Estriol cream $60–$100/month," "Niacinamide or corrective serum $30–$60/month," "Facial hair treatments (laser or electrolysis) $100–$300/month," "Realistic combined cost: $250–$500/mo" — framed as "what women typically spend" to achieve similar results, contrasted against IB's $83/mo.

## Deep blocks

- **PDP-template anatomy (one block — the whole catalog repeats it).** All four product pages share a near-identical shell, so reading one teaches the catalog: **hero** (product name + one-line promise + "HSA/FSA eligible") → **trust badges** (503A Pharmacy · FDA-Inspected · Made in USA · Third-Party Tested · NABP · LegitScript · PCAB) → **mechanism** ("Why it works" / ingredient breakdown) → **"vs injection/other" comparison table** → **patient testimonials** ("Verified patient") → **"Meet Dr. Sarah" clinical Q&A accordion** → **"From $X/mo" pricing card** (cancel anytime · free shipping · unlimited clinical follow-up · HSA/FSA · no insurance) → **"Start in minutes" 3–4 step how-it-works** → **FAQ accordion**. The skincare page (`/pqp/`, a "product-quiz page") is the exception: it surfaces **on-page plan selection** (Monthly vs 3-Month) + the finasteride upgrade toggle before the quiz, where the others route straight to `/quiz/<x>`.

- **Hero product renders (opt-in asset, full-pack request).** Clean isolated product renders captured to `captures/2026-06-04/images/` — the brand's own white-background product shots (240×240 source; skincare 150×144):
  - `images/oestra.webp` — Oestra® jar + "BodyMatched Oestra™ 3 month supply" box
  - `images/libida.webp` — Libida™ purple tin ("Libido support w/ Oxytocin Synergy") + tablets
  - `images/nad.webp` — NAD+ teal tin ("Longevity support") + tablets
  - `images/bodymatched-skincare.webp` — BodyMatched™ dual white/blue pump bottles

## Provenance

- **Pages:** /p/treatment/hrt, /p/sexual-wellness/libida, /p/longevity/nad, /pqp/anti-aging-face-cream (+ homepage & /science for the product grid + "Bestseller" prominence). Firecrawl, basic proxy.
- **Scope:** all four flagship products enumerated + the finasteride add-on variant (5 rows). The nav "conditions" (menopause/perimenopause/PCOS/endometriosis/postpartum) are Oestra applications, not separate SKUs, so not rostered.
- **Gated / couldn't get:** exact dose tiers and final checkout price for each product sit behind the `/quiz/<x>` intake; only the published "From $X/mo" floors are captured.
- **Point-in-time:** Optimizely A/B + standing promo badges (20%/15% off) rotate run-to-run — prices/promos are a snapshot, not fixed.
- **Run profile:** non-vanilla — full-pack request: added the **PDP-template anatomy** deep block and **hero product renders** (4 images) beyond the default roster.
