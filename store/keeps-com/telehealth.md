---
# Query contract for this store: ../../QUERYING.md — parse this frontmatter to filter/group, grep the body to locate; domain is the key.
schema_version: "1.0"          # the telehealth-pack version (independent of profile.md's)
domain: keeps.com
captured_at: 2026-06-04        # derives from the same 2026-06-04 profile.md capture
value_chain_role: DTC brand
pharmacy_model: unclear                  # claims it "built our own supply chain" but names no pharmacy; legal/fulfillment route to parent Thirty Madison — see Fulfillment
audience: men-only                       # "help more men keep more hair," "Men of Action," title "Hair Loss Treatment for Men"
compounding_posture: both                # FDA-approved generics (finasteride, minoxidil, sildenafil, tadalafil, ketoconazole) + compounded multi-ingredient (Minoxidil+ Spray "compounded"; Chew/Drop "X-in-1" combos)
anchor_category: hair                    # hero "Keep your hair. Regrow what you lost."; first nav item Hair Loss
modality: async                          # online consultation reviewed by a provider + "unlimited provider messaging"; no video/synchronous visit named
access_model: à-la-carte/both            # individual products bought separately, no membership wrapper; consult "first visit free, $5 per visit thereafter"
pay_model: unclear                       # DTC framing ("selling directly to you") but no insurance/HSA/FSA/cash-pay statement on captured pages
---

## Fulfillment
- **Pharmacy:** ownership not stated. The about page claims vertical integration — *"By building our own supply chain and selling directly to you, we can provide the highest quality of care while offering treatments that are half the price you would pay at your local pharmacy"* (/about-us) — but names **no pharmacy entity, partner, or accreditation**. Keeps is a **Thirty Madison** brand: all legal pages (Privacy, Terms, Informed Consent) and the patient portal route to **patient.thirtymadison.com**, so fulfillment runs on the parent group's platform rail. 503A/503B lane: not stated. (Claim recorded, not adjudicated.)

## Categories served
- **Categories:** hair-loss/MPB (finasteride · minoxidil · dutasteride compounds · ketoconazole · styling cosmetics · supplement) · sexual-health/ED (sildenafil · tadalafil · compounded "Powerhouse"/"Triple-action")

## Credibility & access
- **Health-merchant credibility:** named clinicians **yes** — Dr. Parth Shah (Sexual Health Clinical Lead) + derm advisors Jerry Shapiro, MD (NYU) and Antonella Tosti, MD (U. Miami); LegitScript seal **not shown** in captured markdown (not confirmed absent); pharmacy accreditation (PCAB/ACHC/NABP) not shown. Press: Fast Company, CNBC, Business Insider, WSJ.
- **Controlled-substance Rx:** non-scheduled only — the catalog is finasteride, minoxidil, dutasteride, ketoconazole (hair) and sildenafil/tadalafil (ED); no testosterone/TRT or other scheduled product appears.
- **Labs:** none — questionnaire/consultation-based prescribing; no lab testing or bloodwork in the captured flow.
- **Payment & commitment:** DTC/direct ("selling directly to you"); **cancel anytime**; medications shipped + billed every **3, 6, or 12 months**; provider consult "first visit free, **$5 per visit** thereafter." Pay rail (cash vs insurance/HSA) not stated on the captured pages.

## Notes
- **pharmacy_model:** kept `unclear` over `integrated` deliberately — the "built our own supply chain" line is a *supply-chain* self-claim, not a pharmacy-ownership claim, and no pharmacy is named on Keeps's own pages. The parent Thirty Madison rail (patient.thirtymadison.com) is the strongest fulfillment signal; resolving actual ownership is a deep-research job, not page-attested state.
- **modality:** `async` read from "your private online consultation is reviewed by a licensed medical provider" + "unlimited provider messaging / regular provider check-ins" — no synchronous video visit is offered or required in the captured journey.
- **anchor_category:** hair is unambiguous and stable here (not A/B-volatile) — the hero, page title, first nav item, and founding mission are all hair-loss; ED is explicitly framed as the newer companion ("New to Keeps").
