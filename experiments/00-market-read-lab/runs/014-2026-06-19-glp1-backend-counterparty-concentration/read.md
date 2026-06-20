# Market Read

## Question

In the store's compounded-GLP-1 cohort, which brands **name** a pharmacy/fulfillment or
clinical-provider backend counterparty, do any named counterparties **recur across brands**
(supplier concentration), and is that relation load-bearing enough to capture as a joinable edge?

## Direct Answer

**Naming is the exception, not the rule, and the one real concentration signal is clinical, not pharmacy.**

Of **19** `anchor_category: GLP-1` brands, only **5** name *any* backend counterparty; the other **14**
route to a `third-party` "partner pharmacy" that is **explicitly unnamed** (the possessive-language pattern
flagged in run 001). Within the named set:

- **Pharmacy counterparties are named but almost all dangling** — 3 brands name a fulfillment pharmacy
  (directmeds → **CraftedRx**; home-medvi → **Triad Rx / RedRock Pharmacy / Beaker Pharmacy & Compounding**;
  eden → **Eden Pharmacy**, an *owned* sibling in `owns:`). **None of the third-party pharmacy names resolve
  to a store profile** — they are named-but-unjoinable. No pharmacy name recurs across two brands.
- **The clinical-provider edge is where concentration actually shows up** — 2 brands name the *same* clinical
  network: home-medvi → **OpenLoop Health** (+ CareGLP Affiliated P.C.s) and joinfridays → **OpenLoop Health**.
  **OpenLoop resolves cleanly to `store/openloophealth-com`** — a captured B2B clinician-staffing /
  telehealth-infrastructure company ("every CTA is Contact Sales", `/provider-staffing`). This is the only
  counterparty in the cohort that *both* recurs across ≥2 brands *and* joins to a store profile.

**Verdict on the MRL-005/006 graduation decision (this run is the designed re-test):** the recurrence test
**fires partially**. It confirms run 001's "named is the minority" on a second cohort (5/19), but for the first
time produces a concrete, store-joinable, cross-brand shared counterparty — **OpenLoop as white-label clinical
infrastructure behind ≥2 GLP-1 DTC brands**. That is a genuine supplier-concentration *lead* (clinical, not
pharmacy) and the strongest evidence yet for a joinable edge — but the joinable set is **sparse** (one recurring
entity, two brands), so it argues for the *minimal* capture shape (a dotted-domain frontmatter mirror for brands
that name a resolvable counterparty), **not** an edge table or relation registry.

## Evidence Used

All from cached store State (no external sources; `store-only`). Store clock: captures dated in each
`telehealth.md`; hims/MEDVi/Fridays bodies carry 2026-06 refresh notes. Claim IDs:

- **C1 — cohort denominator (partial).** `grep -rl "anchor_category: GLP-1" store/*/telehealth.md` → **19** brands:
  brellohealth, directmeds, effecty, eden-health, goodlifemeds, henrymeds, home-medvi, ivimhealth, hims, joinfound,
  joinamble, ivyrx, mydrhank, joinfridays, noom, remedymeds, tryshed, ro-co, telolife. *Anchor-only grep under-counts
  GLP-1 offerers* (MRL-001: LifeMD/Nurx/Wisp sell GLP-1 without anchoring) — this census is scoped to the **anchored**
  cohort and labeled as such, not the whole GLP-1 universe.
- **C2 — pharmacy_model split.** Frontmatter verbatim: **16 third-party**, **3 integrated** (eden, hims, ro-co). 0 of
  19 carry a `parent:`/`owns:` line in `telehealth.md` frontmatter; eden's owned-pharmacy link lives in
  `profile.md` `owns: [edenhealthclubs.com, edenpharmacy.com]`.
- **C3 — named pharmacy counterparties.** Quoted from `telehealth.md` Fulfillment bodies:
  - directmeds: *"CraftedRx is a licensed U.S. compounding pharmacy…"* (skin/pain PDPs); GLP-1 fulfillment cites a
    **separate, unnamed** U.S. pharmacy.
  - home-medvi: *"Partner pharmacies include: **Triad Rx · RedRock Pharmacy · Beaker Pharmacy & Compounding**"*
    (homepage footer, named with addresses).
  - eden: footer "More from Eden" links **Eden Pharmacy (edenpharmacy.com)** — owned sibling, not a third-party partner.
  - **Profile-resolution check:** `store/*craftedrx*`, `*triad*`, `*redrock*`, `*beaker*`, `*edenpharmacy*` → **no
    store profile** for any. (Note: `store/hallandalerx-com` exists but is **not named** by any cohort brand.)
- **C4 — named clinical-provider counterparties.** `grep -il openloop` over the cohort → **2 brands**:
  - home-medvi: *"clinical delivery outsourced to **OpenLoop Health** (US-licensed provider network) + CareGLP
    Affiliated P.C.s — 'OpenLoop Health clinicians retain the decision to prescribe'"*.
  - joinfridays: *"Clinical services are provided by **OpenLoop Health** and other networks of U.S.-licensed
    clinicians"*; card descriptor "OPNLP FRIDAYS."
  - **Profile-resolution check:** **`store/openloophealth-com` exists** (`name: OpenLoop Health`, B2B clinician
    staffing, Contact-Sales pricing). The MEDVi→OpenLoop and Fridays→OpenLoop edges **would both join cleanly.**
- **C5 — the unnamed majority (the 001 contamination pattern).** 14/19 use possessive/generic language with no entity:
  e.g. brellohealth *"our partner pharmacy"*, effecty *"our trusted pharmacy partner"*, goodlifemeds *"U.S.-based,
  state-licensed pharmacies"*, henrymeds *"licensed U.S. compounding pharmacies"*, remedymeds *"licensed U.S.
  compounding pharmacies"*, telolife *"licensed compounding pharmacies"*, tryshed *"a third-party dispensing
  pharmacy"*, ivimhealth *"independent, licensed compounding pharmacies"*, joinamble *"licensed pharmacies within
  its affiliated network"*, etc. These are **not** named counterparties and must not be counted as edges.

## Companies Seen

19 anchored GLP-1 brands (C1). Named-counterparty subset and join status:

| Brand | pharmacy_model | Named pharmacy partner | Named clinical group | Joins to store profile? |
|---|---|---|---|---|
| home-medvi-org | third-party | Triad Rx · RedRock · Beaker | **OpenLoop Health** + CareGLP P.C.s | clinical→**yes** (OpenLoop); pharmacy→no |
| joinfridays-com | third-party | — (list linked, not captured) | **OpenLoop Health** | clinical→**yes** (OpenLoop) |
| directmeds-com | third-party | CraftedRx (non-GLP-1 lane) | — | no |
| eden-health | integrated | Eden Pharmacy (owned, `owns:`) | — | owned sibling has no profile |
| hims-com | integrated | Ohio affiliated facility (unnamed) | — (400+ in-house providers) | n/a (captive) |
| ro-co | integrated | ro.OS (captive, self) | — | n/a (captive) |
| Other 13 (brello, effecty, goodlife, henry, ivim, joinfound, joinamble, ivyrx, mydrhank, noom, remedy, tryshed, telolife) | third-party | **none — unnamed** | **none** | no edge to draw |

## Missing / Stale Coverage

- **Counterparty profiles mostly absent.** CraftedRx, Triad Rx, RedRock, Beaker, Eden Pharmacy, CareGLP — none
  captured. So even where a pharmacy *is* named, there is no join target today; the edge would dangle.
- joinfridays links a partner-pharmacy list at `/terms-conditions/#pharma` that was **not captured** — its pharmacy
  counterparties are unknown, not absent.
- `parent`/`owns` is not used at all in the cohort's `telehealth.md` frontmatter; eden's only sits in `profile.md`.
  Confirms MRL-006's split (clean joinable relations live in `profile.md`; backend partners live in prose).

## Source Gaps

Pure store read — no external denominator, no Signals layer touched. "Named vs unnamed" depends entirely on what
each brand chose to publish on its owned pages and what the capture grabbed; a brand could use OpenLoop (or a shared
pharmacy) without naming it, so **absence of a name is "not stated," not "no relationship."** The OpenLoop
concentration is therefore a **floor**, not a ceiling — there may be more shared-backend reliance than two brands name.

## External Completeness Check

Not run — completeness of the *named-counterparty* set is not the load-bearing claim (the answer is explicitly
"naming is sparse"). The denominator caveat (C1, anchor-only under-count) is carried instead of an external panel,
consistent with `store-only` and the bounded-live clock being preserved.

## Market Pattern

- **Compounded-GLP-1 fulfillment is a black box by design.** 14/19 brands route to an unnamed "partner pharmacy";
  naming a pharmacy is the exception (3/19), and the 3 integrated players (eden/hims/ro) describe *integration* without
  resolving ownership-of-dispensing. Buyers cannot tell who actually compounds their drug from the owned pages — the
  pharmacy layer is deliberately abstracted.
- **The clinical layer is where shared infrastructure leaks through.** Two unrelated DTC brands (MEDVi, Fridays) both
  run on **OpenLoop Health**, a B2B clinician-staffing platform. This is the cohort's only concrete supplier-concentration
  signal and the only counterparty that joins to a store profile. It suggests the reusable "who does brand X depend on"
  edge is **clinical-network-shaped** at least as much as pharmacy-shaped — the opposite emphasis from MRL-005's original
  pharmacy framing.
- **Judgment (labeled):** OpenLoop functioning as white-label clinical backend for ≥2 GLP-1 brands is a *lead* worth a
  joinable edge, but two brands is not "concentration" in any market-power sense — it is one recurrence. The honest
  output is "first cross-brand, store-joinable counterparty observed," not "the cohort is concentrated on OpenLoop."

## What Would Change This Answer

- A **third** brand naming OpenLoop (or any single pharmacy recurring across ≥2 brands) would move this from "one
  recurrence" toward a real concentration claim and strengthen the edge-capture case.
- Capturing the joinfridays `/terms-conditions/#pharma` partner list, or any of the dangling pharmacies
  (CraftedRx, Triad Rx, RedRock, Beaker) as store profiles, would turn named-but-dangling pharmacy edges into joinable ones.
- Running the same read on a **non-compounded / FDA-brand** GLP-1 cut (or a different cohort) to see whether OpenLoop /
  shared clinical networks recur there too — that would test whether clinical-backend concentration is a GLP-1 artifact
  or a telehealth-wide pattern.
