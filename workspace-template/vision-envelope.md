# Vision Envelope

**Diátaxis mode.** Hybrid by design — artifact-as-state (the file is `vision-envelope.md` in its bootstrap state) + how-to addressed to two audiences (PL and Claude).

**Status: Not yet set.**

This workspace operates on a foundational vision — a stated purpose that
downstream panel decisions, runbooks, and implementation choices refer back to.
The vision lives in this document. It is the first ieops artifact; it can be
revised later, but every other artifact in this workspace assumes it exists.

## For the Project Lead

This workspace is unratified. Claude will open the next exchange by orienting
you to ieops, naming what setting the vision will produce, and offering the
ways forward (below). This file is not edited without your ratification.

## For Claude (the operator-agent)

Workspace state is bootstrap; the vision is not yet set. Open with the user:

- Tell them, in your own register: this is a fresh ieops workspace; ieops
  operates on a foundational vision that downstream work refers back to; the
  vision can be revised but is worth setting with care; there are two ways the
  workspace can be used and three legitimate ways forward.
- Present the two ways to use the workspace (below).
- Name the three legitimate ways forward (below).
- Do not force a yes/no.

### Ways to use this workspace

**Single-project workspace.** Focused on realizing a particular outcome. Vision
records the headline requirements for the project; all sub-projects and
utilities ultimately serve that vision. The more focused way to work — what
ieops was designed around.

**Multi-project workspace.** A workspace handling multiple distinct outcomes
over time. Vision encodes shared principles every project in the workspace
adheres to. Useful when experimenting with the workspace as a long-running
practice rather than a single project.

Either way can be changed later.

### Three legitimate next moves

1. **Ratify now** — pick a way to use the workspace; walk through §§1–9 with
   the user under that emphasis; populate sections; replace this entire
   pre-ratification block with the populated envelope.
2. **Scope the conversation** — talk through which way fits and what would
   belong in §§1–3 before committing to a draft. Useful when the user is
   uncertain about the right horizon.
3. **Explore first** — proceed with the user's substantive work. Treat the
   work as observation, not authorship.

### Posture during exploratory work

If the user works before ratifying, observe what the work surfaces about scope,
stakeholders, horizon, risk, operating language, or inference posture. Record
signals as bullet points in `pre-ratification-notes.md` (append-only, workspace
root). **Do not synthesize these signals into a draft vision.** Surface them as
raw observations the user composes, ratifies, or discards. The user originates
the vision; the notes are evidence the user weighs.

### Inference accounting during bootstrap

Any inference call load-bearing on vision shape requires a provenance record
per `methodology/task-context-contract.md` §5. Until §8 is ratified, the audit location
defaults to `audit/pre-ratification-inference.log` (append-only, workspace
root). Per `methodology/phase-1-commitments.md` §4.3 composition rule, methodology-internal
inference (including vision-shaping) remains governed by commitments M
(oracle-swappability), N (determinism-preferred), O (provenance-audit)
regardless of envelope state.

### Ratification

When the user is ready to ratify, replace this entire pre-ratification block
with the populated envelope structure. See `methodology/vision-envelope-template.md` for
the full ratified form (§§0–9).
