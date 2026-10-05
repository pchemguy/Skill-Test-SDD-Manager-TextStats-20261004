# JSON removal impact assessment

Assessment completed on 2026-10-05 against /workspace/scratch/textstats-live-20261004 at 0e4741465c3e086d2ab95c5af73ca89371c16fac, branch phase/2-output-and-source-extensions. Main remains 59debb649545125dd3aa00377ea115451b594271. This is an inspection assessment, not an implemented or verified amendment.

## Scope and authority

The selected REQUEST.md asks to assess removing JSON while retaining text output, counting, BOM policy and named-file line selection. Its explicit assessment-only boundary governs over broader campaign continuation. Pinned sdd-manage/references/revision-authorization.md was successfully read before authority decisions; its scoped effects retain explicit human limits. Pinned sdd-manage, sdd-orient, sdd-steer/objective-and-impact and sdd-report informed this assessment. No branch, product edit, commit, test run, task execution, hosted lookup/write, publication or integration was performed. Only JOURNAL.md and this result are outputs.

Applicable product AGENTS.md requires pinned workflows. PROJECT describes standard-library Python 3.11+, unittest, silent APIs and preserved inputs/resources. Root adoption/disclosure records are present. Current governing roots and their adjacent QC reports incorporate ranges; archived feature002_ea97182 sources are historical, and TASKS is the sole executable owner. Local Git shows no tracked/index difference and only the unrelated untracked sample.

## Assessment

Removing JSON is a narrow CLI format reduction with a wider acceptance/documentation impact. In textstats/cli.py, JSON consists of the json import, --json parser registration and final args.json/json.dumps branch. Both current formats receive the same TextStats after acquisition/counting. The pure core, named-file I/O, public facade and module entry need no behavioral redesign for the stated objective.

A future amendment should remove JSON serialization and the option/help contract, then emit the retained exact text result unconditionally. Existing scripts that invoke --json or parse its output would break; documented JSON pipelines would no longer be supported. Proposed compatibility treatment is normal unknown-option status2 before acquisition, empty stdout and useful stderr, including combinations with --keep-bom or --lines. A filename literally --json must remain addressable after --; dash-prefixed paths remain files, not cleanup targets. This compatibility behavior is proposed, not observed after a change.

## Retained contracts

| Contract | Required retained behavior |
| --- | --- |
| S-1 API/value | Same direct exports TextStats/count_text/count_file; immutable nonnegative integer counts, boolean/type rejection as implemented; whole-input signatures/defaults; silence and input preservation; no public range API. |
| S-2 counting/BOM | CRLF is one terminator, lone CR/LF terminate, final nonempty segment adds a line, no phantom trailing line, empty gives zero, other Unicode separators remain contents; words use str.split Unicode whitespace. Strip exactly one initial U+FEFF by default; preserve second/interior BOMs and all BOMs with keep/False. |
| S-3 named files | Complete binary acquisition and strict UTF-8 without newline translation; str/PathLike API paths; owned handles close on success/failure; OSError/UnicodeDecodeError API behavior and silent failure; bytes unchanged. |
| S-4 text CLI | Exactly lines=<N> words=<N> plus newline, status0 and empty stderr; one INPUT, --keep-bom, -- dash filenames, help0; usage2 before acquisition; expected read/decode failures1 identify input, empty stdout, no traceback. Whole-input default remains. |
| S-8 line selection | Both --lines START:END and --lines=START:END; inclusive one-based positive ASCII decimals, leading zeros, unbounded endpoints, ordered bounds; malformed/missing/repeated ranges rejected before acquisition. Complete decode before selection, including bad bytes after END. One BOM normalization before numbering; selected contents and CRLF/CR/LF terminators preserved; no second BOM stripping at an exposed interior BOM; EOF intersection/empty cases unchanged. --lines and --keep-bom compose before --. |
| S-7 delivery | Runnable retained examples/help/status/docs, separate nonempty unit/integration acceptance, isolated extracted-source import identity and module checks, unchanged archive boundary and standard-library dependencies. |
| Pending S-6 | Stdin remains unimplemented. Preserve intended binary until-EOF strict UTF-8 independent of locale, never-close borrowed stdin, text/BOM behavior, empty/error handling, literal ./- file, no stdin ranges. No stdin or final phase completion is inferred. |

## Affected files and dependencies

| Area | Proposed amendment impact |
| --- | --- |
| textstats/cli.py | Remove JSON import/parser/render branch; align main docstring. Preserve validation/acquisition/range/error order and exact text renderer. |
| tests/unit/test_cli.py | JSON is mixed into usage and file-error matrices. Reclassify removed-option calls as no-acquisition usage rejection; retain text/keep-BOM error tests. Do not merely delete shared error coverage. |
| tests/integration/test_cli.py | JsonModuleTests asserts delivered JSON counts/types/orders/atomicity. Replace JSON acceptance with removed-option rejection, preserving ordinary/empty/terminator/Unicode/BOM/dash/input-unchanged/text/error coverage in remaining scenarios. |
| tests/integration/test_ranges.py | Format and option-order loops include JSON; keep every semantic range row, both spellings, huge endpoints, EOF, malformed/repeated values, late invalid UTF-8 and dash paths in text. Convert JSON-dependent retained-BOM selection checks to exact text, add removed-option/range no-acquisition coverage. |
| tests/integration/test_distribution.py | JSON decoding loops/help assertions and JSON-only range-BOM/late-decode/error scenarios require focused text replacements; retain isolated package identity, extraction, text/BOM/ranges/help/errors and unchanged bytes. No Makefile recipe change is intrinsically needed. |
| tests/unit/test_ranges.py, core/file API tests | Existing pure selection, normalization, value/API, complete decode and lifecycle tests remain relevant unchanged. Retain rather than removing them with format tests. |
| README.md, docs/module.md | Remove JSON availability, syntax, examples/pipelines, two-format wording and order claims; retain text/BOM/range examples, whole-file API, statuses, strict complete decode, no stdin delivery and test/distribution instructions. |
| docs/api.md | Whole-input public API has no JSON surface; accuracy review is sufficient unless links/descriptions change. |
| PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC | Reconcile JSON delivery/serializer/two-format language. Retire S-5 JSON explicitly without silently renumbering S-6–S-8. Update affected S-4/S-6/S-7/S-8 and acceptance boundaries; keep counting/acquisition/selection owners and source-independent seams. |
| PLAN, TASKS and adjacent QC | Reconcile live format scopes and future exits/dependencies; recheck changed governing identities/affected conformance. Do not reuse current Ready reports as evidence for amended inputs. |
| Historical feature and milestone reports | Preserve original JSON implementation/review provenance and archived feature sources as historical. Add scope-aware amendment disposition in current owners/reports; do not rewrite original tests/results as if JSON never existed. |
| Hosted tracking | Existing JSON and range issue/milestone descriptions may need scoped later reconciliation after implementation authorization. No provider state was queried or changed here; local report references are not fresh hosted evidence. |

Completed T-010–T-012 and milestone2.1 are specifically JSON delivery/docs/review history. They should retain stable identities and historical evidence while the future amended current scope receives explicit retirement/reassessment disposition. Completed T-019–T-022 and earlier broad review/parent claims include format-dependent acceptance; their retained text/range portions need scope-aware reassessment before claiming current amendment acceptance. Reassess the affected S-4/S-7/S-8 and historical S-5 claims without marking unaffected core counting work incomplete by default.

Pending T-013–T-015 currently require both formats/JSON composition or extracted text/JSON source acceptance. T-016/T-017 inherit those release obligations. Proposed future changes must make these text-only while retaining stdin lifetime/strict-decode/BOM/errors and named-file ranges. Dependencies referencing T-012, milestones2.1/2.4 and completed range tasks need explicit historical-baseline treatment, not deletion/renumbering or inferred completion. T-013–T-017 remain unchecked; Phase2 remains incomplete.

## Expected future evidence

If removal is separately commanded, demonstrate absence of --json in help and normal usage rejection with no acquisition, including BOM/range combinations; test dash-file access through --. Demonstrate exact text default for ordinary/empty/Unicode/terminator/BOM cases, retained selected-line rows and endpoint validation, complete late decode failure, unchanged APIs/files and owned-handle closure. Re-run meaningful independent nonempty product unit/integration checks and isolated extracted-source retained contract checks, then execute revised public examples. This is a future evidence proposal only; no tests or demonstrations were executed in this assessment and no amended runtime result is claimed.

## Evidence limitations and exact stopping state

Read-only command/source/test/document inspection supports structural impact and contract mapping, not empirical proof of a hypothetical removal. Existing unit21/integration13 and previous JSON counts in TASKS/QC are historical product records, not new verification. One initial missing-path read failed. A subsequent filename search accidentally ranged across /workspace/scratch and exposed other evidence filenames; no contents of those files were read or used. All later content inspection was confined to the permitted REQUEST and product authorities/code/tests/docs. The journal records that deviation and returned native command results, including truncation notices where the command tool limited large outputs.

Stopped after assessment with branch phase/2-output-and-source-extensions and HEAD 0e4741465c3e086d2ab95c5af73ca89371c16fac unchanged. Main is 59debb649545125dd3aa00377ea115451b594271 unchanged. Final tracked/index diff names are empty. Untracked -json-9l969okj/sample.txt remains SHA256 f1945cd6c19e56b3c1c78943ef5ec18116907a4ca1efc40a57d48ab1db7adfc5. JSON remains implemented; ranges remain implemented; stdin/final phase tasks remain pending. No amendment branch or product report was created; no execution continuation, hosted action, publication or integration occurred.

