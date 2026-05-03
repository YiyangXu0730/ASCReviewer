# DMD — ASCReview Core + Corpus & Skill Distillation Build

## 1. Product name

**ASCReview** — Academic / Scientific Critique Review workflow.

## 2. Business and user goal

The user needs a reusable agent/workflow that can evaluate and improve academic writing across:

- current dissertation writing;
- future PhD research papers;
- thesis chapters;
- review papers;
- methodology-heavy biomedical or bioinformatics manuscripts;
- section-level and full-draft revision loops.

The workflow must support immediate specialization to the user's current biomedical dissertation while remaining reusable for unrelated future papers.

## 3. Current thesis seed, not hardcoded core

The current topic may be used only as a seed example:

> Enzalutamide-resistant advanced prostate cancer; androgen receptor inhibitor resistance; observed ATM mutation context; ATR inhibitor–based synthetic lethality; possible interactions with other DDR inhibitors; ATM/ATR/DDR axis; therapeutic vulnerability and biomedical dissertation writing.

This topic must **not** be hardcoded into ASCReview Core.

## 4. Required architectural principle

ASCReview must be built as:

```text
ASCReview Core
  + Corpus Library
  + Distilled Review Skills
  + Adversarial QC Protocol
  + Task Specialization Pack
  + Section / Full Draft / Revision Review
```

## 5. What "general but specializable" means

The core workflow must not pretend that one universal rubric applies to all papers.

Every real review session must first compile a **Task Specialization Pack**:

```text
sessions/<task_id>/
  ReviewTaskSpec.json
  MarkingSchemeMap.json
  SectionRubricMap.json
  DomainBackgroundPack.md
  SourceEvidenceIndex.json
  SectionReviewContract.json
  ReportTemplate.md
  IterationLedger.json
  MissingInformationRequest.md
```

Only after specialization may ASCReview review drafts.

## 6. Corpus and skill layer

ASCReview must develop "reviewing experience" by building a curated library and distilling it into reusable skills.

The corpus must focus first on:

- biomedical academic writing;
- cancer biology;
- oncology;
- prostate cancer as optional seed only;
- DDR biology;
- ATM / ATR / synthetic lethality as optional seed only;
- genomics and bioinformatics methods writing;
- reporting guidelines and section-quality patterns.

The skill layer must distill patterns such as:

- what makes a good Introduction;
- what makes a good Methodology;
- what makes a good Results section;
- what makes a good Discussion;
- what makes a good figure legend;
- how to critique bioinformatics methods;
- how to align writing to teacher marking schemes;
- how to run revision-round comparison.

## 7. Mandatory adversarial QC

Because same-model self-critique often gives itself too much benefit of the doubt, ASCReview's build process must not be simple self-review.

In the single-window constraint, Codex must simulate three separated roles:

1. **LibraryBuilder-Distiller**
   - proposes source candidates;
   - extracts candidate patterns;
   - drafts skills;
   - attaches source IDs, confidence, and limitations.

2. **AdversarialAuditor**
   - assumes the Builder is lazy, overfitting, unsupported, or hallucinating;
   - attacks source quality, copyright risk, genericity, rubric alignment, biomedical accuracy, and usefulness;
   - must produce concrete objections.

3. **Arbiter-Integrator**
   - does not reward either side;
   - only keeps rules that survive evidence-based challenge;
   - patches skills;
   - preserves unresolved disputes.

## 8. Long-run build requirement

The build should not be a quick one-shot.

Target run: **4–5 hours**.

Maximum run: **6 hours**.

The harness should keep iterating until the timebox is reached or hard stop conditions are met. The number of rounds is less important than productive iteration.

Focus allocation:

- 55–65%: corpus library, source policy, pattern extraction, skill distillation;
- 15–25%: adversarial QC and audit ledger;
- 10–15%: ASCReview Core workflow structure;
- 5–10%: schemas, templates, install docs, examples.

## 9. Context compaction

When the context becomes too large or the agent detects loss of continuity risk, it must write:

```text
.ascreview/context/CONTEXT_SNAPSHOT_<n>.md
.ascreview/context/NEXT_PROMPT_TO_CONTINUE_<n>.md
.ascreview/context/ARTIFACT_INDEX_<n>.json
```

The next continuation must restart from those files, not from memory.

## 10. Non-goals

Do not:

- review the dissertation draft yet;
- hardcode one marking scheme;
- hardcode one thesis topic;
- pretend same-model self-QA is independent validation;
- store copyrighted full text without license permission;
- fabricate citations or guidelines;
- treat general LLM memory as source evidence.

## 11. Build deliverables

The final build must include:

- ASCReview Core prompts;
- Task Specialization prompt;
- Section Review prompts;
- Full Draft Review prompts;
- Revision Round prompts;
- Corpus/source policy;
- Corpus acquisition plan;
- distilled section-pattern library;
- skill library with `SKILL.md` files;
- adversarial QC protocol;
- provenance ledger schemas;
- templates for reports;
- usage guide;
- self-QA / adversarial QC report;
- next corpus expansion plan.
