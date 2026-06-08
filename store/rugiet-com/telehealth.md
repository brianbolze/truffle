---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: rugiet.com
captured_at: 2026-06-07
value_chain_role: DTC brand
pharmacy_model: third-party              # "partner pharmacies… FDA-regulated U.S. pharmacies" — no owned facility named (body verbatim)
audience: men-only                       # "Performance Medicine For Men"; all-male copy/imagery, no women's line
compounding_posture: both                # almost all SKUs compounded (ED combos, enclomiphene, topical/oral T, sleep, weight) + FDA-approved injectable testosterone cypionate
anchor_category: sexual-health           # hero + best-seller is the 3-in-1 ED troche "Ready"; "RUGIET FOR SEX"
modality: hybrid                         # async questionnaire for ED/sexual/sleep/weight; live audio-video consult required for TRT (controlled substances)
access_model: all-in                     # "consultation, prescription, and unlimited follow-ups included; no hidden fees"; TRT is one flat all-inclusive price
pay_model: HSA/FSA eligible              # "HSA/FSA eligible" stated across lines; insurance not billed
---

## Fulfillment
- **Pharmacy:** **third-party partner pharmacies, no owned facility claimed.** Homepage: *"All prescriptions filled by FDA-regulated U.S. pharmacies."* The /sex FAQ, asked whether partner pharmacies are FDA-regulated, answers: *"Pharmacies are licensed and regulated at the state level by Boards of Pharmacy and are also subject to applicable federal laws, rules, and regulation."* Other pages: *"made in FDA-regulated U.S. pharmacies"* and *"administered by physicians and pharmacists licensed in the United States."* No named pharmacy entity and **no 503A/503B lane stated** — though the catalog is overwhelmingly compounded (each SKU disclaims *"compounded drug product… not approved by FDA"*), which implies a 503A compounding relationship the site doesn't spell out. Claim recorded, not adjudicated.

## Categories served
- **Categories:** sexual-health/ED · premature-ejaculation · TRT/testosterone · sleep · weight-loss · hair

## Credibility & access
- **Health-merchant credibility:** **LegitScript-certified** (footer seal links to legitscript.com verification for rugiet.com) + a **HIPAA Compliant** footer badge; **named board-certified advisory board** (urology-led: Justin Houman MD, Nicholas Farber MD, Andrew Y. Sun MD — urologists; Vipul Khanpara MD — CMO, emergency medicine; Asim Roy MD — neurology/sleep). No PCAB/ACHC/NABP pharmacy accreditation shown.
- **Controlled-substance Rx:** **offers Schedule-III (testosterone)** — Injectable, Topical, and Oral TRT are each labeled *"a controlled substance"* requiring *"a live audio-video online consultation,"* with Injectable TRT page-attested as **testosterone cypionate**. Enclomiphene (the needle-free, fertility-preserving TRT alternative) is **not** scheduled. ED/PE/sleep/weight lines are non-scheduled compounded Rx.
- **Labs:** **required-step for TRT** — a **$69** blood test (12 biomarkers, at-home/lab draw) that *includes a video call with a licensed clinician*; *"we don't accept outside bloodwork… all baseline and follow-up labs must be completed through our approved testing process."* **None** for the ED/sexual, sleep, or weight lines.
- **Payment & commitment:** **HSA/FSA eligible** across lines (*"Does this qualify for HSA/FSA? Yes"* — contact your plan for reimbursement); **insurance not billed** (cash-pay rail). *"You're only charged if prescribed."* TRT plans run **3, 6, or 12 months** at a flat all-inclusive **from $139/month** (labs + unlimited follow-ups + dose switches included); Ready offers an optional membership, **cancel anytime**.

## Notes
- **anchor_category:** point-in-time front-door read. Both the homepage and /all-treatments lead with **Ready (3-in-1 ED)** — "Best Seller" badge, the "RUGIET FOR SEX" hub, and the only product with a public price — so the front door is **sexual-health**, even as TRT, sleep, and weight fill out the body. Hero copy rotates promos ("Try 2 months of Ready, get 1 free"; "Claim 15% off Ready"); treat the anchor as a snapshot.
- **modality:** genuinely split. The flagship ED/sexual, sleep, and weight lines gate on an **asynchronous** questionnaire (*"complete a health assessment → a doctor reviews your info → medication ships"*). TRT is **synchronous** — controlled-substance rules force *"a live audio-video online consultation."* Recorded `hybrid` for the mixed front door.
- **access_model:** `all-in`, not membership-gated. Across lines the price is stated to **include the consult, prescription, and unlimited follow-ups** with *"no hidden fees"* (*"Your prescription is included at no additional cost"*); TRT is explicitly *"one flat price, every medication."* A Ready membership exists as an **optional** savings/auto-ship plan (cancel anytime), not a mandatory gate — so this is `all-in`, distinct from a membership-required model.
- **compounding_posture:** `both`, but lopsided. Nearly the entire catalog is **compounded** (Ready, Go Long, Daily Boost, Grower, Enclomiphene, Topical TRT, Oral TRT, Recharge, Weigh In — each carries the FDA compounded-drug disclaimer). The **only FDA-approved** product is **injectable testosterone cypionate** (carries the controlled-substance disclaimer, not the compounded one). Per-SKU lane detail lives in `offerings.md`.
