---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: hims.com
captured_at: 2026-05-30           # rides the same 2026-05-30 profile.md capture (Rx PDPs from the 2026-06-03 offerings run)
value_chain_role: DTC brand
pharmacy_model: integrated        # "partner pharmacies" + a company-opened "Ohio-affiliated pharmacy facility" — captive-affiliate; both claims verbatim below
audience: men-only                # hims.com is the men's brand by construction (forhers.com is the separate sibling); no women's line on-site
compounding_posture: both         # FDA-brand GLP-1s (Wegovy/Zepbound/Ozempic) + compounded options coexist; enclomiphene via compounding pharmacies
anchor_category: GLP-1            # hero is weight-loss/GLP-1 ("The GLP-1 pill is here"; "Access our wide GLP-1 lineup") — front-door, point-in-time (see note)
modality: hybrid                  # "Care is delivered asynchronously… In some states, visits happen via live audio or video" (/about/the-company)
access_model: à-la-carte/both     # weight-loss gates a separate membership; every other Rx line is a self-contained subscription (no membership)
pay_model: HSA/FSA eligible       # "FSA & HSA eligible" badges on WL PDPs; "Insurance isn't required" (cash-pay rail, not insurance-billed) — see note
---

## Fulfillment
- **Pharmacy:** ownership posture is **mixed and stated in two places**. The how-it-works copy routes to third parties — *"The provider issues a prescription, which can then be fulfilled by one of **Hims & Hers' partner pharmacies** and discreetly shipped to the customer's front door"* (/about/the-company). But the company milestones claim a captive facility — *"Hims expanded its services to all 50 states, and **the Ohio-affiliated pharmacy facility opened**"* (2020, /about/the-company). A company-opened affiliated pharmacy alongside partner pharmacies reads as **captive-affiliate** (recorded `integrated`), not a pure third-party router — but neither claim is resolved to truth here, and no named pharmacy entity or 503A/503B lane appears on the captured pages. Lane: not stated.

## Categories served
- **Categories:** GLP-1/weight-loss · sexual-health/ED · premature-ejaculation · hair-loss · testosterone · mental-health/psychiatry · labs · skin-care (+ an OTC sexual-wellness shelf: rings, vibrators, condoms, lube)

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer seal links to legitscript.com verification, sitewide); named clinical bench on the homepage (Dr. Craig Primack, obesity medicine; Dr. Peter Stahl, urology; Dr. Brian Williams, Medical Affairs; Dr. Alicia Warnock, endocrinology; Dr. Deepak L. Bhatt, cardiology) + a "400+ U.S.-licensed providers in all 50 states" claim (/about/the-company); no PCAB/ACHC/NABP pharmacy accreditation shown.
- **Controlled-substance Rx:** offers Schedule-III only as enclomiphene-based "Testosterone by Hims" (`/testosterone`), which is **not synthetic TRT** — injectable/oral testosterone is marked "Coming in 2026," not buyable today. Psychiatry is explicitly non-scheduled: *"Controlled substances such as Xanax and Adderall are not available."* So: a TRT *brand* fronts the testosterone line, but no scheduled testosterone SKU is purchasable in this capture.
- **Labs:** required-step for testosterone (an at-home kit gates eligibility — *"a healthcare provider will order labs processed in a CLIA-certified lab, which is required to determine your eligibility"*); also sold as a **standalone product line** — a Quest Diagnostics in-person blood draw (75+ biomarkers baseline, 130+ available, twice-yearly) + the Galleri multi-cancer add-on, no video visit required for Labs.
- **Payment & commitment:** **HSA/FSA eligible** on the weight-loss line (*"FSA & HSA eligible"* badge on the Wegovy Pen / Foundayo PDPs; reimbursement-by-receipt mechanic in the WL FAQ); **insurance not billed** (*"Insurance isn't required"* across lines). Commitment differs by line: weight-loss needs an active **Hims Weight Loss Membership** ($39 first month → $149/mo, billed separately from medication); enclomiphene's only price (FAQ-only $99/mo) is a **10-month plan paid upfront**; other Rx lines are month-to-month self-contained subscriptions.

## Notes
- **anchor_category:** point-in-time front-door read. The capture catches Hims mid-pivot to a **weight-loss-led, GLP-1-centric** front door — the hero image (injection pen + pill), the "The GLP-1 pill is here" banner, the first/dominant homepage module ("Your weight loss breakthrough is here / Access our wide GLP-1 lineup"), and every GLP-1 card badged `RxNew`. The homepage hero carries a rotating carousel and offerings.md flags promo/A-B pricing + rotating ATF heroes (though no formal A/B framework like Optimizely is named in profile `site_notes`) — treat the anchor as a **point-in-time snapshot, not fixed**. Sexual health is the origin franchise; the front door today is GLP-1.
- **audience:** `men-only` is read from site **construction**, not the brand name — hims.com leads with male-only photography and copy ("Get your edge back," "Boost testosterone") and carries **no women's line**; the sibling women's brand lives on a separate domain (forhers.com). (Hims & Hers Health, Inc. as a parent serves all genders; this pack profiles hims.com.)
- **access_model:** genuinely split, hence `à-la-carte/both`. Weight-loss is **membership-required** (*"Medication is not available without a membership"*); every other Rx line bundles the consult/shipping/check-ins/messaging into a **self-contained per-SKU subscription** with no separate fee. The universal `business_model: Subscription` flattens this; the split is the finer cut.
- **pay_model:** asymmetric. The positive signal wins the single-select — the hero weight-loss line is page-stated **"FSA & HSA eligible."** But the **testosterone** line contradicts it: *"Hims & Hers doesn't take FSA or HSA plans as payment at this time"* (`/testosterone`). So HSA/FSA eligibility is **line-dependent**, not universal. Insurance is uniformly **not** billed.
