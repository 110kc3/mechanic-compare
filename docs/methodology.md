# Evidence and limits

The seed was selected for variation: a portable Rust subsystem, two host-specific mods, a Godot C# controller, a Unity port and a simpler Unity movement baseline. It is not an exhaustive or ranked list.

## Source review

Each record stores a full Git commit ID, review date, evidence file paths and SHA-256 hashes of the fetched bytes. Source files were inspected as text; no upstream executable, installer or project was run. Mechanic entries mean implementation code is present in the cited file; they do not certify functionality or fidelity.

Evidence types distinguish code, documentation, license files and dated external listings. A source symbol narrows reading; it does not establish that the symbol alone contains a complete system. Integration and limitation statements are reviewed interpretations of the linked code/docs.

`python scripts/catalog.py check --verify-sources` re-fetches pinned GitHub files, checks their hashes and navigation symbols, and reports failures. It does not review the meaning of claims, audit upstream behavior, validate external listing text or execute upstream code. Offline CI validates schemas, references, pinning and generated output.

## Terms and assets

Record declared code terms separately from asset requirements. Missing root license files and inconsistent declarations remain explicit. We publish original factual summaries and links only. A repository-wide license declaration does not establish the provenance of every bundled asset.

## Runtime observations

All seed runtime statuses are `not-run`. To change a status, supply the exact revision, environment, commands/procedure, observed result and an evidence artifact URL. A headless test passing does not prove movement feel, multiplayer behavior or successful integration into another game.

## Updating a record

Review a new commit, update facts and evidence together, regenerate the comparisons, run checks and document what changed. Previous source review does not automatically apply to a newer revision. Broken links and hashes indicate evidence problems, not that the original project is unusable.
