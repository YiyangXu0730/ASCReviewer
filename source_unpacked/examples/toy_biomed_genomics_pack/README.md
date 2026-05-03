# Toy Biomedical Genomics Pack

This fixture is intentionally unrelated to the user's dissertation.

It exists to test ASCReview's generic biomedical/genomics workflow without reviewing real user writing or creating task-specific dissertation logic.

## Scenario

A fictional short report claims that a toy public single-cell/spatial cancer dataset shows immune exclusion and pathway activation in a mixed tumor sample. The draft intentionally contains common workflow failures: missing accession details, incomplete QC reporting, under-decoded UMAP/spatial figures, enrichment overclaiming, and pan-cancer overgeneralization.

## Files

- `ReviewTaskSpec.toy_biomed.json`
- `MarkingSchemeMap.toy_biomed.json`
- `SectionReviewContract.toy_biomed.json`
- `toy_biomed_genomics_draft.md`
- `MissingInformationRequest.toy_biomed.md`
- `ASCReview_DryRunReport.toy_biomed.md`
- `ASCReview_DryRunFindings.toy_biomed.json`

## Expected ASCReview Behavior

ASCReview may run a workflow test but should:

- avoid treating the toy topic as corpus evidence;
- keep scoring limited to the artificial toy rubric;
- identify missing accession, QC, normalization, clustering, annotation, figure, and enrichment details;
- distinguish source-pattern comments from toy-rubric requirements;
- mark factual oncology and mechanism claims provisional without a real source pack;
- avoid hardcoding any prostate cancer, AR signaling, ENZ resistance, ATM, ATR, or DDR logic.
