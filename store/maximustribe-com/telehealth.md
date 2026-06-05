---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: maximustribe.com
captured_at: 2026-06-04
value_chain_role: DTC brand              # DTC "performance medicine" telehealth brand; tag what they ARE, not the captive-pharmacy bundle
pharmacy_model: third-party              # "we strictly partner with US-based, fully licensed compounding pharmacies" — no owned facility, no named partner
audience: men-first                      # "started by treating declining testosterone… in men… Now… both men and women"; every TRT card "Best for: Men"
compounding_posture: compounded-only     # every Rx explicitly compounded ("Compounded semaglutide… not FDA-approved," "Compounded in US-based pharmacies"); no FDA-brand finished drug surfaced
anchor_category: TRT                      # testosterone is flagship/origin line; "Next-generation testosterone optimization"; H1 rotates (see Notes)
modality: hybrid                         # questionnaire-first intake + "Meet with a Maximus physician 100% online" — captured pages don't pin a sync video call
access_model: membership-required        # recurring monthly membership per protocol; consults/monitoring/messaging bundled in
pay_model: HSA/FSA eligible              # "FSA & HSA eligible" (homepage) + direct-pay, "No insurance required" — positive payer signal page-stated
---

## Fulfillment
- **Pharmacy (claim, verbatim):** "We strictly partner with US-based, fully licensed compounding pharmacies that operate in compliance with rigorous USP standards for sterility and quality assurance… source Active Pharmaceutical Ingredients exclusively from FDA-registered manufacturers" — /about-us + homepage FAQ ("How do we select our pharmacy partners?"). Claim of partnering with (not owning) compounding pharmacies; **no named partner, no owned facility, no sibling pharmacy domain** surfaced. Lane: **not stated** (says "compounding pharmacies" generically — no 503A/503B label on captured pages; PDP trust icon reads "FDA approved pharmacies," not a compounding-tier seal).

## Categories served
- **Categories:** TRT · GLP-1/weight-loss · growth-hormone-peptides · mood/stress (oxytocin) · labs · hair · sexual-health/blood-flow · prescription-multivitamin

## Credibility & access
- **Health-merchant credibility:** **LegitScript-approved** (footer seal → legitscript.com verification, every captured page); **named clinicians** — yes, a medical advisory board on the homepage (Dr. Cameron Sepah CEO, Dr. Matt Coward UNC Urology, Dr. Wayne Hellstrom Tulane, Dr. Justin Houman Cedars-Sinai, Dr. Eugene Shippen); "US-based, fully licensed, board-certified physicians"; pharmacy accreditation (PCAB/NABP/ACHC) **not shown** (no seal — partners described generically).
- **Controlled-substance Rx:** **offers Schedule-III (injectable testosterone)** — page-attested by product: `/testosterone/Injectable-TRT` "Injectable Testosterone starting at $99.99/mo," "weekly at-home injections" (plus cream/oral TRT and an Injectable-TRT + hCG combo).
- **Labs:** **both** — a standalone optional panel line (Comprehensive Lab Testing, Optimal $199.99/yr · Maximal $349.99/yr, up to 146 markers; At-Home Testosterone Test $99.99, 10 markers, "No commitment to buy treatment") *and* a recommended intake step for protocols ("fill out the intake form. Order an at-home lab test to measure key biomarkers" — /testosterone funnel). Draw model: **at-home kit** for the testosterone test; **in-person blood draw at "2,000+ partner lab locations nationwide"** (fasting required, certified labs) for the comprehensive panels.
- **Payment & commitment:** **HSA/FSA eligible** ("FSA & HSA eligible," homepage) + **direct-pay** ("Our services are direct-pay… covers your doctor visits, medications, and ongoing support"; "No insurance required") — does not bill insurance. Commitment: monthly membership per protocol (labs annual); new 12-month-plan customers get **50% off first month**; published TRT ladders run 1-month / 3-month / 12-month (price drops as the plan lengthens). No cancellation terms stated on captured pages.

## Notes
- **Anchor rotation:** the homepage H1 was captured as "Maximum growth hormones" (rotating creative, point-in-time, not fixed), but testosterone is the flagship/origin line — its own hero section ("Next-generation testosterone optimization"), the deepest lineup, and origin framing ("We started by treating declining testosterone levels in men") — so `anchor_category: TRT`. Hero is A/B-volatile; treat as a snapshot.
- **Compounding posture:** recorded `compounded-only` because every captured Rx PDP carries the compounded disclaimer ("Compounded medications are not FDA-approved…"); the "FDA approved" strings on PDPs refer to FDA-**registered** API manufacturers / the GLP-1 mechanism, not an FDA-brand finished drug. No commercial/brand-name SKU surfaced in these captures.
- **Modality:** the flow is questionnaire (async intake) → "Meet with a Maximus physician 100% online" → optional at-home labs → shipped protocol. "100% online" doesn't pin whether the physician step is a live video visit or async review on the captured marketing pages, so `hybrid` over `sync`.
