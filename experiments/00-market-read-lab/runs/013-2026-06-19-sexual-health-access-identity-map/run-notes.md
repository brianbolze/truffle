# Run Notes

```yaml
run_status:            reviewed
evidence_mode:         store-only
autonomous_eligible:   yes
termination_reason:    completed
pressure_lenses_fired: [denominator-reconciliation, coverage-caveat, query-time-grouping-enough]
```

> **Loop 2 outcome (2026-06-19):** Reviewed via a 3-pass adversarial workflow (evidence verifier +
> consumer + developer, Sonnet). **Verifier:** all 30 scored structural cells across 6 brands
> verbatim-correct; both cohort greps independently confirmed (3 anchored / 24 ED-selling — the
> `\bED\b` token is load-bearing for 24). Both Judgments (access↔anchor correlation; men's-ED
> premium-clinical white space) defensible on the 6-brand sample and correctly labeled. **One real
> catch:** the cohort's `ED-tier` labels (origin/companion) were drawn from *body* prose, not the
> `anchor_category` `#` comment, so the read's "all cells verbatim frontmatter" claim was overstated
> for that one column — **fixed in `read.md`** (split into a separate `ED-tier` column explicitly
> labeled a hand-drawn Judgment). Store-only discipline **PASS** (no spend, no live browse, no
> mutation; `unclear` reported as captured value, not absence). **Consumer verdict: valuable**
> (structural access cut is invisible from public surfaces; better than Claude+web). **Developer
> verdict: valuable** — first run carried entirely by *discrete enum* State fields; the new
> **fill-rate-ceiling** sub-caveat is genuinely distinct from the "quote, don't re-derive" guard.
> Triage: appended Evidence Logs to **MRL-001** (3rd-cohort anchored-only under-count) and
> **MRL-002** (4th State-read surface + fill-rate sub-caveat). No graduation; no new item.

## 30-second operator read

- **Did the run work?** Yes. First lab run on the **sexual-health/ED cohort** (breaks 3
  straight GLP-1 runs) and the first whose answer rests on the **structural** frontmatter
  cuts (`pay_model`/`modality`/`compounding_posture`/`access_model`) rather than the
  well-worn pricing/positioning cuts. Store-only, zero spend. The structural fields carried
  the read for 5 of 6 brands.
- **What was awkward?** Two things. (1) `pay_model` is **`unclear` for 2 of 6** brands
  (bluechew, keeps) — a structural field at ~67% fill can't carry a confident cohort-wide
  access claim. (2) The cohort boundary had to be **hand-drawn into 3 tiers** — the
  `anchor_category: sexual-health` grep returns only 3, but the ED-*selling* store set is 24.
- **What should the next agent know?** The structural-cut read is reusable and cheap, but its
  confidence is gated by field fill-rate, not by reasoning. The "access_model tracks anchor
  position" pattern (ED-anchored→all-in; ED-companion→à-la-carte) is a 6-brand correlation
  labeled Judgment, not a law. A bounded-live follow-up on ED trust/objections (Scout
  candidate 4) is the obvious next read and would push the bounded-live clock to 3/3.

## What happened

Resolved the cohort from the store (grep `anchor_category: sexual-health` → 3 anchored;
ED-term grep → 24 ED-sellers; added hims/keeps/ro as ED-franchise-anchored-elsewhere → 6
ED-identity brands). Read the 6 brands' `telehealth.md` frontmatter verbatim across
`pay_model`/`modality`/`compounding_posture`/`access_model`/`audience`/`anchor_category`,
built the access matrix, and labeled the access↔anchor correlation and the white-space call
as Judgments. Wrote `read.md` + one derivation receipt. No external sources, no spend, no
`store/` mutation.

## Inputs and scope

- **Store slices:** `store/{rugiet-com,rexmd-com,bluechew-com,hims-com,keeps-com,ro-co}/telehealth.md`
  frontmatter (scored). Cohort-derivation greps over all `store/*/telehealth.md`.
- **Queries:** `grep -rl "anchor_category: sexual-health"` (3); ED-term grep (24).
- **Exclusions:** the 18-brand straddler tail (sells ED, no ED identity) named but not scored.
- **No** external sources, SERPs, reviews, or Firecrawl.

## Live evidence plan

Required only for `bounded-live`; leave `null` for `store-only` and `local-existing`.

```yaml
live_evidence_plan: null
# For bounded-live, paste the selected Scout plan here.
```

## Live evidence used

Required for every outside source used in `bounded-live`. Leave `[]` for local-only runs.

```yaml
live_evidence_used: []
# For bounded-live entries:
# - source_or_query:
#   source_family:
#   action_taken: searched | opened | captured | scraped | read-local-signal
#   reason:
#   source_grade: primary | secondary | direction-finding
#   captured_at:
#   spend_note: none | free | paid-credit
#   claim_ids_supported: []
```

## Friction log

- The cohort boundary was the only real labor: `anchor_category: sexual-health` (3) vs the
  ED-selling set (24) forced a hand-drawn 3-tier split (anchored / ED-franchise / straddler).
  Same friction MRL-001 names; recurs on a new cohort. The State-read itself (latest-capture →
  frontmatter field-extract → group/label) was mechanical and fast — same recipe family as
  runs 008/009/010, but on the *structural* fields, which are discrete enum cells (cleaner to
  quote than run 010's prose `site_notes`).

## Evidence limits

- `pay_model: unclear` for 2 of 6 (bluechew, keeps) — the access claim is confident for 4 of 6
  only. Structural field, ~67% fill.
- Captures 06-04 → 06-18; structural cuts are the durable part, but front doors are A/B-volatile
  (a hero rotation could re-sort the anchored-vs-companion split the read leans on).
- The access↔anchor correlation and white-space call are Judgments over a 6-brand sample, not
  laws. The ED-franchise tier (hims/keeps/ro) is itself a hand-drawn boundary.

## Loop 1 exit check

Record `pass` / `fail` for the mandatory exit check before setting final `run_status`.

- Status was `scout-only` before Loop 1: **pass**
- `Selected Run Contract` was present and consistent with header: **pass**
- `autonomous_eligible: yes`: **pass**
- `evidence_mode` was `store-only`, `local-existing`, or planned `bounded-live`: **pass** (store-only)
- `approval_needed: no`: **pass**
- If `bounded-live`, `live_evidence_plan` was present and followed: **n/a** (store-only)
- If `bounded-live`, every outside source was logged in `live_evidence_used`: **n/a**
- If `bounded-live`, stop rules and spend notes were recorded: **n/a**
- No disallowed action happened: **pass** (no live browsing, no spend, no `store/` mutation)
- Required citations / receipts present and source-graded: **pass** (derivation receipt, `source_grade: derived`/store-primary)
- No snippet treated as evidence: **pass** (all evidence is verbatim store frontmatter)
- Current/news/pricing/policy claims carry capture dates and source grade: **pass** (per-row `captured_at`; no current/external claims made)
- Absence language says "not found", not "not true": **pass** (`pay_model: unclear` reported as captured value, not inferred)

## Surprises

- The clean correlation between `access_model` and anchor position — all three ED-*anchored*
  brands are `all-in` (no membership wedge), all three ED-*companion* brands are
  `à-la-carte/both` with the membership wedge on their *growth* category, not on ED. Not
  something the question anticipated; surfaced only once the structural cells were lined up.
- ro is the cohort's lone `bills insurance` + `all-genders` brand — the structural fields
  isolate it as the "clinical/serious" outlier exactly the way they isolated One Medical in
  the GLP-1 cohort (run notes prior). The structural cut is good at finding the odd-one-out.

## Pressure tags

Short `kebab-case` tags for system pressure this run exposed. These are recurrence handles, not a fixed taxonomy and not permission to build.

Use an existing tag when it fits; coin a narrow tag only when the guide misses the thing.

| Tag | Use when |
|---|---|
| `denominator-reconciliation` | The answer depends on defining / cleaning / reconciling the company or source **set**. |
| `source-rigor` | Source grade blocks confidence: snippets, weak secondary sources, missing URLs, or missing capture dates. |
| `source-panel` | A repeated external source **set** seems needed to answer this kind of question. |
| `coverage-caveat` | Store coverage, stale captures, or incomplete modules materially limit the answer. |
| `depth-backfill` | A specific field/module is missing across otherwise relevant companies. |
| `query-time-grouping-enough` | The read was answerable by grouping existing store evidence; no durable category object is needed. |
| `freshness-monitoring` | Current pricing, news, policy, regulation, or launch motion could change or materially improve the answer. |
| `relation-pressure` | Competitors, named parents, suppliers, partners, or other counterparties seem repeatedly useful. |
| `tooling-ergonomics` | Repeated manual steps suggest a helper, query recipe, or template tweak. |

Which tags fired, if any? Did this run need a new or clearer tag?

"No new primitive needed" is a valid outcome.

| Fired tag | What fired in this run | Triage implication |
|---|---|---|
| `denominator-reconciliation` | `anchor_category: sexual-health` (3) under-counts the ED-selling store set (24); cohort hand-drawn into 3 tiers. | Append Evidence Log to **MRL-001** — anchored-vs-all-offerers under-count recurs on a 3rd cohort (after GLP-1 in run 012). |
| `coverage-caveat` | `pay_model: unclear` for 2 of 6 cohort brands caps the access claim at 4/6. | Append Evidence Log to **MRL-001/MRL-002** as a structural-field fill-rate caveat; not yet a depth-backfill triage item (only 2 brands, 1 field). Watch for recurrence. |
| `query-time-grouping-enough` | The whole read was grep + group + label over existing frontmatter; no durable cohort/category object needed or wanted. | no-op — reinforces the "no new primitive" posture. |

New tag needed? No. Existing tags covered it.

## Triage submissions

No new triage item proposed. Two **Evidence Log** appends for Loop 2 to consider (additive,
not graduation):

1. **MRL-001 (denominator reconciliation):** 3rd-cohort recurrence of the anchored-only
   under-count — `anchor_category: sexual-health` returns 3, the ED-selling set is 24. Same
   pattern run 012 named for GLP-1 (LifeMD/Nurx/Wisp fall out of the GLP-1 grep). Now on
   sexual-health. Strengthens the "name both the external inclusion rule AND the internal
   anchored-vs-all-offerers cut" recommendation.
2. **MRL-002 (State-read query recipes):** the State-read recipe family extends to a **fourth
   surface** — the *structural* access cut (`pay_model`/`modality`/`compounding_posture`/
   `access_model`), after price-posture (008), positioning (009), and offer-structure (010).
   New flavor: these are **discrete enum cells**, cleaner to quote verbatim than run 010's
   prose `site_notes`, so the MRL-009/010 "quote, don't re-derive" guard is trivially satisfied
   — but a new sub-caveat appears: a structural read's confidence is gated by **field fill-rate**
   (here `pay_model` at ~67%), not by reasoning. Still recipe-level; no helper or stored taxonomy.

**Do not implement, spike, or recommend immediate graduation from inside the run.**

## Next-run advice

- The obvious next read is **Scout candidate 4** — ED trust/objection mining (bounded-live),
  which would be MRL-010's 4th sighting and push the bounded-live review clock to 3/3 (triggers
  its review). Run it deliberately, not by accident.
- If anyone wants to harden the access read, capture bluechew + keeps `pay_model` (closes the
  2/6 hole).
- Avoid scoring the 18-brand straddler tail unless the question explicitly wants the ED-*selling*
  set rather than the ED-*identity* set — they'd dilute the identity read.
