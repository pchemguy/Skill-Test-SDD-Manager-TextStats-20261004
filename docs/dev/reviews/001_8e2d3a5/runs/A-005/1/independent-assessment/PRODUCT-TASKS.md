# TextStats executable task hierarchy

Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-004 are implemented and verified below; the remaining tasks are planned and incomplete. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.

## Hosted tracking

Mode: maintained GitHub tracking in [pchemguy/Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004). The eligible phase 1 label, native milestones 1.1–1.3 and task issues T-001–T-009 are projected. Milestone 1.1 is verified complete and closed; milestones 1.2 and 1.3 remain open. Task issue closure follows verified durable completion. Reconcile the eligible maintained scope before execution and lifecycle transitions; hosted state never establishes completion. Phase 2 projection waits for phase 1 completion, review, verified integration into main and publication.

Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`; activation baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. The tracking checkpoint at `d009899e39790c39be32ae77e7fe8294bf60d04c` preceded implementation. The milestone 1.1 checkpoint below pauses on this branch without phase integration.

## Phase 1 — Named-file utility

- [ ] Phase 1 — Named-file utility
    - [x] Milestone 1.1 — Named-file counting MVP
        Completion evidence (2026-10-04): all T-001–T-004 results/status/report committed and published; independent unit 14/integration 6 tests, code review and normal/BOM/dash demo satisfy PLAN 1.1 exits. Issues #1–#4 verified closed with completed reason; milestone #1 read back closed with 0 open/4 closed issues. Phase 1 remains incomplete; this checkpoint pauses without integration.
        - [x] T-001 — Establish immutable statistics and pure text counting
            Scope: textstats/core.py, initial public facade, tests/unit/ discovery packages and semantic/value tests. Depends on: reviewed preparation inputs.
            Outcome: direct TextStats/count_text imports, immutable nonnegative fields and exact BOM/CRLF/CR/LF/Unicode-word semantics (S-1/S-2).
            Evidence: nonempty unit discovery; all SPEC sample rows, retained/interior/double BOM, silence and immutability/nonnegative checks. Keep pure core independent of acquisition/process state.
            Completion evidence (2026-10-04, Python 3.12.14, phase/1-named-file-utility; task-owned diff from d009899): `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` passed 12 tests with no skips. All 11 SPEC sample rows, 5 additional terminator boundaries, 7 Unicode whitespace separators, 7 BOM interactions, signature/default, silence, input preservation, frozen fields and invalid/zero counts are covered. RED observed missing TextStats export (1 failure), invalid counts (11 failing subtests), missing count_text export (1 failure), and unimplemented semantics (28 failing subtests); each became GREEN after its corresponding implementation. A separate acceptance discovery/run and direct public-import example passed; `git diff --check` was clean. Core inspection confirms only standard-library dataclass dependency and no acquisition/process behavior. Module/API docstrings reviewed; README capability statement aligned. Issue uniquely resolved as pchemguy/Skill-Test-SDD-Manager-TextStats-20261004#1 by exact title and task marker. No T-002 work, integration tests, CLI, distribution or milestone/phase review is claimed.
        - [x] T-002 — Integrate strict UTF-8 named-file API
            Scope: textstats/io.py, facade exports, focused unit/file integration checks and tests/integration/ discovery packages. Depends on: T-001.
            Outcome: count_file supports str/PathLike, preserves input terminators, delegates counts and closes its success-path owned handle (S-3 success).
            Evidence: direct package API import/signatures; real temporary files for BOM/newline/empty/Unicode cases; unchanged input; silent calls and success-handle closure. Required failure-path hardening follows in T-005.
            Completion evidence (2026-10-04): focused test-first run observed 3 missing-export assertion failures before implementation, then 3 passing tests. Independent `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` passed 13 tests; integration discovery passed 2 tests. Real str/Path files, strict binary UTF-8 acquisition, BOM/terminator/Unicode cases, exact signatures, silence, unchanged bytes and owned success closure covered. Module/API docstrings and README capability reviewed; no failure-hardening acceptance is claimed. Issue #2 exact title/body marker uniquely confirmed; diff check clean.
        - [x] T-003 — Deliver the useful named-file module CLI
            Scope: textstats/cli.py, textstats/__main__.py and integration subprocess checks. Depends on: T-001, T-002.
            Outcome: one named input, --keep-bom, -- dash filenames and help; exact text output and option validation before acquisition (S-4 success/options).
            Evidence: actual python -m textstats invocation, stdout/status/stderr assertions, API/CLI agreement, missing/extra/unknown option rejection and no input read on usage errors; demonstrate ordinary/BOM/dash filenames. Keep later JSON/stdin delivery absent from this task.
            Completion evidence (2026-10-04): focused RED observed missing command adapter and absent actual module-entry behavior (12 assertion/subtest failures across 5 tests), then GREEN passed all 5. Independent unit discovery passed 14 tests; integration passed 6, no skips. Actual subprocess checks establish exact stdout/stderr/status, ordinary/empty/Unicode/mixed-terminator/BOM cases, API agreement, --keep-bom and -- dash paths; invalid usage/help never acquire input. A separate normal/BOM/dash demonstration and README/module docstring review passed; diff check clean. Issue #3 exact title/body marker confirmed. Diagnostic hardening remains T-006; no JSON/stdin or release acceptance claimed.
        - [x] T-004 — Review, test and report milestone 1.1
            Depends on: T-001, T-002, T-003. Scope: delivered core, file API, facade and module CLI; relevant nonempty product suites and MVP demonstration.
            Evidence: actual code review, milestone exits/regressions, blocker repairs and committed/pushed report. Report: docs/dev/reports/phases/1/1.1.md. Record TODO or None and the usability decision evidence. No product completion inferred from workflow fixtures.
            Completion evidence (2026-10-04): [milestone review report](reports/phases/1/1.1.md) assesses all delivered modules and test coverage at f2260a2; no in-scope findings or TODOs. Fresh independent product discovery passed unit 14/integration 6 tests, no skips; direct normal/BOM/dash API/module demonstration and help passed, diff check clean. PLAN 1.1 exits verified; reliability/distribution and full phase acceptance remain unclaimed. Issue #4 exact title/body marker confirmed.
    - [ ] Milestone 1.2 — Reliable documented distribution
        - [ ] T-005 — Harden named-file API failure and resource behavior
            Scope: textstats/io.py and focused unit/integration failures. Depends on: T-004.
            Outcome: missing/unreadable files propagate OSError subclasses, strict bad-byte decoding raises UnicodeDecodeError, failure calls are silent, input unchanged, owned handles closed and no partial result (S-3).
            Evidence: real missing/bad-byte files plus portable injected unreadable/read/close seams; both BOM policies; byte-for-byte preservation and owned-handle success/failure checks. Do not rely solely on permission bits under privileged execution.
        - [ ] T-006 — Complete CLI diagnostics and public documentation
            Scope: textstats/cli.py, docs/api.md, docs/module.md, README.md and relevant unit/integration checks. Depends on: T-005.
            Outcome: useful input-identifying expected-error diagnostics, statuses 1/2, empty stdout/no traceback, retained help/options/success and documented runnable phase 1 API/module usage (S-4 and S-7 docs).
            Evidence: actual module missing/read/decode failures, invalid invocation before acquisition, unchanged files; run documented API/help/text/BOM examples. Preserve original README content and SDD links.
        - [ ] T-007 — Establish isolated source-distribution acceptance
            Scope: Makefile, generated-output ignore rules and tests/integration distribution checks. Depends on: T-006.
            Outcome: standard-library source archive includes importable package, README and public docs; generated dist/extractions stay untracked (S-7).
            Evidence: build/extract to temporary root; invoke extracted python -m textstats with a clean import environment from that root; check exact named-file counts, --keep-bom, help and representative failure status. Independently discover nonzero unit/integration suites and run README examples. Keep workflow fixtures separate and pinned resources unchanged.
        - [ ] T-008 — Review, test and report milestone 1.2
            Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.
            Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
    - [ ] Milestone 1.3 — Phase 1 review
        - [ ] T-009 — Review, test and report phase 1
            Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
            Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.

## Phase 2 — Output and source extensions

- [ ] Phase 2 — Output and source extensions
    - [ ] Milestone 2.1 — JSON output
        - [ ] T-010 — Add JSON rendering with preserved named-file behavior
            Scope: textstats/cli.py and unit/integration format checks. Depends on: T-009 and verified/published full phase 1 integration.
            Outcome: --json emits only integer lines/words plus newline, equal to text counts; compose --keep-bom in either order and preserve statuses/errors (S-5).
            Evidence: parse actual module output for normal/empty/BOM/terminator files, exact text default regressions, key/type checks, useful failures and stdout atomicity; demonstrate script consumption. Stdin remains scheduled in 2.2.
        - [ ] T-011 — Document and verify the JSON distribution boundary
            Scope: docs/module.md, README.md and tests/integration extracted-source checks. Depends on: T-010.
            Outcome: runnable JSON examples, accurate delivered option documentation and extracted-package text/JSON acceptance (S-7 at 2.1).
            Evidence: run examples, nonzero unit/integration discovery and tests; invoke extracted source module for both formats/BOM policies and representative failures without checkout imports.
        - [ ] T-012 — Review, test and report milestone 2.1
            Depends on: T-010, T-011. Scope: format implementation, docs/distribution and retained phase 1 contracts.
            Evidence: code review, focused/regression tests, demonstration, blocker repair and committed/pushed report with TODO provenance. Report: docs/dev/reports/phases/2/2.1.md.
    - [ ] Milestone 2.2 — UTF-8 stdin and final release
        - [ ] T-013 — Integrate borrowed binary stdin acquisition
            Scope: textstats/cli.py and source/lifecycle unit/integration checks. Depends on: T-012.
            Outcome: INPUT - reads bytes until EOF, strict UTF-8 independent of locale, never closes stdin; ./- remains a named-file path; formats/BOM policies share whole-input counting (S-6).
            Evidence: actual subprocess piped ordinary/empty/non-ASCII/BOM bytes in both formats and non-UTF-8 locale settings; instrument borrowed stream lifetime and retained named-file behavior. Keep acquisition separate from decoded-text processing for future selection compatibility.
        - [ ] T-014 — Complete stdin failure and interaction acceptance
            Scope: textstats/cli.py and focused unit/integration checks. Depends on: T-013.
            Outcome: read/decode failures identify stdin on stderr, exit 1, empty stdout, no traceback; invalid usage precedes acquisition, and complete decoded input governs all formats (S-4/S-6).
            Evidence: malformed piped bytes, injected binary read failure, never-close checks, both-order --json/--keep-bom, source/format/terminator regressions and unchanged named files. No range option is delivered here.
        - [ ] T-015 — Complete source documentation and final distribution checks
            Scope: docs/api.md, docs/module.md, README.md and tests/integration distribution checks. Depends on: T-014.
            Outcome: final runnable docs describe all delivered sources/formats, stdin UTF-8/error/lifetime rules and whole-input public API (S-7).
            Evidence: execute documented examples; build/extract clean source archive; invoke extracted module for named-file/stdin, text/JSON, empty/BOM/non-ASCII and representative failures. Independently require nonempty passing unit/integration suites; report workflow checks separately.
        - [ ] T-016 — Review, test and report milestone 2.2
            Depends on: T-013, T-014, T-015. Scope: source acquisition, decoding, interactions, docs/distribution and all retained acceptance.
            Evidence: code review, tests/regressions, piped source demonstration and diagnostics, blocker repairs, committed/pushed report and prior TODO disposition. Report: docs/dev/reports/phases/2/2.2.md.
    - [ ] Milestone 2.3 — Phase 2 and final review
        - [ ] T-017 — Review, test and report phase 2 and the complete product
            Depends on: milestones 2.1 and 2.2 complete/closed when tracking is active, including T-012/T-016. Scope: all main SPEC contracts, cross-source/format/BOM interactions and final exits.
            Evidence: phase code review, complete nonempty product suites, runnable docs, isolated extracted-source module checks, blocker repair and committed/pushed reports. Reports: docs/dev/reports/phases/2/PHASE-REPORT.md and docs/dev/reports/IMPLEMENTATION-REPORT.md. Aggregate unresolved admissible TODOs and solution/owner/provenance with resolution references; verify full-phase explicit integration, merged state and publication before claiming complete implementation.
