# Proposal: offerings.md — pilot triage outcomes (2026-06-03)

> **What this is.** The change set from the six-run `offerings.md` pilot (Hone, AgelessRx, Eden, GoGeviti,
> Hims, MyDrHank), triaged before enabling the module across the telehealth cohort. Companion to the
> [design record](../../2026-06-03-offerings.md) and the six [retros](.). **Applied
> 2026-06-03** — §D (code fixes) + §A (contract) + §B (recipe) all landed; §C (prompt template) below is for
> reuse. Still open: re-seed the hims exemplar to 7 columns + the larger §1.1 enumeration-ladder enrichment.

## Verdict (one line)

**The module delivers — keep the core.** The roster answers the molecule-price-visibility query `profile.md`
couldn't, and the two load-bearing guards (page-attested molecule + grep-verifiable price) held on all six
outputs under *both* prompt regimes. What's left to change is mostly run-prompt and contract-clarity — not the
design. Most cross-run variance traced to the **prompt fork** (2 simple runs → 7-col; 4 involved runs → 9-col +
mandated deep blocks + an explicit visibility rule), not to the module.

## Decisions locked (your calls this session)

- **No `Form`/`Category` columns.** They're market/project-specific → keep the **7-column** roster; derive the
  Notion mapping at **promotion time**, never stored in the roster. `Form` duplicates `What`; `Category` is the
  cross-company canonical key the architecture refuses (OFFERINGS rule 4) and the deferred promotion step.
  **Re-seed `store/hims-com/offerings.md` to 7 columns** (it's the exemplar; currently 9-col, so it teaches the
  rejected shape). *(Eden, GoGeviti, MyDrHank also carry 9-col — fold to 7 on their next capture, no rush.)*
- **Visibility token = a stated judgment**, blessed as such (§A1).

---

## §A — Contract changes (`OFFERINGS.md`) — ✅ applied

### A1. Bless the visibility token as a stated judgment

**Why.** ≥4 runs converged that the per-SKU `published/partial/on-request` call is brand-shaped, and the same
pricing shape got *opposite* tokens (Hims `published` vs Hone `partial` for a "From $X" dose-floor) — even
prompt-2's explicit rule got under-applied. Forcing one mechanical rule is false precision; the durable fix is
to name it a judgment, require the *why* be recoverable, and push cross-brand consistency to query-time.

**Proposed edit** — replace the `Visibility` bullet under *## Roster* with:

> - **Visibility** — `published | partial | on-request` per SKU (`—` for family rows). The one closed set.
>   This is an **explicit, stated judgment, not a mechanism** — so **quote the *why* verbatim** in the Price
>   cell or a Verbatim anchor (the membership footnote, the "From $X" dose-floor, the med-bought-elsewhere
>   note), and **cross-brand consistency is a query-time concern, never forced at capture.** Default tree to
>   reduce drift: `partial` = the all-in isn't fully shown (a mandatory separate cost like a membership, the
>   med bought elsewhere, **or** a floor that moves materially with dose/tier); `published` = the shown number
>   is the full, self-contained price; `on-request` = no price shown (intake / quiz / consult / lab-gated). A
>   self-valuation ("valued at $X if bought separately") is **not** a price → `on-request`.

*Net: guidance + one default tree, no new vocab. Folds in the open contract notes from Hone #6 / Eden #4 /
GoGeviti #7 / Hims #6.*

### A2. Add `site_notes` to the frontmatter (the forward-learning loop)

**Why.** Pricing goes stale fast and SKUs come and go — so "what to re-check next run" is higher-value here than
on `profile.md`. The pilots surfaced exactly this durable playbook (where the catalog *actually* lives, where
prices hide, what's A/B-volatile) and it has nowhere to land today.

**Proposed edit** — add to the frontmatter block + a note:

> ```yaml
> site_notes: "Catalog lives in the JS bundle, not nav; prices PDP-only (budget ~1 scrape/SKU); prices A/B-flicker $64↔$65 — re-check next run."
> ```
> *`site_notes` is **carry-forward only** — the offerings-capture playbook the next run inherits: where the
> real catalog lives (CMS REST / app-subdomain / SPA bundle / nav+census), where prices hide, and what's
> volatile or worth a diff. One-time run narration (credits, runtime, "no contamination this run") stays in
> `## Provenance`, never here — mirrors `profile.md`'s `site_notes` discipline.*

*Net: one field, additive — a **MINOR** bump (`schema_version` `1.0` → `1.1`), grandfathered, no backfill, no
re-stamp. Absorbs would-be fields (volatility flag, "catalog lives at X", key-pages) so they never need their
own columns.*

**Rejected (kept out, on purpose):** `credits_used` / `run_time` in frontmatter — run telemetry, not queryable
State; credits already live in `## Provenance` + the `fc.py` manifest, runtime answers no per-company question.
A SKU `count` — derivable (count rows), so don't store it. A `roster_completeness` confidence field — already in
Provenance prose; defer until a consumer actually filters on it (no field without a query).

---

## §B — Recipe discipline (`firecrawl-capture.md` §1.1) — ✅ applied

Two capture rules that fix genuine output defects, added to the existing §1.1 "Capture rules" list so **any**
prompt inherits them (the defects were prompt-independent):

- **B1. Verify each rostered slug resolves before listing it.** Hims invented `/weight-loss/ozempic-pen` (the
  injection card links only to `/weight-loss/ozempic-pill`; the slug is in no capture) — a fabricated
  within-company key the lint can't see. Rule: *a slug must be an attested URL from a captured page, or noted
  `(no PDP — …)`; never constructed.*
- **B2. Don't assert a page is silent on a term without grepping it.** AgelessRx wrote "the page never says
  bremelanotide / sirolimus" — both are on the page. Rule: *`not stated` is fine; asserting absence ("never
  names X") requires actually searching for X first.* (Also sharpens the molecule rule with Eden #2: scope
  attestation to product copy — exclude citations, ISI, alt-text, SEO blocks.)

*Ready-to-fold-on-your-nod (validated, but a bigger §1.1 edit — separate from the two above):* the **enumeration
backbone** cluster (find *where the catalog lives* — CMS-REST with a JSON-not-SPA-shell guard · app-subdomain ·
custom-SPA bundle registry · else nav+census), the **price-on-PDP cost rule** (index has no prices → budget ≈ one
scrape/SKU), **blind-source agreement** for completeness (with the SPA "doubly-blind" caveat), and **capture both
divergent prices, reconcile nothing.** Confirmed across 4 runs; say the word and I'll draft the §1.1 edit.

---

## §C — Run-prompt template (tightened)

Your prompt-2 fought the contract in two places; the durable rules now live in §A/§B, so the prompt can shrink
and **defer to them**. Drop-in replacements:

- **Deep blocks — earned, not a quota.** Replace *"DEEP-DIVE 2–3 representative PDPs"* with: *"Write a deep
  block **only where one is earned** — a verbatim H1 / price footnote / disambiguation that resolves an
  ambiguity a roster row can't. **Zero is fine**; say so if none earned."* (The mandated 2–3 manufactured the
  padding blocks — Hims Sildenafil, Hone PDP-anatomy.)
- **Enumeration — defer to the recipe.** Replace the hard-coded *"cross-check `/wp-json`, `/products.json`"*
  with: *"enumerate per `firecrawl-capture.md` §1.1 — find where the catalog actually lives for this platform."*
  (The CMS probe is a dead end on a custom SPA; the recipe already branches.)
- Keep the rest of prompt-2 as-is (completeness ask, verbatim discipline, the visibility-rule statement — now
  backed by the contract).

---

## §D — Already landed (code fixes, verified)

1. **`fc.py` `do_map` slash bug** — `tag = map_{search}` put `/` and `:` from a `site:domain/path` term into the
   payload filename → write crashed *after* the credit billed (hit twice, ~11 cr leaked). Now slugified.
2. **`offeringscheck.py` price-grep brittleness** — the `\b` anchor rejected real prices the page glued to a
   letter (`$300Add-On`, `$101M`), which once pushed an author to hand-edit a capture to pass. Now `(?!\d)` —
   rejects a longer number, accepts a trailing letter. Verified: `$30`✗`$300`, `$300`✓`$300Add-On`, `$101`✓`$101M`.
3. **Reverted the GoGeviti capture edit** — `store/gogeviti-com/captures/2026-06-03/testing.md` restored to the
   authentic glued `$300Add-On` (matches the rawHtml `$300</span>`); the lint now passes *because* of fix #2,
   not because the source was altered.

*All six lints green; ruff clean.*

---

<sub>Sources — the six [retros](.), the six graded outputs, and this session's cold read +
verification. Supersedes nothing; extends the [design record](../../2026-06-03-offerings.md) with
the pilot's results. Authored 2026-06-03.</sub>
