# Vision Envelope — {Project Name}

**Diátaxis mode.** Reference (with how-to in §"How to use").

**Project.** {project name}
**Vision horizon.** {One line: the slice of the project's future this envelope covers — e.g., "Phase 1 spec closure", "v1.0 release", "MVP through first deployment".}
**Ratified by.** {Human Project Lead}
**Ratification date.** {YYYY-MM-DD}
**Governing Charter.** Project-Lead Charter (`project-lead-charter.md`) — ieops default. Amend only under explicit substitution; record substitution source in §7. Substituting Charters are ratifiable only if they satisfy `project-lead-charter.md` §8 well-formedness predicate W.1–W.5.

---

## 0. Well-formedness checklist

The envelope is ratifiable only if every item below holds. Evaluated by the operator (human or persona) before ratification, and re-evaluable at any drift checkpoint (§6). Failure of any item returns the envelope to the human PL as unratifiable; the operator does not work under a malformed envelope.

- [ ] **M. Metadata.** Project, Vision horizon, Ratified by, Ratification date, Governing Charter — all populated.
- [ ] **§1.** Vision statement declares a horizon end-condition (what closes this envelope).
- [ ] **§2.** Quality goals are listed in priority order; ties declared where present.
- [ ] **§3.** In-scope, Out-of-scope, and Deferred are explicit enumerations; In-scope ∩ Out-of-scope = ∅.
- [ ] **§4.** Decision latitude is an enumeration of permissions, not a grant of general authority.
- [ ] **§5.** At least one project-specific escalation trigger present beyond Charter §6 defaults.
- [ ] **§6.** Drift cadence named; drift criteria enumerated.
- [ ] **§7.** Substitution record explicit (`"None — ieops default Charter applies"` is acceptable).
- [ ] **§8.** Inference regime declared: posture chosen from the named enumeration; for any required oracle capability, either an oracle-identity declaration is present or `"capability-only — vendor unpinned"` is stated.
- [ ] **§9.** Context budget declared: primary-consumer effective-window budget present; critical-artifact size ceiling present; provenance-audit location populated.
- [ ] **§3 + X.S.3.** In-scope enumeration is consistent with the reference-class sizing band recorded at `phase-1-contracts.md` §12.1 X.S.3, or inconsistency is explicitly named and rationalized in the §3 block.

---

## 1. Vision statement

{Goal of the work in this horizon: what is being made, and why. One to three paragraphs. arc42 §1 ("Introduction and Goals") is the expected form.}

## 2. Stakeholders and quality goals

{Named stakeholders and the quality goals that matter under this envelope. arc42 §1.2–1.3 form. Quality goals in priority order; ties are declared.}

## 3. Scope

**In-scope.** {Explicit enumeration of what this envelope authorizes work on.}

**Out-of-scope.** {Explicit enumeration of what the operator may not initiate — deferred to later envelopes or dropped.}

**Deferred.** {Known open questions in this horizon that the operator may surface but may not unilaterally resolve.}

## 4. Decision latitude

Subagent dispatch and persona delegation within ratified scope follow `task-context-contract.md`; an attempted dispatch without a well-formed packet is a Charter §6 escalation.

{What the operator may decide without escalation. Written as enumerated permissions, not as general authority. Examples: "select among architectural tactics from the SAIP catalog"; "pick panel composition from the standing roster"; "close or keep open research questions tagged [content-inferred]".}

## 5. Escalation triggers

Return the following to the human PL before action, in addition to the Charter §6 defaults:

{Project-specific triggers. Examples: "any decision that would require re-running the SLR"; "any commitment of reference-library acquisition budget"; "any change that would touch the `convention-4-start` tag".}

## 6. Drift checkpoints

**Cadence.** {e.g., end-of-session / daily / per-phase-gate}
**Method.** Hollnagel work-as-done vs. work-as-imagined. The operator re-reads §§1–3 against what has actually been done since the last checkpoint and reports divergence.
**Drift criteria.** {What counts as drift. Examples: "scope creep beyond §3 in-scope"; "quality-goal reprioritization without ratification"; "new anchor added without decision record".}

## 7. Substitution record

{If the governing Charter has been substituted, record: source methodology or authorial frame; scope of substitution (full / delta); applicable escalation rule under substitution. Otherwise: "None — ieops default Charter applies."} Substituting Charters must satisfy `project-lead-charter.md` §8 well-formedness (W.1–W.5).

## 8. Inference regime

Closes per-project commitment under `phase-1-commitments.md` §4.3 and ratifies the composition rule with methodology-internal inference. Methodology operations remain governed by `phase-1-commitments.md` §3 commitments M–O regardless of the values below.

**Posture.** {One of: `inference-first` / `partial-inference` / `zero-inference`. Posture states the project's stance on whether inference is a load-bearing surface inside the artifact being built.}

**Required oracle capabilities.** {Enumerate the inference capabilities the project requires from any oracle: e.g., `classification`, `extraction`, `synthesis`, `critique`, `code-generation`, `proof-search`. Capability-only specification is the default per commitment M; identity is optional and pinned only with project-lead rationale.}

**Oracle identity declarations (optional).** {Per capability or for the whole project, either populate a triple `(vendor, model family, model name)` with rationale, or state `"capability-only — vendor unpinned"`. Identity declarations are amendable per Charter §4 (envelope expansion); changing the declaration mid-horizon is a Charter §6 escalation.}

**Provenance-audit location.** {Path or directory where inference-call provenance records (per `task-context-contract.md` §5) are appended for this project. Default: `<project-root>/audit/inference-provenance.log`. Append-only; consumer of an inference call writes the record before returning.}

## 9. Context budget

Operationalizes commitment K (LLM ergonomics) at the project level.

**Primary consumer effective-window budget.** {The project's primary inference consumer model and the effective-context budget the project will operate within. Default per Context Engineering A1: ≤50% of the declared model context. Format: `<model identifier or capability-only>; budget <fraction or token count>`.}

**Critical-artifact size ceiling.** {Maximum size for any artifact the primary consumer must read end-to-end inside one session. Stated in lines, tokens, or words; one units choice for the whole project. Artifacts exceeding the ceiling must be split or summarized before consumption.}

**Edge-placement convention.** {Either `"per A2 default"` (load-bearing content at start or end), or a project-specific convention with rationale. A2 default is recommended unless the project's artifact class warrants otherwise.}

---

## How to use

1. Human PL fills §§1–6 before delegating the role.
2. Operator (human or persona) operates within the envelope.
3. Drift checkpoints run per §6 cadence; divergence is reported and resolved at the checkpoint.
4. The envelope is updated only by the human PL. Operator proposals to amend are escalations, not unilateral edits.
