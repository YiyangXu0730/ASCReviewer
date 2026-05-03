#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def copy_worktree(destination: Path) -> None:
    def ignore(_dir: str, names: list[str]) -> set[str]:
        return {name for name in names if name in {"__pycache__", ".pytest_cache"}}

    shutil.copytree(ROOT, destination, ignore=ignore)


def run_validator(worktree: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "scripts/validate_final_delivery.py"],
        cwd=worktree,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def expect_failure(case_name: str, mutate) -> None:
    with tempfile.TemporaryDirectory(prefix="ascreview-final-negative-") as tmp:
        worktree = Path(tmp) / "pack"
        copy_worktree(worktree)
        mutate(worktree)
        result = run_validator(worktree)
        if result.returncode == 0:
            print("FINAL_DELIVERY_NEGATIVE_VALIDATION_FAILED")
            print(f"{case_name}: validator unexpectedly passed")
            sys.exit(1)
        if "FINAL_DELIVERY_VALIDATION_FAILED" not in result.stdout:
            print("FINAL_DELIVERY_NEGATIVE_VALIDATION_FAILED")
            print(f"{case_name}: validator failed without final-delivery marker")
            print(result.stdout)
            sys.exit(1)
        print(f"FINAL_DELIVERY_NEGATIVE_CASE_OK {case_name}")


def mutate_stale_final_index(worktree: Path) -> None:
    path = worktree / ".ascreview" / "context" / "ARTIFACT_INDEX_final.json"
    data = load_json(path)
    data["delivery_status"] = "CONTINUATION_READY"
    data["next_actions"] = ["Prepare final-report scaffold and final package folder."]
    write_json(path, data)


def mutate_acs_canonical_name(worktree: Path) -> None:
    manifest_path = worktree / "FINAL_DELIVERY_MANIFEST.json"
    index_path = worktree / ".ascreview" / "context" / "ARTIFACT_INDEX_final.json"
    manifest = load_json(manifest_path)
    index = load_json(index_path)
    manifest["project_canonical_name"] = "ACS Review"
    index["project_canonical_name"] = "ACS Review"
    write_json(manifest_path, manifest)
    write_json(index_path, index)


def mutate_backslash_zip_member(worktree: Path) -> None:
    bad_zip = worktree / "bad_backslash_member.zip"
    with zipfile.ZipFile(bad_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("ASCReview_FINAL_DELIVERY\\bad\\path.txt", "bad path")
    bad_hash = sha256_file(bad_zip)
    bad_size = bad_zip.stat().st_size
    manifest_path = worktree / "FINAL_DELIVERY_MANIFEST.json"
    manifest = load_json(manifest_path)
    manifest["canonical_zip"]["path"] = str(bad_zip)
    manifest["canonical_zip"]["sha256"] = bad_hash
    manifest["canonical_zip"]["size_bytes"] = bad_size
    for artifact in manifest["artifacts"]:
        if artifact.get("role") == "canonical_zip":
            artifact["path"] = str(bad_zip)
            artifact["sha256"] = bad_hash
            artifact["size_bytes"] = bad_size
    write_json(manifest_path, manifest)


def mutate_manifest_hash(worktree: Path) -> None:
    path = worktree / "FINAL_DELIVERY_MANIFEST.json"
    data = load_json(path)
    data["artifacts"][0]["sha256"] = "0" * 64
    write_json(path, data)


def mutate_rubric_rule_to_teacher_evidence(worktree: Path) -> None:
    path = worktree / "library" / "provenance_ledger.seed.json"
    data = load_json(path)
    for rule in data["rules"]:
        if rule.get("rule_id") == "RUBRIC-R1-RUBRIC-FIRST":
            rule["evidence_type"] = "teacher_rubric"
            rule["rule"] = "All review comments must be mapped first to teacher rubric criteria when available."
            break
    write_json(path, data)


def mutate_dissertation_review_started(worktree: Path) -> None:
    path = worktree / "FINAL_DELIVERY_MANIFEST.json"
    data = load_json(path)
    data["scope_confirmation"]["dissertation_review_performed"] = True
    data["scope_confirmation"]["teacher_specific_scoring_created"] = True
    write_json(path, data)


def main() -> None:
    required = [
        ROOT / "FINAL_DELIVERY_MANIFEST.json",
        ROOT / ".ascreview" / "context" / "ARTIFACT_INDEX_final.json",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        print("FINAL_DELIVERY_NEGATIVE_VALIDATION_FAILED")
        print("missing final delivery artifacts: " + ", ".join(missing))
        sys.exit(1)

    cases = [
        ("stale_final_index", mutate_stale_final_index),
        ("acs_canonical_name", mutate_acs_canonical_name),
        ("backslash_zip_member", mutate_backslash_zip_member),
        ("manifest_hash_mismatch", mutate_manifest_hash),
        ("rubric_rule_teacher_evidence_regression", mutate_rubric_rule_to_teacher_evidence),
        ("dissertation_review_started", mutate_dissertation_review_started),
    ]
    for case_name, mutate in cases:
        expect_failure(case_name, mutate)
    print("FINAL_DELIVERY_NEGATIVE_VALIDATION_OK")


if __name__ == "__main__":
    main()
