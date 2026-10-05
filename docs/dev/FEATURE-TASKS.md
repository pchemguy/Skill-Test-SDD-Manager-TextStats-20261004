# Named-file ranges executable feature tasks

Active owner for the scoped [FEATURE-SPEC](FEATURE-SPEC.md) delta, derived from Ready [FEATURE-PLAN](FEATURE-PLAN.md), existing [layout](layout.md) and [package design/identity](features/002_ea97182/README.md). Main [TASKS](TASKS.md) retains T-001–T-017; completed T-012 is this feature's baseline prerequisite. T-013–T-017 and stdin remain incomplete and are not prerequisites for named-file range delivery. Project-wide new IDs start at T-018. All feature tasks are planned/unchecked.

Existing Phase2 identity is reused; feature parents measure only this delta. These new2.4/2.5 groups do not close/complete main Phase2, replace2.3/T-017 or reassign existing tasks. Hosted tracking is maintained, but preparation creates no objects; active-phase added-work projection/readback is required before separately authorized execution. No issue numbers are guessed.

## Phase 2 — Output and source extensions

- [ ] Phase 2 — Output and source extensions
    - [ ] Milestone 2.4 — Named-file line ranges
        - [ ] T-018 — Establish normalized logical-line selection seam
            Depends on: T-012 and current feature preparation gates.
            Scope: textstats/core.py, textstats/io.py and tests/unit semantic/acquisition checks; preserve public facade.
            Outcome: source-independent selection consumes text after one BOM normalization, preserves CRLF/CR/LF contents/terminators and EOF semantics; private complete named-file decoding can feed it without altering count_file's whole-input signature or owned-handle lifecycle (R-2/R-3).
            Evidence: pure supplied selection examples, empty/final segments/Unicode separators/interior and double BOM; whole-input API signatures/exports/silence/counts, close-on-success/failure and unchanged bytes. Strict decoding remains complete before any selection. Default CLI stays useful while no range command is exposed yet.
        - [ ] T-019 — Integrate validated named-file range text and JSON commands
            Depends on: T-018.
            Scope: textstats/cli.py and tests/unit/test_cli.py plus tests/integration module/file checks.
            Outcome: --lines spellings validate positive ASCII inclusive endpoints before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (R-1–R-3).
            Evidence: actual module supplied examples in text/JSON and both option orders, leading zeros and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
        - [ ] T-020 — Document ranges and verify extracted-source acceptance
            Depends on: T-019.
            Scope: README.md, docs/module.md, docs/api.md accuracy review and tests/integration/test_distribution.py; existing Makefile recipe.
            Outcome: runnable named-file range examples, syntax/repetition/status/complete-decode/BOM rules and explicit stdin boundary; public API docs retain whole-input contract (R-4/S-7).
            Evidence: execute public examples/help, run independent nonempty product suites, clean archive extraction and actual extracted python -m textstats for both spellings/formats/BOM policies and representative usage/read/decode failures. Remove checkout import leakage, assert extracted package identity and unchanged input. Workflow fixtures remain separate.
        - [ ] T-021 — Review, test and report range milestone 2.4
            Depends on: T-018, T-019, T-020.
            Scope: all named-file range behavior, helper/acquisition/CLI composition, API compatibility, docs/distribution and prior acceptance.
            Evidence: separate code review and focused/regression checks against all2.4 exits, useful demonstrations, required blocker repairs, TODO provenance and committed/pushed report. Reconcile issues and close2.4 only after all constituent issues are verified complete when tracking is active.
            Report: docs/dev/features/002_ea97182/2.4.md.
    - [ ] Milestone 2.5 — Range feature review
        - [ ] T-022 — Review, test and report the named-file range feature
            Depends on: feature milestone2.4 complete/closed when tracking is active, including T-021.
            Scope: cross-component R-1–R-4 and retained named-file S-1–S-5/S-7; feature-only phase/final report, not main T-017 or stdin acceptance.
            Evidence: separate feature phase code review, nonempty suites, API/default/format/BOM/decode/lifecycle regressions, runnable docs and extracted-source checks, blocker repair and final feature TODO aggregation with provenance/resolution references. Separately authorized full implementation incorporates accepted selected feature docs and reconciles task ownership/QC before final target merge and merged-state verification/publication; main Phase2 remains unfinished. No incorporation/merge/implementation during preparation.
            Reports: docs/dev/features/002_ea97182/PHASE-REPORT.md and docs/dev/features/002_ea97182/IMPLEMENTATION-REPORT.md.
