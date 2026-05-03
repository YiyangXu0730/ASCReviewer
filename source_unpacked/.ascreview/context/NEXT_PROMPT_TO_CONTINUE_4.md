# Next Prompt To Continue ASCReview Build From Snapshot 4

You are continuing the ASCReview long-run build.

Do not review my dissertation yet.
Do not ask for my marking scheme yet.
Do not start dissertation-specific specialization yet.

Begin by reading:

1. `README_START_HERE.md`
2. `CODEX_MASTER_RUN_PROMPT.md`
3. `docs/harness/LONG_RUN_HARNESS.md`
4. `docs/harness/ADVERSARIAL_DISTILLATION_PROTOCOL.md`
5. `docs/harness/CONTEXT_COMPACTION_PROTOCOL.md`
6. `.ascreview/context/CONTEXT_SNAPSHOT_4.md`
7. `.ascreview/context/ARTIFACT_INDEX_4.json`
8. `.ascreview/runs/RUN_20260502_102849_ledger.md`

Current build state:

- Sources: 44.
- Provenance rules: 40.
- Adversarial distillation rounds: 36.
- Skills: 9 root skills mirrored into 9 `.agents/skills` copies.
- Validation was passing after Cycle D and should be rerun at the start of the next session.

Next recommended build task:

Run a 2-4 hour ASCReview package improvement pass focused on verified open-access biomedical/cancer/genomics examples and a second non-dissertation biomedical toy fixture.

Priority order:

1. Add verified open-access sources for cancer biology mechanisms, oncology results/discussion examples, single-cell or spatial transcriptomics, proteomics, pathway/enrichment analysis, and figure/legend exemplars.
2. Mark reuse status conservatively; do not store full text unless reuse is verified.
3. Distill rules only through LibraryBuilder-Distiller, AdversarialAuditor, and Arbiter-Integrator cycles.
4. Build a second toy fixture that is biomedical/cancer/genomics flavored but explicitly unrelated to the user's dissertation.
5. Strengthen schema and validation if the toy run exposes gaps.
6. Update context and artifact indexes after major cycles.

Validation commands:

```powershell
python scripts\validate_pack.py
python scripts\validate_ascreview_build.py
```

Do not declare completion while validation fails.

Expected final output marker:

`ASCREVIEW_LONG_RUN_ITERATION_COMPLETE`
