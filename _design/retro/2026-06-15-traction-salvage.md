# RETRO — Traction Signals v1 salvage ($0)

Date: 2026-06-15 · A salvage pass, not a build. Pulled **already-captured** raw tool envelopes for 3 telehealth companies — scattered across this repo's `experiments/` and the Teleprescribe `traction v2` runs — into the engine's new `store/<domain>/signals/` home, keeping only the clean ones. Zero new captures, zero network, zero spend. First real test of the engine's core bet (["capture once, read back, generic across projects"](../2026-06-15-traction-approach.md)) on envelopes this system **didn't place itself**.

## 30-second skim

- **Landed 12** raw envelopes (of 16 clean candidates) for hims-com / honehealth-com / maximustribe-com — **3 trustpilot** baselines + **9 wayback** page tenures — beside each company's existing `profile.md`. The other 4 are clean-but-redundant slash/no-slash twins, deduped (below).
- **The bet held.** The comparator ate the salvaged Hone NAD wayback pair (Jun 8 + Jun 11) **cleanly** read back from the store path: `exit 0`, `read_mode: delta`, four metrics, **zero vetoes, zero drift**. A correct "stable tenure" delta (the archive didn't move in the window), from purely-salvaged data, zero re-capture. That is the whole point.
- **Finding #1 — generic-engine bet:** held on real cross-project data, with one caveat the fixtures hid (trailing-slash subject collision; comparator-grounded, handled by dedup).
- **Finding #2 — path convention bent under real data:** the architecture calls `signals/` **"company-grain"**, but real wayback is **page-grain, many URLs per domain** — the documented `signals/<source_type>/<captured_at>.json` has no slot for the URL. I inserted a `<url-slug>/` segment; it works pairwise but is invisible to the comparator's non-recursive dir-mode glob.
- **Two tools had nothing to salvage:** **zero** `trends` and **zero** `sec_edgar` envelopes exist in *either* tree for *anyone* — not just these 3. (Searched, not assumed: those tools shipped after these runs.)

---

## Provenance ledger

**Origin trees** — `WR` = this repo's `experiments/`; `TP` = `…/Teleprescribe Venture/…/traction/v2/runs/` (read-only; copied out, never modified).

### Promoted → landed in `store/` (12)

| Store path (`store/…`) | Origin | Label | Why it earned promote |
|---|---|---|---|
| `hims-com/signals/trustpilot/20260608T230211Z.json` | TP `…phase1-phase2-d0-seed/raw/trustpilot/trustpilot-hims-com-2026-06-08.json` | **promote** | trustpilot v1, ok, no drift, active, `review_count`=8500; subject `hims.com` ✓ |
| `honehealth-com/signals/trustpilot/20260608T215953Z.json` | TP `…sermorelin-focused-recheck/raw/trustpilot-honehealth-com-2026-06-08.json` | **promote** | v1, ok, no drift, `review_count`=11579; subject `honehealth.com` ✓ |
| `maximustribe-com/signals/trustpilot/20260608T220100Z.json` | TP `…sermorelin-focused-recheck/raw/trustpilot-maximustribe-com-2026-06-08.json` | **promote** | v1, ok, no drift, `review_count`=975; subject `maximustribe.com` ✓ |
| `honehealth-com/signals/wayback/longevity-nad/20260608T192355Z.json` | WR `2026-06-08-wayback-telehealth-pilot/honehealth-nad-tenure.json` | **promote** | wayback (version-less feed), ok, no drift; **D0 of the prove-it pair** |
| `honehealth-com/signals/wayback/longevity-nad/20260611T175449Z.json` | WR `2026-06-11-wayback-telehealth-repeat/honehealth-nad-tenure.json` | **promote** | **D7 of the prove-it pair** — same URL, +2.94 days |
| `honehealth-com/signals/wayback/mens-enclomiphene/20260608T231537Z.json` | TP `…wayback-tenure-seed-panel/raw/wayback-enclomiphene-hone-primary-tenure-…json` | **promote** | ok, no drift; lone D0 baseline |
| `honehealth-com/signals/wayback/mens-sermorelin/20260608T231052Z.json` | TP `…/raw/wayback-sermorelin-hone-primary-tenure-…json` | **promote** | ok, no drift; lone D0 baseline (twin deduped) |
| `hims-com/signals/wayback/testosterone-enclomiphene-supplements/20260608T231438Z.json` | TP `…/raw/wayback-enclomiphene-hims-primary-tenure-…json` | **promote** | ok, no drift; lone D0 (slash-twin deduped) |
| `hims-com/signals/wayback/testosterone-enclomiphene-tadalafil-supplements/20260608T231531Z.json` | TP `…/raw/wayback-enclomiphene-tadalafil-hims-primary-tenure-…json` | **promote** | ok, no drift; lone D0 (slash-twin deduped) |
| `hims-com/signals/wayback/erectile-dysfunction-hard-mint-chewable/20260608T231720Z.json` | TP `…/raw/wayback-tadalafil-hims-hard-mint-primary-tenure-…json` | **promote** | ok, no drift; lone D0 baseline |
| `maximustribe-com/signals/wayback/testosterone-enclomiphene-only/20260608T231436Z.json` | TP `…/raw/wayback-enclomiphene-maximus-primary-tenure-…json` | **promote** | ok, no drift; lone D0 baseline |
| `maximustribe-com/signals/wayback/testosterone-enclomiphene-tadalafil-testosterone-cream/20260608T231805Z.json` | TP `…/raw/wayback-tadalafil-maximus-combo-primary-tenure-…json` | **promote** | ok, no drift; lone D0 baseline |

Copies are **byte-verbatim** (`cmp` confirmed); the filename changed to `<captured_at>.json` per the convention, content untouched. Provenance lives here, not in the files.

### Deduped — clean, but left in source (4)

The seed panel captured several pages **twice, seconds apart**, once with a trailing slash and once without (a URL-form A/B). The comparator's `subject_of()` **rstrips `/`** (`signal_delta.py:94`), so the twin is the *same subject*; `branch_wayback` keys a dict by subject, so co-storing both would **silently clobber one on dir-load**. Kept one per page (the earlier "primary"), left the twin put.

| Left in source | Twin of (promoted) | Reason |
|---|---|---|
| TP `…/wayback-enclomiphene-hims-slash-variant-…json` (`…/enclomiphene-supplements/`, +15s) | hims enclomiphene-supplements | same subject after slash-strip |
| TP `…/wayback-enclomiphene-tadalafil-hims-slash-variant-…json` (+5s) | hims enclomiphene-tadalafil-supplements | same subject after slash-strip |
| TP `…/wayback-sermorelin-hone-slash-variant-…json` (`…/mens/sermorelin`, +20s) | honehealth mens-sermorelin | same subject after slash-strip |
| TP `…/wayback-nad-hone-primary-tenure-…json` (`…/longevity/nad/`, 23:12:33) | honehealth longevity-nad (the WR pair) | same subject, same-day cross-tree dup — **corroborates** the WR Jun-8 capture, doesn't extend the series |

### Demoted / retired / left-put (the traps)

| Items | Label | Reason |
|---|---|---|
| 5 wayback captures for hims/hone/maximus under `…/sandbox-preflight-failures/` (`ok:false`) | **demote** | the capture tool already suppressed its parse (`ok:false`) — the fence (`_fence`) vetoes them; not diffable |
| `experiments/2026-06-15-signal-delta-trustpilot/**` incl. `_out/store/honehealth-com/signals/trustpilot/*.json` | **retire** | hand-built **fixtures** (round-clock `12:00:00Z` timestamps, fake counts). The `_out/` ones masquerade as a real store path — retire on sight |
| 19 serpapi query captures across both trees (8 WR + 11 TP: TRT / sermorelin / NAD / tirzepatide / enclomiphene / semaglutide …) | **leave put** | **category_query-grain** — subject is a search query, not a company. No domain home; `cohorts/` is deferred/unbuilt (see Finding #2) |
| ~40 trustpilot/wayback envelopes for joinamble, rexmd, brello, trtnation, agelessrx, hydramed, bluechew, … | **out of scope** | clean, but subject ≠ one of the 3 cohort companies; not this salvage's mandate |
| `tool=trends`, `tool=sec_edgar` | **not found** | **zero** envelopes exist in either tree for anyone — those tools postdate these runs. *Not-found, not not-there.* |

---

## Finding #1 — Did the generic-engine bet hold on real historical data?

**Yes — with one caveat fixtures structurally couldn't expose.**

The comparator consumed envelopes placed by a *different* project's tooling, months of conventions apart, and produced a correct delta with no special-casing:

```
$ python3 tools/signal_delta.py \
    store/honehealth-com/signals/wayback/longevity-nad/20260608T192355Z.json \
    store/honehealth-com/signals/wayback/longevity-nad/20260611T175449Z.json
→ exit 0 · read_mode "delta" · gap_days 2.94
  archive_presence: stable · snapshot_count: 12→12 (Δ0) · last_seen: stable · content_digest: unchanged
  vetoes: []  comparability_flags: []  schema_drift: []
```

The "stable tenure" result is the *honest* answer (Wayback's last snapshot is Apr 10; nothing new archived in a 3-day window), not a null. The shared **envelope spine** — `tool` / `ok` / `captured_at` / `input` / `schema_drift` — held identically across both trees; the dispatch keyed on `tool` correctly (`"wayback"`, not a concept); the alignment fence found the same subject. **The bet that captures are generic across projects is vindicated on real data.**

The caveat the fixtures hid: **trailing-slash subject collision.** Fixtures invented one clean subject per file; real seed-panel data captured the same page under `/nad` and `/nad/`. Because `subject_of` canonicalizes the slash away, two such files are the *same subject* and clobber on dir-load. This is a real-data-only failure mode — handled here by dedup, but it argues any future importer must dedup on the *canonicalized* subject, not the raw URL string.

## Finding #2 — What path-convention edges did real data expose?

**The convention says "company-grain"; the comparator says "page-grain." Real data forced the contradiction the fixtures never did.**

- The architecture commits `store/<domain>/signals/<source_type>/<captured_at>.json`, **"company-grain"** (`architecture.md:60,74,156`) — one file per `(source_type, captured_at)`. That holds for trustpilot/trends/sec_edgar: one company = one domain = one subject, no collision (the 3 trustpilot landings dropped straight in).
- But `signal_delta.py`'s own `GRAIN` map (`:59-64`) assigns **`wayback → page`** (subject = a URL) and **`serpapi → category_query`** (subject = a query). Wayback is **many URLs per domain** (hims alone: 3 distinct product pages here) — so `(wayback, captured_at)` is *not* unique, and the documented path has nowhere to put the URL. Fixtures, being one-subject-per-file, never hit this.
- **Pragmatic call (made, recorded):** insert a `<url-slug>/` segment — `store/<domain>/signals/wayback/<url-slug>/<captured_at>.json` (e.g. `…/wayback/longevity-nad/20260608T192355Z.json`). It keeps the convention's `<captured_at>.json` *filename* verbatim, disambiguates the page, and makes "all timepoints of one page" a single `ls`. **Pairwise diff (file vs file) works through it** — that's what the prove-it used.
- **The edge it leaves (noted, not fixed):** the comparator's dir-mode loader globs `*.json` **non-recursively** (`_load_envelopes`, `:438`). Verified empirically — pointing dir-mode at a domain's `wayback/` root finds **0 envelopes** (the subdirs are invisible). So *run-vs-run over a whole domain's wayback* would need per-url-dir handing or a recursive walk. Fine for now (D0/D7 reads are pairwise); a real follow-up when whole-domain wayback runs arrive.
- **Category-grain has no home at all.** The 11 serpapi panels are query-grain; `cohorts/<category-slug>/` is reserved-but-unbuilt. They stayed put — that gap is itself the finding the brief predicted.

---

## One line for the deferred orchestration call

**The evidence points to an *import/consolidation affordance*, not a capture batch runner** — this salvage paid **$0 in capture** and spent all its effort *landing already-paid-for envelopes* (gate → canonicalize path → dedup on canonical subject → byte-copy); the friction was scattered provenance and the page-grain path-bend, exactly what a thin `signals_import.py` would absorb, whereas a batch *runner* solves re-capture cost this pass never incurred. (The runner earns its turn later, when a fresh D7/D14 point — e.g. trustpilot velocity's missing second capture — is actually worth the spend.)

<sub>**Method** — read [traction approach](../2026-06-15-traction-approach.md) (#1 storage, #2 grain) + [architecture](../2026-05-30-architecture.md) (`signals/` path) + [`signal_delta.md`](../../tools/signal_delta.md) + the live tool version pins; a Sonnet sub-agent ran the read-only inventory across both trees; triage / land / prove / writeup by the main agent. No new captures, no network, no spend. Teleprescribe tree read-only throughout.</sub>
