# Receipt - Traction-signal store inventory + cohort-rollup overlay

Supports the run's traction-readiness map: which companies expose which traction signal,
at what comparability grain, and whether any cohort rolls up.

```yaml
receipt_type: store-query
created: 2026-06-20
evidence_mode: store-only
source_grade: derived
source_family: local-store
spend_note: none
snippet_only: no
claim_ids_supported: [C1, C2, C3, C4, C5, C6, C7, C8]
```

## Sources

| Source ID | URL / local path | Captured / store clock | Source family / type | Grade | Spend | Snippet-only? | Claims supported |
|---|---|---|---|---|---|---|---|
| S1 | `store/*/signals/<source_type>/[<page>/]<captured_at>.json` (49 signals dirs) | store clock (captures dated 2026-06-08 → 2026-06-15) | local-store / derived inventory | derived | none | no | C1,C2,C3,C4,C5,C8 |
| S2 | `store/*/profile.md` frontmatter + prose (126 profiled) | store snapshot | local-store | derived | none | no | C6 |
| S3 | `store/*/telehealth.md` `anchor_category:` (GLP-1 grep; 54 telehealth.md) | store snapshot | local-store | derived | none | no | C7 |
| S4 | `_design/2026-06-14-traction-frame.md` + `_design/2026-06-15-traction-approach.md` | 2026-06-14/15 | local-design-doc | primary (internal) | none | no | C1 axis-ladder framing |
| S5 | `experiments/00-market-read-lab/runs/018-.../read.md` + MRL-012 evidence | prior run | local-lab-artifact | derived | none | no | C4 comparability quality |

## Method

- **Inventory:** Python walk of every `store/*/signals/` dir. For each company, counted
  capture files per `source_type`; for Wayback, descended to the page-slug grain
  (`signals/wayback/<page>/<clock>.json`) per the run-018 / MRL-012 page-grain note.
  "Delta-able" = ≥2 captures with **distinct** capture timestamps (first 15 chars of the
  `YYYYMMDDThhmmssZ` filename) on a **traction** source-type.
- **Traction axis mapping** (from the traction-frame + SIGNALS.md / tools): `sec_edgar`→
  capital/funding; `trustpilot`→demand/trust-flow proxy; `trends`→attention/search-interest;
  `serpapi`→attention/SERP-visibility; `ads_transparency`→attention/ad-presence.
  **NOT traction:** `wayback`→tenure/continuity (page age/existence); `exa_similar`→neighbors.
- **State scan:** `awk` frontmatter extract over all `profile.md`, grepped for traction-State
  keys (founded/funding/ticker/headcount/employees/revenue/valuation/arr); plus a prose grep
  for funding/public-market language.
- **Cohort rollup:** GLP-1 = `anchor_category:` **value field** (parsed before any `#` comment)
  == `GLP-1` in `telehealth.md` → **19 strict-anchored** members; intersected with the any-traction
  and delta-able sets. Telehealth universe = all 54 `telehealth.md` companies.
  - **Method caveat (MRL-001 / run-016):** a loose `^anchor_category:.*GLP-1` line-grep returns
    **21** and a "any GLP-1 mention" match returns up to **24**, because brands like nurx/prohealth
    carry `GLP-1` in the `#` comment of a `multi/none` or `longevity/NAD` line. The Loop-1 read first
    used the loose grep (21); the Loop-2 evidence verifier caught it. **Parse the value, not the
    comment** — the run-016 method note, recurring here. The numerators (5 any-traction, 4 delta-able)
    are unaffected: all 5 overlap cos are strict-anchored.

## Evidence

**Universe:** 135 store dirs / **126 profiled** (`profile.md`) / 54 with `telehealth.md` /
49 with a `signals/` dir.

**Per-source-type coverage (companies-with-it / delta-able [≥2 dated captures]):**

| source_type | traction axis | companies | delta-able |
|---|---|---|---|
| sec_edgar | capital/funding | 20 | 4 |
| trustpilot | demand/trust-flow | 20 | 9 |
| trends | attention/search | 5 | 0 |
| serpapi | attention/SERP | 2 | 2 |
| ads_transparency | attention/ads | 1 | 0 |
| **wayback** | **NONE (tenure)** | 47 | 10 |
| **exa_similar** | **NONE (neighbors)** | 2 | 0 |

**Traction-signal cos (union of the 5 traction types) = 20:** agelessrx, defymedical,
directmeds, eden-health, getpetermd, gogeviti, hims, honehealth, hydramed, joinamble,
joinfridays, marekhealth, maximustribe, mylifeforce, niagenplus, sermorelin, struthealth,
trtnation, truniagen, waldo. *(sec_edgar and trustpilot cover nearly the identical 20 —
captured as one batch campaign on hormone/men's-health brands → inherits the corpus's
selection bias.)*

**Delta-able traction cos = 11:** agelessrx, eden-health, hims, honehealth, hydramed,
joinamble, joinfridays, maximustribe, niagenplus, sermorelin, waldo.

**Shared-axis check (can delta-able cos be ranked against each other?):** trustpilot 9,
sec_edgar 4, serpapi 2. Only Trustpilot has enough delta-able members to compare — and that
delta is review-count velocity = solicitation cadence on paid profiles, not demand
(MRL-008 / MRL-012).

**GLP-1 cohort rollup (denominator 19 strict-anchored):** any-traction-signal **5/19**
(directmeds, eden, hims, joinamble, joinfridays); delta-able **4/19** (eden, hims, joinamble,
joinfridays) — all four share **only Trustpilot** as their cross-company delta axis (hims also
has a sec_edgar delta, but no other GLP-1 brand does, so it can't be ranked against a peer).

**Telehealth-wide rollup (denominator 54):** any-traction-signal 19/54; delta-able 10/54.

**State layer:** **0** of 126 `profile.md` carry any structured traction frontmatter key;
**29** mention funding/public-market status incidentally in prose (e.g. "publicly traded",
"raised $").

## Limits

- Coverage counts are **capture-campaign artifacts, not market facts** — `signals/` presence
  reflects which companies a prior lab/ops campaign captured (hormone/men's-health-heavy),
  not which companies have real-world traction. Absence = **not captured**, never "no traction."
- "Delta-able" here means **≥2 dated captures of a traction type**, i.e. *cadence* exists; it
  does **not** mean a clean usable velocity. Per run-018/MRL-012, of the delta-able set only
  ~6 Trustpilot velocities are clean; sec_edgar had no `signal_delta.py` delta branch at run time
  (branch shipped 2026-06-22); SERP "pairs" can be unpaired (different query under same dir,
  subject-identity gap); Trends is single-snapshot for all 5 and batch-normalization-fragile. So
  rung-2 quality is weaker than the raw delta-able count suggests.
- This receipt is a **store-substrate inventory**, not a traction read of any company. It
  deliberately emits **no** traction/formidability score or verdict (the frame's hard line).

## Claim Map

| Claim ID | Claim supported | Evidence | Caveat |
|---|---|---|---|
| C1 | Traction is Signals (time-axis), scored on the frame's 5-rung ladder; 5 store source-types proxy traction, 2 (wayback/exa) do not | S1,S4 | axis mapping is interpretive but follows the frame + SIGNALS.md |
| C2 | 49/126 profiled cos have a `signals/` dir, but only **20** carry any genuine traction signal | S1 | capture-campaign artifact |
| C3 | The most-captured signal (Wayback, 47 cos) is **not** traction | S1 | tenure/continuity, not "how doing" |
| C4 | Only **11/126** are delta-able on a traction type, and most deltas are blocked/confounded | S1,S5 | per run-018/MRL-012 |
| C5 | Among delta-able cos, only Trustpilot has enough members to compare (9); sec 4, serp 2 | S1 | no cross-company non-Trustpilot axis |
| C6 | State layer carries **0** structured traction fields (correct by frame); 29 prose mentions | S2 | frame: traction never lands in profile.md |
| C7 | GLP-1 cohort: 5/19 any-signal, 4/19 delta-able, all sharing only Trustpilot → no real rollup | S3,S1 | 19 strict-anchored (method-sensitive 19–24; numerators unaffected) |
| C8 | Append-only `signals/<type>/<clock>.json` accumulation path exists and is the right durable shape | S1 | frame open-Q #1 resolved in v1 |
