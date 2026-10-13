# Mechanic Compare working instructions

- Scope and accepted work live in NEXT.md. Deferred ideas need explicit selection.
- data/implementations.json owns comparison facts. Generate README's comparison block and comparisons/parkour.md with `python scripts/catalog.py render`; never hand-edit generated content.
- Inspect exact commits and files before adding facts. Record evidence for every mechanic and constraint. Keep source review, upstream reports and observed runtime checks distinct.
- A file or symbol is a navigation anchor, not a complete or portable subsystem. Unknown or conflicting license declarations stay unresolved. Do not copy upstream code, binaries, art, animations or audio here.
- Do not claim runtime compatibility, multiplayer support or matching feel without appropriate observed evidence. No catalog match does not mean the mechanic does not exist.
- Run `python scripts/catalog.py check` before committing. Use `--verify-sources` when adding or changing pinned evidence. This fetches text only and never executes upstream code.
- Keep AGENTS.md and CLAUDE.md byte-identical. Commit and push scoped authorized changes; preserve unrelated work. Never wait for Actions after pushing; record pending verification in NEXT.md.
- Publishing this repo does not authorize promotion posts, messages, deployments, merges or installing third-party modding tools.
