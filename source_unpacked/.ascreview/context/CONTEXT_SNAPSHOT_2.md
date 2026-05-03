# ASCReview Context Snapshot 2

## Current Mission

Build ASCReview Core + Corpus Library + Distilled Skills + Adversarial QC Harness + templates/schemas/prompts. Do not review the user's dissertation yet.

## Completed Since Snapshot 1

- Mirrored enriched skills into `.agents/skills/` for compatibility with the package's existing skill layout.
- Added `scripts/validate_ascreview_build.py`.
- Added `examples/toy_specialization_pack/` for non-dissertation specialization testing.
- Re-ran both validation scripts successfully.
- Appended RunSupervisor Checkpoint 2 to `.ascreview/run_ledger.md`.

## Current Validation Status

- `python scripts/validate_pack.py`: `VALIDATION_OK`
- `python scripts/validate_ascreview_build.py`: `ASCREVIEW_VALIDATION_OK`
- Source count: 17
- Provenance rule count: 13
- Distillation round count: 12
- Skill count: 9
- Package file inventory: 100 files

## Current Unresolved Disputes

- Supervisor/institution-specific writing preferences remain unknown until the real marking scheme and handbook are provided.
- Article-style guidance may be useful but cannot override dissertation-specific requirements.
- Additional cancer biology and genomics corpus sources should be added in a future expansion round.
- Some optional citation metadata should be rechecked before citation export.

## Current Corpus Status

The corpus has a legally cautious source policy, acquisition plan, seed source index, and provenance ledger. It stores metadata and distilled patterns rather than full text.

## Current Skill Status

The nine main skills exist in both:

- `skills/*/SKILL.md`
- `.agents/skills/*/SKILL.md`

The skills are complete enough for installation/testing, subject to future corpus enrichment.

## Current QC Status

The harness minimum round counts are satisfied and recorded in:

- `qc/adversarial_qc_report.md`
- `qc/distillation_round_ledger.seed.json`

## Files Created or Modified Since Snapshot 1

- `.agents/skills/assess-bioinformatics-methods/SKILL.md`
- `.agents/skills/assess-rubric-alignment/SKILL.md`
- `.agents/skills/assess-scientific-claim-strength/SKILL.md`
- `.agents/skills/review-discussion/SKILL.md`
- `.agents/skills/review-figures-legends/SKILL.md`
- `.agents/skills/review-introduction/SKILL.md`
- `.agents/skills/review-methodology/SKILL.md`
- `.agents/skills/review-results/SKILL.md`
- `.agents/skills/revision-round-compare/SKILL.md`
- `scripts/validate_ascreview_build.py`
- `examples/toy_specialization_pack/*`
- `.ascreview/run_ledger.md`
- `.ascreview/context/CONTEXT_SNAPSHOT_2.md`
- `.ascreview/context/NEXT_PROMPT_TO_CONTINUE_2.md`
- `.ascreview/context/ARTIFACT_INDEX_2.json`

## Next Highest-Value Actions

1. Expand source index with verified open access cancer biology/genomics papers.
2. Add more source-derived, not heuristic-only, rules to provenance ledger.
3. Run additional adversarial rounds on bioinformatics and scientific-claim-strength skills.
4. Add a toy full-draft review fixture that remains unrelated to the user's dissertation.
5. Once real dissertation materials are supplied in a future session, create a task-specific specialization pack before reviewing anything.

## Stop Conditions Encountered

None.

## Exact Continuation Instruction

Continue ASCReview long-run build from `CONTEXT_SNAPSHOT_2.md` and `ARTIFACT_INDEX_2.json`.
Do not restart from scratch.
Prioritize unresolved disputes and next actions.
Continue the LibraryBuilder -> AdversarialAuditor -> Arbiter loop.
Do not review the dissertation yet.
