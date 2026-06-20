#!/usr/bin/env python3
"""Print selected-question history for Market Read Lab runs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


RUN_NAME_RE = re.compile(r"^(\d{3})-\d{4}-\d{2}-\d{2}-.+$")


@dataclass
class RunQuestion:
    run: str
    path: str
    run_number: int | None
    historical_or_pre_contract: bool
    run_status: str
    evidence_mode: str
    autonomous_eligible: str
    selected_slug: str
    selected_questions: list[str]
    pressure_lenses_fired: str
    notice: str


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "experiments/00-market-read-lab/templates").is_dir():
            return parent
    raise SystemExit("Could not find experiments/00-market-read-lab/templates from script path.")


def relpath(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def strip_yaml_scalar(raw: str) -> str:
    value = raw.strip()
    if not value or value == "null":
        return ""
    value = value.split(" #", 1)[0].strip()
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'").strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].strip()
    return value


def parse_contract_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.M)
    if not match:
        return ""
    return strip_yaml_scalar(match.group(1))


def parse_notes_value(text: str, key: str) -> str:
    return parse_contract_value(text, key)


def section_after_heading(text: str, heading_pattern: str) -> str:
    match = re.search(heading_pattern, text, flags=re.M)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^##\s+", text[start:], flags=re.M)
    if next_heading:
        return text[start : start + next_heading.start()].strip()
    return text[start:].strip()


def compact(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clean_question(value: str) -> str:
    value = compact(value)
    value = re.sub(r"^\*\*Selected by [^*]+:\*\*\s*", "", value)
    value = re.sub(r"^Selected by [^:]+:\s*", "", value)
    return value


def parse_selected_questions_from_section(scout_text: str) -> list[str]:
    block = section_after_heading(scout_text, r"^## Selected Question(?:\(s\))?\s*$")
    if not block:
        return []

    quoted = [line.strip()[1:].strip() for line in block.splitlines() if line.strip().startswith(">")]
    if quoted:
        return [clean_question(" ".join(quoted))]

    questions: list[str] = []
    current: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        numbered = re.match(r"^\d+\.\s+(.+)$", stripped)
        if numbered:
            if current:
                questions.append(clean_question(" ".join(current)))
            current = [numbered.group(1)]
        elif current and (line.startswith(" ") or line.startswith("\t")):
            current.append(stripped)
        elif current and not stripped:
            continue
        elif current:
            break
    if current:
        questions.append(clean_question(" ".join(current)))

    return [question for question in questions if question]


def parse_selected_questions(scout_text: str) -> list[str]:
    selected_question = parse_contract_value(scout_text, "selected_question")
    if selected_question:
        return [clean_question(selected_question)]
    return parse_selected_questions_from_section(scout_text)


def run_number_from_name(name: str) -> int | None:
    match = RUN_NAME_RE.match(name)
    if not match:
        return None
    return int(match.group(1))


def collect_run(root: Path, run_dir: Path) -> RunQuestion:
    scout_path = run_dir / "scout.md"
    notes_path = run_dir / "run-notes.md"
    scout_text = scout_path.read_text(encoding="utf-8") if scout_path.exists() else ""
    notes_text = notes_path.read_text(encoding="utf-8") if notes_path.exists() else ""

    number = run_number_from_name(run_dir.name)
    historical = number is not None and number <= 3
    notice = ""
    if historical:
        notice = "historical/pre-contract"
    if "Historical / incomplete run notice" in notes_text:
        notice = "historical/incomplete scout-only"

    return RunQuestion(
        run=run_dir.name,
        path=relpath(root, run_dir),
        run_number=number,
        historical_or_pre_contract=historical,
        run_status=parse_notes_value(notes_text, "run_status"),
        evidence_mode=parse_notes_value(notes_text, "evidence_mode") or parse_contract_value(scout_text, "evidence_mode"),
        autonomous_eligible=parse_notes_value(notes_text, "autonomous_eligible")
        or parse_contract_value(scout_text, "autonomous_eligible"),
        selected_slug=parse_contract_value(scout_text, "selected_slug"),
        selected_questions=parse_selected_questions(scout_text),
        pressure_lenses_fired=parse_notes_value(notes_text, "pressure_lenses_fired"),
        notice=notice,
    )


def collect_runs(root: Path, runs_dir: Path) -> list[RunQuestion]:
    rows: list[RunQuestion] = []
    if not runs_dir.exists():
        raise SystemExit(f"Runs directory not found: {relpath(root, runs_dir)}")
    for child in sorted(runs_dir.iterdir(), key=lambda path: path.name):
        if child.is_dir():
            rows.append(collect_run(root, child))
    return rows


def escape_markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def truncate(value: str, limit: int) -> str:
    if limit <= 0 or len(value) <= limit:
        return value
    return value[: max(0, limit - 3)].rstrip() + "..."


def render_markdown(rows: list[RunQuestion], *, max_question_chars: int) -> str:
    lines = [
        "| Run | Status | Evidence | Question | Pressure | Notice |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        questions = "<br>".join(row.selected_questions) if row.selected_questions else ""
        lines.append(
            "| "
            + " | ".join(
                [
                    escape_markdown_cell(row.run),
                    escape_markdown_cell(row.run_status),
                    escape_markdown_cell(row.evidence_mode),
                    escape_markdown_cell(truncate(questions, max_question_chars)),
                    escape_markdown_cell(row.pressure_lenses_fired),
                    escape_markdown_cell(row.notice),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def resolve_runs_dir(root: Path, value: str | None) -> Path:
    if not value:
        return root / "experiments/00-market-read-lab/runs"
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--runs-dir",
        help="Runs directory. Defaults to experiments/00-market-read-lab/runs.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format. Defaults to markdown.",
    )
    parser.add_argument(
        "--max-question-chars",
        type=int,
        default=220,
        help="Markdown question truncation length. Use 0 for no truncation.",
    )
    parser.add_argument(
        "--completed-only",
        action="store_true",
        help="Only include runs with run_status: reviewed.",
    )
    args = parser.parse_args()

    root = find_repo_root()
    rows = collect_runs(root, resolve_runs_dir(root, args.runs_dir))
    if args.completed_only:
        rows = [row for row in rows if row.run_status == "reviewed"]

    if args.format == "json":
        print(json.dumps([asdict(row) for row in rows], indent=2))
    else:
        print(render_markdown(rows, max_question_chars=args.max_question_chars))
    return 0


if __name__ == "__main__":
    sys.exit(main())
