# Market Read

## Question

Outside compounded GLP-1, do DTC telehealth brands share **named** clinical-provider or
pharmacy backends — i.e., is the OpenLoop-style backend concentration that run 014 found
in GLP-1 a GLP-1-compounding artifact, or a telehealth-wide market structure?

## Direct Answer

**Backend sharing is NOT a GLP-1 artifact — it recurs across the non-GLP-1 store. But the
*axis flips*.** Outside GLP-1, the shared backend is the **compounding pharmacy**, not a
clinical-provider network. The single cleanest, store-joinable cross-brand edge is **Strive
Pharmacy** (`strivepharmacy-com`), named as a partner by **two** non-GLP-1 brands —
**hevahealth-com** and **invigormedical-com** (C3, C7). Three more compounding pharmacies
each recur across two brands but **dangle** (no store profile): **Curexa** (bluechew +
malemd), **Tailor Made Compounding** (invigormedical + mylifeforce), **Olympia**
(hydramed + invigormedical) (C4–C6).

This is the **mirror image of run 014** (Judgment, J1). In GLP-1 the shared, joinable
backend was *clinical* (OpenLoop Health behind 2 brands) while every pharmacy dangled; in
non-GLP-1 the shared, joinable backend is the *pharmacy* (Strive) while the only named
third-party *clinical* group is a singleton (**Beluga Health**, prohealth-com only, C8) and
no shared clinical network (OpenLoop/SteadyMD/Wheel/Curai) appears anywhere outside GLP-1
(C9). The compounded-Rx **supply substrate is shared either way**; which layer a brand
chooses to *name* on its owned pages differs by cohort.

**Concentration language withheld by contract.** Each pharmacy recurs across only **2**
brands within a ~35-brand non-GLP-1 set — that is a *shared-supplier lead*, not measured
concentration. The aggregate (4 distinct compounding pharmacies, each shared by 2 brands) is
a substrate pattern worth a watch, not a market-structure claim.

## Evidence Used

Store-only; store clocks 2026-06-04 → 2026-06-18. Claim IDs map to receipt `S1`.

| ID | Claim | Source (store-local) |
|---|---|---|
| C1 | 35 non-GLP-1 brands carry structured `telehealth.md` (TRT 8, longevity/NAD 8, multi/none 10, sexual-health 3, peptides 2, + labs/womens-HRT/hair/primary-care singletons). | `grep anchor_category store/*/telehealth.md` |
| C2 | Corporate ownership (`parent`/`owns`) is the only relation cleanly in `profile.md` frontmatter; it captures *brand families* (Thirty Madison → keeps + nurx; LifeMD → rexmd; Niagen Bioscience → niagenplus + truniagen; Amazon → onemedical), not backend suppliers. | `grep ^parent\|^owns store/*/profile.md` |
| C3 | hevahealth-com names **Strive Pharmacy** + Stryker Compounding Pharmacy as partners: *"We work with Strive Pharmacy and Stryker Compounding Pharmacy — both state-licensed specialty pharmacies"* (/how-it-works). | `store/hevahealth-com/telehealth.md` |
| C7 | invigormedical-com names 5 partner pharmacies incl. **Strive Pharmacy**: *"Strive Pharmacy, Tailor Made, Belmar Pharma Solutions, Olympia Pharmacy, and Gogomeds"* (/about-invigor). | `store/invigormedical-com/telehealth.md` |
| C4 | **Curexa** named by 2 brands: malemd-com (footer "Partner Pharmacy: Curexa") + bluechew-com (FAQ names Curexa Pharmacy among 3 LLCs). | `store/{malemd,bluechew}-com/telehealth.md` |
| C5 | **Tailor Made** named by 2 brands: invigormedical ("Tailor Made") + mylifeforce ("Tailor Made Compounding", tailormadecompounding.com). | `store/{invigormedical,mylifeforce}-com/telehealth.md` |
| C6 | **Olympia** named by 2 brands: hydramed ("Olympia Pharmaceuticals", Orlando FL) + invigormedical ("Olympia Pharmacy"). Name variant; same Orlando entity inferred, not adjudicated. | `store/{hydramed,invigormedical}-com/telehealth.md` |
| C8 | Only named third-party **clinical** group outside GLP-1 is **Beluga Health** (prohealth-com: *"Our clinical providers are Beluga Health c/o Jonah Mink MD… Beluga Health, P.A."*); it is a singleton in this cohort. hone + lifemd use unnamed / in-house affiliated medical groups. | `store/{prohealth,honehealth,lifemd}-com/telehealth.md` |
| C9 | No shared clinical network (OpenLoop/SteadyMD/Wheel/Curai) appears in any non-GLP-1 `telehealth.md`; the only OpenLoop citers (home-medvi, joinfridays) are both GLP-1. | `grep -ril steadymd\|wheel\|curai\|openloop store/*/telehealth.md` |
| C10 | Entity resolution, **three join-readiness tiers**: (a) **joinable** (has `profile.md`) — `strivepharmacy-com` (Strive, aliases "Strive Compounding Pharmacy") and `hallandalerx-com`; (b) **captured-but-no-profile** — `belmarpharmasolutions-com` is a store directory with a `captures/` folder only, **no `profile.md`**, so not joinable at depth (Loop-2 verifier catch); (c) **no store entry at all** — Curexa / Tailor Made / Olympia / Empower / Precision / Valiant / Casa Pharma / Beluga (dangle). | `ls store/*<name>*` (per-dir contents checked) |
| C11 | Reverse dangle: `hallandalerx-com` is a captured 503A compounding pharmacy ("supplies… to 15,000+ licensed prescribers") that **no** captured brand names in `telehealth.md` — supplier-in-store, edge-absent. | `store/hallandalerx-com/profile.md` + grep |

## Companies Seen

35 non-GLP-1 structured brands (C1). Backend-naming brands: hevahealth, invigormedical,
malemd, bluechew, hydramed, mylifeforce (pharmacy names); prohealth (clinical name). Supplier
profiles with `profile.md` (joinable): `strivepharmacy-com` (cited ×2), `hallandalerx-com`
(uncited), `openloophealth-com` (GLP-1 only). Captured-but-no-`profile.md` (not joinable at
depth): `belmarpharmasolutions-com` (cited ×1).

## Missing / Stale Coverage

- **Most named pharmacies dangle** (C10): Curexa, Tailor Made, Olympia, Empower, Precision,
  Valiant, Casa Pharma, Meds Health LLC, National Treatment Delivery LLC have no store
  profile, so the supplier substrate is mostly **un-joinable at depth** — the MRL-006
  capture-grain gap, now seen from the *pharmacy* side across a second cohort.
- **Anchored-only denominator** (MRL-001): the 35 is the anchored non-GLP-1 set; multi-service
  generalists that sell into these cohorts without anchoring are not separately counted. The
  recurrence counts are **floors**.
- Naming is owned-page self-report; absence of a named pharmacy ≠ absence of a relationship
  (14/19 GLP-1 brands and several here route to an unnamed "partner pharmacy").

## Source Gaps

No external panel used (store-only by contract). A SERP/state-board lookup could confirm the
Olympia "Pharmaceuticals" vs "Pharmacy" name-variant is one entity (C6) and resolve the
dangling pharmacies — out of scope here, flagged as a bounded-live candidate.

## External Completeness Check

Not run — completeness is explicitly framed as a floor, not a census. The load-bearing
finding (Strive recurs and joins) is a positive existence claim that an external check could
only strengthen, not overturn.

## Market Pattern

- **A shared compounding-pharmacy substrate underlies the compounded-Rx telehealth world**
  (TRT, longevity/peptides, sexual-health, multi). A handful of 503A/503B compounders
  (Strive, Curexa, Tailor Made, Olympia, Empower, Belmar) appear behind multiple otherwise-
  unrelated brands. invigormedical alone fronts 5 of them — the brands are storefronts over a
  smaller pool of fulfillment partners.
- **Brands name the layer they want to credentialize.** Compounded-Rx brands (non-GLP-1)
  name their *pharmacy* partners (it signals quality/legitimacy for compounded meds);
  compounded-GLP-1 brands named their *clinical* network (OpenLoop) and hid the pharmacy. The
  backend exists in both; the disclosed layer is a marketing choice.
- **The join fails from both directions** (J2): named-but-uncaptured suppliers (Curexa,
  Tailor Made) vs captured-but-unnamed suppliers (hallandalerx). A supplier-concentration
  map would need both halves closed.

### Judgments (labeled)

- **J1** — Backend sharing is telehealth-wide, not a GLP-1 artifact; the *joinable axis flips*
  (clinical in GLP-1 → pharmacy in non-GLP-1). Rests on C3–C10 + run 014's OpenLoop finding.
- **J2** — The supplier substrate is real but mostly un-joinable today (C10/C11); the minimal
  graduation shape from run 014 (`clinical_provider:` dotted-domain mirror) is **insufficient
  alone** — a parallel `pharmacy_partner:` axis is needed, populated only when the named
  entity resolves to a `profile.md` (only **Strive** does so among the cited compounders;
  belmar has captures but no profile). Judgment over a partial, anchored sample.
- **No new primitive is needed to *answer* this read** — it was grep+resolve over existing
  State. Whether the *edge* graduates is a separate human decision (MRL-005).

## What Would Change This Answer

- A **third** non-GLP-1 brand naming Strive (or any pharmacy clearing 3 brands) would push
  the pharmacy substrate from "recurrence lead" toward a defensible concentration claim.
- Capturing the dangling compounders (Curexa, Tailor Made, Olympia) would convert most of the
  substrate from un-joinable to joinable and could reveal much denser sharing than the floor
  shows.
- If a future capture shows a shared *clinical* network outside GLP-1 (SteadyMD/Wheel
  recurring), the "axis flips by cohort" judgment (J1) would soften toward "both axes shared
  everywhere."
