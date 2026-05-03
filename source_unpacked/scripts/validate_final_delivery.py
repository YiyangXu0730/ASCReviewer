#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "FINAL_DELIVERY_MANIFEST.json"
FINAL_INDEX_PATH = ROOT / ".ascreview" / "context" / "ARTIFACT_INDEX_final.json"

BASELINE_COMMANDS = [
    ["scripts/validate_pack.py", "VALIDATION_OK"],
    ["scripts/validate_ascreview_build.py", "ASCREVIEW_VALIDATION_OK"],
    ["scripts/validate_negative_cases.py", "NEGATIVE_VALIDATION_OK"],
]

STALE_INDEX_PHRASES = [
    "Prepare final-report scaffold",
    "final package creation is still a next action",
    "Create Desktop folder The Final ACS Review only when final report is ready",
    "ascreview-continue-until-final-report-folder",
]

SELF_REFERENTIAL_ARTIFACTS = {
    "FINAL_DELIVERY_MANIFEST.json",
    "ASCReview_FINAL_DELIVERY_REMEDIATION_REPORT.md",
    ".ascreview/context/ARTIFACT_INDEX_final.json",
}


def fail(message: str) -> None:
    print("FINAL_DELIVERY_VALIDATION_FAILED")
    print(message)
    sys.exit(1)


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing json file: {path}")
    except json.JSONDecodeError as exc:
        fail(f"invalid json file: {path}: {exc}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_artifact_path(path_text: str) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path
    return ROOT / path


def require_field(data: dict, field: str, context: str) -> object:
    if field not in data:
        fail(f"{context} missing required field: {field}")
    return data[field]


def validate_required_shape(manifest: dict, final_index: dict) -> None:
    for field in [
        "manifest_id",
        "created_at",
        "project_canonical_name",
        "delivery_status",
        "source_package_root",
        "final_delivery_folder",
        "canonical_zip",
        "artifacts",
        "validation",
        "provenance_hygiene",
        "naming",
        "limitations",
        "scope_confirmation",
    ]:
        require_field(manifest, field, "FINAL_DELIVERY_MANIFEST.json")
    for field in [
        "snapshot_id",
        "created_at",
        "project_canonical_name",
        "delivery_status",
        "canonical_zip",
        "final_delivery_folder",
        "counts",
        "validation",
        "canonical_artifacts",
    ]:
        require_field(final_index, field, "ARTIFACT_INDEX_final.json")


def validate_naming(manifest: dict, final_index: dict) -> None:
    if manifest.get("project_canonical_name") != "ASCReview":
        fail("manifest project_canonical_name must be ASCReview")
    if final_index.get("project_canonical_name") != "ASCReview":
        fail("final artifact index project_canonical_name must be ASCReview")
    if manifest.get("delivery_status") != "FINAL_DELIVERY_READY":
        fail("manifest delivery_status must be FINAL_DELIVERY_READY")
    if final_index.get("delivery_status") != "FINAL_DELIVERY_READY":
        fail("final artifact index delivery_status must be FINAL_DELIVERY_READY")

    canonical_zip = manifest.get("canonical_zip", {})
    zip_path_text = canonical_zip.get("path", "")
    zip_name = Path(zip_path_text).name
    if "ACS" in zip_name.upper().replace("ASCREVIEW", ""):
        fail(f"canonical ZIP filename still appears to use ACS alias: {zip_name}")
    if "ASCReview" not in zip_name and "ASCREVIEW" not in zip_name.upper():
        fail(f"canonical ZIP filename must name ASCReview: {zip_name}")


def validate_final_index_not_stale(final_index: dict) -> None:
    serialized = json.dumps(final_index, sort_keys=True)
    for phrase in STALE_INDEX_PHRASES:
        if phrase in serialized:
            fail(f"final artifact index contains stale continuation phrase: {phrase}")
    if final_index.get("snapshot_id") != "final":
        fail("final artifact index snapshot_id must be final")
    validation = final_index.get("validation", {})
    if validation.get("latest_known_status") != "passing":
        fail("final artifact index validation.latest_known_status must be passing")
    if final_index.get("continuation_source") not in (None, "not_applicable_final_delivery"):
        fail("final artifact index must not point to a continuation source")


def validate_counts(final_index: dict) -> None:
    sources = load_json(ROOT / "library" / "source_index.seed.json").get("sources", [])
    rules = load_json(ROOT / "library" / "provenance_ledger.seed.json").get("rules", [])
    rounds = load_json(ROOT / "qc" / "distillation_round_ledger.seed.json").get("rounds", [])
    skills = list((ROOT / "skills").glob("*/SKILL.md"))
    expected = {
        "sources": len(sources),
        "provenance_rules": len(rules),
        "distillation_rounds": len(rounds),
        "skills": len(skills),
    }
    counts = final_index.get("counts", {})
    for key, value in expected.items():
        if counts.get(key) != value:
            fail(f"final artifact index count mismatch for {key}: {counts.get(key)} != {value}")


def validate_artifact_hashes(manifest: dict) -> int:
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail("manifest artifacts must be a non-empty list")
    checked = 0
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            fail("manifest artifact entry is not an object")
        path_text = artifact.get("path")
        expected_sha = artifact.get("sha256")
        expected_size = artifact.get("size_bytes")
        role = artifact.get("role", "")
        if not path_text or not expected_sha or expected_size is None:
            fail(f"artifact missing path, sha256, or size_bytes: {artifact}")
        path = resolve_artifact_path(path_text)
        if not path.exists():
            fail(f"artifact path does not exist: {path}")
        actual_sha = sha256_file(path)
        actual_size = path.stat().st_size
        if actual_sha != expected_sha:
            fail(f"artifact sha256 mismatch for {role or path_text}: {actual_sha} != {expected_sha}")
        if actual_size != expected_size:
            fail(f"artifact size mismatch for {role or path_text}: {actual_size} != {expected_size}")
        checked += 1
    return checked


def validate_final_index_artifact_hashes(final_index: dict) -> int:
    artifacts = final_index.get("canonical_artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        fail("final artifact index canonical_artifacts must be a non-empty list")
    checked = 0
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            fail("final artifact index artifact entry is not an object")
        path_text = artifact.get("path")
        expected_sha = artifact.get("sha256")
        expected_size = artifact.get("size_bytes")
        role = artifact.get("role", "")
        if not path_text or not expected_sha or expected_size is None:
            fail(f"final artifact index entry missing path, sha256, or size_bytes: {artifact}")
        normalized = path_text.replace("\\", "/")
        if normalized == ".ascreview/context/ARTIFACT_INDEX_final.json":
            fail("final artifact index must not include a self-hash entry")
        path = resolve_artifact_path(path_text)
        if not path.exists():
            fail(f"final artifact index path does not exist: {path}")
        actual_sha = sha256_file(path)
        actual_size = path.stat().st_size
        if actual_sha != expected_sha:
            fail(f"final artifact index sha256 mismatch for {role or path_text}: {actual_sha} != {expected_sha}")
        if actual_size != expected_size:
            fail(f"final artifact index size mismatch for {role or path_text}: {actual_size} != {expected_size}")
        checked += 1
    return checked


def validate_zip(manifest: dict) -> Path:
    canonical_zip = manifest.get("canonical_zip", {})
    zip_path_text = canonical_zip.get("path")
    if not zip_path_text:
        fail("manifest canonical_zip.path is missing")
    zip_path = resolve_artifact_path(zip_path_text)
    if not zip_path.exists():
        fail(f"canonical ZIP does not exist: {zip_path}")
    if zip_path.suffix.lower() != ".zip":
        fail(f"canonical ZIP path does not end with .zip: {zip_path}")

    expected_root = canonical_zip.get("root_name", "ASCReview_FINAL_DELIVERY").strip("/")
    with zipfile.ZipFile(zip_path) as archive:
        bad_member = archive.testzip()
        if bad_member is not None:
            fail(f"canonical ZIP integrity check failed at member: {bad_member}")
        names = archive.namelist()
        if not names:
            fail("canonical ZIP is empty")
        if len(names) != len(set(names)):
            fail("canonical ZIP contains duplicate member names")
        for name in names:
            if "\\" in name:
                fail(f"canonical ZIP contains non-POSIX member path: {name}")
            if name.startswith("/") or name.startswith("\\"):
                fail(f"canonical ZIP contains absolute member path: {name}")
            if len(name) > 1 and name[1] == ":":
                fail(f"canonical ZIP contains drive-qualified member path: {name}")
            if any(part == ".." for part in name.split("/")):
                fail(f"canonical ZIP contains path traversal member path: {name}")
            if not name.startswith(expected_root + "/"):
                fail(f"canonical ZIP member missing expected root prefix {expected_root}/: {name}")
            rel_without_root = name[len(expected_root) + 1 :]
            if rel_without_root in SELF_REFERENTIAL_ARTIFACTS:
                fail(f"canonical ZIP includes self-referential final-delivery artifact: {rel_without_root}")
    return zip_path


def validate_provenance_hygiene(manifest: dict) -> None:
    provenance = load_json(ROOT / "library" / "provenance_ledger.seed.json")
    rules = provenance.get("rules", [])
    rubric_rule = next((rule for rule in rules if rule.get("rule_id") == "RUBRIC-R1-RUBRIC-FIRST"), None)
    if rubric_rule is None:
        fail("missing RUBRIC-R1-RUBRIC-FIRST")
    if rubric_rule.get("evidence_type") == "teacher_rubric":
        fail("RUBRIC-R1-RUBRIC-FIRST must not use teacher_rubric without a supplied rubric")
    if rubric_rule.get("evidence_type") != "rubric_gate":
        fail(f"RUBRIC-R1-RUBRIC-FIRST must use rubric_gate, got {rubric_rule.get('evidence_type')}")
    rule_text = rubric_rule.get("rule", "")
    if "supplied" not in rule_text or "must not create" not in rule_text:
        fail("RUBRIC-R1-RUBRIC-FIRST wording must explicitly gate supplied rubric and prohibit invented criteria")
    hygiene = manifest.get("provenance_hygiene", {})
    if hygiene.get("teacher_rubric_present") is not False:
        fail("manifest provenance_hygiene.teacher_rubric_present must be false")
    if hygiene.get("rubric_gate_rule_id") != "RUBRIC-R1-RUBRIC-FIRST":
        fail("manifest provenance_hygiene must identify RUBRIC-R1-RUBRIC-FIRST")


def validate_scope(manifest: dict) -> None:
    scope = manifest.get("scope_confirmation", {})
    if scope.get("dissertation_review_performed") is not False:
        fail("manifest must state dissertation_review_performed=false")
    if scope.get("teacher_specific_scoring_created") is not False:
        fail("manifest must state teacher_specific_scoring_created=false")
    if scope.get("corpus_expansion_performed_in_remediation") is not False:
        fail("manifest must state corpus_expansion_performed_in_remediation=false")
    if scope.get("dissertation_specialization_started") is not False:
        fail("manifest must state dissertation_specialization_started=false")


def run_baseline_validators() -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for command, expected_marker in BASELINE_COMMANDS:
        result = subprocess.run(
            [sys.executable, command],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        output = result.stdout.strip()
        if result.returncode != 0 or expected_marker not in output:
            fail(f"baseline validator failed: python {command}\n{output}")
        results.append({"command": f"python {command}", "output": output, "returncode": result.returncode})
    return results


def main() -> None:
    manifest = load_json(MANIFEST_PATH)
    final_index = load_json(FINAL_INDEX_PATH)
    if not isinstance(manifest, dict) or not isinstance(final_index, dict):
        fail("manifest and final artifact index must be JSON objects")

    validate_required_shape(manifest, final_index)
    validate_naming(manifest, final_index)
    validate_final_index_not_stale(final_index)
    validate_counts(final_index)
    artifact_count = validate_artifact_hashes(manifest)
    index_artifact_count = validate_final_index_artifact_hashes(final_index)
    zip_path = validate_zip(manifest)
    validate_provenance_hygiene(manifest)
    validate_scope(manifest)
    baseline_results = run_baseline_validators()

    print("FINAL_DELIVERY_VALIDATION_OK")
    print(f"canonical_zip={zip_path}")
    print(f"artifacts_checked={artifact_count}")
    print(f"index_artifacts_checked={index_artifact_count}")
    print(f"baseline_validators={len(baseline_results)}")


if __name__ == "__main__":
    main()
