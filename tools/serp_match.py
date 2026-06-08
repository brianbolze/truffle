#!/usr/bin/env python3
"""SERP matching consumer — applies `_match.py` to a captured `serpapi.py` envelope.

`serpapi.py` stays raw: it fetches Google and emits organic/AIO signal without cohort judgment. This
consumer is a small manual bridge for SERP callers that need the standard domain+text
classification: which cohort members appear, where, and whether each hit is their own page or a
mention.

Do not copy this file into `exa_match.py`, `wayback_match.py`, etc. That wrapper-per-source shape
would clutter `tools/` and blur the capture/judgment boundary. Repeated SERP query panels now live
in `serp_intent_panel.py`; keep `_match.py` as the shared importable core.

Input is intentionally boring JSON:

    python3 tools/serpapi.py "Ro Hims comparison" --organic-only > serp.json
    python3 tools/serp_match.py serp.json --cohort cohort.json
    cat serp.json | python3 tools/serp_match.py --cohort cohort.json

`cohort.json` can be either a list of `{slug, domain, aliases?, disambiguate_regex?}` objects or an
object with `cohort` / `brands` holding that list. This script is a consumer helper, not a capture
tool, so the capture-tool envelope and exit-code conventions do not apply.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from typing import Any

from _match import TextMode, match_output


def _load_json(path: str | None) -> Any:
    """JSON from `path`, or stdin when `path` is absent / '-'."""
    if not path or path == "-":
        return json.load(sys.stdin)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_cohort(path: str) -> list[Mapping[str, Any]]:
    """The plain cohort list, accepting a bare list or `{cohort|brands: [...]}` wrapper."""
    raw = _load_json(path)
    if isinstance(raw, list):
        cohort = raw
    elif isinstance(raw, Mapping) and isinstance(raw.get("cohort"), list):
        cohort = raw["cohort"]
    elif isinstance(raw, Mapping) and isinstance(raw.get("brands"), list):
        cohort = raw["brands"]
    else:
        raise ValueError("cohort JSON must be a list, or an object with a list at 'cohort' or 'brands'")
    if not all(isinstance(member, Mapping) for member in cohort):
        raise ValueError("cohort entries must be objects")
    return cohort


def _serpapi_payloads(matches: Sequence[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    """SERP rows only; `_match.match_output` may grow more payload routers over time."""
    return [match for match in matches if (match.get("where") or {}).get("payload") in {"ranked_brands", "organic_results"}]


def match_serpapi_output(
    output: Mapping[str, Any], cohort: Sequence[Mapping[str, Any]], text_mode: TextMode = "cohort_context"
) -> dict[str, Any]:
    """The importable caller: SerpAPI envelope + cohort -> a small match report."""
    matches = _serpapi_payloads(match_output(output, cohort, text_mode=text_mode))
    return {
        "source_tool": output.get("tool"),
        "input": output.get("input"),
        "match_count": len(matches),
        "matches": matches,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("serpapi_json", nargs="?", help="Captured serpapi.py JSON envelope; reads stdin when omitted or '-'")
    parser.add_argument("--cohort", required=True, help="JSON cohort list, or object with `cohort` / `brands` list")
    parser.add_argument(
        "--text-mode",
        choices=["cohort_context", "open_text"],
        default="cohort_context",
        help="Text matching mode for title/snippet and ranked-brand text (default: cohort_context)",
    )
    args = parser.parse_args()

    try:
        output = _load_json(args.serpapi_json)
        cohort = _load_cohort(args.cohort)
        if not isinstance(output, Mapping):
            raise ValueError("serpapi JSON must be an object")
        result = match_serpapi_output(output, cohort, text_mode=args.text_mode)
    except Exception as e:
        sys.stderr.write(f"serp_match: {e}\n")
        sys.exit(2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
