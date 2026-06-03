# Context Engineering — Operating Template (v0, thin)

**Diátaxis mode.** Reference (rule set A1–A4, D1–D3, C1–C2).

**Status.** Thin v0; elaboration deferred until practice surfaces gaps.

**Form.** A rule set, evaluable per artifact, per subagent dispatch, or per completeness check. Cited by reference from drift-checkpoint criteria in Vision Envelopes (`vision-envelope-template.md` §6).

**Governing anchor.** Context Engineering composite (see `anchor-map.md`). The rules below name specific findings; the composition rationale is in the anchor map.

---

## 1. Artifact production

- **A1. Budget discipline.** An artifact's length is matched to the effective-context budget of its likely end-to-end reader. Default ceiling: ~50% of the consumer's effective window. Source: `llm-context-attention-degradation` SLR (50% effective-context budget).
- **A2. Edge placement.** Load-bearing content (definitions, contracts, conclusions) is placed at the start or end of the artifact, not the middle. Source: same SLR (lost-in-the-middle spatial layout).
- **A3. Stable vocabulary.** Terms defined in the methodology are used verbatim across artifacts. Introducing a new term for an existing concept is a Charter §6 escalation (change of taste register). Source: `role-persona-prompting-mechanisms-effectiveness` SLR (terminology fracture) + commitment J (named external frameworks, not invented vocabulary).
- **A4. Proportional depth.** Depth of treatment is proportional to task weight, per the Chen SAT triad (what / why / next): heavier work names all three; lighter work names what. Source: `proportional-response-calibration-cognitive-load` SLR (SAT model). Mapping to SAIP weight levels is a composition specific to this methodology, not an SLR lift.

## 2. Subagent dispatch

- **D1. Task-context packet required.** No subagent dispatch proceeds without a well-formed packet per `task-context-contract.md`.
- **D2. Specific persona declarations.** When a persona is invoked, the declaration names the methodological frame and the task — not a generic role. Source: `role-persona-prompting-mechanisms-effectiveness` SLR (specificity effects; soft residual-stream steering, not retrieval).
- **D3. Session boundary stated.** The dispatch declares the session's completion condition: what output, at what location, returned to whom. Source: Suchman situated action (action derives from situation, not an abstract plan).

## 3. Completeness check

- **C1. Deterministic presence verification.** Claims that required artifacts or fields are present are verified by inspection, not by self-report. No inference call gates a "complete" determination. Source: `llm-context-attention-degradation` SLR (deterministic completeness verification).
- **C2. Work-as-done reconciliation.** After a task, the artifact is re-read against what actually happened (Hollnagel work-as-done vs. work-as-imagined); divergence is recorded in the task-context audit record (`task-context-contract.md` Field 14) before proceeding to the next task.

---

## Decidability

Each rule is evaluable without inference. A1/A2 inspect length and structure. A3 compares terminology to an existing glossary. A4 is evaluated against the declared task weight. D1 is evaluated against packet well-formedness. D2 inspects the dispatch declaration. D3 inspects the dispatch declaration. C1 inspects named files. C2 inspects the audit record.

## Cross-references

- `task-context-contract.md` — packet format (D1) and audit record (C2).
- `vision-envelope-template.md` §6 — drift-checkpoint cadence that shares the Hollnagel basis with C2.
- `phase-1-commitments.md` §3.K — LLM ergonomics commitment that these rules operationalize.
