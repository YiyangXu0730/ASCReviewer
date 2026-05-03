#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "ascreview/README_ASCReview.md",
    "ascreview/ASCReview_CORE_PROMPT.md",
    "ascreview/ASCReview_SPECIALIZATION_PROMPT.md",
    "ascreview/ASCReview_SECTION_REVIEW_PROMPT.md",
    "ascreview/ASCReview_FULL_DRAFT_REVIEW_PROMPT.md",
    "ascreview/ASCReview_REVISION_ROUND_PROMPT.md",
    "ascreview/USAGE_GUIDE.md",
    "library/source_policy.md",
    "library/acquisition_plan.md",
    "library/source_index.schema.json",
    "library/source_index.seed.json",
    "library/provenance_ledger.schema.json",
    "library/provenance_ledger.seed.json",
    "patterns/introduction/good_introduction_patterns.md",
    "patterns/introduction/introduction_failure_modes.md",
    "patterns/methodology/good_methodology_patterns.md",
    "patterns/methodology/methodology_failure_modes.md",
    "patterns/results/good_results_patterns.md",
    "patterns/results/results_failure_modes.md",
    "patterns/discussion/good_discussion_patterns.md",
    "patterns/discussion/discussion_failure_modes.md",
    "patterns/figures/good_figure_legend_patterns.md",
    "patterns/figures/figure_legend_failure_modes.md",
    "qc/adversarial_distillation_protocol.md",
    "qc/adversarial_qc_report.md",
    "qc/audit_report.template.md",
    "qc/distillation_round_ledger.schema.json",
    "qc/distillation_round_ledger.seed.json",
    "templates/ReviewTaskSpec.template.json",
    "templates/SpecializationInputContract.template.json",
    "templates/MarkingSchemeMap.template.json",
    "templates/SectionReviewReport.template.md",
    "templates/FullDraftReviewReport.template.md",
    "templates/RevisionRoundReport.template.md",
    "templates/source_index.seed.json",
    "examples/toy_full_draft_pack/ASCReview_DryRunReport.toy_full.md",
    "examples/toy_full_draft_pack/ASCReview_DryRunFindings.toy_full.json",
    "examples/toy_biomed_genomics_pack/ReviewTaskSpec.toy_biomed.json",
    "examples/toy_biomed_genomics_pack/MarkingSchemeMap.toy_biomed.json",
    "examples/toy_biomed_genomics_pack/SectionReviewContract.toy_biomed.json",
    "examples/toy_biomed_genomics_pack/toy_biomed_genomics_draft.md",
    "examples/toy_biomed_genomics_pack/MissingInformationRequest.toy_biomed.md",
    "examples/toy_biomed_genomics_pack/ASCReview_DryRunReport.toy_biomed.md",
    "examples/toy_biomed_genomics_pack/ASCReview_DryRunFindings.toy_biomed.json",
    "examples/toy_partial_specialization_pack/README.md",
    "examples/toy_partial_specialization_pack/SpecializationInputContract.toy_partial.json",
    "examples/toy_partial_specialization_pack/ReviewTaskSpec.toy_partial.json",
    "examples/toy_partial_specialization_pack/MissingInformationRequest.toy_partial.md",
    "examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json",
    "examples/toy_revision_partial_pack/README.md",
    "examples/toy_revision_partial_pack/SpecializationInputContract.toy_revision_partial.json",
    "examples/toy_revision_partial_pack/ReviewTaskSpec.toy_revision_partial.json",
    "examples/toy_revision_partial_pack/SectionReviewContract.revision_gate.toy.json",
    "examples/toy_revision_partial_pack/MissingInformationRequest.toy_revision_partial.md",
    "examples/toy_revision_partial_pack/ASCReview_DryRunFindings.toy_revision_partial.json",
    "examples/toy_figure_permission_pack/README.md",
    "examples/toy_figure_permission_pack/toy_figure_asset.svg",
    "examples/toy_figure_permission_pack/toy_figure_legend.md",
    "examples/toy_figure_permission_pack/MissingInformationRequest.figure_absent.md",
    "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_absent.json",
    "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_present.json",
    "scripts/validate_negative_cases.py",
    ".ascreview/run_ledger.md",
]


REQUIRED_SKILLS = [
    "review-introduction",
    "review-methodology",
    "review-results",
    "review-discussion",
    "review-figures-legends",
    "assess-rubric-alignment",
    "assess-scientific-claim-strength",
    "assess-bioinformatics-methods",
    "revision-round-compare",
]


MIN_ROUNDS = {
    "introduction": 4,
    "methodology": 4,
    "results": 4,
    "discussion": 4,
    "figures": 3,
    "rubric": 2,
    "revision": 2,
    "bioinformatics": 3,
    "claims": 1,
}


SKILL_HEADINGS = [
    "## Purpose",
    "## When To Use",
    "## Required Inputs",
    "## Priority Rules",
    "## Evidence Rules",
    "## Checklist",
    "## Output Schema",
    "## Known Failure Modes",
    "## Stop Conditions",
]


EVIDENCE_TYPES = {
    "source_pattern",
    "official_guideline",
    "teacher_rubric",
    "rubric_gate",
    "domain_expert_heuristic",
    "provisional",
}


AUDIT_STATUSES = {
    "draft",
    "challenged",
    "accepted",
    "rejected",
    "provisional",
}


SEVERITY_IDS = {
    "rubric_failure",
    "scientific_validity_risk",
    "reporting_completeness_risk",
    "reproducibility_risk",
    "policy_compliance_risk",
    "draft_stage_todo",
    "style_or_clarity_polish",
}


def load_json(path: str) -> object:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def fail(message: str) -> None:
    print("ASCREVIEW_VALIDATION_FAILED")
    print(message)
    sys.exit(1)


def _type_matches(value: object, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "null":
        return value is None
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return False


def _resolve_schema_ref(root_schema: dict, ref: str) -> dict:
    if not ref.startswith("#/"):
        fail(f"unsupported schema ref: {ref}")
    node: object = root_schema
    for part in ref[2:].split("/"):
        if not isinstance(node, dict) or part not in node:
            fail(f"unresolvable schema ref: {ref}")
        node = node[part]
    if not isinstance(node, dict):
        fail(f"schema ref does not resolve to object: {ref}")
    return node


def validate_schema_subset(
    value: object,
    schema: dict,
    label: str,
    path: str = "$",
    root_schema: dict | None = None,
) -> None:
    """Validate the JSON Schema subset used by this package.

    The ASCReview build should not depend on optional site packages just to catch
    malformed ledgers, so this deliberately supports only the schema features
    used in `schemas/*.schema.json`.
    """
    if root_schema is None:
        root_schema = schema
    if "$ref" in schema:
        validate_schema_subset(value, _resolve_schema_ref(root_schema, schema["$ref"]), label, path, root_schema)
        return

    expected_type = schema.get("type")
    if expected_type:
        expected_types = expected_type if isinstance(expected_type, list) else [expected_type]
        if not any(_type_matches(value, type_name) for type_name in expected_types):
            fail(f"{label} schema violation at {path}: expected type {expected_type}")

    if "enum" in schema and value not in schema["enum"]:
        fail(f"{label} schema violation at {path}: {value!r} not in enum {schema['enum']}")

    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0):
            fail(f"{label} schema violation at {path}: string shorter than minLength")
        pattern = schema.get("pattern")
        if pattern and not re.search(pattern, value):
            fail(f"{label} schema violation at {path}: value {value!r} does not match {pattern}")

    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0):
            fail(f"{label} schema violation at {path}: array shorter than minItems")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                validate_schema_subset(item, item_schema, label, f"{path}[{index}]", root_schema)

    if isinstance(value, dict):
        required = schema.get("required", [])
        missing = [key for key in required if key not in value]
        if missing:
            fail(f"{label} schema violation at {path}: missing required keys {missing}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extras = sorted(set(value) - set(properties))
            if extras:
                fail(f"{label} schema violation at {path}: additional keys {extras}")
        for key, child_schema in properties.items():
            if key in value:
                validate_schema_subset(value[key], child_schema, label, f"{path}.{key}", root_schema)


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    missing.extend(
        f"skills/{name}/SKILL.md"
        for name in REQUIRED_SKILLS
        if not (ROOT / "skills" / name / "SKILL.md").exists()
    )
    missing.extend(
        f".agents/skills/{name}/SKILL.md"
        for name in REQUIRED_SKILLS
        if not (ROOT / ".agents" / "skills" / name / "SKILL.md").exists()
    )
    if missing:
        fail("missing files:\n" + "\n".join(missing))

    for json_file in ROOT.rglob("*.json"):
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"invalid json: {json_file.relative_to(ROOT)}: {exc}")

    schema_pairs = [
        ("library/source_index.seed.json", "library/source_index.schema.json", "schemas/SourceIndex.schema.json", "source index"),
        ("library/provenance_ledger.seed.json", "library/provenance_ledger.schema.json", "schemas/ProvenanceLedger.schema.json", "provenance ledger"),
        ("qc/distillation_round_ledger.seed.json", "qc/distillation_round_ledger.schema.json", "schemas/DistillationRoundLedger.schema.json", "distillation round ledger"),
    ]
    for data_path, library_schema_path, canonical_schema_path, label in schema_pairs:
        library_schema_text = (ROOT / library_schema_path).read_text(encoding="utf-8")
        canonical_schema_text = (ROOT / canonical_schema_path).read_text(encoding="utf-8")
        if library_schema_text != canonical_schema_text:
            fail(f"{library_schema_path} is not synchronized with {canonical_schema_path}")
        validate_schema_subset(
            load_json(data_path),
            json.loads(library_schema_text),
            label,
        )
    validate_schema_subset(
        load_json("templates/SpecializationInputContract.template.json"),
        load_json("schemas/SpecializationInputContract.schema.json"),
        "specialization input contract template",
    )
    for data_path, schema_path, label in [
        ("templates/ReviewTaskSpec.template.json", "schemas/ReviewTaskSpec.schema.json", "review task spec template"),
        ("examples/toy_specialization_pack/ReviewTaskSpec.toy.json", "schemas/ReviewTaskSpec.schema.json", "toy review task spec"),
        ("examples/toy_full_draft_pack/ReviewTaskSpec.toy_full.json", "schemas/ReviewTaskSpec.schema.json", "toy full draft task spec"),
        ("examples/toy_biomed_genomics_pack/ReviewTaskSpec.toy_biomed.json", "schemas/ReviewTaskSpec.schema.json", "toy biomed task spec"),
        ("examples/toy_partial_specialization_pack/ReviewTaskSpec.toy_partial.json", "schemas/ReviewTaskSpec.schema.json", "toy partial task spec"),
        ("examples/toy_revision_partial_pack/ReviewTaskSpec.toy_revision_partial.json", "schemas/ReviewTaskSpec.schema.json", "toy revision partial task spec"),
        ("templates/MarkingSchemeMap.template.json", "schemas/MarkingSchemeMap.schema.json", "marking scheme map template"),
        ("examples/toy_specialization_pack/MarkingSchemeMap.toy.json", "schemas/MarkingSchemeMap.schema.json", "toy marking scheme map"),
        ("examples/toy_full_draft_pack/MarkingSchemeMap.toy_full.json", "schemas/MarkingSchemeMap.schema.json", "toy full marking scheme map"),
        ("examples/toy_biomed_genomics_pack/MarkingSchemeMap.toy_biomed.json", "schemas/MarkingSchemeMap.schema.json", "toy biomed marking scheme map"),
        ("examples/toy_specialization_pack/SectionReviewContract.introduction.toy.json", "schemas/SectionReviewContract.schema.json", "toy section review contract"),
        ("examples/toy_full_draft_pack/SectionReviewContract.full_draft.toy.json", "schemas/SectionReviewContract.schema.json", "toy full section review contract"),
        ("examples/toy_biomed_genomics_pack/SectionReviewContract.toy_biomed.json", "schemas/SectionReviewContract.schema.json", "toy biomed section review contract"),
        ("examples/toy_revision_partial_pack/SectionReviewContract.revision_gate.toy.json", "schemas/SectionReviewContract.schema.json", "toy revision section review contract"),
        ("examples/toy_full_draft_pack/ASCReview_DryRunFindings.toy_full.json", "schemas/ReviewReport.schema.json", "toy full dry-run findings"),
        ("examples/toy_biomed_genomics_pack/ASCReview_DryRunFindings.toy_biomed.json", "schemas/ReviewReport.schema.json", "toy biomed dry-run findings"),
        ("examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json", "schemas/ReviewReport.schema.json", "toy partial dry-run findings"),
        ("examples/toy_revision_partial_pack/ASCReview_DryRunFindings.toy_revision_partial.json", "schemas/ReviewReport.schema.json", "toy revision partial dry-run findings"),
        ("examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_absent.json", "schemas/ReviewReport.schema.json", "toy figure absent dry-run findings"),
        ("examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_present.json", "schemas/ReviewReport.schema.json", "toy figure present dry-run findings"),
        ("examples/toy_partial_specialization_pack/SpecializationInputContract.toy_partial.json", "schemas/SpecializationInputContract.schema.json", "toy partial specialization contract"),
        ("examples/toy_revision_partial_pack/SpecializationInputContract.toy_revision_partial.json", "schemas/SpecializationInputContract.schema.json", "toy revision partial specialization contract"),
    ]:
        validate_schema_subset(load_json(data_path), load_json(schema_path), label)

    source_index = load_json("library/source_index.seed.json")
    source_template = load_json("templates/source_index.seed.json")
    if source_index != source_template:
        fail("templates/source_index.seed.json is not synchronized with library/source_index.seed.json")
    sources = source_index.get("sources", [])
    source_ids_list = [source.get("source_id") for source in sources]
    source_ids = set(source_ids_list)
    if None in source_ids or not source_ids:
        fail("source index has missing source_id values")
    duplicate_source_ids = [source_id for source_id, count in Counter(source_ids_list).items() if count > 1]
    if duplicate_source_ids:
        fail("duplicate source_id values: " + ", ".join(sorted(duplicate_source_ids)))
    for source in sources:
        text = json.dumps(source)
        if "TO_VERIFY_AT_RUNTIME" in text:
            fail(f"unresolved placeholder in source index: {source.get('source_id')}")
        if source.get("reuse_status") == "unknown":
            fail(f"source has unknown reuse_status: {source.get('source_id')}")

    provenance = load_json("library/provenance_ledger.seed.json")
    rules = provenance.get("rules", [])
    rule_ids_list = [rule.get("rule_id") for rule in rules]
    rule_ids = set(rule_ids_list)
    duplicate_rule_ids = [rule_id for rule_id, count in Counter(rule_ids_list).items() if count > 1]
    if duplicate_rule_ids:
        fail("duplicate rule_id values: " + ", ".join(sorted(duplicate_rule_ids)))
    for rule in provenance.get("rules", []):
        if not rule.get("failure_mode"):
            fail(f"rule missing failure_mode: {rule.get('rule_id')}")
        if rule.get("evidence_type") not in EVIDENCE_TYPES:
            fail(f"invalid evidence_type for rule {rule.get('rule_id')}: {rule.get('evidence_type')}")
        if rule.get("audit_status") not in AUDIT_STATUSES:
            fail(f"invalid audit_status for rule {rule.get('rule_id')}: {rule.get('audit_status')}")
        for source_id in rule.get("source_ids", []):
            if source_id not in source_ids:
                fail(f"unknown source_id {source_id} in rule {rule.get('rule_id')}")

    ledger = load_json("qc/distillation_round_ledger.seed.json")
    rounds = ledger.get("rounds", [])
    round_ids_list = [round_.get("round_id") for round_ in rounds]
    duplicate_round_ids = [round_id for round_id, count in Counter(round_ids_list).items() if count > 1]
    if duplicate_round_ids:
        fail("duplicate round_id values: " + ", ".join(sorted(duplicate_round_ids)))
    counts = Counter(round_.get("skill_family") for round_ in rounds)
    for family, minimum in MIN_ROUNDS.items():
        if counts[family] < minimum:
            fail(f"insufficient rounds for {family}: {counts[family]} < {minimum}")
    for round_ in rounds:
        for rule_id in round_.get("rules_added", []):
            if rule_id not in rule_ids:
                fail(f"round {round_.get('round_id')} references unknown added rule: {rule_id}")
        for rule_id in round_.get("rules_modified", []):
            if rule_id in rule_ids:
                continue
            if "/" in rule_id or "\\" in rule_id or rule_id.startswith("review-") or rule_id.startswith("assess-"):
                continue
            if " " in rule_id or rule_id.endswith("wording") or rule_id.endswith("checklist"):
                continue
            # Some modified entries are artifact labels rather than rule IDs; allow lower-case descriptions.
            if rule_id and rule_id[0].islower():
                continue
            fail(f"round {round_.get('round_id')} references unknown modified rule/artifact: {rule_id}")

    for skill in REQUIRED_SKILLS:
        skill_path = ROOT / "skills" / skill / "SKILL.md"
        mirror_path = ROOT / ".agents" / "skills" / skill / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        mirror_text = mirror_path.read_text(encoding="utf-8")
        if text != mirror_text:
            fail(f"mirrored skill differs from root skill: {skill}")
        missing_headings = [heading for heading in SKILL_HEADINGS if heading not in text]
        if missing_headings:
            fail(f"skill {skill} missing headings: {', '.join(missing_headings)}")

    for dry_run_path in [
        "examples/toy_full_draft_pack/ASCReview_DryRunFindings.toy_full.json",
        "examples/toy_biomed_genomics_pack/ASCReview_DryRunFindings.toy_biomed.json",
    ]:
        dry_run = load_json(dry_run_path)
        if dry_run.get("target_section") != "full_draft":
            fail(f"toy dry-run findings must target full_draft: {dry_run_path}")
        for tag in dry_run.get("evidence_tags_used", []):
            if tag not in EVIDENCE_TYPES:
                fail(f"invalid toy dry-run evidence tag in {dry_run_path}: {tag}")
        for field in ["claim_calibration", "data_method_traceability", "policy_guideline_boundaries"]:
            if field not in dry_run:
                fail(f"toy dry-run findings missing field {field}: {dry_run_path}")

    partial_dry_run = load_json("examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json")
    if partial_dry_run.get("target_section") != "specialization_gate":
        fail("toy partial dry-run findings must target specialization_gate")
    partial_status = partial_dry_run.get("specialization_input_status", {})
    permissions = partial_status.get("review_permissions", {})
    for blocked_permission in [
        "can_review_draft_text",
        "can_score_against_rubric",
        "can_review_figures",
        "can_make_domain_factual_claims",
        "can_export_final_report",
    ]:
        if permissions.get(blocked_permission) is not False:
            fail(f"toy partial dry-run must keep permission false: {blocked_permission}")
    for classification in partial_dry_run.get("severity_classifications", []):
        if classification.get("severity_id") == "rubric_failure":
            fail("toy partial dry-run must not classify missing rubric as rubric_failure")

    revision_dry_run = load_json("examples/toy_revision_partial_pack/ASCReview_DryRunFindings.toy_revision_partial.json")
    if revision_dry_run.get("target_section") != "revision_gate":
        fail("toy revision partial dry-run findings must target revision_gate")
    revision_permissions = revision_dry_run.get("specialization_input_status", {}).get("review_permissions", {})
    for blocked_permission in [
        "can_review_draft_text",
        "can_score_against_rubric",
        "can_review_figures",
        "can_make_domain_factual_claims",
        "can_export_final_report",
    ]:
        if revision_permissions.get(blocked_permission) is not False:
            fail(f"toy revision partial dry-run must keep permission false: {blocked_permission}")
    for classification in revision_dry_run.get("severity_classifications", []):
        if classification.get("severity_id") == "rubric_failure":
            fail("toy revision partial dry-run must not classify missing revision inputs as rubric_failure")

    figure_absent = load_json("examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_absent.json")
    if figure_absent.get("target_section") != "figure_gate":
        fail("toy figure absent dry-run findings must target figure_gate")
    if figure_absent.get("specialization_input_status", {}).get("review_permissions", {}).get("can_review_figures") is not False:
        fail("toy figure absent dry-run must keep can_review_figures false")

    figure_present = load_json("examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_present.json")
    if figure_present.get("target_section") != "figure_gate":
        fail("toy figure present dry-run findings must target figure_gate")
    present_permissions = figure_present.get("specialization_input_status", {}).get("review_permissions", {})
    if present_permissions.get("can_review_figures") is not True:
        fail("toy figure present dry-run must set can_review_figures true")
    if present_permissions.get("can_score_against_rubric") is not False:
        fail("toy figure present dry-run must keep scoring false without rubric")

    for dry_run_path in [
        "examples/toy_full_draft_pack/ASCReview_DryRunFindings.toy_full.json",
        "examples/toy_biomed_genomics_pack/ASCReview_DryRunFindings.toy_biomed.json",
        "examples/toy_partial_specialization_pack/ASCReview_DryRunFindings.toy_partial.json",
        "examples/toy_revision_partial_pack/ASCReview_DryRunFindings.toy_revision_partial.json",
        "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_absent.json",
        "examples/toy_figure_permission_pack/ASCReview_DryRunFindings.figure_present.json",
    ]:
        dry_run = load_json(dry_run_path)
        for bucket in ["must_fix", "should_fix", "optional_polish"]:
            for item in dry_run.get(bucket, []):
                evidence_tag = item.get("evidence_tag")
                if evidence_tag and evidence_tag not in EVIDENCE_TYPES:
                    fail(f"invalid evidence_tag in {dry_run_path}: {evidence_tag}")
                severity_id = item.get("severity_id")
                if severity_id and severity_id not in SEVERITY_IDS:
                    fail(f"invalid severity_id in {dry_run_path}: {severity_id}")
                for rule_id in item.get("rule_ids", []):
                    if rule_id not in rule_ids:
                        fail(f"unknown rule_id in {dry_run_path}: {rule_id}")
        for classification in dry_run.get("severity_classifications", []):
            severity_id = classification.get("severity_id")
            if severity_id not in SEVERITY_IDS:
                fail(f"invalid severity classification in {dry_run_path}: {severity_id}")
            evidence_tag = classification.get("evidence_tag")
            if evidence_tag not in EVIDENCE_TYPES:
                fail(f"invalid severity evidence_tag in {dry_run_path}: {evidence_tag}")

    print("ASCREVIEW_VALIDATION_OK")
    print(f"sources={len(sources)}")
    print(f"provenance_rules={len(provenance.get('rules', []))}")
    print(f"distillation_rounds={sum(counts.values())}")
    print(f"skills={len(REQUIRED_SKILLS)}")


if __name__ == "__main__":
    main()
