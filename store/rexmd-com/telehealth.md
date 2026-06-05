---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: rexmd.com
captured_at: 2026-06-04
value_chain_role: DTC brand
pharmacy_model: third-party              # "one of our partnering pharmacies will deliver it" (/how); "our partnered pharmacy's compounded medications" — no owned facility, no named entity
audience: men-only                       # "Telemedicine for Men"; "Healthcare Services for Men"; finasteride "for use by MEN ONLY" — no women's line
compounding_posture: both                # compounded sermorelin (peptide) + compounded GLP-1 "if appropriate" alongside FDA-brand (Viagra/Cialis/Wegovy/Zepbound/Clomid) + FDA-generic (sildenafil/tadalafil/finasteride/sertraline/valacyclovir/doxepin/ramelteon)
anchor_category: sexual-health           # ED/sexual-health is origin + front door (nav leads "Sexual Health"; persistent ED sale banner; "475,000 men… take charge of their sexual health") — point-in-time, see note
modality: hybrid                         # both async ("store-and-forward" intake) + sync (video consult required for testosterone / where states mandate)
access_model: all-in                     # each line bundles consult + ongoing care + free follow-ups into the program/med price; no separate flat membership fee gating access
pay_model: cash-pay only                 # "Rex MD does not accept insurance"; WM program "does not accept insurance"; meds route to manufacturer cash-pay (NovoCare/Lilly); no HSA/FSA stated
---

## Fulfillment
- **Pharmacy:** third-party partner pharmacies, claim verbatim — *"one of our partnering pharmacies will deliver it in discreet packaging with fast, free shipping"* (/how). Compounded meds route through *"our partnered pharmacy"* with the safety claim *"All ingredients in our partnered pharmacy's compounded medications are sourced from FDA registered manufacturers and are tested for impurities… To date, no third-party testing failures have been noted"* (/our-medications/weight-management). **No owned facility, no named pharmacy entity, no 503A/503B lane stated.** Parent **LifeMD** (lifemd.com) sits above for insurance-billed / branded-GLP-1 patients, but Rex itself names no captive pharmacy.

## Categories served
- **Categories:** sexual-health/ED · premature-ejaculation · GLP-1/weight-loss · TRT/testosterone · hair · sleep/insomnia · herpes · anxiety (beta-blocker/propranolol)

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer seal → legitscript.com verification, seal #4418850); named clinician Dr. Anthony Puopolo (the telehealth-visit face across homepage/PDPs); providers "board-certified," "U.S. state-licensed and U.S.-based" — no standalone /physicians roster captured; **no PCAB/ACHC/NABP pharmacy accreditation shown.**
- **Controlled-substance Rx:** offers Schedule-III (testosterone) — the Testosterone Program sells **Testosterone Cypionate Injection** and **Testosterone Gel 1.62% CIII**, both page-attested as Schedule III ("a Schedule III controlled substance in the Controlled Substances Act"); a synchronous video call is required for these.
- **Labs:** required-step for the Testosterone Program (the $99 one-time fee "includes a lab panel and a video consultation"; results gate the video call); optional/conditional elsewhere ("Some patients will need to get lab work done before they can be considered for medication"). Draw model not stated.
- **Payment & commitment:** **cash-pay only** — *"While Rex MD does not accept insurance, our telehealth services often cost less than what you would pay using your insurance."* Cancel anytime; once treatment is received, follow-ups are free. Weight management routes branded GLP-1 to manufacturer cash-pay (Wegovy via NovoCare® $499/mo flat; Zepbound vial via Eli Lilly $349/mo); the GLP-1 program "does not accept insurance at this time" and deflects insured patients to parent LifeMD. Testosterone is sold as $99 one-time + from $250/mo (quarterly shipments + ongoing labs + ≥1 video consult/yr).

## Notes
- **anchor_category:** `sexual-health` is the durable front door, but read it as a point-in-time snapshot — the homepage hero and a **sitewide promo banner are ED-pinned** ("Memorial Day Sale — Save Up To 95% Off ED Meds & Pay $2 Per Tablet"). Testosterone and GLP-1 weight loss are the visible growth lines; if the hero rotates to weight loss next capture the anchor could read GLP-1.
- **compounding_posture:** `both`, with a notable shift — compounded **sermorelin** (a peptide GH therapy) is current, and Rex states it "can prescribe compounded versions of GLP-1 medications, if appropriate," **but** also that the compounded-**semaglutide** exemption has ended ("the FDA has since declared that the shortage is over… pharmacies can no longer compound semaglutide"), so today's GLP-1 is FDA-brand-routed (Wegovy/Zepbound/Saxenda). FDA-approved generics dominate the rest of the formulary.
- **access_model:** `all-in` rather than `membership-required` — there is no separate flat membership fee; each condition is a self-contained subscription whose price bundles the consult, shipping, messaging, and free follow-ups (TRT/WM are bundled *programs*, ED/hair/sleep/PE/herpes are per-med subscriptions). The universal `business_model: Subscription` flattens this; the absence of a membership wedge (unlike Hims weight loss) is the finer cut.
