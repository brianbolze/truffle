---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: agelessrx.com
captured_at: 2026-05-31           # rides the 2026-05-31 profile.md capture (homepage, how-we-work, about); Rx-page cuts corroborated by the 2026-06-03 offerings captures
value_chain_role: DTC brand       # 100%-online longevity platform selling its own catalog; the partner-pharmacy bundle doesn't change what it is
pharmacy_model: third-party       # "503A certified pharmacy partners" / "partnering pharmacy" — no ownership claim, no sibling pharmacy domain
audience: all-genders             # mixed-gender hero, "whether you're 25 or 70," co-equal Men's-Aging + Women's-Aging need-cats + a Women's Hormone Care line — no gendered front door
compounding_posture: both         # compounded (NAD+/GSH/peptides/tretinoin/women's-HRT, compounded-rapamycin) alongside FDA-brand/generic (metformin, generic rapamycin, Brenzavvy®/Invokana®/Wegovy®/Zepbound®)
anchor_category: longevity/NAD    # hero "Harness the power of longevity science"; first nav family = Longevity; NAD+ is the flagship line (see Note)
modality: hybrid                  # async intake-review by default ("review your intake form(s) within up to 5 business days"); sync video "depending on your state"
access_model: à-la-carte/both     # no membership wrapper — each treatment is its own subscription priced independently (visit bundled in), + one-time tests + an optional paid consult
pay_model: HSA/FSA eligible       # sitewide "Using HSA/FSA" footer link + inline "HSA / FSA eligible" (NAD+ PDP); insurance explicitly not billed ("does not work with insurance," "out-of-pocket")
---

## Fulfillment
- **Pharmacy (claim, verbatim):** "If approved, we'll get your order started with one of our certified pharmacy partners with your prescription being overseen by licensed pharmacists with strict quality control measures at an **FDA-registered facility**." — /how-we-work/. Footer disclaimer: "fulfilled at a **partnering pharmacy**, unless requested otherwise." No owned-pharmacy claim, no named partner, no sibling pharmacy domain.
- **Lane:** 503A stated — "fulfilled by one of our US-licensed, **503A certified** pharmacy partners" (/metformin/); NAD+ "compounded by **LegitScript-certified** pharmacies" (/nad-injection/). No 503B outsourcing facility mentioned.

## Categories served
- **Categories:** longevity/NAD · GLP-1/weight · peptides · sexual-health/ED · womens-HRT · skin · hair · labs · supplements · GSH/glutathione

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (sitewide footer seal — `legitscript.com/seals/5907663.js`; "compounded by LegitScript-certified pharmacies," /nad-injection/, y); named clinicians (six-person medical team with bios on /about/#med-team, y); pharmacy accreditation (PCAB/ACHC/NABP) not shown (n).
- **Controlled-substance Rx:** non-scheduled only — no testosterone/TRT SKU appears in the catalog; the controlled molecule present is Schedule-IV **trazodone** (/trazodone/, sleep). (The three incidental "testosterone" page hits are a hair-loss ingredient, an ED citation, and a DHEA study — not products.)
- **Labs:** optional overall — the front-door journey (how-we-work) makes no lab a required first step; lab gating is **per-Rx**: Rapamycin states "**Blood work is required as part of your prescription**… You must adhere to the required lab schedule to receive refills" (initial + ongoing bloodwork included), while Metformin/NAD+/most lines do not gate on labs. Biological-age testing (methylation/phenotypic/metabolomic) is sold as a separate one-time measurement layer, not a required intake step. Draw model: at-home kit or partner lab (Quest) depending on test.
- **Payment & commitment:** HSA/FSA eligible (sitewide footer link to /using-insurance-hsa-fsa/; inline "HSA / FSA eligible" badge on the NAD+ PDP); insurance explicitly not billed ("AgelessRx does not work with insurance providers" /wegovy-pill-access-monitoring/; "out-of-pocket costs… not affected by insurance" /brenzavvy/, /invokana/). Subscriptions often billed quarterly; "pause or cancel at any time–no strings attached" (/how-we-work/). Charged only on approval: "You'll only be charged if your prescription is approved."

## Notes
- **anchor_category — point-in-time positioning read.** The H1 hero leads with longevity ("What would you do with *more* healthy years? Harness the power of longevity science"); the first Treatments nav family is **Longevity**, and **NAD+ is the flagship line** (offerings.md: newest PDP template, "70,000+ NAD+ users supported," XPRIZE entry "studying NAD+," leads the /treatments/ Featured sort). Credibility-anchor molecules are Rapamycin + Metformin. Recorded as `longevity/NAD` for the front-door positioning. Below the H1 the hero offers four co-equal entry tiles (longevity · weight · heart · energy) — i.e. a generalist catalog under a longevity banner; profile `site_notes` flags rotating coupon-code instrumentation (point-in-time prices), but the captured hero copy itself is not shown A/B-rotating.
- **access_model — no membership.** Unlike a membership-wrapped peer, AgelessRx charges no platform/enrollment fee; each treatment is bought à-la-carte as its own subscription with the medical visit bundled into the price (e.g. Rapamycin "$65/month… free medical visit"; Metformin code MET20 "FREE medical evaluation"). It also sells one-time diagnostics and an optional paid Longevity Consultation ("$50") — hence `à-la-carte/both` rather than a single all-in fee.
- **audience — generalist, lifespan-wide.** Recorded `all-genders` from the page-attested front door (mixed-gender hero imagery, "whether you're 25 or 70," parallel Men's-Aging / Women's-Aging need-categories, and a dedicated Women's Hormone Care line). Not read from the brand name.
