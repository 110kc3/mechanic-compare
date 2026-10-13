# Mechanic Compare

**Find a movement implementation that fits your game—and see the code behind the comparison.**

> “I like Mirror’s Edge parkour. What can I use in my Godot project?”

This experiment compares six parkour and first-person movement implementations by engine, language, integration boundary, dependencies and evidence. Each record links to a reviewed source revision. It helps people and AI agents choose references before changing a game.

**Seed status:** source and documentation reviewed on 2026-10-13. No upstream build, gameplay, multiplayer or integration testing has been performed by this project. Source presence does not establish identical feel, working compatibility or permission to reuse every asset.

## Compare the implementations

<!-- comparison:start -->
| Implementation | Source context | Reviewed mechanics | Integration shape | Declared terms | Runtime check |
| --- | --- | --- | --- | --- | --- |
| [Faith Runner](comparisons/parkour.md#faith-runner) | engine-independent / Rust | wall-run, vault, slide, ledge-grab | subsystem | Unknown | not-run |
| [Beatrun Community Edition](comparisons/parkour.md#beatrun) | garrys-mod / Lua | wall-run, vault, wall-climb | gamemode | WTFPL | not-run |
| [NOSHOT First Person Controller](comparisons/parkour.md#noshot) | godot / C# | wall-run, wall-climb, vault | controller-project | MIT | not-run |
| [Park’s Edge](comparisons/parkour.md#parks-edge) | minecraft / Java | wall-run, wall-climb, vault, slide | mod | CC0-1.0, MIT (conflicting) | not-run |
| [Still Alive / Mirror’s Edge Unity port](comparisons/parkour.md#still-alive) | unity / C# | wall-run, vault | game-port | Unknown | not-run |
| [Dani simple FPS movement](comparisons/parkour.md#dani-fps) | unity / C# | jump, slide | movement-baseline | MIT | not-run |
<!-- comparison:end -->

Read the [full comparison and source entry points](comparisons/parkour.md). The [JSON dataset](data/implementations.json) is the source of truth; this table and the full comparison are generated from it.

### Three practical examples

- **Godot with GDScript only:** NOSHOT uses C# and requires the .NET edition. The seed has no native GDScript wall-running match. A Rust or C# implementation may still be a study reference; adapting it is additional work.
- **An engine-independent Rust controller:** Faith Runner exposes a collision interface and a step function. Its root license declaration was not found in the reviewed snapshot; resolve terms before treating it as a reusable dependency.
- **A Garry’s Mod parkour experience:** Beatrun is a host-specific gamemode. Its movement code depends on Garry’s Mod APIs, rather than exposing a portable controller interface.

## Try it with an AI agent

Give your agent the [agent guide](docs/agent-guide.md) and dataset, then ask:

```text
Compare wall-running implementations for my target: Godot 4, C# allowed,
single player. Explain the integration work and unresolved questions.
Cite exact reviewed files. Do not assume runtime compatibility or identical feel.
```

The dataset is directly readable without installing anything. Optional local filters and checks require Python 3.11+:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/catalog.py query --engine godot --mechanic wall-run --json
python scripts/catalog.py check
```

Filters describe the reviewed source; they do not certify suitability. No match means no match in this small seed, not that an implementation cannot exist.

## Help test whether this is useful

**Did this comparison change your choice or save investigation?** [Report a use case](https://github.com/110kc3/mechanic-compare/issues/new?template=use-case.yml), including your target, candidates considered and what helped or was missing. Corrections and [new implementations](https://github.com/110kc3/mechanic-compare/issues/new?template=implementation.yml) are welcome. A star is an interest signal; a concrete use report is stronger evidence.

We will review traction on **2026-10-27**. The [validation plan](docs/traction.md) separates interest, actual use and benchmark results. The [ten evaluation briefs](evaluation/briefs.json) have not yet been run as an independent agent benchmark.

## Existing work and scope

This complements [Universal Modder](https://github.com/rehan-remade/universal-modder), [Awesome Game Mashups](https://github.com/bailo167/awesome-game-mashups), [Game Design Index](https://github.com/blazium-games/game-design-index) and [Open Game Mechanics Dataset](https://github.com/Thaelith/open-game-mechanics-dataset). They already provide catalogs, design vocabulary or modding workflows. This seed focuses on concrete source boundaries and constraints within one mechanic family.

There is no installer, game-code redistribution, automated mechanic transfer or universal compatibility promise. New mechanic families and an API/MCP service remain deferred until the pilot shows value.

Original comparisons and metadata are [CC0](LICENSE-DATA); project tooling is [MIT](LICENSE). Upstream projects retain their own terms. See [methodology](docs/methodology.md), [contributing](CONTRIBUTING.md) and the [current queue](NEXT.md).
