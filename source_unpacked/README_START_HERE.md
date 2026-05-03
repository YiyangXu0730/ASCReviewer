# ASCReview Codex Long-Run Build Pack v1

This package is intended to be uploaded to Codex together with the user's existing "generic workflow / Plan Library" pack.

## Mission

Build **ASCReview**, a reusable academic writing and dissertation-review workflow/agent system.

ASCReview must be both:

1. **General**: reusable for dissertations, thesis chapters, biomedical research articles, review papers, proposals, and future PhD-period writing tasks.
2. **Specializable**: before each real review task, it must compile a task-specific review environment from draft text, teacher marking scheme, figures/assets, source constraints, assessment context, section requirements, domain background, and supervisor feedback.

## Important boundary

Do **not** review the user's dissertation yet.

This package is for building the workflow, corpus layer, skill layer, adversarial QC protocol, schemas, templates, prompts, and usage guide.

A future session should upload:
- draft sections or full draft
- teacher marking scheme
- dissertation structure requirements
- section weighting
- figures/assets and legends, if figure review is requested
- source constraints and required citation boundaries
- assessment context, draft stage, target output, and deadline
- background pack or permission to use verified open sources
- supervisor feedback

Then ASCReview should first generate `SpecializationInputContract.json`. Only after the contract enables the relevant review permissions should it generate the rest of the task-specific specialization pack and begin section review.

## How to run in Codex

Upload this package and the user's generic workflow pack. Then paste:

```text
Read README_START_HERE.md and CODEX_MASTER_RUN_PROMPT.md. Execute the package as a long-run build task. Do not review my dissertation yet. Build ASCReview Core + Corpus Library + Distilled Skills + Adversarial QC Harness + templates/schemas/prompts. Respect the 4-5 hour target and 6-hour maximum timebox in docs/harness/LONG_RUN_HARNESS.md. Use context compaction when needed.
```

## Key files

- `DMD_ASCReview_Core_Corpus_Distillation.md` — development mandate document.
- `CODEX_MASTER_RUN_PROMPT.md` — main prompt to run the build.
- `docs/harness/LONG_RUN_HARNESS.md` — long-run execution protocol.
- `docs/harness/ADVERSARIAL_DISTILLATION_PROTOCOL.md` — LibraryBuilder vs Auditor vs Arbiter protocol.
- `docs/harness/CONTEXT_COMPACTION_PROTOCOL.md` — how to compress and continue if context grows too large.
- `docs/tasks/TASK-ASCREVIEW-0001_BUILD_CORE.md` — build generic ASCReview Core.
- `docs/tasks/TASK-ASCREVIEW-0002_CORPUS_SKILL_DISTILLATION.md` — build corpus and distilled skills.
- `.codex/agents/*.toml` — optional Codex custom agent profiles.
- `.agents/skills/*/SKILL.md` — skills to install or copy into a Codex-compatible workflow repository.
- `schemas/*.schema.json` — canonical output schemas.
- `templates/*` — report and artifact templates.

## Safety and quality rules

- Teacher marking schemes dominate all review judgments.
- Domain expertise is secondary and must never override explicit rubric requirements.
- The corpus layer must verify license and provenance before storing anything beyond metadata and short permitted excerpts.
- Do not fabricate papers, titles, DOIs, PMIDs, PMCIDs, guideline requirements, or journal policies.
- Same-model self-QA is weak. The workflow must simulate adversarial roles and preserve objections, unresolved disputes, and uncertainty.
- Missing draft, rubric, figures/assets, source constraints, or assessment context must disable the review modes they block instead of being silently inferred.
