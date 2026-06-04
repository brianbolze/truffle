---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"
domain: noom.com
captured_at: 2026-06-04
value_chain_role: DTC brand            # consumer telehealth/wellness brand (+ a B2B distribution arm, Noom Health); tag what they ARE
pharmacy_model: third-party            # "we partner with USP-compliant, state-regulated pharmacies" — not owned; see Fulfillment
audience: all-genders                  # weight-loss leads gender-neutral; a dedicated women-only Menopause/HRT line — see note
compounding_posture: both              # "We prescribe generic, compounded, and brand name medications"
anchor_category: GLP-1                 # homepage front door: "Meds to lose the weight" / Noom Med
modality: async                        # front-door gating consult is async chat ("evaluate your results… all online"); sync video in some programs — see note
access_model: membership-required      # a recurring Noom program subscription gates access; med bundling varies by path — see note
pay_model: HSA/FSA eligible            # "FSA & HSA eligible" badged; also coordinates insurance + offers cash-pay — see note
---

## Fulfillment
- **Pharmacy:** "We partner with U.S. Pharmacopeia (USP)-compliant, state-regulated pharmacies for plans that include medication, and only source active pharmaceutical ingredients from suppliers on the FDA green list." — /glp-1-access-and-transparency. Claim only; **no owned pharmacy, no named partner pharmacy.** Lane (503A/503B) **not stated** by Noom — a Science Advisory Board pharmacist's bio references "503a compounding pharmacies," but that's her background, not Noom's stated lane. Quality framing: pharmacy partners "regulated by State Boards of Pharmacy," third-party batch testing, and a member-requestable Certificate of Analysis (COA).
- **Compounded vs. brand:** offers both — brand-name GLP-1s (Ozempic®, Wegovy®, Zepbound®, Mounjaro®) routed through pharmacies, plus compounded and generic GLP-1s; "any compounded medications are not approved by the FDA or reviewed for quality, safety or efficacy" (homepage/PDP disclaimer).

## Categories served
- **Categories:** GLP-1 / weight-loss meds · behavior-change weight loss (Noom Weight) · menopause / womens-HRT · diabetes prevention (CDC-recognized) & management · obesity care · metabolic / longevity. (`anchor_category: GLP-1` is the front-door slice.)
- **Audience note:** the weight-loss front door is gender-neutral; **Menopause & HRT (`/menopause/`, route=hrt) is a women-only line** with its own Women's Health clinical lead (Dr. Julia Edelman).

## Credibility & access
- **Health-merchant credibility:** LegitScript-certified (footer seal → legitscript.com, y); named clinicians — **y** (CMO Dr. Jeffrey Egler + clinical leadership + Science Advisory Board on /glp-1-access-and-transparency and /about-us); pharmacy accreditation (PCAB/ACHC/NABP) **not named** (an unlabeled "Noom Partners in Safety" badge row appears, but no specific accreditation is stated).
- **Controlled-substance Rx:** non-scheduled only — GLP-1s (semaglutide, tirzepatide, generic liraglutide), oral metformin, Wegovy® pill, and menopause HRT; **no testosterone/TRT or other scheduled substances** appear in the roster.
- **Labs:** optional / program-dependent — "evidence-based lab flows" and "integrated lab testing to assess metabolic health" are referenced, but labs are **not stated as a required gating step**; intake gating is an online survey + a required full-body photo + comprehensive medical history.
- **Payment & commitment:** "FSA & HSA eligible" (badged on Med pages); "you do not need insurance" — for the insured, Noom "work[s] to help maximize your coverage for medication and clinician services"; for the uninsured, "affordable cash-pay options." Commitment is a subscription: e.g. GLP-1Rx "Initial 3 week subscription and 4 weeks of medication from $149… and $349 per month… for 12 week subscription thereafter"; Noom Weight offers a free trial → subscription. Page-stated terms only.

## Notes
- **Access architecture:** `membership-required` is the roll-up — a Noom program subscription always gates clinical care + meds. The bundling differs by path: the **compounded GLP-1 / Microdose** cash-pay path folds medication into the subscription price (reads all-in), while **brand-name** is a lower membership fee ("starting at $69") **plus** the medication's separate out-of-pocket cost through insurance.
- **Modality:** classified `async` on the front-door gating consult ("Connect with an expert clinician… evaluate your results and provide a prescription all online"); Noom explicitly leverages "multiple modalities" and offers "synchronous video visits… in some programs," so a sync option exists downstream.
