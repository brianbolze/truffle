---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: invigormedical.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: third-party              # 5 named partner pharmacies; no owned facility claimed
audience: all-genders                    # "Online Women's and Men's Health Clinic"; sexual-health/TRT skew male (body note)
compounding_posture: both                # compounded majority + generic oral molecules (sildenafil/tadalafil/finasteride) + a retail pharmacy partner
anchor_category: multi/none              # 3 co-equal pillars + rotating hero — generalist, no single front door
modality: async                          # "100% online" consult; provider "will contact you" modality unspecified (body note)
access_model: à-la-carte/both            # no membership; "flexible, no-commitment" individual treatments
pay_model: unclear                       # no HSA/FSA/insurance/cash-pay language found across 11 captured pages
---

## Fulfillment

- **Pharmacy (third-party, named):** *"We bring together our team of licensed physicians and our partnered national pharmacies on a HIPAA-compliant, secure platform"* (/about-invigor). The about page names five **"Partnered Pharmacies": Strive Pharmacy, Tailor Made, Belmar Pharma Solutions, Olympia Pharmacy, and Gogomeds** — four compounding pharmacies plus a retail/mail pharmacy (Gogomeds). No owned pharmacy or in-house facility is claimed.
- **Compounding lane (503A, stated):** every captured Rx PDP carries *"Invigor Medical does not supply FDA-approved branded medications. Instead, compounded alternatives may be prescribed when clinically appropriate and legally permissible. These medications are prepared by **licensed 503A pharmacies** in accordance with the Federal Food, Drug, and Cosmetic Act."* Quality line: *"Our partner compounding pharmacies work with a registered and certified third-party lab to run quality control checks for every lot… sterile compounded medications are free from microbial contamination."* No 503B/outsourcing-facility claim. (Claim only — ownership/lane never adjudicated.)
- **Posture nuance:** predominantly compounded (GLP-1, Trimix, PT-141, NAD+, sermorelin, oxytocin, TRT), with generic oral molecules (sildenafil, tadalafil, finasteride, enclomiphene, metformin-class) and a named retail pharmacy partner → `both`. The "no FDA-approved *branded*" statement is about brand-name drugs, not generics.

## Categories served

- **Categories:** weight-loss/GLP-1 · TRT · sexual-health/ED · libido · longevity/NAD · peptides (sermorelin · GHK-Cu · PT-141 · methylene blue · glutathione) · hair (finasteride · follicle fuel · ReGrow) · B12/vitamins

## Credibility & access

- **Health-merchant credibility:** LegitScript-certified (footer seal `legit-script.webp`, y); named clinicians **Andrew Hamilton, DO** and **Stephen Jones, MD** (homepage "Meet Our Dedicated Experts," y — no dedicated `/physicians` roster page); pharmacy accreditation (PCAB/NABP) **not shown** on Invigor's own site (partner pharmacies named but no seals displayed). "50 States Licensed"; "HIPAA-compliant, secure platform."
- **Controlled-substance Rx:** offers **Schedule-III (testosterone / TRT)** — page-attested by the TRT injection plan (`/plans/testosterone-replacement-therapy-injection/`, "Now Offering Testosterone Replacement Therapy"). Backed by the product appearing, not an asserted DEA schedule.
- **Labs:** **required-step for TRT** — *"$49 Lab Fee Fully Credited Back… Once your labs are reviewed and you're approved, $49 is credited… (plan starting at $199)."* Other lines proceed via the online medical intake / quiz; lab requirement and draw model (at-home vs partner-lab) not stated for non-TRT treatments.
- **Modality (note):** front door is **"100% online"** — an online medical intake/quiz, provider review, then *"one of our doctors will contact you to talk about your health goals."* The modality of that provider contact (phone / message / async review) is **not specified**; no scheduled video visit is advertised. Classified `async` (the gate is an online questionnaire); the provider-contact step keeps it from being purely self-serve.
- **Payment & commitment:** **page-stated:** *"Flexible, no-commitment treatment plans"* — à-la-carte individual treatments, mostly monthly (some one-time, e.g. Trimix "per Vial"), no membership gate; checkout via WooCommerce + FunnelKit + Stripe. **Payer rail unstated** — no HSA/FSA/insurance/cash-pay language found sitewide (`pay_model: unclear`). A "$29.99 shipping fee" appears only in a customer review, not official copy.
