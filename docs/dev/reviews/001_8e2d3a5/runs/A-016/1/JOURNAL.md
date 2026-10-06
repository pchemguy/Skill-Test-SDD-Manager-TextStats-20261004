# A-016 / 1 consumer journal

## Controlled suspension

User requested controlled suspension through coordinator after the push remained held. No retry, release, new task, tests, credentials or tooling change followed. Cancelled only native push session 51170 through its own supported write_stdin with Ctrl-C. Actual completion: exit 130, output empty. Local verified task commit a3e6ab199e06892bf53944ca96ccd26063e87bd8 retained; index/worktree last observed clean. Last remote readback remained d009899e39790c39be32ae77e7fe8294bf60d04c. Pending exact publication is `git push /workspace/scratch/textstats-unpublished-remote-20261005.git HEAD:refs/heads/trial/a016-publication-recovery`, using required PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH. No post-cancel readback/test/mutation performed. Therefore publication is not verified, effects after last readback remain unobserved; retain commit and pending operation. Stop before T-002.

```text
$ write_stdin(session_id=51170, chars=Ctrl-C)
exit_code=130
output=(empty)
```


Scope: actual REQUEST.md, T-001 only, stop before T-002. Product worktree /workspace/scratch/textstats-unpublished-worktree-20261005. Explicit branch trial/a016-publication-recovery and literal remote /workspace/scratch/textstats-unpublished-remote-20261005.git. Git commands use required PATH tooling. No platform rejection was observed. Hosted maintenance inactive by request; historical tracking metadata retained.

Initial actual read-only commands: cat REQUEST.md; rg --files product AGENTS/documents/pinned skills; cat AGENTS.md SDD-MANAGER.md and pinned skill/reference files; git --no-optional-locks status --short (clean), log -4 --oneline (HEAD d009899, prior reviewed preparation), branch --show-current (trial/a016-publication-recovery); git --no-optional-locks ls-remote literal URL refs/heads/trial/a016-publication-recovery (d009899e39790c39be32ae77e7fe8294bf60d04c). All returned exit 0. Startup remote already equals local baseline so no ceremonial push. Read current SPEC/PROJECT/design/PLAN/layout/QC reports, compared hashes to reports: exact matching inputs including TASKS revision 1 1622d35a0bb4a61034e2b92fa52ed986f99cb54c96b49ff4087155af308df208. No source/test modules existed. Bootstrap notices and README links retained, truthful existing attribution inspected.

Pinned workflow source identified by request as 019eb354cf0921ebd6056e6579763ac33d0baec2. Applied pinned sdd-orient, sdd-implement, revision-authorization, document QC, TDD, docs, verification and report references. Initial aggregate read output was truncated; relevant sections reread. Skill hashes below include source identities; hashing does not claim execution of unselected workflows.

TDD sequence: first public existence assertion RED (1 test, exit 1, assertion failure, no import/collection failure). Add interface scaffolding (mutable dataclass, count_text returns zero) and run 1 test GREEN. Write semantic/value tests before relevant behavior; RED 10 collected tests, 31 failed subcases, exit 1, no import/collection errors. Then implement frozen validated value and true line/word semantics. 10 tests GREEN; independent boundary campaign reruns 10 tests, independent collection = 10, README examples/docstrings/signature pass. No test-first exception. Integration/distribution/CLI checks remain scheduled beyond T-001 and not claimed.

## Actual commands and raw results

```text
$ python --version; cat README.md AI_DISCLOSURE.md textstats-run-resources/plugin/skills/sdd-report/references/completion-reports.md
exit_code=0 session_id=none
Python 3.12.14
# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats is in preparation; production code is not yet implemented. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
# AI-Assisted Development Disclosure

This project has been developed with extensive assistance from generative AI, primarily OpenAI ChatGPT. AI assistance was used throughout both code and documentation development, including project exploration, design discussion, specification development, implementation, test generation, technical review, and prose drafting and revision.

The project has been developed under human direction, and responsibility for the published code, documentation, design decisions, and any remaining errors rests with the project maintainer. Users should review and validate the implementation for their own requirements, particularly before relying on it in production or other correctness-sensitive applications.

## README.md Warning Template

> [!IMPORTANT]
> 
> **AI-Assisted Development Disclosure**
> 
> This project has been developed with extensive generative-AI assistance. Assistance covered project exploration, design discussion, specification development, implementation, testing, technical review, and documentation. See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for further details. Responsibility for the published software remains with the maintainer.
# Completion and status reports

Use the requested boundary from the owning TASKS or FEATURE-TASKS list. A checked box is a claim to compare with actual artifacts, verification output, and Git commits. Inspect the current implementation and relevant acceptance or exit conditions; distinguish task commits, working-branch acceptance, integration into the established target, target publication, and hosted issue state. The target need not be the default branch.

## Task

State task ID, outcome, status, and an implemented-feature summary. Then give the change and reason, files or components affected at a useful level, exact checks and outcomes, commit SHA or pending commit, and resolved issue URL or pending hosted reconciliation if applicable. Describe omissions and unverified conditions plainly. Report **completed** only when task-specific acceptance, documentation and tests, required verification, durable commit, and task-list status are reconciled. An issue closed by the host is not proof.

## Milestone and phase

Summarize the actual capabilities delivered across constituent tasks, rather than a list of checkboxes. Name task IDs and relevant commits, aggregate verification and integration evidence, the PLAN or FEATURE-PLAN exit conditions checked, unresolved defects, and the next stopping boundary. In FEATURE-TASKS, a checked parent covers only that feature's listed work and exits; it does not assert completion of the whole-project parent in TASKS. If some tasks or exits remain, report **partial** or **blocked** with the specific cause.

## Review reports and TODO aggregation

Use the [backend object lifecycle](../../sdd-conventions/references/backend-object-lifecycle.md) for report placement and deferral rules. Main phase reports use `docs/dev/reports/phases/<phase-id>/PHASE-REPORT.md`; milestone reports share that directory as `<milestone-id>.md`. Steering records use its nested `revisions/<revision-id>/`; feature reports remain under their feature directory. Link from the owning review task; draft reports before its commit, without requiring the report to contain its own commit SHA.

For a milestone/phase review report, state stable identity, actual reviewed source, delivered capability, implementation code review coverage and findings, commands/outcomes and limits, repairs/commits, exit assessment, TODO and next boundary. Distinguish inspection from test execution. Include fixed findings and rechecks. An unresolved required check, bug, critical issue or contract violation blocks completion; the report does not waive that blocker. Execution owns report persistence and completion decisions.

Put required repairs and findings of unestablished deferral eligibility in Findings/Blockers, not the deferred TODO. Write `TODO: None` when empty. For each admissible deferred non-critical item include stable finding ID, location/evidence, impact/severity, contract-preserving deferral rationale, proposed solution options/tradeoffs and follow-up owner/scope. Phase reports retain unresolved milestone findings and add phase findings, preserving IDs/provenance. When the full owning task list completes, draft its final IMPLEMENTATION-REPORT.md aggregating unresolved/deferred items and solution options, deduplicated by ID, with references to resolved findings. The final phase review task includes this report; a partial range produces no full-list completion claim. Do not create a second progress journal.

## Interrupted or limited evidence

For an interrupted task or unavailable check, state the last trusted Git state, observed dirty or staged work, checks completed and not completed, and the exact blocker. Do not infer that a half-written commit or test log finished the task. **sdd-orient** identifies interrupted task state, **sdd-manage** coordinates scope, and **sdd-implement** owns continuation; this skill summarizes their evidence. If a performance result is statistically inconclusive, a security fix has only partial regression coverage, or a test run excludes a required suite, make that limit visible in the result.

Use the kind-specific sections in [change kinds](change-kinds.md) where they materially explain the outcome. Keep source attribution near claims: task and document sections for intended behavior; command/output and commits for observed behavior. Do not create a second progress journal or alter TASKS while drafting a report.

## Evidence and test-first limits

Carry task/change identity, tested state, actual commands/outcomes, condition coverage, and material limitations from the verification handoff. Name the designated or owning-entry evidence location; taskless maintenance may use its ordinary report/commit body. Include any authorized test-first exception with its concrete rationale, applicable policy or user authorization, observed alternative evidence, and remaining gaps. Missing RED history remains missing; a sensitivity check or characterization run is not proof of an earlier test-first cycle. Do not add a separate mandatory evidence format.

## Branch boundary

Include the campaign/phase identity and retained directory where applicable. A completed task range in an incomplete main phase is a pushed checkpoint, not a completed integration; report phase work/exits remaining and the paused branch. Report eligible feature archive paths and main task owners, without treating historical lists as executable.

Report working and target branches, starting checkpoint, task or amendment commits, merge SHA and parent tips, working-branch and merged-state verification, and remote containment or pending publication. Distinguish a verified task from a completed integrated workflow. A failed merge or target push remains an explicit blocker even when task commits are verified and pushed. Identify already integrated work without claiming a new merge, and state when an explicit user instruction retained work on its branch.

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
exit_code=1 session_id=none
test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports) ... FAIL

======================================================================
FAIL: test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_public.py", line 10, in test_direct_imports
    self.assertIsNotNone(importlib.util.find_spec("textstats"))
AssertionError: unexpectedly None

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
exit_code=0 session_id=none
test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.002s

OK

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
exit_code=1 session_id=none
test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) ... 
  test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) (field='lines') ... FAIL
  test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) (field='words') ... FAIL
test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) ... 
  test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=-1, words=0) ... FAIL
  test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=0, words=-1) ... FAIL
  test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=-1, words=-1) ... FAIL
test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) ... 
  test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=1.5, words=0) ... FAIL
  test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=0, words='2') ... FAIL
  test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=None, words=0) ... FAIL
test_zero_and_positive_values (tests.unit.test_core.StatisticsValueTests.test_zero_and_positive_values) ... ok
test_keyword_only_bom_policy_and_default (tests.unit.test_core.TextCountingTests.test_keyword_only_bom_policy_and_default) ... ok
test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) ... 
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r\n') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r\n\r\n') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\rb') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\n\r') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\r\nb') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\x0b b\x0c c\x85d\u2029e') ... FAIL
  test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\xa0b\u2003c') ... FAIL
test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) ... 
  test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff alpha', strip=True) ... FAIL
  test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff alpha', strip=False) ... FAIL
  test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='alpha \ufeff beta', strip=True) ... FAIL
  test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff\ufeff alpha', strip=True) ... FAIL
  test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff\ufeff alpha', strip=False) ... FAIL
test_silent_and_input_unchanged (tests.unit.test_core.TextCountingTests.test_silent_and_input_unchanged) ... FAIL
test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) ... 
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha beta', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\n', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\n', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\r\nbeta\rgamma\n', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\n\n', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text=' \t', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\u2028beta', strip_bom=True) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\ufeff', strip_bom=False) ... FAIL
  test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\ufeff\ufeff', strip_bom=True) ... FAIL
test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports) ... ok

======================================================================
FAIL: test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) (field='lines')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 74, in test_fields_are_immutable
    with self.subTest(field=name), self.assertRaises(FrozenInstanceError):
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: FrozenInstanceError not raised

======================================================================
FAIL: test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) (field='words')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 74, in test_fields_are_immutable
    with self.subTest(field=name), self.assertRaises(FrozenInstanceError):
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: FrozenInstanceError not raised

======================================================================
FAIL: test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=-1, words=0)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 79, in test_rejects_negative_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(ValueError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

======================================================================
FAIL: test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=0, words=-1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 79, in test_rejects_negative_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(ValueError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

======================================================================
FAIL: test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) (lines=-1, words=-1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 79, in test_rejects_negative_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(ValueError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: ValueError not raised

======================================================================
FAIL: test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=1.5, words=0)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 84, in test_requires_integer_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(TypeError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: TypeError not raised

======================================================================
FAIL: test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=0, words='2')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 84, in test_requires_integer_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(TypeError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: TypeError not raised

======================================================================
FAIL: test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) (lines=None, words=0)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 84, in test_requires_integer_fields
    with self.subTest(lines=lines, words=words), self.assertRaises(TypeError):
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: TypeError not raised

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r\n')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=0)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=0)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\r\n\r\n')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=0)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\rb')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=2)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='\n\r')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=0)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\r\nb')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=2)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\x0b b\x0c c\x85d\u2029e')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=5)

======================================================================
FAIL: test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) (text='a\xa0b\u2003c')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 51, in test_only_cr_lf_terminate_lines
    self.assertEqual(count_text(text), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=3)

======================================================================
FAIL: test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff alpha', strip=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 40, in test_retained_interior_and_double_bom
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=1)

======================================================================
FAIL: test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff alpha', strip=False)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 40, in test_retained_interior_and_double_bom
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=2)

======================================================================
FAIL: test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='alpha \ufeff beta', strip=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 40, in test_retained_interior_and_double_bom
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=3)

======================================================================
FAIL: test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff\ufeff alpha', strip=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 40, in test_retained_interior_and_double_bom
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=2)

======================================================================
FAIL: test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) (text='\ufeff\ufeff alpha', strip=False)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 40, in test_retained_interior_and_double_bom
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=2)

======================================================================
FAIL: test_silent_and_input_unchanged (tests.unit.test_core.TextCountingTests.test_silent_and_input_unchanged)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 58, in test_silent_and_input_unchanged
    self.assertEqual(count_text(text), TextStats(2, 2))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=2)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha beta', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=2)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\n', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=1)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\n', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=0)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\r\nbeta\rgamma\n', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=3, words=3)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\n\n', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=2, words=1)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text=' \t', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=0)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='alpha\u2028beta', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=2)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\ufeff', strip_bom=False)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=1)

======================================================================
FAIL: test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) (text='\ufeff\ufeff', strip_bom=True)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py", line 29, in test_spec_sample_rows
    self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
AssertionError: TextStats(lines=0, words=0) != TextStats(lines=1, words=1)

----------------------------------------------------------------------
Ran 10 tests in 0.006s

FAILED (failures=31)

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
exit_code=0 session_id=none
test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) ... ok
test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) ... ok
test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) ... ok
test_zero_and_positive_values (tests.unit.test_core.StatisticsValueTests.test_zero_and_positive_values) ... ok
test_keyword_only_bom_policy_and_default (tests.unit.test_core.TextCountingTests.test_keyword_only_bom_policy_and_default) ... ok
test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) ... ok
test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) ... ok
test_silent_and_input_unchanged (tests.unit.test_core.TextCountingTests.test_silent_and_input_unchanged) ... ok
test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) ... ok
test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
exit_code=0 session_id=none
test_fields_are_immutable (tests.unit.test_core.StatisticsValueTests.test_fields_are_immutable) ... ok
test_rejects_negative_fields (tests.unit.test_core.StatisticsValueTests.test_rejects_negative_fields) ... ok
test_requires_integer_fields (tests.unit.test_core.StatisticsValueTests.test_requires_integer_fields) ... ok
test_zero_and_positive_values (tests.unit.test_core.StatisticsValueTests.test_zero_and_positive_values) ... ok
test_keyword_only_bom_policy_and_default (tests.unit.test_core.TextCountingTests.test_keyword_only_bom_policy_and_default) ... ok
test_only_cr_lf_terminate_lines (tests.unit.test_core.TextCountingTests.test_only_cr_lf_terminate_lines) ... ok
test_retained_interior_and_double_bom (tests.unit.test_core.TextCountingTests.test_retained_interior_and_double_bom) ... ok
test_silent_and_input_unchanged (tests.unit.test_core.TextCountingTests.test_silent_and_input_unchanged) ... ok
test_spec_sample_rows (tests.unit.test_core.TextCountingTests.test_spec_sample_rows) ... ok
test_direct_imports (tests.unit.test_public.PublicAPITests.test_direct_imports) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

```

```text
$ PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
import ast
import inspect
import unittest
from pathlib import Path
from textstats import TextStats, count_text
suite = unittest.defaultTestLoader.discover('tests/unit', top_level_dir='.')
assert suite.countTestCases() == 10
print('Independent product collection:', suite.countTestCases())
assert count_text('alpha beta\n').lines == 1
assert count_text('alpha beta\n').words == 2
print('README examples: passed')
for path in [Path('textstats/core.py'), Path('textstats/__init__.py')]:
    tree = ast.parse(path.read_text())
    assert ast.get_docstring(tree)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            assert ast.get_docstring(node)
    print('Module/API docstrings:', path)
print('Public signature:', inspect.signature(count_text))
PY
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff --check
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks status --short
exit_code=0 session_id=none
Independent product collection: 10
README examples: passed
Module/API docstrings: textstats/core.py
Module/API docstrings: textstats/__init__.py
Public signature: (text: str, *, strip_bom: bool = True) -> textstats.core.TextStats
 M README.md
?? tests/
?? textstats/

```

```text
$ python - <<'PY'
from pathlib import Path
p = Path('docs/dev/TASKS.md')
s = p.read_text()
s = s.replace('These are planned tasks: none is implemented, verified or complete.', 'T-001 is verified locally; subsequent tasks remain planned and unchecked.')
s = s.replace('- [ ] T-001 —', '- [x] T-001 —', 1)
needle = '            Evidence: nonempty unit discovery; all SPEC sample rows, retained/interior/double BOM, silence and immutability/nonnegative checks. Keep pure core independent of acquisition/process state.'
s = s.replace(needle, needle + '\n            Verified 2026-10-05 on authorized trial/a016-publication-recovery: Python 3.12.14; PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v passed 10 tests, independently collected 10. Public-interface RED collected 1 test and failed (exit 1); subsequent semantic/value RED collected 10 tests and failed 31 subcases (exit 1), without collection errors. All S-2 table rows, BOM policies/interior/double BOM, CRLF/CR/LF, other Unicode whitespace/separators, silent unchanged-text processing, keyword-only signature, immutable/nonnegative integer fields verified. Module/API docstrings and README examples checked; git diff --check passed. Hosted tracking inactive for this authorized range; literal local remote publication only. Scope stops before T-002; phase/milestone remain incomplete, no integration.')
p.write_text(s)
PY
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff --check
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff -- README.md docs/dev/TASKS.md
cat textstats/core.py textstats/__init__.py tests/unit/test_public.py
exit_code=0 session_id=none
diff --git a/README.md b/README.md
index 81c1c6c..a818ca0 100644
--- a/README.md
+++ b/README.md
@@ -4,4 +4,13 @@ SDD Manager TextStats testing
 
 Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).
 
-TextStats is in preparation; production code is not yet implemented. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
+TextStats currently provides the pure Python API `TextStats` and `count_text` for immutable line and word counts. Named-file and CLI support remain planned. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
+
+```python
+from textstats import count_text
+
+assert count_text("alpha beta\n").lines == 1
+assert count_text("alpha beta\n").words == 2
+```
+
+Requires Python 3.11+. Run the current unit suite with `python -m unittest discover -s tests/unit -t .`.
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index fb13cdd..10eb6be 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,6 +1,6 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. These are planned tasks: none is implemented, verified or complete. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001 is verified locally; subsequent tasks remain planned and unchecked. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
 
 ## Hosted tracking
 
@@ -12,10 +12,11 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
 
 - [ ] Phase 1 — Named-file utility
     - [ ] Milestone 1.1 — Named-file counting MVP
-        - [ ] T-001 — Establish immutable statistics and pure text counting
+        - [x] T-001 — Establish immutable statistics and pure text counting
             Scope: textstats/core.py, initial public facade, tests/unit/ discovery packages and semantic/value tests. Depends on: reviewed preparation inputs.
             Outcome: direct TextStats/count_text imports, immutable nonnegative fields and exact BOM/CRLF/CR/LF/Unicode-word semantics (S-1/S-2).
             Evidence: nonempty unit discovery; all SPEC sample rows, retained/interior/double BOM, silence and immutability/nonnegative checks. Keep pure core independent of acquisition/process state.
+            Verified 2026-10-05 on authorized trial/a016-publication-recovery: Python 3.12.14; PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v passed 10 tests, independently collected 10. Public-interface RED collected 1 test and failed (exit 1); subsequent semantic/value RED collected 10 tests and failed 31 subcases (exit 1), without collection errors. All S-2 table rows, BOM policies/interior/double BOM, CRLF/CR/LF, other Unicode whitespace/separators, silent unchanged-text processing, keyword-only signature, immutable/nonnegative integer fields verified. Module/API docstrings and README examples checked; git diff --check passed. Hosted tracking inactive for this authorized range; literal local remote publication only. Scope stops before T-002; phase/milestone remain incomplete, no integration.
         - [ ] T-002 — Integrate strict UTF-8 named-file API
             Scope: textstats/io.py, facade exports, focused unit/file integration checks and tests/integration/ discovery packages. Depends on: T-001.
             Outcome: count_file supports str/PathLike, preserves input terminators, delegates counts and closes its success-path owned handle (S-3 success).
"""Pure statistics value and decoded-text counting."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TextStats:
    """Immutable nonnegative integer counts of lines and words.

    Args:
        lines: Number of logical lines.
        words: Number of Unicode-whitespace-separated words.

    Raises:
        TypeError: A field is not an integer.
        ValueError: A field is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        if not isinstance(self.lines, int) or not isinstance(self.words, int):
            raise TypeError("lines and words must be integers")
        if self.lines < 0 or self.words < 0:
            raise ValueError("lines and words must be nonnegative")


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Count CRLF/CR/LF logical lines and Unicode-whitespace words silently.

    Args:
        text: Decoded input, left unchanged.
        strip_bom: Remove exactly one leading U+FEFF when true. Interior
            and subsequent BOMs are ordinary non-whitespace characters.

    Returns:
        Immutable counts. Empty input has zero lines; a nonempty final
        unterminated segment adds one line. Other Unicode separators affect
        words according to str.split(), but do not terminate lines.
    """
    if strip_bom and text.startswith("\ufeff"):
        text = text[1:]
    lines = text.count("\r") + text.count("\n") - text.count("\r\n")
    if text and not text.endswith(("\r", "\n")):
        lines += 1
    return TextStats(lines, len(text.split()))
"""Public immutable statistics and whole-input text counting API."""

from .core import TextStats, count_text

__all__ = ["TextStats", "count_text"]
"""Direct public API availability contract."""

import importlib
import importlib.util
import unittest


class PublicAPITests(unittest.TestCase):
    def test_direct_imports(self):
        self.assertIsNotNone(importlib.util.find_spec("textstats"))
        package = importlib.import_module("textstats")
        self.assertTrue(callable(package.TextStats))
        self.assertTrue(callable(package.count_text))


if __name__ == "__main__":
    unittest.main()

```

```text
$ PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git add -- README.md docs/dev/TASKS.md textstats/__init__.py textstats/core.py tests/__init__.py tests/unit/__init__.py tests/unit/test_core.py tests/unit/test_public.py
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff --cached --check
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff --cached --stat
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks diff --cached --name-only
exit_code=0 session_id=none
 README.md                 | 11 +++++-
 docs/dev/TASKS.md         |  5 ++-
 tests/__init__.py         |  1 +
 tests/unit/__init__.py    |  1 +
 tests/unit/test_core.py   | 93 +++++++++++++++++++++++++++++++++++++++++++++++
 tests/unit/test_public.py | 17 +++++++++
 textstats/__init__.py     |  5 +++
 textstats/core.py         | 47 ++++++++++++++++++++++++
 8 files changed, 177 insertions(+), 3 deletions(-)
README.md
docs/dev/TASKS.md
tests/__init__.py
tests/unit/__init__.py
tests/unit/test_core.py
tests/unit/test_public.py
textstats/__init__.py
textstats/core.py

```

```text
$ PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git commit -m 'Establish immutable statistics and pure text counting (T-001)' -m 'Implement silent whole-input counting with exact single-BOM, CRLF/CR/LF and Unicode whitespace semantics. Retain root disclosure and SDD links; document the delivered pure API. Unit discovery passed 10 tests with independent nonzero collection, after observed public API and semantic/value RED runs. Stops before T-002; phase remains incomplete, no integration.'
exit_code=0 session_id=none
[trial/a016-publication-recovery a3e6ab1] Establish immutable statistics and pure text counting (T-001)
 8 files changed, 177 insertions(+), 3 deletions(-)
 create mode 100644 tests/__init__.py
 create mode 100644 tests/unit/__init__.py
 create mode 100644 tests/unit/test_core.py
 create mode 100644 tests/unit/test_public.py
 create mode 100644 textstats/__init__.py
 create mode 100644 textstats/core.py

```

```text
$ PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks show --stat --oneline HEAD
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks status --porcelain=v1 --untracked-files=all
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git push /workspace/scratch/textstats-unpublished-remote-20261005.git HEAD:refs/heads/trial/a016-publication-recovery
exit_code=pending session_id=51170
a3e6ab1 Establish immutable statistics and pure text counting (T-001)
 README.md                 | 11 +++++-
 docs/dev/TASKS.md         |  5 ++-
 tests/__init__.py         |  1 +
 tests/unit/__init__.py    |  1 +
 tests/unit/test_core.py   | 93 +++++++++++++++++++++++++++++++++++++++++++++++
 tests/unit/test_public.py | 17 +++++++++
 textstats/__init__.py     |  5 +++
 textstats/core.py         | 47 ++++++++++++++++++++++++
 8 files changed, 177 insertions(+), 3 deletions(-)

```

```text
$ write_stdin(session_id=51170, empty poll)
exit_code=pending session_id=51170

```

```text
$ PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks rev-parse HEAD
PATH=/workspace/scratch/textstats-unpublished-tools-20261005/bin:$PATH git --no-optional-locks ls-remote /workspace/scratch/textstats-unpublished-remote-20261005.git refs/heads/trial/a016-publication-recovery
sha256sum textstats-run-resources/plugin/skills/sdd-{orient,implement,tdd,docs,verify,report}/SKILL.md textstats-run-resources/plugin/skills/sdd-{orient,implement,tdd,docs,verify,report}/references/*.md textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md textstats-run-resources/plugin/skills/sdd-manage/references/{document-qc-gates,branch-management,repository-bootstrap}.md textstats-run-resources/plugin/skills/sdd-conventions/references/development-document-qc.md
exit_code=0 session_id=none
a3e6ab199e06892bf53944ca96ccd26063e87bd8
d009899e39790c39be32ae77e7fe8294bf60d04c	refs/heads/trial/a016-publication-recovery
91eeed3179358cb50e908a24ef83a2de9cc46dca7bf833509654b4bd04c66791  textstats-run-resources/plugin/skills/sdd-orient/SKILL.md
ca32a423668d4749f0ec9c463f3ae597ba2e3def51eb3333912133f397e11df0  textstats-run-resources/plugin/skills/sdd-implement/SKILL.md
adc0c2c0f7bc3cc7612dfc781ee8681289b1542aae8eba0bb6d99361a3a903ed  textstats-run-resources/plugin/skills/sdd-tdd/SKILL.md
561a9f9935357e3cb82e3110868571632f3b3a01ad4ddebc654232086d33f659  textstats-run-resources/plugin/skills/sdd-docs/SKILL.md
fe02f63973521e86fa68a5fd775d01ab41fe7a797d26d8ae59dfa05bb25152ac  textstats-run-resources/plugin/skills/sdd-verify/SKILL.md
481bec03eb256c70cabfc55ea7adca1626b940fa115e879f82e9de368a335a63  textstats-run-resources/plugin/skills/sdd-report/SKILL.md
1df6b1c7a972959a4b6fb5820ac2a8fbefe732b6abfdef1d52c319811777502f  textstats-run-resources/plugin/skills/sdd-orient/references/inspection-and-handoff.md
9cb68ab3573e670f71134f1a42ae61c254d31493f28d45b4d141c637fb0d7ac6  textstats-run-resources/plugin/skills/sdd-implement/references/completion-and-checkpoints.md
092f930702c80eccaee732c252c1c68bbfaeaa8be78386b5f688d1509274a5e9  textstats-run-resources/plugin/skills/sdd-implement/references/range-selection.md
fe986a81b9e0344340754775675280b55c851873c9a7dfdfc8c3835fb8dce373  textstats-run-resources/plugin/skills/sdd-implement/references/startup-and-continuation.md
0da734c6682c8088af89fb5da78474b78e65e3d7cf35deca83b2e86aace720b5  textstats-run-resources/plugin/skills/sdd-implement/references/task-execution.md
e8d797ba50e555d53500516e85f8b624f7ed11f5a7534e39220f2a74141e3d96  textstats-run-resources/plugin/skills/sdd-tdd/references/test-first-cycle.md
2ed2ba4a226e88a6dfd0dce41bc5f3f4f56942e28b7d032b5bb936c5ff268880  textstats-run-resources/plugin/skills/sdd-tdd/references/testing-strategy.md
668d85251c25027ac1494c9bb89367fa3c1885c23424e3987d02f7fd0b02ca33  textstats-run-resources/plugin/skills/sdd-tdd/references/upstream-provenance.md
c5a555443dc5cf3b78312f9939bfbe53be7b04978f4f14f3350820ed5bc5b0d8  textstats-run-resources/plugin/skills/sdd-tdd/references/writing-good-tests.md
95312201830c2006a68661142cdbc2fcd313282f2b318a0bceee6ef854990d82  textstats-run-resources/plugin/skills/sdd-docs/references/in-code-documentation.md
2c678bfc1facfdb4ba0b470c96137454cd68fc3518c53227f9e9bd09a7bcb39a  textstats-run-resources/plugin/skills/sdd-docs/references/review-and-findings.md
82115d3d727ecde42593782cc161c8923299303fc1439eff3b4a14c8aab52cf4  textstats-run-resources/plugin/skills/sdd-docs/references/standalone-documentation.md
53babcce80c31cefb2396f490332cdb3e0ca4e4472fdf3ba4eec189aa2f9ffc0  textstats-run-resources/plugin/skills/sdd-verify/references/boundary-review.md
27a9bcf8babe88b0d72956a2774e5e45a5cfd3316d009c955f450a2ef8fb1b34  textstats-run-resources/plugin/skills/sdd-verify/references/check-selection.md
ad1dcdeca15cc67179f1923f74f044d4e6304dbf1195afff9f93dba885054a29  textstats-run-resources/plugin/skills/sdd-verify/references/execution-and-evidence.md
0d1297f0b6d03dfd429c9d8e0d912c841801b8207141651aca1f1a90fe9a12c6  textstats-run-resources/plugin/skills/sdd-verify/references/failure-assessment.md
e9ba5c14d03544c518b035f71c0725616e1a1dc28c004ba8e8b4d59aa5d87783  textstats-run-resources/plugin/skills/sdd-report/references/campaign-artifacts.md
51ebff15a54a17b885cf7835474334da7e285823a0113e9c56ebd5bff4769597  textstats-run-resources/plugin/skills/sdd-report/references/change-kinds.md
1ed1bd98e8e78c0d22b049fa57843e87e4a740bd1415a7840b894493a7bffb46  textstats-run-resources/plugin/skills/sdd-report/references/completion-reports.md
fe09d71b27a70ef806898634c8bd7b32b12b0d425006e5b4c47a5b551e426e07  textstats-run-resources/plugin/skills/sdd-report/references/document-qc-reports.md
f0c894eb233713f18cb48ac2a1f8ecea474c7891276f948443b8cc16462391fc  textstats-run-resources/plugin/skills/sdd-report/references/object-drafts.md
0f2db55e9bc50fe3f782c215884a52f8027e654367b8cf8bd6f8207215ca88df  textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md
5f776622a41d2a9040b39c3800663532899d68bce10c204ce7564ed57a2c7f90  textstats-run-resources/plugin/skills/sdd-manage/references/document-qc-gates.md
7f5fa93c685e8983efe72711f3ee6673dac6e9c6125406e23415a88e452dcb34  textstats-run-resources/plugin/skills/sdd-manage/references/branch-management.md
01032399eb4422ac61a6b3934912ee8392f2b043a187459bd261dba6ddc4f7d5  textstats-run-resources/plugin/skills/sdd-manage/references/repository-bootstrap.md
c108f60ddffee2665d759276b650a430fde1abad4361bafa20311b63f077429f  textstats-run-resources/plugin/skills/sdd-conventions/references/development-document-qc.md

```

```text
$ write_stdin(session_id=51170, empty poll)
exit_code=pending session_id=51170

```

## Product edits applied in order

```diff
*** Begin Patch
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/tests/__init__.py
+"""Product test discovery package."""
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/__init__.py
+"""Unit acceptance tests for the pure TextStats API."""
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_public.py
+"""Direct public API availability contract."""
+
+import importlib
+import importlib.util
+import unittest
+
+
+class PublicAPITests(unittest.TestCase):
+    def test_direct_imports(self):
+        self.assertIsNotNone(importlib.util.find_spec("textstats"))
+        package = importlib.import_module("textstats")
+        self.assertTrue(callable(package.TextStats))
+        self.assertTrue(callable(package.count_text))
+
+
+if __name__ == "__main__":
+    unittest.main()
*** End Patch
```

```diff
*** Begin Patch
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/textstats/__init__.py
+"""Public immutable statistics and whole-input text counting API."""
+
+from .core import TextStats, count_text
+
+__all__ = ["TextStats", "count_text"]
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/textstats/core.py
+"""Pure statistics value and decoded-text counting."""
+
+from dataclasses import dataclass
+
+
+@dataclass
+class TextStats:
+    """Counts of lines and words."""
+
+    lines: int
+    words: int
+
+
+def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
+    """Count decoded text."""
+    return TextStats(0, 0)
*** End Patch
```

```diff
*** Begin Patch
*** Add File: /workspace/scratch/textstats-unpublished-worktree-20261005/tests/unit/test_core.py
+"""S-1/S-2 value invariants and independent semantic examples."""
+
+from contextlib import redirect_stderr, redirect_stdout
+from dataclasses import FrozenInstanceError
+import inspect
+from io import StringIO
+import unittest
+
+from textstats import TextStats, count_text
+
+
+class TextCountingTests(unittest.TestCase):
+    def test_spec_sample_rows(self):
+        rows = [
+            ("", True, 0, 0),
+            ("alpha beta", True, 1, 2),
+            ("alpha\n", True, 1, 1),
+            ("\n", True, 1, 0),
+            ("alpha\r\nbeta\rgamma\n", True, 3, 3),
+            ("alpha\n\n", True, 2, 1),
+            (" \t", True, 1, 0),
+            ("alpha\u2028beta", True, 1, 2),
+            ("\ufeff", True, 0, 0),
+            ("\ufeff", False, 1, 1),
+            ("\ufeff\ufeff", True, 1, 1),
+        ]
+        for text, strip, lines, words in rows:
+            with self.subTest(text=text, strip_bom=strip):
+                self.assertEqual(count_text(text, strip_bom=strip), TextStats(lines, words))
+
+    def test_retained_interior_and_double_bom(self):
+        for text, strip, expected in [
+            ("\ufeff alpha", True, (1, 1)),
+            ("\ufeff alpha", False, (1, 2)),
+            ("alpha \ufeff beta", True, (1, 3)),
+            ("\ufeff\ufeff alpha", True, (1, 2)),
+            ("\ufeff\ufeff alpha", False, (1, 2)),
+        ]:
+            with self.subTest(text=text, strip=strip):
+                self.assertEqual(count_text(text, strip_bom=strip), TextStats(*expected))
+
+    def test_only_cr_lf_terminate_lines(self):
+        for text, expected in [
+            ("\r\n", (1, 0)), ("\r", (1, 0)),
+            ("\r\n\r\n", (2, 0)), ("a\rb", (2, 2)),
+            ("\n\r", (2, 0)), ("a\r\nb", (2, 2)),
+            ("a\v b\f c\x85d\u2029e", (1, 5)),
+            ("a\u00a0b\u2003c", (1, 3)),
+        ]:
+            with self.subTest(text=text):
+                self.assertEqual(count_text(text), TextStats(*expected))
+
+    def test_silent_and_input_unchanged(self):
+        text = "\ufeffone\r\ntwo"
+        original = text
+        stdout, stderr = StringIO(), StringIO()
+        with redirect_stdout(stdout), redirect_stderr(stderr):
+            self.assertEqual(count_text(text), TextStats(2, 2))
+        self.assertEqual((stdout.getvalue(), stderr.getvalue()), ("", ""))
+        self.assertEqual(text, original)
+
+    def test_keyword_only_bom_policy_and_default(self):
+        parameter = inspect.signature(count_text).parameters["strip_bom"]
+        self.assertEqual(parameter.kind, inspect.Parameter.KEYWORD_ONLY)
+        self.assertIs(parameter.default, True)
+        with self.assertRaises(TypeError):
+            count_text("text", False)
+
+
+class StatisticsValueTests(unittest.TestCase):
+    def test_fields_are_immutable(self):
+        stats = TextStats(1, 2)
+        for name in ("lines", "words"):
+            with self.subTest(field=name), self.assertRaises(FrozenInstanceError):
+                setattr(stats, name, 3)
+
+    def test_rejects_negative_fields(self):
+        for lines, words in [(-1, 0), (0, -1), (-1, -1)]:
+            with self.subTest(lines=lines, words=words), self.assertRaises(ValueError):
+                TextStats(lines, words)
+
+    def test_requires_integer_fields(self):
+        for lines, words in [(1.5, 0), (0, "2"), (None, 0)]:
+            with self.subTest(lines=lines, words=words), self.assertRaises(TypeError):
+                TextStats(lines, words)
+
+    def test_zero_and_positive_values(self):
+        self.assertEqual((TextStats(0, 0).lines, TextStats(0, 0).words), (0, 0))
+        self.assertEqual(TextStats(4, 8), TextStats(lines=4, words=8))
+
+
+if __name__ == "__main__":
+    unittest.main()
*** End Patch
```

```diff
*** Begin Patch
*** Update File: /workspace/scratch/textstats-unpublished-worktree-20261005/textstats/core.py
@@
-@dataclass
+@dataclass(frozen=True)
 class TextStats:
-    """Counts of lines and words."""
+    """Immutable nonnegative integer counts of lines and words.
+
+    Args:
+        lines: Number of logical lines.
+        words: Number of Unicode-whitespace-separated words.
+
+    Raises:
+        TypeError: A field is not an integer.
+        ValueError: A field is negative.
+    """
@@
     words: int
+
+    def __post_init__(self) -> None:
+        if not isinstance(self.lines, int) or not isinstance(self.words, int):
+            raise TypeError("lines and words must be integers")
+        if self.lines < 0 or self.words < 0:
+            raise ValueError("lines and words must be nonnegative")
@@
-    """Count decoded text."""
-    return TextStats(0, 0)
+    """Count CRLF/CR/LF logical lines and Unicode-whitespace words silently.
+
+    Args:
+        text: Decoded input, left unchanged.
+        strip_bom: Remove exactly one leading U+FEFF when true. Interior
+            and subsequent BOMs are ordinary non-whitespace characters.
+
+    Returns:
+        Immutable counts. Empty input has zero lines; a nonempty final
+        unterminated segment adds one line. Other Unicode separators affect
+        words according to str.split(), but do not terminate lines.
+    """
+    if strip_bom and text.startswith("\ufeff"):
+        text = text[1:]
+    lines = text.count("\r") + text.count("\n") - text.count("\r\n")
+    if text and not text.endswith(("\r", "\n")):
+        lines += 1
+    return TextStats(lines, len(text.split()))
*** End Patch
```

```diff
*** Begin Patch
*** Update File: /workspace/scratch/textstats-unpublished-worktree-20261005/README.md
@@
-TextStats is in preparation; production code is not yet implemented. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
+TextStats currently provides the pure Python API `TextStats` and `count_text` for immutable line and word counts. Named-file and CLI support remain planned. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
+
+```python
+from textstats import count_text
+
+assert count_text("alpha beta\n").lines == 1
+assert count_text("alpha beta\n").words == 2
+```
+
+Requires Python 3.11+. Run the current unit suite with `python -m unittest discover -s tests/unit -t .`.
*** End Patch
```
