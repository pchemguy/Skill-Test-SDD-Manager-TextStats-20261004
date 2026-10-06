# Phase 2 — Output and source extensions

T-017 final phase/product review, 2026-10-06, source `82f988b43be93c54add7948ff2b5be1b82607946` on `phase/2-output-and-source-extensions`; target `main` at `59debb649545125dd3aa00377ea115451b594271`. Delivery milestones are complete and hosted closed before this review: retired historical2.1/#4, stdin2.2/#5 and named-file ranges2.4/#7; scoped range review 2.5/#8 is also closed. This is the distinct main2.3 review, not reuse of T-022 scoped review.

## Cross-component code review

Reviewed all five production modules, public interfaces, parser/source/format path, pure selection/counting, file and borrowed-stream lifecycle, product tests, public/development documentation and Makefile. Inspected the entire prospective phase difference against main, including accepted feature/archive and JSON-removal commits, for scope/coherence. It contains accepted Phase 2 product/governing/test/doc/review changes; AGENTS and pinned resources are unchanged, no trial branch or unrelated sample is included.

The pure core remains independent of filesystem/process acquisition. Statistics stay frozen/nonnegative integer values; public signatures/exports, silence and whole-input APIs are preserved. File acquisition owns strict complete UTF-8 and closes its handles; stdin dispatch owns borrowed binary EOF acquisition without locale conversion or closure. Validation completes before either acquisition. Source-independent text normalization occurs once before optional selection, with disabled slice stripping; CRLF/CR/LF contents, Unicode separators, trailing-terminator/EOF and interior/double BOM semantics remain correct. Unbounded normalized ASCII endpoint validation avoids interpreter decimal-limit conversion and clamps only beyond impossible EOF. Output is one exact text line after successful acquisition/counting; expected errors identify file or stdin with status1/empty stdout, usage errors retain2 before acquisition. Removed --json rejects; literal ./- and filenames after -- retain their meaning.

Tests use independently specified expected counts, real byte/file subprocesses and narrow failure/lifetime doubles. Archive tests clear checkout imports, assert extracted identity and exercise current text/source/range/BOM/error interfaces. Public examples/docs and module docstrings accurately distinguish CLI source selection from whole-input API behavior. No located bug, critical code issue, contract violation or missing product evidence; no repair/refactor required by phase review.

## Acceptance and fresh verification

Python 3.12.14, product root, identified source above. Fresh final-phase checks:

| Contract group | Evidence |
| --- | --- |
| S-1/S-2 public value/API/text | Immutable/nonnegative/type checks; exact exports/signatures/silence, all semantic rows, Unicode whitespace, CRLF/CR/LF/EOF and BOM rules |
| S-3 file/lifecycle | Real str/Path files, unchanged bytes, complete decoding, injected open/read/decode/close failure and owned closure |
| S-4/S-5 CLI/text/retirement | Exact stdout/stderr/status/help, usage before acquisition, dash paths/literal --json and removed-option rejection |
| S-6/S-8 sources and selection | Actual binary stdin under C locale, borrowed lifetime, both range spellings/BOM orders, ASCII/huge/repeated/rejected syntax, all supplied logical-line/BOM/EOF rows and malformed bytes beyond END |
| S-7 docs/distribution |13 executed public fences/links, separate nonempty suites, isolated archive/import identity and named-file/stdin/text/range/error invocations |

Independent commands `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` and corresponding `tests/integration` each completed:25 unit/18 integration passed, no skips. Public example execution against isolated extracted sources passed 13 fences with expected counts/statuses;1 suite fence is independently covered. Governing local links,22 unique executable task owners, all production module docstrings, absence of pending reassessment, pinned-resource/sample preservation and `git diff --check` passed. No workflow fixture supplies product acceptance.

Current design/SPEC/PLAN/layout remain the published stdin-clarification/QC state 40a1923; subsequent TASKS changes concern completion/evidence only and preserve reviewed contract/decomposition equivalence. Original named-file feature/QC observations and historical JSON reports remain retained; current S-5 retirement supersedes historical supported-JSON statements.

## Findings, TODO and limitations

No phase product finding; TODO: None. Prior milestone 2.1, feature 2.4/2.5 and stdin2.2 TODO sets are None. Historical TASK-QC-1 resolved in archived feature TASKS QC Revision1; STDIN-QC-1 resolved by governing/QC checkpoint 40a1923. T-016 trailing report whitespace was repaired by 82f988b before publication; no unresolved artifact finding.

T-013 observed RED18/GREEN3; T-014/T-015 acceptance characterizes already-delivered handling without fabricated RED; review tasks make no behavior change. Runtime execution is3.12.14, with3.11 compatibility inspected rather than executed. Complete-input memory scaling remains accepted. The successful README tarfile CLI extraction emits the recorded3.12 deprecation warning. Earlier provider aggregate lag is resolved: native 5 read back closed with 0 open and 4 closed issues after exact member13–16 completed closure. One scope-PATCH transport failure had exact unapplied readback and bounded same-adapter recovery; no unknown write, duplicate effect or transport/account bypass remains.

## Lifecycle and integration boundary

T-013/ac1acf0, T-014/93fff29, T-015/5c0b7e3 and T-016/368a0d8+82f988b are published with matching completion evidence and exact closed/completed issues#13–#16. Native milestone #5 has exact identity18309642/title and closed with 0 open and 4 closed issues membership only those four tasks. Fresh full milestone listing confirms historical4 and delivery7/scoped 8 closed; all Phase 1 milestones remain closed. Exact T-017/#17 marker/title/native 6 was freshly verified open before report persistence.

All current technical PLAN Phase 2/product exits are verified. Publish this final review/status and [implementation report](../../IMPLEMENTATION-REPORT.md), then close17 and native 6 after exact single-member/evidence readback. Persist eligible2.3/Phase 2 parent status only after those observed gates. The entire completed phase then integrates through a pinned explicit two-parent merge, fresh merged-state checks and target publication. Working-branch acceptance, hosted closure and target publication remain distinct; actual integration is recorded in the final merge evidence. Stop after published integration, retain phase branch, and start no third phase.

## Verified final tracking and parent completion

Final review/status and implementation report published at e4d8fb86d28d1fc01f2d4f3d7a4f33dc4c81f4eb. Exact issue17 closed/completed with one matching evidence comment and preserved managed body/foreign fields. Complete native 6 membership contains only17, no PR/foreign member; milestone 6/id18309655/title read back closed with 0 open and 1 closed issue after state-only closure. All preceding seven milestones are closed with zero open members. Local2.3/Phase 2 parent checkboxes now match verified acceptance and observed hosting. Explicit main integration and merged-state verification/publication follow this published boundary; their actual evidence is recorded separately.

## Verified integration result

Pinned target parent: `59debb649545125dd3aa00377ea115451b594271`; pinned completed phase parent: `6006fee487829299353525fa85afb035c155d865`. Refreshed origin/main matches the target. The complete phase difference contains accepted Phase 2 implementation, tests, governing clarification, archived feature/amendment and review/tracking evidence; pinned resources, AGENTS and the unrelated sample are unchanged. The phase tip was not already integrated. `git merge --no-ff --no-commit 6006fee487829299353525fa85afb035c155d865` merged cleanly with no conflicts, and its initial prospective tree matched the completed phase tree.

Fresh merged-state independent unit25/integration18 passed without skips, including isolated extracted-source acceptance. All13 public example fences passed expected counts/statuses and local links;1 suite fence is independently covered. Staged whitespace and sample-hash checks passed. No repair or conflict resolution was required. Only this integration evidence and the final implementation report are added to the verified phase tree in the explicit two-parent merge. The merge message records its parents/checks; ordinary main publication and exact remote containment are verified separately after commitment. Stop after that publication, retain the phase/feature/amendment branches and sample, and start no third phase.
