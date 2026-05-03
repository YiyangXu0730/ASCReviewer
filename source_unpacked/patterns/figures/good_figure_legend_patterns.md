# Good Figure and Legend Patterns

## FIG-P1: Standalone Legend

- Description: A figure legend should allow a reader to understand the panel logic, groups, measurements, statistics, symbols, abbreviations, and scale/normalization without searching the Methods for basic decoding.
- When it applies: all scientific figures and dissertation figure legends.
- Source/provenance ID: `FIGURES-R1-STANDALONE-LEGEND`; `PATTERN-BETTER-FIGURES-2014`; `GUIDE-ICMJE-MANUSCRIPT`.
- Positive example summary: Each panel is named, groups and n are defined, error bars and tests are explained, abbreviations are expanded, and scale bars/units are stated.
- Failure mode: legend only restates the title or omits symbols and group definitions.
- Review checklist use: For each panel, identify what, groups, units, n, test, symbols, and takeaway.

## FIG-P2: Narrative Panel Order

- Description: Figure panels should be arranged and cited in the same logical order as the Results narrative.
- When it applies: multi-panel figures and result-heavy chapters.
- Source/provenance ID: `RESULTS-R1-EVIDENCE-BEFORE-INTERPRETATION`; `PATTERN-BETTER-FIGURES-2014`.
- Positive example summary: Figure 1A shows design/sample summary, 1B primary result, 1C validation or secondary analysis.
- Failure mode: text jumps between panels or uses a figure as a data dump.
- Review checklist use: Trace first mention of each panel and check whether panel order supports the argument.

## FIG-P3: Encoding Consistency

- Description: Groups, colors, labels, axes, units, and statistical symbols should be consistent across figures and text.
- When it applies: figure sets, tables, and repeated experimental groups.
- Source/provenance ID: `PATTERN-BETTER-FIGURES-2014`.
- Positive example summary: Control is always the same color/label, axes use the same units, and symbols mean the same p-value thresholds.
- Failure mode: group colors or abbreviations change across panels.
- Review checklist use: Build a label/color/unit glossary and compare figures.

## FIG-P4: Reproducible Computational Figures

- Description: Where figures are generated computationally, code, data source, software, and key parameters should be findable or described.
- When it applies: bioinformatics plots, genomics figures, computational models, and statistical visualizations.
- Source/provenance ID: `PATTERN-BETTER-FIGURES-2014`; `PATTERN-REPRO-COMP-2013`; `BIOINFO-R1-CODE-DATA-AVAILABILITY`.
- Positive example summary: A plotted analysis cites the script/repository, data accession, package versions, and filtering choices.
- Failure mode: plot cannot be regenerated and visual transformation is unexplained.
- Review checklist use: Ask whether a future reviewer could identify the data and code used for the figure.

## FIG-P5: Figure Supports One Reviewable Claim

- Description: Each figure should have a clear evidence role and avoid overloading unrelated claims into one panel set.
- When it applies: result figures, dissertation chapters, review figures, and model schematics.
- Source/provenance ID: `PATTERN-PAPER-STRUCTURE-2017`; `PATTERN-BETTER-FIGURES-2014`.
- Positive example summary: A figure answers one result question and the caption aligns with that question.
- Failure mode: a multi-panel figure mixes background, method, exploratory analysis, and conclusion without a clear logic.
- Review checklist use: Write one claim the figure supports; if impossible, revise organization.

## FIG-P6: Statistical Annotation Is Decodable

- Description: Figure legends should define group sizes, tests, correction approach where relevant, error bars or intervals, comparison brackets, symbols, and thresholds.
- When it applies: figures with statistical comparisons, omics plots, cohort plots, preclinical experiments, and clinical data summaries.
- Source/provenance ID: `FIGURES-R3-STATISTICAL-VISUAL-ANNOTATION`.
- Positive example summary: The legend states n per group, test used, error-bar meaning, adjustment method, and meaning of asterisks.
- Failure mode: statistical symbols appear without explaining what was compared or how uncertainty is displayed.
- Review checklist use: Ask whether the reader can decode every symbol and uncertainty display without guessing.
- When it does not apply: conceptual schematics with no quantitative comparison.

## FIG-P7: Evidence-Bearing Panels Link to Source Data

- Description: Panels that carry core evidence should be traceable to source data, code, resource identifiers, accession IDs, or supplementary tables.
- When it applies: computational figures, genomics plots, microscopy quantification, graphs supporting main claims, and public-database analyses.
- Source/provenance ID: `FIGURES-R2-RESOURCE-AND-DATA-LEGEND`; `RESULTS-R4-UNDERLYING-DATA-TRACE`.
- Positive example summary: A heatmap legend points to the dataset accession, analysis method, and source table for plotted values.
- Failure mode: a panel is persuasive visually but cannot be traced to data or analysis provenance.
- Review checklist use: For each evidence-bearing panel, identify source data and generation method.
- When it does not apply: purely illustrative schematics that are clearly labeled as conceptual.

## FIG-P8: Genomics QC and Transformation Decodability

- Description: Genomics and bioinformatics figure legends should make sample grouping, QC state, normalization, transformation, filtering, thresholds, scale, and repository provenance decodable.
- When it applies: heatmaps, volcano plots, enrichment plots, genome-browser tracks, survival plots, expression plots, and pathway visualizations.
- Source/provenance ID: `FIGURES-R4-GENOMICS-QC-DECODABILITY`; `BIOINFO-R4-RNASEQ-PIPELINE-QC`.
- Positive example summary: A volcano plot legend states comparison, n, normalization, threshold/correction, gene universe, annotation version or package, and source table.
- Failure mode: a genomics plot looks polished but hides what was filtered, transformed, normalized, or tested.
- Review checklist use: Decode every axis, threshold, color, scale, group, and data source before accepting the figure's claim.
- When it does not apply: non-computational schematics or figures whose data provenance is fully explained elsewhere and clearly cross-referenced.

## FIG-P9: Embedding and Spatial Plot Decodability

- Description: Single-cell, spatial, pathway, and proteomics figures should decode the plotted object, embedding or coordinate system, annotations, color scales, thresholds, feature sets, sample/cell counts, and source provenance.
- When it applies: UMAP/t-SNE, spatial maps, cluster marker plots, ligand-receptor plots, pathway dot plots, heatmaps, and proteomics summaries.
- Source/provenance ID: `FIGURES-R5-EMBEDDING-SPATIAL-PLOT-DECODE`.
- Positive example summary: A spatial transcriptomics figure states tissue region, spot/cell resolution, coordinate/image registration, deconvolution method, color scale, marker/pathway set, sample count, and source-data location.
- Failure mode: visual separation, spatial neighborhood, or pathway activity is persuasive but impossible to decode or reproduce.
- Review checklist use: Ask what each point/spot/pixel/feature represents and how labels or colors were assigned.
- When it does not apply: non-data schematics or simple bar/line plots already covered by statistical-annotation patterns.

## FIG-P10: Multiplexed Tissue Imaging Provenance

- Description: Highly multiplexed tissue imaging figures should make tissue/sample context, markers/channels, acquisition platform, processing, segmentation/cell-calling, spatial regions, color mapping, scale, and source-data provenance traceable.
- When it applies: multiplexed immunofluorescence, imaging mass cytometry, MIBI, CODEX/PhenoCycler-like panels, and imaging-based spatial assays.
- Source/provenance ID: `FIGURES-R6-MULTIPLEXED-TISSUE-IMAGING-PROVENANCE`; `GUIDE-MITI-2022`; `GUIDE-MITI-CONSORTIUM`.
- Positive example summary: A tissue image legend states specimen/region, marker panel, channel mapping, segmentation method, cell/region count, scale, normalization/processing route, and repository/source-data reference.
- Failure mode: colored tissue neighborhoods or marker states look convincing but cannot be traced to channels, segmentation, regions, scale, or source data.
- Review checklist use: Ask whether every color and cell/region label can be traced from image acquisition to processed data and legend.
- When it does not apply: ordinary low-plex microscopy, conceptual diagrams, or non-imaging spatial data already covered by other plot patterns.

## FIG-P11: Figure Asset Permission Gate

- Description: Figure review should first record whether actual figure assets, legends/captions, source data, and citing Results text are available before making visual, panel-level, statistical, or figure-text alignment findings.
- When it applies: every figure, table, plot, image, graph, schematic, or legend review.
- Source/provenance ID: `FIGURES-R7-FIGURE-ASSET-GATE`.
- Positive example summary: A review states that visual/panel judgments are allowed because figure files and legends are present, while source-data checks remain provisional until source data are supplied.
- Failure mode: a reviewer criticizes colors, panel layout, scale bars, or figure-text consistency without seeing the figure or a detailed description.
- Review checklist use: Mark each figure input as asset present, legend present, source data present, Results citation present, or missing before reviewing.
- When it does not apply: it always applies as a gate, even if the result is "figure review unavailable."
