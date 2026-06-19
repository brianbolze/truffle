# Backend-Relations Worksheet — Run 001

Store-only, no scraping, no spend. Captures span ~2026-05-30..06-18.
Working set, not a census: the men-led / hormone / sexual-health slice of the
telehealth cohort packs (`audience ∈ {men-only, men-first}` OR
`anchor_category ∈ {TRT, sexual-health, peptides}`), plus three starter-scope
brands without packs that the body still speaks to.

## Working set (18 DTC brands with `telehealth.md`)

| Brand | audience | anchor | pharmacy_model | parent (frontmatter) | owns |
|---|---|---|---|---|---|
| bluechew-com | men-only | sexual-health | third-party | — | — |
| defymedical-com | men-first | TRT | third-party | — | — |
| getopt-com | men-first | TRT | integrated | — | — |
| getpetermd-com | men-first | TRT | third-party | — | — |
| hims-com | men-only | GLP-1 | integrated | "Hims & Hers Health, Inc." (name-only) | — |
| malemd-com | men-only | multi/none | third-party | — | — |
| marekhealth-com | men-first | TRT | third-party | — | marekdiagnostics.com |
| maximustribe-com | men-first | TRT | third-party | — | — |
| mydrhank-com | men-first | GLP-1 | third-party | — | — |
| rexmd-com | men-only | sexual-health | third-party | lifemd.com (joinable) | — |
| rugiet-com | men-only | sexual-health | third-party | — | — |
| sermorelin-com | men-first | peptides | third-party | — | — |
| trtnation-com | men-first | TRT | third-party | — | — |
| vitalityrx-com | men-only | TRT | unclear | — | — |
| hormonemd-com | all-genders | TRT | third-party | — | — |
| honehealth-com | (no pack here)* | — | unclear | — | — |
| home-medvi-org | (multi front door) | GLP-1 | third-party | — | — |
| invigormedical-com | (no pack here)* | — | — | — | — |

\* honehealth-com / invigormedical-com / home-medvi-org carry `telehealth.md`;
their audience/anchor aren't men-led but the body relations are in-scope.
`lifemd-com` (the parent) also carries a pack: `owns: [rexmd.com, shapiromd.com, navamd.com]`.

## Edge type 1 — Parent / front-door (corporate ownership)

Joinable (dotted-domain) or name-only, from `profile.md` frontmatter `parent`/`owns`:

- **rexmd-com → lifemd.com** (joinable both ways: lifemd `owns` rexmd, shapiromd, navamd).
  Load-bearing: RexMD's branded-GLP-1 / insurance-billed path runs *through* LifeMD —
  *"Parent LifeMD sits above for insurance-billed / branded-GLP-1 patients"* (rexmd telehealth.md).
- **keeps-com → thirtymadison.com** (joinable; not men-cohort-central but a real edge).
- **hims-com → "Hims & Hers Health, Inc."** (name-only — the public parent; not a joinable peer).
- **marekhealth-com → owns marekdiagnostics.com** (its own sibling diagnostics storefront).

Recurrence: this is the **same LifeMD/RexMD parent edge Run 0 already surfaced**.

## Edge type 2 — Pharmacy / fulfillment partner

Mostly third-party; **named only in the minority**. Ownership language is marketing.

| Brand | pharmacy claim | named entity? |
|---|---|---|
| bluechew | "our own compounding pharmacies" — but same FAQ names 3 third parties | **Meds Health LLC · National Treatment Delivery & Care LLC · Curexa** |
| malemd | "our US-based FDA-approved pharmacy" | **Curexa** (footer partner modal) |
| invigormedical | "partnered national pharmacies" | **Strive · Tailor Made · Belmar · Olympia · Gogomeds** |
| sermorelin | "our licensed US compounding pharmacy partner" | **SmartScripts / PerfectRx** (Flower Mound, TX) |
| home-medvi | "MEDVi is not acting as a pharmacy… partner pharmacies include" | **Triad Rx · RedRock · Beaker Pharmacy** |
| getopt | "ship from **our pharmacy**" | none (integrated claim, unverifiable) |
| hims | "partner pharmacies" + "Ohio-affiliated pharmacy facility opened" | none named (captive-affiliate posture) |
| defymedical | "network of pharmacies" | none |
| getpetermd / maximustribe / mydrhank / rexmd / rugiet / trtnation / vitalityrx / hormonemd | "licensed US compounding pharmacy" generic | **none** |

So: 5/18 name a pharmacy entity; the rest say only "licensed US compounding pharmacy."
The `integrated` vs `third-party` posture already lives in `pharmacy_model`.

## Edge type 3 — Clinical provider network / affiliated P.C.

The thinnest captured edge. Named in only ~3 of the men's set:

- **home-medvi → OpenLoop Health (provider network) + CareGLP Affiliated P.C.s** — explicit:
  "MEDVi is the brand/UX layer; both the medical group and the pharmacies are third parties."
- **honehealth → independent physician-owned medical group** ("Hone-affiliated medical practices
  are independently owned and operated by licensed physicians").
- **sermorelin → Wasef Health, PC / Dr. Michael Wasef, MD** (named third-party physician group).
- Everyone else: "licensed providers" / "US-licensed physicians" generically — no named entity.

## Cross-store recurrence of the named backend counterparties

The counterparties are **already profiled store entities** (so a typed edge would *join*, not dangle):

- **Curexa** → bluechew, malemd.
- **OpenLoop** → home-medvi, joinfridays, + `openloophealth-com` profile (B2B white-label
  telehealth infra: clinician network + EHR + payer + back-office).
- **MDIntegrations** (`mdintegrations-com`) → profiled infra ("You control the brand, we power
  the medicine"; physician-only network, 50 states).
- **Strive** (`strivepharmacy-com`) → invigor + profiled (503A pharmacy that *recruits a provider
  partner network*).
- **Hallandale** (`hallandalerx-com`) → profiled (503A, "15,000+ prescribing practitioners").
- **Affiliated P.C. / professional corporation** language: altrx, home-medvi, lifemd,
  mdintegrations, prohealth.

## Load-bearing test (does the relationship change the market read?)

- **Parent/front-door — YES.** Determines branded-drug / insurance path and margin posture
  (RexMD↔LifeMD; Hims captive pharmacy). Already captured via `parent`/`owns`.
- **Pharmacy — WEAKLY.** Most signal is the `pharmacy_model` *posture* (integrated vs third-party),
  already a field. A *named* pharmacy edge matters only where **shared** (supplier concentration:
  Curexa, Strive, Hallandale) — and that's a query-time grep today (QUERYING Recipe 3 relations join).
- **Clinical — POTENTIALLY MOST, evidence THINNEST.** Trust/risk/margin for regulated care turns on
  who holds the medical group, but only ~3 brands name the P.C. Capture-grain gap, not obviously a
  new primitive.
