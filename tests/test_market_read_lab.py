#!/usr/bin/env python3
"""Tests for the local Market Read Lab scaffolder contract."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]
NEW_RUN_PATH = ROOT / ".claude/skills/market-read-lab/scripts/new_run.py"
SCOUT_TEMPLATE_PATH = ROOT / "experiments/00-market-read-lab/templates/scout.md"


def load_new_run_module() -> ModuleType:
    spec = importlib.util.spec_from_file_location("market_read_lab_new_run", NEW_RUN_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {NEW_RUN_PATH}")
    module = importlib.util.module_from_spec(spec)
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
            "evidence_mode": "bounded-live",
            "expected_denominator": "Store cohort plus a small review/forum panel.",
            "likely_source_panel": "Store files, then review/forum sources as a light panel.",
            "allowed_sources": ["store/", "bounded-live review/forum panel"],
            "disallowed_actions": self.new_run.default_disallowed_actions("bounded-live"),
            "live_evidence_plan": {
                "approved_by": "Brian",
                "approval_scope": "autonomous Market Read Lab runs",
                "budget_class": "light",
                "review_after": "3 bounded-live runs",
                "evidence_goal": "Verify trust objections with a small public review/forum panel.",
                "source_families_allowed": ["review/forum"],
                "source_families_preferred": ["review/forum"],
                "source_families_disallowed": ["login-only or paywalled sources", "broad crawling"],
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
        self.assertIn("selected_slug: 'review-objections'", scout)
        self.assertIn("live_evidence_plan:", scout)
        self.assertIn("budget_class: 'light'", scout)
        self.assertIn("source_families_allowed:", scout)
        self.assertIn("- 'review/forum'", scout)
        self.assertIn("approval_needed: no", scout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
