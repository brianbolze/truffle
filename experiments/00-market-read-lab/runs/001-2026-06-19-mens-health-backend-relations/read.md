# Market Read

Status: answered 2026-06-19 (Run 001). Store-only; no scraping, no spend.
Governing clocks: captures 2026-05-30..06-18, oldest ~20d.

## Question

In men's health / hormone telehealth, which companies reveal shared backend relationships
(parent brand, clinical provider network, pharmacy / fulfillment partner), and are those
relationships load-bearing enough to justify a typed relation candidate?

## Direct Answer

**Relations are real and partly load-bearing — but the load-bearing part is mostly *already
captured*, and the genuinely new part is too sparse to typecast yet.** Across 18 men-led /
hormone telehealth brands, the three edge types separate cleanly by how much they move the
market read and how well the store already holds them:

- **Parent / front-door — load-bearing, and already a primitive.** The clearest case:
  **RexMD → LifeMD** (joinable both ways — `lifemd.com owns [rexmd, shapiromd, navamd]`).
  It *explains offer shape*: RexMD punts branded-GLP-1 / insurance-billed patients **up to
  LifeMD**, so the parent edge is why Rex's own menu looks compounded-only. **Hims → Hims & Hers**
  (name-only public parent) and a **captive Ohio pharmacy** is why Hims reads `integrated`. This
  edge already lives in `profile.md` `parent`/`owns` frontmatter — and Run 0 already surfaced the
  same LifeMD/RexMD relation. **No new primitive; it's working.**

- **Pharmacy / fulfillment — weakly load-bearing; the posture beats the name.** Only **5 of 18**
  name a pharmacy entity (Curexa, Strive, SmartScripts/PerfectRx, the MEDVi trio, Belmar/Olympia);
  the other 13 say only *"licensed US compounding pharmacy."* Ownership language is **marketing, not
  structure** — BlueChew says *"our own compounding pharmacies"* then names **three third parties**
  (Meds Health, National Treatment Delivery & Care, Curexa) in the same FAQ. The signal that moves the
  read is the **integrated-vs-third-party posture**, which is *already* the `pharmacy_model` field. A
  *named*-pharmacy edge only earns its keep where the partner is **shared** (supplier concentration).

- **Clinical provider network — potentially the most load-bearing for regulated care, but the
  thinnest evidence.** Only **~3** name the medical group: **MEDVi → OpenLoop + CareGLP Affiliated
  P.C.s** (explicit: *"MEDVi is the brand/UX layer; both the medical group and the pharmacies are
  third parties"*), **Hone → an independent physician-owned medical group**, **Sermorelin → Wasef
  Health, PC**. Everyone else says *"licensed providers"* generically. This is where a typed edge
  *would* matter most (trust / risk / margin) and where the **capture grain is weakest**.

**The structural pattern worth naming:** the modal men's-health brand is a **thin marketing/UX layer
over a third-party clinical network + a third-party compounding pharmacy** — MEDVi states it outright;
most compounded-only brands imply it. A minority are vertically integrated (getOpt *"our pharmacy"*,
Hims' captive affiliate). **And the shared backend counterparties are already store profiles** —
OpenLoop, MDIntegrations, Curexa, Strive, Hallandale — so a typed supplier edge would *join*, not
dangle. That's the one new thing this run surfaces.

**Verdict:** submit a **supplier/fulfillment relation candidate** — but **do not graduate**. Parent
ownership is covered by `parent`/`owns`; integration posture by `pharmacy_model`; everything else is
a **query-time join** (QUERYING Recipe 3) over named, store-resolvable counterparties. The edge is
named in the minority of cases and absence ≠ no relationship — that caveat alone argues against baking
a sparse, half-empty field.

## Evidence Used

- **`store/*/telehealth.md`** (54 packs; 18 in the men/hormone slice) — `audience`, `anchor_category`,
  `pharmacy_model`, `value_chain_role` to scope the cohort; the **Fulfillment** + **Provider** body
  lines for the verbatim pharmacy/clinical claims.
- **`store/*/profile.md`** frontmatter — `parent` / `owns` for the corporate edges (joinable dotted
  domains vs name-only).
- **Supply-side profiles** — `openloophealth-com`, `mdintegrations-com`, `strivepharmacy-com`,
  `hallandalerx-com`: the B2B counterparties the DTC relations point *to*, confirming the edges resolve.
- Receipt: [`receipts/backend-relations-worksheet.md`](receipts/backend-relations-worksheet.md)
  (working set, all three edge tables, cross-store recurrence, load-bearing test).

Verbatim anchors:
- **Parent is load-bearing:** rexmd — *"Parent LifeMD sits above for insurance-billed / branded-GLP-1
  patients, but Rex itself names no captive pharmacy"* (telehealth.md Fulfillment).
- **Ownership claim ≠ structure:** bluechew — *"we partner with our own compounding pharmacies"* then
  names **Meds Health, LLC · National Treatment Delivery and Care LLC · Curexa** in the same FAQ.
- **The thin-layer pattern, stated:** home-medvi — *"MEDVi is not acting as a pharmacy… Partner
  pharmacies include: Triad Rx · RedRock · Beaker"* + *"outsourced to OpenLoop Health + CareGLP
  Affiliated P.C.s."*

## Companies Seen

**18 men-led / hormone DTC brands** with `telehealth.md` (working set, not a census):

- **Vertically integrated (own/captive pharmacy claim):** getOpt, Hims.
- **Third-party, pharmacy named:** BlueChew (Curexa +2), MaleMD (Curexa), Invigor (Strive/Tailor
  Made/Belmar/Olympia/Gogomeds), Sermorelin (SmartScripts/PerfectRx), MEDVi (Triad/RedRock/Beaker).
- **Third-party, pharmacy unnamed ("licensed US compounding pharmacy"):** getPeterMD, Maximus,
  Dr Hank, RexMD, Rugiet, TRT Nation, VitalityRx, HormoneMD, Defy.
- **Parent / front-door edge:** RexMD → LifeMD (joinable), Hims → Hims & Hers (name-only),
  Marek → owns marekdiagnostics.com.
- **Clinical group named:** MEDVi (OpenLoop + CareGLP P.C.), Hone (independent physician-owned group),
  Sermorelin (Wasef Health, PC).

**Supply-side counterparties already profiled** (the edges resolve, not dangle): OpenLoop & MDIntegrations
(white-label clinical infra), Curexa / Strive / Hallandale (503A compounding pharmacies; Strive & Hallandale
*recruit provider partner networks* — the mirror image of the DTC edge).

## Missing / Stale Coverage

- **Clinical-provider grain is the weakest layer.** Most brands name no medical group — *"licensed
  providers"* is as deep as the capture goes. The few named P.C.s (Wasef, CareGLP) are the exception.
  If clinical-provider relations become load-bearing, that's a **capture-grain** ask, not first a primitive.
- **Pharmacy names are minority-captured (5/18).** "Not named" ≠ "no partner" — most brands simply
  don't publish the entity. A `none/third-party` posture is captured; the *identity* usually isn't.
- **honehealth-com / invigormedical-com / home-medvi-org** carry packs but aren't men-led — pulled in
  for their relations only; don't read them as men's-cohort members.
- **Freshness is fine** (oldest ~20d). Backend partners churn slowly, but a brand can swap a pharmacy
  network without notice — re-check before asserting a *current* supplier relationship.

## Source Gaps

- The read needed **nothing outside the store** — no SERP, Wayback, or live fetch. Every edge is a
  page-attested claim the capture already holds, plus the existing `parent`/`owns` frontmatter.
- **Relations are not verifiable from the store, by design.** The pack records the *claim*
  (*"we own our pharmacy"*) and never adjudicates it — BlueChew is the proof the marketing claim and
  the named third parties disagree. Any "who *really* fulfills this" question is a deep-research job,
  not a store read.

## External Completeness Check

Completeness is not the load-bearing claim for this run. The working set is the men/hormone slice of
the telehealth packs — a **scoped working set, not a denominator**. No external panel was used or needed;
the question is about *edge structure within a known set*, not *how many brands exist*.

## Market Pattern

- **Backend structure splits into three postures the front end hides:** vertically integrated
  (getOpt, Hims) · parent-owned front door (RexMD under LifeMD) · thin brand over third-party
  clinic + pharmacy (MEDVi, most compounded-only brands). The universal profile reads identical
  for all three; the relation + `pharmacy_model` cut is what separates them.
- **Marketing ownership language is noise; the named counterparty is signal.** "Our pharmacy" / "our
  own" recurs even when the same page names third parties. Trust the named entity (or the absence),
  never the possessive.
- **Supplier concentration is the real latent finding.** A handful of B2B backends — OpenLoop,
  MDIntegrations, Curexa, Strive, Hallandale — sit behind many DTC brands, and they're *already
  profiled*. The interesting market question ("which compounding pharmacy / clinical network is the
  category's single point of failure?") is answerable as a **query-time in-degree count** the moment a
  few more named edges land — exactly the `store.py relations` join that already exists.

## What Would Change This Answer

- **More named edges.** If the next captures pull pharmacy/clinical entities for the 13 currently-unnamed
  brands, supplier concentration becomes measurable and the typed-edge case strengthens from "submit"
  toward "graduate." Today it's too sparse.
- **Regulatory pressure on 503A compounding.** If compounded access tightens, brands lean on the
  branded-drug path — which routes through the *parent* (RexMD→LifeMD) or a different pharmacy lane,
  re-shaping every edge in the table.
- **A brand swapping its backend.** These are quiet B2B relationships; a pharmacy or provider-network
  change wouldn't show as a price move. A Signal/freshness layer would be where that gets caught —
  not State.
- **Treating clinical-provider as the primary edge.** If trust/risk is the question (not margin), the
  affiliated-P.C. relationship outranks the pharmacy one — and the read flips from "well covered" to
  "thinnest layer, capture it first."
