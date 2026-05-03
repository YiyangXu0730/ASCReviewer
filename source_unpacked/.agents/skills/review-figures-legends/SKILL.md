# Review Figures and Legends

## Purpose

Evaluate figure-panel logic, legend completeness, visual consistency, statistical notation, and figure-text alignment.

## When To Use

Use after specialization whenever figures, tables, plots, diagrams, or legends are part of the review scope.

## Required Inputs

- specialized review pack
- figure files or sufficiently detailed figure descriptions
- legends
- Results text that cites the figures
- marking scheme and section requirements
- source evidence index
- `patterns/figures/`

## Priority Rules

- Teacher or journal figure requirements dominate.
- Visual design and legend norms are secondary unless rubric/journal instructions require them.
- Scientific content concerns should be labeled separately from presentation concerns.
- Missing figure assets block visual-readability and panel-level findings; text-only figure-reference checks must be labeled as such.

## Evidence Rules

Use source-pattern evidence for figure design and official/rubric evidence for required figure elements. Do not infer data values from unavailable images.

## Positive Patterns

- `FIG-P1`: standalone legend.
- `FIG-P2`: narrative panel order.
- `FIG-P3`: encoding consistency.
- `FIG-P4`: reproducible computational figures.
- `FIG-P5`: figure supports one reviewable claim.
- `FIG-P6`: statistical annotation is decodable.
- `FIG-P7`: evidence-bearing panels link to source data.
- `FIG-P8`: genomics QC and transformation decodability.
- `FIG-P9`: embedding and spatial plot decodability.
- `FIG-P10`: multiplexed tissue imaging provenance.
- `FIG-P11`: figure asset permission gate.

## Negative Patterns

- legend cannot decode figure;
- panel order breaks argument;
- inconsistent encoding;
- statistical notation without meaning;
- missing computational provenance.
- statistical symbols without comparison path;
- schematic and evidence mixed;
- omics plot without QC or transformation context;
- embedding or spatial map without decoding path.
- multiplexed tissue image without marker/channel, segmentation, scale, region, or image-derived-data provenance.
- visual or panel-level critique generated without actual figure assets or sufficiently detailed figure descriptions.

## Checklist

- Is every panel defined in the legend?
- Are groups, units, n, symbols, tests, and error bars explained?
- Are figures cited in text in logical order?
- Do figure labels, text, and legends use consistent terminology?
- Can computational figures be traced to data/code/software?
- Does each figure have a clear evidence role?
- Are n, tests, corrections, comparison groups, symbols, and error bars decoded?
- Are evidence-bearing panels linked to source data or analysis provenance?
- Are conceptual schematics clearly labeled as model/hypothesis rather than demonstrated evidence?
- For omics figures, are normalization, transformation, filtering, threshold, scale, sample grouping, and data provenance decodable?
- For single-cell/spatial/pathway/proteomics figures, are object provenance, coordinates/embedding, annotations, counts, and color scales clear?
- For highly multiplexed tissue imaging, are tissue/sample context, markers/channels, acquisition platform, segmentation/cell-calling, regions, scale, color mapping, and source data traceable?
- Are actual figure assets, legends/captions, source data, and citing Results text available before making visual, panel-level, or figure-text consistency findings?

## Output Schema

```json
{
  "section": "figures_legends",
  "panel_logic": [],
  "legend_completeness": [],
  "figure_text_consistency": [],
  "statistics_notation": [],
  "visual_consistency": [],
  "must_fix": [],
  "should_fix": [],
  "optional_polish": [],
  "evidence_links": []
}
```

## Known Failure Modes

- Critiquing aesthetics while missing missing tests, n values, or group labels.
- Inferring content from a figure that was not provided.
- Treating all figures as journal figures when the task is a dissertation draft with different constraints.
- Treating schematic arrows as demonstrated mechanism.
- Failing to distinguish early-draft missing repository links from final-submission traceability gaps.
- Accepting a polished omics plot without checking preprocessing, normalization, thresholds, or source data.
- Reading biological meaning into UMAP geometry, spatial colors, or pathway dots without a decoding path.
- Treating multiplexed tissue image colors or neighborhoods as self-evident biology without channel, segmentation, region, and source-data provenance.
- Critiquing visual design or panel evidence when only a draft sentence says "Figure 1 shows...".

## Uncertainty Handling

- Mark visual/content findings provisional if figures or source data are missing.
- Separate readability, statistical decoding, and scientific validity.
- Do not infer exact data values from images unless values are provided.

## Provenance Expectations

- Use rule IDs such as `FIGURES-R1-STANDALONE-LEGEND`, `FIGURES-R2-RESOURCE-AND-DATA-LEGEND`, `FIGURES-R3-STATISTICAL-VISUAL-ANNOTATION`, `FIGURES-R4-GENOMICS-QC-DECODABILITY`, `FIGURES-R5-EMBEDDING-SPATIAL-PLOT-DECODE`, `FIGURES-R6-MULTIPLEXED-TISSUE-IMAGING-PROVENANCE`, and `FIGURES-R7-FIGURE-ASSET-GATE`.
- Link figure provenance comments to data/code/resource source IDs where relevant.
- Preserve rubric priority over journal-style visual preferences.

## Stop Conditions

Stop or mark provisional if:

- figure files/descriptions or legends are absent;
- the Results text needed for citation alignment is unavailable;
- statistical symbols cannot be interpreted from provided materials;
- scoring is requested without figure-related rubric criteria.
