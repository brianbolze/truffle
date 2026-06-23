# Consumption test — do the store formats actually answer queries?

*2026-05-31. Cold-consumer run: read only README/SCHEMA/TAXONOMIES, then ran a 5-query
battery by hand against the 11-company store (6 telehealth + linear, drinkag1, nike, aws,
benadryl) before building anything. Goal: an honest read on queryability + a concrete
rung-2 recommendation.*

UPDATE: A key caveat to this test is that it was run on the 11-company store that had captures done on an evolving / inconsistent schema. We've since
added a schema versioning mechanism, and backfilled those 11 companies to match the updated schema.

## TL;DR

- **The formats are queryable.** All 5 queries got complete, correct answers from the store
  alone. `profile.md` carries a point read entirely; frontmatter greps carry filter/group;
  profile **bodies** carry cross-brand pricing well enough to tabulate; cleaned `captures/*.md`
  preserve **verbatim** primary-source text.
- **The one thing that fought every query was drift, not structure.** The contract
  (SCHEMA/TAXONOMIES) has evolved — new fields and new enum values — but the 11 captures are
  frozen ~one generation behind it. A cold consumer who trusts the *current* contract greps the
  *wrong* (empty) fields and hits dead ends. This is the headline finding.
- **Rung-2 pick: a `QUERYING.md` recipe doc + a thin `facets` helper.** Measured: the helper
  beat the cold attempt on filter/group/relational; a term-digest helped *locate* cross-brand
  pricing but could not *normalize* it (the real Q3 blocker). Recipe doc is the cheapest, highest-leverage fix.
- **11 companies did not strain file-reading.** Grep-on-frontmatter + targeted body greps kept
  cost low. Rung-3 SQLite earns its place only once the schema fields it would index actually
  exist (relations, structured price) — building it on today's data would inherit empty columns.

---

## The dominant finding: contract ↔ corpus drift

The contract I read as a cold consumer is **ahead of** the data. Four concrete instances, all
discovered by querying:

| Contract says (current) | Corpus actually has | Consequence for a cold query |
|---|---|---|
| `portfolio_shape` (+ a whole tie-breaker section) | `is_multi_product:` boolean — **0/11 use `portfolio_shape`** | `grep '^portfolio_shape:'` → nothing. Looks like "no data." |
| `parent: []` / `owns: []` frontmatter | **0/11 use either** — links live in `#`-comments, `aliases`, and prose | Q5 (relational) un-greppable via the advertised fields. |
| `Usage-based / Consumption` is a `business_model` value | AWS = `business_model: Other` ("no closed value fits") | AWS mis-bucketed; value was added *after* its capture. |
| `Apparel & Footwear` is an `offering_category` value | Nike = `[Retail/E-Commerce, CPG]` ("there is NO Apparel value") | Nike mis-bucketed; value was added *after* its capture. |

The capture comments are honest and self-aware ("the SCHEMA still has no field…") — they were
**true when written**. Nothing is wrong with the captures; the contract simply moved. But for a
consumer, the net effect is the same as a bug: the advertised query path returns empty. **This is
a migration-debt problem, not a format problem** — and it is the single biggest lever on
queryability right now.

---

## Per-path scorecard

| Path | Query | Served? | Cost | Where it fought me |
|---|---|---|---|---|
| **Point read** | Brief me on hims | ✅ fully | 1 file (~115 ln) | nothing — ideal |
| **Filter / group** | B2C+Sub; group all 11 | ✅ fully | 2 greps, 0 full reads | drift: `portfolio_shape`/`parent` empty (dead-end greps) |
| **Aggregate** | GLP-1 table × prices | ⚠ partial | 1 grep (36KB) + 1 capture dig | prices in prose; units non-normalized; site_notes noise; per-offering gaps invisible |
| **Primary source** | verbatim FDA disclaimers | ✅ mostly | 1 capture grep | phrase-guessing (no anchor); md escaping; uneven capture coverage |
| **Relational** | parents / independents | ✅ (prose only) | 1 grep (~50 ln) | not structurally queryable; comment conventions inconsistent |

### Point read — *format serves it excellently*
`profile.md` is the unit of a point read, and its body sections map 1:1 to the ask (Overview →
what; What they offer → offerings; How it works → model; Positioning → positioning; + Strategic
read as a bonus "so what"). One file, complete, correct. **No affordance needed.** This is the
format at its best: the capturing agent's synthesis is exactly what a brief wants.

### Filter / group — *frontmatter is a real strength, modulo drift*
Closed-set values, one field per line, **with an inline `# strain comment` on the same line**, make
`grep '^field:'` return the value *and* its caveat in a single hit — e.g. AWS's `business_model:
Other  # STRAIN: usage-based…`. That co-location is genuinely good design for grep-consumers.
Answer (B2C+Subscription = 7: the 6 telehealth + AG1) fell out in two greps with zero full reads.
The **only** friction was drift: I burned two greps on the advertised-but-empty `portfolio_shape`
and `parent`/`owns` before falling back to `is_multi_product` and prose.
-> UPDATE: Already added a "schema_version" mechanism to the backlog. Ran a migration / back-fill on the 11 in the store. 

### Aggregate — *the hard path; answerable but not clean*
Good news: the capturer **front-loaded offering pricing into the `What they offer` body bullets**,
so the GLP-1 table is buildable from the 6 profiles without opening a single capture. Bad news, in
order of severity:
1. **Units are non-normalized prose.** Across 6 brands the GLP-1 price is quoted as `/mo`,
   `first-month`, `bundle-total`, `financed $/mo`, `From $X† anchor`, and `+ mandatory membership`
   — no two alike. You cannot build an apples-to-apples column without manual reconciliation, and
   you cannot query "GLP-1 under $200/mo" at all.
2. **Clean-price gaps are real and several:** hims (all `From $X†` anchors, true price quiz-walled,
   +$149/mo membership stacked), eden (branded Ozempic/Wegovy quiz-walled), petermd (GLP1 tier→dose
   mapping unclear), **healthspan (names Wegovy/Zepbound/compounded sema but prices none of them)**,
   **hone (no sema/tirz at all — weight-loss is orals + compounded liraglutide, "$60–$160")**. Only
   **telolife** gives a clean per-molecule monthly ($199 sema / $275 tirz).
3. **"Not offered" vs "not captured" is invisible.** Digging deeper *rescued* petermd (its
   `glp1_weight_loss.md` has $105/$134/$158.50 tiers) but hit a wall on healthspan and hone —
   because **neither has a weight-loss/GLP-1 capture page at all**. A consumer can't distinguish a
   product gap from a capture gap without reading `site_notes`/Provenance. Cross-company aggregation
   is what *exposed* this uneven capture coverage.
4. **Broad `$`-greps over profiles hit `site_notes` noise** (36KB for one grep) — capture-meta and
   queryable content share the file.

### Primary source — *format serves it; coverage is the risk*
Verbatim worked: cleaned `captures/*.md` preserve disclaimer text faithfully (bold markers intact),
so quoting is exact. The cross-brand contrast was the payoff and came straight out of the captures:
- **hims** — explicit, and uses *four slightly different wordings*: `"Compounded products are not
  approved nor evaluated for safety, effectiveness, or quality by the FDA. Rx required."` /
  `"…have not been approved nor evaluated…"` / `"The FDA does not verify the safety, effectiveness,
  or quality of compounded drugs…"` / `"Compounded drug products are not approved or evaluated…"`.
- **eden** — `"The FDA does not review or approve any compounded medications for safety or
  effectiveness."` + a 503(a) sourcing line; supplements get the dietary `"These statements have not
  been evaluated by the Food and Drug Administration…"`.
- **petermd** — *no compounded disclaimer; the opposite:* affirmative `"Semaglutide and Terzepatide
  are FDA approved peptides"`, `"FDA-approved and clinically proven"` on a **compounded** drug
  (matches its own flagged FDA-language-softening bellwether).
- **healthspan** — no compounded disclaimer; frames compounded as the *lesser* option behind
  `"FDA-approved, enteric-coated"` generics.
- **hone** — only a dietary-supplement-style NAD+ disclaimer; **no compounded-drug disclaimer in any
  captured page**.
- **telolife** — **no compounded disclaimer captured** (only positive `"FDA-registered pharmacies"`);
  likely on an un-scraped legal/footer page.

What fought me: there's **no anchor or field for "regulatory disclaimer,"** so completeness depends
on guessing phrase variants (`not approved` / `not evaluated` / `does not verify` / `not been
evaluated`); markdown escaping (`\*\*`, `\*`) slightly mangles verbatim fidelity; and **coverage is
hostage to which pages were captured** (telolife/hone gaps are capture-coverage gaps, not site gaps).

### Relational — *answerable only because the prose is diligent*
Every parent link exists **only** in prose + `#`-comments (the `parent`/`owns` fields are empty):
AWS→Amazon (subsidiary), Benadryl→Kenvue (brand-of), Hims→Hims & Hers Health Inc. (brand-of, sibling
Hers); Nike is itself a parent (owns Jordan/Converse/ACG/NikeSKIMS); the other 7 record no parent.
A wide-net prose grep got it — but it is **impossible to JOIN or aggregate** ("show all Kenvue
brands," "link aws→amazon"), and even the comment workaround **isn't standardized**: aws/benadryl
use `# parent: X · relationship: Y`, hims uses `# brand-of:`/`# sibling-brand:`, nike is prose-only.
(My prototype parsed `# parent:` and therefore caught AWS+Benadryl but **missed Hims and Nike** —
proof the comment convention can't be relied on.)

---

## Rung-2: the smallest affordance that helps most

I prototyped a store-aware [`digest.py`](digest.py) (stdlib, ~150 LOC, two modes) and measured it
against the cold attempt. Outputs saved in [`_out/`](_out/).

**`facets` mode** (frontmatter table across all 11, with drift fallbacks built in — reads
`is_multi_product` when `portfolio_shape` is absent, reads the `# parent:` comment when the field is
empty): **materially beat cold.** One ~20-line table replaced two greps + manual cross-referencing
for Q2, and gave the Q5 parent column for free (where the comment was parseable). This is the
sweet-spot helper — small, robust, and it *encodes the drift workarounds so the next consumer
doesn't rediscover them.*

**`term` mode** (cross-brand body slices + price-line flagging): **beat cold on *locating*, not on
*solving*.** It co-located all 7 GLP-1-mentioning brands in one read (vs my 36KB grep + capture dig)
and auto-counted coverage. But it **could not normalize prices** (the actual Q3 pain), pulled in
non-offer lines (it's line-grep, not section-aware), and its price-coverage metric is too coarse —
it counts healthspan as "priced" because *some* matched line has a `$`, missing that the *GLP-1* is
unpriced. Co-location is real value; normalization needs structured data, not a smarter grep.

**Recommendation, in priority order:**

1. **Write `QUERYING.md` (a recipe doc) — do this first, it's nearly free.** It converts cold
   fumbling into first-try success and needs zero maintenance. It should say, concretely:
   - *Point read* → `read store/<domain>/profile.md`.
   - *Filter/group* → `grep '^<field>:' store/*/profile.md`; the inline `#` comment is the strain note.
   - **Drift gotchas** (the whole game): shape is under `is_multi_product`, **not** `portfolio_shape`;
     `parent`/`owns` are empty — get relations from prose/`# parent:`/`aliases`; AWS is really
     Usage-based, Nike really Apparel — both backfillable.
     -> UPDATE: Already added a "schema_version" mechanism to the backlog. Ran a migration / back-fill on the 11 in the store. 
   - *Pricing* lives in the `What they offer` body bullets (+ `captures/*.md`), never frontmatter;
     units are non-normalized; check Provenance to tell "not offered" from "not captured."
   - *Disclaimers/verbatim* → `grep -i 'not approved\|not evaluated\|does not verify' store/<d>/captures/*/*.md`.
2. **Ship the thin `facets` helper** (this prototype, cleaned up) — earns its keep now for Q2/Q5-lite
   and scales painlessly.
3. **A term-digest is optional** — useful for Q3/Q4 triage, but don't oversell it; its ceiling is
   set by the prose/units problem below, which it can't fix.

---

## Did 11 strain plain file-reading? When does rung-3 (SQLite) earn its place?

**11 did not strain it.** No files were missed; cost stayed low because frontmatter is greppable and
bodies only needed targeted greps. The strain that *did* show up was not *count* but *mixing*: each
`profile.md` packs high-cardinality capture-meta (`site_notes`, Provenance) in the same file as
queryable content, so broad greps (e.g. `$[0-9]`) return noise (the 36KB hit). That gets worse
linearly, not catastrophically.

**Rung-3 SQLite earns its place when a query needs something markdown structurally can't express:**
- **Relational JOINs/aggregation** — "every brand Kenvue owns," "link subsidiaries to parents,"
  counts by parent. Prose can't do this at any N.
- **Numeric/range queries on price** — "GLP-1 plans under $200/mo," "cheapest TRT."
- **Scale ~30–50+ companies** where even cheap greps over noisy files add up.

But the order matters: **an index is only as good as the fields it indexes.** Built today it would
inherit empty `parent`/`owns` and prose-trapped prices — i.e. it would index the gaps. So the
sequence is: (1) recipe doc now → (2) backfill the drifted fields + write `offerings.md` with a
structured price → (3) *then* a SQLite lens becomes cheap and powerful. Don't skip to rung 3.

---

## SCHEMA gaps consumption exposed (logged, not fixed)

1. **Migration debt is the top gap.** `portfolio_shape`, `parent`/`owns`, `Usage-based / Consumption`,
   and `Apparel & Footwear` all exist in the contract but 0/11 captures use them. Either backfill the
   corpus or the contract is fiction to a cold consumer. *(Backfill is mechanical for the enum cases:
   AWS→`Usage-based / Consumption`, Nike→add `Apparel & Footwear`, all 11 `is_multi_product`→`portfolio_shape`.)*
   -> UPDATE: Already added a "schema_version" mechanism to the backlog. Ran a migration / back-fill on the 11 in the store. 
2. **No usable relations field.** `parent`/`owns` are defined but unused, and the prose/comment
   workaround has ≥3 incompatible conventions. Q5 needs a *populated, consistent* relational field
   (or it stays prose-only forever). This is the most-cited gap across the corpus's own comments
   (AWS, Benadryl, Hims, Nike all flag it).
   -> UPDATE: That field was added to the SCHEMA later. Should now be populated via the backfill.
3. **No structured price → aggregation can't normalize.** Pricing lives in body prose with
   per-brand units. `offerings.md` was specced but **never written for any company**; a per-offering
   `price` (with a unit) is the fix for Q3. Until then, cross-brand price tables are manual.
4. **No `regulatory_disclaimer` anchor.** Q4 works only by phrase-guessing across capture bodies;
   a key_pages-style pointer or a captured `disclaimer:` quote would make it first-try.
5. **Capture coverage is invisible to consumers.** "Not offered" vs "not captured" is only
   resolvable by reading `site_notes`/Provenance. A machine-readable `captured_pages` /
   `not_captured` list (key_pages half-does this) would let a consumer trust a negative result.

---

## Artifacts
- [`digest.py`](digest.py) — store-aware rung-2 prototype (`facets` + `term` modes).
- [`_out/facets.md`](_out/facets.md), [`_out/glp1-digest.md`](_out/glp1-digest.md) — measured outputs.
- Battery answers were delivered in-session; this doc is the meta-analysis, per the brief.
