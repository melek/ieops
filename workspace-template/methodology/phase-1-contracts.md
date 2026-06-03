# ieops — Phase 1 Contracts

**Diátaxis mode.** Reference (decidable predicates, stage gates, traceability spine).

**Methodology.** ieops (Inferential Engineering Operations)
**Phase.** 1 — Specification (contracts layer)
**Version.** v0.1.
**Status.** v0.1.
**Companion document.** `phase-1-commitments.md` (commitments, modes, structural form, audience, artifact register).

## 0. Preamble

This document is the *contracts layer* of the ieops Phase 1 specification — the decidability spine. It carries the anchor slate with the ATAM activation predicate, the BLOCK criterion, stage-gate entry/exit criteria, and the traceability spine. This layer absorbs review-pass output and grows monotonically under review cycles; the stable layer (name, failure modes, commitments, modes) lives in `phase-1-commitments.md`.

**Predicate decidability.** Predicates in this document are paired with explicit decidability statements. Two classes of decidability exist and are distinguished where the distinction matters:

- **Structural decidability.** The predicate is evaluable by checking file presence, field population, or string match. The evaluator does not need to interpret semantic content.
- **Content-dependent decidability.** The predicate inherits decidability from the inspected content's own well-formedness — e.g., "the Envelope §1 vision statement declares a horizon end-condition" is decidable only if §1 itself was well-formed when ratified. Content-dependent predicates compose: their decidability is no stronger than the upstream artifact's.

The §12.5 stage-gate decidability statement names the structural class as the default; clauses that fall into content-dependent decidability are flagged inline.

## 7. Anchor slate

See `anchor-map.md` for the full diagram and composition rules. Summary:

### Stage-specific anchors

| Stage | Anchor | Role |
|-------|--------|------|
| Scoping (primary) | Flyvbjerg & Gardner, *How Big Things Get Done* (2023) | Reference-class forecasting; modularity-over-monolith; "think slow, act fast" |
| Development (primary) | INCOSE SE Handbook 5e (2023) | Lifecycle vocabulary, process reference |
| Development (primary) | arc42 + C4 + Bass/Clements/Kazman SAIP + DSA | Architecture design: operational template + diagramming + foundational pedagogy + documentation method |
| Development (primary) | Leino *Program Proofs* (2023) → DbC (Meyer) → Dafny → NASA P10 | Specification foundation, verification discipline, instrument, rules. Application rule: see `phase-1-commitments.md` §3 "Verification-application rule." |
| Deployment | ITIL change types (standard / normal / emergency) | Change classification |
| Heartbeat | Hollnagel, resilience engineering | Work-as-done; runtime monitoring |

### Cross-cutting anchors

| Anchor | Scope |
|--------|-------|
| STPA / STAMP (Leveson) | Hazard control structure |
| Diátaxis (Procida) | Documentation architecture (four modes) |
| Chief Engineer composite (Brooks *conceptual integrity* + Johnson Skunk Works 14 rules + aerospace project CE role tradition) | Project leadership: vision-holding, taste, long-term direction |
| Context Engineering composite (attention-degradation SLR + proportional-response SLR + persona-prompting SLR + HCI cognitive-ergonomics tradition: Sweller / Suchman / Hollnagel) | Context ergonomics for model and human; budgets, spatial layout, compression, proportional provisioning, terminology discipline, persona-safety |

### Architecture Design cluster placement

SAIP quality attribute scenarios surface at Scoping (feed arc42 §10); ATAM is an optional Development-exit architecture-review step that activates when scope justifies; SAIP architectural tactics are Development-stage vocabulary.

**ATAM activation predicate (any of T.1–T.4 triggers ATAM at Development-exit).**

- **T.1 Reference-class scale.** Project sized at "megaproject" or "exceptional" reference class at Scoping per Flyvbjerg sizing (recorded in the project's decision log or Vision Envelope).
- **T.2 QAS conflict.** Three or more ratified Quality Attribute Scenarios at the project's QAS list (Envelope §2 / arc42 §10) name a tradeoff against another listed QAS.
- **T.3 Cross-component QAS dependence.** At least one QAS's response measure depends on properties of two or more arc42 §5 building blocks, recorded as a cross-component interaction.
- **T.4 PL flag.** The Vision Envelope §4 decision-latitude or §5 escalation-trigger list explicitly names "ATAM activation" as a PL judgment for this horizon.

**Decidability.** Each trigger is decidable by inspection of named files (the project's decision log, Envelope §2/§4/§5, arc42 §5 and §10). T.2 ("QAS conflict") and T.3 ("cross-component QAS dependence") are content-dependent: they require the QAS list itself to have been authored with well-formed tradeoff and dependence declarations. The activation decision is recorded in the audit log per Envelope §8 once made.

**Soundness/completeness trade.** This predicate trades completeness for soundness — disjunctive triggers approve activation when any clause fires, structurally well-formed cases that fail a clause typographically (e.g., a QAS conflict described in prose rather than enumerated against the list) may not trigger. Pass requires structural well-formedness, not semantic equivalence to it.

## 10. BLOCK criterion (panel verdicts)

**BLOCK criterion (B.1–B.4, all required for a verdict to count as BLOCK).** A panelist's verdict counts as BLOCK rather than CONCERN when:

- **B.1 Failure-mode citation.** The panelist names at least one specific failure mode from `phase-1-commitments.md` §2 — by number or by direct paraphrase that maps to one §2 entry.
- **B.2 Prevention claim.** The panelist asserts the spec as written, including artifacts referenced by pointer (Charter, Envelope, anchor map, task-context contract, Context Engineering operating template), would not prevent that failure mode in a concretely described future scenario the panelist articulates.
- **B.3 Specific gap.** The panelist names one specific decidable gap that would close the prevention argument: a missing predicate, a missing contract, a missing artifact-location specification, or a missing decidability statement. Prose disagreement without a named gap is CONCERN, not BLOCK.
- **B.4 Closure condition.** The panelist states the closure condition: what artifact change would convert the BLOCK to PASS or CONCERN.

**Decidability.** A BLOCK verdict is itself decidable. A reviewer of the verdict checks B.1 (a §2 reference is present), B.2 (a scenario is described), B.3 (the gap is named in the spec's own form: predicate / contract / artifact-location / decidability), and B.4 (the closure condition is stated). Verdicts failing any of B.1–B.4 are returned to the panelist for re-statement; they do not block phase progression by default. B.2 is content-dependent: evaluating whether a described scenario is "concrete" requires interpretation, which is why §10's closing paragraph names the BLOCK criterion as itself a §10 instance of the spec's meta-pattern.

**Soundness/completeness trade.** The predicate trades completeness for soundness — verdicts that meet B.1–B.4 are honored as BLOCK; verdicts that name a real prevention gap but fail to articulate it in B.1–B.4 form are returned for re-statement rather than absorbed. Pass requires structural well-formedness, not semantic equivalence to it.

**Rationale.** A recurring meta-pattern in the methodology's own review was that the spec specifies *what* but under-specifies *when something is decidable*. The BLOCK criterion is itself a §10 instance of that pattern. Without B.1–B.4, BLOCK can be invoked by prose disagreement and can stall phase work without a defined closure path; with B.1–B.4, BLOCK is a precise instrument for catching specific gaps the spec must close.

## 12. Stage-gate criteria (Systems Engineering lens)

Each stage has decidable entry conditions (what must hold before the stage begins) and exit conditions (what must hold before the stage may close). Sources: INCOSE SE Handbook 5e (lifecycle stages and process reference); per-stage anchors named in §7.

### 12.1 Scoping

**Entry (E.S.1–E.S.3, all required).**
- **E.S.1** A Vision Envelope draft exists with §1 Vision statement and §2 Stakeholders + quality goals populated (may be terse; need not be ratified).
- **E.S.2** Reference-class lookup is identified per Flyvbjerg sizing — the project names a comparison class (or declares "no available reference class" with named search effort).
- **E.S.3** A clean working tree or named scoping branch exists (no in-flight implementation work would be invalidated by Scoping outputs).

**Exit (X.S.1–X.S.5, all required).**
- **X.S.1** Vision Envelope is ratified — §0 well-formedness checklist passes.
- **X.S.2** Quality Attribute Scenarios per SAIP exist for each top-priority quality goal in Envelope §2; tradeoffs are recorded.
- **X.S.3** Flyvbjerg reference-class output is recorded: comparison class, sizing band, modularity decision (modular / monolith).
- **X.S.4** STPA hazard analysis at scoping depth is present: top-level losses identified, system-level hazards listed (per Leveson STPA placement, this is a Scoping artifact, not a late-Development one).
- **X.S.5** ATAM activation predicate (§7) is evaluated and recorded — `ATAM activated: yes/no` with the triggers cited.

### 12.2 Development

**Entry (E.D.1–E.D.4, all required).**
- **E.D.1** Scoping exit conditions hold (or were re-ratified by the human PL after the most recent change).
- **E.D.2** arc42 §5 Building Block View has at least the top-level decomposition; each loop stage from Envelope §1 is mapped to a building block.
- **E.D.3** Per-task weight vocabulary (`phase-1-commitments.md` §4.1 — QA-affecting / Structure-affecting / Local) is the active classification; each in-flight task has a weight assigned.
- **E.D.4** Verification classification per task is declared for any task bearing a Leino-anchored verification expectation.

**Exit (X.D.1–X.D.6, all required).**
- **X.D.1** Prove-then-extend acceptance predicate (`phase-1-commitments.md` §3.A) holds for at least the project's stated minimum loop, before any extension iteration is committed.
- **X.D.2** Module decomposition matches arc42 §5 with no orphan code paths (paths that do not appear in §5 require a §5 update before exit).
- **X.D.3** Each ratified Quality Attribute Scenario from Scoping is bound to at least one architectural tactic per SAIP, recorded in the architecture documentation.
- **X.D.4** ATAM has run iff the activation predicate fired at Scoping; ATAM output is recorded.
- **X.D.5** STPA control-structure loss scenarios identified at Scoping have corresponding mitigations or accepted-risk records in the architecture documentation.
- **X.D.6** Verification artifacts exist per task verification classification: `[compiled-verified]` tasks have a Dafny source compiled to target language; `[model-verified]` tasks have a conformance map; `[test-verified]` tasks have tests.

### 12.3 Deployment

**Entry (E.DP.1–E.DP.3, all required).**
- **E.DP.1** Development exit conditions hold.
- **E.DP.2** Change classification per ITIL is selected (standard / normal / emergency) and recorded.
- **E.DP.3** Diátaxis-shaped operator documentation exists: at minimum, a how-to for the deployment operation and a reference for the deployed surface.

**Exit (X.DP.1–X.DP.3, all required).**
- **X.DP.1** Deployment outcome is recorded (success / partial / rolled-back) against the ITIL change record.
- **X.DP.2** Runtime signals required by Heartbeat are emitting (per Envelope §6 drift criteria mapped to runtime where applicable).
- **X.DP.3** Hollnagel work-as-done check has been recorded against the deployment plan.

### 12.4 Heartbeat

**Entry (E.H.1–E.H.2, all required).**
- **E.H.1** Deployment exit conditions hold.
- **E.H.2** Heartbeat instrumentation has at least the runtime signals identified at X.DP.2 emitting.

**Exit (X.H.1–X.H.2, applies on Heartbeat closure or major revision).**
- **X.H.1** Hollnagel adjustment-class summary is recorded for the Heartbeat horizon: which adjustments were routine adaptation, which were disruption response.
- **X.H.2** STPA runtime control-structure violations (if any) are recorded with disposition: mitigated / accepted / escalated.

### 12.5 Stage-gate decidability statement

Each entry and exit criterion above is decidable by inspection of named files: Vision Envelope, the project's decision log, arc42 §5 documentation, SAIP QAS list, ATAM output document, STPA control-structure document, audit log, ITIL change record, Heartbeat signal log. No criterion requires an inference call to evaluate.

**Structural vs. content-dependent decidability.** Most clauses are *structurally decidable*: the evaluator checks file presence, field population, or string match (e.g., X.S.5 "`ATAM activated: yes/no` with the triggers cited" — presence of the string and at least one trigger reference). A subset are *content-dependent*: their decidability is no stronger than the inspected content's own well-formedness. Examples:

- **E.D.2** "each loop stage from Envelope §1 is mapped to a building block" inherits decidability from Envelope §1's having declared crisp loop stages.
- **X.D.5** "STPA control-structure loss scenarios identified at Scoping have corresponding mitigations" inherits decidability from the loss-scenario list being well-formed at X.S.4.
- **X.DP.3** "Hollnagel work-as-done check has been recorded" is presence-decidable; whether the recorded check is a substantive work-as-done observation (vs. a perfunctory entry) is content-dependent.

Content-dependent clauses compose: a downstream stage gate's decidability is no stronger than the upstream gate's content well-formedness. This composition matches commitments M–O (per `phase-1-commitments.md` §3): methodology-internal predicate evaluation is itself subject to provenance and decidability discipline.

**Soundness/completeness trade.** Stage-gate predicates trade completeness for soundness — structurally well-formed cases that fail a clause typographically (e.g., an ITIL change classification declared in prose rather than as the named string) are rejected; pass requires structural well-formedness, not semantic equivalence to it.

## 13. Traceability spine (Systems Engineering lens)

The spine has seven steps; each step is a row in a project-specific traceability table maintained alongside arc42 documentation:

| Step | Source artifact | Per-step record | Forward link |
|---|---|---|---|
| 1. Stakeholder need | Vision Envelope §2 | `Need-N`: stakeholder, need statement | → QAS |
| 2. Quality Attribute Scenario | SAIP QAS list / arc42 §10 | `QAS-N`: stimulus, source, environment, artifact, response, response measure | → Tactic |
| 3. Architectural tactic | SAIP tactics catalog applied | `Tactic-N`: tactic name, QAS bound, rationale | → Module |
| 4. Module / building block | arc42 §5 | `Module-N`: building block ID, tactics realized | → Verification |
| 5. Verification | Per task verification classification | `Verif-N`: classification (`[compiled-verified]`, `[model-verified]`, `[test-verified]`), artifact path | → Change record |
| 6. Change record | ITIL change classification at Deployment | `Change-N`: ITIL type, deploy date, outcome | → Runtime signal |
| 7. Runtime signal | Heartbeat instrumentation | `Signal-N`: signal name, source module, threshold, alert binding | (closes loop to Need via Heartbeat work-as-done) |

**Decidability of spine completeness.** A traceability gap is decidable by inspection: any row missing a forward link is an open gap. The spine is **complete** for an exit gate when every Need row traces forward to at least one Signal; orphan rows (records with no upstream Need) are recorded as "out-of-band" with rationale.

**Per-stage activation.** Steps 1–2 close at Scoping exit (X.S.1–X.S.2). Steps 3–5 close at Development exit (X.D.3, X.D.6). Step 6 closes at Deployment exit (X.DP.1). Step 7 emits at Deployment exit (X.DP.2) and is monitored continuously at Heartbeat.

**Loop-closing rule.** The traceability spine closes back on itself at Heartbeat: Hollnagel work-as-done findings (X.H.1) feed back into Vision Envelope updates and stakeholder-need revisions, opening a new horizon when the divergence warrants.

---

**End of Phase 1 contracts.** Companion: `phase-1-commitments.md`.
