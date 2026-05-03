# Long-Run Harness — ASCReview Build

## Purpose

This harness prevents ASCReview from being a shallow one-shot workflow. It forces sustained iteration over corpus building, skill distillation, adversarial QC, and workflow architecture.

## Timebox

- Target: 4–5 hours.
- Maximum: 6 hours.
- If the environment cannot actually run for that long, produce a partial build and a continuation prompt.

## Round count policy

Round count is secondary. Time and productive quality are primary.

Do not stop merely because "one round" is complete.

Continue until:

1. timebox is reached;
2. context cannot be safely compacted further;
3. external source access is unavailable and all offline-seed work is complete;
4. a hard blocker appears.

## Work allocation

Default allocation:

| Area | Target share |
|---|---:|
| Corpus policy, source index, pattern extraction | 55–65% |
| Adversarial QC and audit ledger | 15–25% |
| Core workflow structure | 10–15% |
| Schemas/templates/docs/examples | 5–10% |

## Execution loop

Each cycle must include:

1. **RunSupervisor checkpoint**
   - What was produced?
   - What remains?
   - What has become the highest-value next action?

2. **Builder/Distiller work**
   - Source policy or corpus or skill or workflow artifact.

3. **Adversarial audit**
   - Attack specificity, source quality, usefulness, legal/copyright handling, hallucination risk, and overfitting.

4. **Arbiter integration**
   - Patch artifact.
   - Preserve uncertainty.
   - Record what was rejected.

5. **Ledger update**
   - Write progress to `.ascreview/run_ledger.md`.

## Minimum cycle requirements

Run at least:

- 2 adversarial cycles for Introduction skill;
- 2 adversarial cycles for Methodology skill;
- 2 adversarial cycles for Results skill;
- 2 adversarial cycles for Discussion skill;
- 1 adversarial cycle for Figures/legends skill;
- 1 adversarial cycle for full task specialization.

If time remains, continue improving corpus and skills, not superficial docs.

## Evidence policy

Every rule must be tagged as one of:

- `source_pattern`
- `official_guideline`
- `teacher_rubric`
- `domain_expert_heuristic`
- `provisional`

Rules tagged only as `domain_expert_heuristic` must be treated as secondary and lower confidence.

## Stop conditions

Stop and report `NEEDS_REVIEW` if:

- the task requires copyrighted full-text storage with unclear license;
- the pack cannot distinguish generic core from task specialization;
- the build starts reviewing the dissertation before specialization;
- sources are fabricated or cannot be verified;
- context is too degraded and compaction fails.

## Final deliverable

The final deliverable must be a workflow package, not a single prompt.
