# ieops Roadmap

**Diátaxis mode.** Reference (planned future work).

**Purpose.** This document records work planned beyond v0.1. Each entry names a concrete addition to the methodology — a contract, predicate, artifact, or mechanism — with the version target at which it is expected to land and the rationale for its deferral from v0.1.

The roadmap is itself a methodology artifact and is governed by the same commitments as the rest of ieops (see `phase-1-commitments.md`).

**A note on provenance.** Each entry's **Provenance** line names the review lens that raised the item. These reviews were simulated: panels of AI personas, each prompted to critique the methodology from the perspective of one named framework or author (Flyvbjerg's reference-class forecasting, Hollnagel's resilience engineering, Leveson's STPA, Ousterhout's module depth, Leino's program proofs). The named authors did not review ieops, and quoted critiques are persona output, not their words.

---

## v0.2 — Methodology self-observation

This cluster addresses how the methodology observes its own operation in practice. The three items share a vocabulary (control actions, unsafe-control-action categories, feedback channels) and benefit from being designed together.

### Outside-view drift surface (audit-replay mechanism)

**What.** Adherence verification via a defined audit-replay surface. The methodology's "decidable by inspection" predicates currently rest on the operating agent reading its own audit records — a structural pattern named as **agent-multiplicity collapse** (the doer, checker, and auditor are all the same LLM session). The methodology already uses agent-multiplicity informally — every panel review is a set of fresh subagent sessions producing independent verdicts — but does not yet apply that pattern to adherence verification specifically. This item specializes the existing subagent-dispatch pattern: a periodic audit replay where a fresh subagent session re-evaluates a sample of recent audit records against the predicates they claim to satisfy and records divergence.

**Why deferred.** Requires design pass on replay cadence (per-stage-gate / per-Heartbeat / sampling rate), sample selection criterion (which audit records, how chosen), divergence-recording form, and integration with the existing audit-log discipline. Worth getting right rather than shipping a thin version in v0.1.

**Provenance.** The Hollnagel-lens and Flyvbjerg-lens personas both flagged the agent-multiplicity gap. Hollnagel-lens persona: "the operator reporting divergence is the same operator whose divergence is in question; there is no second channel." Flyvbjerg-lens persona: similar critique at the Scoping-exit reference-class-sizing step.

### Unsafe-control-action (UCA) enumeration framework

**What.** A vocabulary lift applying STPA's four UCA categories (not-provided / provided-when-hazardous / wrong-timing / stopped-too-soon) to the methodology's own control actions: task-context packet dispatch, methodology-internal inference operations (panel deliberation, classification inside operating-template rules, task-context computation, drift-checkpoint synthesis), Charter substitution, predicate evaluation. The framework gives each control action a stated set of UCA categorizations the methodology must address.

**Why deferred.** Substantive vocabulary lift. The categorization benefits from real operator-record data to calibrate which UCAs are common in practice; v0.1 ships before that data exists.

**Provenance.** The Leveson-lens persona named this directly; the Hollnagel-lens and Ousterhout-lens personas converged on the same gap from work-as-done and module-depth angles respectively.

### STPA control-structure artifact + traceability sub-spine

**What.** A diagram (Mermaid or table) listing controllers, controlled processes, control actions, and feedback channels for the methodology's own operations. Minimum entries: PL ↔ Operator (Charter §1, §6), Operator ↔ Subagent (`task-context-contract.md`), Drift checkpoint ↔ Envelope state (Envelope §6), Panel ↔ Spec (`phase-1-contracts.md` §10). Plus a parallel traceability sub-spine to the existing `phase-1-contracts.md` §13: Loss → System-level hazard → Safety constraint → Control action → UCA → Loss scenario → Mitigation/accepted-risk record. Stage activation: Loss/Hazard/Constraint at X.S.4; UCA/Loss-scenario at Development entry; Mitigation/accepted-risk at X.D.5; runtime UCA records at X.H.2.

**Why deferred.** Substantive new artifact plus a parallel traceability spine. Worth landing after the UCA framework (above) so the artifact and spine reference a stable vocabulary.

**Provenance.** The Leveson-lens persona named both the control-structure artifact and the traceability sub-spine. The current `anchor-map.md` cites STPA as cross-cutting at Scoping / Development / Heartbeat but the methodology does not draw the structure it claims to compose with.

---

## v0.3 — Project application

This cluster sharpens how ieops scopes and operates project work. The reference-class forecast machinery depends on accumulated reference-class data — chicken-and-egg until ieops has been used in a handful of projects.

### Reference-class outside-view forecast machinery at Scoping exit

**What.** Extend the Scoping-exit stage gate (currently `phase-1-contracts.md` §12.1 X.S.3, which records "comparison class, sizing band, modularity decision") to additionally require a base-rate-derived cost/time projection for the comparison class with named adjustments, recorded in the project's decision log. Where "no available reference class" is declared, require an explicit `outside-view: unavailable` record with the PL's substitute estimation method named.

**Why deferred.** The machinery is useful only when ieops has accumulated reference-class data to draw from. v0.1–v0.2 use ieops on a small number of projects; v0.3 captures the discipline once the data exists.

**Provenance.** The Flyvbjerg-lens persona named this as the dominant gap against the iron law: "Naming a comparison class is not reference-class forecasting; producing a base-rate-corrected estimate is."

### Modularity decision criterion at Scoping exit

**What.** Extend X.S.3 to add a sub-predicate: a `monolith` decision requires recorded justification against three named tests — (a) does the horizon decompose into independently-deliverable envelopes that each produce stakeholder-recognized benefit; (b) does the reference class show modular delivery succeeded for comparable scope; (c) what is the unrecoverable-cost-on-cancellation differential between modular and monolith delivery for this horizon. The decision remains the PL's; the justification becomes decidable by inspection.

**Why deferred.** The criterion's value scales with the size of the project space ieops manages. In v0.1 the methodology itself is a single horizon; the criterion is more useful as ieops sees adoption.

**Provenance.** Flyvbjerg-lens persona. The criterion was proposed alongside the reference-class forecast, but stands on its own.

### Operator-behavior anticipation register

**What.** For each load-bearing predicate (acceptance predicate A.1–A.5, ATAM activation T.1–T.4, BLOCK criterion B.1–B.4, stage gates, task-context packet completeness, drift checkpoint), an anticipated-failure-mode note: how a Claude-operator could satisfy the predicate's letter while missing its substance, and what the prevention cue is. Generalizes the "Do not synthesize these signals" pattern already present in `vision-envelope-bootstrap.md` (Posture during exploratory work).

**Why deferred.** Substantive per-predicate addition. Selective application possible in v0.1 (high-stakes predicates only); full pass deferred to v0.3.

**Provenance.** Hollnagel-lens persona. The bootstrap-copy pattern was a work-as-done finding masquerading as a procedural rule; the register generalizes it.

---

## v1.0 — Cleanup

This cluster carries items deferred for principled reasons (overbuild avoidance, dependence on accumulated experience). They land when the methodology's own use produces the signals against which to specify.

### Heartbeat work-as-done check contract

**What.** Replace the current Deployment-exit and Heartbeat-exit clauses (`phase-1-contracts.md` §§12.3 X.DP.3, 12.4 X.H.1) — which currently say "is recorded" — with a minimum-field contract for a Hollnagel work-as-done record analogous to `task-context-contract.md`: observer identity; observed-vs-planned comparison; routine-adaptation / disruption-response classification with cue; reconciliation against ratified vision.

**Why deferred.** `phase-1-commitments.md` §4.4 explicitly names overbuild-avoidance as the Heartbeat-stage directive until real runtime signals exist to specify against. The contract is worth writing once ieops has been operated through Deployment-and-Heartbeat at least once.

**Provenance.** Hollnagel-lens persona. The current X.DP.3 / X.H.1 clauses are presence-decidable but content-dependent in a way that does no methodology work; the contract makes them substantive.

### NASA P10 instantiation

**What.** Either commit to which P10 rules apply at Development (e.g., bounded loops for verified modules, no recursion for `[compiled-verified]` code) or explicitly defer with a recorded reason. Currently P10 is named in the anchor slate (`anchor-map.md`, `phase-1-contracts.md` §7) without obligation.

**Why deferred.** Project-stage obligation work. The verification-application rule in `phase-1-commitments.md` §3 already names P10 as a project obligation, not a methodology obligation; v1.0 specifies which rules in a way that downstream projects can adopt or amend.

**Provenance.** Leino-lens persona. "Naming without contract" is a recurring meta-pattern; v1.0 closes it for P10.

### Stage section re-organization

**What.** Re-organize the cross-stage cross-cuts in `phase-1-commitments.md` §4.1 (weight per stage) and `phase-1-contracts.md` §7 (anchor per stage), §12 (entry/exit per stage), §13 (traceability per stage) into per-stage sub-sections so each stage's treatment is contiguous. The v0.1 form keeps the cross-cut as the organizing principle (per the decomposition into commitments/contracts files); v1.0 considers whether per-stage organization becomes the preferred shape once the methodology has more accumulated material.

**Why deferred.** The v0.1 decomposition handles the most-load-bearing case of the Ousterhout-lens persona's stage-conflation concern (the per-stage cross-reference structure, with stages grouped by file in commitments vs. contracts). Full per-stage re-organization is the heavier alternative and is worth considering against accumulated v0.2 and v0.3 material before committing.

**Provenance.** Ousterhout-lens persona. The lighter v0.1 form was that persona's "lighter option"; the heavier form is the alternative path for v1.0 if the cross-cut organization shows strain.

---

## How this document is maintained

Roadmap entries are added at version-target close (e.g., v0.1 close added the entries above). An entry moves out of the roadmap when the methodology absorbs it: a new entry is recorded in the methodology's decision log naming the change, and the corresponding roadmap entry is marked **Done** with a date and a pointer to the absorption entry.

The roadmap is not a commitment — items can be reordered, retargeted, or retired by PL ratification with a recorded rationale.
