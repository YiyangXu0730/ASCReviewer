# Delivery Status

Final status:

`FINAL_TRANSFER_READY_WITH_EXTERNAL_RUN_EVIDENCE`

This means:

- canonical ZIP integrity passed;
- canonical ZIP hash matched expected value;
- canonical ZIP had 170 members;
- canonical ZIP had no bad paths;
- core final artifacts were sourced from canonical ZIP/canonical folder;
- detailed 2H run evidence was harvested from an external workspace;
- stale latest index was not used as final.

This is not `FINAL_TRANSFER_READY_CANONICAL`.

The distinction is intentional and must be preserved.

Final-delivery validators may depend on Windows-specific local absolute paths when run from an unpacked artifact copy. In GitHub Actions they are allowed to run as non-blocking checks; baseline validators remain blocking when available.
