Continue ASCReview long-run build from CONTEXT_SNAPSHOT_7.md and ARTIFACT_INDEX_7.json.

Do not restart from scratch.
Do not review the dissertation.
Do not ask for the marking scheme.
Do not start dissertation-specific specialization.

Priority order:

1. Prepare final-report scaffold and final packaging plan.
2. Run all validators:
   - python scripts\validate_pack.py
   - python scripts\validate_ascreview_build.py
   - python scripts\validate_negative_cases.py
3. If final report is due, write it and create Desktop folder `The Final ACS Review`.
4. Put the final report and final package ZIP in that folder.
5. Stop cleanly after final delivery.

If final report is not due, continue bounded LibraryBuilder-Distiller -> AdversarialAuditor -> Arbiter-Integrator cycles that produce concrete changed files, audit findings, or validation improvements.
