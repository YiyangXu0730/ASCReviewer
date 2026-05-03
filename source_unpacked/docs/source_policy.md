# ASCReview Source Policy

## Purpose

ASCReview uses a corpus to gain reusable academic reviewing judgment. The corpus is not a dumping ground for full text.

## Allowed storage categories

### Metadata
Always allowed if lawfully accessed:
- title
- authors
- journal
- year
- DOI
- PMID/PMCID
- license
- URL
- article type
- section labels

### Permitted excerpts
Allowed only when license permits or excerpt is short and used for analysis:
- short examples of structure;
- section-level observations;
- paraphrased patterns.

### Distilled patterns
Preferred storage form:
- "Introduction moves from disease burden → mechanistic gap → aim."
- "Methods reports software versions and parameters."
- "Results avoids over-interpreting mechanism before Discussion."

### Full text
Do not store full text unless the source license clearly permits reuse.

## License rule

If unclear, mark:

```json
"reuse_status": "metadata_only"
```

## Source credibility hierarchy

1. Teacher marking scheme / official dissertation handbook.
2. Official reporting guidelines.
3. High-quality peer-reviewed open access articles.
4. Review articles and methods papers.
5. Domain expert heuristics, clearly marked secondary.
