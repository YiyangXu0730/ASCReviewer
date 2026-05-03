# ASCReview Context Snapshot 6

## Current Mission

Build ASCReview as a unified, reusable, specialization-ready academic/scientific review workflow. The core must later specialize from draft, marking scheme, figures/assets, source constraints, and assessment context.

The user's dissertation has not been reviewed. No marking scheme was requested. No dissertation-specific specialization was started.

## Run

- Run ID: `RUN_20260503_062733`
- Start time: `2026-05-03T06:27:33.3808787+08:00`
- Snapshot time: `2026-05-03T06:49:57.0871972+08:00`
- User target final-report time: `2026-05-03 07:30 Europe/London`
- Continuation source used: `.ascreview/context/CONTEXT_SNAPSHOT_5.md`
- Run plan: `.ascreview/runs/RUN_20260503_062733_plan.md`
- Run ledger: `.ascreview/runs/RUN_20260503_062733_ledger.md`
- Heartbeat automation: `ascreview-auto-iteration-until-london-07-30`

## Completed Cycles

- Cycle A: strengthened source/provenance schemas and schema-subset validation.
- Cycle B: added `SpecializationInputContract` schema/template and prompt/template integration.
- Cycle C: expanded modality corpus and provenance rules.
- Cycle D: added adversarial rounds for contract and modality rules.
- Cycle E: added partial-input specialization fixture and broader schema validation.
- Cycle F: added machine-readable partial-input dry-run findings and permission assertions.
- Cycle G: hardened distillation-round ledger schema.
- Cycle H: integrated docs and usage path.
- Cycle I: added dry-run finding reference validation.

## Current Counts

- Sources: 65
- Provenance rules: 56
- Distillation/adversarial rounds: 54
- Skills: 9 root skills mirrored to `.agents/skills`

## New Sources Added In This Run

- `METHOD-SC-MULTIMODAL-BEST-PRACTICES-2023`
- `GUIDE-AIRR-SHARING-2017`
- `GUIDE-AIRR-REPRESENTATION-2018`
- `GUIDE-AIRR-STANDARDS`
- `METHOD-LONG-READ-ANALYSIS-2020`
- `METHOD-DIA-SWATH-TUTORIAL-2018`
- `METHOD-PHOSPHOPROTEOMICS-CANCER-2023`
- `GUIDE-MITI-2022`
- `GUIDE-MITI-CONSORTIUM`

## New Rules Added In This Run

- `RUBRIC-R3-SPECIALIZATION-INPUT-GATE`
- `BIOINFO-R10-SC-MULTIMODAL-ROUTING`
- `BIOINFO-R11-AIRR-METADATA-ANNOTATION`
- `BIOINFO-R12-LONG-READ-PLATFORM-QC`
- `BIOINFO-R13-DIA-DDA-PROTEOMICS-MODE`
- `BIOINFO-R14-PHOSPHOPROTEOMICS-SITE-INFERENCE`
- `FIGURES-R6-MULTIPLEXED-TISSUE-IMAGING-PROVENANCE`

## Important Rejected Rules

- `SpecializationInputContract` can replace the actual marking scheme.
- Missing marking scheme blocks all non-scored formative review.
- All single-cell studies require multimodal integration.
- AIRR metadata standards apply to all immunology or all single-cell studies.
- Long-read sequencing is automatically more valid than short-read sequencing.
- DIA/SWATH is the default requirement for proteomics review.
- Phosphorylation or kinase enrichment proves causal pathway activation.
- MITI metadata checks apply to every figure.
- Partial specialization context permits draft review or rubric scoring.

## Validation Status

Final validation before snapshot:

```text
python scripts\validate_pack.py -> VALIDATION_OK
python scripts\validate_ascreview_build.py -> ASCREVIEW_VALIDATION_OK
sources=65
provenance_rules=56
distillation_rounds=54
skills=9
```

## Current Unresolved Weaknesses

- More negative validator self-tests would improve confidence.
- More source-depth is needed before threshold-level modality-specific rules are added.
- Revision-round and figure-asset edge-case fixtures are still missing.
- Real-session behavior still needs testing once actual user materials are supplied.
- Dissertation-specific specialization remains blocked until the user explicitly supplies the required materials.

## Files Created Or Modified In This Run

- `.ascreview/context/CONTEXT_SNAPSHOT_6.md`
- `.ascreview/context/NEXT_PROMPT_TO_CONTINUE_6.md`
- `.ascreview/context/ARTIFACT_INDEX_6.json`
- `.ascreview/context/ARTIFACT_INDEX_latest.json`
- `.ascreview/run_ledger.md`
- `.ascreview/runs/RUN_20260503_062733_plan.md`
- `.ascreview/runs/RUN_20260503_062733_ledger.md`
- `schemas/SourceIndex.schema.json`
- `schemas/ProvenanceLedger.schema.json`
- `schemas/DistillationRoundLedger.schema.json`
- `schemas/SpecializationInputContract.schema.json`
- `schemas/ReviewTaskSpec.schema.json`
- `schemas/ReviewReport.schema.json`
- `library/source_index.schema.json`
- `library/source_index.seed.json`
- `library/provenance_ledger.schema.json`
- `library/provenance_ledger.seed.json`
- `templates/source_index.seed.json`
- `templates/SpecializationInputContract.template.json`
- `templates/ReviewTaskSpec.template.json`
- `templates/SectionReviewReport.template.md`
- `templates/FullDraftReviewReport.template.md`
- `skills/assess-bioinformatics-methods/SKILL.md`
- `skills/review-figures-legends/SKILL.md`
- `skills/assess-rubric-alignment/SKILL.md`
- `skills/assess-scientific-claim-strength/SKILL.md`
- `.agents/skills/*/SKILL.md`
- `patterns/methodology/*`
- `patterns/figures/*`
- `examples/toy_partial_specialization_pack/*`
- `qc/distillation_round_ledger.schema.json`
- `qc/distillation_round_ledger.seed.json`
- `qc/adversarial_qc_report.md`
- `scripts/validate_pack.py`
- `scripts/validate_ascreview_build.py`
- `ascreview/ASCReview_CORE_PROMPT.md`
- `ascreview/ASCReview_SPECIALIZATION_PROMPT.md`
- `ascreview/USAGE_GUIDE.md`
- `ascreview/README_ASCReview.md`
- `README_START_HERE.md`
- `package_manifest.json`

## Next Highest-Value Actions

1. Add negative validator self-tests that intentionally assert failure paths.
2. Add revision-round partial-input fixture.
3. Add figure-asset absent/present fixture for visual-review permission gating.
4. Deepen modality source modules before adding stricter threshold-level rules.
5. Continue heartbeat cycles until the requested final-report time; if current time is at or after `2026-05-03 07:30 Europe/London`, write the final long-run report.

## Exact Continuation Instruction

Continue ASCReview long-run build from `.ascreview/context/CONTEXT_SNAPSHOT_6.md` and `.ascreview/context/ARTIFACT_INDEX_6.json`.

Do not restart from scratch. Do not review the dissertation. Do not ask for the marking scheme. Do not start dissertation-specific specialization. Continue bounded LibraryBuilder-Distiller -> AdversarialAuditor -> Arbiter-Integrator cycles. Run both validators before stopping each cycle. If at or after `2026-05-03 07:30 Europe/London`, produce the final report.
