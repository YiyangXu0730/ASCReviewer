# ASCReview Corpus Source Policy

## Purpose

The ASCReview corpus exists to improve review judgment, not to archive articles. Store source metadata, provenance, and distilled patterns. Avoid storing full text unless reuse rights are verified and the source is needed for a lawful corpus artifact.

## Storage Classes

### `metadata_only`

Use for sources where ASCReview needs citation, URL, source type, and a note, but not reusable text.

Examples:

- official websites with link-only or unclear republication terms;
- journal author instructions;
- guideline portals;
- paywalled or free-to-read articles without a clear reuse license.

### `permitted_excerpt`

Use for short quotations or examples where fair use or explicit terms permit limited excerpting. Keep excerpts short and attach source IDs.

### `open_reuse_verified`

Use only when license is verified, for example CC BY articles. Even then, prefer summaries and distilled patterns over copied prose.

### `unknown`

Use temporarily during acquisition. Do not distill durable rules from unknown sources until metadata is verified.

## License Rules

- If no license is visible, mark `metadata_only`.
- If a PMC record is free-to-read but not in the PMC Open Access Subset or lacks a CC-like license, mark `metadata_only`.
- If a source is in the PMC Open Access Subset, record the specific license grouping before storing excerpts.
- For ICMJE Recommendations, link to the official page rather than republishing the document.
- For EQUATOR pages, treat the site as a guideline discovery/index source unless the linked guideline has its own reuse terms.

## Evidence Hierarchy

1. `teacher_rubric`: marking scheme, dissertation handbook, assignment brief, supervisor instruction.
2. `official_guideline`: ICMJE, EQUATOR-indexed reporting guideline, journal instructions, repository submission standards.
3. `source_pattern`: repeated pattern distilled from verified open access papers or methods/writing guidance.
4. `domain_expert_heuristic`: expert judgment not directly sourced; useful but secondary.
5. `provisional`: unverified or under-audited rule.

## Corpus Review Rule

Every corpus-derived rule must include:

- rule ID;
- skill ID;
- evidence tag;
- source IDs;
- confidence;
- limitation;
- failure mode;
- audit status.

## Prohibited

- fabricated DOIs, PMIDs, PMCIDs, policies, or titles;
- long copyrighted full text without verified permission;
- treating general model memory as source provenance;
- hardcoding a dissertation topic into the reusable core;
- letting the rule author approve the rule without adversarial audit.
