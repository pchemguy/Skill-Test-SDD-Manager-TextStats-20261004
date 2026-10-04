# Phase 1 — Named-file utility

T-009 phase review, 2026-10-04, Python 3.12.14. Reviewed production, tests, documentation and build source at `dec4ca107a8f0e2f878f580c88fd33303f570c01` on `phase/1-named-file-utility`, from activation baseline `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. This continues the authorized suspended workflow without replaying T-001–T-008. Delivery milestone reports: [1.1](1.1.md), [1.2](1.2.md).

## Capability and code review

Phase 1 delivers immutable statistics, silent whole-input text and strict UTF-8 named-file APIs, a useful named-file module command, atomic expected-error diagnostics, public documentation and a standard-library source distribution. Code inspection separately assessed all five production modules, all product tests, README/public guides, Makefile and ignore rules against S-1–S-4 and delivered S-7.

The pure core validates nonnegative integer results, strips exactly one initial BOM when selected, counts CRLF once before lone CR/LF normalization, preserves final-segment semantics and uses Unicode whitespace words. Facade exports and signatures are stable; acquisition and process state stay outside the core. Binary file reads preserve terminators and decode the complete input strictly. Context-managed owned handles close before result publication; read/decode/close failure propagates silently without a partial result. Real files plus injected permission/read/close seams establish portable failure/resource acceptance.

The command parser validates before acquisition and supports help, --keep-bom and -- dash paths. Only expected OSError/UnicodeDecodeError failures are translated to input-identifying stderr/status 1. Success emits one exact text line; invalid arguments retain status 2 and empty stdout. Cross-component tests compare actual module counts with the public API across BOM, Unicode and terminator inputs, and preserve bytes on success/failure.

Public docs distinguish delivered named-file behavior from planned JSON/stdin. Runnable examples match signatures, statuses and lifetime. Distribution explicitly includes package, public/development docs and product tests while excluding workflow resources/caches/generated outputs. Isolated extraction clears checkout import variables, disables user site, asserts extracted module identity and exercises successful/error commands. The documented proportional-memory tradeoff is retained; no new performance guarantee or future range capability is claimed.

## Findings and provenance

No product finding or required repair. Both prior milestone TODO sets are empty; no unresolved finding is carried forward. T-005 characterized already-correct lifecycle behavior without manufactured RED. T-006 and T-007 retain their recorded RED/GREEN evidence. The T-007 example-runner corrections and premature evidence correction remain explicitly documented in milestone 1.2. T-009 changes only review/status records, so no behavioral RED cycle applies.

## Verification and exit assessment

Fresh checks at the reviewed state, with PYTHONDONTWRITEBYTECODE=1:

| Check | Result and coverage |
| --- | --- |
| python -m unittest discover -s tests/unit -t . -v | 17 pass, no skips; values, line/word/BOM semantics, silent APIs, owned failure lifecycle, validation before acquisition and atomic diagnostics |
| python -m unittest discover -s tests/integration -t . -v | 9 pass, no skips; real API/files, actual module exact output/status, unchanged bytes, help/options/BOM/dash/errors, isolated extracted package |
| README/API/module Python examples and local links | Pass; direct public imports/assertions, Path input, preserved bytes and all local links |
| Normal/BOM/keep-BOM/dash/help/missing/malformed demonstration | Pass; exact counts, statuses, empty failure stdout, identifying stderr, no traceback and unchanged input |
| Fresh source build/extraction/import identity/module invocation | Pass from temporary extraction with clean import environment; exact lines=2 words=3 plus newline and empty stderr |
| git diff --check | Pass |

All PLAN Phase 1 review exits are established: coherent S-1–S-4 and delivered S-7, cross-component regressions, runnable documentation, independent nonzero suites, isolated source distribution, code review, milestone finding disposition and this report. Preparation contracts/design/layout are unchanged; completion/evidence metadata does not invalidate their reviewed conformance. Python 3.11 compatibility is inspected, while actual execution used Python 3.12.14. No workflow suite supplied product acceptance. No full-product/final implementation report is due because Phase 2 remains incomplete.

## Hosting and integration boundary

Before this review, connector/API readback confirmed exact task IDs/markers for #1–#8 closed/completed and milestones #1/#2 closed with zero open/four closed issues each. T-009 uniquely resolves to [issue #9](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9), with exact title/marker and milestone #3. Publish this report/status result, then close #9 with evidence and read back milestone #3 closure before final parent reconciliation. Explicit two-parent integration into main requires the complete phase difference, merged-state checks and normal target push/readback. These effects are separate from this task's review acceptance and are recorded when actually performed.

## TODO

None.

## Stop

Finish only Phase 1 completion, hosting reconciliation, verified integration and publication. Stop before Phase 2 activation, projection or execution. Retain the phase branch and all prior work.

## Completed tracking reconciliation

T-009 report/status committed at `cb9d56ab4060483cd2240cb9553f43f850196968` and published to the retained phase branch, with exact remote tip confirmation. [Evidence comment](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9#issuecomment-5983966503) records commit/check/report evidence. Issue #9 read back closed/completed. The complete milestone #3 issue listing contains only #9; milestone #3 then read back closed with zero open/one closed issue. Milestones #1/#2 and their eight issues remain closed. Local Phase 1 and 1.3 parent status now matches verified acceptance and observed tracking. Integration and main publication follow this checkpoint; Phase 2 remains unprojected and unimplemented.

## Verified integration result

Pinned target parent: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`; pinned phase parent: `b398e258cefc03dbc47630b83967db961a376eae`. Refreshed origin/main matches the target; the full phase difference contains only accepted Phase 1 implementation/tests/docs/build and tracking/review evidence. Governing contracts and pinned resources are unchanged. The phase tip was not already integrated. `git merge --no-ff --no-commit b398e258cefc03dbc47630b83967db961a376eae` merged cleanly with no conflicts. Fresh merged-state independent unit17/integration9 passed with no skips, including isolated distribution; staged whitespace check passed. No repair or conflict resolution was required. This report is included in the explicit two-parent merge; its commit message records the same parents/checks. Normal main publication and exact remote containment are verified separately after the merge commit, with no Phase 2 work.
