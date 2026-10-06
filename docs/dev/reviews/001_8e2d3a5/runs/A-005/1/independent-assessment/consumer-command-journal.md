# A-005 consumer command journal

Scope: T-002–T-004, milestone 1.1; existing phase branch. Standing human GO and repository-scoped read/write grant cover normal scoped commits, pushes and maintained hosting. No phase integration. Authorization policy read before mutations. Initial remote read confirmed 9b24dbd on phase branch; worktree clean. Governing preparation reviews remain current for unchanged contracts. T-001 prior evidence is historical, not fresh RED proof.

## t002-red

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_file_api tests.integration.test_file_api -v`

Exit: 1. Actual combined output: [t002-red.txt](t002-red.txt).

## t002-green

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_file_api tests.integration.test_file_api -v`

Exit: 0. Actual combined output: [t002-green.txt](t002-green.txt).

## t002-unit-acceptance

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`

Exit: 0. Actual combined output: [t002-unit-acceptance.txt](t002-unit-acceptance.txt).

## t002-integration-acceptance

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`

Exit: 0. Actual combined output: [t002-integration-acceptance.txt](t002-integration-acceptance.txt).

## t002-diff-check

Command: `git diff --check`

Exit: 0. Actual combined output: [t002-diff-check.txt](t002-diff-check.txt).

## t002-diff

Command: `git diff --stat`

Exit: 0. Actual combined output: [t002-diff.txt](t002-diff.txt).

## t002-stage

Command: `git add textstats/io.py textstats/__init__.py tests/unit/test_file_api.py tests/integration/__init__.py tests/integration/test_file_api.py README.md docs/dev/TASKS.md`

Exit: 0. Actual combined output: [t002-stage.txt](t002-stage.txt).

## t002-staged

Command: `git diff --cached`

Exit: 0. Actual combined output: [t002-staged.txt](t002-staged.txt).

## t002-commit

Command: `git commit -m 'Integrate strict UTF-8 named-file API (T-002)' -m 'Verify real path/BOM/terminator cases, API silence and owned success closure. Unit discovery: 13; integration: 2, all pass.' -m 'Fixes pchemguy/Skill-Test-SDD-Manager-TextStats-20261004#2'`

Exit: 0. Actual combined output: [t002-commit.txt](t002-commit.txt).

## t002-push

Command: `git push origin phase/1-named-file-utility`

Exit: 0. Actual combined output: [t002-push.txt](t002-push.txt).

## t002-remote

Command: `git ls-remote origin refs/heads/phase/1-named-file-utility`

Exit: 0. Actual combined output: [t002-remote.txt](t002-remote.txt).

## t002-preclose

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/2`. Exit: 0. Sanitized observed metadata: [t002-preclose.json](t002-preclose.json).

## t002-comment

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py POST issues/2/comments /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/t002-comment.json`. Exit: 0. Sanitized observed metadata: [t002-comment.json](t002-comment.json).

## t002-close

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py PATCH issues/2 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/close-completed.json`. Exit: 0. Sanitized observed metadata: [t002-close.json](t002-close.json).

## t002-readback

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/2`. Exit: 0. Sanitized observed metadata: [t002-readback.json](t002-readback.json).

## t003-red

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_cli tests.integration.test_cli -v`

Exit: 1. Actual combined output: [t003-red.txt](t003-red.txt).

## t003-green

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.unit.test_cli tests.integration.test_cli -v`

Exit: 0. Actual combined output: [t003-green.txt](t003-green.txt).

## t003-unit-acceptance

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`

Exit: 0. Actual combined output: [t003-unit-acceptance.txt](t003-unit-acceptance.txt).

## t003-integration-acceptance

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`

Exit: 0. Actual combined output: [t003-integration-acceptance.txt](t003-integration-acceptance.txt).

## t003-demo

Command: `env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/demonstrate.py`

Exit: 0. Actual combined output: [t003-demo.txt](t003-demo.txt).

## t003-diff-check

Command: `git diff --check`

Exit: 0. Actual combined output: [t003-diff-check.txt](t003-diff-check.txt).

## t003-stage

Command: `git add textstats/cli.py textstats/__main__.py tests/unit/test_cli.py tests/integration/test_cli.py README.md docs/dev/TASKS.md`

Exit: 0. Actual combined output: [t003-stage.txt](t003-stage.txt).

## t003-staged

Command: `git diff --cached`

Exit: 0. Actual combined output: [t003-staged.txt](t003-staged.txt).

## t003-commit

Command: `git commit -m 'Deliver useful named-file module CLI (T-003)' -m 'Verify exact text counts, BOM policy, dash paths and help/usage before acquisition. Unit discovery 14 and integration 6 tests pass.' -m 'Fixes pchemguy/Skill-Test-SDD-Manager-TextStats-20261004#3'`

Exit: 0. Actual combined output: [t003-commit.txt](t003-commit.txt).

## t003-push

Command: `git push origin phase/1-named-file-utility`

Exit: 0. Actual combined output: [t003-push.txt](t003-push.txt).

## t003-remote

Command: `git ls-remote origin refs/heads/phase/1-named-file-utility`

Exit: 0. Actual combined output: [t003-remote.txt](t003-remote.txt).

## t003-preclose

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/3`. Exit: 0. Sanitized observed metadata: [t003-preclose.json](t003-preclose.json).

## t003-comment

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py POST issues/3/comments /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/t003-comment.json`. Exit: 0. Sanitized observed metadata: [t003-comment.json](t003-comment.json).

## t003-close

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py PATCH issues/3 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/close-completed.json`. Exit: 0. Sanitized observed metadata: [t003-close.json](t003-close.json).

## t003-readback

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/3`. Exit: 0. Sanitized observed metadata: [t003-readback.json](t003-readback.json).

## t004-reviewed-state

Command: `git show --stat --oneline HEAD`

Exit: 0. Actual combined output: [t004-reviewed-state.txt](t004-reviewed-state.txt).

## t004-unit

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`

Exit: 0. Actual combined output: [t004-unit.txt](t004-unit.txt).

## t004-integration

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`

Exit: 0. Actual combined output: [t004-integration.txt](t004-integration.txt).

## t004-demo

Command: `env PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=. python /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/demonstrate.py`

Exit: 0. Actual combined output: [t004-demo.txt](t004-demo.txt).

## t004-help

Command: `env PYTHONDONTWRITEBYTECODE=1 python -m textstats --help`

Exit: 0. Actual combined output: [t004-help.txt](t004-help.txt).

## t004-diff-check

Command: `git diff --check`

Exit: 0. Actual combined output: [t004-diff-check.txt](t004-diff-check.txt).

## T-004 inspection

Read all five production modules and all product tests at f2260a2 against SPEC/PLAN milestone 1.1. Review covers facade, pure semantics, binary complete strict decoding, success ownership, argparse validation/rendering and module entry. No in-scope defects/TODOs found. Failure hardening, diagnostics and distribution remain later scope, not waived. Report contains exact coverage and limits. No production amendments during review.

## t004-report-diff-check

Command: `git diff --check`

Exit: 0. Actual combined output: [t004-report-diff-check.txt](t004-report-diff-check.txt).

## t004-stage

Command: `git add docs/dev/reports/phases/1/1.1.md docs/dev/TASKS.md`

Exit: 0. Actual combined output: [t004-stage.txt](t004-stage.txt).

## t004-staged

Command: `git diff --cached`

Exit: 0. Actual combined output: [t004-staged.txt](t004-staged.txt).

## t004-commit

Command: `git commit -m 'Review and report named-file MVP milestone 1.1 (T-004)' -m 'Inspect delivered modules and acceptance coverage. Fresh unit 14/integration 6 tests and normal/BOM/dash demonstrations pass. No findings or TODOs; later reliability and phase work remain incomplete.' -m 'Fixes pchemguy/Skill-Test-SDD-Manager-TextStats-20261004#4'`

Exit: 0. Actual combined output: [t004-commit.txt](t004-commit.txt).

## t004-push

Command: `git push origin phase/1-named-file-utility`

Exit: 0. Actual combined output: [t004-push.txt](t004-push.txt).

## t004-remote

Command: `git ls-remote origin refs/heads/phase/1-named-file-utility`

Exit: 0. Actual combined output: [t004-remote.txt](t004-remote.txt).

## t004-preclose

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/4`. Exit: 0. Sanitized observed metadata: [t004-preclose.json](t004-preclose.json).

## t004-comment

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py POST issues/4/comments /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/t004-comment.json`. Exit: 0. Sanitized observed metadata: [t004-comment.json](t004-comment.json).

## t004-close

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py PATCH issues/4 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/close-completed.json`. Exit: 0. Sanitized observed metadata: [t004-close.json](t004-close.json).

## t004-readback

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET issues/4`. Exit: 0. Sanitized observed metadata: [t004-readback.json](t004-readback.json).

## milestone-enumerate

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET 'milestones?state=all&per_page=100'`. Exit: 0. Sanitized observed metadata: [milestone-enumerate.json](milestone-enumerate.json).

## milestone-issues

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET 'issues?milestone=1&state=all&per_page=100'`. Exit: 0. Sanitized observed metadata: [milestone-issues.json](milestone-issues.json).

## Hosted identity/read evidence

Connector reads validated exact title/body markers for T-001–T-004 and milestone association 1. T-001 was already closed; its comment links completion commit 9b24dbd and committed TASKS evidence, so no duplicate write. Comments connector first rejected a missing repo_full_name argument, then the corrected read succeeded; no write or authority rejection. Counts under CR/LF newline translation can remain identical, so the review report clarifies binary-mode preservation is inspection evidence rather than a claim of independent count-test sensitivity. This evidence clarification changes no product behavior.

## t004-evidence-diff

Command: `git diff --check`

Exit: 0. Actual combined output: [t004-evidence-diff.txt](t004-evidence-diff.txt).

## t004-evidence-stage

Command: `git add docs/dev/reports/phases/1/1.1.md`

Exit: 0. Actual combined output: [t004-evidence-stage.txt](t004-evidence-stage.txt).

## t004-evidence-staged

Command: `git diff --cached`

Exit: 0. Actual combined output: [t004-evidence-staged.txt](t004-evidence-staged.txt).

## t004-evidence-commit

Command: `git commit -m 'Clarify binary-mode review evidence for milestone 1.1 (T-004)' -m 'Distinguish inspected binary acquisition from count-test sensitivity: newline translation may preserve counts. No implementation or acceptance change.'`

Exit: 0. Actual combined output: [t004-evidence-commit.txt](t004-evidence-commit.txt).

## t004-evidence-push

Command: `git push origin phase/1-named-file-utility`

Exit: 0. Actual combined output: [t004-evidence-push.txt](t004-evidence-push.txt).

## t004-evidence-remote

Command: `git ls-remote origin refs/heads/phase/1-named-file-utility`

Exit: 0. Actual combined output: [t004-evidence-remote.txt](t004-evidence-remote.txt).

## milestone-close

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py PATCH milestones/1 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-005/1/milestone-close.json`. Exit: 0. Sanitized observed metadata: [milestone-close.json](milestone-close.json).

## milestone-readback

Standing human GO and scoped read/write token grant authorize this maintained repository operation. Command: `python .git/textstats-hosting-curl.py GET milestones/1`. Exit: 0. Sanitized observed metadata: [milestone-readback.json](milestone-readback.json).

## final-content-scope

Command: `git diff 9b24dbd..HEAD --name-only`

Exit: 0. Actual combined output: [final-content-scope.txt](final-content-scope.txt).

## final-protected-scope

Command: `git diff 9b24dbd..HEAD -- AGENTS.md textstats-run-resources docs/dev/PROJECT.md docs/dev/SPEC.md docs/dev/PLAN.md docs/dev/ARCHITECTURE.md docs/dev/DECOMPOSITION.md docs/dev/layout.md`

Exit: 0. Actual combined output: [final-protected-scope.txt](final-protected-scope.txt).

## boundary-diff-check

Command: `git diff --check`

Exit: 0. Actual combined output: [boundary-diff-check.txt](boundary-diff-check.txt).

## boundary-stage

Command: `git add docs/dev/TASKS.md docs/dev/reports/phases/1/1.1.md`

Exit: 0. Actual combined output: [boundary-stage.txt](boundary-stage.txt).

## boundary-staged

Command: `git diff --cached`

Exit: 0. Actual combined output: [boundary-staged.txt](boundary-staged.txt).

## boundary-commit

Command: `git commit -m 'Reconcile verified milestone 1.1 completion and pause (T-004)' -m 'Read back four completed task issues and closed milestone 1.1. Preserve incomplete phase and later task status; no integration. Product acceptance evidence remains applicable to unchanged source.'`

Exit: 0. Actual combined output: [boundary-commit.txt](boundary-commit.txt).

## boundary-push

Command: `git push origin phase/1-named-file-utility`

Exit: 0. Actual combined output: [boundary-push.txt](boundary-push.txt).

## final-remote

Command: `git ls-remote origin refs/heads/phase/1-named-file-utility refs/heads/main`

Exit: 0. Actual combined output: [final-remote.txt](final-remote.txt).

## final-status

Command: `git status --short`

Exit: 0. Actual combined output: [final-status.txt](final-status.txt).

## final-log

Command: `git log -5 --oneline`

Exit: 0. Actual combined output: [final-log.txt](final-log.txt).

## Final boundary

Milestone 1.1 closed/read back; all four issues completed. Local parent reconciliation published at 159c662e06405b1fbf696e8e9d9d5d47024187be. Final remote confirms main unchanged at 4c275cc and phase tip equals local HEAD; final status output empty. Required verification applies to unchanged production source. No authority rejection or bypass; no later work. See CONSUMER-RESULT.md.
