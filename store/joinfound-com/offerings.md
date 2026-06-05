---
# Query contract for this store: ../../QUERYING.md — parse frontmatter; grep the body to locate.
schema_version: "1.2"
domain: joinfound.com
captured_at: 2026-06-04
enumeration: indexed-complete   # all 16 toolkit lines + program + microdosing rostered; per-dose tiers are intake-gated leaf detail (11 branded/oral rows index/nav-attested, not deep-PDP-captured — see scope)
site_notes: "Catalog = the /medication index (rich-captured) + nav flyout + footer toolkit list (Webflow site; molecule + form attested on the index cards, e.g. 'GLP-1injectionsemaglutidecompounded'). Two purchasable price surfaces: /plans-and-pricing (the GLP-1 Program — $149/mo insurance / $199/mo cash on a 12-mo upfront plan; $199/$299 monthly) and the per-PDP comparison tables (compounded = 'one flat price, no separate membership'; Found cash floors for Foundayo/Wegovy/Zepbound in the /foundayo table). The $1100/$650 branded figures in the pricing-page toolkit slider are MARKET-comparison refs, NOT Found's price. Per-dose pricing is intake-gated (clinic.joinfound.com health assessment). Insurance-dependent: the '$17/month' floor on /insurance is the deep-discount in-network membership — a different line than the $149 program price. A/B: not fingerprinted, but pricing/IA reads point-in-time (offer terms 'subject to change')."
---

## Portfolio overview

`Multi-product` weight-care brand: one **membership program** (the clinical-care access layer) over a **~16-medication toolkit** (the breadth pitch — "a toolkit of 10+ medications, including non-GLP-1s and GLP-1s … access regardless of formulary coverage"). The toolkit splits three ways: **compounded GLP-1s** (semaglutide, tirzepatide, liraglutide — Found's own-priced "one flat price" lane), **FDA-brand GLP-1s** (Ozempic, Wegovy, Zepbound, Mounjaro, Rybelsus, Saxenda, Victoza, Trulicity, and Foundayo/orforglipron — prescribed/coordinated, mostly insurance-routed), and **non-GLP-1 orals** (metformin, Contrave, topiramate, zonisamide — low-cost adjuncts).

Prominence (calibrated): **Compounded Tirzepatide + Compounded Semaglutide lead** — first two items in both the homepage "Top treatments" grid and the Medication nav flyout `[HIGH — own grid order + nav order]`. **Foundayo™ (orforglipron)** gets a featured push as a just-approved (4/1/2026) oral GLP-1 `[MED — nav slot + dedicated PDP + homepage card]`. **Microdosing** has its own nav slot + "NEW: Lower starting weights now accepted" badge `[MED]`. Branded injectable GLP-1s (Ozempic/Wegovy/Zepbound/Mounjaro) sit mid-grid `[MED]`; **non-GLP-1 orals are toolkit-depth**, low visibility `[LOW]`. The real pricing story is structural, not per-SKU: compounded = flat cash price, no separate membership; everything else is **insurance-gated** (the wedge), so most rows read `partial`/`on-request`.

## Roster

| Offering | Kind | Parent | Slug | Price (verbatim) | Visibility | What (molecule · form · access) |
|---|---|---|---|---|---|---|
| GLP-1 Program | family | — | /plans-and-pricing | "starting at $149/mo with insurance / $199/mo with cash pay" (12-mo upfront; "$199/mo … insurance and $299/mo for cash-pay" monthly) | partial | clinical care + personalized GLP-1 plan + Aimee AI concierge · membership · async; medication billed separately |
| — DTC, with insurance | buyable | (program) | /insurance | "Weight loss memberships starting at $17/month" ("Save up to 90% … with insurance," "Copays as low as $0") | partial | in-network clinical-care membership · plan/state-dependent |
| — DTC, cash pay | buyable | (program) | /plans-and-pricing | "$199/mo with cash pay" (12-mo upfront); "$299/mo" monthly | published | self-pay membership; clinical care included; medication separate |
| — For business (employer) | buyable | (program) | /business | "Contact sales" (claim: "proven 5.1x ROI") | on-request | employer metabolic-care benefit · in-network claims · MetabolicPrint |
| — For health plans | buyable | (program) | /health-plans | "Contact sales" | on-request | health-plan offering |
| Compounded Semaglutide | buyable | medication | /medication/compounded-semaglutide | "one flat price" at every dose — incl. (GLP-1 Program "$149/mo with insurance / $199/mo with cash pay") | partial | semaglutide · weekly subcutaneous injection · compounded (503A), Rx |
| Compounded Tirzepatide | buyable | medication | /medication/compounded-tirzepatide | "one flat price" at every dose — incl. (GLP-1 Program "$149/mo … / $199/mo with cash pay") | partial | tirzepatide (GLP-1/GIP) · weekly injection · compounded (503A), Rx |
| Compounded Liraglutide | buyable | medication | /medication/compounded-liraglutide | incl. (GLP-1 Program — per-page price not captured) | on-request | liraglutide · injection · compounded (503A), Rx |
| Foundayo™ | buyable | medication | /medication/foundayo | "Starting cash price ~$149/mo" | partial | orforglipron · once-daily oral tablet (6 doses: 0.8–17.2 mg) · FDA-brand (Eli Lilly, approved 4/1/2026), Rx |
| Microdosing | buyable | medication | /microdosing | incl. (program — not separately priced) | on-request | semaglutide (low/micro-dose) · weekly injection · compounded; "preventive metabolic care," Rx |
| Wegovy® | buyable | medication | /medication/wegovy | Found cash: pill "~$149/mo", pen "~$199/mo"; market ref "from $650/mo+" | partial | semaglutide · injection or oral pill · FDA-brand (Novo Nordisk), Rx |
| Zepbound® | buyable | medication | /medication/zepbound | Found cash "~$299/mo"; market ref "from $650/mo+" | partial | tirzepatide (GLP-1/GIP) · weekly injection · FDA-brand (Eli Lilly), Rx |
| Ozempic® | buyable | medication | /medication/ozempic | market ref "$1100/mo" (not Found's price) | on-request | semaglutide · weekly injection · FDA-brand (Novo Nordisk), insurance-routed, Rx |
| Mounjaro® | buyable | medication | /medication/mounjaro | market ref "~$1100/mo" (not Found's price) | on-request | tirzepatide (GLP-1/GIP) · weekly injection · FDA-brand (Eli Lilly), Rx |
| Rybelsus® | buyable | medication | /medication/rybelsus | (not captured) | on-request | semaglutide · oral · FDA-brand (Novo Nordisk), Rx |
| Saxenda® | buyable | medication | /medication/saxenda | "Pricing varies" | on-request | liraglutide · injection · FDA-brand (Novo Nordisk), Rx |
| Victoza® | buyable | medication | /medication/victoza | "Pricing varies" | on-request | liraglutide · injection · FDA-brand (Novo Nordisk), Rx |
| Trulicity® | buyable | medication | /medication/trulicity | (not captured) | on-request | not stated (dulaglutide not page-attested) · injection · FDA-brand (Eli Lilly), Rx |
| Metformin | buyable | medication | /medication/metformin | (not captured) | on-request | metformin · oral tablet · generic, Rx |
| Contrave® | buyable | medication | /medication/contrave | (not captured) | on-request | not stated (molecule absent from index card) · oral · FDA-brand, Rx |
| Topiramate | buyable | medication | /medication/topiramate | (not captured) | on-request | topiramate · oral · generic, Rx |
| Zonisamide | buyable | medication | /medication/zonisamide | (not captured) | on-request | zonisamide · oral · generic, Rx |

## Verbatim anchors

The footnotes that decide `partial` vs `published`, quoted exactly:

- **GLP-1 Program (pricing page):** "starting at / $149/mo / with insurance / $199/mo / with cash pay … *Pricing based on 12-month plans paid up-front. Monthly plans start at $199/mo for insurance and $299/mo for cash-pay. Visits for insurance plans may require copays. … Price varies based on medication, insurance and coverage.*" — /plans-and-pricing. → all-in varies by med/insurance ⇒ `partial`; the cash 12-mo line ($199) is self-contained ⇒ `published` on that row.
- **Insurance floor:** "Weight loss memberships starting at $17/month*" with "*In-network insurance coverage details, pricing and terms vary. Copays, coinsurance and deductibles may apply*"; "Save up to 90% on your membership with insurance," "Copays as low as $0." — /insurance. → in-network/plan-dependent ⇒ `partial`.
- **Compounded flat-price (both compounded GLP-1 PDPs):** "Price stays the same at every dose | **Yes — one flat price** … Separate membership required | **No**" — /medication/compounded-semaglutide & /compounded-tirzepatide. The PDPs state no $ number; price inherits the GLP-1 Program floor ⇒ `partial`.
- **Foundayo / branded cash floors (the /foundayo comparison table):** "Starting cash price | **Foundayo™ ~$149/mo** | **Wegovy® Pill ~$149/mo** | **Wegovy® Pen ~$199/mo** | **Zepbound® ~$299/mo**" — /medication/foundayo. → Found's stated cash floors; move with dose/plan ⇒ `partial`.
- **Market-reference prices (NOT Found's):** "Ozempic® **$1100/mo**," "Mounjaro® **~$1100/mo**," "Wegovy® **from $650/mo+**," "Zepbound® **from $650/mo+**" — /plans-and-pricing toolkit slider. These anchor retail cost for contrast; Found's actual price for these brands is insurance-gated ⇒ `on-request`.
- **Foundayo = orforglipron (molecule + brand, page-attested):** "Foundayo is a brand name for orforglipron, a small molecule GLP-1 receptor agonist manufactured by Eli Lilly … available as an oral tablet in six doses: 0.8 mg, 2.5 mg, 5.5 mg, 9 mg, 14.5 mg, and 17.2 mg … approved by the FDA on April 1, 2026." — /medication/foundayo. (Disclaimer also lists Foundayo™ as a Lilly trademark — mark ownership ambiguous; see profile `unverified_fields`.)
- **Molecule audit (`not stated`):** Contrave® and Trulicity® — the captured /medication index card shows only "oral" (Contrave) / no molecule tag (Trulicity), so molecule is `not stated`, not inferred (bupropion-naltrexone / dulaglutide are NOT page-attested for these SKUs). Metformin, Topiramate, Zonisamide are generic-named ⇒ molecule = the product name (attested). All GLP-1 molecules ARE attested on the index cards (e.g. "tirzepatideGLP-1 / GIPinjection" for Mounjaro).

## Deep blocks

None earned — the roster carries this company. The two real ambiguities are captured inline: Foundayo = orforglipron (anchored above, resolving "is this compounded or brand?" → FDA-brand Lilly), and the layered/insurance-gated pricing (anchored to its three source lines). The compounded GLP-1s are molecule/form variants of one flat-priced program lane; the branded toolkit is prescribe-and-route, not Found-priced.

## Provenance

- **Pages read:** under `captures/2026-06-04/` — /medication (rich index: card molecule/form/order + nav flyout + footer toolkit), /plans-and-pricing, /insurance, /business, /health-plans (nav-attested), /program, and PDPs compounded-semaglutide, compounded-tirzepatide, compounded-liraglutide, foundayo, microdosing; homepage for prominence.
- **Scope:** all 16 medication-toolkit lines + the program (4 channel rows) + microdosing rostered — **complete at the indexed level**. **Deep-PDP-captured: 4 meds** (compounded sema/tirz/lira, foundayo) + microdosing; the **other 11 branded/oral rows are index/nav/footer-attested** (name, slug, molecule + form from the captured index cards, price only where page-shown). Per-dose ladders and exact per-plan prices are intake-gated leaf detail (not exploded into rows). No line/category omitted.
- **Gated/unreachable:** per-dose & per-plan prices (set in the clinic.joinfound.com assessment, not submitted); Found's actual price for insurance-routed brand drugs (Ozempic/Mounjaro/Rybelsus/Trulicity, etc.); /reviews aggregate.
- **Point-in-time:** pricing is a snapshot — offer terms "subject to change"; insurance figures vary by state/plan, and the $100-off promo was live at capture. Re-check before quoting.
- **Run profile:** Express — `offerings.md` enabled alongside `profile.md` + `telehealth.md` + `logos`; plain roster (no hero-image capture, no PDP-anatomy block).
