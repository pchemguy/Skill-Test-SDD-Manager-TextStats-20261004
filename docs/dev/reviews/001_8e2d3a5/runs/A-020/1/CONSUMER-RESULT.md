# A-020 consumer result

Completed only T-001 locally on `trial/a020-preservation`.

Commit: `5719983f2d11266dba58bc8b149505c2519df4cb` — Implement immutable pure text statistics (T-001).

Implemented direct TextStats/count_text exports, frozen nonnegative integer statistics and exact single-BOM, CRLF/CR/LF and Unicode-word semantics. Module/API docstrings and README state match delivered pure API. Only T-001 checked complete.

Checks: Python 3.12.14. RED: importable NotImplementedError scaffolding, 7 tests / 36 missing-behavior errors, exit 1 (RED.txt). GREEN and separate verification: exact command `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`, 7 tests pass, exit 0, no skips (GREEN.txt, VERIFY.txt). Worktree/staged diff whitespace checks pass. Reviewed source gate hashes match governing files. All SPEC sample rows and additional BOM/terminator/Unicode, value invariants, direct imports/signature and silence covered.

Commit contains only README.md, docs/dev/TASKS.md, textstats/__init__.py, textstats/core.py, tests/__init__.py, tests/unit/__init__.py, tests/unit/test_core.py. Unrelated notes/local-retained.txt retains staged and unstaged states and notes/untracked-retained.txt remains unchanged/untracked; final status matches initial. No push, hosting write, integration, shared branch change, clone, credentials inspection or environment edits occurred.

Remaining: T-002 onward; file API, module CLI, distribution and milestone/phase exits. Hosted issue reconciliation/publication deliberately outside local-only scope. No T-001 blocker.
