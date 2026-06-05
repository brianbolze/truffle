---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"                # the telehealth-pack version (independent of profile.md's)
domain: innerbalance.com             # company key (same as profile.md)
captured_at: 2026-06-04              # rode the profile capture (no extra scrapes)
value_chain_role: DTC brand          # a DTC women's-health telehealth brand selling its own compounded Rx products
pharmacy_model: third-party          # "compounded in partnership with a U.S.-licensed pharmacy" / "Our partner pharmacy" — partner, not owned; body Fulfillment carries the verbatim claim
audience: women-only                 # exclusively women's hormonal health — "made by women, for women"; never male-facing
compounding_posture: compounded-only # all four products compounded; not FDA-approved as compounds (some actives FDA-approved individually)
anchor_category: womens-HRT          # Oestra (bioidentical HRT) is the hero / front door — "Balance, prescribed"
modality: async                      # quiz → clinician review → ship; "no visit needed", no video front door
access_model: all-in                 # one monthly price includes treatment, pharmacy processing, shipping & unlimited clinical support — no separate membership fee
pay_model: HSA/FSA eligible          # no insurance ("It's not—…"); HSA/FSA accepted at checkout + letter of medical necessity; cash-pay otherwise
---

## Fulfillment
- **Pharmacy:** "Every Inner Balance prescription is compounded in partnership with a U.S.-licensed pharmacy held to the highest standards" — /science; "Our **partner pharmacy** is NABP-certified, LegitScript-certified, and PCAB-accredited" — /p/longevity/nad. A **partner** pharmacy (no named entity, no owned facility, no sibling pharmacy domain). **Lane:** predominantly **503A** — "Compounded in the USA by a national 503A pharmacy" (/p/longevity/nad), "503A U.S. pharmacy. NABP, LegitScript & PCAB certified" (/p/treatment/hrt, /pqp/anti-aging-face-cream). **But** one Oestra FAQ instead states "Oestra® is made by a **503B FDA-regulated compounding pharmacy** that's inspected by the FDA, DEA, and state licensing boards" (/p/treatment/hrt) — a page-attested 503A↔503B discrepancy, recorded verbatim, **not** adjudicated.

## Categories served
- **Categories:** womens-HRT (menopause · perimenopause · PCOS · endometriosis · postpartum) · sexual-health/libido · longevity/NAD · skin (anti-aging + facial-hair/finasteride)

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer seal + legitscript.com lookup); pharmacy accreditations cited for the partner pharmacy — **NABP-certified, PCAB-accredited** (/science, /p/longevity/nad). Named founder-physician **Dr. Sarah Daccarett, MD** (/p/about-us); the clinicians who review intakes are unnamed ("a licensed clinician/provider"). Third-party potency/purity tested; APIs from FDA-inspected facilities.
- **Controlled-substance Rx:** non-scheduled only — Oestra® (bioidentical **estradiol + micronized progesterone**; explicitly **no added testosterone** — "for women who truly require additional testosterone, our clinicians can evaluate that separately"), NAD+ (nicotinamide), Libida™ (bremelanotide + oxytocin), BodyMatched™ (estriol/tretinoin/niacinamide/finasteride). **No Schedule-III testosterone/TRT SKU** in the captured products.
- **Labs:** optional — "Lab work is not required to begin treatment. Your care is guided first and foremost by your symptoms… not just lab numbers"; optional lab testing offered, "a full clinical review of your results is included" (/p/treatment/hrt).
- **Payment & commitment:** **cash-pay**, not covered by insurance ("It's not—because insurance typically only covers the most limited options"); **HSA/FSA accepted at checkout** + a letter of medical necessity (/p/treatment/hrt). Cancel anytime; **6-month money-back guarantee** on Oestra (full refund within six months if not satisfied), **30-day** on the skincare 3-month plan. Subscription billed monthly against a multi-month supply (Oestra: 90-day supply every 90 days, billed monthly).
