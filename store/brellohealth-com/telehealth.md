---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"                    # the telehealth-pack version (independent of profile.md's)
domain: brellohealth.com                 # company key (same as profile.md)
captured_at: 2026-06-04                  # rode the 2026-06-04 profile capture (no extra scrapes)
value_chain_role: DTC brand              # a consumer-facing compounded-Rx wellness brand; sells care+meds direct, not a pharmacy/lab/platform supplier
pharmacy_model: third-party              # "USA based 503A Partner Pharmacy" — explicitly a partner, not owned (body Fulfillment carries the verbatim claim)
audience: women-only                     # site is exclusively women-facing ("We help women transform their lives"); no men's path/imagery — meds aren't sex-specific (see Audience)
compounding_posture: compounded-only     # every SKU is "Compounded X" + FDA not-approved disclaimers; no FDA-brand drugs
anchor_category: GLP-1                    # weight-loss is the front door (hero, all testimonials, GLP-1 in every bundle); A/B/countdown-driven — point-in-time
modality: async                          # buy → online intake questionnaire → provider review of your info; no video/sync consult stated
access_model: all-in                     # one plan price includes consult + medication + app + classes; no separate membership fee
pay_model: cash-pay only                 # "Priced for out-of-pocket payers… no membership fee"; FSA self-reimbursement via superbill only (body)
---

## Fulfillment
- **Pharmacy:** "Shipped from a USA based **503A** Partner Pharmacy" (homepage); "your medication will be shipped to your doorstep by **our partner pharmacy**" (every PDP). Page-attested as a **503A** (patient-specific compounding) **partner** — third-party, **not owned and never named**. The homepage marquee adds the partner "is transitioning to a new, larger facility," causing shipping delays — so fulfillment is outsourced, not an owned facility. No 503B/outsourcing-facility lane claimed.

## Categories served
- **Categories:** GLP-1/weight-loss · longevity/NAD+ · peptides/sermorelin (GH-secretagogue) · metabolic-tracking (Lumen device bundle). All compounded, all injectable.

## Audience
- **Audience:** exclusively **women-facing** — homepage hero "We help **women** transform their lives through clinician prescribed longevity medicine," bundles "Curated bundles for **women** who are done doing it alone," PDP copy "some **women** report," and all-women beach/lifestyle imagery (midlife-leaning). There is **no men's hub, product, or imagery**. Note: the compounded meds (GLP-1, NAD+, sermorelin) are **not sex-specific** — the women-only stance is an audience/marketing choice, not a clinical gate.

## Credibility & access
- **Health-merchant credibility:** **No LegitScript seal observed** in the captured footer (its absence noted honestly, not asserted either way). **Named clinicians: yes** — provider/coach bios at `/health-guide/bio` and `/bio/*` (e.g., Dr. Stephanie Chan), a "Brello Care Team." **Trustpilot 4.1/5, "3,860 reviews"** (self-embedded TrustBox; recorded, not endorsed). Pharmacy accreditation (PCAB/NABP/ACHC): **not shown**.
- **Controlled-substance Rx:** **non-scheduled only** — compounded semaglutide/tirzepatide (GLP-1), NAD+, and sermorelin are all non-scheduled; **no TRT/testosterone SKU** in the catalog (the product-card filenames `At-Home-Testosterone-Test-*.png` are **reused image assets**, not an actual testosterone product).
- **Labs:** **none required** — the journey is buy → intake questionnaire → provider review → ship; no at-home test kit or partner-lab draw is mentioned as a step.
- **Payment & commitment:** **cash-pay only** — "Priced for out-of-pocket payers with no increase as dose goes up and **no membership fee**" (homepage testimonial); does not bill insurance/HSA. FSA touch is **self-service only**: a member testimonial notes Brello "provided a summary of services for my FSA account reimbursement" (a self-submitted superbill, not a merchant-accepted HSA/FSA rail). Commitment: **3-month minimum**, charged upfront, then auto-renews **every 10 weeks** (sermorelin: **every 11 weeks**); **cancel anytime**. Refunds: full refund if **not approved**; if cancelled after the provider writes a prescription, refund "less a **$50 professional services fee**" within 24h of the completed review.
