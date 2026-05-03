# Figure and Legend Failure Modes

## FIG-F1: Legend Cannot Decode the Figure

- What it looks like: panel labels, groups, n values, tests, symbols, scale bars, or abbreviations are missing.
- Why it hurts: readers cannot evaluate the evidence without guessing.
- How to detect it: cover the main text and ask whether the figure can still be interpreted.
- Suggested revision action: add panel-by-panel legend details and define symbols/abbreviations.

## FIG-F2: Panel Order Breaks the Argument

- What it looks like: the figure starts with secondary analysis, jumps between comparisons, or is cited out of order.
- Why it hurts: weakens the Results narrative and causes avoidable confusion.
- How to detect it: first text citation order differs from panel order without good reason.
- Suggested revision action: reorder panels or rewrite the result paragraph to match evidence flow.

## FIG-F3: Inconsistent Encoding

- What it looks like: group colors, axis labels, abbreviations, units, or p-value symbols change across figures.
- Why it hurts: suggests careless presentation and can lead to wrong interpretation.
- How to detect it: compare labels and legends across all figures.
- Suggested revision action: standardize encodings and define them once.

## FIG-F4: Statistical Notation Without Meaning

- What it looks like: asterisks, brackets, p-values, error bars, or intervals are present but not explained.
- Why it hurts: readers cannot judge uncertainty or comparison structure.
- How to detect it: legend lacks test name, definition of error bars, or threshold definitions.
- Suggested revision action: add test, correction, group comparison, error-bar definition, and exact/threshold p-value policy.

## FIG-F5: Missing Computational Provenance

- What it looks like: heatmaps, volcano plots, survival curves, enrichment plots, or model outputs have no data/code/software provenance.
- Why it hurts: computational figures cannot be verified or regenerated.
- How to detect it: source data, script, package, version, filtering, and transformation cannot be identified.
- Suggested revision action: link figure to data accession, script/repository, package versions, and key parameters.

## FIG-F6: Statistical Symbols Without Comparison Path

- What it looks like: asterisks, brackets, adjusted p-values, intervals, or error bars appear without test, comparison, n, or uncertainty definition.
- Why it hurts: readers cannot evaluate the evidence strength or what was tested.
- How to detect it: legend has statistical marks but no decoding path to groups, tests, and error-bar definitions.
- Suggested revision action: add n, test, correction, comparison groups, and error-bar or interval definition.

## FIG-F7: Schematic and Evidence Mixed

- What it looks like: conceptual arrows, hypotheses, and measured results appear in one figure without distinguishing evidence from model.
- Why it hurts: can make speculative mechanism look demonstrated.
- How to detect it: panels mix cartoons and data while the legend uses the same certainty language for both.
- Suggested revision action: label schematic components as model/hypothesis and separate them from evidence-bearing panels.

## FIG-F8: Omics Plot Without QC or Transformation Context

- What it looks like: heatmaps, volcano plots, enrichment plots, survival curves, or genome-browser panels omit normalization, filtering, transformation, sample grouping, threshold, scale, or repository provenance.
- Why it hurts: the visual impression may depend heavily on hidden preprocessing or query choices.
- How to detect it: the reviewer cannot state what values are plotted and how they were generated.
- Suggested revision action: add comparison, data source, preprocessing, normalization/transformation, threshold/correction, sample count, and source-data reference.

## FIG-F9: Embedding or Spatial Map Without Decoding Path

- What it looks like: UMAPs, t-SNE plots, spatial maps, pathway dot plots, or proteomics summaries omit what points/spots/features represent, how labels were assigned, or what object generated the plot.
- Why it hurts: readers may mistake visualization geometry or annotation labels for direct biological proof.
- How to detect it: the legend does not identify the analysis object, coordinate system, annotation method, counts, color scale, or source-data path.
- Suggested revision action: add plot-object provenance, sample/cell/feature counts, annotation method, scale/threshold definitions, and source-data reference.

## FIG-F10: Multiplexed Tissue Image Without Provenance

- What it looks like: multiplexed tissue imaging panels show marker colors, neighborhoods, segmented cells, or regions without channel definitions, segmentation method, scale, region/sample context, or source-data path.
- Why it hurts: readers may mistake image-processing artifacts, color choices, or segmentation assumptions for biological evidence.
- How to detect it: the reviewer cannot trace the visual claim from tissue/sample and marker panel through acquisition, processing, segmentation, and plotted output.
- Suggested revision action: add marker/channel table, acquisition and processing summary, segmentation/cell-calling method, scale/region definitions, and source-data or repository reference.

## FIG-F11: Figure Review Without Figure Assets

- What it looks like: the review makes claims about panel design, visual readability, color scale, scale bars, plot content, or figure-text alignment when the figure file, legend, or detailed figure description was not provided.
- Why it hurts: the review fabricates visual evidence and can misdirect revision effort.
- How to detect it: the review cannot point to an available figure asset, legend, or source-data record for the finding.
- Suggested revision action: stop figure review or mark it provisional, then request figure files, legends/captions, source data, and citing Results text.
