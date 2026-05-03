# GitHub Publication Manifest

## Repository

- Repository name: ASCReviewer
- Repository full name: YiyangXu0730/ASCReviewer
- Repository URL: https://github.com/YiyangXu0730/ASCReviewer
- Repository visibility: public user-provided target; private was recommended by workflow policy
- Repo creation method: user-created existing repository

## Delivery Identity

- Final transfer status: FINAL_TRANSFER_READY_WITH_EXTERNAL_RUN_EVIDENCE
- Evidence-source status: core artifacts from canonical ZIP/canonical folder; detailed 2H run evidence from external workspace
- Canonical ZIP SHA256: 45f06e6557945f3b01b0a1a5cc8dc9b151506ae93faa7d1c87737967449fa4c8
- Transfer wrapper ZIP SHA256: 11769f9b36816413590158e14a5562c734c9de72bf1ee9051b57fd72afc45893

## Large File Decision

- ZIP artifacts are below 50 MiB.
- Git LFS decision: normal Git commit is acceptable.

## Files Committed

- `README.md`
- `LICENSE_PENDING.md`
- `CHANGELOG.md`
- `docs/`
- `artifacts/canonical/`
- `artifacts/transfer/`
- `delivery/`
- `reports/`
- `manifests/`
- `run_evidence/`
- `source_unpacked/`
- `.github/workflows/validate.yml`

## Files Intentionally Excluded

- `ARTIFACT_INDEX_latest.json` was excluded from `source_unpacked` because it is a stale continuation index and must not be promoted as final.
- `THE FINAL ACS REVIEW.zip` was not committed as canonical.

## Local Validation Commands Run

- Canonical ZIP SHA256 and ZIP path safety check.
- Transfer wrapper SHA256 check.
- Large-file scan.
- Stale-state protection scan for final status docs.
- `python scripts/validate_pack.py` from `source_unpacked`.
- `python scripts/validate_ascreview_build.py` from `source_unpacked`.
- `python scripts/validate_negative_cases.py` from `source_unpacked`.

## Scope Confirmations

- No dissertation review was performed.
- No marking scheme was inferred.
- No corpus expansion was performed.
- The canonical ZIP was not mutated, rebuilt, or repacked.
- No token was printed or committed.

## Publication Result

- Commit hash: PENDING_PUSH
- Remote URL: https://github.com/YiyangXu0730/ASCReviewer.git
- Branch: main
