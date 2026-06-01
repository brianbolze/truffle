# FINDINGS — coded queries

Ran six candidate primitives ([`probe.py`](probe.py)) against the live 45-profile store. The line between
"earns a script" and "stays a `QUERYING.md` recipe" is sharp, and the join-check found four data facts prose
can't.

## The line: what earns code

**Earns code — error-prone or silently-wrong by hand:**

- **`find` (resolver: domain / name / alias / slug → one key).** The happy path is trivial (you'd guess the
  slug), so the value is entirely in the misses an agent makes by eye. All of these resolve, none are obvious:
  `granola.so → granola-ai`, `chatgpt.com → openai-com`, `Peter Uncaged MD → getpetermd-com`,
  `SendGrid → twilio-com`, `NYSE: OWL → blueowl-com`. "Domain is the key" only works if *one* function folds
  every surface form to that key — that function is `canon()` (lowercase, strip scheme/www, dots→dashes), and
  it's exactly what a hand-rolled grep skips.
- **`relations` (join-check).** Eyeballing which of 24 domain-shaped `parent`/`owns` targets point at a held
  profile, across 45 files, is where an agent quietly miscounts. Code says it flatly: **1 joinable · 23
  dangling · 8 name-only.** (See the four findings below — all fell out of this one probe.)

**Stays a recipe — already a one-liner in QUERYING.md:**

- **`stats` / count, `recent`, `facet`, `coverage`.** Real conveniences, but each is a `Counter`/`sorted` over
  the parsed dict that QUERYING.md already spells out. Worth code only if they ride along in a module that
  exists for `find`/`relations` anyway — not worth a script of their own. `recent` gets a small bump from
  `captured_at` parsing as a native date (free chronological sort + day-age staleness).

**The dividing rule** (the reusable takeaway): commit a query as code when it's *(a)* error-prone by hand
(alias resolution) or *(b)* silently wrong by hand (membership counts on multi-selects — the `grep | uniq`
trap QUERYING.md already calls out — or counting joins across the corpus). Everything else stays prose.

## What the join-check surfaced (prose wouldn't)

1. **The JOIN gap is 23/24 — the relation graph points almost entirely *out* of the corpus.** Only
   `delighted-com --parent--> qualtrics-com` resolves. Expected at N=45, but now it's a *number*, not a vibe:
   it quantifies exactly how empty the rung-3 index would be today. Argues for keeping the index deferred.

2. **Top re-capture target by in-degree: `richemont.com` (2 — A. Lange *and* Cartier point to it).** Every
   other dangling target has in-degree 1. A captured child with an un-captured parent that *two* held profiles
   share is the highest-value next capture — and ranking by in-degree is a code-only move (prose can't sort 23
   targets by how many profiles reference them). The join-check doubles as a **re-capture ranker**; that
   maintenance use may beat the consume-side one.

3. **A slug-convention split in `owns`.** Casio stores `gshock-casio-com` / `edifice-watches-com` (dashed
   slug-form); everyone else stores dotted domains (`converse.com`, `reverb.com`). SCHEMA's own example is
   dotted (`kenvue.com`). `canon()` folds both, so matching survives — but a naive JOIN that string-equals one
   form would silently miss the other. **Fix:** name `canon()` the official join key, or normalize
   `parent`/`owns` to one form on write. Cheap now (13 profiles have `owns`), compounding later.

4. **~~A mis-typed alias: `clari-com` lists `salesloft.com`.~~ → FALSE POSITIVE on review.** The probe
   flagged `salesloft.com → clari-com` as a suspect alias (my prior was "competitors, distinct entities"). But
   the `clari-com` profile *documents* it: Clari and Salesloft **merged in 2025** into one combined company —
   the exact "M&A escape hatch" `aliases` exists for (SCHEMA). So the resolver mapping the acquired co's domain
   to the survivor is **correct behavior, not a bug**. Lesson worth keeping: the join/resolve heuristic can't
   tell a *merger* from a *typo* — a resolver hit that looks wrong needs the profile body (or a human) as the
   backstop before you "fix" it. Net: this is validation that aliases + the resolver handle M&A right.

5. **`facet` only pays off on closed-set fields.** `facet design_framework` fragments
   (`react` / `react (custom SPA)` / `custom React SPA`; `salesforce-commerce-cloud` /
   `Salesforce Commerce Cloud (Demandware)`) because it's a free-text field, not a TAXONOMIES enum. Useful as a
   *drift detector* there, but not a clean group-by. On closed sets (`portfolio_shape`, `business_model`) it's
   exact.

## Cost: the index stays deferred

The whole battery — five separate processes, each loading all 45 frontmatters from scratch — runs in **~1.3s
wall / 0.11s CPU**. No caching, no index, no SQLite. At this N a derived index would be pure overhead; this
confirms QUERYING.md's rung-3 call rather than challenging it.

## Relationship to `querycheck.py`

No overlap. [`scripts/querycheck.py`](../../scripts/querycheck.py) is a *contract self-test* (does the corpus
still satisfy QUERYING.md's structural assumptions — run on schema change). These probes are *consume-side*
(answer a reader's question). A graduated module would sit beside querycheck, not replace it.

## Recommendation

1. **Graduate two functions** into a small `scripts/store.py`: `resolve(query) → slug` and `relations()`
   (join-check + dangling-target in-degree). These are the error-prone-by-hand pair; the rest stay QUERYING.md
   recipes. `canon()` ships with them as the documented join key.
2. **Pick one relation form** (recommend dotted domain, matching SCHEMA's `kenvue.com` example) and normalize
   the two Casio entries; or, equivalently, declare `canon()` the join key in SCHEMA so the form stops
   mattering. Either kills finding #3.
3. ~~Fix the `clari-com` / `salesloft.com` alias.~~ **No fix** — finding #4 was a false positive; the alias is a
   correct, documented 2025 merger.
4. **Do not build SQLite** — see cost.

*Acted on (2026-06-01): #1 → [`scripts/store.py`](../../scripts/store.py) (`resolve` + `relations`), pointers in
[`QUERYING.md`](../../QUERYING.md). #2 → Casio `owns` normalized to dotted domains; [`SCHEMA.md`](../../SCHEMA.md)
names `canon()` the join key. #3 → verified, no change. #4 → no SQLite.*

*Throwaway probe; `probe.py` is the artifact, not load-bearing. If #1 is taken, the graduated module supersedes
it.*
