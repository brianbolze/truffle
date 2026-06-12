# Presentation layer: where humans read

> **What this is.** The frame (problem) and approach (solution) for the engine's human-facing
> surface — the company brief, the comparison sheet, the index. Companion to the
> [Frame](2026-05-29-frame.md) and [Architecture](2026-05-30-architecture.md); written 2026-06-12,
> when the layer graduated from prototype to keeper. Part A is *why and for whom*; Part B is *how*.
> Don't let solution ideas leak into Part A.

---

## Part A — The problem / frame

### The one-liner

Everything in the store is written for **agents**. The presentation layer exists because
**humans** also need to read this knowledge — and humans read differently.

### The split

- **The store is the engine's memory.** Its readers are agents: they grep, parse frontmatter,
  tolerate density, follow citations. Lossless and dense *on purpose*.
- **The presentation layer is the engine's voice.** Its readers are humans: they don't filter,
  they glance. The layer must do the editing the store deliberately refuses to do.
- It is a **one-way translation boundary**: store → artifact. Nothing flows back.

### Who reads it

**Trusted humans only** — we do not design for artifacts traveling onward (a brief forwarded to
a stranger). Revisit if that changes. Two personas, one artifact:

- **Brian** — technical, the system's own developer; cares about provenance, clocks, what wasn't
  verified.
- **Scott-shaped readers** — senior, non-technical, allergic to complexity; need the read, not
  the machinery.

The same artifact serves both by **placement, not omission**: the front of every artifact speaks
to the non-technical reader (the read); provenance and limits stay first-class but live in a
consistent quiet zone the technical reader knows to find. Engine vocabulary ("schema 2.5",
"enumeration floor") is welcome in the provenance zone, avoided in the read zone.

### What "good" means

- **5-second land.** A non-operator gets the point unaided. Humans can't grep — visual
  hierarchy is their query language.
- **Trust is rendered, not appended.** Capture clocks, enumeration floors, unverified fields —
  shown as design, because a human can't check frontmatter. This is the layer's honesty
  contract, replacing the agent's citation contract.
- **Identity-dressed.** Artifacts wear the company's own captured palette, type, and marks.
  No agent needs this; every human feels it.
- **Survives the hand-off.** One self-contained file: AirDrop, Quick Look, print, no server.
  An agent re-reads at query time; a human's copy lives on in Downloads — so every artifact
  date-stamps itself loudly.
- **Curated cardinality.** Agents get a composable query surface; humans get a *small set of
  opinionated views*, each earned by a real human ask. This layer must never become "a query
  language, but HTML."

### The vow

The store's vow is *never paraphrase*. This layer's vow is weaker and different:
**select, compress, arrange — never invent.** Editing for a human reader is the job;
adding facts the dossier doesn't hold is forbidden.

### Non-goals

- Not an agent surface — agents keep `store.py` / SQL; the HTML is not for parsing.
- Not interactive or live; no feedback channel from artifact back into the store.
- Not per-recipient views — **one house view** per artifact (navigation inside it is fine).
- Not an operational dashboard — coverage/staleness triage is a different tool, not the index.
- Not in the store — human artifacts never sit beside agent records.

---

## Part B — The approach / architecture / solution

### The three views (today)

| View | The human ask it answers |
|---|---|
| **Brief** (`render.py <company>`) | "Tell me about X" |
| **Comparison sheet** (`compare.py A B …`) | "Show me X against its category" |
| **Index** (`render.py --index`) | "What's in here?" — the browsing front door; search is the likely next feature |

New views are rationed by a real human ask (rule of two), and every view is a **regenerable
lens** — derived from the store, never authoritative, cheap to throw away.

### Code layout

One package, one job per file; views never import each other; theme is the only home for style.

```
scripts/
  present/
    model.py            # read side: extract from store records (no HTML)
    assets.py           # fonts, logos, screenshots, caches; color math
    md.py               # dossier-markdown subset → HTML
    theme.py            # design tokens + css loader
    css/                # real .css files: base.css (shared dress) + one per view
    brief.py  compare.py  index.py     # one view = one module
  render.py  compare.py # thin CLIs — commands unchanged
```

CSS lives in real files for editing and is **inlined at render time** (stdlib `open()`), so the
output stays one self-contained file. HTML stays in f-strings — templates would relocate the
same code behind a new dependency.

### Output location

All derived artifacts in **top-level `_out/`** (briefs, sheets, index, `store.db`) — one
gitignored derived-root. Never in `store/`: the store is the agent surface, and a stale
rendered copy beside a fresher record quietly lies.

### Compression (kept deliberately light)

Mechanical first: truncation, type scale, collapsed sections with peeks. Where verbatim text is
genuinely too long for a human surface (e.g. the hero headline), **condensed copy is in-frame**
under the vow — but it is written agent-side (a skill / slash-command step at refresh time,
cached beside other derived output), **never an LLM API call inside the renderer**. The
renderer stays dumb: it reads condensed copy if present, falls back to verbatim, and marks
condensed text as condensed.

### What we refuse (the anti-Doro line, presentation edition)

No server, no build chain (npm/Tailwind/PostCSS), no template dependency, no JS beyond trivial
progressive enhancement, no machine-parseable HTML contract, no per-recipient theming.

### Verification convention

Refactors of this layer prove themselves by before/after render diff across the demo set +
index — byte-equivalence modulo the generated date is the acceptance test.
