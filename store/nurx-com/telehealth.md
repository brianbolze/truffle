---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: nurx.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: integrated            # "Our pharmacy fills…"/"our partner pharmacy" (mail-order); branded GLP-1 routed to a 3rd-party local pharmacy — see Fulfillment
audience: women-only                  # 100% women-framed nav/hero/copy; men pointed to sibling Keeps. (Some conditions aren't inherently gendered — see note)
compounding_posture: FDA-brand-only   # all meds FDA-approved brand/generic; GLP-1s are all branded pens; no compounded lane shown
anchor_category: multi/none           # co-equal women's-health grid; heritage lead = birth control (not a closed-set value), promo bar pushes GLP-1 — rotation flagged
modality: async                       # front-door = online consultation + photos; no scheduled video visit in the flow
access_model: à-la-carte/both         # no required membership; per-line consult fee + (some lines) a recurring care/support fee
pay_model: bills insurance            # 7 private payers named + FSA/HSA eligible; cash-pay where not covered
---

## Fulfillment

- **Pharmacy (captive + partner, claimed):** "Our pharmacy fills your birth control prescription and sends a three-month supply straight to your doorstep" (/birthcontrol/); "Our pharmacy will fill the prescription and mail medication to your home" (/acne-treatment/); and "Certain medications are fulfilled by **our partner pharmacy** and mailed directly to your home" (/weight-management-treatment/). The self-description toggles between "our pharmacy" and "our partner pharmacy" — coarse posture `integrated` (owned-or-captive, page can't disambiguate); Nurx is a **Thirty Madison** company, which operates pharmacy infrastructure. Claim recorded, not verified.
- **Branded GLP-1 = third-party local pharmacy:** "Branded GLP-1s are not available for shipment via our pharmacy. These medications can be filled at the pharmacy of your choice" / "In-person pharmacy pick up only" (/weight-management/glp1-injections/). For this line Nurx is a prescriber + clinician-fee layer, not the dispenser.
- **EC routing option:** for prescription Ella, "We can also send the prescription to a local pharmacy of your choice for you to pick up" (overnight delivery also offered). Lane (503A/503B): **not stated** (no compounding claimed).

## Categories served

- **Categories:** birth-control/contraception · emergency-contraception · GLP-1/weight-management · mental-health · skin (acne · anti-aging · eyelash · melasma · rosacea) · sexual-health (cold sore · genital herpes) · hair (women's hair loss · dandruff) · general/urgent (bacterial vaginosis · vaginitis · yeast infection · UTI · menopause) · migraine (routed to sibling Cove). "150+ prescription treatment options."

## Credibility & access

- **Health-merchant credibility:** **named clinicians — yes** (/team/: Dr. Peter Young, Medical Director; Cristin Hackel, WHNP; Dr. Neil Zlatniski, Medical Director; Dr. Crystal Jacovino, VP Clinical Operations; Dr. Marie Leger, MD, PhD, FAAD on the hair page), described as an "independent medical organization." **LegitScript / pharmacy accreditation (PCAB/ACHC/NABP): not shown** in captured pages. Trustpilot rating shown (4.5; "1,874+ Nurx-wide reviews", "26k+ reviews all time"); "2M+ patients served" (self-reported).
- **Controlled-substance Rx:** **non-scheduled only** — "Nurx does not prescribe benzodiazepines (such as Xanax®, Valium®, and Ativan®), stimulants (such as Adderall® or Concerta®), or any controlled substances" (/mental-health/). No TRT/testosterone line (women's brand).
- **Labs:** **none** as a required step or sold product in the current nav. Marketing copy references "tests" ("prescriptions and tests delivered"; team page: "vital medications and tests") — a legacy at-home-testing posture not represented in the captured catalog. Skin/hair consults use uploaded **photos**, not labs.
- **Payment & commitment:** **bills insurance** — "we accept most forms of private health insurance for medications, including Aetna, Anthem, Blue Cross Blue Shield, Cigna, CVS Caremark, Express Scripts, OptumRx, United Health Care"; **FSA/HSA eligible**. Cash-pay where insurance doesn't cover (anti-aging, melasma, eyelash, women's hair loss, and all weight-management care fees — "The care fee is cash pay only"). Commitment: "Pause or cancel anytime"; medication "shipped and billed monthly or quarterly."

### Notes
- **Audience nuance:** classified `women-only` on the brand's framing (every line is women-positioned; men are redirected to sibling Keeps). Several conditions (mental health, weight management, acne, herpes) are not inherently gendered — Nurx simply markets them within a women's-health frame. The App Store listing ("Nurx — birth control and PrEP") points to a historical all-genders PrEP line that is **absent from the current site**.
- **Anchor rotation:** `anchor_category` is a point-in-time read. The persistent top promo bar pushes weight management ("$0 with insurance"); the mega-nav and hero carousel still lead with birth control. Recorded as `multi/none` because the front door is a co-equal women's-health grid and the heritage lead (birth control) has no closed-set value.
