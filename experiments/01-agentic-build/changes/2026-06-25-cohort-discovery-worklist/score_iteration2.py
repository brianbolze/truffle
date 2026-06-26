#!/usr/bin/env python3
"""Score the second validation panel against frozen packet inputs.

The scorer deliberately measures only observable retrieval hits in raw tool output:
SERP organic/AIO/reference fields and Exa result titles/domains. It does not decide
whether a net-new candidate should be Tier A/B; that remains a human-verification
receipt because precision depends on cohort membership and source quality.
"""

from __future__ import annotations

import argparse
import copy
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

PACKET = Path(__file__).resolve().parent
RAW_DIR = PACKET / "receipts" / "raw" / "iteration-2"
TELEHEALTH_INPUT = PACKET / "validation-inputs" / "telehealth-holdouts.json"
CI_INPUT = PACKET / "validation-inputs" / "conversation-intelligence-targets.json"

TELEHEALTH_ALIASES: dict[str, list[str]] = {
    "Hims & Hers": ["hims", "hims & hers", "hims.com"],
    "LifeMD": ["lifemd", "lifemd.com", "life md"],
    "Niagen Plus": ["niagen plus", "niagenplus", "niagenplus.com"],
    "One Medical (Amazon)": ["one medical", "amazon one medical", "onemedical.com"],
    "Rex MD": ["rex md", "rexmd", "rexmd.com"],
    "Wisp": ["wisp", "hellowisp", "hellowisp.com"],
    "Eden": ["eden.health", "tryeden"],
    "Hone Health": ["hone health", "honehealth", "honehealth.com"],
    "Lifeforce": ["lifeforce", "mylifeforce", "mylifeforce.com"],
    "Noom Med": ["noom", "noom med", "noom.com/med"],
    "Peter MD": ["peter md", "petermd", "getpetermd.com"],
    "Remedy Meds": ["remedy meds", "remedymeds", "remedymeds.com"],
    "Ro": ["ro.co", "roman", "ro body"],
    "AgelessRx": ["agelessrx", "ageless rx", "agelessrx.com"],
    "Amble": ["amble", "joinamble", "joinamble.com"],
    "Blokes": ["blokes", "joi and blokes", "joiandblokes.com"],
    "BlueChew": ["bluechew", "blue chew", "bluechew.com"],
    "Defy Medical": ["defy medical", "defymedical.com"],
    "Fridays": ["fridays", "joinfridays", "fridays health", "joinfridays.com"],
    "Geviti": ["geviti", "gogeviti", "gogeviti.com"],
    "Invigor Medical": ["invigor medical", "invigormedical.com"],
    "Ivy Rx": ["ivy rx", "ivyrx", "ivyrx.com"],
    "Kingsberg Medical": ["kingsberg medical", "kingsbergmedical.com"],
    "Marek Health": ["marek health", "marekhealth.com"],
    "Maximus Tribe": ["maximus tribe", "maximus", "maximustribe.com"],
    "Nurx": ["nurx", "nurx.com"],
    "ProHealth": ["prohealth", "prohealth.com"],
    "Rugiet Ready": ["rugiet", "rugiet ready", "rugiet.com"],
}

CI_STORE_BASELINE_HITS = {
    "Gong",
    "Clari",
    "Granola AI",
    "Dovetail",
    "AlphaSense",
}

CI_ALIASES: dict[str, list[str]] = {
    "Gong": ["gong", "gong.io"],
    "Clari": ["clari", "clari.com"],
    "Loom": ["loom", "loom.com"],
    "Otter": ["otter", "otter.ai"],
    "Granola AI": ["granola", "granola ai", "granola.ai"],
    "Dovetail": ["dovetail", "dovetail.com"],
    "Zoom AI Companion": ["zoom ai companion", "zoom companion", "zoom"],
    "Microsoft Copilot for Teams": ["microsoft copilot", "copilot for teams", "teams copilot"],
    "AlphaSense": ["alphasense", "alpha sense"],
    "Fathom AI": ["fathom", "fathom ai", "fathom.video"],
    "Notion AI Meeting Notes": ["notion ai meeting notes", "notion meeting notes", "notion ai"],
    "OpenAI Whisper": ["openai whisper", "whisper"],
    "ChatGPT transcript workflow": ["chatgpt transcript", "chatgpt"],
    "Claude transcript workflow": ["claude transcript", "claude"],
    "Rewind": ["rewind", "rewind.ai"],
    "Apple Voice Memos": ["apple voice memos", "voice memos"],
    "Jamie AI": ["jamie ai", "meetjamie", "jamie"],
    "Rev": ["rev", "rev.com"],
    "Deepgram": ["deepgram", "deepgram.com"],
    "ElevenLabs": ["elevenlabs", "eleven labs"],
    "AWS Transcribe": ["aws transcribe", "amazon transcribe"],
    "AssemblyAI": ["assemblyai", "assembly ai"],
    "Nuance": ["nuance", "nuance.com"],
    "Verbit": ["verbit", "verbit.ai"],
    "Descript": ["descript", "descript.com"],
    "Symbl.ai": ["symbl.ai", "symbl"],
}


def load_json(path: Path) -> Any:
    """Load a JSON document with UTF-8 explicitly."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def norm(text: str) -> str:
    """Normalize text for loose brand/domain matching."""
    return re.sub(r"\s+", " ", text.lower())


def alias_pattern(alias: str) -> re.Pattern[str]:
    """Compile a conservative alias matcher with word-ish boundaries."""
    escaped = re.escape(alias.lower())
    if len(alias) <= 3 and "." not in alias:
        return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])")
    return re.compile(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])")


def collect_serpapi_text(data: dict[str, Any]) -> str:
    """Extract only result/source fields from a SerpAPI envelope, excluding input query text."""
    chunks: list[str] = []
    for item in data.get("organic_results", []):
        chunks.extend(str(item.get(key) or "") for key in ("title", "link", "snippet", "displayed_link"))
    for item in data.get("ranked_brands", []):
        chunks.extend(str(item.get(key) or "") for key in ("label", "after_colon", "raw_snippet"))
    chunks.extend(str(value) for value in data.get("narrative_paragraphs", []))
    chunks.extend(str(value) for value in data.get("headings", []))
    for item in data.get("references", []):
        chunks.extend(str(item.get(key) or "") for key in ("title", "source", "link"))
    return norm(" ".join(chunks))


def collect_exa_text(data: dict[str, Any]) -> str:
    """Extract only result fields from an Exa envelope, excluding input query text."""
    chunks: list[str] = []
    for item in data.get("results", []):
        chunks.extend(str(item.get(key) or "") for key in ("title", "url", "domain"))
    return norm(" ".join(chunks))


def raw_text_for(row: dict[str, Any]) -> str:
    """Load and extract matchable text for one query-panel row."""
    folder = "serpapi" if row["tool"] == "serpapi" else "exa"
    data = load_json(RAW_DIR / folder / f"{row['id']}.json")
    if row["tool"] == "serpapi":
        return collect_serpapi_text(data)
    if row["tool"] == "exa_search":
        return collect_exa_text(data)
    return ""


def find_aliases(text: str, aliases: list[str]) -> list[str]:
    """Return aliases observed in a normalized text blob."""
    found = []
    for alias in aliases:
        if alias_pattern(alias).search(text):
            found.append(alias)
    return found


def score_targets(
    rows: list[dict[str, Any]],
    targets: list[dict[str, Any]],
    alias_map: dict[str, list[str]],
    cohort: str,
) -> dict[str, Any]:
    """Score target retrieval by row and feeder for one cohort."""
    cohort_rows = [row for row in rows if row["cohort"] == cohort]
    text_by_row = {row["id"]: raw_text_for(row) for row in cohort_rows}
    target_results = []
    feeder_hits: dict[str, set[str]] = defaultdict(set)
    row_hits: dict[str, set[str]] = defaultdict(set)

    for target in targets:
        name = target["name"]
        aliases = alias_map.get(name, [name])
        hit_rows = []
        matched_aliases: dict[str, list[str]] = {}
        for row in cohort_rows:
            found = find_aliases(text_by_row[row["id"]], aliases)
            if not found:
                continue
            hit_rows.append(row["id"])
            matched_aliases[row["id"]] = found
            feeder_hits[row["feeder"]].add(name)
            row_hits[row["id"]].add(name)
        target_results.append(
            {
                **target,
                "hit": bool(hit_rows),
                "hit_rows": hit_rows,
                "matched_aliases": matched_aliases,
            }
        )

    return {
        "targets": target_results,
        "feeder_hits": {feeder: sorted(names) for feeder, names in sorted(feeder_hits.items())},
        "row_hits": {row_id: sorted(names) for row_id, names in sorted(row_hits.items())},
    }


def summarize_telehealth(scored: dict[str, Any]) -> dict[str, Any]:
    """Summarize telehealth must-hit and should-hit retrieval."""
    targets = scored["targets"]
    must = [target for target in targets if target["gate"] == "must_hit"]
    should = [target for target in targets if target["gate"] == "should_hit"]
    return {
        "must_hit": {
            "hit": sum(1 for target in must if target["hit"]),
            "total": len(must),
            "misses": [target["name"] for target in must if not target["hit"]],
        },
        "should_hit": {
            "hit": sum(1 for target in should if target["hit"]),
            "total": len(should),
            "misses": [target["name"] for target in should if not target["hit"]],
        },
    }


def summarize_conversation(scored: dict[str, Any], adjacent_names: set[str]) -> dict[str, Any]:
    """Summarize conversation-intelligence top-10 and adjacent retrieval."""
    core = [target for target in scored["targets"] if target.get("kind") == "core"]
    adjacent = [target for target in scored["targets"] if target["name"] in adjacent_names]
    top10 = [target for target in core if target["rank"] <= 10]
    return {
        "top_10": {
            "hit": sum(1 for target in top10 if target["hit"]),
            "total": len(top10),
            "misses": [target["name"] for target in top10 if not target["hit"]],
        },
        "core_all": {
            "hit": sum(1 for target in core if target["hit"]),
            "total": len(core),
            "misses": [target["name"] for target in core if not target["hit"]],
        },
        "adjacent_observed": [target["name"] for target in adjacent if target["hit"]],
    }


def add_conversation_store_baseline(scored: dict[str, Any]) -> dict[str, Any]:
    """Return a copy of CI scoring with known store-baseline company hits applied.

    This intentionally adds only company/profile hits from the existing receipt's
    local-store baseline. Product/workflow rows such as Notion AI Meeting Notes,
    OpenAI Whisper, ChatGPT transcript workflow, and Apple Voice Memos remain
    boundary cases rather than automatic company-discovery hits.
    """
    with_store = copy.deepcopy(scored)
    for target in with_store["targets"]:
        if target["name"] not in CI_STORE_BASELINE_HITS:
            continue
        target["hit"] = True
        if "store_baseline" not in target["hit_rows"]:
            target["hit_rows"].append("store_baseline")
        target["matched_aliases"]["store_baseline"] = ["local store profile"]
    with_store["feeder_hits"]["store_baseline"] = sorted(CI_STORE_BASELINE_HITS)
    with_store["row_hits"]["store_baseline"] = sorted(CI_STORE_BASELINE_HITS)
    return with_store


def main() -> None:
    parser = argparse.ArgumentParser(description="Score iteration-2 raw outputs against frozen validation inputs.")
    parser.add_argument("--output", default=str(RAW_DIR / "score-summary.json"))
    args = parser.parse_args()

    rows = load_json(RAW_DIR / "query-panel.json")
    telehealth_inputs = load_json(TELEHEALTH_INPUT)
    ci_inputs = load_json(CI_INPUT)

    telehealth_scored = score_targets(rows, telehealth_inputs["holdouts"], TELEHEALTH_ALIASES, "telehealth")
    ci_core = [{**target, "kind": "core"} for target in ci_inputs["core_ranked"]]
    ci_adjacent = [{**target, "kind": "adjacent"} for target in ci_inputs["adjacent_transcription_dev_tools"]]
    ci_scored = score_targets(rows, ci_core + ci_adjacent, CI_ALIASES, "conversation_intelligence")
    ci_store_first_scored = add_conversation_store_baseline(ci_scored)

    adjacent_names = {target["name"] for target in ci_inputs["adjacent_transcription_dev_tools"]}
    ci_external_summary = summarize_conversation(ci_scored, adjacent_names)
    ci_store_first_summary = summarize_conversation(ci_store_first_scored, adjacent_names)
    summary = {
        "inputs": {
            "telehealth": str(TELEHEALTH_INPUT.relative_to(PACKET)),
            "conversation_intelligence": str(CI_INPUT.relative_to(PACKET)),
            "raw_dir": str(RAW_DIR.relative_to(PACKET)),
        },
        "limits": "Retrieval scoring only; excludes input query text and does not verify candidate precision.",
        "telehealth": {
            **summarize_telehealth(telehealth_scored),
            "feeder_hits": telehealth_scored["feeder_hits"],
            "row_hits": telehealth_scored["row_hits"],
            "targets": telehealth_scored["targets"],
        },
        "conversation_intelligence": {
            "external_only": ci_external_summary,
            "store_first": ci_store_first_summary,
            "store_baseline_hits": sorted(CI_STORE_BASELINE_HITS),
            "feeder_hits": ci_store_first_scored["feeder_hits"],
            "row_hits": ci_store_first_scored["row_hits"],
            "targets": ci_store_first_scored["targets"],
        },
    }

    output = Path(args.output)
    output.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
