---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.1"
domain: nurx.com
captured_at: 2026-06-04
site_notes: "Prices are per-category — each condition page shows a consult fee + either a per-med out-of-pocket table (acne, mental health) or per-brand 'Starts at $X/mo' cards (GLP-1); no central /pricing. GLP-1 brand pens have NO individual PDP (cards on /weight-management/glp1-injections/) and are filled/paid at a 3rd-party local pharmacy — not shipped by Nurx. 50+ birth-control SKUs sit behind the quiz at with.nurx.com; only method-level without-insurance floors are public. OTC items (Nurx EC) at shop.nurx.com. All prices 'not guaranteed', vary by insurance; promo bar ($0 weight mgmt) implies promo/A-B rotation — re-check next run."
---

## Portfolio overview

Nurx is a **`Multi-product`** women's-health telehealth catalog — 7 condition lines, ~30 conditions, "150+ prescription treatment options." Indexed at the **condition level**: each condition is a service line with its own consult fee + (for some) a recurring care fee; specific medications are enumerated with prices only on the deeper lines (acne, mental health, GLP-1). The roster below is complete at that indexed level — every condition line, plus the priced SKUs/methods each page actually lists. The 50+ individual birth-control products live behind the intake quiz and are not publicly priced (method-level floors only).

**Shape findings worth flagging:**
- **The "$650/month" GLP-1 anchor is the *cheapest brand pen's floor at a third-party pharmacy*, not an all-in.** Branded GLP-1 is **not dispensed by Nurx** — you pay the drug at your local pharmacy *plus* Nurx's **$79 consult + $79/mo support fee**. Real all-in ≫ the headline. (See deep block.)
- **Two pricing worlds.** Insurance-billable clinical lines (birth control, mental health, general health) show "$0 with insurance" floors; cosmetic/cash-pay lines (anti-aging, melasma, eyelash, women's hair loss) carry no insurance and quote flat cash prices or hide them behind the consult.
- **No compounded lane.** Every priced molecule is FDA-brand or generic; GLP-1s are all branded pens.

**Prominence read:** weight management (GLP-1) is foregrounded `[MED]` — a persistent promo bar ("$0 with insurance") and the only line with real branded product renders — but the mega-nav and hero carousel still lead with **birth control** `[MED]` (heritage anchor). Acne is nav item #3 `[LOW]`. Treat the lead as rotating (no A/B tool fingerprinted).

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| Birth control | family | — | /birthcontrol/ | — | — | contraception · pill/patch/ring/shot · "Over 50+ types"; consult → Rx → mail (3-mo supply) |
| The pill | buyable | /birthcontrol/ | /birthcontrol/ (50+ SKUs behind quiz; e.g. /combination-pill/feirza-1-20/) | "as little as $15 per pill pack without" ("As low as $0 with insurance") | published | combination & progestin-only pills · oral daily · 50+ brands/generics |
| The ring | buyable | /birthcontrol/ | (no PDP — section on /birthcontrol/) | "as little as $150 per ring without" ("$0 with insurance") | published | vaginal ring · replace monthly · not stated (brand) |
| The patch | buyable | /birthcontrol/ | (no PDP — section on /birthcontrol/) | "as little as $50 per month without" ("$0 with insurance") | published | transdermal patch · replace weekly · not stated (brand) |
| Estrogen-free / hormone-free | buyable | /birthcontrol/ | /birth-control/progestin-only-pill-mini-pill/norethindrone/ ; /birthcontrol-estrogen-free | — (priced as pill, above) | on-request | norethindrone (mini-pill) + hormone-free options · oral · per /our-services |
| Emergency contraception | family | — | /emergencycontraception/ | — | — | morning-after · OTC pill + Rx · ship or local-pharmacy pickup |
| Nurx Emergency Contraceptive (OTC) | buyable | /emergencycontraception/ | shop.nurx.com/products/nurx-emergency-contraception | "$19.50 per pill with $0 shipping" | published | levonorgestrel (generic Plan B One-Step®) · oral · OTC, no Rx |
| Ella® (Rx) | buyable | /emergencycontraception/ | /emergencycontraception/ | "As low as $0 with insurance or $45 without (+ $15 medical consultation fee)" | published | molecule not stated (ulipristal not named on page) · oral · Rx, within 5 days; +$15 expedited overnight |
| Weight management | family | — | /weight-management-treatment/ | "Starts at $650/month" | partial | GLP-1 + orals; $79 consult + $79/mo provider support fee (cash-pay) |
| GLP-1 injections | family | /weight-management-treatment/ | /weight-management/glp1-injections/ | "Starts at $650/month" | partial | branded GLP-1 pens · subcutaneous injection · **not shipped — local-pharmacy pickup**; *(exemplar)* |
| Zepbound® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $1000 / month on average" | partial | tirzepatide · auto-injector pen · in-person pharmacy pickup only |
| Wegovy® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $1300 / month on average" | partial | semaglutide · injection pen · pickup, not shipped |
| Saxenda® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $1300 / month on average" | partial | liraglutide · injection pen · pickup, not shipped |
| Ozempic® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $1000 / month on average" | partial | semaglutide · injection pen · pickup, not shipped |
| Mounjaro® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $1000 / month on average" | partial | tirzepatide · injection pen · pickup, not shipped |
| Victoza® | buyable | /weight-management/glp1-injections/ | (no PDP — card on /weight-management/glp1-injections/) | "Starts at $650 / month on average" | partial | liraglutide · injection pen · pickup, not shipped (the $650 line floor) |
| Weight-loss orals | buyable | /weight-management-treatment/ | /weight-management/orals/ | "$60-329/month" (cash; may use insurance) | partial | naltrexone · bupropion · topiramate · metformin · oral · shipped; + $79/mo fee |
| Mental health | family | — | /mental-health/ | "$59 for the initial consultation and $69 per month for ongoing medication management" | partial | SSRIs/SNRIs/others · oral · meds shipped; no controlled substances |
| Escitalopram (Lexapro®) | buyable | /mental-health/ | /antidepressant/escitalopram-lexapro/ | "$0/month copay" (insurance) / "$25" without | partial | escitalopram oxalate · oral 5/10/20 MG · + $69/mo mgmt fee |
| Sertraline (Zoloft®) | buyable | /mental-health/ | /antidepressant/sertraline/ | "$0/month copay" / "$25" | partial | sertraline HCl · oral 25/50/100 MG · + $69/mo mgmt fee |
| Fluoxetine (Prozac®) | buyable | /mental-health/ | /antidepressant/fluoxetine/ | "$0/month copay" / "$25" | partial | fluoxetine HCl · oral 10/20/40/60 MG · + $69/mo mgmt fee |
| Buspirone (Buspar®) | buyable | /mental-health/ | /antidepressant/buspirone/ | "$0/month copay" / "$25" | partial | buspirone HCl · oral 10 MG · + $69/mo mgmt fee |
| Bupropion (Wellbutrin®) | buyable | /mental-health/ | /antidepressant/bupropion-wellbutrin/ | "$0/month copay" / "$25" | partial | bupropion HCl · oral 150/300 MG · + $69/mo mgmt fee |
| Skincare / dermatology | family | — | /skincare-treatments/ | — | — | acne · anti-aging · eyelash · melasma · rosacea · topical/oral |
| Acne | family | /skincare-treatments/ | /acne-treatment/ | "$40 for your medical consultation" (meds "as little as $0" w/ insurance) | published | topical + oral acne Rx; *(exemplar — only fully-priced skincare line)* |
| Spironolactone | buyable | /acne-treatment/ | /diuretic/spironolactone/ | "$45 for a 3-month supply" | published | spironolactone · oral · hormonal acne |
| Tretinoin Cream | buyable | /acne-treatment/ | /retinoid/tretinoin-cream-025-2mo | "$60 for a 2-month supply" | published | tretinoin 0.025% · topical cream |
| Azelaic Acid | buyable | /acne-treatment/ | /antiseptic/azelaic-acid/ | "$90 for a 3-month supply" | published | azelaic acid · topical |
| Clindamycin Phosphate Solution | buyable | /acne-treatment/ | /antibiotic/clindamycin/ | "$40 for a 2-month supply" | published | clindamycin phosphate · topical solution |
| Clindamycin Phosphate Gel | buyable | /acne-treatment/ | /antibiotic/clindamycin-phosphate-gel/ | "$60 for a 3-month supply" | published | clindamycin phosphate · topical gel |
| Clindamycin Phosphate Lotion | buyable | /acne-treatment/ | /antibiotic/clindamycin-phosphate-lotion/ | "$80 for a 3-month supply" | published | clindamycin phosphate · topical lotion |
| Minocycline | buyable | /acne-treatment/ | /antibiotic/minocycline/ | "$40 for a 1-month supply" | published | minocycline · oral antibiotic |
| Benzaclin Gel | buyable | /acne-treatment/ | /antibiotic/benzaclin/ | "$70 for a 2-month supply" | published | clindamycin + benzoyl peroxide · topical gel |
| Anti-aging | buyable | /skincare-treatments/ | /anti-aging-treatment/ | — (cash-pay; no insurance) | on-request | retinoids/Rx + OTC · topical · price behind consult |
| Eyelash growth serum | buyable | /skincare-treatments/ | /eyelash-serum/ | — (cash-pay) | on-request | molecule not stated (bimatoprost-class) · topical · "darker, longer, up to 2x fuller in 16 weeks" |
| Melasma & dark spots | buyable | /skincare-treatments/ | /melasma-treatment/ | — (cash-pay) | on-request | topical · price behind consult |
| Rosacea | buyable | /skincare-treatments/ | /rosacea-treatment/ | — (insurance/FSA per /our-services) | on-request | topical · price behind consult |
| Sexual health (herpes) | family | — | — | — | — | cold sore + genital herpes Rx |
| Cold sore (oral herpes) | buyable | sexual health | /oral-herpes-treatment/ | — | on-request | antiviral · oral · treat/prevent oral herpes |
| Genital herpes | buyable | sexual health | /genital-herpes-treatment/ | — | on-request | antiviral · oral · treat/prevent genital herpes |
| Hair & scalp | family | — | — | — | — | women's hair loss + dandruff |
| Women's hair loss | buyable | hair & scalp | /womens-hair-loss/ | "initial consultation fee of $80" + "Most women's hair loss patients pay $20 per month" | partial | minoxidil/oral (per-SKU molecule not stated) · topical/oral · cash-pay (HSA/FSA); free shipping |
| Dandruff | buyable | hair & scalp | /dandruff-treatment/ | — | on-request | topical · price behind consult |
| General health | family | — | — | — | — | BV · menopause · UTI · vaginitis · yeast · migraine |
| Bacterial vaginosis | buyable | general health | /bacterial-vaginosis-treatment/ | — ("Insurance") | on-request | Rx · oral/topical · "get treatment fast" |
| Vaginitis | buyable | general health | /vaginitis-treatment/ | — ("Insurance") | on-request | Rx · price behind consult |
| Yeast infection | buyable | general health | /yeast-infection-treatment/ | — ("Insurance") | on-request | Rx antifungal · price behind consult |
| UTI | buyable | general health | /uti-treatment/ | — ("Insurance") | on-request | Rx antibiotic · price behind consult |
| Menopause | buyable | general health | /menopause-treatment/ | — | on-request | menopause/HRT Rx · price behind consult |
| Migraine | buyable | general health | /cove/ | — | on-request | routed to sibling brand **Cove** (withcove.com) — not Nurx-fulfilled |

## Verbatim anchors

The footnotes that decide `partial` vs `published`:

- **GLP-1 page anchor:** "### Starts at $650/month" with "Medication cost may vary based on prescribed treatment, price not guaranteed. **Medications are not available for shipment through Nurx. Final cost determined by your pharmacy and insurance coverage.** … Additional costs apply, including a medical review, provider support, and side effect management." (/weight-management/glp1-injections/)
- **Weight-management fees (the on-top cost):** "Anyone who requests weight management treatment will be charged a **$79 consultation fee**." + "you will pay a recurring monthly **$79 provider support fee** … this fee is not eligible for insurance coverage." + "If you are prescribed oral medication, the cash price for your treatment plan will cost **$60-329/month**." + "Brand-name GLP-1 … pricing typically ranges from **$650-1300/month** … for the lowest dose without insurance … You will pick up and pay for your medication at your local pharmacy." (/weight-management-treatment/)
- **Mental-health fee structure:** "Mental health treatment through Nurx costs **$59 for the initial consultation and $69 per month for ongoing medication management** … The consultation is not covered by insurance. We bill insurance for medications." Med table: "As little as **$0/month copay**" (insurance) / "**$25**" (without). (/mental-health/)
- **Acne:** "Once you share your health history and **pay $40 for your medical consultation** … If covered under your insurance plan, your prescribed treatment could cost as little as **$0**." (/acne-treatment/)
- **EC:** OTC "**$19.50 per pill with $0 shipping**"; Ella "As low as **$0 with insurance or $45 without (+ $15 medical consultation fee)**"; "expedited overnight shipping for **$15**." (/emergencycontraception/)
- **Women's hair loss:** "There is an **initial consultation fee of $80**, and then the cost of your treatments. **Most women's hair loss patients pay $20 per month**. Shipping is always free." + "We do not accept insurance for women's hair loss treatment … We accept most HSA and FSA cards." (/womens-hair-loss/)

**Molecule-sourcing audit (`not stated`):** Ella's molecule (ulipristal acetate) is **not named** on /emergencycontraception/ — only the brand "Ella®" and Rx status; left `not stated`. The ring/patch brand names and women's-hair-loss/eyelash per-SKU molecules are **not stated** on their pages (described by form/class only) — left `not stated`, never inferred. GLP-1 and mental-health/acne molecules **are** page-attested (brand→molecule printed beside each).

## Deep blocks

**GLP-1 injections — the flagship, and the one line whose headline price misleads.** *(Earned: the "$650/month" anchor materially understates the all-in, and the line is the only one with real branded product renders.)*

- **Spine:** [/weight-management/glp1-injections/](store/nurx-com/captures/2026-06-04/glp1_injections.md). Six branded pens, each a "Starts at $X/month on average" card (no individual PDP), all "In-person pharmacy pick up only / not shipped by Nurx."
- **Why the headline lies:** the page leads "Starts at $650/month" — that is **Victoza's** floor *at your local pharmacy, lowest dose, without insurance*. On top sits a **$79 one-time consult** and a **$79/mo provider support fee** (neither insurance-eligible), and the higher-demand pens run **$1000–1300/mo** (Zepbound $1000, Wegovy $1300, Saxenda $1300, Ozempic $1000, Mounjaro $1000). So the realistic all-in for a popular GLP-1 is the **$1000–1300/mo pen price plus the $79/mo support fee** (plus the one-time $79 consult) — well above the $650 headline. Oral alternatives (naltrexone/bupropion/topiramate/metformin) are the in-house, shippable, cheaper path at "$60-329/month" + the same $79/mo fee.
- **Structural tell:** for GLP-1 Nurx is a **clinician-fee business, not a dispensary** (it earns the $79+$79 while the pharmacy sells the drug) — the inverse of its mail-order model on every other line.
- **Hero / product renders (captured):** the flagship's clean branded renders are saved under `captures/2026-06-04/images/`:
  - `glp1-injections-hero.png` — labeled multi-pen hero (Zepbound · Saxenda · Wegovy, 985×985)
  - per-pen isolated renders: `zepbound.jpg`, `wegovy.jpg`, `saxenda.jpg`, `ozempic.png`, `mounjaro.png`, `victoza.png`
  - *All carry "For illustration purposes only"; downloaded headed from imgix (browser UA + Referer) — fc.py's bare fetch 403s.*

*No other per-SKU deep block earned — the roster carries the rest. (Other lines reuse generic "Nurx RX only" stock imagery, not true product renders.)*

## Provenance

- **Pages read (cited captures, 2026-06-04):** /birthcontrol/, /weight-management-treatment/, /weight-management/glp1-injections/, /our-services, /acne-treatment/, /mental-health/, /emergencycontraception/, /womens-hair-loss/ (+ homepage). All in `store/nurx-com/captures/2026-06-04/`.
- **Scope:** enumerated to the **company's indexed level** — every condition line + the SKUs/methods each page prices. **Not enumerated:** the 50+ individual birth-control products (behind the quiz at with.nurx.com; only method floors public) and the un-deep-scraped lines (anti-aging, melasma, rosacea, eyelash, cold sore, genital herpes, dandruff, BV, vaginitis, yeast, UTI, menopause) — rostered as lines with their nav slugs, prices `on-request`.
- **Gated / unreachable:** final per-prescription pricing sits behind the intake (with.nurx.com), not submitted; branded GLP-1 final cost is set by the patient's local pharmacy.
- **Point-in-time caveat:** prices are page-stated and explicitly "not guaranteed"; a promo bar pushes weight management ("$0 with insurance") — treat pricing/IA as a snapshot, re-check next run.
- **Run profile:** opt-in module, express run — **+ hero/PDP product images** captured for the flagship GLP-1 line (7 renders promoted to `captures/2026-06-04/images/`), referenced from the deep block. No PDP-template anatomy block requested.
