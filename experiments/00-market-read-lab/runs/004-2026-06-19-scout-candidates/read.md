# Market Read

## Question

Across the captured telehealth store, which product/condition categories are most
crowded (most distinct DTC brands competing) and which are thin?

## Direct Answer

**GLP-1 / weight is the most crowded category by a wide margin, on every measure the
store supports. Mental health is the thinnest. Everything in between is a band of
overlapping "men's / hormone / longevity" lines that the same brands bolt onto each
other.** Working set: **53 DTC telehealth brands** that carry both a `telehealth.md`
pack and an `offerings.md` roster (the one captured non-DTC pack, functionhealth-com /
`diagnostics/labs`, is excluded per contract). Read every number as a **captured floor,
not a market census** (`coverage-caveat`).

Two complementary cuts agree:

**Front door — `anchor_category` (normalized, one per brand, n=53) [State]**

| Front-door category | DTC brands | 
|---|---:|
| GLP-1 | 19 |
| multi/none | 10 |
| longevity/NAD | 8 |
| TRT | 8 |
| sexual-health | 3 |
| peptides | 2 |
| hair | 1 |
| womens-HRT | 1 |
| primary-care | 1 |

**Breadth — distinct brands with a *buyable SKU* whose molecule names the category, in
the `offerings.md` roster (n=53) [State]**

| Category | DTC brands selling in it |
|---|---:|
| GLP-1 / weight | 41 |
| peptides | 30 |
| longevity / NAD | 30 |
| TRT / testosterone | 27 |
| sexual health / ED | 24 |
| hair loss | 23 |
| women's HRT | 22 |
| mental health | 10 |

The single sharpest finding: **41 of 53 brands carry a buyable GLP-1 SKU, but only 19
anchor on it — 22 brands sell GLP-1 as a bolt-on to a different front door** (TRT,
longevity, sexual health, primary care). GLP-1 is both the most common storefront *and*
the near-universal add-on. [Judgment, from the two State tables above: GLP-1 is the
gravity well of the captured cohort.]

## Evidence Used

All store-only; no external claims, no current/news/pricing/policy assertions.

- **C1** — DTC gating + front-door counts: `store/*/telehealth.md` frontmatter
  (`value_chain_role`, `anchor_category`), 54 packs, 53 gated to `DTC brand`.
- **C2** — breadth counts: `store/*/offerings.md` `## Roster` rows, molecule matched
  inside the buyable-SKU `What (molecule · form · access)` / name cells only (family
  header rows excluded).
- **C3** — GLP-1 spillover (41 sell / 19 anchor / 22 bolt-on): C1 ∩ C2 on the GLP-1
  molecule set.

Receipt: `receipts/category-crowdedness-derivation.md` (source grade: derived).

Governing clocks: `telehealth.md` captures **2026-05-30 .. 2026-06-18** (oldest ~20d);
`offerings.md` captures **2026-06-03 .. 2026-06-18** (oldest ~16d), as of 2026-06-19.

## Companies Seen

53 DTC telehealth brands (the gated working set):
agelessrx-com, bluechew-com, brellohealth-com, defymedical-com, directmeds-com,
eden-health, effecty-com, gethealthspan-com, getopt-com, getpetermd-com, gogeviti-com,
goodlifemeds-com, hellopepti-com, hellowisp-com, henrymeds-com, hevahealth-com, hims-com,
home-medvi-org, honehealth-com, hormonemd-com, hydramed-com, innerbalance-com,
invigormedical-com, ivimhealth-com, ivyrx-com, joiandblokes-com, joinamble-com,
joinfound-com, joinfridays-com, keeps-com, kingsbergmedical-com, lifemd-com, malemd-com,
marekhealth-com, maximustribe-com, mydrhank-com, mylifeforce-com, niagenplus-com,
noom-com, nurx-com, onemedical-com, prohealth-com, remedymeds-com, rexmd-com, ro-co,
rugiet-com, sermorelin-com, struthealth-com, telolife-com, trtnation-com, truniagen-com,
tryshed-com, vitalityrx-com.

Excluded: functionhealth-com (`diagnostics/labs`, not a DTC brand).

## Missing / Stale Coverage

- **Telehealth is the only deep cohort.** Store census: 135 profiles, 54 `telehealth.md`,
  67 `offerings.md`. Non-telehealth verticals (watches, energy, SaaS, VC) are sparse, so
  this read is *within captured telehealth only* — a category's thinness here is
  **"few captured brands competing," never "thin market."** [coverage-caveat]
- All 53 DTC packs carried a parseable `offerings.md` with ≥1 roster row, so no brand
  silently dropped out of the breadth count (no enumeration-floor zeros).
- Oldest captures are ~20d (`telehealth.md`) / ~16d (`offerings.md`); recent enough that
  roster composition is unlikely to have shifted, but not real-time.

## Source Gaps

- **No normalized category tag per SKU exists in the store.** `anchor_category` is one
  value per brand (front door only); per-SKU category is *not* a stored field. The
  breadth table is a **query-time** count derived from molecule strings in roster cells,
  not a stored taxonomy. [denominator-reconciliation / tooling-ergonomics]
- **Whole-file keyword grep is unreliable here and was rejected.** A first pass grepping
  full `offerings.md` + `telehealth.md` bodies returned TRT 53/53 and labs 53/53 — clearly
  inflated by comparison prose, FAQ, and "we don't do X" mentions. The breadth table uses
  the tighter **roster-cell, buyable-row** match instead. Treat the breadth numbers as
  *directionally* solid (the GLP-1 lead and mental-health floor are robust to method); the
  mid-band ranks (peptides vs longevity vs TRT, all 27–30) are close enough that molecule-
  string choices could reorder them. [source-rigor]
- `multi/none` (10 brands) is a real anchor value, not a gap — but it means the front-door
  table *structurally undercounts* every category those 10 compete in; the breadth table
  is the corrective.

## External Completeness Check

Not run — `evidence_mode: store-only` and `approval_needed: no` forbid external
denominators this run. The read is explicitly scoped to captured telehealth and labels
every count a captured floor. **If category *completeness* were load-bearing** (e.g.
"is GLP-1 actually the most crowded *market*?"), an outside denominator would be required
and this run cannot supply it.

## Market Pattern

[Judgment, tied to the two State tables and C3:]

- **GLP-1 is the cohort's gravity well.** Most common front door (19/53) *and* near-
  universal bolt-on (41/53). The 22 brands that sell it without anchoring it show GLP-1
  functioning as the attach-everywhere line — the category a hormone/longevity/men's
  brand adds to monetize existing intake. [from front-door + breadth + spillover]
- **The "crowded middle" is one shared shelf, not distinct markets.** Peptides (30),
  longevity/NAD (30), TRT (27), ED (24), hair (23), women's HRT (22) cluster tightly —
  the same multi-line platforms (the 10 `multi/none` + the TRT/longevity anchors) stock
  most of these simultaneously. Crowdedness here is *breadth of the same players*, not
  many specialists per category. [from breadth table + multi/none anchor share]
- **Mental health is the genuine thin spot inside the cohort** (10 breadth, ~0 as a
  front door). [Judgment] Likely a capture-scope artifact as much as a market one — the
  store's telehealth cohort skews hormone/weight/longevity, so mental-health specialists
  may simply be under-captured. Flagged, not asserted. [coverage-caveat]

## What Would Change This Answer

- A normalized per-SKU category tag (or a committed molecule→category map) would replace
  the hand-built breadth count and let the mid-band ranks settle — the recurring
  denominator/query-ergonomics pressure (MRL-001/002), now seen a third time.
- Capturing telehealth brands outside the hormone/weight/longevity skew (mental-health,
  derm, pediatrics specialists) would test whether "mental health is thin" survives a
  broader cohort, or is a capture artifact.
- An external category denominator would convert "most crowded *in the store*" into "most
  crowded *market*" — out of scope for store-only Loop 1.
