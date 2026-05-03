# ASCReview Context Snapshot 7

## Current Mission

Continue building ASCReview as a unified, reusable, specialization-ready review workflow. The final deliverable after final report completion should be placed in a new Desktop folder named `The Final ACS Review`.

The user's dissertation has not been reviewed. No marking scheme was requested. No dissertation-specific specialization was started.

## Run

- Run ID: `RUN_20260503_062733`
- Snapshot time: `2026-05-03T07:02:50.9252865+08:00`
- Continuation source used: `.ascreview/context/CONTEXT_SNAPSHOT_6.md`
- Run plan: `.ascreview/runs/RUN_20260503_062733_plan.md`
- Run ledger: `.ascreview/runs/RUN_20260503_062733_ledger.md`
- Active heartbeat automation: `ascreview-continue-until-final-report-folder`

## Completed Since Snapshot 6

### Negative Validator Self-Tests

- Added `scripts/validate_negative_cases.py`.
- Negative cases now confirm validator failure for:
  - unknown source reuse status;
  - missing distillation auditor objection;
  - unknown dry-run rule ID;
  - partial specialization permission incorrectly enabled;
  - partial specialization rubric-failure misuse;
  - revision permission incorrectly enabled without inputs;
  - absent figure asset with figure permission enabled;
  - present figure asset with scoring enabled despite absent rubric.

### Revision-Round Partial Fixture

- Added `REVISION-R4-REVISION-INPUT-GATE`.
- Updated `skills/revision-round-compare/SKILL.md` and mirror.
- Added `examples/toy_revision_partial_pack/`.
- Validator now checks revision-gate target and blocked permissions.

### Figure-Asset Permission Fixture

- Added `FIGURES-R7-FIGURE-ASSET-GATE`.
- Updated `skills/review-figures-legends/SKILL.md` and mirror.
- Added `FIG-P11` and `FIG-F11`.
- Added `examples/toy_figure_permission_pack/` with absent and present dry-run findings.
- Validator now checks absent-asset blocks figure review, present-asset enables limited figure review, and scoring remains false without rubric.

### Adversarial QC

- Added rounds:
  - `REV-04`
  - `FIG-07`
  - `TOY-REVISION-01`
  - `TOY-FIGURE-01`
- Updated `qc/adversarial_qc_report.md`.

## Current Counts

- Sources: 65
- Provenance rules: 58
- Distillation/adversarial rounds: 58
- Skills: 9

## Validation Status

```text
python scripts\validate_pack.py -> VALIDATION_OK
python scripts\validate_ascreview_build.py -> ASCREVIEW_VALIDATION_OK
sources=65
provenance_rules=58
distillation_rounds=58
skills=9

python scripts\validate_negative_cases.py -> NEGATIVE_VALIDATION_OK
```

## New Rules Since Snapshot 6

- `REVISION-R4-REVISION-INPUT-GATE`
- `FIGURES-R7-FIGURE-ASSET-GATE`

## Important Rejected Rules Since Snapshot 6

- Revision partial context permits resolution classification or score movement.
- Visual figure critique can be generated from absent assets.
- Figure asset present means rubric scoring is allowed.

## Files Created Or Modified Since Snapshot 6

- `scripts/validate_negative_cases.py`
- `scripts/validate_ascreview_build.py`
- `library/provenance_ledger.seed.json`
- `skills/revision-round-compare/SKILL.md`
- `skills/review-figures-legends/SKILL.md`
- `.agents/skills/revision-round-compare/SKILL.md`
- `.agents/skills/review-figures-legends/SKILL.md`
- `patterns/figures/good_figure_legend_patterns.md`
- `patterns/figures/figure_legend_failure_modes.md`
- `examples/toy_revision_partial_pack/*`
- `examples/toy_figure_permission_pack/*`
- `qc/distillation_round_ledger.seed.json`
- `qc/adversarial_qc_report.md`
- `.ascreview/run_ledger.md`
- `.ascreview/runs/RUN_20260503_062733_plan.md`
- `.ascreview/runs/RUN_20260503_062733_ledger.md`

## Remaining Weaknesses

- Final-report scaffold and final packaging folder have not yet been produced because the final report is not complete.
- More malformed-artifact negative tests could be added later.
- More modality-specific source depth can still be added before stricter threshold-level rules.
- Real dissertation specialization remains blocked until the user explicitly supplies the required materials.

## Next Highest-Value Actions

1. Prepare final-report scaffold and final packaging plan for Desktop folder `The Final ACS Review`.
2. Continue any remaining bounded improvements only if they produce concrete validation or QC value.
3. At final-report point, run all validators, write final report, create `C:\Users\xyydsb666\Desktop\The Final ACS Review`, and place final report plus final ZIP/package there.

## Exact Continuation Instruction

Continue ASCReview long-run build from `.ascreview/context/CONTEXT_SNAPSHOT_7.md` and `.ascreview/context/ARTIFACT_INDEX_7.json`.

Do not review the dissertation. Do not ask for the marking scheme. Do not start dissertation-specific specialization. If final report is due, produce the final report, create Desktop folder `The Final ACS Review`, package the final product there, and then stop cleanly.
