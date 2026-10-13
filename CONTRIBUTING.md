# Contributing

Start with an issue for a missing implementation, factual correction or a real target-game comparison. The current pilot covers parkour and adjacent first-person movement.

For a dataset change:

1. Pin an upstream **commit**, inspect its files, and add evidence objects with file hashes. A tree hash or mutable branch name is not a reviewed commit.
2. Describe mechanics visible in reviewed source and give navigation symbols. Evidence references must support each claim. Keep creator-reported fidelity and runtime observations separate.
3. Explain the integration boundary, dependencies and limitations. State uncertainty. Use `unknown` or `conflicting` license status where appropriate; a catalog listing and a source manifest can disagree.
4. Add or update evaluation expectations if the comparison changes an answer. Do not create benchmark scores from those expectations.
5. Run `python scripts/catalog.py render` and `python scripts/catalog.py check --verify-sources`.

Please contribute your own descriptions and factual metadata. Link to upstream source; do not submit upstream code, game files, decompiler dumps or assets. Changes to runtime-test status require a reproducible environment, revision, procedure and observation in the runtime evidence field.

The JSON Schema is in schema/implementations.schema.json. The tooling reports structural errors but does not automatically judge whether prose is accurate; reviewers must read the evidence.
