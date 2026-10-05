# Named-file range milestone 2.4 review

T-021, 2026-10-05. Reviewed source: feature/002_ea97182-line-ranges at 749a89844249d3b1c5ebb04c459d7e66bcb3ed2e plus accepted governing-owner reconciliation and CLI docstring-only pending changes. T-018–T-020 deliver the feature; main Phase 2/stdin remains incomplete.

## Code review

Inspected facade, core, io, cli, module entry, new selection/validation/module tests, existing API/lifecycle/default CLI tests, extracted-source test, Makefile and public documentation separately from test execution. Core normalization strips once on complete text; regex CRLF-first scanning preserves exact terminators, final segments and Unicode contents. The command compares normalized ASCII decimal strings before acquisition, rejects repeats through its argparse action, and clamps only to an impossible line past available text before safe integer conversion. This accepts endpoints beyond interpreter conversion limits without an arbitrary bound. Full strict io decoding completes before selection and closes owned handles on success/failure; count_file retains whole-input signatures and facade exports. Selected counts disable second BOM removal. Text/JSON share one result and render only after successful acquisition. Dependency direction remains cli → io/core and io → core, without core process/file state or new public API. No product bugs, contract violations or critical findings found. CLI module description was clarified to include selected counts; no behavioral repair required.

## Checks and exit evidence

On Python 3.12.14, from the product root:

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`: 21 tests passed, no skips.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`: 13 tests passed, no skips.
- `git diff --check`: passed.
- Public fenced Python and module examples ran in temporary directories with correct statuses; source build/extraction and independent product commands are verified by the product suites.
- All supplied R-4/S-8 rows, both option spellings/text/JSON/orders, leading-zero and 5000-digit endpoint success/reversal, all grammar/repetition rejection categories before acquisition, EOF/empty/trailing terminators, CRLF/CR/LF, Unicode separators, double/interior/kept BOM and malformed UTF-8 after END pass. API signatures/exports/silence/counts, unchanged bytes, owned resource closure and baseline failures/default/help/dash paths regress successfully.
- Isolated source archive verifies extracted package import identity with checkout import settings removed; actual extracted text/JSON/range/BOM/usage/read/decode paths and unchanged inputs pass.
- Useful module demonstrations: `--lines 2:3` on `alpha beta\nbeta\nlast two` gives `lines=2 words=3`; `4:99` gives `lines=0 words=0`; `2:1` exits 2 with empty stdout before acquisition. These show syntax utility, EOF intersection and useful validation for the human continuation decision.

T-018 observed helper RED (2 missing-seam assertions), then unit19/integration11 GREEN. T-019 observed 73 unknown-range-option failures, then unit21/integration13 GREEN. T-020 extended acceptance characterizes already delivered behavior without production change or a manufactured RED. Only Python 3.12.14 was executed; no Python 3.11 run is claimed. Workflow fixtures did not supply product acceptance.

## Result and lifecycle

Every PLAN 2.4 implementation/code-review/testing/documentation/distribution exit is verified. Current main governing owners incorporate accepted range scope; affected main and active feature conformance reports are Ready with exact identities and original history retained. Task IDs have exactly one executable owner in TASKS. Report/task/status publication precedes hosted issue #21 and milestone #7 closure. T-018 issue #18 closure had an initial unknown preHTTP exit2; scoped assisted same-adapter recovery succeeded and consumer readback confirms closed/completed. Issues #19/#20 closures succeed; #19's subsequent GET transport failure was resolved by independent readonly connector state inspection. No denied-write bypass or duplicate task18 comment occurred.

TODO: None. Prior feature preparation TASK-QC-1 was resolved in its retained Revision 1; no unresolved implementation finding exists. Next boundary: complete/close maintained milestone 2.4, then execute only T-022 feature review/incorporation/archive/integration into paused phase 2. No stdin or main final review work is selected.
