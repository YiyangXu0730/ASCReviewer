# ASCReview Section Review Prompt

Use this prompt only after task specialization is complete.

## Mission

Review one section against the specialized marking scheme, section contract, source evidence, and relevant distilled skills.

## Required Inputs

- `ReviewTaskSpec.json`
- `MarkingSchemeMap.json`
- relevant `SectionReviewContract.json`
- draft section text
- draft stage
- domain background pack
- source evidence index
- figure files or legends, if the section depends on figures
- prior review report, if this is a revision round

## Review Sequence

1. Confirm specialization artifacts exist.
2. Restate the section objective in one sentence.
3. Map rubric criteria to concrete section requirements.
4. Apply the relevant section skill:
   - introduction;
   - methodology;
   - results;
   - discussion;
   - figures and legends;
   - rubric alignment;
   - scientific claim strength;
   - bioinformatics methods.
5. Separate `must_fix`, `should_fix`, and `optional_polish`.
6. Label each finding with evidence type and confidence.
7. Provide paragraph-level comments and sentence-level examples only where they help revision.
8. Identify missing information that blocks reliable review.
9. Separate rubric failures, scientific validity risks, reporting completeness risks, and draft-stage caveats.

## Review Boundaries

- Do not score if the marking scheme does not permit or support scoring.
- Do not rewrite the full section unless explicitly asked.
- Do not make unsupported biomedical claims.
- Do not treat general writing preference as rubric failure.
- Do not use corpus sources as if they were the teacher rubric.
- Do not convert journal data/code/repository expectations into final-submission failures for an early draft unless the task requires that level of readiness.

## Output

Use `templates/SectionReviewReport.template.md` or the `ReviewReport.schema.json` shape.

Each issue must include:

- location;
- issue;
- why it matters for the rubric or scientific quality;
- suggested fix;
- evidence tag;
- confidence;
- limitation or uncertainty, if any.
- draft-stage caveat, if severity depends on draft maturity.
