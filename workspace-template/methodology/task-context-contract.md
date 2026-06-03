# Task-Context Packet — Contract

**Diátaxis mode.** Reference (fields, contract, decidability).

**Purpose.** Specify the task-context-calculation contract at the level of inputs, outputs, completeness/staleness conditions, and what a subagent or inference call is entitled to assume about it.

**Implements.** Commitment L (`phase-1-commitments.md` §3). The methodology computes a task-context packet per task and supplies it to any operator — Claude itself, a delegated persona, a dispatched subagent, or a raw inference call. This file specifies what the packet contains, what consumers may assume, and when a packet becomes stale.

The contract is a Phase 1 artifact (the *what*). Wire format, serialization, and computation mechanics are Phase 3 concerns (the *how*).

---

## 1. Fields

Every well-formed packet contains the 14 fields below. **D** = deterministic structure (derived by rule from named files). **I** = inferred content (supplied by caller, or produced by an inference call).

The D/I split is the A1 analog named by Context Assembly — the packet records which fields the consumer may treat as ground truth vs. which it may re-examine.

| # | Field | Kind | Source |
|---|---|---|---|
| 1 | Task identifier | D | Caller-supplied or system-generated |
| 2 | Envelope pointer | D | Path to the ratified Vision Envelope governing the task |
| 3 | Charter pointer | D | Envelope metadata (`Governing Charter`) |
| 4 | Stage | D | Scoping / Development / Deployment / Heartbeat |
| 5 | Weight | D | Vocabulary from the Stage's anchor (Flyvbjerg / SAIP three-level / ITIL / ITIL + Hollnagel) |
| 6 | Mode | D | Deliberation / Execution (spec §4.2) |
| 7 | Inference regime | D | Envelope-declared (spec §4.3) |
| 8 | In-scope anchors | D | Computed from Stage + Weight per `anchor-map.md` composition rules |
| 9 | Decision latitude | D | Envelope §4, verbatim |
| 10 | Escalation triggers | D | Envelope §5 + Charter §6, verbatim |
| 11 | Task description | I | Caller-supplied natural language |
| 12 | Acceptance condition | I | Caller-supplied; operator verifies on completion |
| 13 | Prior-art pointers | D | Relevant prior decisions and related task audit records |
| 14 | Audit record pointer | D | Path the consumer writes its decisions and outputs to |

## 2. Consumer contract

A consumer receiving a well-formed packet may assume:

- **C1.** The referenced Envelope was ratified and satisfied `vision-envelope-template.md` §0 at ratification time.
- **C2.** Deterministic fields (D) are current as of the packet's timestamp; no hidden inputs shape the consumer's scope.
- **C3.** The Audit record pointer (Field 14) is writable and append-only.

And is bound by:

- **B1.** No anchor outside Field 8 may be introduced unilaterally; introducing a new anchor is an escalation per Charter §6.
- **B2.** Decisions within Field 9 are issued without escalation; decisions matching any Field 10 trigger return to the human PL before action.
- **B3.** The consumer appends its decisions and outputs to Field 14 before returning.

## 3. Completeness

A packet is **complete** iff all 14 fields are populated. Fields 11–12 may be terse but not empty. Field 8 is non-empty — at minimum, the Project-Leadership anchor (Chief Engineer composite) plus the stage-specific anchor apply to every task.

An incomplete packet is not supplied; the computation fails closed.

## 4. Staleness

A packet becomes **stale** when any of the following occur after its timestamp:

- **S1.** The referenced Envelope is amended or re-ratified.
- **S2.** The Governing Charter is amended or substituted.
- **S3.** `anchor-map.md` is modified in a way that would change Field 8.
- **S4.** A drift checkpoint (Envelope §6) reports divergence.

A stale packet must be recomputed before the consumer begins a new sub-step. In-flight work under a packet that becomes stale mid-execution is not invalidated retroactively; the next sub-step triggers recomputation.

## 5. Audit record

The Audit record (Field 14) is append-only and records, at minimum:

- The packet supplied (by value or content hash).
- The consumer's identity (persona name, subagent dispatch ID, or "PL").
- The decision or output produced.
- The timestamp.

## 6. Decidability

Packet well-formedness, completeness, and staleness are decidable by inspection of named files: `vision-envelope-template.md`, `project-lead-charter.md`, `anchor-map.md`, the task-specific Envelope, and the audit log at Field 14. No consumer assumption or staleness trigger requires an inference call to evaluate.

---

## Cross-references

- `phase-1-commitments.md` §3.L — commitment this contract implements.
- `vision-envelope-template.md` §0 — well-formedness predicate referenced by C1.
- `project-lead-charter.md` §4, §6 — ratification and escalation rules referenced by C1, B1, B2.
- `anchor-map.md` — composition rules referenced by Field 8.
