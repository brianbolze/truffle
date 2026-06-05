---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: home.medvi.org
captured_at: 2026-06-04           # rides the 2026-06-04 profile.md capture
value_chain_role: DTC brand
pharmacy_model: third-party              # "MEDVi is not acting as a pharmacy"; named partner pharmacies, no ownership claim
audience: all-genders                    # gender-neutral GLP-1 front door (female-skewed proof); QUAD men's line live, women's "Coming Soon" — see note
compounding_posture: both                # compounded GLP-1 (semaglutide) + branded Wegovy®/Zepbound® cards
anchor_category: GLP-1                    # weight loss is the flagship + front door (500k-patient claim, homepage is ~all weight loss)
modality: sync                           # gating "online consultation" — "a clinician will meet with an individual after checkout" (channel unpinned — see note)
access_model: all-in                     # flagship compounded program "No membership or hidden fees! Everything you need is included" (branded path adds $99 membership — see note)
pay_model: HSA/FSA eligible              # "HSA/FSA Approved!" (glp1) — the positive payer-rail signal; also cash-pay / "no insurance required" (see note)
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "MEDVi is **not acting as a pharmacy**… you may be entering into a relationship with a pharmacy, pharmacist, and/or pharmacy group… Partner pharmacies include:" **Triad Rx · RedRock Pharmacy · Beaker Pharmacy & Compounding** (homepage footer, named with addresses/links). No owned-pharmacy claim, no captive facility, no sibling pharmacy domain.
- **Clinical delivery (separate from pharmacy):** outsourced to **OpenLoop Health** (US-licensed provider network) + **CareGLP Affiliated P.C.s** — "OpenLoop Health clinicians retain the decision to prescribe" (homepage disclaimer). MEDVi is the brand/UX layer; both the medical group and the pharmacies are third parties.
- **Lane:** not stated — "dispensed by state-licensed pharmacies," "produced in FDA-regulated facilities"; neither 503A nor 503B is named. Compounded GLP-1s explicitly **not FDA-approved**.

## Categories served

- **Categories (live Rx):** GLP-1 (weight loss, flagship) · sexual-health/ED (QUAD™ — a 4-in-1 apomorphine+vardenafil+sildenafil+tadalafil sublingual). Plus **MEDVi Meals** (non-Rx chef-prepared meal delivery, separate funnel). **Coming Soon (roadmap, not buyable):** women's-HRT · peptides/longevity · supplements · hair · skin.

## Credibility & access

- **Health-merchant credibility:** LegitScript-verified (footer seal → `legitscript.com/websites/?checker_keywords=medvi.org`, y); named clinicians — care provided by the **OpenLoop** network but no public `/physicians` roster page (n); pharmacy accreditation (PCAB/ACHC/NABP) not shown (n).
- **Controlled-substance Rx:** **non-scheduled only** — the page-attested products are compounded GLP-1 (semaglutide) + QUAD's PDE5/dopamine actives. **No testosterone/TRT SKU** despite the "hormones, energy and performance" men's-health framing (QUAD is an ED stack, not TRT — see profile.md / offerings.md).
- **Labs:** **none** as a required step — intake is an online questionnaire; the program includes a "metabolic report" but no at-home kit or blood-draw gate is described on the captured pages.
- **Payment & commitment:** "HSA/FSA Approved!"; "all MEDVi prescriptions are **cash-pay**," "no insurance required" (branded options "your insurance may reimburse you"). Compounded program `$179` first month → `$299` refills, "no contract"; QUAD cancel-anytime. The **branded-GLP-1 path adds a separate `$99 Membership`** (the only membership architecture on the site). Promo-driven, point-in-time — re-check on recapture.

## Notes

- **audience:** read off the pages, not the name. The flagship front door (GLP-1 weight loss) is gender-neutral and its social proof skews **female** (testimonial roster is largely women); the live **men's** line (QUAD) is a distinct, deliberately masculine sub-brand, and a **women's-health** line is announced "Coming Soon." Serving both head-on with no single gendered lead ⇒ `all-genders`, not `men-first`.
- **modality:** the gating consult is a **provider consultation**, recorded `sync` — "Prescriptions are issued only after an **online consultation** with an independent licensed provider"; "an OpenLoop Health clinician **will meet with** an individual after checkout to determine if they qualify"; glp1 offers "unlimited **appointments**, messaging and support"; QUAD "Doctor Consultation Included." The **channel** (video vs phone) is not pinned on the captured pages, and no async-where-allowed fallback is stated (so not `hybrid`); the "meet with / consultation / appointments" language tips it past a pure async quiz-review.
- **access_model:** recorded `all-in` for the flagship's one-bundled-fee architecture — compounded GLP-1 is "**No membership or hidden fees! Everything you need is included**" (`$179`→`$299`), and QUAD is a standalone monthly Rx with no membership. The exception lives in the body: the three **branded** GLP-1 cards show "**$99 Membership + Medication Cost**," a genuine membership sub-path; the dominant/front-door model is still the no-membership all-in program.
- **pay_model:** per the asymmetric-fill rule, the positive payer-rail signal is recorded — `HSA/FSA eligible` ("HSA/FSA Approved!"). The site **also** states direct-pay ("all MEDVi prescriptions are cash-pay," "no insurance required"), so it is not insurance-billing; HSA/FSA is the stronger informative positive of the two attested signals.
