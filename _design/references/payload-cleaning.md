# Reference: payload-markdown cleaning (research — not yet acted)

> Research for the BACKLOG item *"payload-markdown cleaning pass."* An empirical noise inventory of the captured markdown, a proposed **subtractive** cleaning ruleset, and the section-tagging decision. **Nothing is applied** — the next step is a de-risking experiment (bottom). Authored 2026-05-31 (Opus research session); a sibling to [`firecrawl-capture.md`](../../skills/research-company/firecrawl-capture.md) (capture mechanics) — this covers what to do with the markdown *after* capture.

## The premise (confirmed)

- **"Cleaned" captures = raw, byte-for-byte.** All 111 `captures/<date>/*.md` are identical to their payload's `data.markdown`. The write in `scripts/fc.py` (`md = data.get("markdown")` → `write_text(md)`) is verbatim; the "cleaned markdown" label is aspirational. **That write site is exactly where a pass slots in.** (SCHEMA/architecture call captures "cleaned observations" — currently untrue; the doc and the code will reconcile when cleaning lands.)
- **The honesty backstop is partial.** `.payloads/` (raw `html`/`rawHtml`/`markdown`) is the lossless original — but it's **gitignored** (iCloud-only). On a fresh git clone the cleaned `.md` is the *only* surviving primary source. So cleaning must be honesty-preserving **on its own merits**, not "raw is there." This is what forces the subtractive invariant below.
- **Scale:** 111 files, ~74.5K lines, ~656K tokens. **47.5% of all lines are blank.** A conservative subtractive clean removes ~59% of lines / **~19% of bytes (~125K tokens)** while keeping every content byte verbatim.

## 1. Noise inventory

| Pattern | Frequency | Example |
|---|---|---|
| **Blank lines** | 35,433 (**47.5%** of lines); 6 files >60%, `mac.md` 78.5% | every other line |
| **Hard-break residue** — lone `\\`/`\-`, trailing `\\` (Firecrawl renders intra-element breaks as escaped backslashes) | 5,556 lines (**7.5%**), 56 files, 222 KB | apple `services.md`: `\\` ×1,392; `Stream now\\` ×hundreds |
| **Stat-counter digit columns** — animated odometers explode into the digit *alphabet*, one char/line | 4,108 lines (**5.5%**), 92 files | gong `homepage.md:202‑233`: `0`⏎`1`⏎…`9`⏎`.`⏎`,`⏎`+`⏎`%`⏎`$` per slot. The real stat is in the surrounding prose, not here |
| **Leaked minified JS** — VWO/Optimizely/React internals dumped into md | 27 lines >1500c, 70 KB, 14 files | gethealthspan `homepage.md`: a 7,207-char VWO blob buries the real H1 to line 6 |
| **Repeated banner/card text** — visually-hidden + badge dup in dynamic grids | per-file | airbnb `Guest favorite` ×122, `for 2 nights` ×56; stripe demo dashboard `Succeeded`/`Visa ••••4010` ×14 |
| **Consent / form-proxy chrome** (repeats on *every* page) | 35 files | hims `Powered by Transcend`/`I consentI do not consent` ×8; gong Marketo proxy-frame ×7 |
| **Form-control dumps** — `<select>` flattened to one line | 7 lines, ~2.5 KB each | blueowl `Please selectAfghanistanAlbania…` ×6 |
| **Decorative (empty-alt) images** `![](url)` | 1,848 lines, 186 KB | logo carousels, spacers. **Distinct from 1,626 alt-bearing images** (`![LinkedIn logo]`) — those are proof-strip *signal*, keep |
| **Inline data-URI / base64 SVG** | 306 lines, 49 KB; one airbnb line 7.4 KB | `![Google](data:image/svg+xml,%3Csvg…)` |
| **Player/widget chrome** | scattered | nike caption menu `TextColorWhiteBlack…`; maximus chart legend `- OPTIMALO`/`- MAXIMALM` ×256 |
| **Glued no-space text** — animated/rotating text loses spaces | 123 lines | gong `Theworld'srichestrevenuegraph…`; airbnb `cultureBeachMountains…` |

## 2. Proposed cleaning ruleset

**The linchpin invariant — what makes it honest:**

> **Cleaning is *subtractive + whitespace-only*.** It may delete whole noise lines/regions and collapse blank runs. It may **never** reword, reorder, merge, or re-space a content line. Every surviving byte is verbatim. — This is the guarantee that survives the git-clone case: a subtractively-cleaned file is still faithful primary source with no raw fallback needed.

- **Tier A — mechanical artifacts (always safe):** collapse 3+ blank lines → 1; drop lone `\\`/`\-` and trailing `\\`; collapse stat-counter digit-column runs; drop **empty-alt** images `![](url)` (keep alt-bearing verbatim).
- **Tier B — leaked non-content blobs (safe, high value):** minified JS (VWO/Optimizely/GTM/React — detect by line length + JS signature); consent/form-proxy boilerplate (Transcend, Marketo proxy-frame, cookie modals); `<select>` option-dumps; caption-settings menus.
- **Tier C — never touch (the honesty boundary):** anything claim/price/tagline/regulated-language bearing; visually-hidden *duplicates* (a dup is harmless — deleting the wrong copy risks dropping the only number; leave both); nav lists, testimonials, real headings — **including mangled glued ones** (re-spacing = rewriting).

**Operational:** run at the `fc.py` write site; **keep the manifest md5 on the raw markdown** so dedup/`verify` is unaffected — the `.md` becomes a cleaned *derived* view, raw JSON in `.payloads` stays the original. Prepend a one-line audit header so the file announces it's curated and points home, e.g.:
`<!-- wr-clean/1: -412 blank · -86 hardbreak · -1 vwo-script · -1 cookie-block · raw: .payloads/homepage.json -->`

## 3. Section-tagging — decision

Brian's idea: tag section types (`faq`, `footer`, `primary-nav`, `trust-strip`, `testimonials`) with a maintained vocab so a consumer can grep to a region. The bar it must clear: **`profile.md` already provides a fixed, greppable section vocabulary** (Overview / What they offer / Nav structure / Credibility & proof / Provenance + the bold-lead-in convention), and the [rung-2 experiment](../../experiments/2026-05-29-query-affordance/FINDINGS.md) found fidelity comes from *profile/offering-schema consistency*, **not** from navigating raw captures by section.

| Name | Description | Pros | Cons | Mitigation |
|---|---|---|---|---|
| **A. Lean on profile.md** | Captures stay verbatim phrase-grep fallback; the *profile* is the section-structured surface | Zero surface; honors "earn every structure"; matches the rung-2 finding | No region-grep into raw captures | Revisit on ≥2 real consumer sightings |
| **B. HTML-comment markers** | Cleaner wraps regions: `<!-- wr:faq -->…<!-- /wr:faq -->` | Honesty-preserving (comments ≠ content); greppable | A vocab to govern; mis-label risk; adds lines | Tiny closed vocab (≤8); tag only high-confidence |
| **C. Strip-not-tag** | Don't tag footer/nav/cookie — *remove* the chrome (Tier B). What survives is mostly signal | Same payoff by deletion; one mechanism, no new vocab | No positive "this *is* the FAQ" pointer | Audit header lists what was stripped; keep nav (signal) |
| **D. Sidecar section map** | `<page>.sections.tsv` (type → line-range) beside an untouched `.md` | `.md` stays pure; machine-clean; feeds a future index | Another file; drifts on re-clean; unread by hand | Generate from the clean pass; regenerable, never authoritative |
| **E. Heading-prefix rewrite** | `## [faq] Questions & answers` | Most grep-ergonomic inline | **Rewrites primary source — breaks the invariant**; pollutes verbatim grep | *(reject)* |

**Decision: C + A now; defer B and D; reject E.** Stripping chrome (C, which *is* the cleaning pass) already removes the *need* to tag footer/nav/cookie, and `profile.md` (A) already answers "grep to the right region." Don't introduce a maintained section vocabulary until a consumer demonstrably needs to grep *into raw captures* by region. Lightest thing that works; resists the additive pull.

## Next step (not started)

De-risk before any contract/corpus change: `experiments/<date>-payload-clean/` with a `clean.py` running Tier-A/B over the 111 existing files into `_out/`, and a `FINDINGS.md` reporting the content-line-loss diff (**target: zero**). Only if that diff is clean, propose the `SCHEMA.md` + `fc.py` change.
