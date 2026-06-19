# Commit style

`scope: lowercase imperative subject` — a **short** prefix at the start, kept glanceable (e.g. `store:`, `docs:`, `query:`). Detail goes in the **body** (blank line after the subject): rationale, what you rejected, validation steps, trailers. Trivial commits can skip the body.

Reuse a scope you already see in `git log` where one fits; coin a new short one only when none do. Don't reword commits already pushed to `origin`.

## Example

    query: simplify company suggestions — drop rapidfuzz, ungate substring path

    Address review of the fuzzy-suggestion change:
    - Drop the rapidfuzz dependency; difflib scores identically on these keys.
    - Restore the substring-candidate path in _miss_line (the >=5-char gate
      had throttled exact substrings); adds a regression test.
    Validation: ruff check; pytest (19 passed).
