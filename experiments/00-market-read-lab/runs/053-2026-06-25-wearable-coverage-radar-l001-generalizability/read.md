# Market Read

## Question

For a buyer choosing a wearable / sleep / recovery tracker, which category members do
third-party "best of 2026" listicles + SERPs repeatedly name, and which of those does
Truffle's store not have captured at all? And does the **graduated L001 coverage-radar
recipe** (SERP → ≥2 listicles → cross-source intersection → token-match store diff) hold
on a fuzzy-boundary consumer-hardware category, or does category blur (smart ring vs
smartwatch vs recovery band vs sleep system) degrade the cross-source intersection?

`gap-probe`, `bounded-live`. Two source families (SERP + editorial listicle), 3 outside
sources read, 3 net paid credits of an 8-credit ceiling.

## Result

**The radar produced a clean, corroborated coverage gap — AND it exposed two failure
modes of L001's recipe that the telehealth source-runs never could. Both halves are the
result.**

**(1) The buyer-facing answer (clean).** Of the externally-named "best tracker 2026" set,
the store holds exactly **4** — Oura, Whoop, Apple Watch, Eight Sleep — and lacks the
**mainstream-volume majority**. The missing set is **tiered by evidence strength** (sharpened
per evidence-verifier VR2): **Fitbit** (incl. the 2026 Fitbit Air + Charge 6), **Withings**
(ScanWatch Light + Sleep mat), and **Amazfit** (Active 2 + Bip 6) are explicit *picks* on a
full editorial list plus SERP corroboration — high confidence; **Garmin** and **Samsung** rest
on a full-list *nav/related mention* + SERP snippet only — weaker footing, still ≥2-source.
Google/Pixel rides in as Fitbit's parent. None captured (C1). A single-source tail (Huawei,
Xiaomi, Hume, Ultrahuman, Muse, Bía, RISE, Apollo Neuro) is leads-only, not a corroborated
gap. (Caveat per verifier C1: `apple-com` is a company-level capture, not an Apple-Watch-SKU
capture.) So a buyer asking "what am I missing" gets a real answer: the store over-indexes on
premium *recovery/optimization* brands (Oura/Whoop/Eight Sleep) and is blind to the
high-volume *mainstream fitness-band* brands (Fitbit/Garmin/Samsung/Amazfit).

**(2) L001 mechanically generalizes, but category blur degrades it two specific ways:**

- **Sub-category listicle disjointness (denominator-sensitivity).** The category does not
  resolve to one editorial population. The **sleep-axis** list (Oura, Eight Sleep, Bía,
  Muse, RISE) and the **fitness-axis** list (Hume, Fitbit, Huawei, Amazfit, Garmin)
  intersect on only **Oura, Whoop, and Withings** (C2 — corrected per evidence-verifier
  VR1; Withings appears on both lists, so the original "almost nothing but Oura/Whoop" was
  an overreach — 3 of ~15 distinct brands overlap, still a steep disjointness). In
  telehealth (L001's source runs
  012/022/024), "best GLP-1" lists largely *overlapped*, so "≥2 listicles corroborate"
  was robust. Here, *which two lists you pick drives the named-set* — a sharper
  `denominator-reconciliation` failure: a naïve single-list radar would report a wildly
  different "missing" set depending on whether it grabbed a sleep list or a fitness list.
- **The store's cohort boundary doesn't match the editorial category** (C3). The store's
  "wearable/recovery" set includes Peloton (connected fitness equipment), Therabody &
  Hyperice (percussive/recovery hardware), and Nike (athletic apparel + a recovery
  partnership) — and **none of the four appears in either tracker list**. So the diff's
  denominator is contested *before* any token-matching: "what counts as in the category"
  is itself the question. The radar can answer "who is missing" only after a human fixes
  the category boundary it cannot derive.

**Verdict on L001:** the recipe **holds** (it produced a corroborated missing-set on a
fresh, non-telehealth vertical), but its load-bearing assumption — that a category maps
to one overlapping listicle population — is telehealth-shaped. On a fuzzy consumer-
hardware category it needs an explicit sub-category + cohort-boundary step that L001 as
written does not name. **No new primitive needed**; membership stays a query-time recipe,
now with a documented generalization caveat.

## Gap Map

| Dimension | Truffle answered | Truffle fell short | What would change it |
|---|---|---|---|
| Who is in the store's wearable cohort | ✓ Clean — 8 dedicated makers via grep (oura/whoop/eightsleep/peloton/apple/therabody/hyperice/nike) | — | — |
| Who the *category* names externally | Recovered cheaply (1 SERP + 2 listicles) | The named-set depends on which sub-axis list is read (C2) | A 3rd, category-spanning editorial list, or an analyst taxonomy |
| Who the store is **missing** | ✓ High-confidence for ≥2-source brands: Fitbit, Garmin, Withings, Samsung, Amazfit, Google | Single-source tail (Huawei/Xiaomi/Hume/Ultrahuman/Muse/Bía) is leads-only | More independent editorial lists to corroborate the tail |
| What "the category" even is | — | **The store's cohort boundary ≠ the editorial tracker category** (Peloton/Therabody/Hyperice/Nike in neither list) (C3) | A human-fixed category definition; the radar cannot derive it |
| Ranking / which is best | — | Listicle rankings are vendor/affiliate-biased (Hume #1–2 advertiser; Circular self-#1) (C4) | A neutral analyst grid; out of bounded scope |

## Evidence Used

Lines up with `run-notes.md` `live_evidence_used`. Full table + excerpts in receipt
[`C1-external-named-set-and-store-diff.md`](receipts/C1-external-named-set-and-store-diff.md).

- **C1** (store holds 4, lacks mainstream majority): S1 SERP + S2 Sleep Foundation + S3
  Wareable + S4 store token-match.
- **C2** (sub-category listicle disjointness): S2 (sleep axis) vs S3 (fitness axis).
- **C3** (store cohort boundary ≠ editorial category): S2, S3 vs S4 + store frontmatter.
- **C4** (vendor/affiliate ranking bias): S3 (Hume advertiser, #1–2) + S1 (Circular self-#1).

Current/pricing/named-set claims rest on dated scrapes (S2 page modified 2026-04-22; S3
modified 2026-06-02), not snippets. SERP rows (S1) are labeled direction-finding.

## Companies Seen

**Store-captured wearable/recovery cohort (8 dedicated makers + Casio watches):**
ouraring, whoop, eightsleep, onepeloton, apple, therabody, hyperice, nike (casio = watches,
not a health tracker). Of these, only Oura/Whoop/Eight Sleep/Apple appear in any external
tracker list; Peloton/Therabody/Hyperice/Nike appear in none (C3).

**Externally-named, missing from store (high-confidence, ≥2 sources):** Fitbit, Garmin,
Withings, Samsung, Amazfit, Google/Pixel.
**Externally-named, missing, single-source (leads only):** Huawei, Xiaomi, Hume, Ultrahuman,
Muse, Bía, RISE, Apollo Neuro, SLEEPON, Wellue, Oxiline, Circular, Polar/Coros (not named
this panel).

## Missing / Stale Coverage

The 6 high-confidence missing brands (Fitbit/Garmin/Withings/Samsung/Amazfit/Google) are
the volume center of the consumer wearable market — the store's captured set is skewed to
premium recovery/optimization. This is a *capture-coverage* gap, not a market fact:
"not captured" ≠ "not a real competitor" (L005 corollary). Whether to capture them is
spend/approval-gated and out of scope here.

## Source Gaps

- **A neutral, category-spanning denominator.** Both editorial lists are sub-axis-scoped
  (sleep vs fitness) and carry affiliate bias; neither is a clean category census. A
  buyer-grade ranked neighborhood would need an analyst/lab taxonomy (e.g. a tracker
  category grid) — a source family the bounded plan did not model (cousin of run-047 CR3).
- **The single-source tail** would need ≥1 more independent editorial list to promote any
  of Huawei/Xiaomi/Hume/Ultrahuman from lead to corroborated gap.

## Raw Learning to Preserve

For Loop 2 to append to `learning/observations.md`. See `run-notes.md` Observations:
G1 (sub-category listicle disjointness — L001 generalization caveat), G2 (store cohort
boundary ≠ editorial category), S1 (L001 mechanically generalizes — positive), S2 (the
missing-set is the market's volume center, store skews premium), R1 (vendor/affiliate
ranking bias — L004 instance), R2 (bounded-live source-substitution when a planned list
is unscrapeable).

## External Completeness Check

Done — that is the run. Store-derived cohort (8) was diffed against an external named-set
from 2 independent editorial listicles + SERP leads. The completeness limit is explicit:
light panel, high-confidence missing-set only for ≥2-source brands; "not found in this
panel," not "not a category member."

## Market Pattern

**(Judgment — run inference from a 2-list panel + 10-brand diff, not store State; flagged
per dev-review DR1. Read as a hypothesis, not a market fact.)** The consumer wearable-tracker
market reads as **bimodal, with the store sitting in one mode**: a premium
*recovery/optimization* tier (Oura, Whoop, Eight Sleep — subscription-led, $300–3000, the
store's strength) and a high-volume *mainstream fitness-band/smartwatch* tier (Fitbit,
Garmin, Samsung, Amazfit, Xiaomi — $50–400, hardware-led, the store's blind spot). The two
tiers barely share listicles, which is exactly why a single coverage-radar denominator
misleads on this category. The store-level fact this rests on — *capture skews to premium
recovery, misses the fitness-band mainstream* — is solid; the "bimodal market" framing is
the more speculative extrapolation (2-list artifact risk per C2 applies here too).

## What Would Change This Answer

- A 3rd category-spanning editorial list that overlaps both sub-axes would test whether
  C2's disjointness is a 2-list artifact or a real category property.
- If a real downstream consumer needed a *queryable* wearable-category membership set
  (not a one-shot radar), the W1 question reopens: does category membership stay a
  query-time recipe, or earn a stored cohort tag? Today it stays query-time — the named
  set is cheap to re-derive and the cohort boundary needs a human anyway (C3).
- Capturing the 6 missing volume brands would convert the radar's "negative space" into
  a store-queryable neighborhood — but only a real consumer justifies that spend.
