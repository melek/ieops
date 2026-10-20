# ieops — Inferential Engineering Operations

ieops is a build-side methodology for infrastructure-grade software projects run
by inference. Its primary operator is Claude Code; its primary audience for
natural-language interaction is the human Project Lead. The methodology is shipped
as a workspace template — copied per related-project group — anchored throughout to
named external frameworks (Flyvbjerg, INCOSE, arc42 + SAIP + DSA + C4, Leino, ITIL,
Hollnagel, Leveson-STPA, Diátaxis, the Chief Engineer composite, and a Context
Engineering composite).

## Repository layout

| Path | What it is |
|---|---|
| `workspace-template/` | The self-contained workspace a project runs in. This is what `create-workspace.py` copies. |
| `workspace-template/methodology/` | The v0.1 methodology itself — the spec (commitments + contracts) and operating templates. |
| `create-workspace.py` | Spin-up script: copies the template into a fresh, git-initialized workspace. Zero variable substitution. |
| `roadmap.md` | ieops's own forward-development plan (v0.2 / v0.3 / v1.0). Not part of a scaffolded project workspace. |
| `LICENSE` | MIT. |

## Start a project

```bash
git clone https://github.com/melek/ieops.git
cd ieops
python3 create-workspace.py my-project        # → ~/ieops-workspaces/my-project/
#   …or pass an absolute / ~-prefixed path to place it anywhere:
python3 create-workspace.py ~/code/my-project
```

Requires Python 3.9+ and `git`. The script copies `workspace-template/` verbatim
into the destination and runs `git init` (branch `main`) with one initial commit.

Then open the new workspace with Claude Code and ask it to read `README.md` /
`CLAUDE.md`. The workspace opens in a **bootstrap state**: its vision is not yet
set, and Claude orients you before any work begins. Behavior is driven by artifact
content (the workspace is self-describing about its own state), not by special
first-run logic.

## What a scaffolded workspace contains

- `vision-envelope.md` — the project's foundational vision, shipped in bootstrap
  state (`Status: Not yet set`).
- `methodology/` — the embedded v0.1 methodology (read `methodology/README.md`
  first).
- `pre-ratification-notes.md` and `audit/pre-ratification-inference.log` — empty,
  append-only; used during the pre-ratification bootstrap phase.
- `README.md` / `CLAUDE.md` — operator orientation for the fresh workspace.

## Maintaining ieops

The v0.1 release in `workspace-template/methodology/` is a cleaned derivation of an
internal working copy; the methodology's full development provenance (records of the
simulated-persona review panels, decision log) lives outside this repository. Where
`roadmap.md` attributes a critique to a named author, it means an AI persona reviewing
through that author's framework, not the author. There is no render or generate step:
the methodology evolves by editing these files directly (or re-deriving the clean
release) when a ratified change lands, with the change reflected in `roadmap.md`.

## License

MIT — see `LICENSE`.
