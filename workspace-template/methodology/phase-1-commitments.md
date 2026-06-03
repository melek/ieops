# ieops — Phase 1 Commitments

**Diátaxis mode.** Hybrid — reference (commitments, modes, structural form, artifacts) + explanation (name, failure modes, audience).

**Methodology.** ieops (Inferential Engineering Operations)
**Phase.** 1 — Specification (commitments layer)
**Version.** v0.1.
**Status.** v0.1.
**Scope classification.** Tier 3 (Architectural).
**Decision authority.** Project Lead.
**Companion document.** `phase-1-contracts.md` (decidability spine: anchor slate with ATAM predicate, BLOCK criterion, stage gates, traceability).

## 0. Preamble

This document is the *commitments layer* of the ieops Phase 1 specification. It carries the methodology's name, failure modes, commitments, modal structure, structural form, audience, and one-page summary — the stable layer of the specification.

The decidability spine — anchor-slate predicates, BLOCK criterion, stage-gate entry/exit criteria, traceability spine — lives in the companion `phase-1-contracts.md`, the absorption surface that grows monotonically under review cycles.

## 1. Name (Q1)

**ieops** — Inferential Engineering Operations. Methodology name. Shortened form revised twice: `inf-engops → iengops → ieops`; full name and grounding unchanged across revisions.

**Commitments carried by the name:** critical-engineering scope (not general PM); operational (runs through execution, not planning only); apparatus-shaped (workspace + expert team + executive + lead, not a single document); inference-honest (the `i-` prefix names the simulation-through-inference rather than deterministic institutional machinery).

## 2. Failure modes ieops prevents (Q2)

Each failure mode is a pattern the methodology must prevent in the next project.

1. **Keystone construction.** No fundamental productivity loop established first; interaction surfaces existed but no working pipeline behind them to extend. Plumbing grew heavy managing inference safety before inference could do one thing Claude Code can do.
2. **Risk mitigation before capability.** The procedural way to reliably perform real work *is* the product; direct inference is already available. Gates around it are architecturally unsound as a starting point.
3. **Post-hoc rigor.** Leveson-grade discipline bolted on after architecture was set.
4–5. **Phase map without architectural anchor.** Late-added phase dashboard became the sole completion metric; no concrete deliverable vision anchored it.
6. **No stable SWE methodology codified.** Verification-first discipline takes longer to take hold than expected; delegated implementation under general-purpose agent tooling generates large volumes of tests. The methodology needs its own methodology-compatible skills, not upstream defaults.
7. **Nomenclature drift as unmanaged organizational-change hazard.** Human-organization change-management techniques apply; they were not used.
8. **Fabricated panel independence.** Convergent-panel evidence is strong only when panelists are structurally independent. Where independence comes from and how it is protected must be specified, not assumed.

## 3. Commitments (Q3)

The methodology's commitments, lettered A–O. Commitment B is held at the project-vision layer rather than the methodology: the methodology commitments are A and C–I, the cross-cutting commitment J, the LLM-first commitments K–L, and the trust-architecture commitments M–O.

### Methodology commitments

- **A. Prove-then-extend iteration.** A stable proof-of-concept with a working productivity loop exists before the project iterates on extensions. Avoids the pattern of iterating on untested ideas behind heavy plumbing.
  - **Acceptance predicate (A.1–A.5, all required).** A project may transition from proof-of-concept to extension iteration only when:
    - **A.1** The productivity loop has executed end-to-end (declared input → declared output via the loop's named stages) at least three times against the acceptance criterion in the Vision Envelope §1, with each run recorded in the inference-provenance / audit location declared in Envelope §8.
    - **A.2** No modification of the loop's stages or interfaces occurred between the three runs (the audit log shows no `loop-modify` events between the first and third recorded run).
    - **A.3** A drift checkpoint per Envelope §6 has executed at or after the third run with a `divergence: none` or `divergence: resolved` record.
    - **A.4** Module decomposition exists per arc42 §5 (Building Block View), referencing each loop stage to a building block.
    - **A.5** At least one loop-affecting module carries verification per the Leino tradition (specification + proof or specification + test) appropriate to its assigned weight per §4.1.
  - **Decidability.** Each of A.1–A.5 is decidable by inspection of named files (audit log, Envelope, arc42 §5 document, the module's verification artifacts). No inference call is required to evaluate the predicate. **Soundness/completeness trade.** This predicate trades completeness for soundness — structurally well-formed cases that fail a clause typographically are rejected; pass requires structural well-formedness, not semantic equivalence to it.
- **C. Architectural plan as anchor; cognitive-ergonomic tractability.** Production-grade enforceable policies and procedures; *Documenting Software Architectures* and SAIP as literature base; slow-and-steady by default; chunk sizes tuned for inference context-tree reliability.
- **D. STPA as methodology default.** Design-time hazard analysis is part of any project's methodology; runtime application is a general principle a project may automate within its own domain.
- **E. Working-before-modifying.** Something must work before it is modified or extended.
- **F. Methodological-lens diversity; persona as ergonomic overlay.** Named methodologies and disciplines drive model behavior; personas help the human Project Lead relate and coalesce understanding. Persona use is a Holodeck-mode activity with distinct obligations.
- **G. Purposeful, named roleplay.** When the workspace engages in roleplay, it is named and purposeful. Holodeck vs. Working mode distinction carries across the workspace.
- **H. Methodology-owned, methodology-matched skills.** Upstream defaults (general-purpose agent frameworks, Claude Code built-ins) are learned-from, not inherited; the workspace writes its own.
- **I. One-page communicability.** Any piece describable in one page to an incoming agent.

### Cross-cutting commitment

- **J. Anchoring in named external frameworks, not invented terminology.** Every methodology concept is grounded in a named external framework (INCOSE, arc42, Leino, Flyvbjerg, ITIL, Hollnagel, STPA, Diátaxis, Chief Engineer composite, Context Engineering composite). Invented vocabulary is avoided wherever an external canonical concept serves.

### LLM-first commitments

- **K. LLM ergonomics and meaningful-artifact production as first-class constraints.** Methodology artifacts are structured for Claude's traversable context space — short, cross-linked, chunked — not as monolithic documents. Chunking sessions by work topic keeps context coherent within Claude's effective window.
- **L. Task-context calculation as a methodology affordance.** The methodology computes and supplies ergonomic, methodology-grounded task context per task (to Claude itself, to subagents, to any inference call) — analogous to a human's job description + social context. Substitutes for enormous preambles; situates action inside the methodology's frame. Contract: `task-context-contract.md` (14 fields, consumer assumptions, completeness/staleness, audit record).

### Trust-architecture commitments

- **M. Oracle-swappability and vendor-neutrality.** No methodology commitment, template, or contract is written against a single LLM vendor's API surface, model family, or session mechanics. Inference calls specify the capability required (classification, extraction, synthesis, critique) rather than the vendor or model. A project that pins a specific oracle does so in its Vision Envelope inference-regime declaration (§4.3), not in the methodology. Rationale: methodology survives vendor churn; oracle choice is a per-project axiom, not a methodology commitment.
- **N. Determinism-preferred-where-sufficient.** Where a deterministic rule, file inspection, or structural check produces the needed answer, inference is not invoked. Inference is used where natural-language interpretation, novel synthesis, or judgment is load-bearing; structure is used everywhere else. Rationale: each inference call is an auditable cost and a failure surface; determinism is both cheaper and more auditable where it suffices. Grounding: the principle of deterministic structure with nondeterministic content, and the Leino formal-methods tradition (prefer proof to test where proof suffices).
- **O. Inference-provenance audit.** Every inference call load-bearing for a methodology decision leaves a provenance record: the packet supplied (or its hash), the consumer identity, the decision or output, and the timestamp. Recording is append-only. The skeletal form is specified in `task-context-contract.md` Field 14 and §5 (Audit record); methodology operations that invoke inference outside a task-context packet (e.g., a convention panel's inference calls) satisfy the same minimum-field standard.

### Verification-application rule

The Leino → DbC → Dafny → NASA P10 stack (anchor at Development per `anchor-map.md`) applies to ieops artifacts as follows:

- **Methodology artifacts** (Charter, Envelope, task-context packet, this specification, anchor-map, operating templates) carry **well-formedness predicates** and **decidability statements**. They do not carry compiled-verified or model-verified proofs; their correctness is structural and decidable by inspection.
- **Project artifacts** (the codebases produced under the methodology) at Development stage carry **verification artifacts** per §3.A.5 and the stage-gate exit `phase-1-contracts.md` §12.2.X.D.6.
- **NASA P10 rules** are project-stage obligations, not methodology-artifact obligations. The methodology specifies *that* the stack applies; the project specifies *which* P10 rules apply at Development per the project's verification classification.

The boundary is decidable: an artifact lives in the `methodology/` subfolder of an ieops workspace and is subject to methodology rules; a project artifact lives in a project workspace scaffolded from the ieops template and is subject to project rules. Methodology-internal inference is governed by commitments M–O regardless (per §4.3 composition rule).

## 4. Modes (Q4)

The methodology recognizes four distinct modal axes, each with decided content.

### 4.1 Weight (Q4(a))

Per-stage weight vocabulary sourced from the stage's anchor.

- **Scoping:** Flyvbjerg reference-class sizing.
- **Development:** three-level SAIP-anchored weight vocabulary:
  - **QA-affecting** — change modifies a ratified quality attribute scenario, introduces a new QAS, or re-prioritizes QAS response measures. Heaviest. Triggers architectural review (panel or ATAM where activated).
  - **Structure-affecting** — change modifies module decomposition, adds or removes components, or changes interfaces between components per arc42 §5 (Building Block View). Heavy. Requires arc42 §5 update and spec-first verification for affected modules.
  - **Local** — change is within-module, within-component, or within-tactic. Standard verification; no architectural review required.
  Each level is decidable against a concrete artifact: the QAS list (for QA-affecting), arc42 §5 building blocks and component boundaries (for Structure-affecting), existing module/tactic scope (for Local). Sources: SAIP's QA → tactics → implementation stack; arc42 §5 as the structural referent.
- **Deployment:** ITIL change types (standard / normal / emergency).
- **Heartbeat:** ITIL (ongoing change) + Hollnagel adjustment class (routine adaptation / disruption response).

### 4.2 Activity kind (Q4(b))

Modal separation between deliberation and execution.

- **Deliberation mode** (convention, panel, systematic literature review (SLR), conference): no code is committed, no implementation decisions are ratified; produces specifications, findings, or assessments.
- **Execution mode** (implementation): no vision is re-interpreted, no commitments are re-opened; produces code and artifacts against an already-ratified plan.
- **Transition between modes is explicit** — a named hand-off, not a drift.

Empirical failure this addresses: the observed "PM-launches-into-fixes" pattern where procedural deliberation slipped into engineer-mode patching; and a related finding that "conventions and ideas drove development instead of user experience materializing."

### 4.3 Inference regime (Q4(c))

Not a methodology-level mode. Inference posture (inference-first, partial-inference, or zero-inference for the artifact being built) is a **per-project axiom**, declared in the project's Vision Envelope. The methodology provides the discipline container; each project fills in its own inference values. An inference-first product interface is an example project axiom, not a methodology-level commitment.

**Composition rule (methodology vs. project inference).** Two distinct inference scopes coexist and compose as follows:

- **Methodology-internal inference** — inference invoked by methodology operations themselves (panel deliberation, classification inside operating-template rules, task-context computation, drift-checkpoint synthesis). Governed unconditionally by commitments M, N, O. Applies regardless of project posture.
- **Project-internal inference** — inference invoked by the artifact being built (e.g., a product's pipeline calls, a research instrument's classification calls). Governed by the project's Vision Envelope §8 inference-regime declaration.

The two compose by **strictness composition**: where the project's regime is stricter than M–O (e.g., the project forbids inference for a class of operations), the project's regime governs; where M–O require audit or capability-only specification, that requirement holds regardless of project posture. The project's regime cannot relax M–O for methodology operations executed inside the project's workspace.

Decidability: the composition is evaluated by inspecting (a) the project's Envelope §8, (b) the operation's classification (methodology-internal vs. project-internal), (c) the M–O commitments. No inference call is needed to decide which regime applies.

### 4.4 Build vs. runtime (Q4(d))

**Build-side only.** ieops governs the builder's work. It does not specify how end-users of products built with ieops interact with those products; products carry their own runtime concerns. Heartbeat remains in scope (already anchored with ITIL + Hollnagel + STPA + Diátaxis) but is deliberately left minimal until real runtime signals exist to specify against — overbuild-avoidance is an explicit directive.

## 5. Structural form (Q5)

### 5.1 Primary form (Q5(a))

**Workspace template** as the primary and sole shipping form. The methodology ships as: a workspace template directory + a spin-up script + a repo-level README + CLAUDE.md that imports README. ieops does not specify, bundle, or commit to a plugin architecture. Future Claude Code plugins may pair with ieops as separate, user-built tools.

### 5.2 Project relationship (Q5(b))

**Copy-per-related-project-group.** A project adopting ieops copies the template into its own workspace and diverges from upstream. One workspace may host multiple *related* projects (reference subjects, supporting utilities, companion plugins). Relatedness is the gating constraint — unrelated projects get their own copies. The template carries structure (scaffolding, templates, decision-log skeleton, CLAUDE.md patterns), not heavy reference content; users populate `references/` themselves. Workspace usage at first contact is presented as two light suggestions — single-project (canonical) or multi-project (changeable) — per the workspace-root `../vision-envelope.md`.

### 5.3 Forms in tension

**Intentional Diátaxis hybrid.** The workspace-root `../vision-envelope.md` is, in its bootstrap state, by design a Diátaxis hybrid (the artifact serves as both the in-bootstrap-state envelope and as how-to instruction to two audiences — Claude and the PL — until ratification). This is the artifact-as-state principle: the workspace's documents are self-describing about their own state, and behavior emerges from artifact content rather than from special first-run mode logic. The hybrid is a deliberate design choice, not a Diátaxis violation.

## 6. Audience (Q6)

**Primary audience and operator: Claude Code**, as the inference agent that runs the project. The methodology scaffolds Claude's inference toward reliable, product-oriented results.

**Human interface: natural language.** The human Project Lead communicates with Claude Code through natural language; they are not a direct methodology operator. Documentation priorities follow: methodology artifacts are written for Claude consumption first; human-facing documentation is shaped around the language interface (understanding what Claude is doing, intervening, redirecting).

This directly motivates commitments K and L.

## 8. Phase 1 artifacts produced

| Artifact | Path | Role |
|----------|------|------|
| Project-Lead Charter (ieops default) | `project-lead-charter.md` | Default PL methodology; grounds the Chief Engineer composite into operating rules, responsibilities, interaction protocol, escalation rule, substitution path |
| Vision Envelope template (ratified form) | `vision-envelope-template.md` | Project-level artifact the Charter references; blank form for per-horizon instantiation by the human PL |
| Vision Envelope (bootstrap form) | `../vision-envelope.md` | Bootstrap-state content at the workspace root; instructs first-contact behavior until ratification |
| Anchor map | `anchor-map.md` | Diagram, composition rules, summary table, anchor-literacy assumption statement |
| Task-context contract | `task-context-contract.md` | 14-field contract for any task-context packet supplied to a subagent, persona, or load-bearing inference call |
| Context Engineering operating template | `context-engineering-operating-template.md` | Nine rules operationalizing commitment K |
| Phase 1 commitments | `phase-1-commitments.md` | This document |
| Phase 1 contracts | `phase-1-contracts.md` | Decidability spine (anchor predicates, BLOCK criterion, stage gates, traceability) |

## 11. Methodology's own commitments, summarized in one page

Per commitment I (one-page communicability), the methodology's spine in short form:

- **Name.** ieops — Inferential Engineering Operations.
- **Scope.** Build-side methodology for infrastructure-grade, consequential software projects run by inference.
- **Primary audience.** Claude Code as inference agent; human PL through natural language.
- **Structural form.** Workspace template (copy-per-related-project-group) shipped with a spin-up script, README, and CLAUDE.md.
- **Spine.** Lifecycle Scoping → Development → Deployment → Heartbeat, with stage anchors (Flyvbjerg, INCOSE, arc42+SAIP+DSA+C4, Leino, ITIL, Hollnagel) and cross-cutting anchors (STPA, Diátaxis, Chief Engineer, Context Engineering). See `phase-1-contracts.md` §7 for the slate with ATAM activation predicate; see `anchor-map.md` for diagram and composition rules.
- **Modal structure.** Modal separation between deliberation and execution; per-stage weight vocabulary; inference regime is per-project; build-only scope.
- **Load-bearing commitments.** Working pipeline first (A); architectural plan anchor (C); STPA-early (D); working-before-modifying (E); one-page communicability (I); anchoring in named external frameworks (J); LLM ergonomics (K) and task-context calculation (L) as first-class; trust-architecture commitments M (oracle-swappability), N (determinism-preferred), O (inference-provenance audit).
- **PL role.** Grounded in the Chief Engineer composite; operates via the PL Charter; delegates to personas or other operators via a ratified Vision Envelope.
- **Decidability surface.** See `phase-1-contracts.md` §§7, 10, 12, 13 for the predicate spine (ATAM activation, BLOCK criterion, stage gates, traceability).
