---
name: final-delivery-remediation
description: Use for ASCReview post-QC final-delivery remediation: final artifact index, canonical naming, POSIX-portable ZIP packaging, final delivery manifest, provenance meta-rule hygiene, and validation without expanding corpus or reviewing a dissertation.
---

# Final Delivery Remediation

## Purpose

Use this skill only after ASCReview has a completed build that needs narrow final-delivery repair. The goal is to make the final package auditable, portable, consistently named, and validation-backed.

## Scope

Allowed work:

- Create a final artifact index distinct from continuation indexes.
- Canonicalize delivery naming around `ASCReview`; preserve `ACS` names only as historical aliases.
- Produce a POSIX-portable ZIP whose member names use `/`, have no absolute paths, and contain no `..` traversal.
- Create a final delivery manifest and schema with hashes, sizes, artifact roles, validation results, and known limitations.
- Correct provenance meta-rules that imply a real teacher rubric exists when no rubric has been supplied.
- Add final delivery validators and negative-case validators.
- Write a remediation report, changed-file summary, validation transcript, and blocker log.

Forbidden work:

- Do not review, score, rewrite, or infer anything about the user's dissertation.
- Do not ask for a draft, marking scheme, figures/assets, source constraints, or assessment context.
- Do not expand the corpus or add new biomedical sources.
- Do not invent teacher-specific criteria, scores, rubrics, PMIDs, DOIs, licenses, or source facts.
- Do not change skill or corpus counts unless a validation fix absolutely requires it.

## Cycle Protocol

Run bounded cycles:

1. Inspect the specific artifact or rule under repair.
2. State the smallest viable patch.
3. Apply the patch.
4. Validate the touched area.
5. Run negative checks where feasible.
6. Record the cycle in the remediation ledger.
7. Stop when all acceptance gates pass or a blocker is documented.

Each cycle must produce changed files, validation output, or a justified decision not to change.

## Required Artifacts

Create or update:

- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/plan.md`
- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/ledger.md`
- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/validation_transcript.md`
- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/diff_summary.md`
- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/blockers.md`
- `.ascreview/runs/FINAL_DELIVERY_REMEDIATION_<timestamp>/cycle_ledger.jsonl`
- `.ascreview/context/ARTIFACT_INDEX_final.json`
- `FINAL_DELIVERY_MANIFEST.json`
- `schemas/FinalDeliveryManifest.schema.json`
- `scripts/repack_posix_zip.py`
- `scripts/validate_final_delivery.py`
- `scripts/validate_final_delivery_negative_cases.py`
- `FINAL_NAMING_CANONICALIZATION.md`
- `ASCReview_FINAL_DELIVERY_REMEDIATION_REPORT.md`

## Manifest Model

The final manifest should include:

- `manifest_id`, `created_at`, `project_canonical_name`, `delivery_status`.
- `source_package_root`, `final_delivery_folder`, and `canonical_zip`.
- `artifacts`: path, role, sha256, size_bytes, portability status, and notes.
- `validation`: commands, outputs, status, and timestamps where available.
- `provenance_hygiene`: rubric gate status and no-teacher-rubric assertion.
- `naming`: canonical name, historical aliases, and renamed deliverables.
- `limitations`: explicit non-specialization and no-dissertation-review limitations.

## Stop Gates

Stop with `NEEDS_REPAIR` if:

- Any required validator fails and cannot be restored.
- The canonical ZIP cannot be produced or inspected.
- Source verification or hash verification is impossible.
- A teacher rubric, dissertation content, or scoring criterion would need to be fabricated.

Stop with `FINAL_DELIVERY_REMEDIATION_COMPLETE` only when baseline validators, final delivery validator, and final delivery negative cases all pass.
