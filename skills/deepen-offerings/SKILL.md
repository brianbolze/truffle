---
name: deepen-offerings
description: >
  Re-capture one company to make its offerings.md roster comprehensive — drive it to "complete at the
  indexed level" across ALL product lines, pulling in any line or subdomain a prior run left out of
  scope. Use when a roster looks incomplete: "deepen offerings for X", "enumerate more of X's catalog",
  "/deepen-offerings henrymeds", "make X's offerings comprehensive", "X's roster is missing SKUs". Takes
  any company form (slug / domain / name). A focused preset of research-company; it spends Firecrawl.
---

# /deepen-offerings — make a company's offerings roster comprehensive

A focused preset of [`/research-company`](../research-company/SKILL.md): re-capture a company with one goal —
drive its `offerings.md` to **complete at the indexed level across every product line**. It fixes a roster that
stopped early and now *reads* as a small catalog, so any count under-reports it. **Follow research-company's
`SKILL.md` + `firecrawl-capture.md` for all capture mechanics** (offerings ladder = §1.1; contract =
`OFFERINGS.md`) — this skill only presets the focus and the gap-targeting below. **One override:** pass
`--verb deepen-offerings` (not `research-company`) on every `fc.py map`/`scrape` call, so `runcost.py`
attributes this preset's credit cost to its own routine.

## Steps

1. **Resolve → slug.** `python "$WEB_RESEARCH_HOME/scripts/store.py" find "$ARGUMENTS"` folds any form (domain /
   name / alias / slug) to the key. **NOT in store** → nothing to deepen; run `/research-company "$ARGUMENTS"`
   for a first capture instead, then stop.

   When there is something to deepen, stamp the run clock after slug resolution:
   ```bash
   RUN_STARTED_AT="$(python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" now)"
   ```

2. **Find the gaps.** First read the frontmatter **`enumeration`** flag — it's the explicit TODO: **`lines-omitted`**
   (a whole line was skipped — the `## Provenance` scope note names it) or **`unknown`/absent** (scope unverified) is
   the work; **`indexed-complete` is already comprehensive → decline with reason** (nothing to deepen). Then read
   `## Provenance` + `site_notes` and chase only the **breadth** gaps: whole product lines, an off-host / sibling
   **subdomain** (a `shop.` storefront), categories priced but not rostered, anything "out of scope" last run.
   **Leave the by-design leaf omissions** (dose / quantity tiers, per-SKU PDP price depth, `Catalog` leaves) —
   chasing those just burns credits. No `enumeration` flag *and* no scope note (a pre-1.2 file) → treat the whole
   roster as unverified and re-enumerate off the index pages.

3. **Re-capture for breadth.** Force a refresh (the warm-capture skip never applies here); drive `offerings.md` to complete
   at the indexed level across all lines + the step-2 gaps. Refresh the `## Provenance` scope note, and **set the
   frontmatter `enumeration`** to the achieved state — `indexed-complete` if every line was reached, or
   `lines-omitted` (naming the residual line in the scope note) if one was found but still deferred — bumping
   `schema_version` to `"1.2"` if the file predates it. That one token is what graduates a count from "floor" to
   trustworthy-as-breadth (contract: [`OFFERINGS.md`](../../modules/OFFERINGS.md) → `enumeration`).

4. **Record the run (required — the run is not done until this is written).** After `offeringscheck.py` passes, write a run record:
   ```bash
   python3 "$WEB_RESEARCH_HOME/scripts/runrecord.py" write \
     --slug <slug> \
     --verb deepen-offerings \
     --started-at "$RUN_STARTED_AT" \
     --artifact offerings.md
   ```
   Tool is env-detected for **both Claude Code and Codex** — no `--tool` needed. Pass `--model <id>` if you know it — the model you were told at session start; else it falls back to `unknown`. Add `--status partial` if the run fell short. Omit the record only if the preset declined before doing any work.

**Scope:** offerings only (a full refresh or first capture is `/research-company`); it spends Firecrawl, so
research-company's credit pre-flight applies.
