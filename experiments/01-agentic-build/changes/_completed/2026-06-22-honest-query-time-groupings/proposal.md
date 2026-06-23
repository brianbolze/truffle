# Proposal: The Grouping Stamp — honest answers about groups of companies

Date: 2026-06-23
Status: implemented — merged to master 2026-06-23 (commit `4fcaa16`); lead decisions `accept-for-implementation` → `merge`. Three open choices resolved: words-only (no tool); plain labels (no coined jargon); general coverage principle (not a dated snapshot).
Source request: [`frame.md`](frame.md) (Honest Query-Time Company Groupings, 2026-06-22). Options developed with a Claude Workflow — four solution shapes, an independent critic for each, and a judge — at Brian's request.

## The one-paragraph version

When Truffle answers a question about a *group* of companies — "GLP-1 brands", "women's-health companies", "names from this list" — the answer can look more solid than it is. The fix is a short writing rule: every group answer opens with one line saying **what set was used, why, what it leaves out, and what kind of claim it's allowed to make.** No code, nothing running in the background. It pulls ~30 scattered cautions we've already learned into one habit an agent follows by default.

## The fields the process needs

- **risk:** low
- **write_scope:** Two existing files, words only. `QUERYING.md` gets one new section ("§0 The grouping stamp") before Recipe 1. `skills/query-companies/SKILL.md` gets one step plus one rule-bullet. No new files, no code, no schema changes, no `store/` writes.
- **spend_stop:** none. Nothing here scrapes or spends. Validation reads the store we already have (tokens, not credits). If checking it ever seems to need a capture, stop — scope has crept.
- **acceptance_checks:** Run four real group questions through the new rule (see below); each must come out honest, not just answered. Then confirm the rule text is in the docs and `/drift-sweep` runs clean.
- **escalate_if:** Stop and ask Brian if the fix starts needing a stored field, a checker that must keep running, or a 5th set-type to handle an edge case (the edge should resolve to "open question" instead).

## The problem in plain terms

Truffle began as one-company lookup. Now people ask it to compare groups, and two things go wrong:

- **The set is built wrong.** E.g. counting folders instead of real profiles, or a category filter quietly dropping companies that sell the thing but aren't tagged for it.
- **The set is fine but the answer over-claims.** "The GLP-1 companies we captured" quietly becomes "the GLP-1 market." "Names from two listicles" becomes "the whole market."

Both produce a clean-looking number with a hidden hole. We've hit these enough times that the lesson is settled: the fix is a convention, not new machinery.

**Why this is real, not hypothetical (checked today):** the store is clearly skewed — e.g. 17 men-leaning vs 5 women-leaning telehealth profiles. But the *rule* we write is the durable principle — "an answer built only from the store can't speak for the market; check for skew before claiming completeness" — not today's specific numbers. Baking in the snapshot would just rot.

## What we will NOT do

No defining "the market" for all time, no stored "group" objects, no forcing fuzzy questions into rigid fields, no machinery that has to keep running.

## The options we weighed

A workflow generated four shapes, simplest to boldest, and a critic tried to break each:

- **The grouping stamp** (simplest, words only) — **chosen.** Cleanest and most readable; the claim-table makes over-claiming literally un-writable.
- **Add a "weakest-link" rule** — *kept as an idea, not shipped.* Good rule (a set's claim is capped by its weakest part). Its companion lint was dropped — too brittle.
- **Add a small vocabulary for empty fields** — *kept as an idea.* Nails one real bug (an empty field read as "nobody does this"). Its extra file was dropped.
- **Build a helper script** — *declined for now.* ~250 lines of code whose only guarantee is "if you remember to run it" — no better than a rule you can skip, and the lab's whole history says don't.

## The recommendation

Ship the simplest shape, and fold the two good ideas from the bolder ones into it as plain text:

1. **Weakest-link rule** — the claim is set by how the set was *built*, never by the topic. Stops "a store search" from ever becoming "a market claim."
2. **Empty-field rule** — an empty field means "at least N", never "only N" or "the rest don't."
3. **Coverage principle** — the rule states a durable principle: an answer built only from the store can't speak for the market, so a completeness question gets a *"can't tell from the store"* instead of a fake percentage. A principle, not a dated snapshot — nothing to keep updating.

Skip the helper script. **Revisit only if** the rule ships and we still see ~2 of the next 10 group answers built wrong under a clean-looking stamp — that's the signal a tool is finally worth it.

## What the rule actually says

Every answer about more than one company opens with:

`Group: <name> · Set: <how built + count> · Leaves out: <blind spot> · Claim: <type>`

`<type>` comes from a fixed short list; it caps what the answer may say. If the question needs more than the type allows, the answer becomes **"open question"** — say what's missing instead of inventing a clean number.

| Set type | Built from | May say | Must not say |
|---|---|---|---|
| **store filter** | every profile matching a field filter | facts about the matched set | market coverage / share / ranking |
| **tag or keyword** | a tag or keyword cut | who's tagged that way | the tag = the real market; empty = absent |
| **outside list** | names from outside listicles | who's present/absent in our store | it's the whole market |
| **one-off set** | a hand-picked grouping | a dated, throwaway read | a durable or stored fact |

Each type carries a required caveat (e.g. store filter → "our coverage ≠ the market"). The mechanics of building sets correctly already live in Recipes 2/4/7/9 — this is just the honest label they all have to wear.

## How we'll know it works

Run four real questions; each must come out honest, not just answered:

- **"Which captured GLP-1 companies publish pricing?"** — must widen past the narrow tag and read empty pricing fields as "at least N", not "the rest hide it."
- **"How complete is our women's-health coverage?"** — must *refuse* a clean number and say coverage ≠ market.
- **"Finance: software sellers vs investors?"** — must park the in-between firms as "open question", not force them into one bucket.
- **"Which of these names are missing?"** — must say "not in our store", never "not in the market."

## Decisions

1. **Words-only, no tool — settled.** Ship the rule; revisit a tool only if answers keep coming out wrong under a clean header (the trigger above).
2. **Plain language — settled.** No coined umbrella term; the header line plus four plain labels (store filter / tag or keyword / outside list / one-off) carry it.
3. **Coverage caveat — settled: general principle.** State the durable principle ("a store-only answer can't speak for the market"), not today's specific skew — baking in the snapshot is exactly the overfitting and staleness this engine avoids.
