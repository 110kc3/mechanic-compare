# Evaluation briefs

`briefs.json` contains ten fixed tasks with reviewer expectations tied to this seed. **No independent agent benchmark has been run.** Expectations are not benchmark results and do not establish that all eligible implementations have been found.

Run each brief twice in fresh agent sessions with the same model, tool access and time limit:

1. Baseline: ordinary web/code search, without this dataset.
2. Assisted: the same tools plus this dataset and agent guide.

Hide the `expected` field from both agents. Alternate run order. Record the model/version, prompt, tool access, date, elapsed time, token use when observable, final answer and source links. Do not execute mod installers to answer a discovery question.

Review each answer on four binary criteria: respects target constraints; identifies appropriate candidates or correctly states the coverage gap; cites exact supporting code/docs; separates unknowns and untested claims. Log material errors separately (e.g. claiming C# runs in GDScript-only Godot or that a host-specific mod is an engine-independent library).

Measure quality and investigation time against the same tasks. The [traction gate](../docs/traction.md) requires observed improvement; schema checks and agreement with our own expected answers cannot demonstrate it.

Publish redacted artifacts and environment details before claiming results. Existing public data might occur in a model's training; this is a practical workflow comparison, not a leakage-free research benchmark.
