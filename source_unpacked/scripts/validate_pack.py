#!/usr/bin/env python3
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README_START_HERE.md",
    "DMD_ASCReview_Core_Corpus_Distillation.md",
    "CODEX_MASTER_RUN_PROMPT.md",
    "docs/harness/LONG_RUN_HARNESS.md",
    "docs/harness/ADVERSARIAL_DISTILLATION_PROTOCOL.md",
    "docs/harness/CONTEXT_COMPACTION_PROTOCOL.md",
    "docs/tasks/TASK-ASCREVIEW-0001_BUILD_CORE.md",
    "docs/tasks/TASK-ASCREVIEW-0002_CORPUS_SKILL_DISTILLATION.md",
    "AGENTS.md",
    ".codex/config.toml",
    "schemas/ReviewTaskSpec.schema.json",
    "schemas/SpecializationInputContract.schema.json",
    "schemas/MarkingSchemeMap.schema.json",
    "schemas/SectionReviewContract.schema.json",
    "schemas/ReviewReport.schema.json",
    "schemas/SourceIndex.schema.json",
    "schemas/ProvenanceLedger.schema.json",
    "schemas/DistillationRoundLedger.schema.json",
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print("VALIDATION_FAILED")
    for p in missing:
        print(f"missing: {p}")
    sys.exit(1)

# ensure JSON files parse
for p in ROOT.rglob("*.json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print("VALIDATION_FAILED")
        print(f"invalid json: {p}: {e}")
        sys.exit(1)

print("VALIDATION_OK")
