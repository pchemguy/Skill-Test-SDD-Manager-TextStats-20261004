# TextStats delivery plan

Deliver the complete [SPEC.md](SPEC.md) through a useful named-file MVP, reliable/documented release, then source extensions. [layout.md](layout.md) assigns physical ownership; TASKS derives executable units.

## Phase 1 — Named-file utility

### Milestone 1.1 — Named-file counting MVP

Scope: immutable public value, count_text/count_file, exact text/BOM semantics, named-file UTF-8 success, and useful module CLI with one input, help, --keep-bom and -- handling. API and CLI agree on counts. Establish real, discoverable unit/integration checks alongside the slice. Included contracts: S-1/S-2, S-3 success and owned success-handle lifecycle, S-4 success/help/option validation. Required failure hardening and release documentation/distribution conclude in 1.2; stdin concludes in phase 2.

Prerequisite: reviewed preparation inputs and Python 3.11+. Exit: users can count a named UTF-8 file through the public API and actual module entry; exact stdout/stderr/status, path forms, BOM and terminator examples pass; input is unchanged. Final milestone code review, relevant tests, blocker repairs and committed report are mandatory. Demonstrate a normal file, a BOM file and a dash-prefixed filename. This informs the human's continue/amend/simplify/stop decision about usefulness and command syntax; routine authorized work needs no renewed approval.

### Milestone 1.2 — Reliable documented distribution

Prerequisite: 1.1 complete. Scope: all file/decode/resource and CLI diagnostic failures, invalid invocation before acquisition, public API/module docs, runnable README and source distribution checks. Included contracts: complete S-3/S-4 and phase 1 S-7. Keep the 1.1 path working throughout.

Exit: missing/unreadable/malformed inputs, failure silence and status/diagnostics, handle closure, unchanged input and no partial success are verified; nonempty product unit/integration suites pass independently; documented examples work; an isolated extracted source package runs python -m textstats. Workflow fixtures remain a separate suite. Final milestone code review/testing/repair/report is required. Demonstrate useful failure diagnostics and the extracted-package invocation to inform release readiness.

### Milestone 1.3 — Phase 1 review

Dedicated single phase code review/testing/report outcome after both delivery milestones complete (and close when hosting is active). Exit: cross-component S-1 through S-4 and delivered S-7 acceptance, docs and distribution evidence, prior milestone findings carried forward, required defects repaired and phase report committed/pushed. Only full phase completion permits explicit phase-branch integration into main, merged-state verification and publication.

## Phase 2 — Output and source extensions

### Milestone 2.1 — Retired historical JSON output

Stable milestone 2.1 and T-010–T-012 retain completed historical evidence; their JSON delivery is retired by the accepted scope. Current delivery requires text output only. The steering amendment reassesses retained S-1–S-4/S-7/S-8 acceptance; historical JSON acceptance does not govern remaining work.

### Milestone 2.2 — UTF-8 stdin and final release

Prerequisite: historical 2.1/T-012 baseline and accepted text-only amendment. Scope: INPUT -, binary stdin until EOF, locale-independent strict UTF-8, borrowed-handle lifecycle, empty/error inputs and text output and both BOM policies. Included contracts: S-6, stdin composition under S-8 and final S-7 with S-1–S-4 retained and S-5 retired. Selection uses the retained ASCII validation, full strict decode, single BOM normalization and original terminator/EOF rules. ./- addresses a literal file named -.

Exit: actual module subprocess accepts piped UTF-8 bytes independent of locale, empty stdin and invalid bytes produce required outcomes; an injected read failure identifies stdin without partial stdout; borrowed stdin stays open; named-file behavior regresses successfully. Both range spellings and BOM option orders, invalid/repeated ranges before acquisition, huge ASCII endpoints, beyond-EOF and malformed bytes after END pass for stdin. Updated API/module/README docs and isolated extracted-source checks cover stdin/text/ranges. Final milestone code review/testing/repair/report is mandatory. Demonstrate piped text and error behavior to inform final release readiness.

### Milestone 2.3 — Phase 2 and final review

Dedicated single phase code review/testing/report outcome after current delivery milestones complete/close and historical 2.1 retirement is reconciled. Exit: complete main SPEC acceptance, cross-source/BOM regressions, nonempty suites, runnable documentation and extracted-source distribution checks pass; blockers repaired; prior findings retained; phase report and final implementation report aggregate unresolved admissible TODOs and resolution references. Explicit verified phase integration and publication conclude the authorized full implementation when separately requested.

### Milestone 2.4 — Named-file line ranges

Prerequisite: historical completed/published milestone2.1/T-012 at the pinned paused baseline, current main SPEC/design QC and separately authorized implementation. No prerequisite on unfinished stdin or main final review; whole-input named-file text already works. Delivery retains the useful baseline while introducing a source-independent normalization/selection seam, then composing command validation/acquisition/rendering into a named-file slice. Pure helper work is a bounded prerequisite to the earliest usable changed CLI path, not a released skeleton.

Scope: S-8 and retained S-1–S-4/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded decimals, text and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.

Exit: actual module invocation counts selected named-file lines in text with exact stdout/status/stderr; supplied examples, ASCII/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.

### Milestone 2.5 — Range feature review

Dedicated single feature-scoped phase review/testing/report outcome after delivery milestone2.4 completes/closes when tracking is active. Exit: cross-component range/API/BOM/text/decode/lifecycle/docs/distribution acceptance, prior finding disposition, blocker repair and committed/pushed feature phase report. Aggregate feature TODOs and final feature implementation report. This is not main milestone2.3/T-017 or a whole-project Phase2 completion claim.

Range integration requires accepted main owners, unique task ownership and verified feature exits before an explicit merge into the paused phase target. Main stdin tasks remain incomplete. Full Phase 2 completion additionally requires 2.2/2.3; the scoped 2.5 review cannot complete Phase 2.

## Verification and sequencing

Count product tests separately from workflow checks; zero-test discovery never passes. Unit evidence covers pure semantics and boundaries; integration evidence invokes actual module entry and public imports against real files/bytes. Distribution evidence runs extracted sources from an isolated working directory with no checkout-derived import path. Documentation examples are verified when delivered.

Use unittest discovery for each product suite. Required checks include API silence, failure atomicity, strict decoding, owned/borrowed stream lifetime and unchanged bytes. Do not rely on CLI tests alone to verify API resource contracts, or on mocks alone to establish end-to-end success. Full-phase exits require code review and testing, not just checkboxes. Hosting is optional and inactive for preparation; later activation projects only an eligible phase before its first task.

## Scope and risk

Phase 1 has two cohesive delivery milestones; Phase 2 has two current delivery milestones (2.2, 2.4) and retired historical 2.1, its main final review 2.3 and the scoped range review 2.5. Range delivery is independent of unfinished stdin; numeric milestone order does not impose a dependency. Design preserves complete decoding and single BOM normalization before source-independent selection. Main API remains whole-input. Locale decoding, universal-newline translation, accidental second BOM stripping, borrowed-stream closure, checkout leakage into distribution checks and zero-test discovery are explicit verification risks. There are no unresolved material planning decisions.
