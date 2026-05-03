# ASCReview Context Snapshot 3

## Snapshot Metadata

- Snapshot ID: `CONTEXT_SNAPSHOT_3`
- Created at: `2026-05-02T10:14:45.6018181+08:00`
- Continuation run: `.ascreview/runs/RUN_20260502_100153_ledger.md`
- Continuation source used: `.ascreview/context/CONTEXT_SNAPSHOT_2.md`
- Mode: ASCReview workflow package build only
- Dissertation review: not performed
- Marking scheme request: not made
- Specialization session: not started

## Current Build State

- Source index count: 32 sources.
- Provenance ledger count: 30 rules.
- Adversarial distillation ledger count: 26 rounds.
- Skill count: 9 root skills and 9 mirrored `.agents/skills` copies.
- File inventory after this continuation: at least 112 files before this snapshot set.
- Validation status before snapshot: passing.

## Completed In This Continuation

### Cycle 1: Corpus Expansion and Source Quality

The source index was expanded from 17 to 32 sources. New sources covered reporting standards, journal/source guidance, bioinformatics/genomics methods examples, and optional cancer/prostate-cancer domain seeds. The optional prostate-cancer and enzalutamide-resistance adjacent sources remain metadata-only seed material and do not hardcode the generic ASCReview Core.

Added source families include ARRIVE 2.0, FAIR, TRIPOD, TRIPOD+AI, SAMPL, BRISQ, Nature reporting standards, BMC Cancer author guidance, Cell Press STAR Methods/key resources guidance, JCI guidance, DESeq2, cBioPortal, TCGA prostate adenocarcinoma, and metastatic castration-resistant prostate cancer genomics.

Reuse discipline was preserved. Open-reuse status was recorded only when clear; journal policy pages, PubMed pages, and uncertain source examples were marked metadata-only. No copyrighted full text was stored.

### Cycle 2: Pattern and Skill Distillation

The provenance ledger was expanded from 13 to 30 rules. New rules addressed study-type scope, public data rationale, ARRIVE/Biospecimen/key-resource reporting, data/code access conditions, denominators and exclusions, underlying-data traceability, preclinical-model limits, prediction-model limits, resource and data figure legends, statistical visual annotation, RNA-seq design reporting, public cancer-portal provenance, guideline-as-support not scoring, revision traceability, and translational evidence ladders.

Pattern files were improved across:

- `patterns/introduction/`
- `patterns/methodology/`
- `patterns/results/`
- `patterns/discussion/`
- `patterns/figures/`

All 9 skills were updated and mirrored into `.agents/skills/`. Each now includes added uncertainty handling and provenance expectations, with stronger biomedical, bioinformatics, evidence-linkage, and claim-calibration checks.

### Cycle 3: Adversarial QC Deepening

The distillation ledger was expanded from 12 to 26 rounds. The continuation minimums were exceeded:

- Introduction: 4 total rounds.
- Methodology: 4 total rounds.
- Results: 4 total rounds.
- Discussion: 4 total rounds.
- Figures/legends: 3 total rounds.
- Bioinformatics methods: 3 total rounds.
- Rubric alignment: 2 total rounds.
- Revision-round compare: 2 total rounds.

The QC report was updated with accepted, rejected, downgraded, and unresolved rule disputes. Important rejected or downgraded claims included:

- ARRIVE does not apply to every preclinical study.
- DESeq2 must not be treated as a mandatory RNA-seq method.
- Public cancer-genomics portal findings are not automatically clinical evidence.
- Repository/code gaps should not be labeled misconduct without evidence.

### Cycle 4: Workflow, Schema, Template, and Validator Improvements

`scripts/validate_ascreview_build.py` was strengthened to check higher round-count thresholds, duplicate IDs, valid evidence tags, valid audit statuses, source ID resolution, QC rule references, and exact sync between root and mirrored skill files.

Schemas and templates were updated to include draft-stage, assessment/venue, specialization-gate, evidence-tag, uncertainty, and draft-stage caveat fields. Core prompts were improved for draft-stage caveats, source provenance, public-data validation, and revision traceability.

A non-dissertation toy full-draft fixture was added under `examples/toy_full_draft_pack/` for future workflow testing without touching the user's dissertation.

## Validation State

Most recent validation before this snapshot:

```text
python scripts\validate_pack.py
VALIDATION_OK

python scripts\validate_ascreview_build.py
ASCREVIEW_VALIDATION_OK
Source count: 32
Provenance rule count: 30
Distillation round count: 26
Skill count: 9
```

Final validation should be rerun after this snapshot and index are written.

## Files Created Or Modified In This Continuation

- `.ascreview/runs/RUN_20260502_100153_plan.md`
- `.ascreview/runs/RUN_20260502_100153_ledger.md`
- `.ascreview/context/ARTIFACT_INDEX_latest.json`
- `library/source_index.seed.json`
- `library/provenance_ledger.seed.json`
- `patterns/introduction/*`
- `patterns/methodology/*`
- `patterns/results/*`
- `patterns/discussion/*`
- `patterns/figures/*`
- `skills/*/SKILL.md`
- `.agents/skills/*/SKILL.md`
- `qc/distillation_round_ledger.seed.json`
- `qc/adversarial_qc_report.md`
- `scripts/validate_ascreview_build.py`
- `schemas/*`
- `templates/*`
- `examples/toy_full_draft_pack/*`
- `ascreview/ASCReview_*_PROMPT.md`

## Retained Uncertainty

- Metadata-only journal/source pages should not be used for long excerpts unless reuse status is checked later.
- Optional prostate-cancer and AR/DDR-related sources are seed examples only; they are not generic ASCReview requirements.
- Reporting guidelines support review quality but do not create grading criteria without a teacher rubric.
- Draft-stage severity calibration still requires the future user's draft stage and assessment context.
- Bioinformatics pattern rules remain method-family specific and must not be converted into software mandates.

## Recommended Next Build Step

Run a 2-4 hour source-expansion and dry-run validation pass:

1. Add more verified open-access examples from cancer biology, oncology, genomics, and biomedical methods journals.
2. Add more negative and boundary-case patterns for overreach, missing evidence linkage, missing method reproducibility, and unsupported translational claims.
3. Run the toy full-draft fixture through the generic prompt workflow and patch any schema/template gaps found.
4. Keep all dissertation-specific specialization blocked until the user explicitly supplies the required dissertation materials in a future session.

## Hard Stop Status

No hard stop condition was triggered. Validation was passing before this snapshot, and no source fabrication or dissertation review occurred.
