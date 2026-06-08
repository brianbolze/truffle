# tools backlog

Review notes, weaknesses, and possible enhancements for the shared capture utilities in `tools/`.
This is a curated list, not an append-only roadmap. The capture tools should stay small: one source
in, one JSON object out, no project judgment baked in.

**Not this file:**
- Root [`BACKLOG.md`](../BACKLOG.md) — engine-level schema, verbs, and workflow decisions.
- Tool companion docs (`*.md`) — durable gotchas and output examples for a specific source.
- Project workflows — Teleprescribe-specific panels, ledgers, and strategic reads stay project-side
  unless they prove a reusable method capability.

**Item format.** A bold punchline + tags on one scannable line, then 1-3 tight sentences. Tags:
`[weakness]` gap likely to bite · `[idea]` possible improvement · `[bug]` confirmed defect ·
`[tbd]` pending decision · `[simplification]` removes surface area / prescriptiveness.

**Bias to remove.** If an item adds a new helper, name the caller pain it replaces. If the pain is
only "the current tool makes the caller think," leave it alone.

**Soft cap: <=15 open items.** Over that, cut or graduate before adding more.

---

- **Fix tool status/documentation drift before first commit** `[bug]`
  `README.md` still marks `wayback.py` and `trends.py` as planned even though both exist, and
  `wayback.py` cites a missing `wayback.md`. `ruff check tools` passes, but `ruff format --check tools`
  currently says `serpapi.py` and `wayback.py` would reformat. Also keep generated `__pycache__/`
  files out of the first staged add; `.gitignore` covers them, but the whole `tools/` dir is new.
  **Act when:** staging `tools/` for commit.

- **Wayback exact-URL semantics need one small hardening pass** `[weakness]`
  The docstring says a bare domain becomes a homepage exact match, but `lookup()` passes the raw arg
  directly to CDX. Either normalize bare domains to a deliberate canonical URL (`https://domain/` or
  documented CDX domain behavior), or update the docs so callers do not think `example.com` and
  `https://example.com/` are interchangeable.
  **Act when:** using Wayback as the SKU-tenure axis for a ledger.

- **Clarify partial-capture exit semantics** `[tbd]`
  The library convention says exit `0` means clean, but `trends.py` exits `0` for partial runs while
  setting top-level `ok: false`. That may be the right shell behavior, because partial Trends data is
  still useful, but callers need one rule: either "exit code is transport/drift only; read `ok` for
  completeness" or "partial means non-zero." Pick once and update `README.md`.
  **Act when:** first batch/orchestration caller depends on shell exit status.

- **Golden fixture tests for parser contracts** `[weakness]`
  The parsers are careful, but their safety is mostly in prose. Add small fixture tests for the
  stable edge cases already documented: SerpAPI inline AIO / async error / list rejection,
  Trustpilot active-empty-removed-not-found plus Cloudflare challenge classification, Exa missing
  `results`, and Wayback empty CDX / malformed header. This protects the "fail loud, suppress parsed
  fields" promise without hitting live APIs.

- **Tiny envelope validator before an envelope builder** `[idea]`
  Every tool repeats the reserved JSON spine. Do not jump straight to a shared factory; a lightweight
  `tools/_check.py` or test helper that validates top-level keys, UTC shape, `schema_drift` behavior,
  and JSON-object output would catch drift while preserving each tool's simple local construction.
  **Act when:** adding the next tool or writing fixture tests.

- **Dependency/install smoke for optional clients** `[weakness]`
  `trends.py` requires `pytrends`, but the repo has no tools dependency manifest or smoke command.
  Keep the dependency optional, but make setup discoverable: a minimal `requirements-tools.txt` or a
  documented `python3 tools/trends.py --help`/import smoke in the tool docs. Avoid turning this into a
  package unless another real dependency appears.

- **Generic matcher helper has probably earned its place** `[idea]`
  The tools correctly stay match-free, but every useful SERP/discovery/ledger caller needs the same
  boring operations: domain extraction, `www.` strip, alias-aware text match, first-match provenance,
  and "own page vs mention" classification. A small `_match.py` should be generic and importable; it
  should not know about Teleprescribe, Notion, or vertical taxonomies.
  **Act when:** a second caller beyond SERP needs the same domain/text matching.

- **Batch runner for repeated captures, not per-tool loops** `[idea]`
  SERP, Trustpilot, Exa, and Wayback intentionally take one input per invocation; Trends is the one
  exception because its loop is the method. A reusable batch wrapper could read JSON/CSV/stdin rows,
  invoke one tool repeatedly, preserve each tool's raw envelope, and emit a combined JSONL/object.
  Keep it as orchestration glue, not a destination writer.
  **Act when:** running the 15-brand Trustpilot panel or a 30+ URL SKU-tenure ledger by hand feels
  silly twice.

- **SERP intent bake-off should be a consumer recipe over `serpapi.py`** `[idea]`
  The category probe needs query sets, repeated captures, own-page/listicle/local classification, and
  stop/continue gates. Do not widen `serpapi.py`; build a small recipe or helper that consumes its
  organic output plus `_match.py` and leaves buyer-intent judgment to the project.
  **Act when:** repeating the TRT/sermorelin/NAD/GLP query set after 48-72 hours.

- **Trustpilot velocity/integrity belongs beside, not inside, `trustpilot.py`** `[idea]`
  `trustpilot.py` draws the right capture/judgment line. The reusable next layer is a comparator over
  two or more Trustpilot envelopes: deltas, monthly velocity, solicitation segmentation, profile-state
  vetoes, duplicate/template flags, and a "suppressed/not comparable" reason. Keep SKU/category claims
  out unless the review text names the SKU.
  **Act when:** the D7/D14 review panel is run from captured JSON instead of a markdown hand table.

- **SKU ledger builder should consume store/cartography + tools, not become a tool parser** `[idea]`
  The ledger shape is useful, but most of it is orchestration: seed SKUs from cartography/store,
  call Wayback/SERP/Trustpilot as independent axes, then label `supply only`, `visibility`,
  `plausible movement`, `not measurable`, or `vetoed`. Build that as a consumer-side method only
  after the Wayback and SERP repeat passes prove the axes separate anything.

- **Do not migrate Reddit into `tools/` by inertia** `[simplification]`
  Prior traction work repeatedly found raw Reddit/forum counts sparse, rate-limit-frictiony, and easy
  to overread. Keep `reddit.py` off the planned table unless a new consumer has a narrow source,
  query, and text-classification reason that beats the old failure mode.

- **Do not add Ad Library until the capture path is stable enough to pin** `[tbd]`
  Meta ads are a useful push signal, but the old route depended on an Apify actor and unreadable DPA
  placeholders. Before promoting it, confirm the actor/build pin, schema-drift path, cost envelope,
  and "push, not demand" language. Otherwise it will be the first tool that looks quantitative while
  mostly measuring capture artifacts.
