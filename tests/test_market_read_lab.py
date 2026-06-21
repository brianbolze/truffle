#!/usr/bin/env python3
"""Tests for the local Market Read Lab scaffolder contract."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
NEW_RUN_PATH = ROOT / ".claude/skills/market-read-lab/scripts/new_run.py"
QUESTION_HISTORY_PATH = ROOT / ".claude/skills/market-read-lab/scripts/question_history.py"
SCOUT_TEMPLATE_PATH = ROOT / "experiments/00-market-read-lab/templates/scout.md"


def load_new_run_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("market_read_lab_new_run", NEW_RUN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {NEW_RUN_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_question_history_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("market_read_lab_question_history", QUESTION_HISTORY_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {QUESTION_HISTORY_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class MarketReadLabScaffoldTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.new_run = load_new_run_module()

    def test_bounded_live_defaults_do_not_disallow_the_planned_live_panel(self) -> None:
        actions = self.new_run.default_disallowed_actions("bounded-live")

        self.assertNotIn("live browsing", actions)
        self.assertNotIn("paid capture", actions)
        self.assertIn("write-back to store/", actions)
        self.assertIn("triage graduation", actions)

    def test_seeded_scout_renders_bounded_live_plan(self) -> None:
        template = SCOUT_TEMPLATE_PATH.read_text(encoding="utf-8")
        contract = {
            "run_type": "market",
            "question_mode": "gap-probe",
            "evidence_mode": "bounded-live",
            "expected_denominator": "Store cohort plus a small review/forum panel.",
            "likely_source_panel": "Store files, then review/forum sources as a light panel.",
            "builder_lens": "Source-family reach: can a small review/forum panel surface objections store files can't?",
            "reach_reason": "Probes trust objections beyond the cached store answer.",
            "allowed_sources": ["store/", "bounded-live review/forum panel"],
            "disallowed_actions": self.new_run.default_disallowed_actions("bounded-live"),
            "live_evidence_plan": {
                "approved_by": "Brian",
                "approval_scope": "autonomous Market Read Lab runs",
                "budget_class": "light",
                "ceilings": self.new_run.DEFAULT_BOUNDED_LIVE_CEILINGS,
                "review_after": "3 bounded-live runs",
                "evidence_goal": "Verify trust objections with a small public review/forum panel.",
                "source_families_allowed": ["review/forum"],
                "source_families_preferred": ["review/forum"],
                "source_families_disallowed": ["login-only or paywalled sources", "broad crawling"],
                "fail_closed_when": self.new_run.DEFAULT_BOUNDED_LIVE_FAIL_CLOSED_WHEN,
                "stop_when": ["the next source would expand the question rather than verify it"],
            },
            "why_autonomous_safe": "Bounded source panel with no store write-back.",
            "loop1_failure_mode": "Treating a small public sample as representative.",
        }

        scout = self.new_run.seeded_scout(
            template,
            "What objections show up in reviews?",
            contract,
            selected_slug="review-objections",
        )

        self.assertIn("evidence_mode: bounded-live", scout)
        self.assertIn("question_mode: gap-probe", scout)
        self.assertIn("| gap-probe |", scout)
        self.assertIn("builder_lens: 'Source-family reach", scout)
        self.assertIn("reach_reason: 'Probes trust objections", scout)
        self.assertIn("selected_slug: 'review-objections'", scout)
        self.assertIn("live_evidence_plan:", scout)
        self.assertIn("budget_class: 'light'", scout)
        self.assertIn("ceilings:", scout)
        self.assertIn("source_families_allowed:", scout)
        self.assertIn("- 'review/forum'", scout)
        self.assertIn("approval_needed: no", scout)


class MarketReadLabQuestionHistoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.history = load_question_history_module()

    def test_parses_current_selected_run_contract_question(self) -> None:
        scout = """# Scout

## Selected Run Contract

```yaml
selected_question: "Which brands are defaults?"
selected_slug: defaults-panel
evidence_mode: bounded-live
autonomous_eligible: yes
```
"""

        self.assertEqual(
            self.history.parse_selected_questions(scout),
            ["Which brands are defaults?"],
        )
        self.assertEqual(self.history.parse_contract_value(scout, "selected_slug"), "defaults-panel")

    def test_parses_historical_selected_question_section(self) -> None:
        scout = """# Scout

## Selected Question(s)

1. **Selected by Brian:** Who are Hone Health's closest competitors, and which are true substitutes vs adjacent peers?
2. In compounded Rx telehealth, which product categories are most crowded?

These are Scout recommendations until Brian confirms one.

## Selection Notes
"""

        self.assertEqual(
            self.history.parse_selected_questions(scout),
            [
                "Who are Hone Health's closest competitors, and which are true substitutes vs adjacent peers?",
                "In compounded Rx telehealth, which product categories are most crowded?",
            ],
        )

    def test_render_markdown_keeps_history_readable(self) -> None:
        row = self.history.RunQuestion(
            run="012-2026-06-19-glp1-default-brand-leaderboard",
            path="experiments/00-market-read-lab/runs/012-2026-06-19-glp1-default-brand-leaderboard",
            run_number=12,
            historical_or_pre_contract=False,
            run_status="reviewed",
            evidence_mode="bounded-live",
            autonomous_eligible="yes",
            selected_slug="glp1-default-brand-leaderboard",
            selected_questions=["Which GLP-1 brands are third-party defaults?"],
            pressure_lenses_fired="[denominator-reconciliation]",
            notice="",
        )

        rendered = self.history.render_markdown([row], max_question_chars=0)

        self.assertIn("| Run | Status | Evidence | Question | Pressure | Notice |", rendered)
        self.assertIn("bounded-live", rendered)
        self.assertIn("Which GLP-1 brands are third-party defaults?", rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
