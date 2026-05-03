# Next Prompt To Continue ASCReview Build From Snapshot 3

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
6. `.ascreview/context/CONTEXT_SNAPSHOT_3.md`
7. `.ascreview/context/ARTIFACT_INDEX_3.json`
8. `.ascreview/runs/RUN_20260502_100153_ledger.md`

Current continuation state:

- Source index: 32 sources.
- Provenance ledger: 30 rules.
- Adversarial distillation ledger: 26 rounds.
- Skills: 9 root skills mirrored into 9 `.agents/skills` copies.
- Validation was passing after Cycle 4 and should be rerun at the start of the next session.

Next recommended build task:

Run a 2-4 hour ASCReview package improvement pass focused on corpus expansion and dry-run workflow validation. Keep the generic core reusable and do not hardcode prostate cancer, enzalutamide resistance, ATM, ATR, DDR, or any user dissertation topic.

Priority order:

1. Add more verified open-access source metadata from biomedical writing, cancer biology, oncology, bioinformatics, genomics methods, figures/legends, and reporting guidelines.
2. Mark reuse status conservatively. Store metadata and distilled patterns only unless open reuse is verified.
3. Distill new source-linked rules through the LibraryBuilder-Distiller, AdversarialAuditor, and Arbiter-Integrator loop.
4. Add or revise pattern files only when rules survive adversarial review.
5. Run the non-dissertation fixture in `examples/toy_full_draft_pack/` through the generic prompt workflow to find schema, template, and prompt gaps.
6. Strengthen validation if gaps are found.
7. Update `.ascreview/context/ARTIFACT_INDEX_latest.json` and write a new context snapshot if the run is substantial.

Validation commands to run after major changes:

```powershell
python scripts\validate_pack.py
python scripts\validate_ascreview_build.py
```

Do not declare completion while either validation command fails.

Expected final output marker:

`ASCREVIEW_LONG_RUN_ITERATION_COMPLETE`
