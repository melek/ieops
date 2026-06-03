# You're in a fresh ieops workspace

This is an ieops project workspace, scaffolded from the ieops methodology
template. ieops is a build-side methodology for infrastructure-grade software run
by inference: Claude Code operates the project; you, the Project Lead, direct it
in natural language.

The workspace opens in a **bootstrap state** — its foundational vision is not yet
set. Nothing downstream (panels, runbooks, implementation) proceeds until the
vision is ratified, and **you** originate it.

## First contact

Read `vision-envelope.md`. It is the project's foundational vision in its
not-yet-set state, and it instructs the opening exchange: Claude orients you to
ieops, names what setting the vision will produce, and offers the legitimate ways
forward (ratify now, scope the conversation first, or explore the work first and
treat it as observation). Behavior here is driven by artifact content, not by
special first-run logic — the workspace is self-describing about its own state.

Until the vision is ratified, Claude records raw signals from any exploratory work
in `pre-ratification-notes.md` (append-only) and does **not** synthesize a draft
vision on your behalf.

## What's here

| Path | Role |
|---|---|
| `vision-envelope.md` | The project's foundational vision (bootstrap state). Edited only on your ratification. |
| `methodology/` | The ieops methodology — start with `methodology/README.md` for the reading order. |
| `pre-ratification-notes.md` | Append-only log of pre-ratification observations. |
| `audit/pre-ratification-inference.log` | Append-only provenance log for vision-shaping inference, until the Vision Envelope §8 (Inference regime) specifies the project audit location. |

## How to use it

1. Open this folder with Claude Code and ask it to read `README.md`.
2. Claude follows the `vision-envelope.md` bootstrap instructions and orients you.
3. When you're ready, ratify the Vision Envelope (see
   `methodology/vision-envelope-template.md` for the full ratified form) — this
   replaces the bootstrap block with your populated envelope.
4. From there the methodology governs: stage gates, task-context packets for any
   subagent dispatch, drift checkpoints, and the Project-Lead Charter.

If this workspace was created with `create-workspace.py`, git is already
initialized (branch `main`, one initial commit).

## Modes

Work happens in distinct modes — **Deliberation** (panels, specification — no code
committed) and **Execution** (implementation against a ratified plan — no vision
re-interpreted), defined in `methodology/phase-1-commitments.md` §4.2, plus
**Holodeck** (purposeful, named roleplay) per commitments F–G. Transitions between
modes are explicit hand-offs, not drift. See the methodology and the Project-Lead
Charter's escalation rule for the full treatment.
