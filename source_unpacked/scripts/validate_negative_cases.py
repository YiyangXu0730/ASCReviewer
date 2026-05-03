#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def run_validator(worktree: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_ascreview_build.py"],
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def copy_worktree(destination: Path) -> None:
    def ignore(_dir: str, names: list[str]) -> set[str]:
        return {name for name in names if name in {"__pycache__", ".pytest_cache"}}

    shutil.copytree(ROOT, destination, ignore=ignore)


def expect_failure(case_name: str, mutate) -> None:
    with tempfile.TemporaryDirectory(prefix="ascreview-negative-") as tmp:
        worktree = Path(tmp) / "pack"
        copy_worktree(worktree)
        mutate(worktree)
        result = run_validator(worktree)
        if result.returncode == 0:
            print("NEGATIVE_VALIDATION_FAILED")
            print(f"{case_name}: validator unexpectedly passed")
            sys.exit(1)
        if "ASCREVIEW_VALIDATION_FAILED" not in result.stdout:
            print("NEGATIVE_VALIDATION_FAILED")
            print(f"{case_name}: validator failed without ASCReview failure marker")
            print(result.stdout)
            sys.exit(1)
        print(f"NEGATIVE_CASE_OK {case_name}")


def mutate_unknown_source_reuse(worktree: Path) -> None:
    for rel in ["library/source_index.seed.json", "templates/source_index.seed.json"]:
        path = worktree / rel
        data = load_json(path)
        data["sources"][0]["reuse_status"] = "unknown"
        write_json(path, data)


def mutate_missing_distillation_auditor(worktree: Path) -> None:
    path = worktree / "qc/distillation_round_ledger.seed.json"
    data = load_json(path)
    data["rounds"][0].pop("auditor_objections")
    write_json(path, data)


def mutate_unknown_dry_run_rule_id(worktree: Path) -> None:
    path = worktree / "examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json"
    data = load_json(path)
    data["must_fix"][0]["rule_ids"] = ["UNKNOWN-RULE-ID"]
    write_json(path, data)


def mutate_partial_permission_enabled(worktree: Path) -> None:
    path = worktree / "examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json"
    data = load_json(path)
    data["specialization_input_status"]["review_permissions"]["can_score_against_rubric"] = True
    write_json(path, data)


def mutate_partial_rubric_failure(worktree: Path) -> None:
    path = worktree / "examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json"
    data = load_json(path)
    data["severity_classifications"][0]["severity_id"] = "rubric_failure"
    write_json(path, data)


def mutate_revision_permission_enabled(worktree: Path) -> None:
    path = worktree / "examples/toy_revision_partial_pack/ASCReview_DryRunFindings.toy_revision_partial.json"
    data = load_json(path)
    data["specialization_input_status"]["review_permissions"]["can_review_draft_text"] = True
    write_json(path, data)


def mutate_figure_absent_permission_enabled(worktree: Path) -> None:
    path = worktree / "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_absent.json"
    data = load_json(path)
    data["specialization_input_status"]["review_permissions"]["can_review_figures"] = True
    write_json(path, data)


def mutate_figure_present_scoring_enabled(worktree: Path) -> None:
    path = worktree / "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_present.json"
    data = load_json(path)
    data["specialization_input_status"]["review_permissions"]["can_score_against_rubric"] = True
    write_json(path, data)


def main() -> None:
    cases = [
        ("unknown_source_reuse_status", mutate_unknown_source_reuse),
        ("missing_distillation_auditor_objection", mutate_missing_distillation_auditor),
        ("unknown_dry_run_rule_id", mutate_unknown_dry_run_rule_id),
        ("partial_permission_enabled", mutate_partial_permission_enabled),
        ("partial_rubric_failure_without_rubric", mutate_partial_rubric_failure),
        ("revision_permission_enabled_without_inputs", mutate_revision_permission_enabled),
        ("figure_absent_permission_enabled", mutate_figure_absent_permission_enabled),
        ("figure_present_scoring_enabled_without_rubric", mutate_figure_present_scoring_enabled),
    ]
    for case_name, mutate in cases:
        expect_failure(case_name, mutate)
    print("NEGATIVE_VALIDATION_OK")


if __name__ == "__main__":
    main()
