# FINDINGS — consumption-mechanics probe (2026-06-09)

Store state at probe time: 105 `store/` folders, **90** `profile.md`, **49** `telehealth.md`,
**55** `offerings.md`; `scripts/_out/store.db` built Jun 6.

## Per-question log

### Q1 — "Tell me about Henry Meds — how fresh?" (Recipe 1, point read)
- **Steps:** 2 (`store.py find "Henry Meds"` → read `store/henrymeds-com/profile.md`).
- **Worked as written:** yes. Resolver folded the name; `captured_at: 2026-06-04` (5 days old) answers freshness.
- **Trap:** none. Freshness nuance: `offerings.md`/`telehealth.md` carry their own `captured_at` — a reader answering "how fresh" from `profile.md` alone may overstate roster freshness.
- **One-step affordance:** `store.py find` could print `captured_at` next to the slug — resolve + freshness in one call.

### Q2 — women-only / women-first telehealth brands (Recipe 6, cohort cut)
- **Steps:** 2 (grep TELEHEALTH.md for the `audience` closed set → 5-line PyYAML scan of `store/*/telehealth.md`).
- **Worked as written:** yes. Answer: women-only = brellohealth, innerbalance, nurx; women-first = effecty, remedymeds.
- **Trap (stale doc claim):** QUERYING.md Recipe 6 says "the telehealth set is 13/13 identical" — the cohort is **49**. Harmless here, but a cold agent calibrating effort off that number is misled.
- **One-step affordance:** a `store.py cohort telehealth --cut audience` one-liner; the PyYAML snippet is fine but re-typed every session.

### Q3 — semaglutide pricing across brands (Recipe 4, the ceiling)
- **Steps:** 3 (count pass → OFFERINGS.md contract skim → `rg -n 'semaglutide' store/*/offerings.md` filtered to table rows).
- **Worked as written:** yes — one grep enumerated ~70 SKU rows across **39 brands** with verbatim `Price` + `Visibility` cells.
- **The ceiling, exactly:** enumeration + verbatim quotation is achievable; the stop line is **producing any sorted/averaged $-per-month comparison**. The same grep returns `$199/mo` all-in, `$399/3-months` bundles, `From $149/mo†` med-only-excluding-membership, `$1300/mo on average` brand-name pass-through, first-month promos, and "market ref" prices that aren't the brand's own. There is deliberately no `price_num` — hand-normalization per unit is where the recipe ends, and we stopped there.
- **Trap (footgun, dodged):** raw `rg -c` hits `site_notes` and prose, not just roster rows — naive counting overstates SKUs; filter to `| `-prefixed table rows. And never rank brands on row counts without `enumeration` — **Hims' offerings.md is schema 1.1, predating the field** → its count is no-claim.
- **One-step affordance:** the `offerings` table in store.db does exactly this (`what LIKE '%semaglutide%'`) — *if* the db were trustworthy-fresh (see side-check).

### Q4 — parent of Delighted + siblings (Recipe 3, relations)
- **Steps:** 2 (read delighted frontmatter → `store.py relations` + qualtrics frontmatter, batched).
- **Worked as written:** yes. `parent: [qualtrics.com]` → joinable to held `qualtrics-com` profile. Qualtrics `owns: ['Press Ganey Forsta']` (name-only, un-joinable by design).
- **Trap (real, non-obvious):** relations are **not reciprocal** — Qualtrics' `owns` does *not* list delighted.com. "What else does the parent own" requires the reverse join over `parent` edges (which `store.py relations` does); reading the parent's `owns` field alone silently misses Delighted itself.
- **Stale doc claim:** QUERYING.md says "today it's 1 joinable / 23 dangling / 8 name-only"; actual: **3 / 31 / 8**.
- **One-step affordance:** `store.py relations <slug>` — a per-company view (parents, children via reverse join, dangling) instead of the full-corpus dump.

### Q5 — does Hims offer ketamine? (negative-trust rules)
- **Steps:** 3 (`rg -i ketamine store/hims-com/` = 0 hits → frontmatter signals → Provenance + mental-health line check).
- **Worked as written:** yes — and the rules earned their keep. Verdict: **strong "not offered"**, not just "not captured": the mental-health line *was* captured at SKU grain (sertraline/escitalopram) and the roster's family row states **"No controlled substances"** — a positive attestation, not silence. Caveats: profile 2026-05-30 / offerings 2026-06-03; Hims offerings.md predates `enumeration`, so scope is contract-unstated — the explicit attestation is what upgrades the negative.
- **Trap:** skipping the rules gives the same answer with false confidence; over-applying them could refuse to answer despite the attestation. The rules give signals, not a verdict procedure.
- **One-step affordance:** a `store.py negative <slug> <term>` that prints the three signals would mechanize the checklist.

### Q6 — corpus-wide B2B SaaS (generalization test)
- **Steps:** 2 (TAXONOMIES.md value check — `Software / SaaS`, not `SaaS` → membership filter on `target_market` + `offering_category`).
- **Worked as written:** yes, generalizes cleanly beyond telehealth. **23** companies sell B2B software; **19** are *primarily* B2B (position-1 rule drops apple, doordash, granola, openai).
- **Trap (dodged because the doc warns):** hardcoding `SaaS` or testing list equality silently fragments. Primary-vs-membership is the question's real ambiguity — the recipe makes it expressible; the asker still picks.
- **One-step affordance:** `store.py filter target_market=B2B offering_category="Software / SaaS"`.

### Q7 — stalest 5 + stubs (health visibility)
- **Steps:** 1 (one python pass: sort `captured_at`, diff folder set vs profile set).
- **Worked:** the *primitives* work; **no recipe exists** — this is the gap. Stalest: blueowl, eden-health, hims, nike (all 2026-05-30; tie), agelessrx (2026-05-31).
- **Finding (the headline):** **15 of 105 folders are stubs** — `captures/` only, no `profile.md` (anazaohealth, belmarpharmasolutions, ddpmedical, dewittpharma, exaveyra, goinfusive, hellopepti, jinfiniti, kingsbergmedical, mdpep, medsupplysolutions, millspharmacy, norexi, pfizerpro, stemnovanetwork). Every documented recipe globs `store/*/profile.md`, so stubs are **invisible to all of them** — paid-for captures no consumer can find, and "is X in our research?" answers "no" for 15 companies we partially captured.
- **One-step affordance:** `store.py health` — stub list, staleness ranking, per-layer `captured_at` skew, db freshness.

### Q8 — "is brello in our research?" (alias resolution)
- **Steps:** 2 (`store.py find brello` → read `store/brellohealth-com/profile.md`).
- **Worked as written:** yes — exactly the resolver's case ("brello" → `brellohealth-com`). Women-only DTC telehealth: compounded GLP-1 (semaglutide/tirzepatide + B6), NAD+, sermorelin; buy-first cash-pay quarterly plans; 503A partner pharmacy; captured 2026-06-04.
- **Trap:** none here. **But** Q7 shows the resolver's blind-spot class: a stub company resolves to nothing and reads as "not in our research" when captures exist.

## Side-check — store.db staleness

**Stale, and nothing tells you.** db mtime Jun 6 13:45; markdown newer in 5+ companies (rugiet
profile/telehealth/offerings; prohealth; jinfiniti/hellopepti/goinfusive captures, Jun 7–9). Row
counts confirm: `companies` 88 vs 90 profiles; `telehealth_full` 47 vs 49 packs; rugiet absent from
`companies`, prohealth absent from `telehealth_full`. No `built_at`/meta table, no staleness banner
on query; `--check` validates schema drift, not freshness. QUERYING.md *says* "stale the moment a
capture lands — rebuild," but a consumer reaching for the lens mid-session gets confidently stale
rows with zero signal. Q3 done via the db would have silently dropped rugiet's semaglutide SKUs.

## Cross-cutting findings

**Wrong/stale doc claims in QUERYING.md** (all in the "live numbers" class — the recipes themselves were all correct):
1. "telehealth set is 13/13 identical" → cohort is 49.
2. "1 joinable / 23 dangling / 8 name-only" → 3 / 31 / 8.
3. Footer: "Written against `schema_version: 1`" → corpus is at 2.5.
Pattern: **baked counts rot** — the doc's own anti-reconciliation principle, violated by its own prose. Name mechanics, never live numbers (or mark numbers as-of).

**Missing affordances, ranked by friction:**
1. **Store health is invisible** (Q7) — 15 stub folders no documented query path can see; no staleness/skew view. Highest because it silently corrupts *other* answers ("is X researched?" → false negative).
2. **store.db has no freshness signal** — the only rung-3 surface can be confidently wrong; a `meta(built_at, source_count)` table + a one-line mtime check in QUERYING.md would fence it.
3. **Stale numbers in QUERYING.md** — misleads a cold agent's mental model (cohort size off 3.7×).
4. **No memoized filter/cohort one-liners** — every session re-types the same 5-line PyYAML scan; `store.py filter/cohort` would make Q2/Q6 one call each.
5. **Per-company relations view** — corpus-dump-only; the per-company question needs the reverse-join done for you or you miss children.
6. **Resolver surfaces no freshness or stub-ness** — `find` returns a bare slug; can't say "captures exist but no profile."

**Ranked friction (overall):** (1) stub invisibility · (2) silent db staleness · (3) stale doc
numbers · (4) re-typed filter/cohort boilerplate · (5) corpus-only relations view · (6) `rg -c`
over offerings counts prose, not rows (minor) · (7) per-layer freshness skew (minor).

**What worked unambiguously:** `store.py find` (name + alias, zero-shot), the PyYAML snippet
(copy-paste correct), the offerings molecule grep, the negative-trust signal triad, and closed-set
discipline (TAXONOMIES exact strings prevented silent fragmentation in Q6). Probe cost: ~14 tool
calls for 8 questions + side-check, $0, no Firecrawl.
