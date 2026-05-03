# Context Compaction


## Purpose

Compress the long-run build context into durable files.

## Required files

- `.ascreview/context/CONTEXT_SNAPSHOT_<n>.md`
- `.ascreview/context/NEXT_PROMPT_TO_CONTINUE_<n>.md`
- `.ascreview/context/ARTIFACT_INDEX_<n>.json`

## Rule

Continuation must restart from snapshot files, not memory.

