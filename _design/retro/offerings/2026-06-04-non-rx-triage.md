# Proposal: offerings.md — non-Rx cross-shape triage (2026-06-04)

> **What this is.** The change set from running `offerings.md` on **7 deliberately-different shapes** — Clerky
> (legal docs), Warby Parker (eyewear catalog), Stripe (metered rate-card), Ford (vehicle catalog), Airbnb
> (two-sided marketplace), Notion (tiered SaaS), and **IDEO's decline** (bespoke services) — each graded
> *independently* (blind → verify lint/prices/slugs → diff the self-retro), then triaged. Companion to the
> [telehealth pilot triage](telehealth/2026-06-03-offerings-pilot-triage.md), whose decisions stay **LOCKED**.
> **Propose-only** — nothing here is applied to the contract / recipe / lint this run.

## Verdict (one line)

**The module flexed across all 7 shapes — it cracked in exactly one place, and that one place recurs everywhere.** Six wildly different shapes all came out **lint-clean, every sampled price grep-verbatim, zero fabricated molecules**, and the seventh (IDEO) **correctly declined**. The single crack: the spine has **no honest price token for a leaf whose price lives at a parent bundle** — 5 of 6 runs hit it and each invented a *different* workaround. Everything else is a one-paragraph clause or a one-line lint widening. **No redesign — the core holds.**

## The change set (sorted by impact)

| # | Finding | Home | Severity · Runs |
|---|---|---|---|
| **A1** | <span color="orange">change</span> — Bundled-price has no token; 5 runs improvised 5 of them | `OFFERINGS.md` | queryability · **5** |
| **A2** | <span color="orange">change</span> — Catalog/marketplace under-specified (+ a shipped self-contradiction) | `OFFERINGS.md` | queryability · **3** |
| **B1** | <span color="orange">change</span> — Lint price-grep is **`$`-only** → %/¢ rides unverified; also rejects footnote-glued `$` | `offeringscheck.py` | **fidelity-guard** · 1+1 |
| **C1** | <span color="orange">change</span> — No "services floor"; decline-with-reason isn't blessed | `OFFERINGS.md` + step 2.5 | queryability · 1 *(class)* |
| **A3** | <span color="orange">change</span> — Visibility silent on a maker-floor priced by a third party | `OFFERINGS.md` | queryability · 1 |
| **A4** | <span color="orange">change</span> — Header reworded off the canonical spine label *(most droppable)* | `OFFERINGS.md` | polish · 1 |

A1 leads on frequency (the headline). **B1 is the only finding that touches the integrity guard** — severity-purists, read it first. A4 is one line; drop it to hold the line count if you like.

---

## §A — Contract (`OFFERINGS.md`)

<details>
<summary><b>A1 — Bless one bundled-price token. Five runs invented five workarounds for the same gap.</b> <span color="orange">change · queryability · 5 runs</span></summary>

**Why.** The Price column is *verbatim-or-`—`*, and `—` means "family umbrella." But a **bundle-included leaf is neither** — it has a real price, just one *inherited from a parent* package/plan. Five of six runs hit this and each improvised a **different** token. Nothing is mis-stated (every workaround greps and is honest) — so it's queryability, not fidelity: a cross-company price digest can't read inherited prices uniformly because each file minted its own convention. **n=5 independent convergence on the same missing affordance is the strongest signal in the cohort** — this is the one gap that earns a contract change.

| Run | What it improvised |
|---|---|
| Clerky | `incl. in $427 / $819` |
| Notion | `incl. (Business $20)` (~12 rows) |
| Stripe | `Included with Payments` → `published` |
| Warby | `(priced at checkout)` → `on-request` |
| Airbnb | `—` + an improvised status |

**Proposed edit** — add under the `## Roster` Price bullet:

> **Bundled / included-in-parent price.** A buyable leaf whose price is *inherited from a named parent* package/plan (not a family umbrella) takes the token **`incl. (<parent> $X)`** — carry the parent's **verbatim** price inside (e.g. `incl. (Business $20)`), so the leaf still satisfies the grep-verifiable-price rule. Its **Visibility is `published`** when the parent's all-in is the shown, self-contained price; `partial` only if a *further* mandatory cost sits on top. Reserve `—` for true family-umbrella rows. A parent package row *is* the price card when the verbatim anchors live there (Clerky's two one-time packages).

**Simplification.** One paragraph **retires five ad-hoc conventions**. Do **not** also adopt Clerky's softer retro sub-clause ("Kind/Visibility advisory for non-storefronts") — it loosens two lint-backing concepts for no proven need (see Rejected).

**Evidence.** Clerky `homepage.md:407/417` (`$427`/`$819` verbatim); Notion `incl. (Business $20)` across ~12 rows; Stripe `Included with Payments`; Warby `/eyeglasses/progressives` row; Airbnb free/bundled leaves. Three of seven graders routed this same fix to `OFFERINGS.md` unprompted.
</details>

<details>
<summary><b>A2 — One Catalog/marketplace clause — which also fixes a contradiction already sitting in the contract.</b> <span color="orange">change · queryability · 3 runs</span></summary>

**Why.** The contract **self-contradicts** on roster completeness: the `## Roster` line says *"complete at the indexed level… never every leaf,"* while `## Capture & depth` says *"`Catalog` → shape + exemplars only, never the SKUs."* For a Catalog company these read as opposite instructions and the doc never reconciles them — **both the Warby and Airbnb graders flagged it independently.** Compounding silences for the un-enumerable-leaf shape: `Slug`-as-within-company-key is near-meaningless when most rows are `(no PDP — …)` and the real stable key (Airbnb's service-tag id) is buried in the string; and the `*(exemplar)*` row-marker Warby improvised is unblessed.

**Proposed edit** — reword the `## Roster` "complete at the indexed level" line to point at one new clause:

> **Catalog / marketplace shape.** For a `Catalog` or marketplace (host/seller-priced), *complete at the indexed level* means **line + pricing-tier + marked flagship exemplars — never the leaf SKUs** (this is exactly what *"shape + exemplars only"* in `## Capture & depth` means; the two are one rule). Mark a representative row **`*(exemplar)*`**. Where a leaf has no canonical URL, its within-company key may be a stable non-URL id, written **`(no PDP — <tag/partner-id>)`** (Airbnb's `Tag:89xx`).

**Simplification.** One paragraph + a four-word edit kills the contradiction **and** blesses both the `*(exemplar)*` marker and the non-URL key. Do **not** mint new `Kind`/`Visibility` enum values, and do **not** add a Status/availability column (see Rejected — hold at n=1).

**Evidence.** `OFFERINGS.md` "complete at the indexed level" vs "Catalog → shape + exemplars only, never the SKUs" — both lines verified present. Airbnb keyed 9 service tag IDs (`Tag:8949…8943`) all matching `services.md`; Warby tagged Durand/Percey/Boaz `*(exemplar)*`.
</details>

<details>
<summary><b>A3 — One sentence: a maker-floor priced by a third party stays <code>published</code>.</b> <span color="orange">change · queryability · 1 run</span></summary>

**Why.** Ford shows a real, self-contained base MSRP, but the *all-in* is dealer-set (markup + destination + fees) and rises with trim. The `partial` default tree's "a floor that moves materially with dose/tier" could be misread to force `partial` on **every** vehicle row. The agent ruled `published` (base MSRP is self-contained; dealer markup is third-party, not a same-seller hidden cost) and flagged the guess — correctly, but the contract doesn't adjudicate it. Recurs for any dealer/MSRP/marketplace-floor vertical (autos, appliances, anything with a manufacturer floor + reseller final price).

**Proposed edit** — append one sentence to the existing `partial`/`published` default tree:

> A **published manufacturer/maker floor** whose final price is set by a *third party* (dealer/marketplace markup, destination, fees) stays **`published`** — distinguish it from a *same-seller* hidden mandatory cost (a membership, a required add-on), which is `partial`.

**Simplification.** One sentence into the tree that already exists — no new value, no new section. Rides in the same edit pass as A1. n=1, so low priority — but it's the general principle (maker-floor vs same-seller-cost), not a Ford carve-out.

**Evidence.** Ford ruled priced vehicle rows `published` with the `S1` footnote ("Excludes destination/delivery fee plus government fees and taxes…") in Verbatim anchors; Ford GT correctly `on-request` (no price shown).
</details>

<details>
<summary><b>A4 — Keep the 7th header literally <code>What (molecule · form · access)</code> (minor, foldable).</b> <span color="orange">change · polish · 1 run</span></summary>

**Why.** Clerky reworded the header to `What (form · access)` — defensible (legal docs have no molecule) and lint-clean (the gate matches columns by `startswith`, so it passes). The impulse recurs on *any* non-pharma shape (Clerky, Notion, Warby, Airbnb all have no molecule). A one-line steer settles it cross-shape.

**Proposed edit** — add to the `## Roster` column note: *"keep the 7th header literally `What (molecule · form · access)` even for molecule-free verticals — vary the cell content (lead with the form clause), not the spine label."*

**Honest caveat — this is the most droppable item.** The "a cross-company digest keys on the literal header string" risk is **partly theoretical**: the lint matches by prefix and QUERYING recipes grep the body, so nothing actually breaks today. Include it as a half-sentence folded into A2, or **drop it** — I lean drop-or-fold.
</details>

## §B — Lint (`offeringscheck.py`)

<details>
<summary><b>B1 — One regex edit closes the only integrity-guard hole + a known footnote wart. Do them as one commit.</b> <span color="orange">change · fidelity-guard + queryability · 1+1 runs</span></summary>

**Why — this is the highest-severity finding.** Rule 1 (the anti-hallucination guard) greps **only `$`** (`PRICE_RE = \$\s?(\d[\d,]*…)`). For a metered/usage-priced seller the load-bearing prices are **percentages and cents** — Stripe rosters `2.9%+30¢`, `0.7%`, `3.5%`, `0.25%`, FX `+0.25%/+0.5%`, none of which the gate touches. **The bulk of a metered seller's price signal currently rides unverified.** Stripe's percentages happened to be faithful (I hand-checked), so no bad data shipped — but the guard is *provably blind to a whole pricing class*, which is a fidelity-class hole, not a hunch. Separately (Ford), the `(?!\d)` guard rejects a real `$` price the page glued to a footnote digit — `$79,0051`, `$106,4901`, `$79,9951` — so three halo MSRPs could not be rostered-quoted; footnote-glued prices are common in auto/finance/regulated copy.

**Proposed edit** — one widening of `PRICE_RE` / the grep loop, two gaps closed:
1. a rostered **`%`** or **`¢`** amount must also grep verbatim into a cited capture (same `(?!\d)` trailing discipline);
2. a `$NUM` glued to a **1–2-digit footnote marker** verifies (`$79,005` ✓ `$79,0051`), keeping the existing distinctions (`$30` ✗ `$300`; `$300` ✓ `$300Add-On`).

**Simplification.** Both are one-line changes to the **same** regex/guard → **one commit, one regression block**. Reuse check-4's existing corpus machinery; add no new check or section. Do **not** add a Ford-specific carve-out — the footnote tolerance generalizes.

**Implementation nuance (flagging, not blocking).** Widening to `%` is safe because the check is *presence-in-corpus*: the author only writes page-sourced numbers (the verbatim rule already requires it), so a real `2.9%` greps; a prose "20% off" that the author quotes is also on the page and greps too. Worth a quick look at whether any `%` should be *exempt* (e.g. a stat in prose vs a price) before landing — but the default (every rostered `%` must grep) is the right strict posture.

**Evidence.** `offeringscheck.py:42` confirmed `$`-only; `offeringscheck.py:163` is the `(?!\d)` guard. Ford glued prices `f150:647`, `mustang:640`, `bronco:2135` confirmed.
</details>

## §C — Contract + Skill menu (the services floor)

<details>
<summary><b>C1 — Bless "decline-with-reason" as a first-class outcome: a floor clause + a soft menu warn.</b> <span color="orange">change · queryability · 1 run (a whole class)</span> · = Decision (b)</summary>

**Why.** The "When to write it" gate names only consumer **pull** ("only when a cohort's consumer needs the per-SKU grain") and is **silent at the hard floor** — a Services/Consulting company with no published price and no enumerable SKU, where the schema has nothing to bind *even if a consumer asked*. And step 2.5 offers `+ per-SKU offerings.md` as a flat multi-select with **no shape guard**, so a guided user can request a structurally-empty module. IDEO hit exactly this and handled it well — but today the outcome is **recoverable, not repeatable**: the next services run must re-derive the decline on judgment.

**Proposed edit** — two surfaces, one fix:
- **`OFFERINGS.md` "When to write it":** add a one-line floor clause — *pure-services / bespoke companies (no published price, no enumerable SKU) → **don't write even on request**; `profile.md`'s What-they-offer lines + per-line `[on-request]` tokens are complete; record the decline in `## Provenance` → `### Run profile` ("Skipped with reason: …").* IDEO is the seed exemplar.
- **`SKILL.md` step 2.5:** when `offering_category` resolves to Services/Consulting, **warn — don't block** — the offerings options.

**Simplification.** **Reuses the existing Run-profile "Skipped with reason" note — no new field, no new file, no new module state.** Warn-not-block because `offering_category` can resolve late or wrong; the contract floor clause is the real backstop, so the menu change is one conditional.

**Evidence.** IDEO recorded the decline in two greppable places — `profile.md` What-they-offer line ("no `offerings.md` — a services firm has no SKU grain") **and** the `### Run profile` ("Skipped with reason… a bespoke design consultancy has no per-SKU grain… the family-line breadth in *What they offer* is the right altitude"). The lint returns the expected `no offerings.md (module not active here)` — a clean declined-run signal, not a defect.
</details>

---

## ⚠️ Decisions needed from Brian

> Two calls are yours — both touch governance, and **(a) reopens the wording of a locked decision** (flagged per protocol).

**(a) Notion's added `Category` column vs the locked "No Form/Category."** — *Recommend: <span color="green">keep project-local + fix the doc collision</span> (don't fold it out, don't promote it to the spine).*

The column is **already compliant** with the customization clause: strictly project-local (invisible to any cross-company `rg`, which greps the 7 spine columns), Run-profile-noted *twice*, lint-clean, and Brian-requested. Its 7 values (`plan · app · AI feature · workspace feature · developer · add-on · ecosystem`) are a within-company product-vs-feature axis — **not** the cross-company canonical key rule 4 forbids.

The real defect is a **doc collision, not the run**: `OFFERINGS.md`'s customization clause *invites* "a Form/Category for its own promotion mapping," while the locked pilot decision *bans* "Form/Category columns" — **the same word, two meanings.** Resolve by clarifying the lock's scope: a **cross-company canonical** Category stays forbidden (rule 4 / promotion-time mapping); a **within-company, project-local, Run-profile-noted** grouping column is the clause's blessed territory. This reopens the lock's *wording* — hence your nod — but preserves its *rationale* exactly (the cross-company key still rides in `What`, derived at promotion time). The leaner alternative (strike the clause's "Form/Category" example, force the column out) is defensible if you want the roster maximally lean, but it discards a useful, discipline-compliant axis and means editing the contract text anyway. *(Reject Notion's own retro-proposed `/pricing#business` slug fix regardless — constructed anchor; see Rejected.)*

**(b) Should the contract + menu bless "decline-with-reason," or keep it a per-run judgment?** — *Recommend: <span color="green">bless lightly</span> (= C1 above).*

Declining is already the *default* ("don't write the file"), and IDEO recorded its decline first-class via the existing Run-profile note — so blessing it costs almost nothing and removes real risk. The one-line floor clause + soft menu warn make the right call **repeatable instead of luck**, while leaving judgment intact for the ambiguous middle (the warn doesn't block). No new mechanism. *If you'd rather keep it pure judgment, the cost is: every services run re-derives the decline, and a guided user can still request an empty module.*

---

## Rejected, on purpose

- <span color="red">reject</span> **A Status / availability column** (`live | coming-soon | rolling-out`) — only Airbnb genuinely showed it, and it correctly folded into `What`. Hold at **n=1**; promoting a column now also collides with the no-Category posture. Re-evaluate only if a 2nd non-SKU run reproduces it.
- <span color="red">reject</span> **Clerky's "Kind/Visibility advisory for non-storefronts"** — loosens two lint-backing concepts for no demonstrated need. The bundled-price token (A1) is the earned part; this is scope creep the Clerky grader itself flagged.
- <span color="red">reject</span> **Notion's `/pricing#tier` slug convention** — would mint anchors (`/pricing#business`) that appear in no capture: a **constructed URL**, the exact sin the never-construct rule + lint exist to stop. The shared-real-slug half (what the run already does) is fine; the `#fragment` half must be explicitly rejected.
- <span color="red">reject</span> **A false-absence lint check** (tempting after Ford + Airbnb both shipped one) — real defects, but **instance-level and not cheaply mechanizable**: the lint greps `$`-presence and can't adversarially audit every prose absence claim without heavy machinery (anti-Doro). The recipe's B2 rule already says "don't assert a page is silent without grepping it" — the fix is **run discipline, not a new gate.**
- <span color="red">reject</span> **Per-vertical shape paragraphs** (a "legal-docs" note, an "auto/MSRP" note, an "eyewear" note) — the whole point of A1/A2/A3 is to handle these **generically**. A fourth per-vertical paragraph is the additive drift the engine-dev least-complexity line forbids.
- <span color="red">reject</span> **All per-run instance defects as *module* changes** — company-noise (wrong data in one file), not a contract/recipe/lint gap. The module-level lesson they'd suggest ("the lint can't catch a fabricated slug or false-absence") is **already known**, and the recipe rules already exist. *(Two are worth an instance pass — below.)*

## Not a module change — but worth a quick instance pass

- **Ford commercial block** *(one root-cause edit)* — a **misattributed slug** (the F-600's real URL `/trucks/f-600-super-duty-chassis-cab` applied to the **F-650/F-750** row — wrong product, present only in the raw `map.json` payload, not on a cited capture), a **9-row collapse** onto a footer anchor, and **two false-absence "no commercial landing" claims** its own `commercial.md` contradicts. *(I corrected the grader here: it's not "fabricated / resolves to nothing" — it's a real Ford path misapplied. Still a slug-fidelity defect the lint can't see; the retro both missed it and over-claimed the collapse was "forced.")*
- **Warby — the cohort's only real correctness miss** — `pdp_durand.md:211–229` shows **Progressives $325, blue-light +$50, anti-fatigue +$100, light-responsive +$125, 1.67 high-index +$60**; the roster drops them to `on-request "(priced at checkout)"`. Real shown prices, captured this run, hidden — a completeness gap + a visibility misjudgment the retro never engaged.
- *(ops, not the module)* a stray `</content>` wrapper tag surfaced in **both** a file and a retro — worth a scan of other 2026-06-04 outputs for a harness-wrapper leak.

## Ranking (the 7, for calibration)

Comparative reads surface the outliers better than absolute grades:

1. **Stripe** — hardest shape (100s-of-fees metered rate-card) handled cleanest; every `$` *and* `%`/`¢` verbatim, honest molecule→pricing-basis swap, one earned deep block. Only a contained misattributed justification-quote + a disclosed altitude seam.
2. **Notion** — airtight fidelity on the first tiered-SaaS run; docked only for the honest non-storefront strain it volunteered (the `incl.` token + degenerate `/pricing` slugs).
3. **Clerky** — cleanest pure-roster non-Rx run; 21 real offerings, 13 no-PDP rows correctly point at attested anchors. Nicked by a "homepage hero" mislabel + the reworded header.
4. **Airbnb** — best altitude judgment in the cohort (refused SKU grain on a marketplace, keyed on stable tag IDs). One fidelity slip the retro missed (3% host fee recorded "not stated" — it's on a cited page).
5. **IDEO** — correct decline, cleanly recorded in two greppable places; high-fidelity in the `profile.md` fallback. The engine's clean seed for the services floor — its value is the routed gap (C1), not a roster.
6. **Warby** — strong Catalog spine fit, but the **one run with a real correctness miss**: captured a PDP lens-price table and dropped it as `on-request`.
7. **Ford** — excellent on consumer models (all prices verbatim, powertrain page-attested, model-grain altitude), but the commercial block carries the cohort's worst defects (misattributed slug + 9-row collapse + two false-absences), and the retro missed the slug.

---

<sub>Sources — the 7 self-retros + 7 **independent** grades (each blind-graded, then verified: lint run, a sample of `$` prices greped, slugs + molecule/spec attestation spot-checked) + this session's firsthand verification of the Notion `Category` column, IDEO's decline recording, and the Ford/Warby instance defects. Extends the [design record](../../2026-06-03-offerings.md) and the [pilot triage](telehealth/2026-06-03-offerings-pilot-triage.md) (whose decisions remain locked); supersedes nothing. Propose-only. Authored 2026-06-04.</sub>
