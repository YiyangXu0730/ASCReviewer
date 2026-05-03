# Toy Figure Permission Pack

This non-dissertation regression fixture tests figure-review permission gating.

It has two machine-readable dry runs:

- `ASCReview_DryRunFindings.figure_absent.json`: no figure asset is supplied, so visual and panel-level review is blocked.
- `ASCReview_DryRunFindings.figure_present.json`: a toy SVG figure and legend are supplied, so limited figure review is allowed, but scoring remains blocked because no marking scheme is supplied.

The fixture is not source evidence, not a grading model, and not related to the user's dissertation.
