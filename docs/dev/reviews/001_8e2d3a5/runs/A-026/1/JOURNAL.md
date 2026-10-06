# A-026/1 verification journal

Verification-only authorization: named REQUEST.md; product root AGENTS.md. Product AGENTS requires pinned skills and protects credentials. No other case or harness files inspected.

## Runtime and baseline

Working directory: `/workspace/scratch/textstats-verification-worktree-20261005`
Interpreter: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`
Resolved interpreter: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3.12`
Version: `3.12.14 (main, Aug 25 2026, 14:00:49) [Clang 22.1.3 ]`
Platform: `Linux-6.18.44-x86_64-with-glibc2.39`
Environment override: PYTHONDONTWRITEBYTECODE=1. No dependency installation, configuration changes, /pyenv use, hosted access, credential discovery, clone, commit, push or source/task mutation.

## Loaded pinned skills (SHA-256)

- `sdd-orient/SKILL.md`: `91eeed3179358cb50e908a24ef83a2de9cc46dca7bf833509654b4bd04c66791`
- `sdd-orient/references/inspection-and-handoff.md`: `1df6b1c7a972959a4b6fb5820ac2a8fbefe732b6abfdef1d52c319811777502f`
- `sdd-manage/SKILL.md`: `b826b549817648a7ab0ce68f324b0d8158d4ede6b687e4034cb664306256cd3e`
- `sdd-manage/references/workflows.md`: `8ca466b140717b3cd8a33ea5fb1b9aafa8aa4fd696c8bee2455ef3edcf1912c2`
- `sdd-manage/references/coordination.md`: `71228af38e0c333ae5ac5aa671d5df5370589dc131cca4ee336f28189fd46183`
- `sdd-verify/SKILL.md`: `fe02f63973521e86fa68a5fd775d01ab41fe7a797d26d8ae59dfa05bb25152ac`
- `sdd-verify/references/execution-and-evidence.md`: `ad1dcdeca15cc67179f1923f74f044d4e6304dbf1195afff9f93dba885054a29`
- `sdd-verify/references/check-selection.md`: `27a9bcf8babe88b0d72956a2774e5e45a5cfd3316d009c955f450a2ef8fb1b34`
- `sdd-verify/references/failure-assessment.md`: `0d1297f0b6d03dfd429c9d8e0d912c841801b8207141651aca1f1a90fe9a12c6`
- `sdd-report/SKILL.md`: `481bec03eb256c70cabfc55ea7adca1626b940fa115e879f82e9de368a335a63`
- `sdd-report/references/completion-reports.md`: `1ed1bd98e8e78c0d22b049fa57843e87e4a740bd1415a7840b894493a7bffb46`

## Read-only orientation and selection

Commands inspected: `rg --files` restricted to product paths/AGENTS/skills/request; `cat` request, AGENTS, loaded skills and references, disclosure/usage/README, PROJECT/SPEC/PLAN/TASKS, milestone 1.1 report, ARCHITECTURE/DECOMPOSITION/layout and five product test modules; `sed -n 20,90p docs/dev/TASKS.md`; `command -v python`; Git commands below. Large first product read was truncated; relevant TASKS entries and layout/design were read in focused follow-up.

Ordinary product documents establish S-1/S-2 and S-3 success/S-4 success/help/validation as delivered milestone 1.1. TASKS records T-001–T-004 complete, T-005 onward incomplete. Latest five log entries agree with milestone 1.1 boundary at T-004; no pending task changes. Historical reports are context only, not fresh runtime evidence. No explicit boundary code review requested; no new full implementation code-review claim.

Command: `git --no-optional-locks status --short --branch`
Exit: 0
stdout:
```text
## trial/a026-verification
```
stderr:
```text

```

Command: `git --no-optional-locks rev-parse --show-toplevel HEAD`
Exit: 0
stdout:
```text
/workspace/scratch/textstats-verification-worktree-20261005
159c662e06405b1fbf696e8e9d9d5d47024187be
```
stderr:
```text

```

Command: `git --no-optional-locks log -5 --format=%h %s`
Exit: 0
stdout:
```text
159c662 Reconcile verified milestone 1.1 completion and pause (T-004)
fc3a0ec Clarify binary-mode review evidence for milestone 1.1 (T-004)
7bfadcb Review and report named-file MVP milestone 1.1 (T-004)
f2260a2 Deliver useful named-file module CLI (T-003)
299670c Integrate strict UTF-8 named-file API (T-002)
```
stderr:
```text

```

## Fresh authorized checks

### Check 1

Command: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -p acceptance_no_match_*.py -v`
Exit status: 5; wall duration: 0.052187s.
Interpreter resolved by python: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python` (same inherited PATH; no PATH mutation).
stdout:
```text

```
stderr:
```text

----------------------------------------------------------------------
Ran 0 tests in 0.000s

NO TESTS RAN
```

### Check 2

Command: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`
Exit status: 0; wall duration: 0.108883s.
Interpreter resolved by python: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python` (same inherited PATH; no PATH mutation).
stdout:
```text

```
stderr:
```text
test_usage_errors_and_help_never_acquire (tests.unit.test_cli.CliValidationTests.test_usage_errors_and_help_never_acquire) ... ok
test_fields_are_immutable (tests.unit.test_core.StatisticsTests.test_fields_are_immutable) ... ok
test_negative_counts_are_rejected (tests.unit.test_core.StatisticsTests.test_negative_counts_are_rejected) ... ok
test_noninteger_counts_are_rejected (tests.unit.test_core.StatisticsTests.test_noninteger_counts_are_rejected) ... ok
test_public_statistics_value (tests.unit.test_core.StatisticsTests.test_public_statistics_value) ... ok
test_zero_counts_are_valid (tests.unit.test_core.StatisticsTests.test_zero_counts_are_valid) ... ok
test_api_is_silent_and_input_unchanged (tests.unit.test_core.TextCountingTests.test_api_is_silent_and_input_unchanged) ... ok
test_count_text_is_public (tests.unit.test_core.TextCountingTests.test_count_text_is_public) ... ok
test_default_bom_policy_and_keyword_only_option (tests.unit.test_core.TextCountingTests.test_default_bom_policy_and_keyword_only_option) ... ok
test_only_one_initial_bom_is_removed (tests.unit.test_core.TextCountingTests.test_only_one_initial_bom_is_removed) ... ok
test_specification_samples (tests.unit.test_core.TextCountingTests.test_specification_samples) ... ok
test_terminator_boundaries (tests.unit.test_core.TextCountingTests.test_terminator_boundaries) ... ok
test_unicode_whitespace_is_not_a_line_terminator (tests.unit.test_core.TextCountingTests.test_unicode_whitespace_is_not_a_line_terminator) ... ok
test_success_closes_owned_handle (tests.unit.test_file_api.FileLifecycleTests.test_success_closes_owned_handle) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.004s

OK
```

### Check 3

Command: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`
Exit status: 0; wall duration: 0.612400s.
Interpreter resolved by python: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python` (same inherited PATH; no PATH mutation).
stdout:
```text

```
stderr:
```text
test_help (tests.integration.test_cli.ModuleCliTests.test_help) ... ok
test_invalid_invocations (tests.integration.test_cli.ModuleCliTests.test_invalid_invocations) ... ok
test_keep_bom_and_dash_prefixed_filename (tests.integration.test_cli.ModuleCliTests.test_keep_bom_and_dash_prefixed_filename) ... ok
test_named_files_counts_and_api_agreement (tests.integration.test_cli.ModuleCliTests.test_named_files_counts_and_api_agreement) ... ok
test_public_export_and_signature (tests.integration.test_file_api.FileApiTests.test_public_export_and_signature) ... ok
test_real_files_paths_bom_terminators_and_silence (tests.integration.test_file_api.FileApiTests.test_real_files_paths_bom_terminators_and_silence) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.538s

OK
```

## Post-check state

Command: `git --no-optional-locks status --porcelain=v1 --untracked-files=all`
Exit: 0
stdout:
```text

```
stderr:
```text

```

Command: `git --no-optional-locks rev-parse HEAD`
Exit: 0
stdout:
```text
159c662e06405b1fbf696e8e9d9d5d47024187be
```
stderr:
```text

```

