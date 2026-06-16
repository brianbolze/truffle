#!/usr/bin/env python3
"""visualcheck — lint an opt-in `visual.md` against the module contract (modules/VISUAL.md).

`visual.md` is the per-company visual-evidence layer: blind, cited cards + a prose impression,
and *no score* — scoring failed calibration through v5 and stays parked. The load-bearing rule
this script makes mechanical is exactly that boundary: a `score:`/`rating:` field (or an `N/5`
quality figure) anywhere in the file fails the lint. The rest assert the cards stay falsifiable
and cited — every card points at a tile that exists, carries a visible tell, and the prose
impression is a lens over those cards rather than fresh assertion.

  1. no score, ever      — no `score:`/`rating:`/`quality:` field, no `N/5`/`N/10`, no PQR scale.
  2. tile paths active    — every `tile_path`/`contrast_with` exists on disk under a `tiles/` dir.
  3. falsifiable          — every card has a non-empty claim and >=1 visible_tell.
  4. closed sets          — family / polarity / confidence / qa_status hold contract values.
  5. impression is a lens — the impression section is present and cites >=1 real card id.
  6. structural           — frontmatter keys + both body sections present; no leaked tool tags.

Per-file by design (`--slug functionhealth-com`): the workflow's verifier runs it on one draft.
No `--slug` lints every `store/*/visual.md`. Exit 0 = the contract holds; nonzero prints how it
broke. Stdlib-only on purpose (matches offeringscheck / cohortcheck) — no PyYAML.

CLI:  python3 scripts/visualcheck.py [--slug <slug>]
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import sys

from storelint import leaked_tags  # shared, schema-independent guard

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORE = os.path.join(ROOT, "store")

FAMILIES = {"typography_hierarchy", "layout_composition_components",
            "color_brand_imagery", "iconography_illustration"}
POLARITIES = {"strong", "mixed", "poor"}
CONFIDENCES = {"high", "medium", "low"}
QA_STATUS = {"clean", "exclusions-noted", "recapture-used"}
REQUIRED_FM = ["schema_version", "domain", "captured_at", "source_capture", "qa_status"]

# Rule 1 — the parked-score guard. Each pattern is a way a quality score sneaks back in.
SCORE_PATTERNS = [
    (re.compile(r"(?mi)^\s*(score|rating|quality|visual_quality|overall_visual_quality|pqr[_a-z]*)\s*:"),
     "forbidden score/rating field"),
    (re.compile(r"(?<![\d./])([1-9]|10)\s*/\s*(5|10)\b"), "forbidden N/5 or N/10 quality figure"),
    (re.compile(r"(?i)\b(pqr-?lite|1\s*-\s*5 scale|1\s*-\s*10 scale)\b"), "forbidden scoring-scale reference"),
]


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Top-level frontmatter as a flat dict (stdlib scan). None if no leading '---' fence."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm: dict[str, str] = {}
    for line in text[3:end].splitlines():
        match = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if match:
            val = re.sub(r"\s+#.*$", "", match.group(2).strip())  # drop an inline YAML comment
            fm[match.group(1)] = val.strip().strip('"').strip("'")
    return fm


def section(text: str, heading: str) -> str | None:
    """The body of a `## heading` section (up to the next `## `), or None if absent."""
    head = re.search(r"(?m)^##\s+" + re.escape(heading) + r"\s*$", text)
    if not head:
        return None
    rest = text[head.end():]
    nxt = re.search(r"(?m)^##\s+", rest)
    return rest[: nxt.start()] if nxt else rest


def cards_in(cards_section: str) -> list[tuple[str, str]]:
    """(card_id, card_block) for each `- id:` entry in the evidence-cards section (fence-agnostic)."""
    starts = list(re.finditer(r"(?m)^- id:[ \t]*(\S+)", cards_section))
    out = []
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(cards_section)
        # strip quotes so a scripted `id: 'typography_01'` still matches the impression's [typography_01]
        out.append((match.group(1).strip("\"'"), cards_section[match.start():end]))
    return out


def field(block: str, key: str) -> str | None:
    """A scalar `key: value` from a card block, unquoted; None if absent."""
    match = re.search(r"(?m)^\s*" + re.escape(key) + r":\s*(.+)$", block)
    return match.group(1).strip().strip('"').strip("'") if match else None


def tells_count(block: str) -> int:
    """Number of list items under this card's `visible_tells:`."""
    pivot = block.find("visible_tells:")
    if pivot < 0:
        return 0
    return len(re.findall(r"(?m)^[ \t]+-[ \t]+\S", block[pivot:]))


def check(path: str) -> list[str]:
    """Return the contract violations in one visual.md (empty = passes)."""
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    errors: list[str] = []
    rel = os.path.relpath(path, ROOT)

    # 1 — no score, ever
    for pattern, label in SCORE_PATTERNS:
        hit = pattern.search(text)
        if hit:
            line = text[: hit.start()].count("\n") + 1
            errors.append(f"{rel}:{line}: {label} — `{hit.group(0).strip()}` (the score stays parked)")

    fm = parse_frontmatter(text)
    if fm is None:
        return errors + [f"{rel}: missing frontmatter fence"]

    # 6 — structural (frontmatter + sections + leaked tags)
    for key in REQUIRED_FM:
        if key not in fm:
            errors.append(f"{rel}: frontmatter missing `{key}`")
    if fm.get("qa_status") and fm["qa_status"] not in QA_STATUS:
        errors.append(f"{rel}: qa_status `{fm['qa_status']}` not in {sorted(QA_STATUS)}")
    impression = section(text, "Visual & brand impression")
    cards_section = section(text, "Evidence cards")
    if impression is None:
        errors.append(f"{rel}: missing `## Visual & brand impression`")
    if cards_section is None:
        return errors + [f"{rel}: missing `## Evidence cards`"]
    for tag in leaked_tags(text):
        errors.append(f"{rel}: leaked tool-call tag `{tag}`")

    cards = cards_in(cards_section)
    if not cards:
        errors.append(f"{rel}: no evidence cards found")
    card_ids = {cid for cid, _ in cards}

    for cid, block in cards:
        # 4 — closed sets
        fam, pol, conf = field(block, "family"), field(block, "polarity"), field(block, "confidence")
        if fam not in FAMILIES:
            errors.append(f"{rel}: card {cid}: family `{fam}` not in the four families")
        if pol not in POLARITIES:
            errors.append(f"{rel}: card {cid}: polarity `{pol}` not in {sorted(POLARITIES)}")
        if conf not in CONFIDENCES:
            errors.append(f"{rel}: card {cid}: confidence `{conf}` not in {sorted(CONFIDENCES)}")
        # 3 — falsifiable
        if not field(block, "claim"):
            errors.append(f"{rel}: card {cid}: empty or missing claim")
        if tells_count(block) < 1:
            errors.append(f"{rel}: card {cid}: needs >=1 visible_tell")
        # 2 — tile paths active
        tpath = field(block, "tile_path")
        for key in ("tile_path", "contrast_with"):
            val = field(block, key)
            if key == "contrast_with" and not val:
                continue
            if not val:
                errors.append(f"{rel}: card {cid}: missing tile_path")
                continue
            if "/tiles/" not in val:
                errors.append(f"{rel}: card {cid}: {key} `{val}` is not under a tiles/ dir")
            if not os.path.exists(os.path.join(ROOT, val)):
                errors.append(f"{rel}: card {cid}: {key} `{val}` does not exist on disk")
            if key == "contrast_with" and val == tpath:
                errors.append(f"{rel}: card {cid}: contrast_with points at its own tile_path (no contrast)")

    # 5 — impression is a lens (cites >=1 real card id)
    if impression is not None:
        cited = set(re.findall(r"\[([a-z0-9_]+)\]", impression))
        if not (cited & card_ids):
            errors.append(f"{rel}: impression cites no card id (must be a lens over the cards)")

    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description="Lint visual.md against modules/VISUAL.md.")
    parser.add_argument("--slug", help="one store slug; omit to lint every store/*/visual.md")
    args = parser.parse_args()

    if args.slug:
        paths = [os.path.join(STORE, args.slug, "visual.md")]
    else:
        paths = sorted(glob.glob(os.path.join(STORE, "*", "visual.md")))
    if not paths or (args.slug and not os.path.exists(paths[0])):
        raise SystemExit(f"no visual.md to lint{' for ' + args.slug if args.slug else ''}")

    failures = 0
    for path in paths:
        errors = check(path)
        if errors:
            failures += 1
            print("\n".join(errors))
    if failures:
        print(f"\nvisualcheck: {failures} file(s) failed")
        sys.exit(1)
    print(f"visualcheck: {len(paths)} file(s) OK")


if __name__ == "__main__":
    main()
