# Using the comparison with an agent

Read `data/implementations.json` and `comparisons/parkour.md` before making a recommendation.

Get the target engine/game and version, language restrictions, required moves, multiplayer needs, asset access and dependency constraints. Ask for a missing consequential constraint; otherwise state your assumptions.

For each candidate return:

- The relevant mechanic and **exact pinned evidence URL**.
- The integration boundary and work the host must provide.
- Requirements, exclusions and unresolved questions.
- Source-review and runtime status, separately.

Describe a candidate as a reference, library, mod or full project as appropriate. Filtering by `engine` means the implementation's existing engine context, not every possible host. `engine-independent` still requires an adapter.

Read the cited source before explaining detailed behaviour. The evidence `symbols` are navigation anchors; dependencies can extend beyond them. Treat undocumented mechanics as unknown. Never fill missing compatibility, networking or fidelity fields from a game's genre or reputation.

Licenses describe the declarations observed, not an asset audit or legal certification. In particular, keep unknown and conflicting declarations visible in the answer.

There are no independently measured agent benchmark results yet. `evaluation/briefs.json` contains reviewer expectations for an experiment, not model performance or comprehensive ground truth.
