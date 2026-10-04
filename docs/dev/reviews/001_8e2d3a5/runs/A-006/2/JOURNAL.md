# A-006/2 consumer journal

2026-10-04 — Read REQUEST.md, product AGENTS and pinned sdd-manage/orient/implement/verify/report/forge references including revision-authorization. Existing human standing grant covers designated repository read/write workflow and scoped token use. No credentials/helper inspected.

Orientation commands: git --no-optional-locks status --short; branch --show-current; rev-parse HEAD main; remote -v. Results: clean, phase/1-named-file-utility, dec4ca107a8f0e2f878f580c88fd33303f570c01; main 4c275cc46fc0163c9e1e50871d3cc33c4c38567e; origin designated GitHub repository.

Startup command: git ls-remote origin refs/heads/phase/1-named-file-utility refs/heads/main. Exit 0; exact tips matched local. No outstanding push.

Read current governing documents, QC reports, milestone reports, all production modules/product tests/public guides/build recipe. Prior complete T-001–T-008 preserved; only T-009 selected. Read-only implementation review: no finding. Existing RED/GREEN provenance retained in TASKS and milestone reports; no behavior change or new RED required for review-only T-009.

Connector github_fetch_issue(repo=designated repository, issue_number=9): open, exact title [T-009] Review, test and report phase 1; milestone 3; exact sdd-forge:task-id=T-009 marker; 0 comments. Body not reproduced.
## Command

```sh
python .git/textstats-hosting-curl.py GET 'milestones?state=all&per_page=100'
```

Exit 0
```text
{"http_status": 200, "result": [{"closed_issues": 4, "description_sha256": "90eed64da1fb803a181c5aa8dcd0992c3ff265a3afba0a37d2d910038a8cb453", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1", "id": 18303256, "number": 1, "open_issues": 0, "state": "closed", "title": "sdd-1.1-Named-file-counting-MVP"}, {"closed_issues": 4, "description_sha256": "7d4093d70123814e0eb04004430ed765d07a18dc49082ef56ac160e5b225b914", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2", "id": 18303258, "number": 2, "open_issues": 0, "state": "closed", "title": "sdd-1.2-Reliable-documented-distribution"}, {"closed_issues": 0, "description_sha256": "0fdb02b760e43ed1b245ceae4b451b208885dbd9a790642b8bec67531135b790", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3", "id": 18303268, "number": 3, "open_issues": 1, "state": "open", "title": "sdd-1.3-Phase-1-review"}], "transport": "curl"}
```
## Command

```sh
python .git/textstats-hosting-curl.py GET 'issues?state=all&per_page=100'
```

Exit 0
```text
{"http_status": 200, "result": [{"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9", "id": 5700128035, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 0, "description_sha256": "0fdb02b760e43ed1b245ceae4b451b208885dbd9a790642b8bec67531135b790", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3", "id": 18303268, "number": 3, "open_issues": 1, "state": "open", "title": "sdd-1.3-Phase-1-review"}, "number": 9, "state": "open", "state_reason": null, "title": "[T-009] Review, test and report phase 1"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/8", "id": 5700127270, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "7d4093d70123814e0eb04004430ed765d07a18dc49082ef56ac160e5b225b914", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2", "id": 18303258, "number": 2, "open_issues": 0, "state": "closed", "title": "sdd-1.2-Reliable-documented-distribution"}, "number": 8, "state": "closed", "state_reason": "completed", "title": "[T-008] Review, test and report milestone 1.2"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/7", "id": 5700126592, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "7d4093d70123814e0eb04004430ed765d07a18dc49082ef56ac160e5b225b914", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2", "id": 18303258, "number": 2, "open_issues": 0, "state": "closed", "title": "sdd-1.2-Reliable-documented-distribution"}, "number": 7, "state": "closed", "state_reason": "completed", "title": "[T-007] Establish isolated source-distribution acceptance"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/6", "id": 5700125883, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "7d4093d70123814e0eb04004430ed765d07a18dc49082ef56ac160e5b225b914", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2", "id": 18303258, "number": 2, "open_issues": 0, "state": "closed", "title": "sdd-1.2-Reliable-documented-distribution"}, "number": 6, "state": "closed", "state_reason": "completed", "title": "[T-006] Complete CLI diagnostics and public documentation"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/5", "id": 5700125215, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "7d4093d70123814e0eb04004430ed765d07a18dc49082ef56ac160e5b225b914", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2", "id": 18303258, "number": 2, "open_issues": 0, "state": "closed", "title": "sdd-1.2-Reliable-documented-distribution"}, "number": 5, "state": "closed", "state_reason": "completed", "title": "[T-005] Harden named-file API failure and resource behavior"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/4", "id": 5700124593, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "90eed64da1fb803a181c5aa8dcd0992c3ff265a3afba0a37d2d910038a8cb453", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1", "id": 18303256, "number": 1, "open_issues": 0, "state": "closed", "title": "sdd-1.1-Named-file-counting-MVP"}, "number": 4, "state": "closed", "state_reason": "completed", "title": "[T-004] Review, test and report milestone 1.1"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/3", "id": 5700123890, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "90eed64da1fb803a181c5aa8dcd0992c3ff265a3afba0a37d2d910038a8cb453", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1", "id": 18303256, "number": 1, "open_issues": 0, "state": "closed", "title": "sdd-1.1-Named-file-counting-MVP"}, "number": 3, "state": "closed", "state_reason": "completed", "title": "[T-003] Deliver the useful named-file module CLI"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/2", "id": 5700123176, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "90eed64da1fb803a181c5aa8dcd0992c3ff265a3afba0a37d2d910038a8cb453", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1", "id": 18303256, "number": 1, "open_issues": 0, "state": "closed", "title": "sdd-1.1-Named-file-counting-MVP"}, "number": 2, "state": "closed", "state_reason": "completed", "title": "[T-002] Integrate strict UTF-8 named-file API"}, {"html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/1", "id": 5700122430, "labels": [{"color": "1d76db", "description_sha256": "1d10e5e13dcb525725652cbd824d6dc4ba7d45e53a176d6d5435804d013cdef3", "id": 12538641934, "name": "sdd-phase-1-Named-file-utility"}], "milestone": {"closed_issues": 4, "description_sha256": "90eed64da1fb803a181c5aa8dcd0992c3ff265a3afba0a37d2d910038a8cb453", "html_url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1", "id": 18303256, "number": 1, "open_issues": 0, "state": "closed", "title": "sdd-1.1-Named-file-counting-MVP"}, "number": 1, "state": "closed", "state_reason": "completed", "title": "[T-001] Establish immutable statistics and pure text counting"}], "transport": "curl"}
```
## Command

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
```

Exit 0
```text
test_expected_errors_are_identified_and_atomic (tests.unit.test_cli.CliFailureTests.test_expected_errors_are_identified_and_atomic) ... ok
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
test_open_failure_is_silent_and_preserves_exception (tests.unit.test_file_api.FileFailureTests.test_open_failure_is_silent_and_preserves_exception) ... ok
test_read_decode_and_close_failure_are_atomic_and_close_owned_handle (tests.unit.test_file_api.FileFailureTests.test_read_decode_and_close_failure_are_atomic_and_close_owned_handle) ... ok
test_success_closes_owned_handle (tests.unit.test_file_api.FileLifecycleTests.test_success_closes_owned_handle) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.009s

OK
```
## Command

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v
```

Exit 0
```text
test_help (tests.integration.test_cli.ModuleCliTests.test_help) ... ok
test_invalid_invocations (tests.integration.test_cli.ModuleCliTests.test_invalid_invocations) ... ok
test_keep_bom_and_dash_prefixed_filename (tests.integration.test_cli.ModuleCliTests.test_keep_bom_and_dash_prefixed_filename) ... ok
test_named_files_counts_and_api_agreement (tests.integration.test_cli.ModuleCliTests.test_named_files_counts_and_api_agreement) ... ok
test_expected_file_failures (tests.integration.test_cli.ModuleFailureTests.test_expected_file_failures) ... ok
test_extracted_package_public_docs_and_module_contract (tests.integration.test_distribution.SourceDistributionTests.test_extracted_package_public_docs_and_module_contract) ... ok
test_public_export_and_signature (tests.integration.test_file_api.FileApiTests.test_public_export_and_signature) ... ok
test_real_files_paths_bom_terminators_and_silence (tests.integration.test_file_api.FileApiTests.test_real_files_paths_bom_terminators_and_silence) ... ok
test_real_missing_directory_and_malformed_files_are_silent_and_unchanged (tests.integration.test_file_api.FileFailureIntegrationTests.test_real_missing_directory_and_malformed_files_are_silent_and_unchanged) ... ok

----------------------------------------------------------------------
Ran 9 tests in 1.308s

OK
```
## Command

```sh
git diff --check
```

Exit 0
```text

```


## Connector identity readback before T-009 report persistence

[
  {
    "number": 1,
    "title": "[T-001] Establish immutable statistics and pure text counting",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 1,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/1",
    "marker": "sdd-forge:task-id=T-001",
    "body_sha256": "ef70d43152eb9cf8cdc9cf6620393942571a9c97cf1fad3d5bcf9d6c7155bbed"
  },
  {
    "number": 2,
    "title": "[T-002] Integrate strict UTF-8 named-file API",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 1,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/2",
    "marker": "sdd-forge:task-id=T-002",
    "body_sha256": "1f9b21dee23b72ada993ac6adb8b35df446d3d9fb5f238e9b2111260bbca58ad"
  },
  {
    "number": 3,
    "title": "[T-003] Deliver the useful named-file module CLI",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 1,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/3",
    "marker": "sdd-forge:task-id=T-003",
    "body_sha256": "127d85225f7cdc1711313802b400e1efd5cc7cded2039ca9e7ca96cdb8337c86"
  },
  {
    "number": 4,
    "title": "[T-004] Review, test and report milestone 1.1",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 1,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/4",
    "marker": "sdd-forge:task-id=T-004",
    "body_sha256": "171b5291c5b294baf5f6cb68dfa2807d1ab00f105e6e4f96a9b83e2d87d3bf47"
  },
  {
    "number": 5,
    "title": "[T-005] Harden named-file API failure and resource behavior",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 2,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/5",
    "marker": "sdd-forge:task-id=T-005",
    "body_sha256": "0dff58859f4d04b85056a76f5336de64f13b32754f14ed0820c3d8c1fa4364c6"
  },
  {
    "number": 6,
    "title": "[T-006] Complete CLI diagnostics and public documentation",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 2,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/6",
    "marker": "sdd-forge:task-id=T-006",
    "body_sha256": "c2831432f6a923fc3514662f53482c7a21dba0a6b7a8a2dc4d38843980afbdb6"
  },
  {
    "number": 7,
    "title": "[T-007] Establish isolated source-distribution acceptance",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 2,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/7",
    "marker": "sdd-forge:task-id=T-007",
    "body_sha256": "18ae9be63f7cadd13d28765d3e6bca5e6b10a533c709fb6463dc9ab5e1413082"
  },
  {
    "number": 8,
    "title": "[T-008] Review, test and report milestone 1.2",
    "state": "closed",
    "state_reason": "completed",
    "milestone": 2,
    "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/8",
    "marker": "sdd-forge:task-id=T-008",
    "body_sha256": "574d99635fcc7e88918799e761562ddf30de13020155546883f0613d2bfc732d"
  }
]


## Command

```sh
PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
from pathlib import Path
import os,re,subprocess,sys,tempfile,tarfile
from textstats import TextStats,count_text
assert count_text('alpha beta\r\ngamma\r')==TextStats(2,3)
for doc in ('README.md','docs/api.md','docs/module.md'):
 text=Path(doc).read_text()
 for code in re.findall(r'```python\n(.*?)```',text,re.S):exec(code,{})
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if not target.startswith(('http','app:')):assert (Path(doc).parent/target).exists(),target
root=Path.cwd()
env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','PYTHONSTARTUP')}
env.update(PYTHONNOUSERSITE='1',PYTHONDONTWRITEBYTECODE='1')
with tempfile.TemporaryDirectory() as d:
 p=Path(d)
 def run(cwd,*args):return subprocess.run([sys.executable,'-m','textstats',*args],cwd=cwd,env=env,text=True,capture_output=True)
 def check(cwd,args,status,out=None):
  r=run(cwd,*args);assert r.returncode==status,(args,r)
  if out is not None:assert r.stdout==out,(args,r.stdout)
  if status==0:assert not r.stderr,r.stderr
  else:assert r.stderr and 'Traceback' not in r.stderr and not r.stdout
 for name,data,args,out in [('sample.txt',b'alpha beta\ngamma\n',[],'lines=2 words=3\n'),('bom.txt',b'\xef\xbb\xbf\n',[],'lines=1 words=0\n'),('bom.txt',b'\xef\xbb\xbf\n',['--keep-bom'],'lines=1 words=1\n'),('-sample.txt',b'alpha\n',['--'],'lines=1 words=1\n')]:
  path=p/name;path.write_bytes(data);check(root,[*args,str(path)],0,out);assert path.read_bytes()==data
 check(root,['--help'],0)
 check(root,[str(p/'nonexistent.txt')],1,'')
 bad=p/'bad.txt';bad.write_bytes(b'valid\xff');check(root,[str(bad)],1,'');assert bad.read_bytes()==b'valid\xff'
 b=subprocess.run(['make','dist',f'DIST_DIR={p}/dist'],capture_output=True,text=True);assert b.returncode==0,b.stderr
 extracted=p/'extracted';extracted.mkdir()
 with tarfile.open(p/'dist/textstats.tar.gz') as archive:archive.extractall(extracted,filter='data')
 identity=subprocess.run([sys.executable,'-c','import textstats;print(textstats.__file__)'],cwd=extracted,env=env,text=True,capture_output=True)
 assert Path(identity.stdout.strip()).resolve()==extracted/'textstats/__init__.py'
 check(extracted,['--help'],0)
 (extracted/'sample.txt').write_bytes(b'alpha beta\ngamma\n');check(extracted,['sample.txt'],0,'lines=2 words=3\n')
print('PASS: README/API/module Python examples, local links, normal/BOM/keep-BOM/dash/help/failure demonstrations; isolated distribution identity and module counts.')
PY
```

Exit 0
```text
PASS: README/API/module Python examples, local links, normal/BOM/keep-BOM/dash/help/failure demonstrations; isolated distribution identity and module counts.
```

## Command

```sh
git diff --stat main...HEAD && git log --oneline main..HEAD
```

Exit 0
```text
.gitignore                             |   1 +
 Makefile                               |  13 ++++
 README.md                              |  55 ++++++++++++++-
 docs/api.md                            |  38 +++++++++++
 docs/dev/TASKS-REVIEW-REPORT.md        |   8 ++-
 docs/dev/TASKS.md                      |  38 ++++++++---
 docs/dev/reports/phases/1/1.1.md       |  45 +++++++++++++
 docs/dev/reports/phases/1/1.2.md       |  50 ++++++++++++++
 docs/module.md                         |  33 +++++++++
 tests/__init__.py                      |   1 +
 tests/integration/__init__.py          |   1 +
 tests/integration/test_cli.py          |  74 ++++++++++++++++++++
 tests/integration/test_distribution.py |  80 ++++++++++++++++++++++
 tests/integration/test_file_api.py     |  60 +++++++++++++++++
 tests/unit/__init__.py                 |   1 +
 tests/unit/test_cli.py                 |  38 +++++++++++
 tests/unit/test_core.py                | 120 +++++++++++++++++++++++++++++++++
 tests/unit/test_file_api.py            |  54 +++++++++++++++
 textstats/__init__.py                  |   6 ++
 textstats/__main__.py                  |   6 ++
 textstats/cli.py                       |  34 ++++++++++
 textstats/core.py                      |  52 ++++++++++++++
 textstats/io.py                        |  26 +++++++
 23 files changed, 821 insertions(+), 13 deletions(-)
dec4ca1 Reconcile milestone 1.2 closure and suspend after T-008
3256b95 Review reliable documented distribution milestone (T-008)
7939e1c Reconcile source-example warning and extraction evidence (T-007)
b686559 Verify isolated standard-library source distribution (T-007)
a436d3a Deliver atomic CLI diagnostics and public guides (T-006)
386c140 Verify named-file failure atomicity and lifecycle (T-005)
159c662 Reconcile verified milestone 1.1 completion and pause (T-004)
fc3a0ec Clarify binary-mode review evidence for milestone 1.1 (T-004)
7bfadcb Review and report named-file MVP milestone 1.1 (T-004)
f2260a2 Deliver useful named-file module CLI (T-003)
299670c Integrate strict UTF-8 named-file API (T-002)
9b24dbd Establish immutable statistics and pure text counting (T-001)
d009899 Enable maintained phase 1 GitHub tracking
```

## Command

```sh
sha256sum docs/dev/PROJECT.md docs/dev/ARCHITECTURE.md docs/dev/DECOMPOSITION.md docs/dev/SPEC.md docs/dev/PLAN.md docs/dev/layout.md
```

Exit 0
```text
85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24  docs/dev/PROJECT.md
0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c  docs/dev/ARCHITECTURE.md
d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d  docs/dev/DECOMPOSITION.md
8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb  docs/dev/SPEC.md
8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8  docs/dev/PLAN.md
ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d  docs/dev/layout.md
```

## Command

```sh
git diff 4c275cc -- textstats-run-resources AGENTS.md docs/dev/PROJECT.md docs/dev/SPEC.md docs/dev/PLAN.md docs/dev/ARCHITECTURE.md docs/dev/DECOMPOSITION.md docs/dev/layout.md
```

Exit 0
```text

```

## Command

```sh
sed -n '53,61p' docs/dev/TASKS.md
```

Exit 0
```text
Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.
            Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
            Completion evidence (2026-10-04): [milestone report](reports/phases/1/1.2.md) covers separate full implementation review at 7939e1c, fresh unit17/integration9 without skips, all public examples, useful normal/missing/malformed diagnostics and independent extracted-source invocation. Every PLAN1.2 exit verified; original T-007 runner/evidence failures and correction retained, no unresolved product finding/TODO. Python3.12.14 tested; no3.11 execution claim. Issue #8 exact title/marker confirmed; issue/milestone closure and local parent reconciliation follow report publication.
    - [ ] Milestone 1.3 — Phase 1 review
        - [ ] T-009 — Review, test and report phase 1
            Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
            Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.

## Phase 2 — Output and source extensions
```

## Command

```sh
git diff --check && git diff -- docs/dev/TASKS.md && git status --short
```

Exit 0
```text
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index 69de283..eb49d77 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,6 +1,6 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-008 are implemented and verified below; the remaining tasks are planned and incomplete. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-009 are implemented and verified below; Phase 2 tasks remain planned and incomplete. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
 
 ## Hosted tracking
 
@@ -54,9 +54,10 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
             Completion evidence (2026-10-04): [milestone report](reports/phases/1/1.2.md) covers separate full implementation review at 7939e1c, fresh unit17/integration9 without skips, all public examples, useful normal/missing/malformed diagnostics and independent extracted-source invocation. Every PLAN1.2 exit verified; original T-007 runner/evidence failures and correction retained, no unresolved product finding/TODO. Python3.12.14 tested; no3.11 execution claim. Issue #8 exact title/marker confirmed; issue/milestone closure and local parent reconciliation follow report publication.
     - [ ] Milestone 1.3 — Phase 1 review
-        - [ ] T-009 — Review, test and report phase 1
+        - [x] T-009 — Review, test and report phase 1
             Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
             Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.
+            Completion evidence (2026-10-04): [phase review report](reports/phases/1/PHASE-REPORT.md) inspects all production/test/docs/build source at dec4ca1 against S-1–S-4 and delivered S-7; no findings or TODOs. Fresh independent unit17/integration9 passed with no skips; public Python examples/local links, exact normal/BOM/keep-BOM/dash/help/failure demonstrations and isolated extracted-source identity/counts passed. Diff check clean; prior RED/GREEN provenance retained with no new behavior change. #1–#8 exact title/marker and closed/completed state confirmed; milestones #1/#2 closed with zero open/four closed issues. #9 exact title/marker confirmed. Task report/status publication precedes #9/milestone3 closure and final parent/integration reconciliation; Phase2 remains unselected.
 
 ## Phase 2 — Output and source extensions
 
 M docs/dev/TASKS.md
?? docs/dev/reports/phases/1/PHASE-REPORT.md
```

## Command

```sh
git add docs/dev/TASKS.md docs/dev/reports/phases/1/PHASE-REPORT.md && git diff --cached --stat && git diff --cached --check
```

Exit 0
```text
docs/dev/TASKS.md                         |  5 ++--
 docs/dev/reports/phases/1/PHASE-REPORT.md | 44 +++++++++++++++++++++++++++++++
 2 files changed, 47 insertions(+), 2 deletions(-)
```

## Command

```sh
git commit -m 'Review and report completed named-file phase (T-009)' -m 'Verify S-1 through S-4 and delivered S-7 with 17 unit and 9 integration tests, examples and isolated distribution. No findings. Closes #9.'
```

Exit 0
```text
[phase/1-named-file-utility cb9d56a] Review and report completed named-file phase (T-009)
 2 files changed, 47 insertions(+), 2 deletions(-)
 create mode 100644 docs/dev/reports/phases/1/PHASE-REPORT.md
```

## Command

```sh
git show --stat --oneline HEAD && git status --short
```

Exit 0
```text
cb9d56a Review and report completed named-file phase (T-009)
 docs/dev/TASKS.md                         |  5 ++--
 docs/dev/reports/phases/1/PHASE-REPORT.md | 44 +++++++++++++++++++++++++++++++
 2 files changed, 47 insertions(+), 2 deletions(-)
```

## Command

```sh
git push origin phase/1-named-file-utility
```

Exit 0
```text
To https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004.git
   dec4ca1..cb9d56a  phase/1-named-file-utility -> phase/1-named-file-utility
```

## Command

```sh
git ls-remote origin refs/heads/phase/1-named-file-utility
```

Exit 0
```text
cb9d56ab4060483cd2240cb9553f43f850196968	refs/heads/phase/1-named-file-utility
```

## Command

```sh
python .git/textstats-hosting-curl.py GET issues/9
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9","id":5700128035,"number":9,"title":"[T-009] Review, test and report phase 1","labels":[{"id":12538641934,"name":"sdd-phase-1-Named-file-utility","color":"1d76db"}],"state":"open","milestone":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":1,"closed_issues":0,"state":"open"},"state_reason":null}}
```

## Command

```sh
python .git/textstats-hosting-curl.py POST issues/9/comments /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-006/2/issue9-evidence.json
```

Exit 0
```text
{"transport":"curl","http_status":201,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9#issuecomment-5983966503","id":5983966503}}
```

## Command

```sh
python .git/textstats-hosting-curl.py PATCH issues/9 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-006/2/issue9-close.json
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9","id":5700128035,"number":9,"title":"[T-009] Review, test and report phase 1","labels":[{"id":12538641934,"name":"sdd-phase-1-Named-file-utility","color":"1d76db"}],"state":"closed","milestone":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":0,"closed_issues":1,"state":"open"},"state_reason":"completed"}}
```

## Command

```sh
python .git/textstats-hosting-curl.py GET issues/9
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9","id":5700128035,"number":9,"title":"[T-009] Review, test and report phase 1","labels":[{"id":12538641934,"name":"sdd-phase-1-Named-file-utility","color":"1d76db"}],"state":"closed","milestone":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":0,"closed_issues":1,"state":"open"},"state_reason":"completed"}}
```

## Command

```sh
python .git/textstats-hosting-curl.py GET 'issues?state=all&milestone=3&per_page=100'
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":[{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9","id":5700128035,"number":9,"title":"[T-009] Review, test and report phase 1","labels":[{"id":12538641934,"name":"sdd-phase-1-Named-file-utility","color":"1d76db"}],"state":"closed","milestone":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":0,"closed_issues":1,"state":"open"},"state_reason":"completed"}]}
```

## Command

```sh
python .git/textstats-hosting-curl.py PATCH milestones/3 /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-006/2/milestone3-close.json
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":0,"closed_issues":1,"state":"closed"}}
```

## Command

```sh
python .git/textstats-hosting-curl.py GET milestones/3
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":{"html_url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3","id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","open_issues":0,"closed_issues":1,"state":"closed"}}
```

## Command

```sh
git diff --check && git diff --stat && git diff -- docs/dev/TASKS.md
```

Exit 0
```text
docs/dev/TASKS.md                         | 12 +++++++-----
 docs/dev/reports/phases/1/PHASE-REPORT.md |  4 ++++
 2 files changed, 11 insertions(+), 5 deletions(-)
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index eb49d77..927ba1f 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,16 +1,17 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-009 are implemented and verified below; Phase 2 tasks remain planned and incomplete. Maintained GitHub tracking is enabled for this repository; phase 1 is projected and ready for separately authorized implementation. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-009 are implemented and verified below; Phase 2 tasks remain planned and incomplete. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
 
 ## Hosted tracking
 
-Mode: maintained GitHub tracking in [pchemguy/Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004). The eligible phase 1 label, native milestones 1.1–1.3 and task issues T-001–T-009 are projected. Milestones 1.1 and 1.2 are verified complete and closed; milestone 1.3 remains open. Task issue closure follows verified durable completion. Reconcile the eligible maintained scope before execution and lifecycle transitions; hosted state never establishes completion. Phase 2 projection waits for phase 1 completion, review, verified integration into main and publication.
+Mode: maintained GitHub tracking in [pchemguy/Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004). The eligible phase 1 label, native milestones 1.1–1.3 and task issues T-001–T-009 are projected. Milestones 1.1–1.3 are verified complete and closed. Task issue closure follows verified durable completion. Reconcile the eligible maintained scope before execution and lifecycle transitions; hosted state never establishes completion. Phase 2 projection waits for phase 1 completion, review, verified integration into main and publication.
 
-Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`; activation baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. The tracking checkpoint at `d009899e39790c39be32ae77e7fe8294bf60d04c` preceded implementation. The milestone 1.1 checkpoint below is historical. The current milestone 1.2 suspension checkpoint pauses on this branch without phase review or integration.
+Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`; activation baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. The tracking checkpoint at `d009899e39790c39be32ae77e7fe8294bf60d04c` preceded implementation. The milestone 1.1 checkpoint below is historical. The milestone 1.2 suspension checkpoint is historical; authorized resumption completed T-009 and all Phase 1 tracking. Integration follows this published completion record.
 
 ## Phase 1 — Named-file utility
 
-- [ ] Phase 1 — Named-file utility
+- [x] Phase 1 — Named-file utility
+    Completion evidence (2026-10-04): T-001–T-009 verified and published; Phase 1 report/status at cb9d56ab4060483cd2240cb9553f43f850196968. Unit17/integration9, cross-component code review, public examples and isolated distribution satisfy PLAN1.3. Issues #1–#9 closed/completed; native milestones #1/#2/#3 read back closed with 0 open and 4/4/1 closed issues. This is local/working-branch acceptance; verified explicit integration and target publication are recorded separately. Stop before Phase2.
     - [x] Milestone 1.1 — Named-file counting MVP
         Completion evidence (2026-10-04): all T-001–T-004 results/status/report committed and published; independent unit 14/integration 6 tests, code review and normal/BOM/dash demo satisfy PLAN 1.1 exits. Issues #1–#4 verified closed with completed reason; milestone #1 read back closed with 0 open/4 closed issues. Phase 1 remains incomplete; this checkpoint pauses without integration.
         - [x] T-001 — Establish immutable statistics and pure text counting
@@ -53,7 +54,8 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.
             Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
             Completion evidence (2026-10-04): [milestone report](reports/phases/1/1.2.md) covers separate full implementation review at 7939e1c, fresh unit17/integration9 without skips, all public examples, useful normal/missing/malformed diagnostics and independent extracted-source invocation. Every PLAN1.2 exit verified; original T-007 runner/evidence failures and correction retained, no unresolved product finding/TODO. Python3.12.14 tested; no3.11 execution claim. Issue #8 exact title/marker confirmed; issue/milestone closure and local parent reconciliation follow report publication.
-    - [ ] Milestone 1.3 — Phase 1 review
+    - [x] Milestone 1.3 — Phase 1 review
+        Completion evidence (2026-10-04): T-009 report/status published at cb9d56a; issue #9 closed/completed with evidence comment 5983966503; exact milestone3 issue listing contains only #9, closed/completed. Milestone #3 read back closed with zero open/one closed issue after preceding delivery closures.
         - [x] T-009 — Review, test and report phase 1
             Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
             Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.
```

## Command

```sh
git add docs/dev/TASKS.md docs/dev/reports/phases/1/PHASE-REPORT.md && git diff --cached --check && git commit -m 'Reconcile verified Phase 1 and final review closure (T-009)'
```

Exit 0
```text
[phase/1-named-file-utility b398e25] Reconcile verified Phase 1 and final review closure (T-009)
 2 files changed, 11 insertions(+), 5 deletions(-)
```

## Command

```sh
git push origin phase/1-named-file-utility
```

Exit 0
```text
To https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004.git
   cb9d56a..b398e25  phase/1-named-file-utility -> phase/1-named-file-utility
```

## Command

```sh
git ls-remote origin refs/heads/phase/1-named-file-utility refs/heads/main
```

Exit 0
```text
4c275cc46fc0163c9e1e50871d3cc33c4c38567e	refs/heads/main
b398e258cefc03dbc47630b83967db961a376eae	refs/heads/phase/1-named-file-utility
```

## Command

```sh
git fetch origin main && git rev-parse HEAD main origin/main && git status --short && git diff --stat main...HEAD
```

Exit 0
```text
From https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004
 * branch            main       -> FETCH_HEAD
b398e258cefc03dbc47630b83967db961a376eae
4c275cc46fc0163c9e1e50871d3cc33c4c38567e
4c275cc46fc0163c9e1e50871d3cc33c4c38567e
 .gitignore                                |   1 +
 Makefile                                  |  13 ++++
 README.md                                 |  55 +++++++++++++-
 docs/api.md                               |  38 ++++++++++
 docs/dev/TASKS-REVIEW-REPORT.md           |   8 +-
 docs/dev/TASKS.md                         |  47 ++++++++----
 docs/dev/reports/phases/1/1.1.md          |  45 +++++++++++
 docs/dev/reports/phases/1/1.2.md          |  50 +++++++++++++
 docs/dev/reports/phases/1/PHASE-REPORT.md |  48 ++++++++++++
 docs/module.md                            |  33 ++++++++
 tests/__init__.py                         |   1 +
 tests/integration/__init__.py             |   1 +
 tests/integration/test_cli.py             |  74 ++++++++++++++++++
 tests/integration/test_distribution.py    |  80 ++++++++++++++++++++
 tests/integration/test_file_api.py        |  60 +++++++++++++++
 tests/unit/__init__.py                    |   1 +
 tests/unit/test_cli.py                    |  38 ++++++++++
 tests/unit/test_core.py                   | 120 ++++++++++++++++++++++++++++++
 tests/unit/test_file_api.py               |  54 ++++++++++++++
 textstats/__init__.py                     |   6 ++
 textstats/__main__.py                     |   6 ++
 textstats/cli.py                          |  34 +++++++++
 textstats/core.py                         |  52 +++++++++++++
 textstats/io.py                           |  26 +++++++
 24 files changed, 875 insertions(+), 16 deletions(-)
```

## Command

```sh
git diff main...HEAD -- docs/dev/TASKS-REVIEW-REPORT.md .gitignore && git diff main...HEAD -- docs/dev/TASKS.md
```

Exit 0
```text
diff --git a/.gitignore b/.gitignore
index 62a87fe..ac5e008 100644
--- a/.gitignore
+++ b/.gitignore
@@ -3,3 +3,4 @@
 .env.*
 __pycache__/
 *.pyc
+dist/
diff --git a/docs/dev/TASKS-REVIEW-REPORT.md b/docs/dev/TASKS-REVIEW-REPORT.md
index 95e22e1..5844daf 100644
--- a/docs/dev/TASKS-REVIEW-REPORT.md
+++ b/docs/dev/TASKS-REVIEW-REPORT.md
@@ -2,7 +2,7 @@
 
 ## Current gate
 
-State: Ready. Owner assessment: sdd-tasks, 2026-10-04. Reviewed root TASKS; no focused children or active feature task list. Current PLAN/SPEC/design identities and upstream reports were checked before derivation. No confirmed issue or material open decision remains. This prepares 17 unchecked executable tasks; it neither selects a range nor activates hosted tracking or implements production code.
+State: Ready. Owner assessment: sdd-tasks, 2026-10-04. Reviewed root TASKS; no focused children or active feature task list. Current PLAN/SPEC/design identities and upstream reports were checked before derivation. No confirmed issue or material open decision remains. This prepares 17 unchecked executable tasks. The current metadata recheck below records separately authorized maintained hosted tracking; no task range is implemented and no production code is delivered.
 
 Reviewed and governing states:
 
@@ -38,3 +38,9 @@ Manually mapped each PLAN outcome/exit to task scope, dependency and concrete ev
 Each delivery milestone ends with explicit code review/testing/repair/report work; final phase review depends on delivery milestone completion/closure, not itself. Review tasks have lifecycle-compliant report paths; T-017 includes final TODO aggregation. Nonzero product discovery, strict decoding, owned/borrowed resource checks, useful human demonstrations and checkout-independent extracted source invocation have executable coverage. Phase integration/publication gates and partial-range pause are preserved. Future range is excluded while the source-independent seam is maintained.
 
 No findings or correction cycle. Preparation stops with all tasks unchecked and no hosted projection.
+
+## Revision 1 — Hosted tracking metadata recheck
+
+Owner assessment: sdd-tasks, 2026-10-04. No finding or correction to the accepted decomposition. The tracking workflow replaces the historical “No hosted objects are active” sentence with maintained mode and phase 1 context. Reviewed TASKS.md SHA-256: `1622d35a0bb4a61034e2b92fa52ed986f99cb54c96b49ff4087155af308df208`.
+
+Compared every phase, milestone and task entry against the initial reviewed source at `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`: hierarchy, scope, dependency, acceptance, prescribed checks and completion checkboxes are byte-for-byte unchanged. All other reviewed/governing inputs retain the hashes above. Counts, grouped PLAN/SPEC coverage and original no-finding assessment remain equivalent. Readiness: Ready for eligible phase 1 projection/implementation only when separately authorized; tracking metadata is not task completion. All 17 tasks remain unchecked. No product tests were run.
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index 4d9f9eb..927ba1f 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,46 +1,65 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. These are planned tasks: none is implemented, verified or complete. No hosted objects are active. Future range implementation is separately requested and has no executable owner here.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-009 are implemented and verified below; Phase 2 tasks remain planned and incomplete. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Future phase 2 remains unprojected. Future range implementation is separately requested and has no executable owner here.
+
+## Hosted tracking
+
+Mode: maintained GitHub tracking in [pchemguy/Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004). The eligible phase 1 label, native milestones 1.1–1.3 and task issues T-001–T-009 are projected. Milestones 1.1–1.3 are verified complete and closed. Task issue closure follows verified durable completion. Reconcile the eligible maintained scope before execution and lifecycle transitions; hosted state never establishes completion. Phase 2 projection waits for phase 1 completion, review, verified integration into main and publication.
+
+Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`; activation baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. The tracking checkpoint at `d009899e39790c39be32ae77e7fe8294bf60d04c` preceded implementation. The milestone 1.1 checkpoint below is historical. The milestone 1.2 suspension checkpoint is historical; authorized resumption completed T-009 and all Phase 1 tracking. Integration follows this published completion record.
 
 ## Phase 1 — Named-file utility
 
-- [ ] Phase 1 — Named-file utility
-    - [ ] Milestone 1.1 — Named-file counting MVP
-        - [ ] T-001 — Establish immutable statistics and pure text counting
+- [x] Phase 1 — Named-file utility
+    Completion evidence (2026-10-04): T-001–T-009 verified and published; Phase 1 report/status at cb9d56ab4060483cd2240cb9553f43f850196968. Unit17/integration9, cross-component code review, public examples and isolated distribution satisfy PLAN1.3. Issues #1–#9 closed/completed; native milestones #1/#2/#3 read back closed with 0 open and 4/4/1 closed issues. This is local/working-branch acceptance; verified explicit integration and target publication are recorded separately. Stop before Phase2.
+    - [x] Milestone 1.1 — Named-file counting MVP
+        Completion evidence (2026-10-04): all T-001–T-004 results/status/report committed and published; independent unit 14/integration 6 tests, code review and normal/BOM/dash demo satisfy PLAN 1.1 exits. Issues #1–#4 verified closed with completed reason; milestone #1 read back closed with 0 open/4 closed issues. Phase 1 remains incomplete; this checkpoint pauses without integration.
+        - [x] T-001 — Establish immutable statistics and pure text counting
             Scope: textstats/core.py, initial public facade, tests/unit/ discovery packages and semantic/value tests. Depends on: reviewed preparation inputs.
             Outcome: direct TextStats/count_text imports, immutable nonnegative fields and exact BOM/CRLF/CR/LF/Unicode-word semantics (S-1/S-2).
             Evidence: nonempty unit discovery; all SPEC sample rows, retained/interior/double BOM, silence and immutability/nonnegative checks. Keep pure core independent of acquisition/process state.
-        - [ ] T-002 — Integrate strict UTF-8 named-file API
+            Completion evidence (2026-10-04, Python 3.12.14, phase/1-named-file-utility; task-owned diff from d009899): `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` passed 12 tests with no skips. All 11 SPEC sample rows, 5 additional terminator boundaries, 7 Unicode whitespace separators, 7 BOM interactions, signature/default, silence, input preservation, frozen fields and invalid/zero counts are covered. RED observed missing TextStats export (1 failure), invalid counts (11 failing subtests), missing count_text export (1 failure), and unimplemented semantics (28 failing subtests); each became GREEN after its corresponding implementation. A separate acceptance discovery/run and direct public-import example passed; `git diff --check` was clean. Core inspection confirms only standard-library dataclass dependency and no acquisition/process behavior. Module/API docstrings reviewed; README capability statement aligned. Issue uniquely resolved as pchemguy/Skill-Test-SDD-Manager-TextStats-20261004#1 by exact title and task marker. No T-002 work, integration tests, CLI, distribution or milestone/phase review is claimed.
+        - [x] T-002 — Integrate strict UTF-8 named-file API
             Scope: textstats/io.py, facade exports, focused unit/file integration checks and tests/integration/ discovery packages. Depends on: T-001.
             Outcome: count_file supports str/PathLike, preserves input terminators, delegates counts and closes its success-path owned handle (S-3 success).
             Evidence: direct package API import/signatures; real temporary files for BOM/newline/empty/Unicode cases; unchanged input; silent calls and success-handle closure. Required failure-path hardening follows in T-005.
-        - [ ] T-003 — Deliver the useful named-file module CLI
+            Completion evidence (2026-10-04): focused test-first run observed 3 missing-export assertion failures before implementation, then 3 passing tests. Independent `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` passed 13 tests; integration discovery passed 2 tests. Real str/Path files, strict binary UTF-8 acquisition, BOM/terminator/Unicode cases, exact signatures, silence, unchanged bytes and owned success closure covered. Module/API docstrings and README capability reviewed; no failure-hardening acceptance is claimed. Issue #2 exact title/body marker uniquely confirmed; diff check clean.
+        - [x] T-003 — Deliver the useful named-file module CLI
             Scope: textstats/cli.py, textstats/__main__.py and integration subprocess checks. Depends on: T-001, T-002.
             Outcome: one named input, --keep-bom, -- dash filenames and help; exact text output and option validation before acquisition (S-4 success/options).
             Evidence: actual python -m textstats invocation, stdout/status/stderr assertions, API/CLI agreement, missing/extra/unknown option rejection and no input read on usage errors; demonstrate ordinary/BOM/dash filenames. Keep later JSON/stdin delivery absent from this task.
-        - [ ] T-004 — Review, test and report milestone 1.1
+            Completion evidence (2026-10-04): focused RED observed missing command adapter and absent actual module-entry behavior (12 assertion/subtest failures across 5 tests), then GREEN passed all 5. Independent unit discovery passed 14 tests; integration passed 6, no skips. Actual subprocess checks establish exact stdout/stderr/status, ordinary/empty/Unicode/mixed-terminator/BOM cases, API agreement, --keep-bom and -- dash paths; invalid usage/help never acquire input. A separate normal/BOM/dash demonstration and README/module docstring review passed; diff check clean. Issue #3 exact title/body marker confirmed. Diagnostic hardening remains T-006; no JSON/stdin or release acceptance claimed.
+        - [x] T-004 — Review, test and report milestone 1.1
             Depends on: T-001, T-002, T-003. Scope: delivered core, file API, facade and module CLI; relevant nonempty product suites and MVP demonstration.
             Evidence: actual code review, milestone exits/regressions, blocker repairs and committed/pushed report. Report: docs/dev/reports/phases/1/1.1.md. Record TODO or None and the usability decision evidence. No product completion inferred from workflow fixtures.
-    - [ ] Milestone 1.2 — Reliable documented distribution
-        - [ ] T-005 — Harden named-file API failure and resource behavior
+            Completion evidence (2026-10-04): [milestone review report](reports/phases/1/1.1.md) assesses all delivered modules and test coverage at f2260a2; no in-scope findings or TODOs. Fresh independent product discovery passed unit 14/integration 6 tests, no skips; direct normal/BOM/dash API/module demonstration and help passed, diff check clean. PLAN 1.1 exits verified; reliability/distribution and full phase acceptance remain unclaimed. Issue #4 exact title/body marker confirmed.
+    - [x] Milestone 1.2 — Reliable documented distribution
+        Completion evidence (2026-10-04): T-005–T-008 result/status/report commits published; independent unit17/integration9, code review, examples/diagnostics and isolated distribution satisfy PLAN1.2. Issues #5–#8 read back closed/completed; milestone #2 closed with zero open/four closed issues. Human gradual suspension arrived during T-008 publication; finish only its reconciliation and stop. T-009/phase integration not started; Phase2 remains unprojected and unimplemented.
+        - [x] T-005 — Harden named-file API failure and resource behavior
             Scope: textstats/io.py and focused unit/integration failures. Depends on: T-004.
             Outcome: missing/unreadable files propagate OSError subclasses, strict bad-byte decoding raises UnicodeDecodeError, failure calls are silent, input unchanged, owned handles closed and no partial result (S-3).
             Evidence: real missing/bad-byte files plus portable injected unreadable/read/close seams; both BOM policies; byte-for-byte preservation and owned-handle success/failure checks. Do not rely solely on permission bits under privileged execution.
-        - [ ] T-006 — Complete CLI diagnostics and public documentation
+            Completion evidence (2026-10-04): existing binary context-managed acquisition already satisfies S-3; characterization tests added before any production edit passed after correcting a test import NameError (setup error, not behavioral RED). No production change or manufactured RED. Real missing/directory/malformed files, both BOM policies, open/read/decode/close failures, silent exception propagation, no returned partial value, unchanged bytes and closed owned handles verified. Focused 6 tests, independent unit 16/integration 7 passed with no skips; diff check clean. Existing API docstring reviewed against exceptions/lifetime. Issue #5 uniquely matched exact title and body marker; test-first cycle explicitly permits already-passing existing behavior.
+        - [x] T-006 — Complete CLI diagnostics and public documentation
             Scope: textstats/cli.py, docs/api.md, docs/module.md, README.md and relevant unit/integration checks. Depends on: T-005.
             Outcome: useful input-identifying expected-error diagnostics, statuses 1/2, empty stdout/no traceback, retained help/options/success and documented runnable phase 1 API/module usage (S-4 and S-7 docs).
             Evidence: actual module missing/read/decode failures, invalid invocation before acquisition, unchanged files; run documented API/help/text/BOM examples. Preserve original README content and SDD links.
-        - [ ] T-007 — Establish isolated source-distribution acceptance
+            Completion evidence (2026-10-04): focused RED before production edits had 8 unhandled expected-error subtests and 6 real module diagnostic failures; GREEN passed both tests after narrow OSError/UnicodeDecodeError translation. Independent unit 17/integration 8 passed with no skips; retained options/help/validation-before-acquisition and exact success regressions pass. Real missing/directory/bad UTF-8, injected permission/read failures and both BOM policies return 1 with identifying stderr, empty stdout/no traceback; bytes unchanged. README original heading/focus/SDD links retained; public API and module guides/docstring reviewed. All Python/shell API/help/text/BOM/dash/failure examples executed in temporary directories with exact count/status assertions; local links valid; diff check clean. No JSON/stdin delivered. Issue #6 exact title/marker confirmed.
+        - [x] T-007 — Establish isolated source-distribution acceptance
             Scope: Makefile, generated-output ignore rules and tests/integration distribution checks. Depends on: T-006.
             Outcome: standard-library source archive includes importable package, README and public docs; generated dist/extractions stay untracked (S-7).
             Evidence: build/extract to temporary root; invoke extracted python -m textstats with a clean import environment from that root; check exact named-file counts, --keep-bom, help and representative failure status. Independently discover nonzero unit/integration suites and run README examples. Keep workflow fixtures separate and pinned resources unchanged.
-        - [ ] T-008 — Review, test and report milestone 1.2
+            Completion evidence (2026-10-04): RED source-distribution test observed missing make dist target before build implementation; GREEN passes isolated standard-library build/extraction with cleansed PYTHONPATH/PYTHONHOME/PYTHONSTARTUP, disabled user site and exact extracted __file__ assertion. Package/public docs/README/build recipe/tests included; workflow resources, caches and generated outputs excluded; dist ignored. Normal/empty/Unicode/BOM/keep-BOM text, help, missing/malformed/usage/unknown JSON errors and unchanged input verified. Independent unit17/integration9 passed, no skips. README/API/module examples rerun, including actual build/extract/help sequence with checkout import settings removed (initial temporary-cwd example runner failure corrected, not a product defect). A second example-runner assertion rejected a successful extraction solely for Python 3.12 tarfile deprecation stderr; corrected the runner to distinguish this known warning from failed commands, then reran all examples successfully. Test extraction now requests the data filter when available, with a validated-path fallback for earlier Python 3.11. This is a correction to the premature example-pass assertion in b686559; all previous failures remain recorded. Independent unit17/integration9 and example checks rerun successfully, no skips; diff check clean. Issue #7 exact title/marker confirmed.
+        - [x] T-008 — Review, test and report milestone 1.2
             Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.
             Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
-    - [ ] Milestone 1.3 — Phase 1 review
-        - [ ] T-009 — Review, test and report phase 1
+            Completion evidence (2026-10-04): [milestone report](reports/phases/1/1.2.md) covers separate full implementation review at 7939e1c, fresh unit17/integration9 without skips, all public examples, useful normal/missing/malformed diagnostics and independent extracted-source invocation. Every PLAN1.2 exit verified; original T-007 runner/evidence failures and correction retained, no unresolved product finding/TODO. Python3.12.14 tested; no3.11 execution claim. Issue #8 exact title/marker confirmed; issue/milestone closure and local parent reconciliation follow report publication.
+    - [x] Milestone 1.3 — Phase 1 review
+        Completion evidence (2026-10-04): T-009 report/status published at cb9d56a; issue #9 closed/completed with evidence comment 5983966503; exact milestone3 issue listing contains only #9, closed/completed. Milestone #3 read back closed with zero open/one closed issue after preceding delivery closures.
+        - [x] T-009 — Review, test and report phase 1
             Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
             Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.
+            Completion evidence (2026-10-04): [phase review report](reports/phases/1/PHASE-REPORT.md) inspects all production/test/docs/build source at dec4ca1 against S-1–S-4 and delivered S-7; no findings or TODOs. Fresh independent unit17/integration9 passed with no skips; public Python examples/local links, exact normal/BOM/keep-BOM/dash/help/failure demonstrations and isolated extracted-source identity/counts passed. Diff check clean; prior RED/GREEN provenance retained with no new behavior change. #1–#8 exact title/marker and closed/completed state confirmed; milestones #1/#2 closed with zero open/four closed issues. #9 exact title/marker confirmed. Task report/status publication precedes #9/milestone3 closure and final parent/integration reconciliation; Phase2 remains unselected.
 
 ## Phase 2 — Output and source extensions
```

## Command

```sh
git merge-base --is-ancestor b398e258cefc03dbc47630b83967db961a376eae main
```

Exit 1
```text

```

## Command

```sh
git switch main && git merge --no-ff --no-commit b398e258cefc03dbc47630b83967db961a376eae
```

Exit 0
```text
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
Automatic merge went well; stopped before committing as requested
```

## Command

```sh
git diff --cached --check && git status --short
```

Exit 0
```text
M  .gitignore
A  Makefile
M  README.md
A  docs/api.md
M  docs/dev/TASKS-REVIEW-REPORT.md
M  docs/dev/TASKS.md
A  docs/dev/reports/phases/1/1.1.md
A  docs/dev/reports/phases/1/1.2.md
A  docs/dev/reports/phases/1/PHASE-REPORT.md
A  docs/module.md
A  tests/__init__.py
A  tests/integration/__init__.py
A  tests/integration/test_cli.py
A  tests/integration/test_distribution.py
A  tests/integration/test_file_api.py
A  tests/unit/__init__.py
A  tests/unit/test_cli.py
A  tests/unit/test_core.py
A  tests/unit/test_file_api.py
A  textstats/__init__.py
A  textstats/__main__.py
A  textstats/cli.py
A  textstats/core.py
A  textstats/io.py
```

## Command

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v
```

Exit 0
```text
test_expected_errors_are_identified_and_atomic (tests.unit.test_cli.CliFailureTests.test_expected_errors_are_identified_and_atomic) ... ok
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
test_open_failure_is_silent_and_preserves_exception (tests.unit.test_file_api.FileFailureTests.test_open_failure_is_silent_and_preserves_exception) ... ok
test_read_decode_and_close_failure_are_atomic_and_close_owned_handle (tests.unit.test_file_api.FileFailureTests.test_read_decode_and_close_failure_are_atomic_and_close_owned_handle) ... ok
test_success_closes_owned_handle (tests.unit.test_file_api.FileLifecycleTests.test_success_closes_owned_handle) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.009s

OK
```

## Command

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v
```

Exit 0
```text
test_help (tests.integration.test_cli.ModuleCliTests.test_help) ... ok
test_invalid_invocations (tests.integration.test_cli.ModuleCliTests.test_invalid_invocations) ... ok
test_keep_bom_and_dash_prefixed_filename (tests.integration.test_cli.ModuleCliTests.test_keep_bom_and_dash_prefixed_filename) ... ok
test_named_files_counts_and_api_agreement (tests.integration.test_cli.ModuleCliTests.test_named_files_counts_and_api_agreement) ... ok
test_expected_file_failures (tests.integration.test_cli.ModuleFailureTests.test_expected_file_failures) ... ok
test_extracted_package_public_docs_and_module_contract (tests.integration.test_distribution.SourceDistributionTests.test_extracted_package_public_docs_and_module_contract) ... ok
test_public_export_and_signature (tests.integration.test_file_api.FileApiTests.test_public_export_and_signature) ... ok
test_real_files_paths_bom_terminators_and_silence (tests.integration.test_file_api.FileApiTests.test_real_files_paths_bom_terminators_and_silence) ... ok
test_real_missing_directory_and_malformed_files_are_silent_and_unchanged (tests.integration.test_file_api.FileFailureIntegrationTests.test_real_missing_directory_and_malformed_files_are_silent_and_unchanged) ... ok

----------------------------------------------------------------------
Ran 9 tests in 1.211s

OK
```

## Command

```sh
git add docs/dev/reports/phases/1/PHASE-REPORT.md && git diff --cached --check && git diff --cached --stat
```

Exit 0
```text
.gitignore                                |   1 +
 Makefile                                  |  13 ++++
 README.md                                 |  55 +++++++++++++-
 docs/api.md                               |  38 ++++++++++
 docs/dev/TASKS-REVIEW-REPORT.md           |   8 +-
 docs/dev/TASKS.md                         |  47 ++++++++----
 docs/dev/reports/phases/1/1.1.md          |  45 +++++++++++
 docs/dev/reports/phases/1/1.2.md          |  50 +++++++++++++
 docs/dev/reports/phases/1/PHASE-REPORT.md |  52 +++++++++++++
 docs/module.md                            |  33 ++++++++
 tests/__init__.py                         |   1 +
 tests/integration/__init__.py             |   1 +
 tests/integration/test_cli.py             |  74 ++++++++++++++++++
 tests/integration/test_distribution.py    |  80 ++++++++++++++++++++
 tests/integration/test_file_api.py        |  60 +++++++++++++++
 tests/unit/__init__.py                    |   1 +
 tests/unit/test_cli.py                    |  38 ++++++++++
 tests/unit/test_core.py                   | 120 ++++++++++++++++++++++++++++++
 tests/unit/test_file_api.py               |  54 ++++++++++++++
 textstats/__init__.py                     |   6 ++
 textstats/__main__.py                     |   6 ++
 textstats/cli.py                          |  34 +++++++++
 textstats/core.py                         |  52 +++++++++++++
 textstats/io.py                           |  26 +++++++
 24 files changed, 879 insertions(+), 16 deletions(-)
```

## Command

```sh
git commit -m 'Integrate verified Phase 1 named-file utility' -m 'Two-parent integration: target 4c275cc46fc0163c9e1e50871d3cc33c4c38567e; phase b398e258cefc03dbc47630b83967db961a376eae. No conflicts. Merged-state unit 17/integration 9 pass; whitespace check clean. T-001 through T-009 complete; issues 1-9 and milestones 1-3 closed. Stop before Phase 2.'
```

Exit 0
```text
[main 59debb6] Integrate verified Phase 1 named-file utility
```

## Command

```sh
git show --no-patch --format=fuller HEAD && git rev-list --parents -n 1 HEAD && git status --short
```

Exit 0
```text
commit 59debb649545125dd3aa00377ea115451b594271
Merge: 4c275cc b398e25
Author:     Codex <codex@openai.com>
AuthorDate: Sun Oct 4 16:17:54 2026 -0400
Commit:     Codex <codex@openai.com>
CommitDate: Sun Oct 4 16:17:54 2026 -0400

    Integrate verified Phase 1 named-file utility
    
    Two-parent integration: target 4c275cc46fc0163c9e1e50871d3cc33c4c38567e; phase b398e258cefc03dbc47630b83967db961a376eae. No conflicts. Merged-state unit 17/integration 9 pass; whitespace check clean. T-001 through T-009 complete; issues 1-9 and milestones 1-3 closed. Stop before Phase 2.
59debb649545125dd3aa00377ea115451b594271 4c275cc46fc0163c9e1e50871d3cc33c4c38567e b398e258cefc03dbc47630b83967db961a376eae
```

## Command

```sh
git push origin main
```

Exit 0
```text
To https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004.git
   4c275cc..59debb6  main -> main
```

## Command

```sh
git ls-remote origin refs/heads/main refs/heads/phase/1-named-file-utility
```

Exit 0
```text
59debb649545125dd3aa00377ea115451b594271	refs/heads/main
b398e258cefc03dbc47630b83967db961a376eae	refs/heads/phase/1-named-file-utility
```

## Command

```sh
git merge-base --is-ancestor b398e258cefc03dbc47630b83967db961a376eae main && git diff --check && git status --short
```

Exit 0
```text

```

## Command

```sh
python .git/textstats-hosting-curl.py GET 'milestones?state=all&per_page=100'
```

Exit 0
```text
{"transport":"curl","http_status":200,"result":[{"id":18303256,"number":1,"title":"sdd-1.1-Named-file-counting-MVP","state":"closed","open_issues":0,"closed_issues":4,"url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/1"},{"id":18303258,"number":2,"title":"sdd-1.2-Reliable-documented-distribution","state":"closed","open_issues":0,"closed_issues":4,"url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/2"},{"id":18303268,"number":3,"title":"sdd-1.3-Phase-1-review","state":"closed","open_issues":0,"closed_issues":1,"url":"https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/milestone/3"}]}
```

## Final connector issue readback

{
  "number": 9,
  "title": "[T-009] Review, test and report phase 1",
  "state": "closed",
  "state_reason": "completed",
  "milestone": 3,
  "url": "https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/9",
  "comments": 1,
  "marker": "sdd-forge:task-id=T-009",
  "body_sha256": "cd6690eea7a3184b305c806c671ed5a30621cf44f87a20327d21e1e17eccc9f8"
}


No pending effects. Stop before Phase2 activation/projection/execution. Main remote exact merge tip confirmed. Consumer evidence is not committed or pushed.
