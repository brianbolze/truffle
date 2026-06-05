---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: tryshed.com
captured_at: 2026-06-04
value_chain_role: DTC brand               # DTC telehealth brand; explicitly "not a pharmacy" — routes Rx to a third-party dispensing pharmacy
pharmacy_model: third-party               # "Prescriptions are fulfilled and shipped by a third-party dispensing pharmacy" — /products/foundayo; no named partner, no owned facility
audience: all-genders                     # parallel Women's Hair + Men's Hair hubs; weight-loss/longevity gender-neutral
compounding_posture: both                 # compounded semaglutide/tirzepatide ("not FDA-approved") + FDA-approved Foundayo/orforglipron, Wegovy, Zepbound
anchor_category: GLP-1                     # homepage hero "Sustainable wellness, made simple" + "GLP-1 Weight Loss / Lose up to 15-20%"; "Foundayo® Is Here. The FDA-Approved GLP-1 Pill" banner
modality: async                           # "no appointment required" — 5-minute form → provider review → ship; "100% online visit + checkout"
access_model: à-la-carte/both             # per-product monthly subscriptions, but Foundayo (and the zepbound-shed-membership slug) layer a mandatory $125/mo Shed Membership + provider fee
pay_model: HSA/FSA eligible               # "FSA eligible" homepage badge; Foundayo priced "for new patients using cash pay"; no insurance billing stated
---

## Fulfillment

- **Pharmacy (claim, verbatim):** "**Shed is not a pharmacy and does not dispense medications. Prescriptions are fulfilled and shipped by a third-party dispensing pharmacy.**" — /products/foundayo. Homepage step 3 echoes it: "Your prescription will be discreetly delivered right to your doorstep." No named pharmacy partner, no owned facility, no sibling pharmacy domain surfaced.
- **Lane:** **not stated** — captured pages name no 503A/503B designation. Compounded meds are described only as "made by a licensed pharmacy based on a provider's prescription" / "prepared by licensed pharmacies to meet the specific needs of individual patients" (semaglutide/foundayo disclaimers), language consistent with patient-specific compounding but the 503A/503B lane is not page-attested.
- **Sibling brands (not pharmacies):** Shed Supplements lives off-site on shednutrition.com / shedsupplements.com (OTC protein/greens/GLP-1 companion powders) — a retail catalog, not a fulfillment entity (`owns:` in profile.md).

## Categories served

- **Categories:** GLP-1/weight-loss · longevity/NAD · peptides · hair · skin(coming-soon) · health-coaching

## Credibility & access

- **Health-merchant credibility:** **LegitScript-certified** (footer seal → legitscript.com, "Verify Approval for www.tryshed.com"); **named clinicians** — yes, a photographed care team with credentials on the homepage (Dr. Asad Niazi MD provider, Neely Wood RN, Roseanne Schnell RD, Pardise Mossalman CHC, plus a member-success manager), though no dedicated `/physicians` roster page; pharmacy accreditation (PCAB/ACHC/NABP) — **not shown**.
- **Controlled-substance Rx:** **non-scheduled only** (page-attested by product). No TRT/testosterone SKU appears anywhere in the captured nav or PDPs; the catalog is GLP-1s, longevity peptides (NAD+, sermorelin, glutathione), low-dose naltrexone, and topical/oral hair Rx — none Schedule-III.
- **Labs:** **none** stated. The 4-step flow is "5-minute form → provider reviews answers (no appointment) → medication shipped → ongoing support"; no required or optional lab panel or draw model appears on the captured pages.
- **Payment & commitment:** **HSA/FSA eligible** ("FSA eligible" badges on the homepage GLP-1 and NAD+ heroes; FSA Store badge on the semaglutide PDP); Foundayo "starts at $149/month for new patients **using cash pay**" — no insurance billing claimed. Commitment: per-medication monthly subscriptions sold as **1 / 6 / 12-month prepay plans** (per-month price drops with longer prepay, e.g. Semaglutide $249→$175); **Foundayo and the `zepbound-shed-membership` slug add a separate $125/month Shed Membership + provider fee** on top of the med price (paid directly to Shed; medication paid separately to the dispensing pharmacy). A "Lose 10% of your bodyweight or your money back" guarantee anchors the weight-loss program (terms apply). Explicit cancel/lockup terms not page-stated on the captured pages.

## Notes

- **Access-model nuance:** there is no single sitewide membership gate — most lines read as à-la-carte per-product subscriptions, but Foundayo (and the Zepbound slug) bolt a mandatory $125/mo Shed Membership onto the med price, so the architecture is mixed → tagged `à-la-carte/both`.
- **Anchor stability:** GLP-1 weight loss is a stable, non-rotating hero (member-count proof, money-back guarantee, and the Foundayo "FDA-Approved GLP-1 Pill" banner all front-and-center) — not A/B-volatile this capture; longevity and hair are secondary tiles.
