# Context Compaction Protocol

## Why

The ASCReview build may run for 4–6 hours. Context may become too large. The agent must not rely on memory alone.

## Trigger conditions

Write a context snapshot when any of these occur:

- the agent detects it is losing track of artifacts;
- the run reaches a major milestone;
- many files have been created/modified;
- context feels near limit;
- before any long new corpus or skill-distillation phase.

## Required files

Create:

```text
.ascreview/context/CONTEXT_SNAPSHOT_<n>.md
.ascreview/context/NEXT_PROMPT_TO_CONTINUE_<n>.md
.ascreview/context/ARTIFACT_INDEX_<n>.json
```

## Context snapshot must include

- current mission;
- completed tasks;
- files created/modified;
- current unresolved disputes;
- current corpus status;
- current skill status;
- current QC status;
- next highest-value actions;
- stop conditions encountered;
- exact continuation instruction.

## Next prompt format

```text
Continue ASCReview long-run build from CONTEXT_SNAPSHOT_<n>.md and ARTIFACT_INDEX_<n>.json.
Do not restart from scratch.
Prioritize unresolved disputes and next actions.
Continue the LibraryBuilder ↔ AdversarialAuditor ↔ Arbiter loop.
Do not review the dissertation yet.
```

## Artifact index schema

```json
{
  "snapshot_id": "",
  "created_at": "",
  "mission": "",
  "files": [
    {
      "path": "",
      "status": "created | modified | pending | provisional",
      "summary": "",
      "next_action": ""
    }
  ],
  "open_questions": [],
  "next_actions": []
}
```

## Rule

If compaction is used, the next cycle must first read the latest context snapshot and artifact index.
