# ieops methodology — v0.1

The ieops methodology, embedded in this workspace. ieops is a build-side
methodology for infrastructure-grade software projects run by inference; its
primary operator is Claude Code, and its human interface is natural language with
the Project Lead.

## Read in order

1. **`phase-1-commitments.md`** — the stable layer: name, failure modes the
   methodology prevents, commitments A–O, modal structure (Deliberation /
   Execution / Holodeck), structural form, audience, artifact register, and a
   one-page summary.
2. **`phase-1-contracts.md`** — the decidability spine: the anchor slate with the
   ATAM activation predicate, the BLOCK criterion for panel verdicts, stage-gate
   entry/exit criteria for all four lifecycle stages, and the traceability spine.
3. **`anchor-map.md`** — the anchor slate (named external frameworks per stage and
   cross-cutting), the composition rules, the summary table, and the
   anchor-literacy assumption.
4. **`project-lead-charter.md`** — the default Project-Lead methodology, grounded
   in the Chief Engineer composite. Read before any PL action; §8 carries the
   substitution well-formedness predicate.
5. **`vision-envelope-template.md`** — the per-horizon artifact each project
   ratifies before delegating PL responsibility; §0 is the well-formedness
   checklist. (The workspace-root `../vision-envelope.md` is the bootstrap-state
   instance.)
6. **`task-context-contract.md`** — the 14-field contract for any task-context
   packet supplied to a subagent, persona, or load-bearing inference call.
7. **`context-engineering-operating-template.md`** — nine rules (A1–A4, D1–D3,
   C1–C2) operationalizing commitment K (LLM ergonomics).

ieops's own forward-development plan (v0.2 / v0.3 / v1.0) lives in the ieops
repository root (roadmap.md), not in a scaffolded project workspace.

## By task

- **Ratify a Vision Envelope.** `vision-envelope-template.md` §0 (well-formedness)
  → §§1–9 (populate). A substituting Charter must satisfy `project-lead-charter.md`
  §8.
- **Dispatch a subagent or load-bearing inference call.**
  `task-context-contract.md` (14-field packet) +
  `context-engineering-operating-template.md` §§D1–D3 + `project-lead-charter.md`
  §6 (a dispatch without a well-formed packet is an escalation).
- **Close a stage gate.** `phase-1-contracts.md` §12.<stage> entry/exit criteria,
  with the named files cited per clause.
- **Run a drift checkpoint.** `vision-envelope-template.md` §6 (Hollnagel
  work-as-done vs. work-as-imagined).

## Discoverability

Every artifact that names an anchor or a commitment points to where it is defined:
anchors → `anchor-map.md`; commitments → `phase-1-commitments.md` §3. Pointers are
by file path, not by inference. Introducing a new anchor without a corresponding
entry in the project's decision log is a Charter §6 escalation.
