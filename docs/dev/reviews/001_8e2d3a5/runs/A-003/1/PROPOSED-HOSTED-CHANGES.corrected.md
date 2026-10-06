# Corrected proposed hosted changes — assisted correction

Every object below is **proposed and unexecuted**. This is a separate reviewable proposal, not a successful hosted reconciliation or an activation claim. Both requested hosted reconciliation passes remain pending because the exposed connector lacks required native milestone and repository label creation/inventory/readback operations. No numerical issue, milestone or label ID is guessed.

Repository: `pchemguy/Skill-Test-SDD-Manager-TextStats-20261004`. Source baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. Owning list: `docs/dev/TASKS.md`; supporting outcomes/exits: `docs/dev/PLAN.md`; requirements/design/layout remain governing. Project only Phase 1; keep Phase 2 unprojected. All tasks remain unchecked, no implementation is authorized here.

## Proposed, unexecuted phase label

Name: `sdd-phase-1-Named-file-utility`.

Description: `Phase 1: useful named-file UTF-8 counting API/CLI and reliable documented source distribution.`

Stable phase identity: Phase 1 — Named-file utility. No hosted object ID is available. Repository label inventory and readback must precede activation.

## Proposed, unexecuted native milestone 1.1

Title: `sdd-1.1-Named-file-counting-MVP`. Initial state: open. Owning phase: Phase 1 — Named-file utility. Native milestone number: unresolved; obtain it from confirmed provider readback.

Proposed description, derived from PLAN:

Scope: immutable public value, count_text/count_file, exact text/BOM semantics, named-file UTF-8 success, and useful module CLI with one input, help, --keep-bom and -- handling. API and CLI agree on counts. Establish real, discoverable unit/integration checks alongside the slice. Included contracts: S-1/S-2, S-3 success and owned success-handle lifecycle, S-4 success/help/option validation. Required failure hardening and release documentation/distribution conclude in 1.2; JSON and stdin conclude in phase 2.

Prerequisite: reviewed preparation inputs and Python 3.11+. Exit: users can count a named UTF-8 file through the public API and actual module entry; exact stdout/stderr/status, path forms, BOM and terminator examples pass; input is unchanged. Final milestone code review, relevant tests, blocker repairs and committed report are mandatory. Demonstrate a normal file, a BOM file and a dash-prefixed filename. This informs the human's continue/amend/simplify/stop decision about usefulness and command syntax; routine authorized work needs no renewed approval.

## Proposed, unexecuted native milestone 1.2

Title: `sdd-1.2-Reliable-documented-distribution`. Initial state: open. Owning phase: Phase 1 — Named-file utility. Native milestone number: unresolved; obtain it from confirmed provider readback.

Proposed description, derived from PLAN:

Prerequisite: 1.1 complete. Scope: all file/decode/resource and CLI diagnostic failures, invalid invocation before acquisition, public API/module docs, runnable README and source distribution checks. Included contracts: complete S-3/S-4 and phase 1 S-7. Keep the 1.1 path working throughout.

Exit: missing/unreadable/malformed inputs, failure silence and status/diagnostics, handle closure, unchanged input and no partial success are verified; nonempty product unit/integration suites pass independently; documented examples work; an isolated extracted source package runs python -m textstats. Workflow fixtures remain a separate suite. Final milestone code review/testing/repair/report is required. Demonstrate useful failure diagnostics and the extracted-package invocation to inform release readiness.

## Proposed, unexecuted native milestone 1.3

Title: `sdd-1.3-Phase-1-review`. Initial state: open. Owning phase: Phase 1 — Named-file utility. Native milestone number: unresolved; obtain it from confirmed provider readback.

Proposed description, derived from PLAN:

Dedicated single phase code review/testing/report outcome after both delivery milestones complete (and close when hosting is active). Exit: cross-component S-1 through S-4 and delivered S-7 acceptance, docs and distribution evidence, prior milestone findings carried forward, required defects repaired and phase report committed/pushed. Only full phase completion permits explicit phase-branch integration into main, merged-state verification and publication.

## Proposed, unexecuted task issue T-001

Title: `[T-001] Establish immutable statistics and pure text counting`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.1 — Named-file counting MVP, native title `sdd-1.1-Named-file-counting-MVP`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-001 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: textstats/core.py, initial public facade, tests/unit/ discovery packages and semantic/value tests. Depends on: reviewed preparation inputs.

Outcome: direct TextStats/count_text imports, immutable nonnegative fields and exact BOM/CRLF/CR/LF/Unicode-word semantics (S-1/S-2).

Evidence: nonempty unit discovery; all SPEC sample rows, retained/interior/double BOM, silence and immutability/nonnegative checks. Keep pure core independent of acquisition/process state.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-001 -->

## Proposed, unexecuted task issue T-002

Title: `[T-002] Integrate strict UTF-8 named-file API`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.1 — Named-file counting MVP, native title `sdd-1.1-Named-file-counting-MVP`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-002 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: textstats/io.py, facade exports, focused unit/file integration checks and tests/integration/ discovery packages. Depends on: T-001.

Outcome: count_file supports str/PathLike, preserves input terminators, delegates counts and closes its success-path owned handle (S-3 success).

Evidence: direct package API import/signatures; real temporary files for BOM/newline/empty/Unicode cases; unchanged input; silent calls and success-handle closure. Required failure-path hardening follows in T-005.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-002 -->

## Proposed, unexecuted task issue T-003

Title: `[T-003] Deliver the useful named-file module CLI`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.1 — Named-file counting MVP, native title `sdd-1.1-Named-file-counting-MVP`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-003 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: textstats/cli.py, textstats/__main__.py and integration subprocess checks. Depends on: T-001, T-002.

Outcome: one named input, --keep-bom, -- dash filenames and help; exact text output and option validation before acquisition (S-4 success/options).

Evidence: actual python -m textstats invocation, stdout/status/stderr assertions, API/CLI agreement, missing/extra/unknown option rejection and no input read on usage errors; demonstrate ordinary/BOM/dash filenames. Keep later JSON/stdin delivery absent from this task.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-003 -->

## Proposed, unexecuted task issue T-004

Title: `[T-004] Review, test and report milestone 1.1`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.1 — Named-file counting MVP, native title `sdd-1.1-Named-file-counting-MVP`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-004 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Depends on: T-001, T-002, T-003. Scope: delivered core, file API, facade and module CLI; relevant nonempty product suites and MVP demonstration.

Evidence: actual code review, milestone exits/regressions, blocker repairs and committed/pushed report. Report: docs/dev/reports/phases/1/1.1.md. Record TODO or None and the usability decision evidence. No product completion inferred from workflow fixtures.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-004 -->

## Proposed, unexecuted task issue T-005

Title: `[T-005] Harden named-file API failure and resource behavior`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.2 — Reliable documented distribution, native title `sdd-1.2-Reliable-documented-distribution`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-005 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: textstats/io.py and focused unit/integration failures. Depends on: T-004.

Outcome: missing/unreadable files propagate OSError subclasses, strict bad-byte decoding raises UnicodeDecodeError, failure calls are silent, input unchanged, owned handles closed and no partial result (S-3).

Evidence: real missing/bad-byte files plus portable injected unreadable/read/close seams; both BOM policies; byte-for-byte preservation and owned-handle success/failure checks. Do not rely solely on permission bits under privileged execution.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-005 -->

## Proposed, unexecuted task issue T-006

Title: `[T-006] Complete CLI diagnostics and public documentation`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.2 — Reliable documented distribution, native title `sdd-1.2-Reliable-documented-distribution`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-006 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: textstats/cli.py, docs/api.md, docs/module.md, README.md and relevant unit/integration checks. Depends on: T-005.

Outcome: useful input-identifying expected-error diagnostics, statuses 1/2, empty stdout/no traceback, retained help/options/success and documented runnable phase 1 API/module usage (S-4 and S-7 docs).

Evidence: actual module missing/read/decode failures, invalid invocation before acquisition, unchanged files; run documented API/help/text/BOM examples. Preserve original README content and SDD links.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-006 -->

## Proposed, unexecuted task issue T-007

Title: `[T-007] Establish isolated source-distribution acceptance`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.2 — Reliable documented distribution, native title `sdd-1.2-Reliable-documented-distribution`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-007 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Scope: Makefile, generated-output ignore rules and tests/integration distribution checks. Depends on: T-006.

Outcome: standard-library source archive includes importable package, README and public docs; generated dist/extractions stay untracked (S-7).

Evidence: build/extract to temporary root; invoke extracted python -m textstats with a clean import environment from that root; check exact named-file counts, --keep-bom, help and representative failure status. Independently discover nonzero unit/integration suites and run README examples. Keep workflow fixtures separate and pinned resources unchanged.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-007 -->

## Proposed, unexecuted task issue T-008

Title: `[T-008] Review, test and report milestone 1.2`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.2 — Reliable documented distribution, native title `sdd-1.2-Reliable-documented-distribution`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-008 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.

Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-008 -->

## Proposed, unexecuted task issue T-009

Title: `[T-009] Review, test and report phase 1`.

Initial state: open. Phase label: `sdd-phase-1-Named-file-utility`. Parent: Milestone 1.3 — Phase 1 review, native title `sdd-1.3-Phase-1-review`. Issue number and milestone number: unresolved; never guess them.

Proposed issue body:

### Task brief <!-- sdd-forge:task-id=T-009 -->

**Context:** Planned Phase 1 named-file utility work under the accepted owning milestone. The intended task outcome and checks below are requirements, not achieved results.

Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.

Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.

**Sources:** [TASKS](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/TASKS.md), [PLAN](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/PLAN.md), [SPEC](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/SPEC.md), [layout](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/layout.md), [design](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/blob/main/docs/dev/DECOMPOSITION.md).

<!-- /sdd-forge:task-id=T-009 -->

## Required recovery and repeat reconciliation

With a capable approved client/transport, re-read repository identity/access and complete native label/milestone inventory, then search exact task IDs across open and closed issues excluding PRs. Validate title and identity marker; stop on duplicate IDs, ownership conflicts or incomplete inventory. Reconcile only managed fields and sections, preserving user material, unrelated labels, assignees and comments. Reuse existing parents by stable identity, then create any missing phase label and native milestones, and create/reconcile each issue with both parent associations. Read back all phase parents and nine task issue title/marker/associations before activation can be Ready. Reconcile that same phase a second time by identity; do not duplicate objects. No task/milestone closure or later-phase creation is proposed. Stop before implementation.

## Exact governing source identities

- `docs/dev/PROJECT.md`: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- `docs/dev/ARCHITECTURE.md`: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- `docs/dev/DECOMPOSITION.md`: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- `docs/dev/SPEC.md`: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.
- `docs/dev/PLAN.md`: SHA-256 `8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8`.
- `docs/dev/layout.md`: SHA-256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- `docs/dev/TASKS.md`: SHA-256 `2e0af38698b5edf3911265da98815790143e2e5c1500b3bc04148ead2b9a8454`.
- `docs/dev/SPEC-REVIEW-REPORT.md`: SHA-256 `e4522d4a6d566d3dd6c7b208930547f152229ca3dd9a04028ce136a937a0df68`.
- `docs/dev/PLAN-REVIEW-REPORT.md`: SHA-256 `01f3041e8ccd688060ff51e0c7dd825475d44dfbcca73c31910bab038e231591`.
- `docs/dev/TASKS-REVIEW-REPORT.md`: SHA-256 `7a7e8f361bd18f4a6e5f580d87cc8f9757996be2fdbb214c44d59ca321404412`.
