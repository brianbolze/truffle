#!/usr/bin/env python3
"""Scaffold a numbered Market Read Lab run."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

RUN_RE = re.compile(r"^(\d{3})-")
TEMPLATE_FILES = [
    "read.md",
    "run-notes.md",
    "consumer-review.md",
    "developer-review.md",
]
EVIDENCE_MODES = ("store-only", "local-existing", "bounded-live", "live-external-needs-approval")
EVIDENCE_MODE_HINT = "/".join(EVIDENCE_MODES)
DEFAULT_LOCAL_DISALLOWED_ACTIONS = [
    "live browsing",
    "paid capture",
    "broad external research",
    "write-back to store/",
    "new durable primitives",
    "triage graduation",
]
DEFAULT_BOUNDED_LIVE_DISALLOWED_ACTIONS = [
    "write-back to store/",
    "code, schema, or template changes",
    "durable primitive creation",
    "triage graduation",
]
DEFAULT_LIVE_SOURCE_FAMILIES_DISALLOWED = [
    "login-only or paywalled sources",
    "broad crawling",
    "private / non-public data",
]
DEFAULT_BOUNDED_LIVE_STOP_WHEN = [
    "the source panel is good enough to answer with visible caveats",
    "the next source would expand the question rather than verify it",
    "the remaining uncertainty is a framing judgment, not a sourcing gap",
    "sources conflict in a way that needs human interpretation",
]


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "experiments/00-market-read-lab/templates").is_dir():
            return parent
    raise SystemExit("Could not find experiments/00-market-read-lab/templates from script path.")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80].strip("-") or "market-read"


def next_run_number(runs_dir: Path) -> int:
    seen: list[int] = []
    if runs_dir.exists():
        for child in runs_dir.iterdir():
            if child.is_dir():
                match = RUN_RE.match(child.name)
                if match:
                    seen.append(int(match.group(1)))
    return max(seen, default=-1) + 1


def escape_table_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def escape_yaml_string(value: str) -> str:
    return "'" + value.replace("'", "''").replace("\n", " ") + "'"


def format_yaml_list(values: list[str]) -> str:
    return "[" + ", ".join(escape_yaml_string(value) for value in values) + "]"


def format_yaml_sequence(key: str, values: list[str], *, indent: int = 2) -> list[str]:
    spaces = " " * indent
    if not values:
        return [f"{spaces}{key}: []"]
    lines = [f"{spaces}{key}:"]
    lines.extend(f"{spaces}  - {escape_yaml_string(value)}" for value in values)
    return lines


def format_live_evidence_plan(plan: dict[str, object] | None) -> str:
    if not plan:
        return "live_evidence_plan: null"

    lines = [
        "live_evidence_plan:",
        f"  approved_by: {escape_yaml_string(str(plan['approved_by']))}",
        f"  approval_scope: {escape_yaml_string(str(plan['approval_scope']))}",
        f"  budget_class: {escape_yaml_string(str(plan['budget_class']))}",
        f"  review_after: {escape_yaml_string(str(plan['review_after']))}",
        f"  evidence_goal: {escape_yaml_string(str(plan['evidence_goal']))}",
    ]
    for key in (
        "source_families_allowed",
        "source_families_preferred",
        "source_families_disallowed",
        "stop_when",
    ):
        values = [str(value) for value in plan[key]]
        lines.extend(format_yaml_sequence(key, values, indent=2))
    return "\n".join(lines)


def default_disallowed_actions(evidence_mode: str) -> list[str]:
    if evidence_mode == "bounded-live":
        return DEFAULT_BOUNDED_LIVE_DISALLOWED_ACTIONS.copy()
    return DEFAULT_LOCAL_DISALLOWED_ACTIONS.copy()


def seeded_scout(
    template: str,
    question: str | None,
    contract: dict[str, object] | None,
    *,
    selected_slug: str | None = None,
) -> str:
    if not question:
        return template

    if contract:
        table_row = (
            f"| {escape_table_cell(question)} | {contract['run_type']} | yes | "
            f"{contract['evidence_mode']} | Selected by operator; see Selected Run Contract. | "
            f"Allowed sources: {escape_table_cell(', '.join(contract['allowed_sources']))} | "
            f"{escape_table_cell(str(contract['loop1_failure_mode']))} |"
        )
    else:
        table_row = (
            f"| {escape_table_cell(question)} | mixed | yes/no | {EVIDENCE_MODE_HINT} | TODO | TODO | TODO |"
        )
    scout = template.replace(
        f"|  | market/system-test/mixed | yes/no | {EVIDENCE_MODE_HINT} |  |  |  |",
        table_row,
    )
    scout = scout.replace("1. \n\nThese may", f"1. {question}\n\nThese may", 1)
    scout = scout.replace("selected_question:\n", f"selected_question: {escape_yaml_string(question)}\n", 1)
    scout = scout.replace("selected_slug:          # short kebab-case folder slug, e.g. telehealth-category-crowdedness\n", f"selected_slug: {escape_yaml_string(selected_slug or slugify(question))}\n", 1)
    scout = scout.replace("selected_slug:          # 3-5 word kebab-case folder slug, e.g. telehealth-category-crowdedness\n", f"selected_slug: {escape_yaml_string(selected_slug or slugify(question))}\n", 1)
    if contract:
        replacements = {
            "run_type:              # market | system-test | mixed": f"run_type: {contract['run_type']}",
            "autonomous_eligible:   # yes | no": "autonomous_eligible: yes",
            "evidence_mode:         # store-only | local-existing | bounded-live | live-external-needs-approval": f"evidence_mode: {contract['evidence_mode']}",
            "expected_denominator:": f"expected_denominator: {escape_yaml_string(str(contract['expected_denominator']))}",
            "likely_source_panel:": f"likely_source_panel: {escape_yaml_string(str(contract['likely_source_panel']))}",
            "allowed_sources: []": f"allowed_sources: {format_yaml_list(contract['allowed_sources'])}",
            "disallowed_actions: []": f"disallowed_actions: {format_yaml_list(contract['disallowed_actions'])}",
            "live_evidence_plan: null  # required only for bounded-live": format_live_evidence_plan(contract.get("live_evidence_plan")),
            "approval_needed:       # yes | no": "approval_needed: no",
            "why_autonomous_safe:": f"why_autonomous_safe: {escape_yaml_string(str(contract['why_autonomous_safe']))}",
            "loop1_failure_mode:": f"loop1_failure_mode: {escape_yaml_string(str(contract['loop1_failure_mode']))}",
        }
        for old, new in replacements.items():
            scout = scout.replace(old, new, 1)
    scout += (
        "\n\n## Bootstrap Notes\n\n"
        "- Created by `.claude/skills/market-read-lab/scripts/new_run.py`.\n"
        "- Edit the candidate row and Selected Run Contract before running Loop 1 if the question needs sharper scope.\n"
    )
    return scout


def rendered_run_notes(
    template: str,
    *,
    run_status: str = "",
    evidence_mode: str = "",
    autonomous_eligible: str = "",
    termination_reason: str = "",
) -> str:
    header = "\n".join(
        [
            "```yaml",
            f"run_status: {run_status}".rstrip(),
            f"evidence_mode: {evidence_mode}".rstrip(),
            f"autonomous_eligible: {autonomous_eligible}".rstrip(),
            f"termination_reason: {termination_reason}".rstrip(),
            "pressure_lenses_fired: []",
            "```",
        ]
    )
    return re.sub(r"```yaml\n.*?\n```", header, template, count=1, flags=re.S)


def render_loop_prompt(template_text: str, run_rel: str) -> str:
    return template_text.replace(
        "`experiments/00-market-read-lab/runs/NNN-YYYY-MM-DD-short-slug`",
        f"`{run_rel}`",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True, help="Short run slug, e.g. backend-relations")
    parser.add_argument("--question", help="Optional selected question to seed into scout.md")
    parser.add_argument("--date", help="Run date, YYYY-MM-DD. Defaults to today.")
    parser.add_argument("--run-type", choices=("market", "system-test", "mixed"), default="mixed")
    parser.add_argument(
        "--evidence-mode",
        choices=EVIDENCE_MODES,
        help="Required for --mode loop1.",
    )
    parser.add_argument("--expected-denominator", help="Required for --mode loop1.")
    parser.add_argument("--likely-source-panel", help="Source panel summary for the selected run contract.")
    parser.add_argument("--allowed-source", action="append", dest="allowed_sources", help="Allowed source/path. Repeatable.")
    parser.add_argument(
        "--disallowed-action",
        action="append",
        dest="disallowed_actions",
        help="Disallowed action. Repeatable. Defaults depend on the evidence mode.",
    )
    parser.add_argument("--why-autonomous-safe", help="Required for --mode loop1.")
    parser.add_argument("--loop1-failure-mode", help="Required for --mode loop1.")
    parser.add_argument("--live-evidence-goal", help="Required when --evidence-mode bounded-live.")
    parser.add_argument(
        "--source-family-allowed",
        action="append",
        dest="source_families_allowed",
        help="Allowed live source family for bounded-live. Repeatable.",
    )
    parser.add_argument(
        "--source-family-preferred",
        action="append",
        dest="source_families_preferred",
        help="Preferred live source family for bounded-live. Repeatable.",
    )
    parser.add_argument(
        "--source-family-disallowed",
        action="append",
        dest="source_families_disallowed",
        help="Disallowed live source family for bounded-live. Repeatable.",
    )
    parser.add_argument(
        "--stop-when",
        action="append",
        dest="stop_when",
        help="Stop rule for bounded-live. Repeatable; defaults to the lab stop rules.",
    )
    parser.add_argument(
        "--mode",
        choices=("scout", "loop1"),
        default="scout",
        help="Prompt to print after scaffolding. Defaults to scout.",
    )
    args = parser.parse_args()

    run_date = args.date or dt.date.today().isoformat()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", run_date):
        raise SystemExit("--date must be YYYY-MM-DD")

    contract: dict[str, object] | None = None
    if args.mode == "loop1":
        missing = []
        if not args.question:
            missing.append("--question")
        if not args.evidence_mode:
            missing.append("--evidence-mode")
        if not args.expected_denominator:
            missing.append("--expected-denominator")
        if not args.allowed_sources:
            missing.append("--allowed-source")
        if not args.why_autonomous_safe:
            missing.append("--why-autonomous-safe")
        if not args.loop1_failure_mode:
            missing.append("--loop1-failure-mode")
        if missing:
            raise SystemExit(
                "--mode loop1 requires a contract-ready scaffold. Missing: "
                + ", ".join(missing)
                + ". Use --mode scout if Scout should fill the contract."
            )
        if args.evidence_mode == "live-external-needs-approval":
            raise SystemExit("--mode loop1 cannot use live-external-needs-approval; run Scout or get approval first.")
        live_evidence_plan: dict[str, object] | None = None
        if args.evidence_mode == "bounded-live":
            if not args.live_evidence_goal:
                missing.append("--live-evidence-goal")
            if not args.source_families_allowed:
                missing.append("--source-family-allowed")
            if missing:
                raise SystemExit(
                    "--mode loop1 with --evidence-mode bounded-live requires a live evidence plan. Missing: "
                    + ", ".join(missing)
                )
            live_evidence_plan = {
                "approved_by": "Brian",
                "approval_scope": "autonomous Market Read Lab runs",
                "budget_class": "light",
                "review_after": "3 bounded-live runs",
                "evidence_goal": args.live_evidence_goal,
                "source_families_allowed": args.source_families_allowed,
                "source_families_preferred": args.source_families_preferred or [],
                "source_families_disallowed": args.source_families_disallowed
                or DEFAULT_LIVE_SOURCE_FAMILIES_DISALLOWED,
                "stop_when": args.stop_when or DEFAULT_BOUNDED_LIVE_STOP_WHEN,
            }
        contract = {
            "run_type": args.run_type,
            "evidence_mode": args.evidence_mode,
            "expected_denominator": args.expected_denominator,
            "likely_source_panel": args.likely_source_panel or "Allowed sources only.",
            "allowed_sources": args.allowed_sources,
            "disallowed_actions": args.disallowed_actions or default_disallowed_actions(args.evidence_mode),
            "live_evidence_plan": live_evidence_plan,
            "why_autonomous_safe": args.why_autonomous_safe,
            "loop1_failure_mode": args.loop1_failure_mode,
        }

    root = find_repo_root()
    lab_dir = root / "experiments/00-market-read-lab"
    templates_dir = lab_dir / "templates"
    runs_dir = lab_dir / "runs"

    run_num = next_run_number(runs_dir)
    run_name = f"{run_num:03d}-{run_date}-{slugify(args.slug)}"
    run_dir = runs_dir / run_name
    run_rel = f"experiments/00-market-read-lab/runs/{run_name}"

    if run_dir.exists():
        raise SystemExit(f"Run already exists: {run_rel}")

    run_dir.mkdir(parents=True)
    receipts_dir = run_dir / "receipts"
    receipts_dir.mkdir()
    (receipts_dir / ".gitkeep").write_text("", encoding="utf-8")

    scout_template = (templates_dir / "scout.md").read_text(encoding="utf-8")
    (run_dir / "scout.md").write_text(
        seeded_scout(scout_template, args.question, contract, selected_slug=slugify(args.slug)),
        encoding="utf-8",
    )

    for name in TEMPLATE_FILES:
        if name == "run-notes.md":
            run_notes_template = (templates_dir / name).read_text(encoding="utf-8")
            run_notes_text = rendered_run_notes(
                run_notes_template,
                run_status="scout-only" if contract else "",
                evidence_mode=str(contract["evidence_mode"]) if contract else "",
                autonomous_eligible="yes" if contract else "",
                termination_reason="completed" if contract else "",
            )
            (run_dir / name).write_text(run_notes_text, encoding="utf-8")
        else:
            shutil.copyfile(templates_dir / name, run_dir / name)

    prompt_name = "operator-scout-prompt.md" if args.mode == "scout" else "operator-loop1-prompt.md"
    loop_prompt = render_loop_prompt((templates_dir / prompt_name).read_text(encoding="utf-8"), run_rel)

    print(f"Created {run_rel}")
    print()
    print(("Scout-only" if args.mode == "scout" else "Loop 1") + " prompt:")
    print()
    print(loop_prompt)
    return 0


if __name__ == "__main__":
    sys.exit(main())
