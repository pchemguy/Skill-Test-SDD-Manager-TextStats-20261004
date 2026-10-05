# Acceptance incorporation journal

Selected input only: /workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-022/1/REQUEST.md

First authority read: /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md (success, before scope decisions). Prior read-only orientation commands are replayed below for exact retained results. No other coordinator/assessor input read.

### Command ['cat', '/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-022/1/REQUEST.md']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
# Acceptance change

Incorporate the selected revised acceptance requirement Expand the named-file --lines START:END endpoint grammar from ASCII decimal digits to all Unicode decimal digits (Unicode category Nd), including mixed ASCII/Unicode decimal endpoints and leading zeros. For example --lines ١:٢ selects inclusive lines1–2 and --lines １:２ does likewise. Preserve positivity, START<=END, full-input strict UTF-8 decode, BOM policy, existing EOF semantics, single option and usage-before-input; retain rejection of signs, spaces and non-decimal numerals such as ². This revises the delivered CLI acceptance associated with the existing T-019 owner; only incorporate the revised acceptance and report next executable work now. for the current product work, then orient and report the next executable work. Do not implement a newly selected task.

## Actual product current state and authorization

Use isolated existing worktree /workspace/scratch/textstats-acceptance-change-worktree-20261005, branch trial/a022-acceptance-change at0e4741465c3e086d2ab95c5af73ca89371c16fac. The named-file range feature is delivered, T-019 is checked, and phase2 remains incomplete. Inspect current product authorities and evidence. Only this isolated trial is selected: governing acceptance incorporation and next-work orientation; no production/test edits or implementation. Authorized publication destination is absolute local bare URL /workspace/scratch/textstats-acceptance-change-remote-20261005.git; publish owned document results there with exact ref readback. Do not use origin for publication, mutate shared origin/config, integrate into live branches, or perform hosted operations. Follow product AGENTS and immutable textstats-run-resources/plugin/skills at019eb354cf0921ebd6056e6579763ac33d0baec2. Before authority decisions read pinned sdd-manage/references/revision-authorization.md. Actual human full campaign GO and Resume authorize this bounded isolated trial; local-only scope controls effects. No clones/reset/stash/cleanup/forcepush, credential/helper source inspection, frozen-package edits or /pyenv access.

```

Exit: 0

### Command ['git', '--no-optional-locks', 'rev-parse', '--show-toplevel']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
/workspace/scratch/textstats-acceptance-change-worktree-20261005

```

Exit: 0

### Command ['git', '--no-optional-locks', 'rev-parse', 'HEAD']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
0e4741465c3e086d2ab95c5af73ca89371c16fac

```

Exit: 0

### Command ['git', '--no-optional-locks', 'branch', '--show-current']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
trial/a022-acceptance-change

```

Exit: 0

### Command ['git', '--no-optional-locks', 'status', '--porcelain=v1', '--untracked-files=all']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'log', '-8', '--format=%H %P %s']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
0e4741465c3e086d2ab95c5af73ca89371c16fac ea97182d2d6a3984599238312a13e78d54d3221a d518cc23650018542e43d8fb5a63f44a4d283518 Merge named-file line ranges into paused phase 2
d518cc23650018542e43d8fb5a63f44a4d283518 3f93cd40d90001ee7e4f54b36c764d1d5067b72e Conclude range feature and archive accepted sources (T-022)
3f93cd40d90001ee7e4f54b36c764d1d5067b72e 749a89844249d3b1c5ebb04c459d7e66bcb3ed2e Review range milestone and incorporate governing owners (T-021)
749a89844249d3b1c5ebb04c459d7e66bcb3ed2e 9ade315a9f6ded1fade6f457a504f5e07e58fba5 Document ranges and verify extracted sources (T-020)
9ade315a9f6ded1fade6f457a504f5e07e58fba5 905d7a851124235db27f4f5a553ee39729957a44 Deliver validated named-file range text and JSON (T-019)
905d7a851124235db27f4f5a553ee39729957a44 89664adb46b70e66d99445e28a04e8f53760fa02 Establish normalized logical-line selection (T-018)
89664adb46b70e66d99445e28a04e8f53760fa02 152fb8f6ab316e4bd893aeea8d2dc03b96fbb3a9 Retain original preparation QC identity history
152fb8f6ab316e4bd893aeea8d2dc03b96fbb3a9 53da8a9dbbe9fccdc1fcc24fffec29079912a247 Incorporate range delivery owners and recheck document readiness

```

Exit: 0

### Command ['git', '--no-optional-locks', 'ls-remote', '/workspace/scratch/textstats-acceptance-change-remote-20261005.git']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
0e4741465c3e086d2ab95c5af73ca89371c16fac	refs/heads/trial/a022-acceptance-change

```

Exit: 0

### Command ['git', '--no-optional-locks', 'ls-tree', 'HEAD', 'textstats-run-resources']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
040000 tree 5a0f908a405f7b3d0213c505525a7c1ca1c7e745	textstats-run-resources

```

Exit: 0

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/AGENTS.md

SHA-256: `d7dabe4ba00c81bc17d15c6b2ef05c10beadc583a156776800d39f803592761e`

```text
This is a dedicated SDD Manager plugin test repository. Follow the pinned skills in textstats-run-resources/plugin/skills. Product documents and implementation must be generated through the authorized consumer workflows. Credentials remain protected and outside evidence.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/SDD-MANAGER.md

SHA-256: `07947f37a7a69fdfe45331d51e46d21267297e9fc547c84448949e711469403b`

```text
# SDD Manager usage

This repository uses [SDD Manager](https://github.com/pchemguy/Skill-SDD-Manager), a plugin for specification-driven development, to assist its development workflow: project exploration and design, specifications, plans, task lists, implementation, verification, and reporting. Actual use is bounded by the accepted project scope and recorded development evidence; this notice does not claim that every workflow stage has been executed.

See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for the AI-assisted development disclosure. The project maintainer remains responsible for the published work. Use of SDD Manager does not imply endorsement or certification by its author.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/AI_DISCLOSURE.md

SHA-256: `09411dc61f4966efabe8e821f2270c768baf5b96f4fd4587eb5c05233de7ffea`

```text
# AI-Assisted Development Disclosure

This project has been developed with extensive assistance from generative AI, primarily OpenAI ChatGPT. AI assistance was used throughout both code and documentation development, including project exploration, design discussion, specification development, implementation, test generation, technical review, and prose drafting and revision.

The project has been developed under human direction, and responsibility for the published code, documentation, design decisions, and any remaining errors rests with the project maintainer. Users should review and validate the implementation for their own requirements, particularly before relying on it in production or other correctness-sensitive applications.

## README.md Warning Template

> [!IMPORTANT]
> 
> **AI-Assisted Development Disclosure**
> 
> This project has been developed with extensive generative-AI assistance. Assistance covered project exploration, design discussion, specification development, implementation, testing, technical review, and documentation. See [AI_DISCLOSURE.md](AI_DISCLOSURE.md) for further details. Responsibility for the published software remains with the maintainer.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/README.md

SHA-256: `69bcab8ae7d0aad2e4061dbd78c76106cc2c319f952500a2a87f70a81ee16636`

```text
# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats counts lines and words in strings and named UTF-8 files on Python 3.11+, using only the standard library. Its immutable results and silent API are described in the [API guide](docs/api.md); options, errors and statuses are in the [module guide](docs/module.md). JSON output is available for named files; stdin remains planned for milestone 2.2. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).

## Quick start

Run from the source root:

```python
from textstats import TextStats, count_text
assert count_text("alpha beta\r\ngamma\r") == TextStats(2, 3)
```

```sh
printf 'alpha beta\ngamma\n' > sample.txt
python -m textstats sample.txt
# lines=2 words=3
python -m textstats --json sample.txt
# {"lines": 2, "words": 3}
python -m textstats --json sample.txt | python -c 'import json, sys; print(json.load(sys.stdin)["words"])'
# 3
python -m textstats --help
printf '\357\273\277\n' > bom.txt
python -m textstats bom.txt
# lines=1 words=0
python -m textstats --keep-bom bom.txt
# lines=1 words=1
python -m textstats --json --keep-bom bom.txt
# {"lines": 1, "words": 1}
python -m textstats --keep-bom --json bom.txt
# {"lines": 1, "words": 1}
printf 'alpha\n' > ./-sample.txt
python -m textstats -- -sample.txt
# lines=1 words=1
```

Empty input counts zero lines and words. Only CRLF, CR and LF terminate lines; a trailing terminator creates no extra line. Words follow Python Unicode whitespace splitting. By default exactly one initial BOM is removed. Input bytes stay unchanged, reads decode strict UTF-8, and owned file handles close. Complete-input processing uses memory proportional to input size.

Text remains the default. `--json` writes one JSON object plus newline with only integer `lines` and `words`; key order and spacing may vary. Counts, BOM policy, input preservation and errors are the same in both formats.

Success/help exit 0. Invalid arguments exit 2 before reading input. Expected file/read/decode failures exit 1 with an input-identifying diagnostic on stderr, no stdout or traceback. API errors propagate as OSError subclasses or UnicodeDecodeError.

## Product tests

Run the nonempty product suites independently:

```sh
python -m unittest discover -s tests/unit -t . -v
python -m unittest discover -s tests/integration -t . -v
```

Workflow fixtures under tests/workflows, when present, are separate from product acceptance.

## Source distribution

Build a standard-library source archive and extract it in an empty directory:

```sh
make dist
mkdir -p dist/extracted
python -m tarfile -e dist/textstats.tar.gz dist/extracted
cd dist/extracted
python -m textstats --help
```

The archive includes the package, public/development documentation and product tests. Generated dist output stays untracked. Integration discovery builds and extracts to a temporary directory, clears checkout import settings and verifies the extracted module's text/JSON/BOM/help/error behavior and import location. `make check` runs the two product suites independently.

## Named-file line ranges

```sh
printf 'alpha beta\nbeta\nlast two' > ranges.txt
python -m textstats --lines 2:3 ranges.txt
# lines=2 words=3
python -m textstats --json --lines=2:3 ranges.txt
# {"lines": 2, "words": 3}
python -m textstats --lines 4:99 ranges.txt
# lines=0 words=0
python -m textstats --lines=2:1 ranges.txt
# status 2; empty stdout; useful stderr; no file acquisition
```

`--lines START:END` and `--lines=START:END` select inclusive one-based logical lines of a named file. Endpoints must be positive ASCII decimals with START <= END; leading zeros and arbitrarily long endpoints are accepted. Missing/open endpoints, signs, whitespace, Unicode digits, zero, reversed bounds, extra colons and repeated range options are usage errors (status 2) before input is read. Selection intersects available lines; beyond EOF may yield empty counts. Only CRLF, CR and LF terminate lines, and original contents/terminators are preserved.

The entire file is strictly decoded before selection, so bad UTF-8 after END still fails (status 1). Apply the default one-leading-BOM removal or `--keep-bom` once to complete text before line numbering. An interior BOM exposed at the selection start stays ordinary non-whitespace. `--lines`, `--json` and `--keep-bom` compose in either order before `--`. Text and JSON count the same selection. Public APIs always count the whole input; they have no range parameter. Stdin remains scheduled for milestone 2.2; stdin ranges are unsupported.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/Makefile

SHA-256: `d8973498f1d1ec5a264f79501105b1d099adb6f5b2d4fb591d970d4b54a216c1`

```text
PYTHON ?= python
DIST_DIR ?= dist

.PHONY: dist check

# Explicit package/test files keep bytecode caches and workflow resources out.
dist:
	mkdir -p "$(DIST_DIR)"
	$(PYTHON) -m tarfile -c "$(DIST_DIR)/textstats.tar.gz" textstats/*.py README.md Makefile AI_DISCLOSURE.md SDD-MANAGER.md docs tests/__init__.py tests/unit/*.py tests/integration/*.py

check:
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests/unit -t . -v
	PYTHONDONTWRITEBYTECODE=1 $(PYTHON) -m unittest discover -s tests/integration -t . -v

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/module.md

SHA-256: `aceed32bcac843f1d784128f08e1198d2f06a08b81b4ef69e3a4bed0d32bd8f7`

```text
# TextStats module command

Use Python 3.11+ from the source root or an extracted source archive:

```sh
python -m textstats --help
printf 'alpha beta\ngamma\n' > sample.txt
python -m textstats sample.txt
# lines=2 words=3
printf '\357\273\277\n' > bom.txt
python -m textstats bom.txt
# lines=1 words=0
python -m textstats --keep-bom bom.txt
# lines=1 words=1
printf 'alpha\n' > ./-sample.txt
python -m textstats -- -sample.txt
# lines=1 words=1
```

## JSON consumption

```sh
python -m textstats --json sample.txt
# {"lines": 2, "words": 3}
python -m textstats --json sample.txt | python -c 'import json, sys; print(json.load(sys.stdin)["words"])'
# 3
python -m textstats --json --keep-bom bom.txt
# {"lines": 1, "words": 1}
python -m textstats --keep-bom --json bom.txt
# {"lines": 1, "words": 1}
```

## Input and options

Syntax: `python -m textstats [--json] [--keep-bom] [--lines START:END] INPUT`. Exactly one named UTF-8 file is required. `--` permits dash-prefixed filenames. `--keep-bom` retains all leading BOM characters; otherwise exactly one initial BOM is removed. CRLF/CR/LF lines and Unicode whitespace words follow the [API rules](api.md). Files stay unchanged. `--json` selects JSON output. It composes with `--keep-bom` in either order. Stdin input remains planned for milestone 2.2; INPUT currently names a file.

## Output and status

Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout, and leaves stderr empty. With `--json`, success instead emits exactly one JSON object plus newline, with only integer `lines` and `words` equal to the text counts; key order and whitespace are unrestricted. Both formats retain the same acquisition, BOM and error behavior. Help exits 0. Missing, extra or unknown arguments exit 2, with useful stderr, empty stdout, no traceback and no file acquisition. Expected open/read/decode failures exit 1, identify INPUT on stderr, and produce no stdout or traceback. Strict complete UTF-8 decoding prevents partial success even when invalid bytes follow valid text. File handles opened by the API are owned and closed.

```sh
python -m textstats nonexistent.txt
# status 1; stderr identifies nonexistent.txt; stdout is empty
```

See the [README](../README.md) for test and distribution commands.

## Named-file line ranges

```sh
printf 'alpha beta\nbeta\nlast two' > ranges.txt
python -m textstats --lines 2:3 ranges.txt
# lines=2 words=3
python -m textstats --json --lines=2:3 ranges.txt
# {"lines": 2, "words": 3}
python -m textstats --lines 4:99 ranges.txt
# lines=0 words=0
python -m textstats --lines=2:1 ranges.txt
# status 2; empty stdout; useful stderr; no file acquisition
```

`--lines START:END` and `--lines=START:END` select inclusive one-based logical lines of a named file. Endpoints must be positive ASCII decimals with START <= END; leading zeros and arbitrarily long endpoints are accepted. Missing/open endpoints, signs, whitespace, Unicode digits, zero, reversed bounds, extra colons and repeated range options are usage errors (status 2) before input is read. Selection intersects available lines; beyond EOF may yield empty counts. Only CRLF, CR and LF terminate lines, and original contents/terminators are preserved.

The entire file is strictly decoded before selection, so bad UTF-8 after END still fails (status 1). Apply the default one-leading-BOM removal or `--keep-bom` once to complete text before line numbering. An interior BOM exposed at the selection start stays ordinary non-whitespace. `--lines`, `--json` and `--keep-bom` compose in either order before `--`. Text and JSON count the same selection. Public APIs always count the whole input; they have no range parameter. Stdin remains scheduled for milestone 2.2; stdin ranges are unsupported.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/api.md

SHA-256: `0d056269a70aa6e6b6768d74a1ff045931e123245241d17308b32ad2f61aa785`

```text
# TextStats Python API

Python 3.11+ is supported. Import the public interfaces directly:

```python
from textstats import TextStats, count_text, count_file

assert count_text("alpha beta\r\ngamma\r") == TextStats(lines=2, words=3)
assert count_text("\ufeff\n", strip_bom=False) == TextStats(1, 1)
```

## Signatures and rules

- `TextStats(lines: int, words: int)` is immutable. Counts must be nonnegative integers; negative counts raise ValueError and other types (including booleans) raise TypeError.
- `count_text(text: str, *, strip_bom: bool = True) -> TextStats` counts the whole string.
- `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats` reads a whole named UTF-8 file.

CRLF is one terminator; lone CR and LF are terminators. Each terminator contributes one line; a nonempty final unterminated segment adds one. Empty text has zero lines and a trailing terminator adds no phantom line. Other Unicode separators do not terminate lines. Words use Python str.split() Unicode whitespace rules.

By default, exactly one leading U+FEFF BOM is removed. Interior and subsequent BOMs remain ordinary non-whitespace characters. Set strip_bom=False to keep all BOMs.

## Files, exceptions and ownership

Named files are read in binary mode and decoded strictly as UTF-8 without newline translation. Missing/unreadable/open/read/close failures propagate OSError subclasses; malformed UTF-8 raises UnicodeDecodeError. The API emits no stdout/stderr or partial result. Handles it opens close on success and read/decode failure. Input strings and file bytes are unchanged. Memory use scales with the complete input size.

```python
from pathlib import Path
from tempfile import TemporaryDirectory
from textstats import TextStats, count_file

with TemporaryDirectory() as directory:
    path = Path(directory) / "sample.txt"
    path.write_bytes(b"alpha beta\r\ngamma\r")
    assert count_file(path) == TextStats(2, 3)
    assert path.read_bytes() == b"alpha beta\r\ngamma\r"
```

See [module usage](module.md) for CLI diagnostics and process statuses.

Named-file CLI `--lines` selection does not change these whole-input API signatures or semantics. No range API is exported.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/PLAN-REVIEW-REPORT.md

SHA-256: `7f7f8c8a0f061b4881c4ab909ab496c1a6c2cdbefbe9900a9be2c125e60a040c`

```text
# PLAN review report

## Current gate

State: Ready for current PLAN.md conformance. Owner: sdd-plan, 2026-10-05. Revision 3 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Retained original gate and identities (historical)

State: Ready. Owner assessment: sdd-plan, 2026-10-04. Reviewed PLAN and layout; no focused children. SPEC/design readiness was checked against unchanged exact governing states. This review is document evidence; no product test was run and no implementation is claimed. TASKS derivation may proceed. No blockers or material open decisions.

Reviewed and governing states:

- PLAN.md: SHA-256 `8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8`.
- layout.md: SHA-256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- SPEC.md: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.
- SPEC-REVIEW-REPORT.md: SHA-256 `e4522d4a6d566d3dd6c7b208930547f152229ca3dd9a04028ce136a937a0df68`.
- PROJECT.md: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.

## Initial review

Compared every significant S-1 through S-7 contract with capability/exits, checked the earliest meaningful end-to-end named-file outcome, prerequisites, retained behavior, resource/error paths, documentation/distribution, code review/testing/report outcomes and component-to-path allocation. Layout was checked against existing repository ownership and design dependency direction.

| Phase | Delivery milestones | Excluded review unit | Scope/count assessment |
| --- | --- | --- | --- |
| 1 | 2: 1.1 and 1.2 | 1.3 single phase review outcome | Retained after explicit fragmentation review: MVP has immediate named-file/API/CLI utility; reliability/docs/distribution is a coherent release boundary. Further splitting would add handoff overhead to a small utility without independent outcome. |
| 2 | 2: 2.1 and 2.2 | 2.3 single phase review outcome | Retained after explicit fragmentation review: format and borrowed-source extensions have distinct observable value and failure ownership. Combining hides separate compatibility risks; padding to 3–5 invents work. |

| SPEC coverage | Delivery route |
| --- | --- |
| S-1/S-2 | 1.1 value/text/facade and regressions throughout |
| S-3/S-4 | 1.1 useful success/options, 1.2 full error/resource acceptance |
| S-5 | 2.1 named-file JSON and retained text/errors |
| S-6 | 2.2 binary stdin, locale/error/lifetime interactions |
| S-7 | 1.2 docs/distribution; extension docs/extracted-source checks at 2.1/2.2; aggregate 2.3 exits |

No findings or correction cycle. The mandatory per-delivery milestone review and final single-task phase review outcomes are reserved. Count exceptions retain the user's requested coherent phase/milestone identities. Future range delivery is excluded; compatible source-independent processing is retained by design/layout. API/module documentation, separate nonempty product suites and extracted-source module entry are all allocated. Phase activation and hosted writes remain outside preparation.

## Revision 1 — Authorized range reconciliation recheck

Integrated accepted 2.4/2.5 outcomes without renumbering 2.3. S-1–S-7 retain existing routes; S-8/R-1–R-4 map to 2.4 and scoped 2.5, independent of 2.2. Phase 1: two delivery milestones retained for useful MVP/reliability boundaries; Phase 2: three delivery milestones, main review 2.3 and feature-only review 2.5. Separate scoped review is not a second whole-phase review. Complete-decode/BOM/parser/API/docs/distribution exits and feasible component placement assessed. Layout unchanged and sufficient. Historical 2.1 exits do not establish range acceptance; task reassessment owns that. No product test run for this document checkpoint.

Exact reviewed/governing SHA256:

- PLAN.md: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- SPEC-REVIEW-REPORT.md: `93f0b8c602bde38ddcc5b8c1550475e12514c9cecd512b2c6e12b2d970c72534`
- layout.md: `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`
- FEATURE-PLAN.md: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`

## Revision 2 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-plan under sdd-integrate-feature correction ownership, 2026-10-05.

Complete S-1–S-8 coverage: Phase1 1.1/1.2 whole-input/decode/errors/docs; 2.1 JSON, 2.2 later stdin, 2.4 named-file ranges, 2.3 full final review and 2.5 scoped feature review. Phase1 two delivery milestones retained because useful MVP then reliable distribution are cohesive bounded outcomes; excluded1.3 review. Phase2 three delivery milestones with two excluded review units2.3/2.5; no padding/fragmentation. Ranges depend on completed JSON, not stdin. Updated design/layout owners preserve physical dependency routing. All exits include code review/nonempty suites/docs/distribution; range completion cannot complete Phase2. No confirmed unresolved finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

Upstream gate identities at this recheck:

- `SPEC-REVIEW-REPORT.md`: `acea3e8790c31bc3906af83039c4d68c1d1a114a3c2cbe8361fc886da0711cde`

## Revision 3 — Final range incorporation and archive conformance

Selected complete main owner reassessment, 2026-10-05. Accepted contract/design scope unchanged; PLAN2.4 now refers to canonical S8/main QC, and TASKS references S8/main readiness with sole T018–T022 ownership. Historical feature sources and adjacent reports moved together into features/002_ea97182, with local links repaired; main roots are standalone intended descriptions. TASKS status/reassessment changes have implementation evidence in T021/T022 reports and do not alter task decomposition/dependencies. S1–S8 routes, delivery counts/rationale and boundary obligations from previous revisions remain applicable. Original findings/identities retained, no unresolved conformance finding. Main Phase2/stdin/final review remain incomplete.

Exact current reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e1aa667a8bea06ed9feb9211697a9d70ac3f75b688f1f877ee4d38443cd8c629`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`

Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/TASKS.md

SHA-256: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`

```text
# TextStats executable task hierarchy

Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-012 are implemented and verified below; T-018–T-022 range implementation/review is verified below; remaining Phase 2 tasks retain their incomplete status. Range tasks are owned only here; feature snapshots are not executable lists. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Phase 2 is activated on phase/2-output-and-source-extensions; JSON milestone2.1 is selected, with stdin and final review incomplete. Range tasks T-018–T-022 have this list as their sole executable owner.

## Hosted tracking

Mode: maintained GitHub tracking in [pchemguy/Skill-Test-SDD-Manager-TextStats-20261004](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004). The eligible phase 1 label, native milestones 1.1–1.3 and task issues T-001–T-009 are projected. Milestones 1.1–1.3 are verified complete and closed. Task issue closure follows verified durable completion. Reconcile the eligible maintained scope before execution and lifecycle transitions; hosted state never establishes completion. Phase 2 projection waits for phase 1 completion, review, verified integration into main and publication.

Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`; activation baseline: `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`. The tracking checkpoint at `d009899e39790c39be32ae77e7fe8294bf60d04c` preceded implementation. The milestone 1.1 checkpoint below is historical. The milestone 1.2 suspension checkpoint is historical; authorized resumption completed T-009 and all Phase 1 tracking. Integration follows this published completion record.

## Phase 1 — Named-file utility

- [x] Phase 1 — Named-file utility
    Completion evidence (2026-10-04): T-001–T-009 verified and published; Phase 1 report/status at cb9d56ab4060483cd2240cb9553f43f850196968. Unit17/integration9, cross-component code review, public examples and isolated distribution satisfy PLAN1.3. Issues #1–#9 closed/completed; native milestones #1/#2/#3 read back closed with 0 open and 4/4/1 closed issues. This is local/working-branch acceptance; verified explicit integration and target publication are recorded separately. Stop before Phase2.
    - [x] Milestone 1.1 — Named-file counting MVP
        Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
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
            Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
            Depends on: T-001, T-002, T-003. Scope: delivered core, file API, facade and module CLI; relevant nonempty product suites and MVP demonstration.
            Evidence: actual code review, milestone exits/regressions, blocker repairs and committed/pushed report. Report: docs/dev/reports/phases/1/1.1.md. Record TODO or None and the usability decision evidence. No product completion inferred from workflow fixtures.
            Completion evidence (2026-10-04): [milestone review report](reports/phases/1/1.1.md) assesses all delivered modules and test coverage at f2260a2; no in-scope findings or TODOs. Fresh independent product discovery passed unit 14/integration 6 tests, no skips; direct normal/BOM/dash API/module demonstration and help passed, diff check clean. PLAN 1.1 exits verified; reliability/distribution and full phase acceptance remain unclaimed. Issue #4 exact title/body marker confirmed.
    - [x] Milestone 1.2 — Reliable documented distribution
        Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
        Completion evidence (2026-10-04): T-005–T-008 result/status/report commits published; independent unit17/integration9, code review, examples/diagnostics and isolated distribution satisfy PLAN1.2. Issues #5–#8 read back closed/completed; milestone #2 closed with zero open/four closed issues. Human gradual suspension arrived during T-008 publication; finish only its reconciliation and stop. T-009/phase integration not started; Phase2 remains unprojected and unimplemented.
        - [x] T-005 — Harden named-file API failure and resource behavior
            Scope: textstats/io.py and focused unit/integration failures. Depends on: T-004.
            Outcome: missing/unreadable files propagate OSError subclasses, strict bad-byte decoding raises UnicodeDecodeError, failure calls are silent, input unchanged, owned handles closed and no partial result (S-3).
            Evidence: real missing/bad-byte files plus portable injected unreadable/read/close seams; both BOM policies; byte-for-byte preservation and owned-handle success/failure checks. Do not rely solely on permission bits under privileged execution.
            Completion evidence (2026-10-04): existing binary context-managed acquisition already satisfies S-3; characterization tests added before any production edit passed after correcting a test import NameError (setup error, not behavioral RED). No production change or manufactured RED. Real missing/directory/malformed files, both BOM policies, open/read/decode/close failures, silent exception propagation, no returned partial value, unchanged bytes and closed owned handles verified. Focused 6 tests, independent unit 16/integration 7 passed with no skips; diff check clean. Existing API docstring reviewed against exceptions/lifetime. Issue #5 uniquely matched exact title and body marker; test-first cycle explicitly permits already-passing existing behavior.
        - [x] T-006 — Complete CLI diagnostics and public documentation
            Scope: textstats/cli.py, docs/api.md, docs/module.md, README.md and relevant unit/integration checks. Depends on: T-005.
            Outcome: useful input-identifying expected-error diagnostics, statuses 1/2, empty stdout/no traceback, retained help/options/success and documented runnable phase 1 API/module usage (S-4 and S-7 docs).
            Evidence: actual module missing/read/decode failures, invalid invocation before acquisition, unchanged files; run documented API/help/text/BOM examples. Preserve original README content and SDD links.
            Completion evidence (2026-10-04): focused RED before production edits had 8 unhandled expected-error subtests and 6 real module diagnostic failures; GREEN passed both tests after narrow OSError/UnicodeDecodeError translation. Independent unit 17/integration 8 passed with no skips; retained options/help/validation-before-acquisition and exact success regressions pass. Real missing/directory/bad UTF-8, injected permission/read failures and both BOM policies return 1 with identifying stderr, empty stdout/no traceback; bytes unchanged. README original heading/focus/SDD links retained; public API and module guides/docstring reviewed. All Python/shell API/help/text/BOM/dash/failure examples executed in temporary directories with exact count/status assertions; local links valid; diff check clean. No JSON/stdin delivered. Issue #6 exact title/marker confirmed.
        - [x] T-007 — Establish isolated source-distribution acceptance
            Scope: Makefile, generated-output ignore rules and tests/integration distribution checks. Depends on: T-006.
            Outcome: standard-library source archive includes importable package, README and public docs; generated dist/extractions stay untracked (S-7).
            Evidence: build/extract to temporary root; invoke extracted python -m textstats with a clean import environment from that root; check exact named-file counts, --keep-bom, help and representative failure status. Independently discover nonzero unit/integration suites and run README examples. Keep workflow fixtures separate and pinned resources unchanged.
            Completion evidence (2026-10-04): RED source-distribution test observed missing make dist target before build implementation; GREEN passes isolated standard-library build/extraction with cleansed PYTHONPATH/PYTHONHOME/PYTHONSTARTUP, disabled user site and exact extracted __file__ assertion. Package/public docs/README/build recipe/tests included; workflow resources, caches and generated outputs excluded; dist ignored. Normal/empty/Unicode/BOM/keep-BOM text, help, missing/malformed/usage/unknown JSON errors and unchanged input verified. Independent unit17/integration9 passed, no skips. README/API/module examples rerun, including actual build/extract/help sequence with checkout import settings removed (initial temporary-cwd example runner failure corrected, not a product defect). A second example-runner assertion rejected a successful extraction solely for Python 3.12 tarfile deprecation stderr; corrected the runner to distinguish this known warning from failed commands, then reran all examples successfully. Test extraction now requests the data filter when available, with a validated-path fallback for earlier Python 3.11. This is a correction to the premature example-pass assertion in b686559; all previous failures remain recorded. Independent unit17/integration9 and example checks rerun successfully, no skips; diff check clean. Issue #7 exact title/marker confirmed.
        - [x] T-008 — Review, test and report milestone 1.2
            Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
            Depends on: T-005, T-006, T-007. Scope: API/CLI failures, lifecycle, docs/distribution and all phase 1 regressions.
            Evidence: code review, independent nonempty product suites, diagnostic demonstration, extracted-source checks, blocker repair and committed/pushed report. Report: docs/dev/reports/phases/1/1.2.md. Carry prior TODO provenance and record release decision evidence.
            Completion evidence (2026-10-04): [milestone report](reports/phases/1/1.2.md) covers separate full implementation review at 7939e1c, fresh unit17/integration9 without skips, all public examples, useful normal/missing/malformed diagnostics and independent extracted-source invocation. Every PLAN1.2 exit verified; original T-007 runner/evidence failures and correction retained, no unresolved product finding/TODO. Python3.12.14 tested; no3.11 execution claim. Issue #8 exact title/marker confirmed; issue/milestone closure and local parent reconciliation follow report publication.
    - [x] Milestone 1.3 — Phase 1 review
        Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
        Completion evidence (2026-10-04): T-009 report/status published at cb9d56a; issue #9 closed/completed with evidence comment 5983966503; exact milestone3 issue listing contains only #9, closed/completed. Milestone #3 read back closed with zero open/one closed issue after preceding delivery closures.
        - [x] T-009 — Review, test and report phase 1
            Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
            Depends on: milestones 1.1 and 1.2 complete/closed when tracking is active, including T-004/T-008. Scope: cross-component phase 1 S-1 through S-4 and delivered S-7.
            Evidence: phase code review, nonempty product suites, documented examples/distribution/regressions, blocker repairs and committed/pushed report with milestone TODO aggregation. Report: docs/dev/reports/phases/1/PHASE-REPORT.md. Complete phase exits before explicit phase-branch merge to main, merged-state verification and publication; a partial range pauses on its phase branch.
            Completion evidence (2026-10-04): [phase review report](reports/phases/1/PHASE-REPORT.md) inspects all production/test/docs/build source at dec4ca1 against S-1–S-4 and delivered S-7; no findings or TODOs. Fresh independent unit17/integration9 passed with no skips; public Python examples/local links, exact normal/BOM/keep-BOM/dash/help/failure demonstrations and isolated extracted-source identity/counts passed. Diff check clean; prior RED/GREEN provenance retained with no new behavior change. #1–#8 exact title/marker and closed/completed state confirmed; milestones #1/#2 closed with zero open/four closed issues. #9 exact title/marker confirmed. Task report/status publication precedes #9/milestone3 closure and final parent/integration reconciliation; Phase2 remains unselected.

## Phase 2 — Output and source extensions

- [ ] Phase 2 — Output and source extensions
    - [x] Milestone 2.1 — JSON output
        Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
        Completion evidence (2026-10-04): T-010–T-012 implementation/tests/docs/report/status normally published on phase/2-output-and-source-extensions. Report ebecf1de74985acd3a9be62423c0a12e349b6586, independent unit17/integration11, public examples/extracted-source checks and distinct code review satisfy PLAN2.1. Issues#10/#11/#12 read back closed/completed with exact markers and evidence comments; exact native milestone#4 membership contains only these3 issues, closed with0 open/3 closed. Phase2 remains unchecked and milestones2.2/2.3/T-013–T-017 remain incomplete. Pause before stdin; no integration into main59debb649545125dd3aa00377ea115451b594271.
        - [x] T-010 — Add JSON rendering with preserved named-file behavior
            Scope: textstats/cli.py and unit/integration format checks. Depends on: T-009 and verified/published full phase 1 integration.
            Outcome: --json emits only integer lines/words plus newline, equal to text counts; compose --keep-bom in either order and preserve statuses/errors (S-5).
            Evidence: parse actual module output for normal/empty/BOM/terminator files, exact text default regressions, key/type checks, useful failures and stdout atomicity; demonstrate script consumption. Stdin remains scheduled in 2.2.
            Completion evidence (2026-10-04): focused RED `PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.integration.test_cli.JsonModuleTests -v` observed 30 behavioral failures (unknown --json exits2); GREEN passed2 tests after command-adapter JSON rendering. Independent unit17/integration11 pass, no skips. Seven real-byte fixtures cover ordinary/empty/terminator/Unicode/BOM/double-BOM, JSON only integer lines/words and one object/newline, both BOM option orders, exact retained text outputs/dash paths and unchanged inputs. Real missing/directory/malformed JSON failures and injected permission/read/decode errors retain status1, identifying stderr and empty stdout; invalid JSON usage acquires nothing. API/core/io remain unchanged; module docstring reviewed. Separate script-consumption demo parses counts2/3. Phase1 unknown-option regressions now use --jsn, since --json is delivered. Issue#10 exact title/body marker verified; Phase2 label12541856034, milestones#4/#5/#6 and all issues#10–#17 read back before tests. Baseline59debb649545125dd3aa00377ea115451b594271; target main; no stdin or phase integration.
        - [x] T-011 — Document and verify the JSON distribution boundary
            Scope: docs/module.md, README.md and tests/integration extracted-source checks. Depends on: T-010.
            Outcome: runnable JSON examples, accurate delivered option documentation and extracted-package text/JSON acceptance (S-7 at 2.1).
            Evidence: run examples, nonzero unit/integration discovery and tests; invoke extracted source module for both formats/BOM policies and representative failures without checkout imports.
            Completion evidence (2026-10-04): focused extracted-source check passed1 test; independent `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v` passed17 and integration discovery passed11, no skips. Added characterization acceptance of already delivered T-010 JSON (no production edit or manufactured RED): extraction clears checkout imports, asserts exact extracted package identity and text/JSON counts for ordinary/empty/Unicode/BOM/retained-BOM, both option orders, help and representative missing/malformed/invalid-option failures with unchanged bytes. README/module guide accurately deliver --json, keep stdin planned and retain original content/SDD links. API guide reviewed: unchanged whole-input signatures and lifecycle remain accurate. All9 public Python/shell blocks/local links executed in isolated temporary source, including JSON script consumption, source build/extract/help and statuses; expected nonexistent-file exit1 passed. Python3.12 tarfile CLI extraction deprecation warning recorded, no failed example. Issue#11 exact title/marker confirmed. No stdin or phase exit claim.
        - [x] T-012 — Review, test and report milestone 2.1
            Completion reassessment resolved (2026-10-05): prior whole-input evidence remains historical; current affected named-file S-1–S-5/S-7/S-8 acceptance is supported by T-021/T-022 code review, unit21/integration13, public examples and isolated extraction. See feature002_ea97182 milestone/phase reports. Stdin and whole Phase2 completion are not established.
            Depends on: T-010, T-011. Scope: format implementation, docs/distribution and retained phase 1 contracts.
            Evidence: code review, focused/regression tests, demonstration, blocker repair and committed/pushed report with TODO provenance. Report: docs/dev/reports/phases/2/2.1.md.
            Completion evidence (2026-10-04): [milestone2.1 report](reports/phases/2/2.1.md) records separate all-module/test/docs/build code review at27251ae6b73eb4179c422449abacc080051b49a0, fresh independent unit17/integration11 passing/no skips, actual JSON script consumption and unchanged T-011 all9 public examples/local links and isolated distribution evidence. All PLAN2.1/S-5 plus retained S-1–S-4 and delivered S-7 exits verified; no product finding/TODO. RED30/GREEN2 chronology and known tarfile CLI deprecation warning retained; actual Python3.12.14, no3.11 runtime claim. Issue#12 exact title/marker confirmed. Hosted issue/milestone closure and local parent reconciliation follow report publication; Phase2 remains incomplete, stop before T-013/stdin/integration.
    - [ ] Milestone 2.2 — UTF-8 stdin and final release
        - [ ] T-013 — Integrate borrowed binary stdin acquisition
            Scope: textstats/cli.py and source/lifecycle unit/integration checks. Depends on: T-012.
            Outcome: INPUT - reads bytes until EOF, strict UTF-8 independent of locale, never closes stdin; ./- remains a named-file path; formats/BOM policies share whole-input counting (S-6).
            Evidence: actual subprocess piped ordinary/empty/non-ASCII/BOM bytes in both formats and non-UTF-8 locale settings; instrument borrowed stream lifetime and retained named-file behavior. Keep acquisition separate from decoded-text processing for future selection compatibility.
        - [ ] T-014 — Complete stdin failure and interaction acceptance
            Scope: textstats/cli.py and focused unit/integration checks. Depends on: T-013.
            Outcome: read/decode failures identify stdin on stderr, exit 1, empty stdout, no traceback; invalid usage precedes acquisition, and complete decoded input governs all formats (S-4/S-6).
            Evidence: malformed piped bytes, injected binary read failure, never-close checks, both-order --json/--keep-bom, source/format/terminator regressions and unchanged named files. Retain named-file ranges; this task does not extend range selection to stdin.
        - [ ] T-015 — Complete source documentation and final distribution checks
            Scope: docs/api.md, docs/module.md, README.md and tests/integration distribution checks. Depends on: T-014.
            Outcome: final runnable docs describe all delivered sources/formats, stdin UTF-8/error/lifetime rules and whole-input public API (S-7).
            Evidence: execute documented examples; build/extract clean source archive; invoke extracted module for named-file/stdin, text/JSON, empty/BOM/non-ASCII and representative failures. Independently require nonempty passing unit/integration suites; report workflow checks separately.
        - [ ] T-016 — Review, test and report milestone 2.2
            Depends on: T-013, T-014, T-015. Scope: source acquisition, decoding, interactions, docs/distribution and all retained acceptance.
            Evidence: code review, tests/regressions, piped source demonstration and diagnostics, blocker repairs, committed/pushed report and prior TODO disposition. Report: docs/dev/reports/phases/2/2.2.md.
    - [ ] Milestone 2.3 — Phase 2 and final review
        - [ ] T-017 — Review, test and report phase 2 and the complete product
            Depends on: milestones 2.1, 2.2 and 2.4 complete/closed when tracking is active, including T-012/T-016. Scope: all main SPEC contracts, cross-source/format/BOM interactions and final exits.
            Evidence: phase code review, complete nonempty product suites, runnable docs, isolated extracted-source module checks, blocker repair and committed/pushed reports. Reports: docs/dev/reports/phases/2/PHASE-REPORT.md and docs/dev/reports/IMPLEMENTATION-REPORT.md. Aggregate unresolved admissible TODOs and solution/owner/provenance with resolution references; verify full-phase explicit integration, merged state and publication before claiming complete implementation.

    - [x] Milestone 2.4 — Named-file line ranges
        - [x] T-018 — Establish normalized logical-line selection seam
            Depends on: T-012 and current main preparation gates.
            Scope: textstats/core.py, textstats/io.py and tests/unit semantic/acquisition checks; preserve public facade.
            Outcome: source-independent selection consumes text after one BOM normalization, preserves CRLF/CR/LF contents/terminators and EOF semantics; private complete named-file decoding can feed it without altering count_file's whole-input signature or owned-handle lifecycle (S-8/S-3).
            Evidence: pure supplied selection examples, empty/final segments/Unicode separators/interior and double BOM; whole-input API signatures/exports/silence/counts, close-on-success/failure and unchanged bytes. Strict decoding remains complete before any selection. Default CLI stays useful while no range command is exposed yet.
            Completion evidence (2026-10-05): focused selection RED ran 2 tests with 2 missing-seam assertion failures; GREEN independent unit19/integration11 passed, no skips. Supplied logical-line/BOM/Unicode/EOF rows preserve characters and terminators; whole-input facade/signature/silence/unchanged bytes and existing success/read/decode/close lifecycle regressions pass after private full-decode factoring. Default CLI unchanged. `git diff --check` passed. Issue #18 title/phase/milestone confirmed; protected metadata omits body marker, so prior projection marker verification in authorized request is retained rather than claimed freshly inspected.
        - [x] T-019 — Integrate validated named-file range text and JSON commands
            Depends on: T-018.
            Scope: textstats/cli.py and tests/unit/test_cli.py plus tests/integration module/file checks.
            Outcome: --lines spellings validate positive ASCII inclusive endpoints before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (S-8).
            Evidence: actual module supplied examples in text/JSON and both option orders, leading zeros and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
            Completion evidence (2026-10-05): actual module RED observed 73 unknown-option failures across 2 test methods; after parser/composition implementation GREEN independent unit21/integration13 passed, no skips. Both range spellings/text/JSON/orders, ASCII/leading-zero/5000-digit endpoints, malformed/repeated ranges before acquisition, complete bad UTF-8 after END, BOM/Unicode/CRLF/EOF rows, file preservation and owned-handle/expected errors verified. API stays whole-input; no stdin delivered. `git diff --check` passed. #19 exact title and opening/closing task markers verified through readonly connector; maintained closure pending adapter facility resolution.
        - [x] T-020 — Document ranges and verify extracted-source acceptance
            Depends on: T-019.
            Scope: README.md, docs/module.md, docs/api.md accuracy review and tests/integration/test_distribution.py; existing Makefile recipe.
            Outcome: runnable named-file range examples, syntax/repetition/status/complete-decode/BOM rules and explicit stdin boundary; public API docs retain whole-input contract (S-8/S-7).
            Evidence: execute public examples/help, run independent nonempty product suites, clean archive extraction and actual extracted python -m textstats for both spellings/formats/BOM policies and representative usage/read/decode failures. Remove checkout import leakage, assert extracted package identity and unchanged input. Workflow fixtures remain separate.
            Completion evidence (2026-10-05): README/module named-file range examples, full syntax/repetition/status/decode/BOM/EOF rules and explicit stdin boundary added; API reviewed whole-input unchanged. Existing delivered behavior characterized, no production edit or manufactured RED. Extended isolated archive test passed with extracted import identity, both spellings/text/JSON/BOM orders, dash file and usage/read/late-decode errors; bytes unchanged. Independent unit21/integration13 passed, no skips; public fenced Python/shell examples executed in temporary directories with expected statuses, build/test blocks separately covered by suites. Diff check passed. #20 exact title/markers verified; hosted reconciliation pending unknown preHTTP adapter failure.
        Completion evidence (2026-10-05): T018–T021 implementation, separate code review, unit21/integration13, public examples/isolated source checks and all PLAN2.4 exits verified. [Range milestone report](features/002_ea97182/2.4.md) records current acceptance. Hosted report/issue/milestone transitions are separately observed after publication; Phase2 remains incomplete.
        - [x] T-021 — Review, test and report range milestone 2.4
            Depends on: T-018, T-019, T-020.
            Scope: all named-file range behavior, helper/acquisition/CLI composition, API compatibility, docs/distribution and prior acceptance.
            Evidence: separate code review and focused/regression checks against all2.4 exits, useful demonstrations, required blocker repairs, TODO provenance and committed/pushed report. Reconcile issues and close2.4 only after all constituent issues are verified complete when tracking is active.
            Report: docs/dev/features/002_ea97182/2.4.md.
            Completion evidence (2026-10-05): [milestone code review/testing report](features/002_ea97182/2.4.md), reviewed749a898 plus accepted owner/docstring-only changes; independent unit21/integration13 no skips, public examples/links/diff check pass. No in-scope finding/TODO. Governing-owner incorporation/QC Ready; issue#21 exact title/markers verified, closure follows commit/push.
    - [x] Milestone 2.5 — Range feature review
        Completion evidence (2026-10-05): T022 cross-component review, independent unit21/integration13, examples/links/archive and main owner QC verify scoped PLAN2.5 exits; [feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) retain TODO: None. Hosting closure follows publication; main Phase2 remains incomplete.
        - [x] T-022 — Review, test and report the named-file range feature
            Depends on: feature milestone2.4 complete/closed when tracking is active, including T-021.
            Scope: cross-component S-8 and retained named-file S-1–S-5/S-7; feature-only phase/final report, not main T-017 or stdin acceptance.
            Evidence: separate feature phase code review, nonempty suites, API/default/format/BOM/decode/lifecycle regressions, runnable docs and extracted-source checks, blocker repair and final feature TODO aggregation with provenance/resolution references. Separately authorized full implementation incorporates accepted selected feature docs and reconciles task ownership/QC before final target merge and merged-state verification/publication; main Phase2 remains unfinished. No incorporation/merge/implementation during preparation.
            Reports: docs/dev/features/002_ea97182/PHASE-REPORT.md and docs/dev/features/002_ea97182/IMPLEMENTATION-REPORT.md.

## Range feature conclusion

T-018–T-022 are verified completed on feature/002_ea97182-line-ranges. Governing owners and task ownership are reconciled; feature sources/adjacent QC are historical under [feature002_ea97182](features/002_ea97182/README.md). Fresh independent unit21/integration13, code review, public examples, links and diff checks establish named-file feature exits. [Feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) record evidence and TODO: None. 2.4/#7 closed with0open/4closed after report/status publication; 2.5/#8 closure follows T022 publication. Main Phase2, stdin2.2 and final2.3/T013–T017 remain unchecked; no Phase2→main integration is authorized here.

T-022 completion evidence (2026-10-05): reviewed full delivered production/test/docs/build boundaries separately from fresh unit21/integration13 (no skips), verified R1–R4/mainS8 and retained named-file/API/format/decode/BOM/resource/docs/distribution conditions. Sources and adjacent QC archived only after owner/task/evidence disposition; main owner QC rechecked, links/unique IDs/whitespace passed. No findings/TODO. #22 exact title/opening+closing markers verified; report/status push precedes issue/milestone closure and explicit feature integration.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/ARCHITECTURE.md

SHA-256: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`

```text
# TextStats architecture

[PROJECT.md](PROJECT.md) defines purpose and boundaries. This describes intended design, not implemented behavior.

## Blocks and dependencies

A pure counting core owns statistics and text semantics. An acquisition adapter owns UTF-8 decoding and named-file resource lifecycle. A command adapter owns option validation, source choice, output formats, diagnostics and process status. Public exports expose the core and named-file adapter; the module entry delegates to the command adapter. Dependencies flow command → acquisition/core and acquisition → core. The core never imports CLI, filesystem or process state.

All mutable state is per call. There is no persistent store or external service. Input belongs to the caller; the named-file adapter closes handles it opens, while the command adapter borrows stdin. Output is published only after successful complete acquisition and counting.

## Choices and invariants

A frozen value object plus functions gives a small public surface without an inheritance hierarchy. Separate acquisition from counting to keep Unicode and line semantics testable without filesystem or process fixtures. Standard-library argument parsing and JSON serialization are sufficient; no runtime third-party dependency is needed.

Decode complete bytes using strict UTF-8 before text processing. File reads preserve CR/LF terminators, avoiding universal-newline translation. Apply the BOM policy once at the boundary of text processing; the core operates on the resulting text. Keep formatting outside the counting core. These boundaries allow small integrated delivery increments while retaining a stable whole-input API.

## Named-file range selection

A CLI-only selection stage sits between complete decoding/BOM normalization and counting. It identifies only CRLF, CR and LF logical lines, preserves selected contents and terminators, and never applies BOM stripping again to a slice. Source-independent decoded-text processing supports named files and future stdin. Range syntax is validated before acquisition, including repetition and positive ordered ASCII decimals without an endpoint cap or interpreter conversion limit. Named-file acquisition exposes complete decoded text privately, while count_file retains its whole-input contract. The command selects normalized logical lines and counts the slice with BOM stripping disabled. Stdin acquisition remains a separate delivery; stdin ranges are unsupported.

See [DECOMPOSITION.md](DECOMPOSITION.md) for component seams and [SPEC.md](SPEC.md) for observable contracts.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/SPEC-REVIEW-REPORT.md

SHA-256: `1d7e0ceebc9b832e354646bc1b3c64c72d16d8220a7ade862a0631ae438d6919`

```text
# SPEC review report

## Current gate

State: Ready for current SPEC.md conformance. Owner: sdd-specify, 2026-10-05. Revision 3 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Original reviewed identities

Reviewed and governing states:

- PROJECT.md: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- SPEC.md: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.

Checks: compared the accepted brief with every S-1 through S-7 contract and design ownership; inspected public signatures, result invariants, source/resource/error boundaries, format preservation, end-to-end acceptance and local document links. No confirmed issue or material open decision remains. PLAN authoring may proceed; implementation is not authorized.

## Initial review

| Contract group | Design and project coverage | Result |
| --- | --- | --- |
| S-1/S-2 value and text | Pure counting, immutable value and public facade | Complete CRLF/CR/LF, Unicode words and single-BOM behavior with objective examples |
| S-3 file failures/lifecycle | Named-file adapter, atomic complete UTF-8 decoding | API exceptions, silence, unchanged input and close ownership specified |
| S-4 CLI | Command adapter/module entry | Exact output, option errors, help, dash filenames and expected failures specified |
| S-5/S-6 extensions | Renderers and borrowed stdin adapter | JSON preservation and locale-independent binary stdin specified |
| S-7 product exits | Verification/distribution component | Public docs, runnable README, nonempty separated suites and extracted-source entry specified |

No findings. The future range contract is a source-independent design constraint, not an unrequested main delivery feature. Memory scaling is a documented scope tradeoff, not a claimed performance guarantee. No correction cycle occurred.

## Revision 1 — Selected named-file range incorporation

Scope: SPEC.md and this adjacent QC report only. Incorporation uses accepted FEATURE-SPEC R-1–R-4; all active feature sources and their reports remain in place. Existing review observations above are historical and retained.

Exact reviewed/governing states (SHA-256):

- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`.
- FEATURE-SPEC.md: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`.
- PROJECT.md: `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.

| Contract group | Accepted coverage / current result |
| --- | --- |
| S-1–S-3 | Immutable value, silent whole-input APIs, exact text/BOM semantics, complete strict UTF-8 decode and resource ownership unchanged |
| S-4/S-5/S-8; R-1/R-3 | Command adapter owns one optional range, both spellings, unbounded positive ASCII decimals, repetition/invalid usage before acquisition, both renderers/BOM options, unchanged APIs/errors |
| S-2/S-3/S-8; R-2 | Acquisition fully decodes before pure source-independent normalization/selection; preserved CRLF/CR/LF, EOF and exposed interior BOM have objective contracts |
| S-6 | Borrowed binary stdin whole-input contract retained; named-file range acceptance makes no stdin range delivery claim |
| S-7/S-8; R-4 | All supplied examples and edge/failure cases, runnable docs/help, independent nonempty product suites and extracted-source range invocation required |

Assessment: accepted design already provides every structural owner/seam; PROJECT identifies ranges as separately requested rather than rejecting them. The selected request accepts their incorporation without moving them into the main delivery hierarchy. No design change or material unresolved behavioral decision is required. Read the full main root as a standalone intended contract, checked original S-1–S-7 preservation and R-1–R-4 coverage, format/error/lifecycle guarantees, absence of editing-history language, local links and objective acceptance. Removed the obsolete main range exclusion and integrated selection into S-4/S-5/S-7 plus canonical S-8. Editorial recheck removed implementation-stage language from the incorporated source prose. Whitespace, link, hash and selected-path checks passed; no product tests were run for this document-only checkpoint. No confirmed in-scope finding remains. SPEC gate: Ready.

Outside selected scope: main PLAN excludes range allocation and PLAN-REVIEW-REPORT reviews the old SPEC; main TASKS/TASKS-REVIEW-REPORT consequently cannot establish complete expanded-main conformance. Their affected gates require authorized PLAN/TASKS reconciliation and owner rechecks before dependent execution/projection. FEATURE-SPEC's own R-1–R-4 content is unchanged, but its recorded main SPEC identity and feature PLAN/TASKS upstream equivalence need reassessment before dependent use; those reports are retained historical evidence, not a fresh gate for this main incorporation. Feature tasks T-018–T-022 remain the sole executable range owners, unchecked; no transfer or duplicate entry was made. Main T-013–T-017 remain incomplete. Existing checked tasks and milestone/phase evidence are preserved for their historical whole-input/JSON boundaries; expanded S-4/S-5/S-7 or whole-project acceptance claims (notably T-004/T-008/T-009/T-012 and their parents) need scope-aware reassessment in their owning lists/evidence before reuse as complete current acceptance. Those locations are outside scope, so no pending note or checkbox change is made here.

The package README and feature PLAN/TASKS retain preparation-era incorporation boundary wording; their later continuation must account for this SPEC checkpoint and its QC without treating the entire package as incorporated. Active sources remain required by feature planning/tasks/links and unfinished implementation. Archival, task ownership transfer, hosted reparenting/projection and final feature-to-phase integration are deferred. This selected SPEC checkpoint may finish on the existing feature branch without claiming whole-project readiness or implementing ranges.

## Revision 2 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-specify under sdd-integrate-feature correction ownership, 2026-10-05.

S-1–S-3 whole-input API/value/decode/lifecycle map to facade/core/io; S-4/S-5/S-8 option validation, named-file ranges and formatting map to cli plus source-independent core/io seam. S-6 remains later borrowed stdin without ranges. S-7 maps tests/docs/build. Accepted design/PROJECT incorporation resolves stale future-range exclusions without new contract or public API. Every objective row/error/BOM obligation remains owned and assessable. No focused children or confirmed unresolved finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

## Revision 3 — Final range incorporation and archive conformance

Selected complete main owner reassessment, 2026-10-05. Accepted contract/design scope unchanged; PLAN2.4 now refers to canonical S8/main QC, and TASKS references S8/main readiness with sole T018–T022 ownership. Historical feature sources and adjacent reports moved together into features/002_ea97182, with local links repaired; main roots are standalone intended descriptions. TASKS status/reassessment changes have implementation evidence in T021/T022 reports and do not alter task decomposition/dependencies. S1–S8 routes, delivery counts/rationale and boundary obligations from previous revisions remain applicable. Original findings/identities retained, no unresolved conformance finding. Main Phase2/stdin/final review remain incomplete.

Exact current reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e1aa667a8bea06ed9feb9211697a9d70ac3f75b688f1f877ee4d38443cd8c629`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`

Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/PLAN.md

SHA-256: `e1aa667a8bea06ed9feb9211697a9d70ac3f75b688f1f877ee4d38443cd8c629`

```text
# TextStats delivery plan

Deliver the complete [SPEC.md](SPEC.md) through a useful named-file MVP, reliable/documented release, then format and source extensions. [layout.md](layout.md) assigns physical ownership; TASKS derives executable units.

## Phase 1 — Named-file utility

### Milestone 1.1 — Named-file counting MVP

Scope: immutable public value, count_text/count_file, exact text/BOM semantics, named-file UTF-8 success, and useful module CLI with one input, help, --keep-bom and -- handling. API and CLI agree on counts. Establish real, discoverable unit/integration checks alongside the slice. Included contracts: S-1/S-2, S-3 success and owned success-handle lifecycle, S-4 success/help/option validation. Required failure hardening and release documentation/distribution conclude in 1.2; JSON and stdin conclude in phase 2.

Prerequisite: reviewed preparation inputs and Python 3.11+. Exit: users can count a named UTF-8 file through the public API and actual module entry; exact stdout/stderr/status, path forms, BOM and terminator examples pass; input is unchanged. Final milestone code review, relevant tests, blocker repairs and committed report are mandatory. Demonstrate a normal file, a BOM file and a dash-prefixed filename. This informs the human's continue/amend/simplify/stop decision about usefulness and command syntax; routine authorized work needs no renewed approval.

### Milestone 1.2 — Reliable documented distribution

Prerequisite: 1.1 complete. Scope: all file/decode/resource and CLI diagnostic failures, invalid invocation before acquisition, public API/module docs, runnable README and source distribution checks. Included contracts: complete S-3/S-4 and phase 1 S-7. Keep the 1.1 path working throughout.

Exit: missing/unreadable/malformed inputs, failure silence and status/diagnostics, handle closure, unchanged input and no partial success are verified; nonempty product unit/integration suites pass independently; documented examples work; an isolated extracted source package runs python -m textstats. Workflow fixtures remain a separate suite. Final milestone code review/testing/repair/report is required. Demonstrate useful failure diagnostics and the extracted-package invocation to inform release readiness.

### Milestone 1.3 — Phase 1 review

Dedicated single phase code review/testing/report outcome after both delivery milestones complete (and close when hosting is active). Exit: cross-component S-1 through S-4 and delivered S-7 acceptance, docs and distribution evidence, prior milestone findings carried forward, required defects repaired and phase report committed/pushed. Only full phase completion permits explicit phase-branch integration into main, merged-state verification and publication.

## Phase 2 — Output and source extensions

### Milestone 2.1 — JSON output

Prerequisite: phase 1 fully reviewed, integrated and published. Scope: --json and both-order composition with --keep-bom for named files, one object/newline, only integer lines/words, preserved text default and errors. Included contracts: S-5 with phase 1 regression acceptance and updated public/module docs and README examples.

Exit: JSON parses to the same counts for ordinary/BOM/empty/terminator cases, default text and failures remain exact, nonempty product suites pass, and extracted-source module invocation demonstrates JSON and text. Final milestone code review/testing/repair/report is mandatory. Demonstrate script consumption of JSON to inform format usefulness.

### Milestone 2.2 — UTF-8 stdin and final release

Prerequisite: 2.1 complete. Scope: INPUT -, binary stdin until EOF, locale-independent strict UTF-8, borrowed-handle lifecycle, empty/error inputs and both formats/BOM policies. Included contracts: S-6 and final S-7 with all S-1 through S-5 retained. ./- addresses a literal file named -.

Exit: actual module subprocess accepts piped UTF-8 bytes independent of locale, empty stdin and invalid bytes produce required outcomes; an injected read failure identifies stdin without partial stdout; borrowed stdin stays open; named-file behavior regresses successfully. Updated API/module/README docs and isolated extracted-source checks cover stdin/text/JSON. Final milestone code review/testing/repair/report is mandatory. Demonstrate piped text/JSON and error behavior to inform final release readiness.

### Milestone 2.3 — Phase 2 and final review

Dedicated single phase code review/testing/report outcome after both delivery milestones complete/close. Exit: complete main SPEC acceptance, cross-format/source/BOM regressions, nonempty suites, runnable documentation and extracted-source distribution checks pass; blockers repaired; prior findings retained; phase report and final implementation report aggregate unresolved admissible TODOs and resolution references. Explicit verified phase integration and publication conclude the authorized full implementation when separately requested.

### Milestone 2.4 — Named-file line ranges

Prerequisite: completed/published JSON milestone2.1/T-012 at the pinned paused baseline, current main SPEC/design QC and separately authorized implementation. No prerequisite on unfinished stdin or main final review; whole-input named-file text/JSON already works. Delivery retains the useful baseline while introducing a source-independent normalization/selection seam, then composing command validation/acquisition/rendering into a named-file slice. Pure helper work is a bounded prerequisite to the earliest usable changed CLI path, not a released skeleton.

Scope: S-8 and retained S-1–S-5/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded decimals, text/JSON and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.

Exit: actual module invocation counts selected named-file lines in text/JSON with exact stdout/status/stderr; supplied examples, ASCII/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.

### Milestone 2.5 — Range feature review

Dedicated single feature-scoped phase review/testing/report outcome after delivery milestone2.4 completes/closes when tracking is active. Exit: cross-component range/API/BOM/format/decode/lifecycle/docs/distribution acceptance, prior finding disposition, blocker repair and committed/pushed feature phase report. Aggregate feature TODOs and final feature implementation report. This is not main milestone2.3/T-017 or a whole-project Phase2 completion claim.

Range integration requires accepted main owners, unique task ownership and verified feature exits before an explicit merge into the paused phase target. Main stdin tasks remain incomplete. Full Phase 2 completion additionally requires 2.2/2.3; the scoped 2.5 review cannot complete Phase 2.

## Verification and sequencing

Count product tests separately from workflow checks; zero-test discovery never passes. Unit evidence covers pure semantics and boundaries; integration evidence invokes actual module entry and public imports against real files/bytes. Distribution evidence runs extracted sources from an isolated working directory with no checkout-derived import path. Documentation examples are verified when delivered.

Use unittest discovery for each product suite. Required checks include API silence, failure atomicity, strict decoding, owned/borrowed stream lifetime and unchanged bytes. Do not rely on CLI tests alone to verify API resource contracts, or on mocks alone to establish end-to-end success. Full-phase exits require code review and testing, not just checkboxes. Hosting is optional and inactive for preparation; later activation projects only an eligible phase before its first task.

## Scope and risk

Phase 1 has two cohesive delivery milestones; Phase 2 has three delivery milestones (2.1, 2.2, 2.4), its main final review 2.3 and the scoped range review 2.5. Range delivery is independent of unfinished stdin; numeric milestone order does not impose a dependency. Design preserves complete decoding and single BOM normalization before source-independent selection. Main API remains whole-input. Locale decoding, universal-newline translation, accidental second BOM stripping, borrowed-stream closure, checkout leakage into distribution checks and zero-test discovery are explicit verification risks. There are no unresolved material planning decisions.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/DECOMPOSITION.md

SHA-256: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`

```text
# TextStats component decomposition

The intended components refine [ARCHITECTURE.md](ARCHITECTURE.md). [SPEC.md](SPEC.md) owns normative public behavior.

| Component | Responsibility and collaborators | State / verification seam |
| --- | --- | --- |
| Statistics value | Immutable nonnegative integer lines/words; consumed by public callers and renderers | Frozen per-result data; construction and mutation checks |
| Text processing | One leading BOM policy, source-independent logical-line selection preserving contents/terminators, CR/LF line counting and Unicode whitespace words; returns statistics | Pure per-call text; table-driven unit checks |
| Named-file acquisition | Read bytes unchanged, strict complete UTF-8 decode, close its file handle; private decoded-text acquisition and whole-input public counting | Context-managed owned handle; real temporary-file and error checks |
| Public facade | Export TextStats, count_text, count_file directly from textstats | Import check and signature checks; no process side effects |
| Command adapter | Validate options, acquire the selected source, count, render once, map errors to diagnostics/status | Arguments and borrowed streams; subprocess checks for actual module entry |
| Module entry | Delegate process invocation to command adapter | Extracted-package module invocation |
| Product verification/distribution | Discoverable unit/integration suites, source archive with package/docs, extracted-source smoke check | Isolated temporary extraction; independent suite counts |

## Collaboration and ownership

`count_text` consumes caller text and owns only normalization/counting. `count_file` consumes a path and delegates after complete decoding. The command adapter delegates named-file acquisition and, at its later delivery boundary, reads borrowed stdin bytes until EOF. Read/decode failures propagate through the API; the CLI translates expected failures and produces no partial success output. The core cannot emit diagnostics.

Text formatting and JSON rendering consume the same statistics. Option validation precedes any input acquisition. The internal range selector consumes already normalized text and passes retained contents/terminators to counting without a second BOM normalization. It has no source dependency or public export. The command adapter validates one ordered positive ASCII range before acquisition, composes format/BOM options and invokes source-independent selection after complete decoding and one BOM normalization. Stdin acquisition remains separately scheduled; stdin ranges are unsupported.

No extra abstraction layer or focused child document is needed for this bounded utility. Source allocation belongs to layout, and delivery order belongs to PLAN.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/PROJECT.md

SHA-256: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`

```text
# TextStats project brief

TextStats is a small Python utility for people counting lines and words in UTF-8 files, and Python callers processing strings. Its public package is `textstats`, with the module CLI `python -m textstats`.

## Scope and constraints

Use Python 3.11+, the standard library and unittest. Deliver the named-file API/CLI first, then JSON output and byte-based stdin. Keep counting deterministic, API calls silent, input unchanged, diagnostics useful, and owned file resources closed. The complete behavioral contract is [SPEC.md](SPEC.md); structural responsibilities are in [ARCHITECTURE.md](ARCHITECTURE.md) and [DECOMPOSITION.md](DECOMPOSITION.md).

Provide importable immutable statistics, public API/module documentation, a runnable README, discoverable nonempty unit/integration tests, and an extracted-source distribution smoke check. Workflow fixture checks have their own test directory and cannot establish product acceptance.

## Boundaries

Named-file line ranges are part of the delivery hierarchy alongside JSON output and later byte-based stdin. Range selection is a named-file CLI option; public APIs count whole input and expose no range parameter or additional export. Source-independent decoded-text selection shares semantics with future source acquisition. Stdin line ranges are unsupported. Network services, GUI, encodings other than UTF-8, file mutation, plugins and performance guarantees for unbounded data are non-goals.

## Decisions

The preparation brief supplies the product requirements and phase/milestone identities. No material requirement decision remains open. Entire-input decoding is accepted: this keeps strict UTF-8 failures atomic and supports future selection after decoding. Memory use scales with input size; streaming optimization is outside the requested scope.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/layout.md

SHA-256: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`

```text
# TextStats physical layout

This maps intended [DECOMPOSITION.md](DECOMPOSITION.md) responsibilities. README, AGENTS and the pinned package already exist; proposed product paths below do not imply implementation. [PLAN.md](PLAN.md) owns delivery sequence.

| Location | Owner and contents |
| --- | --- |
| textstats/__init__.py | Public facade and direct exports; no CLI side effects |
| textstats/core.py | Immutable statistics, pure BOM normalization/logical-line selection and text semantics |
| textstats/io.py | Complete named-file bytes, strict decoding, private decoded-text acquisition and owned resource lifecycle |
| textstats/cli.py | Range/option validation, source dispatch, later borrowed stdin, output and process status |
| textstats/__main__.py | Minimal module entry delegating to CLI |
| tests/__init__.py, tests/unit/__init__.py, tests/integration/__init__.py | Importable unittest discovery packages |
| tests/unit/test_*.py | Nonempty semantic/API/lifecycle/adapter unit coverage |
| tests/integration/test_*.py | Nonempty actual API/file/module subprocess and distribution coverage |
| tests/workflows/ | Separate workflow fixtures; excluded from product acceptance counts |
| docs/api.md | Public API signatures, exceptions, lifecycle and usage |
| docs/module.md | Module CLI formats, option/source semantics and statuses |
| README.md | Preserve existing focus and SDD links; add runnable delivered product examples |
| docs/dev/ | Governing product documents and adjacent preparation QC reports |
| docs/dev/reports/phases/<id>/ | Later milestone and phase implementation review reports |
| docs/dev/reports/IMPLEMENTATION-REPORT.md | Later final implementation result/TODO aggregation |
| Makefile | Standard-library source-archive creation and check entry commands |
| dist/ | Generated source archives, excluded from tracked source |

## Placement and verification rules

A flat root package makes python -m textstats runnable from the checkout and extracted source without installation. Imports flow facade → core/io, io → core, cli → core/io, module entry → cli. CLI validation/formatting stays outside core and public exports. Internal range selection belongs in core decoded-text processing, with no acquisition dependency or public export; cli owns syntax and composes it with complete io acquisition.

Proposed unittest commands: python -m unittest discover -s tests/unit -t . and python -m unittest discover -s tests/integration -t .; workflow checks use their own explicit discovery invocation and counts. Product discovery packages and test modules must produce nonzero suites. Distribution checks create a temporary archive extraction, change to its root and invoke the extracted module with a clean import environment. The archive includes package sources, README and public docs, and excludes pinned workflow resources and generated archives. A Makefile using standard-library Python archive commands avoids runtime/build dependency additions.

Keep generated archive/extraction artifacts out of committed source. Preserve AGENTS.md and textstats-run-resources/ unchanged. No source, product test, packaging file or generated artifact is created during preparation. There are no unresolved placement choices.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/SPEC.md

SHA-256: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`

```text
# TextStats specification

The intended product serves Python callers and CLI users as defined in [PROJECT.md](PROJECT.md). Component owners are in [DECOMPOSITION.md](DECOMPOSITION.md); acquisition and counting depend only on the standard library. These contracts cover the complete main product, with delivery boundaries in PLAN. Named-file CLI line selection is included; public APIs remain whole-input. Line selection with stdin is unsupported.

## S-1 Public API and value

Python 3.11+ can import `TextStats`, `count_text` and `count_file` directly from `textstats`. `TextStats(lines: int, words: int)` is immutable and has nonnegative integer fields; invalid negative construction is rejected. `count_text(text: str, *, strip_bom: bool = True)` and `count_file(path: str | os.PathLike[str], *, strip_bom: bool = True)` return TextStats. API calls produce no stdout/stderr. The text-processing and facade components own these contracts.

## S-2 Text semantics

Remove exactly one leading U+FEFF when strip_bom=True; preserve interior BOMs, a second initial BOM, and every BOM when False. A retained BOM is ordinary non-whitespace. Count CRLF as one line terminator, lone CR/LF as terminators, and each terminator as one line. Add one for a nonempty final unterminated segment. Empty input has zero lines; a trailing terminator creates no phantom line. Other Unicode separators do not terminate lines. Words follow Python `str.split()` Unicode whitespace semantics. The pure text-processing component owns these rules for every source/format.

| Input notation | lines | words |
| --- | --- | --- |
| empty | 0 | 0 |
| `alpha beta` | 1 | 2 |
| `alpha\n` | 1 | 1 |
| `\n` | 1 | 0 |
| `alpha\r\nbeta\rgamma\n` | 3 | 3 |
| `alpha\n\n` | 2 | 1 |
| space and tab | 1 | 0 |
| `alpha\u2028beta` | 1 | 2 |
| BOM-only, default | 0 | 0 |
| BOM-only, retained | 1 | 1 |
| two leading BOMs, default | 1 | 1 |

## S-3 Named files and failure atomicity

Read named-file bytes and decode as strict UTF-8 without newline translation. Support str and os.PathLike[str] paths. Missing/unreadable files raise OSError subclasses; malformed bytes raise UnicodeDecodeError. API failures emit no partial result and no output; handles opened by the API close on success and failure. Inputs remain unchanged. Named-file acquisition owns lifecycle; callers retain exception control.

## S-4 Baseline CLI

`python -m textstats [--keep-bom] [--json] [--lines START:END] INPUT` accepts exactly one input; `--` permits dash-prefixed filenames. --keep-bom corresponds to strip_bom=False. Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout and leaves stderr empty. Help exits 0. Missing/extra input or unknown options exit 2 with useful stderr, empty stdout, no traceback and no input acquisition. Named-file input/read/decode failures exit 1, identify the input usefully on stderr, leave stdout empty and emit no traceback. CLI input remains unchanged. Optional named-file selection follows S-8; without --lines, count the whole input. The command adapter owns validation, rendering, diagnostics and status; the module entry exposes invocation.

## S-5 JSON

`--json` emits exactly one JSON object plus newline on success. Its only keys are lines and words, with integer values equal to the same input or selection's text counts. Key order and spacing are unrestricted. Text output remains the default, and BOM/source/error behavior is retained. Compose --json, --keep-bom and named-file --lines in either order before the -- separator. Rendering belongs to the command adapter.

## S-6 Standard input

INPUT `-` selects stdin at its later milestone. Read bytes until EOF, decode UTF-8 strictly independent of locale, and never close borrowed stdin. Empty stdin gives (0,0). Read/decode failures exit 1 with stderr identifying stdin, empty stdout and no traceback. Both output modes and BOM policies apply to whole-input stdin; --lines with INPUT - is unsupported. Named-file behavior remains available; `./-` addresses a named file literally called `-`.

## S-7 Documentation, tests and distribution

Public API/module documentation describes signatures, text/BOM rules, UTF-8 exceptions and lifecycle. The README provides runnable API/CLI examples, help, statuses, supported Python, unittest commands and delivered output/source options, including runnable named-file range examples, both option spellings, validation/status rules, complete decoding and single BOM normalization. Discoverable nonempty product tests live under tests/unit/ and tests/integration/; workflow fixture checks live separately under tests/workflows/ and cannot substitute for product checks. A source distribution contains an importable package and relevant documentation. A distribution check extracts it to an isolated directory and invokes that extracted source package with `python -m textstats`, establishing counts and CLI behavior without importing the working checkout. Named-file range distribution acceptance covers text/JSON, BOM policy and representative usage/read/decode failures. Test/distribution ownership is described in DECOMPOSITION.

## S-8 Named-file line selection

### Invocation and validation

Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.

### Selection semantics

Decode the entire named file as strict UTF-8 before selection; malformed bytes after END still fail. Apply the existing BOM policy exactly once to the complete decoded text before numbering. Default removes one leading U+FEFF, --keep-bom removes none. Number logical lines using only CRLF, lone CR and LF terminators; every terminator contributes one line, and a nonempty final unterminated segment contributes one. A trailing terminator adds no phantom line; empty normalized text has zero. Other Unicode separators remain contents.

Select the available intersection with inclusive START:END, preserving all selected characters and original terminators. Beyond EOF selects available lines or empty text. Count selected text under S-2 without BOM stripping again: an interior BOM exposed at the start of the selection remains ordinary non-whitespace. Unicode words use str.split semantics.

### Results and compatibility

Success text is exactly `lines=<N> words=<N>\n`, status0, empty stderr. --json produces one object/newline, only integer lines and words, equal to the same selection's text counts. Empty selection gives (0,0). Named-file read/decode errors retain status1, identifying stderr, empty stdout and no traceback; opened handles close, files remain unchanged. Public count_text/count_file remain silent whole-input calls with unchanged exports/signatures, exceptions and BOM policy. Without --lines, CLI output and error behavior satisfy S-4/S-5.

Normalization and selection operate on decoded strings independently of source acquisition, preserving compatibility with the borrowed-stdin adapter. Selection acceptance is named-file text/JSON only; stdin ranges and a public range API are unsupported.

### Objective selection acceptance

| Complete decoded input | Range | Expected lines / words |
| --- | --- | --- |
| `alpha beta\nbeta\nlast two` | 2:3 or 2:99 | 2 / 3 |
| same | 1:1 | 1 / 2 |
| same | 4:99 | 0 / 0 |
| `a\n\n` | 2:9 | 1 / 0 |
| `a\r\nb c\rd\n` | 2:3 | 2 / 3 |
| empty | 1:9 | 0 / 0 |
| BOM-only, default / keep | 1:1 | 0 / 0 and 1 / 1 |
| two leading BOMs, default | 1:1 | 1 / 1 |
| `a\n\ufeff\n` | 2:2 | 1 / 1 |
| `a\u2028b\nlast` | 1:1 | 1 / 2 |

Acceptance includes both option spellings/orders/formats, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout.

The command adapter owns syntax, option composition and rendering; named-file acquisition owns complete decoding and handle closure; pure text processing owns normalization, selection and counting. Public facade exports remain unchanged.

## Acceptance boundaries

Phase 1 milestone 1.1 demonstrates useful named-file counting, public API and module CLI with S-1/S-2/S-3 success and S-4 success/help/option handling. Milestone 1.2 establishes all S-3/S-4 failure/resource contracts and S-7 documentation/distribution exits. Phase 2 milestone 2.1 demonstrates S-5 while retaining phase 1 behavior; milestone 2.2 demonstrates S-6 and updated S-7 exits, with all prior acceptance retained. Evidence includes exact stdout/status/stderr checks, path/BOM/terminator cases, complete decoding and unchanged input. Neither passing a workflow fixture nor a zero-test discovery is product acceptance.

Named-file line-selection acceptance establishes S-8 and the affected S-4/S-5/S-7 obligations, retaining S-1–S-3 and whole-input behavior. It covers every selection example and rejection category above through actual named-file module invocation, both output modes, unchanged input and resource/error checks. It makes no stdin range claim and does not establish whole-project phase completion.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/TASKS-REVIEW-REPORT.md

SHA-256: `b887f9be642365bea340b932bf68ac4864575f147b4b5e6e8898e34fc9fe72c5`

```text
# TASKS review report

## Current gate

State: Ready for current TASKS.md conformance. Owner: sdd-tasks, 2026-10-05. Revision 4 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Retained original gate and identities (historical)

State: Ready. Owner assessment: sdd-tasks, 2026-10-04. Reviewed root TASKS; no focused children or active feature task list. Current PLAN/SPEC/design identities and upstream reports were checked before derivation. No confirmed issue or material open decision remains. This prepares 17 unchecked executable tasks. The current metadata recheck below records separately authorized maintained hosted tracking; no task range is implemented and no production code is delivered.

Reviewed and governing states:

- TASKS.md: SHA-256 `2e0af38698b5edf3911265da98815790143e2e5c1500b3bc04148ead2b9a8454`.
- PLAN.md: SHA-256 `8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8`.
- layout.md: SHA-256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- PLAN-REVIEW-REPORT.md: SHA-256 `01f3041e8ccd688060ff51e0c7dd825475d44dfbcca73c31910bab038e231591`.
- SPEC.md: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.
- SPEC-REVIEW-REPORT.md: SHA-256 `e4522d4a6d566d3dd6c7b208930547f152229ca3dd9a04028ce136a937a0df68`.
- PROJECT.md: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.

## Initial review

Manually mapped each PLAN outcome/exit to task scope, dependency and concrete evidence; compared against SPEC and design/layout ownership. Programmatically checked 17 unique monotonic IDs, six milestone parent groups, exact four-space checklist levels, forward-safe task prerequisites, one phase heading/root per phase and no checked completion. Checked local links and required future report paths. Product tests were not run because no product implementation/tests exist.

| Milestone | Delivery tasks | Excluded review tasks | Assessment |
| --- | --- | --- | --- |
| 1.1 | 3: T-001–T-003 | T-004 | Cohesive core → file API → actual CLI slice; narrow component seams with tests, no delayed mocked-only MVP |
| 1.2 | 3: T-005–T-007 | T-008 | API failure/lifetime, CLI diagnostics/docs and isolated distribution supply distinct bounded exits |
| 2.1 | 2: T-010–T-011 | T-012 | Explicit fragmentation review retained small group: renderer/interaction correctness and docs/extracted-source acceptance are useful coherent units. Further splitting introduces trivial/padding work; no subsystem-sized task hidden here. |
| 2.2 | 3: T-013–T-015 | T-016 | Borrowed byte acquisition, failure interactions and final docs/distribution are bounded compatible increments |
| 1.3 and 2.3 | 0 delivery, intentionally excluded | T-009 and T-017, exactly one each | Mandatory dedicated phase review milestones, not empty delivery groups |

| Planned outcome | Executable coverage |
| --- | --- |
| 1.1 S-1/S-2/S-3 success/S-4 useful path | T-001–T-004 |
| 1.2 full failures/lifecycle/S-7 release | T-005–T-008 and phase exit T-009 |
| 2.1 S-5 and retained named-file/docs/distribution | T-010–T-012 |
| 2.2 S-6/final S-7 and regressions | T-013–T-016 and complete exits T-017 |

Each delivery milestone ends with explicit code review/testing/repair/report work; final phase review depends on delivery milestone completion/closure, not itself. Review tasks have lifecycle-compliant report paths; T-017 includes final TODO aggregation. Nonzero product discovery, strict decoding, owned/borrowed resource checks, useful human demonstrations and checkout-independent extracted source invocation have executable coverage. Phase integration/publication gates and partial-range pause are preserved. Future range is excluded while the source-independent seam is maintained.

No findings or correction cycle. Preparation stops with all tasks unchecked and no hosted projection.

## Revision 1 — Hosted tracking metadata recheck

Owner assessment: sdd-tasks, 2026-10-04. No finding or correction to the accepted decomposition. The tracking workflow replaces the historical “No hosted objects are active” sentence with maintained mode and phase 1 context. Reviewed TASKS.md SHA-256: `1622d35a0bb4a61034e2b92fa52ed986f99cb54c96b49ff4087155af308df208`.

Compared every phase, milestone and task entry against the initial reviewed source at `4c275cc46fc0163c9e1e50871d3cc33c4c38567e`: hierarchy, scope, dependency, acceptance, prescribed checks and completion checkboxes are byte-for-byte unchanged. All other reviewed/governing inputs retain the hashes above. Counts, grouped PLAN/SPEC coverage and original no-finding assessment remain equivalent. Readiness: Ready for eligible phase 1 projection/implementation only when separately authorized; tracking metadata is not task completion. All 17 tasks remain unchecked. No product tests were run.

## Revision 2 — Authorized range reconciliation recheck

Transferred T-018–T-022 into Phase 2 once; retired independent source checklist in same change. Main IDs T-001–T-022 unique. Delivery task counts 1.1=3,1.2=3,2.1=2,2.2=3,2.4=3; excluded reviews T004/T008/T012/T016/T021 and final T009/T017/scoped T022. Retained two-task JSON outcome avoids trivial fragmentation; other groups have bounded seams, timely real command and docs/extraction acceptance. Dependencies preserve T012 baseline, no stdin dependency for ranges, and T017 requires main delivery completion including2.4. Checked historical review/parent claims explicitly retain reassessment pending. R1–R4 map T018–T022; all main routes remain covered. Four-space hierarchy, unique executable ownership, links and report lifecycle assessed. No completion inferred.

Exact reviewed/governing SHA256:

- TASKS.md: `558140529154e5ffdde1010b47a1dc6314be5cb286911cf6d81a9a5ae3512e62`
- PLAN.md: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- PLAN-REVIEW-REPORT.md: `c816262a759b9c5e6701f939dd07053e181585d24a8115605c8f2594d24d62ca`
- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- layout.md: `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`
- FEATURE-TASKS.md: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

## Revision 3 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-tasks under sdd-integrate-feature correction ownership, 2026-10-05.

T001–T022 unique, sole executable owner TASKS; FEATURE-TASKS pointer has zero checked executable tasks. Four-space hierarchy and stable dependency/report paths retained. Delivery counts1.1=3,1.2=3,2.1=2,2.2=3,2.4=3; excluded T004/T008/T009/T012/T016/T017/T021/T022. Two-task JSON group is bounded command+docs/extraction outcome, not trivial fragmentation. R1–R4/S8 map T018 helpers→T019 real command→T020 docs/extraction→T021/T022 review. All main contracts retain delivery routes. Progress entries are evidence, not conformance proof; T013–T017 and Phase2 remain unchecked. No scope/dependency changes in task delivery, no confirmed unresolved finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

Upstream gate identities at this recheck:

- `SPEC-REVIEW-REPORT.md`: `acea3e8790c31bc3906af83039c4d68c1d1a114a3c2cbe8361fc886da0711cde`
- `PLAN-REVIEW-REPORT.md`: `8b830a449363331db4931aa2684586b0caaeec28f3bf23263e301155a04403fe`

## Revision 4 — Final range incorporation and archive conformance

Selected complete main owner reassessment, 2026-10-05. Accepted contract/design scope unchanged; PLAN2.4 now refers to canonical S8/main QC, and TASKS references S8/main readiness with sole T018–T022 ownership. Historical feature sources and adjacent reports moved together into features/002_ea97182, with local links repaired; main roots are standalone intended descriptions. TASKS status/reassessment changes have implementation evidence in T021/T022 reports and do not alter task decomposition/dependencies. S1–S8 routes, delivery counts/rationale and boundary obligations from previous revisions remain applicable. Original findings/identities retained, no unresolved conformance finding. Main Phase2/stdin/final review remain incomplete.

Exact current reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e1aa667a8bea06ed9feb9211697a9d70ac3f75b688f1f877ee4d38443cd8c629`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`

Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/reports/phases/2/2.1.md

SHA-256: `e40773707191e76e109a2b0a9a5eb922add616933bd7c0b4053321d7de6fc872`

```text
# Milestone 2.1 — JSON output

T-012 milestone review, 2026-10-04, Python 3.12.14. Reviewed implementation at `27251ae6b73eb4179c422449abacc080051b49a0` on `phase/2-output-and-source-extensions`, target `main`, activation baseline `59debb649545125dd3aa00377ea115451b594271`. Constituent task results: T-010 `e97da0a98ecd6dd75f71ae682a409325a4b6d453`, T-011 `27251ae6b73eb4179c422449abacc080051b49a0`.

## Delivered capability and code review

Named-file commands support `--json`, emitting one object/newline with only integer lines and words. Text output remains exact by default. Both orders of `--json` and `--keep-bom` preserve shared count semantics, strict complete UTF-8 acquisition, useful diagnostics/statuses and unchanged input bytes.

Code review separately inspected all five production modules, unit/integration tests, public API/module guides, README and Makefile against S-5, retained S-1–S-4 and delivered S-7. The only production change is command-adapter parsing/rendering and its docstring: argparse validates before acquisition, both renderers consume the same immutable statistics, and standard-library JSON serialization stays outside core/acquisition. Rendering occurs only after complete successful counting; the narrow expected-error catch remains before either output path. API signatures, core semantics, binary file ownership/closure, facade exports and module entry are unchanged. No stdin/range branch is introduced.

Tests derive literal expected counts independently and reject missing/extra fields, string/boolean values, incorrect BOM policy, extra output and changed text defaults. Actual module subprocesses cover ordinary/empty/Unicode/mixed/trailing terminators, one/two BOMs, dash filenames and both option orders. Real missing/directory/malformed inputs and injected open/read/decode errors establish atomic diagnostics; usage checks establish no acquisition. Existing API silence, immutable/nonnegative values and resource checks remain active. Permission failure uses injection because privileged runtime permission bits are unreliable.

Distribution tests create and extract a fresh explicit source archive, clear checkout import variables, disable user site and assert the extracted package location before invoking text/JSON/BOM/help/error commands. Required source/docs are present and workflow resources/caches/generated output are excluded. Public guides accurately describe delivered JSON and planned stdin; README focus/disclosure links and whole-input API remain intact. The proportional-memory limitation remains documented.

## Findings and chronology

No product blocker or required repair found. Prior Phase 1 milestone/phase TODO sets are None. T-010's focused RED was observed before production changes: two test methods produced 30 behavioral failures because absent --json returned2. The narrow renderer then passed both methods. T-011 adds acceptance for existing delivered behavior and documentation, so its passing characterization has no manufactured RED. Earlier Phase 1 runner corrections remain in their historical reports.

Public README tarfile CLI extraction emits Python 3.12's existing deprecation warning concerning future extraction defaults; the example succeeds. Product test extraction explicitly requests the data filter when available. Python 3.11 compatibility was inspected; execution used 3.12.14 and makes no 3.11 runtime claim.

## Verification and exits

Fresh task-boundary checks at reviewed source with PYTHONDONTWRITEBYTECODE=1:

| Check | Observed result |
| --- | --- |
| python -m unittest discover -s tests/unit -t . -v | 17 pass, no skips; pure semantics, values, silent API/lifecycle, validation and atomic diagnostics |
| python -m unittest discover -s tests/integration -t . -v | 11 pass, no skips; real files/APIs, actual module JSON/default/error regressions and extracted-source identity/commands |
| JSON script-consumption demonstration | Parsed integer lines2/words3; status0, empty stderr, unchanged named bytes |
| README/API/module examples and links (T-011, unchanged) | All9 Python/shell blocks and local links pass, including both BOM orders, JSON consumer, source archive/extraction/help and expected nonexistent-file status1 |
| git diff --check | Pass |

All PLAN2.1 exits are verified: equal JSON counts for ordinary/BOM/empty/terminator inputs, retained exact text/default/errors, nonempty passing suites, runnable public docs, isolated extracted text/JSON invocation, distinct implementation code review and this report. Workflow fixtures supplied no product acceptance.

## Hosted state and stopping boundary

Phase 1 predecessor was explicitly reviewed/integrated/published at baseline59debb6, with issues1–9 completed and milestones1–3 closed. Phase2 label `sdd-phase-2-Output-and-source-extensions` ID12541856034, all native milestones4/5/6 and issues10–17 with exact task markers/initial associations were read back before T-010. T-010/#10 and T-011/#11 commits were normally pushed and provider ref equality verified; their issues closed/completed with evidence comments.

Persist/push T-012 report/status, close/read back #12, then close/read back milestone#4 containing exactly #10/#11/#12. Local milestone parent reconciliation follows actual closure. Phase2 remains incomplete: T-013–T-017 and milestones2.2/2.3 remain unchecked/open. Pause before stdin; retain the pushed phase branch without integrating into main or starting further tasks.

## TODO

None.

## Completed milestone reconciliation

T-012 report/status commit `ebecf1de74985acd3a9be62423c0a12e349b6586` was normally pushed and exact provider ref equality confirmed. #12 closed/completed with [evidence comment5984209263](https://github.com/pchemguy/Skill-Test-SDD-Manager-TextStats-20261004/issues/12#issuecomment-5984209263). Fresh connector title/marker/state checks confirmed #10/#11/#12 completed. Exact native milestone#4 listing contained only these three issues, all closed/completed, before closure; milestone#4 then read back closed with0 open/3 closed. Local milestone2.1 parent now reconciles to verified exits and observed closure. Phase2 remains incomplete and unintegrated; remaining tasks/hosted objects stay open. An unexpected untracked `-json-9l969okj/sample.txt` fixture was preserved/excluded from commits because ownership could not be established; it does not affect the product or archive checks. No further implementation starts.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/reports/phases/1/PHASE-REPORT.md

SHA-256: `56cbe118a8ed5cf052ffaf16e20d31b9055f1bbcdcfc1747944a3b3b68b144c9`

```text
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

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/reports/phases/1/1.2.md

SHA-256: `74e2848ec9a75ce51bee7b200a91fc60d6835dcd9b4da24649740f834e863c01`

```text
# Milestone 1.2 — Reliable documented distribution

T-008 review, 2026-10-04, Python 3.12.14, phase/1-named-file-utility. Reviewed clean production/test/docs/build source at 7939e1ccfe5bddea2733681e5bc77b2e9664ef9b. Constituent results: T-005 386c140, T-006 a436d3a, T-007 b686559 plus evidence/extraction correction 7939e1c.

## Delivered capability and implementation review

Inspected all five production modules, public guides/README, Makefile and product unit/integration tests against complete S-3/S-4, delivered S-7 and retained S-1/S-2. Code review was distinct from check execution.

The core remains pure, frozen and validated; BOM normalization occurs once, CRLF precedes CR replacement, Unicode words and final segments retain their established semantics. The facade exports only the three APIs and the guarded module entry delegates status. The file adapter uses binary context-managed whole-input reads and strict UTF-8; it emits nothing and returns only after successful read/decode/close. Real missing/directory/malformed cases plus injected open/read/decode/close failure seams establish portable failure acceptance, closure, silence and unchanged bytes. Permission denial is injected because permission bits are unreliable under this privileged runtime.

The CLI validates with argparse before acquisition; a narrow OSError/UnicodeDecodeError catch identifies the input and returns 1 before rendering. Other programming errors are not swallowed. Success remains exact text, help/usage status unchanged, both BOM policies and dash filenames retained. No JSON/stdin/range implementation is introduced.

Public signatures, BOM/line/word rules, exceptions, ownership, statuses and runnable examples align with delivered behavior. README focus and adoption/disclosure links are preserved. Makefile explicitly selects package/test sources and relevant documentation, excludes caches/workflow resources, and uses standard-library tar creation. Generated dist paths are ignored. Distribution tests build/extract in temporary directories, clear checkout-related import variables/disable user site, assert the extracted __file__, then invoke the actual module against real bytes. Product suite counts are independent and nonzero; workflow fixtures provide no acceptance.

## Findings and repairs

No unresolved product finding or exit blocker. The original milestone 1.1 TODO was None.

T-005 tests characterized already-correct lifecycle behavior, without a fabricated RED. A test import NameError was corrected before acceptance. T-006 observed 8 unhandled expected-error subtests and 6 actual-module diagnostic failures before the catch, followed by GREEN. T-007 observed missing make dist before archive implementation. Its example runner first used a wrong working directory, then rejected a successful extraction for known Python 3.12 tarfile deprecation stderr. The premature example-pass assertion in b686559 was explicitly corrected in 7939e1c; all examples were rerun successfully. Test extraction now selects the data filter when available and uses validated project paths on older Python 3.11. Those failures were runner/evidence corrections, not waived acceptance.

## Verification and exits

At reviewed source, using PYTHONDONTWRITEBYTECODE=1:

| Check | Actual result |
| --- | --- |
| python -m unittest discover -s tests/unit -t . -v | 17 passing, no skips; core/value, validation-before-acquisition, injected error/lifecycle contracts |
| python -m unittest discover -s tests/integration -t . -v | 9 passing, no skips; real APIs/files, actual CLI and isolated extracted distribution |
| Executed README/API/module Python and shell examples | Exact API assertions/counts, help/BOM/dash/error statuses and local links pass |
| Fresh normal/missing/malformed diagnostic demonstration | Normal stdout lines=2 words=3 plus newline, status0/empty stderr; errors status1/empty stdout/input-identifying stderr/no traceback |
| Fresh extracted source invocation | status0, exactly lines=2 words=3 plus newline, empty stderr |
| git diff --check | exit0 |

All PLAN 1.2 exits verified: atomic silent API failure/lifecycle, useful CLI diagnostics, unchanged files, nonempty independent suites, runnable public docs, isolated distribution invocation and explicit code review/report. No Python 3.11 interpreter was run; compatibility is inspected, actual runtime is 3.12.14. README tarfile CLI extraction emits a known deprecation warning on this runtime but succeeds; this warning concerns future tarfile defaults and does not invalidate counts or isolation.

The diagnostic and extracted-package demonstrations make release readiness reviewable. Issue closures for T-005–T-007 were verified after each result was pushed. This report/status commit and its #8 closure precede milestone #2 closure/readback; local parent reconciliation follows actual hosted state.

## TODO

None. No unresolved provenance from milestone 1.1.

## Next boundary

Proceed only to authorized Phase 1 review T-009 after milestone 1.2 persistence and closure. Phase 2 remains unselected, unprojected and unimplemented. Full-phase integration is still pending this milestone report.

## Suspension and final reconciliation

The human instructed gradual process suspension while T-008 report commit 3256b953383f9c8218e62a4c051d73e3ccd081bf was in its normal push. Existing scoped repository/workflow authority permitted completing this current task and eligible existing hosting reconciliation only. Push and exact remote containment were confirmed; #8 received the review evidence and closed with completed reason. The full milestone2 issue readback contained only #5–#8, all closed/completed; milestone2 then closed and read back with zero open/four closed issues. Milestone1 remains closed; milestone3/#9 remain open.

This final T-008 reconciliation records the local milestone parent and suspension. T-009 and Phase1 integration have not started. Retain the phase branch and stop after publication of this checkpoint. Main remains 4c275cc46fc0163c9e1e50871d3cc33c4c38567e. Phase1 is incomplete because its dedicated phase review/integration remain pending; no Phase2 activation or work occurred. No outstanding hosting effect remains for completed T-005–T-008.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/reports/phases/1/1.1.md

SHA-256: `227a5a7e0eda7616bd95d7c7167ed3a71abb84458f87139197030de25ef39734`

```text
# Milestone 1.1 — Named-file counting MVP

T-004 review completed 2026-10-04 on `phase/1-named-file-utility`, Python 3.12.14. Reviewed production/test source at `f2260a280b80fbbceb912594943a69c6075dcf07` with a clean worktree. T-001 is the historical `9b24dbd` core checkpoint; T-002 is `299670cbf19022fce5b12a8df1099857f1322ffb`; T-003 is the reviewed tip. This report/status is the T-004 result; its commit identity is discoverable by task ID.

## Delivered result

Python callers can directly import immutable `TextStats`, `count_text` and `count_file`. Named-file counting supports str and Path inputs, reads complete binary UTF-8 without newline translation, normalizes exactly one leading BOM when requested, preserves input bytes, and closes its owned success handle. `python -m textstats [--keep-bom] INPUT` prints exactly one text result. Help and option validation occur before acquisition; `--` enables dash-prefixed filenames.

## Implementation code review

Inspected all five production modules and the unit/integration tests against S-1/S-2, S-3 success, S-4 success/help/options, PLAN 1.1 and physical/component ownership. This was code inspection in addition to test execution.

- `core.py`: frozen nonnegative integer fields; one leading BOM only; CRLF replacement precedes lone CR normalization; final unterminated segment adds one; Unicode whitespace splits words without broad Unicode line splitting. No filesystem or process coupling.
- `io.py`: context-managed binary read and complete strict UTF-8 decode; invokes the same pure counter once with the caller's BOM policy. No input writes or output. Binary mode and absence of newline translation were established by inspection; the owned handle double verifies closure in addition to real integration success. Counting-equivalent newline translation is not independently detected by the count assertions.
- Facade/module entry: direct public exports, no invocation on import; guarded minimal CLI entry delegates status.
- `cli.py`: argparse requires one named input, disables option abbreviation, validates before count_file, and renders after a complete result. No JSON/stdin behavior was introduced. Expected input-error translation remains the explicitly planned T-006 reliability work.
- Tests: independent literal SPEC counts; real UTF-8 bytes and both path forms; exact subprocess stdout/stderr/status; help and invalid invocations; acquisition spy for ordering; byte preservation. Discovery is nonempty and separate by product suite. Documentation inspection found module/API docstrings consistent with delivered signatures and README accurately separating delivered and planned behavior.

Findings/blockers: None within milestone 1.1. No repair cycle was required. Missing/unreadable/decode failure campaigns, broader resource failures, full public guides and extracted distribution acceptance are required in milestone 1.2 and were not waived or claimed here.

## Verification and exit assessment

Actual checks at the reviewed source, with `PYTHONDONTWRITEBYTECODE=1`:

| Command / evidence | Observed result and contract |
| --- | --- |
| `python -m unittest discover -s tests/unit -t . -v` | 14 tests, exit 0, no skips: S-1/S-2 samples/value/signature/silence; owned success closure; validation before acquisition |
| `python -m unittest discover -s tests/integration -t . -v` | 6 tests, exit 0, no skips: public file API, real bytes/paths, API/CLI agreement, exact module results, help/options and dash paths |
| Direct API/module demonstration with temporary normal and BOM files and dash-prefixed relative paths | Normal: `lines=2 words=3\n`; BOM default: `lines=1 words=0\n`; BOM retained: `lines=1 words=1\n`; all exit 0, stderr empty, API counts equal and bytes unchanged |
| `python -m textstats --help` | Exit 0; describes INPUT and --keep-bom; no stderr |
| `git diff --check` | Exit 0, no output |

T-002 test-first evidence observed three missing-export assertions before production work, followed by three focused passing tests. T-003 observed twelve assertion/subtest failures across five tests for the absent adapter/module capability, then five focused passing tests. Actual runs are retained in the consumer evidence. T-001 RED history is prior task evidence; this review did not recreate or independently certify its historical sequence. Passing discovery and review establish this milestone's acceptance, not future phase or distribution correctness. Workflow fixtures were not used as product acceptance.

All PLAN 1.1 exits are satisfied: usable named-file API/module invocation, exact counts and process output, BOM/terminator/path examples, unchanged input, nonempty relevant suites, code review and this committed report. Demonstration makes the command syntax and retained BOM effect reviewable; the human retains the continue/amend/simplify/stop decision.

## TODO

None.

## Persistence and stopping boundary

Task issue identities #1–#4 were resolved by exact titles and task body markers in the designated repository. T-002/T-003 results were individually committed, pushed and remote-confirmed, then their issues closed with completion evidence. T-004 report/status publication and issue closure precede milestone closure/readback. Hosted state remains separately observed by the execution workflow. Final reconciliation read back issues #1–#4 closed with completed reason and milestone #1 closed with zero open/four closed issues. The local milestone checkbox is reconciled in the subsequent T-004 boundary commit.

Stop after verified milestone 1.1 persistence and reconciliation. T-005 onward and milestones 1.2/1.3 remain incomplete. Phase 1 remains open and is not merged into main; phase 2 is not activated. This is a useful MVP checkpoint, not complete product or phase acceptance.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-SPEC-REVIEW-REPORT.md

SHA-256: `ef039d1d5b3f5a3c2ecf73754b2873d1435b5264e63164d313360199f524a7e3`

```text
> Historical feature preparation QC. Original observations/identities are retained; main adjacent QC reports govern current use.

# Range FEATURE-SPEC review report

## Current gate

State: Ready for current FEATURE-SPEC.md conformance. Owner: sdd-specify, 2026-10-05. Revision 2 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Initial review

Compared every request range contract against R-1–R-4 and accepted main design, inspected current core/io/cli/export seams and relevant tests. Existing design already allocates validation, full decode, BOM normalization and pure selection; no architecture overlay required. Main S-6 delivery remains unchanged.

| Coverage | Evidence / result |
| --- | --- |
| R-1 | Every syntax/repetition/ASCII/positivity/order case and unbounded decimals covered; pre-acquisition status2 explicit |
| R-2 | Strict full decoding, preserved CRLF/CR/LF, EOF and single BOM policy covered; no Unicode splitlines assumption |
| R-3 | Both renderers, unchanged whole-input API, lifecycle/error atomicity and stdin exclusion covered |
| R-4 | Objective supplied examples, interior BOM/Unicode, public docs/nonempty suites/extracted module evidence covered |

No confirmed finding or correction cycle. Structural ownership and directed dependencies match accepted main design. Endpoint representation remains an internal choice with an assessable no-limit contract.

## Reviewed identities

- `FEATURE-SPEC.md` SHA256 `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`.
- `PROJECT.md` SHA256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- `ARCHITECTURE.md` SHA256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- `DECOMPOSITION.md` SHA256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- `SPEC.md` SHA256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.
- `features/002_ea97182/README.md` SHA256 `a1b81bc6c130e03020d03591c751dd6cdc4251a348927f814aee52bb2999c86e`.

## Revision 1 — Authorized range reconciliation recheck

R-1–R-4 unchanged and exactly represented by S-8 plus S-4/S-5/S-7. Current main SPEC incorporation changes no feature behavior; design already owns parsing/acquisition/normalization/selection/rendering seams. All contract groups and no-public-API/stdin boundary reviewed; no correction required.

Exact reviewed/governing SHA256:

- FEATURE-SPEC.md: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- PROJECT.md: `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`
- ARCHITECTURE.md: `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`
- DECOMPOSITION.md: `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`

## Revision 2 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-specify under sdd-integrate-feature correction ownership, 2026-10-05.

R1–R4 preserved exactly; current main S8 represents complete accepted selection behavior and affected S4/S5/S7. PROJECT/design/layout incorporation establishes canonical pure selection and private complete decode without public API changes. Feature contract remains accepted active source pending feature conclusion/archive. No confirmed unresolved finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/IMPLEMENTATION-REPORT.md

SHA-256: `304d6a7007281a9b1d078bd97fa280feaf32c48bc286b2017038193e984df782`

```text
# Named-file range implementation result

Feature002_ea97182, T-018–T-022. Named-file `--lines START:END`/`--lines=START:END` selects inclusive logical lines in text or JSON, with unbounded positive ASCII endpoints, pre-acquisition syntax/repetition validation, full strict UTF-8 decoding, one BOM policy and preserved contents/terminators. Public APIs remain whole-input; no stdin or public range API is delivered.

Task commits: T018905d7a851124235db27f4f5a553ee39729957a44; T0199ade315a9f6ded1fade6f457a504f5e07e58fba5; T020749a89844249d3b1c5ebb04c459d7e66bcb3ed2e; T0213f93cd40d90001ee7e4f54b36c764d1d5067b72e. T022 status/report/archive publication concludes this feature branch; Git identifies its commit by task ID. Separate feature and merged-state acceptance/publication are recorded in the phase report and explicit merge commit.

[Milestone2.4](2.4.md) and [feature phase review](PHASE-REPORT.md) establish code review, independent unit21/integration13, examples, error/lifecycle/API regressions and isolated extracted-source acceptance. Main governing owners/QC and unique TASKS ownership are reconciled; historical sources/adjacent reports are retained here. Prior TASK-QC-1 is resolved in archived FEATURE-TASKS-REVIEW-REPORT Revision1. No unresolved implementation findings or deferred TODOs exist; TODO: None. No full-project implementation report is claimed.

Initial hosted closure18 returned an unknown preHTTP exit2; scoped assisted same-adapter recovery and consumer readback confirmed completion, preserving the diagnostic limitation without inferring platform rejection. A later readonly19 transport failure was resolved by connector readback after successful adapter closure. Other writes remain through the established protected adapter; no credential/helper inspection or denied-write transport bypass.

Integration target is paused phase/2-output-and-source-extensions at ea97182d2d6a3984599238312a13e78d54d3221a. Main59debb649545125dd3aa00377ea115451b594271 remains unchanged. Stop after verified explicit feature→phase2 merge publication, retaining incomplete stdin2.2/main review2.3/T013–T017 and Phase2 status. Unrelated untracked sample remains excluded and unchanged.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/PHASE-REPORT.md

SHA-256: `de0900dd513199936f5e9726373ffbf2680b5ed66c666f9ec1a5cc4d2246152b`

```text
# Named-file range feature phase review

T-022, feature002_ea97182, baseline ea97182d2d6a3984599238312a13e78d54d3221a, 2026-10-05. Reviewed published feature source at 3f93cd40d90001ee7e4f54b36c764d1d5067b72e plus final source/archive/owner-reference and status reconciliation. Delivery milestone2.4/#7 is independently read back closed with0open/4closed; #18–#21 closed/completed after verified publication. This is scoped range review2.5, not main phase reviewT017.

## Cross-component code review

Reinspected all five production modules and their dependency/resource boundaries separately from executing tests. Checked normalized decimal ordering/EOF-only clamping, repetition action, complete UTF-8 decode before selection, owned handle closure, exactly-one complete-input BOM normalization and disabled slice stripping, preserved CRLF/CR/LF/Unicode/EOF content, exact atomic text/JSON output and unchanged whole-input facade/API signatures/exceptions/silence. Pure selection has no acquisition/process dependency or public export. Reviewed new semantic/validation/resource/module/distribution checks plus retained core/file/CLI tests, public docs/build placement. No bugs, critical issues, contract violations or unresolved findings. No production repair required; prior T021 docstring clarification is retained.

## Verification and acceptance

Python3.12.14; product root independent commands:

- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/unit -t . -v`: 21 tests, passed/no skips.
- `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests/integration -t . -v`: 13 tests, passed/no skips.
- Public Python/module examples run in temporary directories with expected statuses; build/extraction separately verified by the product integration suite.
- Final main/archive local-link and unique task-owner checks, governing owner QC and `git diff --check` pass.

S-8/R1–R4 supplied rows and all required syntax/ASCII/leading-zero/huge-decimal/repetition-before-acquisition cases, exact module text/JSON/option orders, complete decoding including bytes after END, BOM/terminator/Unicode/empty/EOF cases, API/default/help/dash behavior, file preservation and resource/error regressions are verified. Extraction asserts actual extracted package identity with checkout import settings removed and exercises ranges/text/JSON/BOM/usage/read/decode behavior. No workflow fixture supplies product acceptance. Python3.11 compatibility is designed but was not executed. Complete-input memory scaling remains accepted; no streaming/performance guarantee is claimed.

## Incorporation, lifecycle and result

Accepted PROJECT/design/layout concerns are incorporated with main SPEC/PLAN/TASKS, maintaining one executable task entry per stable ID. All necessary owners and affected preparation QC are independently reconciled; original observations remain historical. Sources and adjacent feature QC are archived under this campaign with repaired local links and historical-only status. Implementation reports stay under the feature campaign. Current S8 requirements are main-owned; unfinished stdin/main review has current TASKS owners.

Affected historical completion reassessment notes for prior named-file/JSON reviews and parents are resolved against current scoped regression evidence without discarding their historical reports or claiming stdin/fullPhase2 completion. Main Phase2/T013–T017 remain unchecked. T018 helper RED and T019 actual-command RED/GREEN history is recorded in 2.4; T020 characterizes delivered behavior without manufacturing RED.

Prior preparation TASK-QC-1 resolved in retained FEATURE-TASKS QC Revision1. Milestone2.4 found no product TODOs; this cross-component review adds none. TODO: None. [IMPLEMENTATION-REPORT](IMPLEMENTATION-REPORT.md) aggregates the scoped result.

Report/task/status commit and push precede #22/#8 closure and final integration. After coherent feature acceptance and complete-difference inspection, integrate with an explicit two-parent merge into phase/2-output-and-source-extensions, verify the merged state and publish the target. The merge commit records actual pinned parents and merged checks. Stop there; feature completion is distinct from published integration, and Phase2 remains incomplete.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-TASKS-REVIEW-REPORT.md

SHA-256: `23c779b2effa874428e311dd11e74a4202ae90e0a57bc4f0baf0bb2fed09b958`

```text
> Historical feature preparation QC. Original observations/identities are retained; main adjacent QC reports govern current use.

# Range FEATURE-TASKS review report

## Current gate

State: Ready for current FEATURE-TASKS.md conformance. Owner: sdd-tasks, 2026-10-05. Revision 3 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Initial review

Initial FEATURE-TASKS SHA256 `c6b3026adac6236a27b1722a560053290ce30432dbe4fbc62522921e5580200a`. Governing PLAN/SPEC gates were persisted and current before derivation. Mapped2.4/2.5 outcomes to helper, actual command, docs/distribution and explicit milestone/phase review work. Reviewed bounded component breadth, end-to-end timing and dependency feasibility; T-012 supplies completed prerequisite, stdin tasks retain independent unfinished ownership.

| Milestone | Delivery count | Excluded reviews | Assessment |
| --- | --- | --- | --- |
| 2.4 | 3:T-018–T-020 | T-021 | Cohesive pure/acquisition seam, command behavior, docs/distribution; actual command integration precedes release, no subsystem-sized or trivial unit |
| 2.5 | 0, intentionally excluded | T-022, exactly one | Dedicated feature-scoped phase review; cannot close main Phase2 |

| Coverage | Tasks |
| --- | --- |
| R-2/R-3 decoded normalization/selection/API/resources | T-018, retained checks T-019/T-021/T-022 |
| R-1/R-3 actual text/JSON and usage/failure composition | T-019, reviews T-021/T-022 |
| R-4/S-7 public examples/help/extracted source | T-020, reviews T-021/T-022 |

| Finding | Location / consequence | Correction / objective recheck | Disposition |
| --- | --- | --- | --- |
| TASK-QC-1 | T-019 evidence did not explicitly require decimal-conversion-limit and mixed repeated-spelling cases; otherwise a capped converter or last-wins parser could evade intended acceptance | sdd-tasks: name both cases without changing R-1 or strategy; recheck request→SPEC→PLAN→task evidence | Resolved in Revision1 |

## Revision 1

Corrected only T-019 evidence to explicitly require endpoints beyond interpreter conversion limits, valid huge/beyond-EOF/reversed numbers, and duplicate options in separate/equal/mixed spellings. Recompared R-1 and PLAN2.4 exits; no upstream behavioral/strategy change. Programmatic document checks passed:17 unique main IDs plus5 disjoint IDs18–22, exact four-space three-level checklist, exact Phase2 identity, two milestone parents and5 unchecked tasks, dependency chain/join and2.4 closure gate. Checked local links and blank heading spacing. Git comparison confirms source/tests/docs/build/main TASKS/PLAN/layout/instructions unchanged from baseline; unknown fixture hash unchanged. No product tests executed for document-only preparation. Counts/ownership/coverage rechecked; no remaining blocker.

## Current reviewed identities

- `FEATURE-TASKS.md` SHA256 `7734ece5dec88c86e04b6163b06c49dd78236d23fa1337fc04e4a988554de73b`.
- `FEATURE-PLAN.md` SHA256 `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`.
- `FEATURE-PLAN-REVIEW-REPORT.md` SHA256 `df68f887aada16b7f822c5952852a1fc89c245231704596d242fe536fde10dcc`.
- `FEATURE-SPEC.md` SHA256 `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`.
- `FEATURE-SPEC-REVIEW-REPORT.md` SHA256 `bc194a3f729794c3156357813db75630470e9c4d07f48277c924e6c7498ec1e6`.
- `TASKS.md` SHA256 `3523f6c900f776a0b1d90ce389295dc63650c9b54c5379121d6e85449a1fe9c1`.
- `layout.md` SHA256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- `DECOMPOSITION.md` SHA256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.

## Revision 2 — Authorized range reconciliation recheck

Feature task pointer has zero independently executable entries after authorized transfer. T018–T022 remain stable, unchecked and solely in main TASKS. Original five-task decomposition/evidence unchanged at receiving owner; current main QC governs execution. No duplicate task ownership or hidden completion. Historical preparation remains retained.

Exact reviewed/governing SHA256:

- FEATURE-TASKS.md: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`
- TASKS.md: `558140529154e5ffdde1010b47a1dc6314be5cb286911cf6d81a9a5ae3512e62`
- TASKS-REVIEW-REPORT.md: `9c299a81273ac9ba9db9f503de925b7f751cf49095c4fb58b73185986f47f459`
- FEATURE-PLAN.md: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`

## Revision 3 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-tasks under sdd-integrate-feature correction ownership, 2026-10-05.

Pointer remains zero independently executable entries; stable T018–T022 solely in main TASKS. Current design/main upstream ownership changes do not alter accepted task contracts or dependencies. No duplicated task owner or hidden completion. Feature pointer remains active pending final source/evidence disposition; no confirmed unresolved conformance finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-PLAN-REVIEW-REPORT.md

SHA-256: `40bc5abdd0139d1b9c084dcdecfeb9940b3f4ad2bf7deca7bc9279b7432e3dd7`

```text
> Historical feature preparation QC. Original observations/identities are retained; main adjacent QC reports govern current use.

# Range FEATURE-PLAN review report

## Current gate

State: Ready for current FEATURE-PLAN.md conformance. Owner: sdd-plan, 2026-10-05. Revision 2 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.

## Initial review

Mapped R-1–R-4 to milestone2.4 delivery/exits and2.5 feature review; checked useful changed module path, prerequisite seam, complete decoding/normalization/API/lifecycle/failure regressions, docs/extracted distribution and physical owners. Existing Phase2 IDs/names and main2.1–2.3 preserved. Explicit feature-only review cannot complete main Phase2 or replace T-017. T-012 supplies usable named-file JSON baseline; waiting for unimplemented stdin would contradict the named-file delivery boundary. Added active-phase objects are projected only before separately authorized execution.

| Phase | Delivery milestones | Excluded review | Assessment |
| --- | --- | --- | --- |
| 2, feature delta | 1:2.4 | 2.5 single feature phase review | Explicit fragmentation review: bounded one-option named-file capability, existing format/core retained. Helper→CLI→docs has cohesive scope, timely real integration and objective release evidence; padding creates overhead. |

| Contracts | Route |
| --- | --- |
| R-1/R-2 | Normalized text seam and validated named-file CLI integration2.4 |
| R-3 | Both renderers, atomic failures, API/default regressions2.4; aggregate review2.5 |
| R-4/S-7 | Independent product checks, runnable docs/extracted-source2.4; aggregate2.5 |

No confirmed issue or correction cycle. New phase numbering would incorrectly gate named-file work on unfinished stdin; retaining active Phase2 with scoped new milestones respects the baseline and predecessor lifecycle. Main acceptance updates are deferred to explicitly authorized accepted incorporation, not silently changed here.

## Reviewed identities

- `FEATURE-PLAN.md` SHA256 `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`.
- `FEATURE-SPEC.md` SHA256 `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`.
- `FEATURE-SPEC-REVIEW-REPORT.md` SHA256 `bc194a3f729794c3156357813db75630470e9c4d07f48277c924e6c7498ec1e6`.
- `PLAN.md` SHA256 `8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8`.
- `layout.md` SHA256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- `ARCHITECTURE.md` SHA256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- `DECOMPOSITION.md` SHA256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- `TASKS.md` SHA256 `3523f6c900f776a0b1d90ce389295dc63650c9b54c5379121d6e85449a1fe9c1`.

## Revision 1 — Authorized range reconciliation recheck

Feature 2.4/2.5 strategy remains equivalent against expanded SPEC and incorporated PLAN. Three delivery tasks plus milestone review and one scoped final review fit bounded named-file slice. No stdin dependency; no main phase completion claim. Main strategy contains both outcomes; accepted feature plan remains active until final archive.

Exact reviewed/governing SHA256:

- FEATURE-PLAN.md: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- FEATURE-SPEC.md: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- PLAN.md: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- layout.md: `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`

## Revision 2 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-plan under sdd-integrate-feature correction ownership, 2026-10-05.

Feature2.4 has three bounded delivery tasks and explicit reviewT021; excluded2.5 final scoped reviewT022. Single narrow delivery milestone retained for cohesive named-file range outcome, avoiding artificial text/JSON splitting. Updated main owners preserve routes and independent-of-stdin dependency; hosted closure precedes T022 and full verified incorporation precedes archive/integration. No confirmed unresolved conformance finding; hosting transition blocker is execution state.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-PLAN.md

SHA-256: `f2deac1776918a83fadc5779db601c75ee81efa7a1e4ff6d87e96a8b0d2c6398`

```text
> Historical accepted feature source. Current governing behavior, strategy and executable progress are in main [SPEC](../../SPEC.md), [PLAN](../../PLAN.md) and [TASKS](../../TASKS.md). This snapshot is not an executable task owner.

# Named-file line ranges delivery plan

Active delta: [FEATURE-SPEC](FEATURE-SPEC.md), [package identity/design](README.md). The reviewed specification is Ready. Preserve main [PLAN](../../PLAN.md) and [TASKS](../../TASKS.md): JSON2.1 is complete at T-012; stdin2.2 and main review2.3 remain incomplete. This feature reuses Phase2's identity with new feature-only milestone IDs2.4/2.5, allocated after existing2.1–2.3. Numerical order does not impose a stdin dependency. Feature progress measures only the delta and cannot complete Phase2.

## Phase 2 — Output and source extensions

### Milestone 2.4 — Named-file line ranges

Prerequisite: completed/published JSON milestone2.1/T-012 at the pinned paused baseline, current feature SPEC/design QC and separately authorized implementation. No prerequisite on unfinished stdin or main final review; whole-input named-file text/JSON already works. Delivery retains the useful baseline while introducing a source-independent normalization/selection seam, then composing command validation/acquisition/rendering into a named-file slice. Pure helper work is a bounded prerequisite to the earliest usable changed CLI path, not a released skeleton.

Scope: R-1–R-4 and retained S-1–S-5/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded decimals, text/JSON and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.

Exit: actual module invocation counts selected named-file lines in text/JSON with exact stdout/status/stderr; supplied examples, ASCII/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.

### Milestone 2.5 — Range feature review

Dedicated single feature-scoped phase review/testing/report outcome after delivery milestone2.4 completes/closes when tracking is active. Exit: cross-component range/API/BOM/format/decode/lifecycle/docs/distribution acceptance, prior finding disposition, blocker repair and committed/pushed feature phase report. Aggregate feature TODOs and final feature implementation report. This is not main milestone2.3/T-017 or a whole-project Phase2 completion claim.

A full separately authorized feature implementation must incorporate accepted in-scope feature documents and reconcile task ownership before final feature merge into the established paused phase target; main stdin tasks retain incomplete state. Incorporation triggers affected main QC and rechecks changed review dependencies without renumbering T-017. Preparation stops on the published feature branch before implementation, incorporation/archive or merge.

## Layout and integration constraints

Reuse [layout](../../layout.md): core owns pure normalization/selection/counting; io owns complete named-file UTF-8 acquisition; cli owns validation, command composition, diagnostics and renderers. Private acquisition factoring may allow the command to obtain decoded text while count_file remains whole-input. The selected slice is counted with stripping disabled. Future stdin can call the same decoded-text seam; no borrowed source is acquired/delivered in this feature.

Pure/helper and parser/lifecycle checks belong under tests/unit; real file/module and isolated extraction checks under tests/integration. README/docs/module describe the feature; docs/api retains whole-input signatures. Existing Makefile archive includes updated package/docs with no workflow fixture substitution. Feature review reports reside under features/002_ea97182; preparation QC reports remain adjacent to active FEATURE roots. No new source home or main layout edit is required.

## Activation, risks and boundary

Preparation creates no label, milestone, issue or PR. If separately implemented while Phase2 remains active, project the added feature work in that active phase before first execution, preserving managed IDs and existing issue/milestone ownership. The feature delta must not close Phase2 or existing2.2/2.3.

Primary risks: argparse silently accepts repeats; unrestricted integer-string conversion hits interpreter limits; splitlines treats Unicode separators as terminators; range processing strips an interior BOM twice; slicing hides late bad UTF-8; helper factoring changes whole-input APIs/resources; distribution imports the checkout. Planned evidence explicitly addresses these risks. One delivery milestone plus mandatory feature review is intentionally small: the bounded named-file option has one coherent changed end-to-end outcome, and splitting text/JSON or validation into artificial release milestones delays usefulness. No unresolved delivery decision remains.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-SPEC.md

SHA-256: `3ea5af202942b72ac743c400a5cc810932d65e2e9f66e046b2911da5d511fe08`

```text
> Historical accepted feature source. Current governing behavior, strategy and executable progress are in main [SPEC](../../SPEC.md), [PLAN](../../PLAN.md) and [TASKS](../../TASKS.md). This snapshot is not an executable task owner.

# Named-file line range specification

Active scoped delta for [feature002_ea97182](README.md), based on completed JSON milestone2.1/T-012. Extend main [SPEC](../../SPEC.md) S-4/S-5/S-7; preserve S-1–S-3 and unaffected S-4/S-5 behavior. S-6/stdin remains later main delivery, with source-independent compatibility required by [architecture](../../ARCHITECTURE.md). Public API stays whole-input: no new export or range parameter.

## R-1 Invocation and validation

Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.

## R-2 Selection semantics

Decode the entire named file as strict UTF-8 before selection; malformed bytes after END still fail. Apply the existing BOM policy exactly once to the complete decoded text before numbering. Default removes one leading U+FEFF, --keep-bom removes none. Number logical lines using only CRLF, lone CR and LF terminators; every terminator contributes one line, and a nonempty final unterminated segment contributes one. A trailing terminator adds no phantom line; empty normalized text has zero. Other Unicode separators remain contents.

Select the available intersection with inclusive START:END, preserving all selected characters and original terminators. Beyond EOF selects available lines or empty text. Count selected text under S-2 without BOM stripping again: an interior BOM exposed at the start of the selection remains ordinary non-whitespace. Unicode words use str.split semantics.

## R-3 Results and compatibility

Success text is exactly `lines=<N> words=<N>\n`, status0, empty stderr. --json produces one object/newline, only integer lines and words, equal to the same selection's text counts. Empty selection gives (0,0). Named-file read/decode errors retain status1, identifying stderr, empty stdout and no traceback; opened handles close, files remain unchanged. Public count_text/count_file remain silent whole-input calls with unchanged exports/signatures, exceptions and BOM policy. Default CLI behavior regresses successfully.

Source-independent normalization/selection is testable on decoded strings and supports a later borrowed-stdin adapter without implementing stdin now. This feature's acceptance is named-file text/JSON only; no stdin range CLI claims or new public API.

## R-4 Acceptance and delivery documentation

| Complete decoded input | Range | Expected lines / words |
| --- | --- | --- |
| `alpha beta\nbeta\nlast two` | 2:3 or 2:99 | 2 / 3 |
| same | 1:1 | 1 / 2 |
| same | 4:99 | 0 / 0 |
| `a\n\n` | 2:9 | 1 / 0 |
| `a\r\nb c\rd\n` | 2:3 | 2 / 3 |
| empty | 1:9 | 0 / 0 |
| BOM-only, default / keep | 1:1 | 0 / 0 and 1 / 1 |
| two leading BOMs, default | 1:1 | 1 / 1 |
| `a\n\ufeff\n` | 2:2 | 1 / 1 |
| `a\u2028b\nlast` | 1:1 | 1 / 2 |

Acceptance includes both option spellings/orders/formats, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout. No unresolved behavioral decisions remain.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/README.md

SHA-256: `d2dc7a1e1c1ae2dad047e3fa4def813999fadcc10677f98ab554168bc4167634`

```text
# Named-file line ranges feature

Campaign: `002_ea97182`. Baseline: `ea97182d2d6a3984599238312a13e78d54d3221a`.
Working branch: `feature/002_ea97182-line-ranges`. Integration target: `phase/2-output-and-source-extensions` in pchemguy/Skill-Test-SDD-Manager-TextStats-20261004. Main remains `59debb649545125dd3aa00377ea115451b594271`.

Authorized delivery: implement named-file text/JSON selection, incorporate governing owners, project maintained tracking and integrate into the paused phase target after verification. Stop before stdin or later phase execution. T-012 is complete; T-013–T-017/stdin remain unfinished. Preserve their identities and current acceptance.

Historical sources and adjacent preparation QC are archived here: [FEATURE-SPEC](FEATURE-SPEC.md), [FEATURE-PLAN](FEATURE-PLAN.md), [FEATURE-TASKS](FEATURE-TASKS.md). Main [PROJECT](../../PROJECT.md), [ARCHITECTURE](../../ARCHITECTURE.md), [DECOMPOSITION](../../DECOMPOSITION.md), [SPEC](../../SPEC.md), [PLAN](../../PLAN.md), [layout](../../layout.md) and sole executable [TASKS](../../TASKS.md) incorporate accepted range scope. Archived sources/checklists are historical, not current executable owners. [2.4 report](2.4.md), [feature phase review](PHASE-REPORT.md) and [feature implementation report](IMPLEMENTATION-REPORT.md) retain implementation provenance. Feature integration into paused phase2 is a separate verified/published transition; Phase2/stdin remains incomplete.

## Design decision

Reuse [ARCHITECTURE](../../ARCHITECTURE.md) and [DECOMPOSITION](../../DECOMPOSITION.md): command validation → complete named-file byte decoding → one leading BOM normalization → pure logical-line selection → count_text with stripping disabled → existing text/JSON rendering. Whole-input APIs retain signatures/exports and lifecycle. Internal acquisition may share a private decode helper with count_file; selection and normalization have no file/stdin dependency. Counting a selected slice never removes an exposed interior BOM. No new abstraction layer, public range API, encoding or stdin delivery is needed. Existing layout places pure helpers in core, acquisition in io, validation/rendering in cli, product tests in unit/integration and workflow fixtures separately.

The selector recognizes only CRLF/CR/LF and preserves original contents/terminators; str.splitlines would violate the Unicode-separator contract. Endpoint parsing/comparison must accept arbitrarily long ASCII decimals without Python's configured integer-string conversion limit becoming a usage rejection (normalized decimal strings or incremental conversion are viable internal choices). Memory scales with complete input, as accepted by the main design.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/FEATURE-TASKS.md

SHA-256: `5fa674945d145e00e76f0a90ae7a8f6ee0b701fa711ed89f2e35cd61117e16b0`

```text
> Historical accepted feature source. Current governing behavior, strategy and executable progress are in main [SPEC](../../SPEC.md), [PLAN](../../PLAN.md) and [TASKS](../../TASKS.md). This snapshot is not an executable task owner.

# Named-file range task ownership

T-018–T-022 are transferred once to [TASKS.md](../../TASKS.md), preserving IDs, dependencies, incomplete status and feature report paths. TASKS is their sole executable owner. [FEATURE-PLAN](FEATURE-PLAN.md) and [FEATURE-SPEC](FEATURE-SPEC.md) remain active accepted deltas until final verified incorporation/archive. This pointer is not a checked task list.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/features/002_ea97182/2.4.md

SHA-256: `630d94bf1e4d69368c329b05d2968b88ed3fd335301ffa1e00fd7c3db58ab3e1`

```text
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

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats/cli.py

SHA-256: `89856582e849bf17d31d363e85d22cc1440c561b20f3e7818901819fa41341a5`

```text
"""Validate named-file arguments and render whole-input or selected counts."""

import argparse
import json
import sys
from collections.abc import Sequence

from .io import count_file, _read_text
from .core import _normalize_text, _select_lines, count_text


def _parse_range(value: str) -> tuple[str, str]:
    """Validate unbounded ASCII decimals without integer-string conversion."""
    parts = value.split(":")
    if len(parts) != 2 or any(not p or any(c < "0" or c > "9" for c in p) for p in parts):
        raise argparse.ArgumentTypeError("lines must be positive ASCII START:END")
    start, end = (p.lstrip("0") for p in parts)
    if not start or not end or (len(start), start) > (len(end), end):
        raise argparse.ArgumentTypeError("lines require 1 <= START <= END")
    return start, end


class _SingleRange(argparse.Action):
    """Reject repeated options rather than accepting argparse's last value."""
    def __call__(self, parser, namespace, values, option_string=None):
        if getattr(namespace, self.dest) is not None:
            parser.error("--lines may be specified only once")
        setattr(namespace, self.dest, values)


def _available_endpoint(value: str, text_length: int) -> int:
    """Clamp only to an impossible line past EOF before safe conversion."""
    past_eof = text_length + 1
    limit = str(past_eof)
    return past_eof if (len(value), value) > (len(limit), limit) else int(value)


def main(argv: Sequence[str] | None = None) -> int:
    """Run the named-file CLI; argparse exits for help or invalid usage.

    Args:
        argv: Explicit arguments, or None to use process arguments.

    Returns:
        Zero after emitting exactly one line of successful text or JSON counts; one
        for named-file read/decode failures, with a diagnostic on stderr.

    Validation precedes acquisition. Expected OSError and UnicodeDecodeError
    failures identify the input without emitting partial counts or a traceback.
    """
    parser = argparse.ArgumentParser(prog="textstats", allow_abbrev=False,
                                     description="Count lines and words in a UTF-8 file.")
    parser.add_argument("--json", action="store_true", help="emit JSON counts")
    parser.add_argument("--keep-bom", action="store_true", help="retain a leading BOM")
    parser.add_argument("--lines", type=_parse_range, action=_SingleRange,
                        metavar="START:END", help="select inclusive named-file logical lines")
    parser.add_argument("input", metavar="INPUT", help="named UTF-8 input file")
    args = parser.parse_args(argv)
    try:
        if args.lines is None:
            stats = count_file(args.input, strip_bom=not args.keep_bom)
        else:
            text = _normalize_text(_read_text(args.input), strip_bom=not args.keep_bom)
            start, end = (_available_endpoint(value, len(text)) for value in args.lines)
            stats = count_text(_select_lines(text, start, end), strip_bom=False)
    except (OSError, UnicodeDecodeError) as error:
        print(f"textstats: {args.input!r}: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps({"lines": stats.lines, "words": stats.words}))
    else:
        print(f"lines={stats.lines} words={stats.words}")
    return 0

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats/core.py

SHA-256: `d2bd9bfd7c4b2f413d38a3429aec96c805971dc7775e8e124ccbd6f6da60c937`

```text
"""Pure whole-input counting and its immutable statistics value."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class TextStats:
    """Immutable nonnegative integer line and word counts.

    Args:
        lines: Number of CRLF, CR, or LF terminated lines and final segments.
        words: Number of whitespace-separated words.

    Raises:
        TypeError: A count is not an integer (booleans are rejected).
        ValueError: A count is negative.
    """

    lines: int
    words: int

    def __post_init__(self) -> None:
        for field in ("lines", "words"):
            value = getattr(self, field)
            if type(value) is not int:
                raise TypeError(f"{field} must be an integer")
            if value < 0:
                raise ValueError(f"{field} must be nonnegative")


def count_text(text: str, *, strip_bom: bool = True) -> TextStats:
    """Count a string without modifying it or emitting output.

    Args:
        text: The complete decoded input.
        strip_bom: Remove exactly one leading U+FEFF when true. Interior and
            subsequent BOMs remain ordinary non-whitespace characters.

    Returns:
        Immutable counts. Only CRLF, lone CR, and LF terminate lines; a
        nonempty final unterminated segment adds one line. Empty text has no
        lines, and trailing terminators add no phantom line. Words follow
        Python's Unicode whitespace splitting rules.
    """
    text = _normalize_text(text, strip_bom=strip_bom)
    # Normalizing CRLF first prevents its two characters counting twice.
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = normalized.count("\n")
    if normalized and not normalized.endswith("\n"):
        lines += 1
    return TextStats(lines, len(text.split()))


def _normalize_text(text: str, *, strip_bom: bool = True) -> str:
    """Apply the whole decoded input's BOM policy exactly once."""
    return text[1:] if strip_bom and text.startswith("\ufeff") else text


def _select_lines(text: str, start: int, end: int) -> str:
    """Select inclusive logical lines from already normalized decoded text.

    Preserve contents and CRLF/CR/LF terminators. Unicode separators are
    contents, and a trailing terminator does not create a phantom line.
    """
    selected = []
    offset = 0
    number = 1
    for match in re.finditer(r"\r\n|\r|\n", text):
        if start <= number <= end:
            selected.append(text[offset:match.end()])
        offset = match.end()
        number += 1
        if number > end:
            return "".join(selected)
    if offset < len(text) and start <= number <= end:
        selected.append(text[offset:])
    return "".join(selected)

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats/io.py

SHA-256: `840e420abf011fce8d571664d64ada1f1417c6a2c929bcaa31dd3cb7b5a026f0`

```text
"""Acquire complete named-file bytes without newline translation."""

import os

from .core import TextStats, count_text


def count_file(path: str | os.PathLike[str], *, strip_bom: bool = True) -> TextStats:
    """Count a UTF-8 file silently, leaving its bytes unchanged.

    Args:
        path: String or filesystem path to the named input.
        strip_bom: Remove exactly one leading BOM before counting.

    Returns:
        Immutable line/word counts using count_text's CR/LF and Unicode rules.

    Raises:
        OSError: The file cannot be opened or read.
        UnicodeDecodeError: Complete input is not valid UTF-8.

    The owned binary handle closes before counting; no caller stream is owned.
    """
    return count_text(_read_text(path), strip_bom=strip_bom)


def _read_text(path: str | os.PathLike[str]) -> str:
    """Decode complete named-file bytes strictly, closing the owned handle."""
    with open(path, "rb") as source:
        return source.read().decode("utf-8")

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/tests/unit/test_ranges.py

SHA-256: `0cb46659cc72f16deebc3213af3dd15a304ce460a6b425f10cab7ceec9a53071`

```text
"""Decoded selection preserves logical lines and normalizes the BOM once."""
import contextlib
import io
import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import textstats
from textstats import TextStats, count_text, count_file
from textstats import core


class SelectionTests(unittest.TestCase):
    def test_selection_contract(self):
        self.assertTrue(hasattr(core, '_select_lines'), 'selection seam missing')
        rows=[('alpha beta\nbeta\nlast two',2,3,'beta\nlast two'),
              ('alpha beta\nbeta\nlast two',2,99,'beta\nlast two'),
              ('alpha beta\nbeta\nlast two',1,1,'alpha beta\n'),
              ('alpha beta\nbeta\nlast two',4,99,''),
              ('a\n\n',2,9,'\n'),('a\r\nb c\rd\n',2,3,'b c\rd\n'),
              ('',1,9,''),('a\u2028b\nlast',1,1,'a\u2028b\n'),
              ('a\n\ufeff\n',2,2,'\ufeff\n'),('a\r\n',2,3,'')]
        for text,start,end,expected in rows:
            with self.subTest(text=text,start=start,end=end):
                self.assertEqual(core._select_lines(text,start,end),expected)

    def test_normalization_once_and_whole_api(self):
        self.assertTrue(hasattr(core, '_normalize_text'), 'normalization seam missing')
        for text,keep,expected in [('\ufeff',False,TextStats(0,0)),('\ufeff',True,TextStats(1,1)),
                                   ('\ufeff\ufeff',False,TextStats(1,1)),('a\n\ufeff\n',False,TextStats(1,1))]:
            normalized=core._normalize_text(text,strip_bom=not keep)
            selected=core._select_lines(normalized,2 if text.startswith('a') else 1,2)
            self.assertEqual(count_text(selected,strip_bom=False),expected)
        self.assertEqual(textstats.__all__,['TextStats','count_text','count_file'])
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'sample'
            data=b'alpha beta\r\ngamma\r'
            path.write_bytes(data)
            out,err=io.StringIO(),io.StringIO()
            with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                self.assertEqual(count_file(path),TextStats(2,3))
            self.assertEqual((out.getvalue(),err.getvalue()),('',''))
            self.assertEqual(path.read_bytes(),data)

class RangeValidationTests(unittest.TestCase):
    def test_invalid_usage_before_either_acquisition(self):
        from textstats.cli import main
        huge='9'*5000
        invalid=['','0:1','1:0','2:1','1:',' :2',':2','+1:2','-1:2','1: 2','1:2 ','١:2','1:２','1:2:3','1.0:2',huge+':1',huge+':'+('8'*5000)]
        arguments=[['--lines='+value,'missing'] for value in invalid]
        arguments += [['--lines'],['--lines','missing'],['--lines','1:2','--lines','2:3','missing'],
                      ['--lines=1:2','--lines=2:3','missing'],['--lines','1:2','--lines=2:3','missing']]
        for args in arguments:
            with self.subTest(args=[a[:50] for a in args]):
                out,err=io.StringIO(),io.StringIO()
                with patch('textstats.cli.count_file',side_effect=AssertionError('acquired')) as whole,patch('textstats.io.open',side_effect=AssertionError('opened')) as opened:
                    with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                        with self.assertRaises(SystemExit) as result:main(args)
                self.assertEqual(result.exception.code,2)
                self.assertEqual(out.getvalue(),'')
                self.assertTrue(err.getvalue())
                self.assertNotIn('Traceback',err.getvalue())
                whole.assert_not_called();opened.assert_not_called()

class RangeResourceTests(unittest.TestCase):
    def test_owned_handle_closes_on_range_success_and_failure(self):
        from textstats.cli import main
        for data,status in [(b'a\r\nb c\r',0),(b'a\nlate\xff',1)]:
            handle=io.BytesIO(data)
            out,err=io.StringIO(),io.StringIO()
            with patch('textstats.io.open',return_value=handle):
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    actual=main(['--lines=1:1','sample'])
            self.assertEqual(actual,status)
            self.assertTrue(handle.closed)
            self.assertEqual(out.getvalue(),'lines=1 words=1\n' if status==0 else '')
        for error in [PermissionError('denied'),OSError('read failed')]:
            out,err=io.StringIO(),io.StringIO()
            with patch('textstats.cli._read_text',side_effect=error):
                with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                    self.assertEqual(main(['--lines=1:1','sample']),1)
            self.assertEqual(out.getvalue(),'');self.assertIn('sample',err.getvalue());self.assertNotIn('Traceback',err.getvalue())

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/tests/integration/test_ranges.py

SHA-256: `9141b3775e67c75b77a8c8cc5f507be3632d3f6984afc92e2a87e8805e9641f8`

```text
"""Actual named-file module selection, validation and API regressions."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from textstats import TextStats, count_file

class RangeModuleTests(unittest.TestCase):
    def invoke(self,*args):
        return subprocess.run([sys.executable,'-m','textstats',*args],capture_output=True,text=True,
                              env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})

    def test_supplied_rows_formats_spellings_and_order(self):
        rows=[('alpha beta\nbeta\nlast two','2:3',(2,3)),('alpha beta\nbeta\nlast two','2:99',(2,3)),
              ('alpha beta\nbeta\nlast two','1:1',(1,2)),('alpha beta\nbeta\nlast two','4:99',(0,0)),
              ('a\n\n','2:9',(1,0)),('a\r\nb c\rd\n','2:3',(2,3)),('', '1:9',(0,0)),
              ('\ufeff','1:1',(0,0)),('\ufeff\ufeff','1:1',(1,1)),('a\n\ufeff\n','2:2',(1,1)),
              ('a\u2028b\nlast','1:1',(1,2)),('a\r\n','2:3',(0,0))]
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'sample'
            for text,value,expected in rows:
                data=text.encode();path.write_bytes(data)
                for range_args in (['--lines',value],['--lines='+value]):
                    for options in (range_args,['--json',*range_args],[*range_args,'--json']):
                        with self.subTest(text=text,value=value,options=options):
                            run=self.invoke(*options,str(path))
                            self.assertEqual((run.returncode,run.stderr),(0,''))
                            self.assertTrue(run.stdout.endswith('\n'))
                            if '--json' in options:
                                result=json.loads(run.stdout);self.assertEqual(result,dict(zip(['lines','words'],expected)))
                                self.assertTrue(all(type(x) is int for x in result.values()));self.assertEqual(len(run.stdout.splitlines()),1)
                            else:self.assertEqual(run.stdout,f'lines={expected[0]} words={expected[1]}\n')
                            self.assertEqual(path.read_bytes(),data)
            path.write_bytes(b'alpha beta\nbeta\nlast two')
            self.assertEqual(count_file(path),TextStats(3,5))

    def test_huge_leading_zero_bom_dash_and_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'-sample'
            path.write_bytes('\ufeff\nsecond two\n\ufeff\n'.encode())
            huge='9'*5000
            for value,expected in [('0002:0003','lines=2 words=3\n'),('2:'+huge,'lines=2 words=3\n'),(huge+':'+huge,'lines=0 words=0\n')]:
                run=self.invoke('--lines',value,'--',str(path));self.assertEqual((run.returncode,run.stdout,run.stderr),(0,expected,''))
            for options in (['--keep-bom','--lines=1:1','--json'],['--json','--lines','1:1','--keep-bom'],['--lines=1:1','--keep-bom','--json']):
                run=self.invoke(*options,str(path));self.assertEqual((run.returncode,run.stderr),(0,''));self.assertEqual(json.loads(run.stdout),{'lines':1,'words':1})
            path.write_bytes(b'a\nsecond\xff')
            for options in (['--lines=1:1'],['--json','--lines','1:1'],['--keep-bom','--lines=1:1']):
                run=self.invoke(*options,str(path));self.assertEqual((run.returncode,run.stdout),(1,''));self.assertIn(str(path),run.stderr);self.assertNotIn('Traceback',run.stderr)
                self.assertEqual(path.read_bytes(),b'a\nsecond\xff')
            for args,status in [(['--lines=1:1',str(path)+'missing'],1),(['--lines=2:1',str(path)+'missing'],2),(['--lines=1:1','--lines','1:2',str(path)],2)]:
                run=self.invoke(*args);self.assertEqual((run.returncode,run.stdout),(status,''));self.assertTrue(run.stderr);self.assertNotIn('Traceback',run.stderr)

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/tests/integration/test_distribution.py

SHA-256: `1d27805fdd34a25fc114b59edf67a8137308b69db6ad9636e00ece14c942ac24`

```text
"""Run a source archive independently of checkout imports."""

import os
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import unittest


class SourceDistributionTests(unittest.TestCase):
    def test_extracted_package_public_docs_and_module_contract(self):
        root = Path(__file__).resolve().parents[2]
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            build = temporary / "build"
            result = subprocess.run(["make", "dist", f"DIST_DIR={build}"],
                                    cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            archive = build / "textstats.tar.gz"
            extracted = temporary / "extracted"
            extracted.mkdir()
            with tarfile.open(archive) as source:
                names = source.getnames()
                for required in ("textstats/__init__.py", "textstats/__main__.py",
                                 "README.md", "Makefile", "docs/api.md", "docs/module.md"):
                    self.assertIn(required, names)
                self.assertFalse(any("textstats-run-resources" in name or
                                     "__pycache__" in name or name.startswith("dist/")
                                     for name in names))
                # The archive is produced locally from explicit project paths.
                self.assertFalse(any(Path(name).is_absolute() or ".." in Path(name).parts
                                     for name in names))
                options = {"filter": "data"} if hasattr(tarfile, "data_filter") else {}
                source.extractall(extracted, **options)
            environment = {key: value for key, value in os.environ.items()
                           if key not in ("PYTHONPATH", "PYTHONHOME", "PYTHONSTARTUP")}
            environment.update(PYTHONNOUSERSITE="1", PYTHONDONTWRITEBYTECODE="1")
            identity = subprocess.run(
                [sys.executable, "-c", "import textstats; print(textstats.__file__)"],
                cwd=extracted, env=environment, capture_output=True, text=True)
            self.assertEqual(identity.returncode, 0, identity.stderr)
            self.assertEqual(Path(identity.stdout.strip()).resolve(),
                             extracted / "textstats" / "__init__.py")

            def invoke(*arguments):
                return subprocess.run([sys.executable, "-m", "textstats", *arguments],
                                      cwd=extracted, env=environment,
                                      capture_output=True, text=True)

            path = extracted / "sample.txt"
            for data, options, expected in [
                (b"alpha beta\r\ngamma\r", (), "lines=2 words=3\n"),
                (b"", (), "lines=0 words=0\n"),
                ("café\u2028tea\n".encode(), (), "lines=1 words=2\n"),
                ("\ufeff\n".encode(), (), "lines=1 words=0\n"),
                ("\ufeff\n".encode(), ("--keep-bom",), "lines=1 words=1\n"),
            ]:
                with self.subTest(data=data, options=options):
                    path.write_bytes(data)
                    run = invoke(*options, "sample.txt")
                    self.assertEqual((run.returncode, run.stdout, run.stderr),
                                     (0, expected, ""))
                    self.assertEqual(path.read_bytes(), data)
                    formats = [("--json", *options)]
                    if options:
                        formats.append((*options, "--json"))
                    for json_options in formats:
                        json_run = invoke(*json_options, "sample.txt")
                        self.assertEqual((json_run.returncode, json_run.stderr), (0, ""))
                        self.assertEqual(len(json_run.stdout.splitlines()), 1)
                        self.assertTrue(json_run.stdout.endswith("\n"))
                        expected_counts = dict((k, int(v)) for k, v in
                                               (part.split("=") for part in expected.split()))
                        self.assertEqual(json.loads(json_run.stdout), expected_counts)
                        self.assertTrue(all(type(v) is int for v in json.loads(json_run.stdout).values()))
                        self.assertEqual(path.read_bytes(), data)
            path.write_bytes("\ufeffalpha beta\r\nbeta\n\ufefflast two".encode())
            original = path.read_bytes()
            for options, expected in [
                (("--lines", "2:3"), "lines=2 words=3\n"),
                (("--lines=4:99",), "lines=0 words=0\n"),
                (("--lines=1:1",), "lines=1 words=2\n"),
                (("--keep-bom", "--lines=1:1"), "lines=1 words=2\n"),
            ]:
                run = invoke(*options, "sample.txt")
                self.assertEqual((run.returncode, run.stdout, run.stderr), (0, expected, ""))
                counts = dict((k, int(v)) for k, v in (part.split("=") for part in expected.split()))
                for json_options in (("--json", *options), (*options, "--json")):
                    run = invoke(*json_options, "sample.txt")
                    self.assertEqual((run.returncode, run.stderr), (0, ""))
                    self.assertEqual(json.loads(run.stdout), counts)
                self.assertEqual(path.read_bytes(), original)
            path.write_bytes("\ufeff\n".encode())
            for options, words in [(("--lines=1:1",), 0),
                                   (("--lines", "1:1", "--keep-bom"), 1)]:
                run = invoke("--json", *options, "sample.txt")
                self.assertEqual((run.returncode, run.stderr), (0, ""))
                self.assertEqual(json.loads(run.stdout), {"lines": 1, "words": words})
            for arguments, status in [(("--lines=2:1", "sample.txt"), 2),
                                      (("--lines=1:1", "--lines", "1:1", "sample.txt"), 2),
                                      (("--lines=1:1", "missing.txt"), 1)]:
                run = invoke(*arguments)
                self.assertEqual((run.returncode, run.stdout), (status, ""))
                self.assertTrue(run.stderr)
                self.assertNotIn("Traceback", run.stderr)
            path.write_bytes(b"valid\nlate\xff")
            run = invoke("--json", "--lines=1:1", "sample.txt")
            self.assertEqual((run.returncode, run.stdout), (1, ""))
            self.assertIn("sample.txt", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
            self.assertEqual(path.read_bytes(), b"valid\nlate\xff")
            path.write_bytes(b"alpha\n")
            dash = extracted / "-sample.txt"
            dash.write_bytes(b"alpha\n")
            run = invoke("--lines=1:1", "--", "-sample.txt")
            self.assertEqual((run.returncode, run.stdout, run.stderr), (0, "lines=1 words=1\n", ""))
            help_run = invoke("--help")
            self.assertEqual((help_run.returncode, help_run.stderr), (0, ""))
            self.assertIn("--keep-bom", help_run.stdout)
            self.assertIn("--json", help_run.stdout)
            self.assertIn("--lines", help_run.stdout)
            for arguments, status in [(("missing.txt",), 1), ((), 2),
                                      (("--jsn", "sample.txt"), 2)]:
                run = invoke(*arguments)
                self.assertEqual((run.returncode, run.stdout), (status, ""))
                self.assertTrue(run.stderr)
                self.assertNotIn("Traceback", run.stderr)
            missing_json = invoke("--json", "missing.txt")
            self.assertEqual((missing_json.returncode, missing_json.stdout), (1, ""))
            self.assertIn("missing.txt", missing_json.stderr)
            path.write_bytes(b"valid prefix\xff")
            run = invoke("sample.txt")
            self.assertEqual((run.returncode, run.stdout), (1, ""))
            self.assertIn("sample.txt", run.stderr)
            self.assertNotIn("Traceback", run.stderr)
            self.assertEqual(path.read_bytes(), b"valid prefix\xff")
            for options in (("--json",), ("--json", "--keep-bom"), ("--keep-bom", "--json")):
                bad_json = invoke(*options, "sample.txt")
                self.assertEqual((bad_json.returncode, bad_json.stdout), (1, ""))
                self.assertIn("sample.txt", bad_json.stderr)
                self.assertNotIn("Traceback", bad_json.stderr)
                self.assertEqual(path.read_bytes(), b"valid prefix\xff")

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-design/SKILL.md

SHA-256: `bacf686f53b4f2e1a759624ddd70ae34cd6b55ed51c3dd5e1a6624eb0ea028aa`

```text
---
name: sdd-design
description: Use when exploring a software project or feature, forming architecture decisions, developing a component decomposition, or creating and revising docs/dev/PROJECT.md, ARCHITECTURE.md, DECOMPOSITION.md, and scoped architectural change documents before specification.
---

# Explore and design

Choose the work requested and load only its reference. A request for a later stage can start there when its inputs are established; do not replay earlier stages as ceremony.

| Work | Load |
| --- | --- |
| Clarify the problem, compare alternatives, resolve decisions, or identify open questions | [exploration](references/exploration.md) |
| Define or revise major system blocks, dependency direction, and architectural decisions | [architecture](references/architecture.md) |
| Define or revise component responsibilities, collaboration, and provisional interfaces | [decomposition](references/decomposition.md) |

When the request crosses stages, load the next reference as that stage becomes relevant. Exploration can remain conversational. Do not create project documents solely because discussion has matured. Document creation or revision requires **sdd-manage** to coordinate the user's request and a current **sdd-orient** handoff identifying a usable Git worktree, applicable instructions, target paths, and unresolved dirty state. This skill does not perform orientation or authorize a different workflow.

Use the **sdd-conventions** modularity reference when defining or reviewing boundaries, and its design heuristics when assessing a chosen approach or comparing options. Keep these checks separate from the document-specific procedures below. Observe project instructions and existing contracts; do not overwrite unowned changes. If required project evidence conflicts, resolve the conflict before mutation.

`PROJECT.md` owns the concise project brief, `ARCHITECTURE.md` owns high-level design, and `DECOMPOSITION.md` owns detailed logical component boundaries. Both architecture and decomposition may have focused children. Scoped feature documents express a proposed architectural delta where necessary. These documents inform SPEC; they neither replace its behavioral contracts nor authorize implementation, planning, layout authoring, or task execution.

## Document boundaries

| Document | Governing concern |
| --- | --- |
| ARCHITECTURE | Major blocks, system-wide relationships and dependency direction, and consequential structural rationale. |
| DECOMPOSITION | Logical components within those blocks: responsibility, collaboration, state ownership, and design-level interface and verification seams. |
| SPEC | Observable behavior and precise success/failure contracts, required qualities, and acceptance. |
| PLAN | Practical delivery order, capability increments, dependencies, and exit/decision evidence. |
| layout.md | Physical allocation of source, tests, documentation, and artifacts. |

Support required modularity, extensibility, scalability, decoupling, and testability through the accepted design. Tie variation and load decisions to actual requirements and credible needs; these qualities do not require realizing every anticipated capability in the first increment.

Use the relevant architecture or decomposition reference for read-only design review. Incorporation of accepted feature design into main PROJECT, ARCHITECTURE, or DECOMPOSITION belongs to **sdd-integrate-feature**.

At completion, state what was explored or changed, the decisions established, unresolved material questions, and which documents were inspected or updated. Report design as design, never as implemented functionality.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/SKILL.md

SHA-256: `b826b549817648a7ab0ce68f324b0d8158d4ede6b687e4034cb664306256cd3e`

```text
---
name: sdd-manage
description: Coordinate SDD workflows for initial development, feature preparation, bounded or resumed task implementation, human-directed checkpoint amendments, accepted feature integration, focused review or maintenance, and hosted task synchronization. Use for multi-stage project requests, shared prerequisites, branch management and phase transitions, workflow transitions, stopping boundaries, recovering shell authentication, or supplying hosting credentials to sdd-forge.
---

# Coordinate specification-driven development

Translate the user's objective into a scoped workflow and coordinate the responsible skills. Use the request and established session decisions as authorization; continue routine steps within that scope without repeated confirmation. Apply the dedicated scoped authorization policy for review/revision commits, pushes and verified integration; after rejection, supply the actual human request, scope, destinations and verification evidence to platform review. Discussion, assessment, or review alone does not authorize edits. Start at the requested stage when its inputs are established, and stop at the requested boundary.

| Coordination concern | Load |
| --- | --- |
| Select a practical workflow and its entry, outputs, and stopping point | [available workflows](references/workflows.md) |
| Place disclosure and discoverable usage records in the first target-repository SDD commit | [repository bootstrap](references/repository-bootstrap.md) |
| Enforce SPEC/PLAN/TASKS preparation readiness and affected reassessment | [document QC gates](references/document-qc-gates.md) |
| Establish prerequisites, pass scope, resolve blockers, and persist results | [coordination protocol](references/coordination.md) |
| Resolve identities, create/reuse workflow branches, or manage phase transitions | [branch management](references/branch-management.md) |
| Establish review/revision publication authorization or respond to an approval rejection | [scoped authorization](references/revision-authorization.md) |
| Integrate verified boundaries or continue a blocked merge | [Git workflows](references/git-workflows.md) |
| Discover, save, or supply a repository token; recover shell/API authentication | [hosting credentials](references/credentials.md) |
| Gate phase eligibility and active hosted object creation before execution | [phase activation](references/phase-activation.md) |
| Plan or coordinate focused/systematic review and accepted revisions | [review and revision](references/review-and-revision.md) |
| Check representative requests and expected boundaries | [workflow examples](references/examples.md) |

1. **Establish the request.** Identify the project, objective, requested operation, authoritative inputs, and stopping boundary. Distinguish initial preparation, feature deltas, task-list implementation, checkpoint steering, integration, and focused review. Ask only for missing decisions that materially prevent the requested work.
2. **Orient at startup.** Invoke **sdd-orient** for a current scoped handoff: project and Git roots, governing instructions, documents, environment, branch and HEAD, dirty-path ownership, and interrupted task state. Read-only discussion can proceed outside Git; repository mutations require an eligible worktree. Re-orient when material state or scope changes.
3. **Coordinate the responsible skills.** Follow the selected workflow. Supply the objective, allowed paths and effects, authoritative decisions, task IDs where applicable, Git baseline, pending-change ownership, and exit conditions. Load their instructions rather than reproducing their procedures. Preserve valid existing work; dirty state alone does not justify reset.
4. **Respect ownership and decisions.** Leave executable range selection, main execution, completion, commits, and pushes to **sdd-implement**, and checkpoint amendments to **sdd-steer**. Leave accepted feature reconciliation to **sdd-integrate-feature**. Return governing-document amendments identified by **sdd-docs** to the user; do not automatically route them into authoring. Coordinate hosting only when requested or already active for the selected work.
5. **Finish and stop.** Coordinate explicit integration/publication only when the workflow's integration gate is met: main development requires full phase completion; a partial task/milestone range pushes and pauses on its phase branch. Collect evidence and unresolved differences. For authorized repository changes outside implementation or steering, coordinate scoped verification, commit composition through **sdd-report**, commit, and push as specified by the request and project policy. Report blockers accurately. Never resume implementation after steering without a separate human instruction.

Use **sdd-report** for presentation, keeping planned, implemented, verified, committed, pushed, and hosted states distinct. Return the accomplished objective, affected artifacts or task IDs, evidence and limitations, commit/push and hosting outcomes when applicable, remaining decisions, and the exact stopping point. Do not require a transaction journal, recovery directory, extra issue map, or a new skill for interruption recovery. This coordinator requires the focused skills selected by the workflow; if one is unavailable, report the blocked capability rather than claiming it ran.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-steer/SKILL.md

SHA-256: `fcd5c2ea4a6eb877ceadadc7211e82f7d9abf1e76a4d8f1b381b369d9b286162`

```text
---
name: sdd-steer
description: Use when the human defines a focused amendment at a checkpoint during partial SDD task-list implementation, especially reducing previously implemented functionality, and requests impact assessment or amendment implementation across existing development documents, code, tests, and documentation. Stop after reporting; do not resume sdd-implement.
---

# Apply a human-directed checkpoint amendment

Steering is the lightweight checkpoint variant of the revision core workflow. Use **sdd-manage**'s **Core development workflows** model in its **Available workflows** reference for purpose and routing; this skill owns the focused amendment procedure and requires no formal campaign artifacts.

The human defines the objective at a checkpoint and decides whether to command its implementation. Distinguish an assessment request from an implementation request; discussion alone does not authorize repository changes. A command to implement the established amendment authorizes routine steps within that scope without repeated confirmation. **sdd-manage** coordinates scope and shared prerequisites. Use **sdd-manage**'s **Branch management** reference to establish or reuse an amendment branch from the paused implementation checkpoint, with that implementation branch as its target. Use a current **sdd-orient** handoff for repository instructions, Git and task state, pending-change ownership, and the implementation checkpoint.

| Work | Load |
| --- | --- |
| Establish the objective, scope, and affected work | [objective and impact](references/objective-and-impact.md) |
| Amend existing development documents and implemented behavior | [amendment execution](references/amendment-execution.md) |
| Bootstrap disclosure and usage records before the first SDD commit | **sdd-manage**: `skills/sdd-manage/references/repository-bootstrap.md` (bundled dependency) |
| Verify, commit, push, report, and stop | [verification and stop](references/verification-and-stop.md) |

1. **Establish the amendment.** Allocate or recover its shared review-campaign identity and matching revision branch; retain a minimal REVISION-REPORT with objective, scope, full baseline and paused target, adding observed verification/publication at completion. Require no fabricated review or plan. Identify the human's intended end state, affected implemented features, retained behavior, relevant existing documents and task IDs, and the checkpoint baseline. Report missing decisions or conflicts that prevent the focused amendment.
2. **Update existing development documents.** Within the commanded scope, directly amend affected SPEC, PLAN, TASKS or active FEATURE-TASKS, design, and layout so they describe the accepted end state. Preserve unaffected content and stable identities. Create no feature-document layer and invoke no feature-integration step.
3. **Align implementation.** Use **sdd-tdd** for test strategy and changes, perform focused production changes, and use **sdd-docs** for module, API, README, and guide alignment. For a reduction, remove affected functionality consistently while protecting the retained contracts and dependencies. This skill owns the production edits and repairs within the amendment.
4. **Verify and finish.** Use **sdd-verify** to assess the amendment and relevant regressions. Reassess affected completion claims, use **sdd-report** for the commit and result, commit and push the verified amendment, perform the default explicit merge into the paused implementation branch, verify and publish the target, and coordinate any warranted hosted reconciliation through **sdd-forge** when tracking is active.
5. **Stop.** Report the resulting checkpoint, implemented amendment, verification and limitations, working/target branches, amendment and merge commits and publication state, and remaining work. Do not hand off to, invoke, or resume **sdd-implement**, select further tasks, or start another amendment. The human separately decides when to resume the main task list.

**sdd-implement** owns the main task-list workflow; this skill owns the human-commanded checkpoint amendment, including its direct development-document updates, completion reassessment, commits, pushes, and issue-state coordination. A planning-only request returns findings and proposed scope, then stops. Preserve pending work and do not reset or delete unrelated implementation. Git and the current documents retain history; no separate transaction journal or recovery workflow is required.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-tdd/SKILL.md

SHA-256: `adc0c2c0f7bc3cc7612dfc781ee8681289b1542aae8eba0bb6d99361a3a903ed`

```text
---
name: sdd-tdd
description: Use when defining an SDD project's testing strategy, deriving test scenarios from accepted contracts, writing or reviewing tests, reproducing a bug, or guiding a test-first red-green-refactor cycle for a selected implementation task.
license: MIT
---

# Design tests and guide test-first implementation

Choose the requested operation and load its references:

| Work | Load |
| --- | --- |
| Define testing strategy and scenario coverage | [testing strategy](references/testing-strategy.md) |
| Guide a feature, bug fix, or behavior change through TDD | [test-first cycle](references/test-first-cycle.md) and [writing good tests](references/writing-good-tests.md) |
| Write, revise, or review tests, doubles, or test helpers | [writing good tests](references/writing-good-tests.md) |

Use the selected TASKS or FEATURE-TASKS entry, accepted SPEC contracts, relevant design, PLAN and layout, inspected implementation, and project test commands. **sdd-manage** coordinates scope and a current **sdd-orient** handoff establishing Git eligibility, governing instructions, and ownership of dirty changes. Strategy and review can remain read-only; test edits and execution follow the authorized scope and environment.

For new or changed behavior and bug fixes, establish a test that fails for the intended reason before the production change. Observe the failure, guide the smallest implementation that satisfies the accepted contract, and refactor with checks remaining green. **sdd-tdd** owns test strategy, scenarios, test changes, and development-cycle test execution. The active implementation workflow, **sdd-implement** for main task work or **sdd-steer** for a checkpoint amendment, owns production changes and applies the GREEN and production-refactoring steps; this skill supplies the test and evidence at each handoff. A strategy-only request does not authorize implementation.

Preserve existing work when resuming. If code predates the tests, report missing test-first evidence and use characterization or a safe isolated baseline where appropriate; do not delete or reset code to reconstruct an unobserved history. Follow applicable project policy and previously authorized exceptions for work that cannot use a meaningful test-first cycle. When an exception is still required and undecided, explain the concrete limitation and defer that decision to the user.

Return the testing strategy or test changes, covered contracts and scenarios, actual RED and GREEN commands and outcomes, regression results, remaining coverage gaps, and any exception or blocker. Do not invent a failed run or infer whole-project correctness from a focused passing test. **sdd-verify** owns the verification campaign and acceptance assessment; the active implementation workflow owns completion updates, commits, pushes, and issue-closure coordination. **sdd-docs** owns documentation maintenance and **sdd-report** presents completion evidence.

This skill adapts both Superpowers TDD and its test-writing companion. See [upstream provenance and adaptation](references/upstream-provenance.md) and the included [license](LICENSE).

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-report/SKILL.md

SHA-256: `481bec03eb256c70cabfc55ea7adca1626b940fa115e879f82e9de368a335a63`

```text
---
name: sdd-report
description: Use when drafting a task issue, Git commit message, pull request description, or evidence-backed task, milestone, phase or final implementation report, or review/revision campaign plan or report for an SDD project. Adapt the summary to feature, bug, code health, performance, security, testing, documentation, integration, or compatibility work without inventing results.
---

# Report SDD work

Choose the requested output and load only its reference:

| Output | Load |
| --- | --- |
| First SDD commit disclosure/usage evidence (drafting only) | **sdd-manage**: `skills/sdd-manage/references/repository-bootstrap.md` (bundled dependency) |
| Planned task issue title and body, task/amendment or merge commit message, or pull request draft | [drafts for hosted and Git objects](references/object-drafts.md) |
| Task, milestone, phase, final implementation, branch boundary, or interrupted-work status report | [completion reports](references/completion-reports.md) |
| Adjacent SPEC/PLAN/TASKS preparation QC reports and appended correction/recheck sections | [document QC reports](references/document-qc-reports.md) |
| Review plan/report or revision plan/report, including focused prompt-driven review | [campaign artifacts](references/campaign-artifacts.md) |
| Kind-specific emphasis and reusable What, Why, Verification, Result patterns | [change kinds](references/change-kinds.md) |

Use the owning TASKS or active FEATURE-TASKS entry, applicable design, SPEC, PLAN, and layout, actual changes, verification output, and Git evidence appropriate to the requested output. Obtain hosted issue references from **sdd-forge** when available; a guessed issue number is never acceptable. Separate *planned*, *performed*, *verified*, and *blocked* statements. State missing or limited evidence plainly; do not turn an example, unchecked task, or intended benchmark into a completed result. Follow project-specific title and reporting conventions where they exist.

Compose only the requested text or structured draft. Keep a concise shared core of **What**, **Why**, **Verification**, and **Result**, varying the labels and optional sections to suit the actual change. For a planned issue, Verification is an acceptance or check plan and Result is an intended outcome, not a completed claim. Emoji labels are optional presentation, not required metadata. For Markdown output, separate each heading from adjacent content with blank lines; a heading at the start needs no preceding blank line.

This skill drafts reports and messages. The active implementation or steering workflow owns its work commits and task status; **sdd-manage** coordinates other persistence and explicit boundary merges, **sdd-forge** owns hosted issue/milestone mutations, and any future PR workflow owns PR creation or merge. A draft does not grant authorization for those actions or establish task completion. Return the draft, source task IDs and issue references actually resolved, evidence used, and any facts still needed before publication.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-tasks/SKILL.md

SHA-256: `c669a4c270f8c7ffedaff6cc456c0dbaf7a24020bb4830357f32d0e8883cc800`

```text
---
name: sdd-tasks
description: Use when deriving or reviewing executable software-development tasks from an accepted design, SPEC, PLAN, and layout; creating docs/dev/TASKS.md or scoped docs/dev/FEATURE-TASKS.md; or reviewing task status and dependencies.
---

# Create and review task lists

Choose the requested operation and load only its reference. A request to generate TASKS does not authorize implementation.

Apply **sdd-conventions**' **Development-document QC** reference (`skills/sdd-conventions/references/development-document-qc.md`, bundled dependency). Authoring includes scoped review, correction/recheck and the adjacent report before dependent progression; pure review does not authorize corrections.

| Work | Load |
| --- | --- |
| Derive the complete task hierarchy or a scoped feature task list | [task derivation](references/task-derivation.md), then [conformance review](references/conformance-review.md) |
| Review generated task structure and PLAN conformance | [conformance review](references/conformance-review.md) |
| Review status, completion evidence, and dependencies | [progress review](references/progress-review.md) |

Read the relevant accepted PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, layout, and their focused children or active feature documents as needed for the operation. Inspect TASKS and any active FEATURE-TASKS, Git evidence, and affected code or tests when status or existing work matters. Use **sdd-conventions** to assess task boundaries and Phase → Milestone → Task identity and parentage. Do not invent requirements, delivery strategy, or physical ownership when those inputs are unresolved.

Read-only review can proceed without mutation. Creating or modifying TASKS or FEATURE-TASKS requires **sdd-manage** to coordinate the user's request and a current **sdd-orient** handoff establishing an eligible Git worktree, applicable instructions, target paths, and ownership of dirty changes. This skill does not implement orientation, verification, recovery, or code changes.

`docs/dev/TASKS.md` owns the complete intended phase → milestone → task hierarchy. An active `docs/dev/FEATURE-TASKS.md` owns the feature's scoped executable delta and inspectable progress until reconciled into TASKS. Use one project-wide task ID space; never copy a task as a second independently checked item. Give each phase a Markdown heading and keep its phase checkbox as the root of the nested checklist. Use **four spaces per nested level**: phase check item at the left margin, milestone indented four spaces, task indented eight. PLAN or an active FEATURE-PLAN owns strategic phase and milestone definitions and exit conditions; the applicable task list breaks them into executable work without redefining them. Layout owns physical placement; SPEC owns required behavior and acceptance. A checked box is a claim to verify against evidence, not evidence by itself.

Feature-delta reconciliation of TASKS and FEATURE-TASKS and incorporation into the main hierarchy belong to **sdd-integrate-feature** within its selected scope. Human-commanded direct checkpoint amendments belong to **sdd-steer**. **sdd-implement** owns executable range selection, main task-list execution, and completion updates.

At completion, report the task structure established, completion findings and evidence checked, dependencies or blockers, and documents inspected or updated. Do not report planned tasks as implemented features or continue beyond the selected work boundary.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-conventions/SKILL.md

SHA-256: `f441da1bfc36aaedceec0cb18838dc5496ea70e198edfa1ba66027bcbc619f0a`

```text
---
name: sdd-conventions
description: "Use when designing or reviewing a chosen architecture, design pattern, component boundary, API, module, refactor, Phase → Milestone → Task hierarchy, task breakdown, hosted task mapping, repository hosting-token storage or authentication recovery, workflow branch identities and artifact locations, review/revision campaign records, or code change; also use during code review and when comparing design options. Assess cohesion, dependencies, testability, complexity, and SOLID, DRY, and KISS where relevant."
---

# Shared conventions

Use the relevant convention only when its concern occurs in the current work. Respect applicable project instructions and established contracts. This skill supplies reusable criteria; it does not perform repository orientation, own project artifacts, execute a workflow, or authorize mutation.

## Available conventions

- **Modularity:** Read [modularity](references/modularity.md) when creating or assessing boundaries among system blocks, components, document nodes, code modules, or executable tasks, including code review.
- **Design heuristics:** Read [design heuristics](references/design-heuristics.md) when evaluating a chosen design or pattern, reviewing an implementation or refactor, or comparing options using SOLID, DRY, or KISS.
- **Task hierarchy:** Read [task hierarchy](references/task-hierarchy.md) when defining or reviewing Phase → Milestone → Task identity and parentage in TASKS, or projecting that hierarchy to hosted issues, labels, and milestones.

- **Backend object lifecycle:** Read [backend object lifecycle](references/backend-object-lifecycle.md) for phase-gated projection, explicit review units, issue/milestone closure, report placement and interruption recovery.

- **Workflow identity:** Read [workflow identity](references/workflow-identity.md) when allocating revision/feature campaign identities, naming workflow branches, or locating active and retained workflow artifacts.

- **Development-document QC:** Read [development-document QC](references/development-document-qc.md) when authoring/reviewing SPEC, PLAN or TASKS, evaluating delivery decomposition, establishing stage readiness, or reassessing affected feature/steering documents.

- **Review campaigns:** Read [review campaigns](references/review-campaigns.md) when organizing review/revision plans and reports, assigning campaign/finding identities, or retaining findings and evidence alongside governing project documents.

- **Hosting tokens:** Read [hosting tokens](references/hosting-tokens.md) when discovering, storing, or supplying repository credentials, or recovering shell/backend authentication.

Add a convention here only when it defines a clear invariant used by multiple workflows, can be applied without absorbing their stage-specific procedures, and does not own an artifact or operational workflow. Give each added concern its own focused reference and explicit trigger. Otherwise place it with the skill that owns the work.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-verify/SKILL.md

SHA-256: `fe02f63973521e86fa68a5fd775d01ab41fe7a797d26d8ae59dfa05bb25152ac`

```text
---
name: sdd-verify
description: Use when selecting and running checks for an SDD task, selected change, milestone, phase, or project; assessing acceptance and exit-condition coverage; classifying observed failures; performing read-only milestone/phase implementation code review, or returning verification evidence and remaining gaps before completion.
---

# Verify a selected work boundary

Establish the requested task, change, milestone, phase, or project scope. Load the relevant references:

| Work | Load |
| --- | --- |
| Review milestone/phase implementation code and findings | [boundary review](references/boundary-review.md) |
| Derive checks from requirements, changes, and dependencies | [check selection](references/check-selection.md) |
| Execute checks and assess acceptance evidence | [execution and evidence](references/execution-and-evidence.md) |
| Classify failures and return unresolved work | [failure assessment](references/failure-assessment.md) |

Use a current **sdd-orient** handoff for governing instructions, Git state, dirty-path ownership, relevant documents, and declared commands. **sdd-manage** coordinates the requested scope and execution prerequisites; the active implementation workflow, **sdd-implement** for main task work or **sdd-steer** for a checkpoint amendment, requests verification within its boundary. Read the owning TASKS or FEATURE-TASKS, relevant SPEC contracts, PLAN exit conditions, design and layout, actual changes, tests, and existing evidence as needed. Read-only check planning can precede execution; commands with side effects require the established eligible Git worktree and authorized environment.

For an explicit boundary review task, load boundary review and assess implementation code separately from test execution. Neither activity substitutes for the other. Return findings and recheck evidence without repairs or task/hosted state changes.

1. Identify the acceptance and exit conditions to verify and the implementation state being checked.
2. Select sufficient direct, dependent, integration, and boundary checks. Use project commands and an existing verification map where useful; neither a map nor new scripts are required.
3. Run the selected checks and inspect actual outcomes, including failures, warnings, skips, and collection counts where relevant.
4. Associate each condition with evidence and any limitation. Distinguish verified, failed, blocked, and not checked conditions; passing checks do not establish acceptance they never exercised.
5. Classify observed failures where evidence permits and return remaining work to its owner. Do not silently omit an unrelated or pre-existing failure from the results.

**sdd-tdd** owns testing strategy and test design or changes; this skill assesses coverage and executes the verification campaign. **sdd-docs** owns documentation maintenance. The active implementation workflow owns repairs, completion checkboxes, commits, pushes, and issue-closure coordination. Leave source, tests, governing documents, and task status unchanged during verification; report necessary changes rather than repairing them here. Account for command-generated artifacts and preserve unrelated pending work.

Return the boundary and implementation state, conditions assessed, check selection and rationale, commands and environment, observed outcomes and evidence locations, failure classifications, omitted or blocked checks, and remaining gaps. **sdd-report** owns presentation of these facts. Existing task evidence or a project-designated record may hold durable results; no separate verification journal is required. State when the selected conditions are verified without equating that finding with task completion or whole-project correctness.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-docs/SKILL.md

SHA-256: `561a9f9935357e3cb82e3110868571632f3b3a01ad4ddebc654232086d33f659`

```text
---
name: sdd-docs
description: Use when creating, reviewing, or maintaining professional module and API documentation, aligning README and standalone guides with an SDD project's supported implementation, checking documentation examples and links, or auditing documentation after code changes or across the project.
---

# Maintain project documentation

Choose the requested scope: documentation for affected code, README or selected guides, or a project-wide audit. Read only the relevant references:

| Work | Load |
| --- | --- |
| Module docstrings, API documentation, and explanatory comments | [in-code documentation](references/in-code-documentation.md) |
| README, standalone guides, examples, and navigation | [standalone documentation](references/standalone-documentation.md) |
| Change-scoped or project-wide audit and amendment findings | [review and findings](references/review-and-findings.md) |

Use a current **sdd-orient** handoff for applicable instructions, Git state, target paths, and ownership. **sdd-manage** coordinates the requested editing scope; the active implementation workflow, **sdd-implement** for main task work or **sdd-steer** for a checkpoint amendment, coordinates documentation maintenance after substantive code changes. Read project documentation policies, relevant layout, accepted design, SPEC and PLAN or their active feature equivalents, affected code and tests, and existing documentation as needed. Review can remain read-only; edits require an eligible Git worktree and established ownership of pending changes.

Follow the documentation style specified by governing project documents. Otherwise select an established professional style appropriate to the language and documentation tooling, such as Google-style Python docstrings. Keep documentation accurate, useful, and proportionate to the code's responsibility. Ensure every code module within the selected scope has a professional module docstring or its language's equivalent; a project-wide audit covers every project-owned code module. Report generated or externally maintained modules separately and follow project policy for editing them.

Maintain documentation against both accepted requirements and observed implementation. Clearly distinguish supported behavior from planned capabilities. If a discrepancy requires an amendment to SPEC, PLAN, design, layout, or another authoritative requirement, identify its location, issue, impact, and proposed amendment and report it to the user. Defer the decision to the user; do not amend the governing document or invoke its owning skill automatically. Continue independent documentation work and report anything dependent on that decision as unresolved.

Keep code edits confined to documentation unless additional work is authorized. Do not mark tasks complete, create commits, push, or change hosted objects here; the active implementation workflow owns those operations. For Markdown, separate every heading from adjacent content with blank lines; a heading at the beginning of a file or template needs no preceding blank line.

Return the reviewed scope, chosen style and source, documentation changed, checks and observed outcomes, unreviewed or excluded areas, and unresolved findings or user decisions. Use **sdd-report** for a completion summary when requested.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-integrate-feature/SKILL.md

SHA-256: `62bbe9725faada9934eea8ce29a6ab0bc40462747a1e49243c2d48331ca05bc9`

```text
---
name: sdd-integrate-feature
description: Use when incorporating accepted feature or change documents into the main PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, PLAN, or layout documents, or reconciling TASKS and FEATURE-TASKS from accepted feature deltas, including optional incorporation of FEATURE-TASKS into TASKS. Reconcile one selected document or a bounded set without requiring task-list changes.
---

# Integrate an accepted feature

Read [feature incorporation](references/feature-incorporation.md) for the scoped reconciliation procedure. This skill owns incorporation of accepted feature deltas into main project documents and reconciliation of TASKS and FEATURE-TASKS within the requested scope, including feature-related task and dependency revisions and feature-list incorporation into TASKS. Direct human-commanded checkpoint amendments belong to **sdd-steer**, which updates existing documents without this integration step. A request to reconcile one document does not authorize edits to the others. Review without mutation remains with the relevant focused skill.

Identify the requested target set before editing: PROJECT, ARCHITECTURE and its children, DECOMPOSITION and its children, SPEC and its children, PLAN and its children, layout and its children, TASKS, or FEATURE-TASKS. Reconcile any subset whose accepted source delta and main owner are established. Include TASKS or FEATURE-TASKS only when task-list reconciliation is requested or explicitly included in the coordinated scope. Transferring task ownership into TASKS requires both TASKS and FEATURE-TASKS in the edit scope so each task retains exactly one executable entry. TASKS-only reconciliation may revise existing main entries but does not copy active feature tasks. A document-only reconciliation can leave FEATURE-TASKS active; report its affected links or assumptions for later work.

Before mutation, **sdd-manage** coordinates the user's requested scope and a current **sdd-orient** handoff establishing an eligible Git worktree, applicable instructions, target paths, and ownership of dirty changes. Use **sdd-manage**'s **Branch management** reference to establish or reuse the selected integration branch and target; within an active feature campaign, reconcile on its existing working branch. Inspect accepted feature sources, main owners, and relevant dependents. Resolve conflicts or missing decisions with their owning workflow rather than guessing. Use **sdd-conventions** for affected document and component boundaries. This skill does not authorize implementation, task execution, hosted mutations, or automatic progression to other stages.

Return the main documents incorporated, feature sources active or historically archived, dependency impacts outside the selected scope, unresolved conflicts, and task-list status. Distinguish document incorporation from implementation or verified task completion.

For interrupted incorporation, load the continuation section of [feature incorporation](references/feature-incorporation.md). Inspect actual selected documents against the established checkpoint and accepted sources; resume the same scoped reconciliation without assuming that dirty files represent interrupted task implementation. Return coherent document differences and unresolved reassessment to the coordinator for verification, persistence, and default explicit Git integration. This skill owns document incorporation, not the Git merge.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-plan/SKILL.md

SHA-256: `816cc68dc8322ec0a9a1fb6c2bd1a1da648ed0447ca48037d0804e0e847ad2d3`

```text
---
name: sdd-plan
description: Use when planning delivery phases, milestones, dependencies, or exit gates, or when designing or reviewing a software project's repository layout, directory and package structure, and physical ownership of code, tests, and documentation. Produces or revises PLAN.md, FEATURE-PLAN.md, layout.md, and focused children before executable TASKS or FEATURE-TASKS are derived.
---

# Plan delivery and physical layout

Default to an early meaningful end-to-end MVP followed by small, testable capability increments; preserve the complete intended design and SPEC. Use the delivery reference for scope, prerequisite exceptions, and exit evidence.

Choose the requested work and load only its references. A request for complete delivery planning develops both PLAN and layout when physical ownership needs to be established; a focused request to review or revise one document does not automatically authorize rewriting the other.

Apply **sdd-conventions**' **Development-document QC** reference (`skills/sdd-conventions/references/development-document-qc.md`, bundled dependency). Authoring includes scoped review, correction/recheck and the adjacent report before dependent progression; pure review does not authorize corrections.

| Work | Load |
| --- | --- |
| Prepare both delivery strategy and physical placement for task derivation | [delivery plan](references/delivery-plan.md) and [physical layout](references/physical-layout.md) |
| Define or revise delivery strategy, phases, milestones, dependencies, or a scoped feature plan | [delivery plan](references/delivery-plan.md) |
| Define or revise physical ownership of implementation, tests, and documentation | [physical layout](references/physical-layout.md) |
| Review PLAN and layout consistency | [review](references/review.md) |

Before authoring, read the relevant PROJECT, ARCHITECTURE, DECOMPOSITION, SPEC, their focused children, and any existing PLAN and layout. Inspect relevant code, tests, and packaging for existing projects; distinguish observed placement from intended placement. If inputs conflict or a required behavioral or architectural decision is unresolved, identify its owner instead of silently settling it in PLAN or layout. Start at the requested operation when its inputs are established.

Read-only review can proceed without changing files. Creating, revising, or removing project documents requires **sdd-manage** to coordinate the user's request and a current **sdd-orient** handoff establishing an eligible Git worktree, applicable instructions, target paths, and ownership of dirty changes. This skill does not perform orientation or authorize another workflow.

PLAN owns delivery strategy and boundary verification; layout owns physical placement and ownership. SPEC owns behavior and acceptance; design owns logical structure; TASKS and an active FEATURE-TASKS own their respective stable, ordered execution units and progress. Use **sdd-conventions** when assessing component or task boundaries, without incorporating its shared rules here. Neither PLAN nor layout is a task checklist, a progress journal, or permission to implement. The downstream task workflow consumes the accepted design, SPEC, PLAN, and layout together.

Incorporation of an accepted FEATURE-PLAN into main PLAN or layout belongs to **sdd-integrate-feature**. Direct plan or layout corrections remain in their owning authoring workflows.

At completion, report the strategy or placement established, affected phases or ownership boundaries, unresolved material decisions, and documents inspected or updated. Describe proposed work as planned, not implemented.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-orient/SKILL.md

SHA-256: `91eeed3179358cb50e908a24ef83a2de9cc46dca7bf833509654b4bd04c66791`

```text
---
name: sdd-orient
description: Use when locating and inspecting a software project's repository before SDD work, checking Git worktree and interrupted-task state, discovering governing instructions and development documents, or handing a scoped project orientation to an orchestrating agent. Read-only; report whether a proposed mutation has the required Git and authority baseline.
---

# Orient in a project

Establish a factual, scoped starting point before another SDD skill changes repository files. This skill is a shared, **read-only** capability. It neither authorizes a mutation nor decides which later workflow to run. Read [inspection and handoff](references/inspection-and-handoff.md) for the evidence checks and report contract.

1. Establish the user's intended project path and proposed scope, if supplied. Distinguish the project root from its enclosing Git root; do not assume the current directory is the project.
2. Inspect root `SDD-MANAGER.md`, `AI_DISCLOSURE.md` and README links as adoption/disclosure evidence and report missing or conflicting records in the handoff; do not create them during orientation. Identify applicable repository instructions, including root and path-scoped `AGENTS.md`, referenced policies, and project-designated sources. Inspect `docs/dev/PROJECT.md` for the project brief; if it contains operating instructions, preserve their applicability and report their scope and any conflict.
3. Inspect Git, current branch or detached/unborn state, HEAD, worktree status, and changes affecting the intended paths. Suppress optional Git writes with command-scoped `git --no-optional-locks` or an equivalent scoped `GIT_OPTIONAL_LOCKS=0`. Git commands must not change the index, branch, working tree, or configuration.
4. Inspect adjacent SPEC/PLAN/TASKS (and selected feature) review reports, finding/gate state and reviewed/governing identities; report absent or apparently stale readiness without performing QC or writing reports. Discover present development documents and their focused children, the active feature or change context, relevant code and tests, and declared project commands. When a task list exists, identify the last committed task and compare it with the owning checklist, pending changes, and existing verification evidence. Distinguish completed work awaiting commit from incomplete work; pass the identified state to **sdd-implement** for continuation.
5. Produce the scoped orientation report. Separate observed facts from inferences and unknowns, identify concrete blockers, and state whether the Git prerequisite for a contemplated mutation is met. Re-orient when the project path, target scope, HEAD, instructions, or material worktree state changes.

If the target is outside a usable Git worktree, mark **repository mutation blocked**. Do not initialize Git, create files, clean worktrees, restore files, run tests with side effects, commit, or invoke a mutating workflow. A conversational or read-only inspection may continue.

For a subagent, the orchestrator supplies the applicable path scope, instructions, relevant document authorities, Git baseline, known dirty paths, and prohibited mutations. A subagent can inspect additional evidence within its scope; the orchestrator rechecks the overall state before coordinating any mutation or commit.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-forge/SKILL.md

SHA-256: `21cba41d7d64fc54206dc981fab665b16b7b868e4fe1c75769048a59b294b9b4`

```text
---
name: sdd-forge
description: Use when projecting software-development phases, milestones, and tasks to a hosted repository; creating or reconciling GitHub labels, milestones, and task issues; finding an issue for a task ID; or closing verified task issues and milestones, reopening invalidated milestones, or recovering interrupted hosted transitions. GitHub is the available backend. Ordinary local Git and SDD work does not require hosting access.
---

# Hosted task coordination

## Shared protocol

- **Scope:** Run only for a requested hosted operation. Identify the provider before loading its backend; report ambiguous remotes or unsupported providers without guessing. Local SDD work does not require hosting access.
- **Hierarchy:** Use the **sdd-conventions** task hierarchy to read phase, milestone, and task IDs and names from TASKS or the active FEATURE-TASKS and preserve their parentage in the host projection. The selected backend defines its concrete objects.
- **Coordination:** Before a hosted mutation, **sdd-manage** coordinates the user's request and a current **sdd-orient** handoff establishing the eligible Git worktree and governing instructions. Read-only inspection needs no Git mutation gate.
- **Credentials:** Use the available authenticated client or a suitable supplied token. **sdd-manage** discovers, accepts, and persists tokens under **sdd-conventions**' **Hosting tokens** rules and recovers the affected client's authentication when needed. A direct caller may supply a token to **sdd-forge**. Consume it through a protected mechanism without ordinary handoff/output exposure; Git shell authentication does not prove API-client access. The selected backend defines provider-specific checks and permission requirements.
- **Access failure:** For a backend access-related 403, request a suitable token from **sdd-manage** and return the endpoint, required access, and any provider-indicated non-credential cause without exposing the credential. The coordinator checks credential suitability and identifies any policy or other restriction requiring a different remedy; escalation does not require substituting a token when the existing credential is suitable. For direct use without **sdd-manage**, ask the user. Recheck access before retrying; a replacement token does not establish permission by itself.
- **Operational failure:** Let the selected backend distinguish access failures, rate limits, service/transport outages, invalid requests, and uncertain writes. Preserve successful independent results and return pending/unknown effects with bounded retry or deferred-reconciliation context; do not route every 403 to credential replacement.
- **Handoff:** Return the repository, task ID to issue number and URL associations, changed objects, access failures, ambiguity, and remaining differences. Pass issue references to implementation and reporting for commit composition. Issue state does not establish task completion.

Do not create commits, push branches, or create or merge pull requests here.

Add a backend only when it supports a concrete hosted operation with its own repository resolution, authentication, object mapping, and reconciliation rules. Give it a focused reference and explicit trigger; do not advertise a provider before its workflow is defined.

## Available backends

- **GitHub:** Read [GitHub backend](references/github.md) when the requested operation targets a GitHub repository. It resolves repository identity and access, then routes eligible-phase projection, issue lifecycle and milestone lifecycle operations. Apply the shared backend object lifecycle; task completion evidence comes from execution, not hosted state.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-specify/SKILL.md

SHA-256: `7b2fc98175350c9a5385e779cccaf93a7207ac429d4b3302b2c88b1dbd395fa9`

```text
---
name: sdd-specify
description: Use when creating, reviewing, or revising docs/dev/SPEC.md, focused specification children, or FEATURE-SPEC.md; defining required software behavior, interfaces, data contracts, error semantics, invariants, and objective acceptance for a new or existing system.
---

# Specify required behavior

Choose the requested operation and load only its reference. Enter directly when adequate decisions and project evidence exist; do not replay design exploration as ceremony.

Apply **sdd-conventions**' **Development-document QC** reference (`skills/sdd-conventions/references/development-document-qc.md`, bundled dependency). Authoring includes scoped review, correction/recheck and the adjacent report before dependent progression; pure review does not authorize corrections.

| Work | Load |
| --- | --- |
| Create or revise the complete intended system specification | [system specification](references/system-specification.md) |
| Define a scoped change to existing specified behavior | [change specification](references/change-specification.md) |
| Review SPEC quality and identify conflicts | [review](references/review.md) |

Before authoring, identify accepted decisions and the relevant PROJECT, ARCHITECTURE, DECOMPOSITION, existing SPEC, and applicable focused children. For an existing implementation, inspect only relevant code and tests to establish observed behavior; do not promote an observation into a requirement without an accepted decision. If a material architectural boundary is undecided or governing sources conflict, return that decision to design or the user rather than inventing a contract.

Read-only review can proceed without modifying files. Creating, revising, or removing project documents requires **sdd-manage** to coordinate the user's request and a current **sdd-orient** handoff establishing an eligible Git worktree, applicable instructions, affected paths, and ownership of dirty changes. This skill does not implement orientation or authorize another workflow.

SPEC is authoritative for intended observable behavior and acceptance. PROJECT owns the brief; ARCHITECTURE and DECOMPOSITION own structural design; PLAN owns delivery strategy; TASKS and an active FEATURE-TASKS own their respective executable units; layout owns physical paths. Use **sdd-conventions** when evaluating contract boundaries and necessary decomposition, without moving those shared checks into SPEC procedure. A feature specification states a scoped intended delta; it does not silently replace the complete main SPEC.

Incorporation of an accepted FEATURE-SPEC into main SPEC belongs to **sdd-integrate-feature**. Direct SPEC corrections remain in the owning system specification workflow.

Report the behavior specified or changed, affected contracts and acceptance conditions, unresolved material questions, and the precise documents inspected or updated. Document work does not authorize code changes, task selection, or continuation into implementation.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-implement/SKILL.md

SHA-256: `ca32a423668d4749f0ec9c463f3ae597ba2e3def51eb3333912133f397e11df0`

```text
---
name: sdd-implement
description: Use when selecting an executable task range, or executing or resuming a bounded SDD implementation workflow driven by TASKS or FEATURE-TASKS, completing pending task work, coordinating tests and documentation, verifying results, marking completion, committing and pushing each task, or stopping at a requested checkpoint.
---

# Implement a selected task range

Execute the user's requested task-list boundary. **sdd-manage** coordinates authorization, prerequisites, and focused capabilities; an implementation request authorizes work within its established scope without repeated confirmation for routine steps. Use a current **sdd-orient** handoff at startup for repository instructions, Git and task state, dirty-path ownership, and environment. Read the relevant references:

| Work | Load |
| --- | --- |
| Push outstanding commits, resume pending work, and select the range | [startup and continuation](references/startup-and-continuation.md) |
| Resolve next task, next N tasks, milestone, or phase requests | [range selection](references/range-selection.md) |
| Execute tasks with tests, documentation, and verification | [task execution](references/task-execution.md) |
| Bootstrap disclosure and usage records before the first SDD commit | **sdd-manage**: `skills/sdd-manage/references/repository-bootstrap.md` (bundled dependency) |
| Mark completion, commit and push, reconcile issues, and stop | [completion and checkpoints](references/completion-and-checkpoints.md) |

For a selection-only request, use the range-selection reference and return the IDs, dependencies, and stopping point without mutations. For an implementation request, follow this protocol:

1. **Push first.** Using the established repository and branch, push all outstanding commits before task selection, tests, or edits, even when the worktree is clean. Confirm the remote contains the commits. Stop on an unresolved push blocker before beginning further implementation.
2. **Resume before advancing.** Use orientation's last task commit, owning checklist, pending changes, and existing evidence. Finish a completed task awaiting commit without repeating its implementation, or resume the identified incomplete task. Preserve valid work and resolve ambiguous ownership or task identity before the affected mutation.
3. **Select the boundary.** Resolve the requested TASKS or FEATURE-TASKS range, dependencies, and stopping point using the range-selection reference. Record selected task IDs and exit conditions. Establish or reuse the scoped working branch and target under **sdd-manage**'s **Branch management** reference after startup pushing and before new task edits. Do not expand the range or invent requirements to bypass a blocker.
4. **Check readiness and execute one task at a time.** After push-first and before new task work/projection, apply **sdd-manage**'s **Document QC gates** reference (`skills/sdd-manage/references/document-qc-gates.md`, bundled dependency) to the selected owning inputs; report missing/stale gates and coordinate focused review within scope rather than silently rewriting requirements. Selection-only remains read-only and can return candidate IDs with blocked execution eligibility. Coordinate **sdd-tdd**, apply production changes, maintain documentation through **sdd-docs**, and obtain acceptance evidence through **sdd-verify**. Repair failures within scope and repeat affected checks as needed.
5. **Make each result durable.** Mark the task complete only after its implementation, tests, documentation, and required verification are complete. Use **sdd-report** for its commit message, commit the result and status, and push before advancing. When hosted tracking is active, coordinate verified issue closure through **sdd-forge**.
6. **Integrate and stop.** Execute the selected explicit review/report tasks, verify milestone/phase exits, persist their reports and coordinate issue then milestone closures through sdd-forge when tracking is active. Update eligible parent checkboxes using the shared backend lifecycle. Coordinate selected feature-document incorporation when required, verify the completed boundary, then apply the workflow integration gate: main task work merges only a complete verified phase; an incomplete phase pushes and pauses. Other coherent authorized boundaries integrate explicitly under the Git protocol. Return an evidence-backed report. Stop at the requested boundary or an unresolved blocker; do not start steering or additional tasks automatically.

This skill owns executable range selection, task execution, repairs, completion updates, commits, pushes, and issue-closure coordination. **sdd-tasks** owns task-list creation and review; **sdd-integrate-feature** owns feature-delta reconciliation. Human-commanded checkpoint amendments to existing development documents and prior implementation belong to **sdd-steer**. Report governing-document changes needed outside the selected implementation scope to the user rather than silently rewriting the requirements.

Git commits and the owning checklist provide continuation state. No transaction journal, recovery state directory, or separate recovery skill is required. Return completed task IDs and implemented capabilities, verification evidence and gaps, commit and push results, hosted reconciliation, remaining work, and the stopping boundary through **sdd-report**.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/workflows.md

SHA-256: `8ca466b140717b3cd8a33ea5fb1b9aafa8aa4fd696c8bee2455ef3edcf1912c2`

```text
# Available workflows

Select by the user's objective, not by which documents happen to be missing. A scoped request may enter any stage whose required inputs are established. A combined request may authorize preparation and implementation together; retain its explicit implementation boundary. Do not require fresh approval for a transition already covered by that request.

## Core development workflows

Choose among three core workflows by the intended change. They describe purpose and overall path; focused skills and the operation catalog below supply reusable stages. A workflow name grants no authorization or branch destination. Apply **sdd-conventions**' **Workflow identity** and [branch management](branch-management.md) for actual names and target context.

| Workflow | Purpose | Typical path |
| --- | --- | --- |
| Main / greenfield | Build the complete intended system from its initial definition. | Exploration → architecture/decomposition → SPEC → PLAN/layout → TASKS → bounded implementation and verification. |
| Revision | Correct, simplify, or improve previously defined or implemented work. | Review plan when needed → review → review report → revision plan → revision → revision report. |
| Feature | Add a scoped capability to an existing system. | Necessary feature design/specification/plan documents → FEATURE-TASKS → implementation → accepted document incorporation and verification. |

- **Entry:** Greenfield follows the main path from exploration; an existing project may enter at an established stage. Main names the development purpose, not Git's main or default branch. Reuse accepted inputs rather than replaying stages.
- **Revision scope:** Use [review and revision](review-and-revision.md) for formal campaigns. A focused prompt may define review scope or an accepted revision directly; do not invent a preceding review or mandatory artifact stage when it adds no needed evidence.
- **Feature preparation:** Define the scoped feature package before dependent implementation, using only the design, specification, and planning deltas it needs. FEATURE-TASKS governs active task-list feature work. Reuse sufficient existing design/layout; not every correction needs a feature package.
- **Shared execution:** Implement only the authorized bounded scope. Apply relevant verification and commit/push checkpoints under [Git workflows](git-workflows.md). Main development uses phase branches: partial ranges pause after pushes, complete phases explicitly integrate, and an authorized next phase starts from updated main. Revision/feature and steering use their applicable integration gates. Preparation, assessment, and review stop before implementation unless it is authorized. A narrow task request does not authorize unrelated incorporation or a whole-project campaign.

### Steering as lightweight revision

**sdd-steer** is the focused human-directed revision path at a paused task-list checkpoint, especially for reducing implemented functionality. The human supplies the amendment objective and commands execution. Steering directly updates affected existing documents, code, tests, and documentation; it creates no feature-document layer and requires no feature-document integration step or obligatory formal review/revision campaign.

Steering still verifies, commits/pushes, explicitly integrates into the paused implementation branch, verifies/publishes that target, and reports. It returns control without handing off to or resuming sdd-implement; the human separately resumes the task list. A broader revision may use the formal campaign instead. Steering is a revision variant, not a fourth core workflow.

## Operation catalog

These entries select stages or supporting operations within a core workflow; they can also be requested independently within their stated boundaries.

| Operation | Entry and coordination | Outputs and stop |
| --- | --- | --- |
| Prepare initial development | Enforce [document QC gates](document-qc-gates.md) between dependent stages, including scoped corrections/rechecks and adjacent reports. Use **sdd-design** for the brief, architecture, and decomposition; **sdd-specify** for behavior and acceptance; **sdd-plan** for delivery strategy and layout; **sdd-tasks** for TASKS. Resolve consequential decisions as they arise. | Selected preparation artifacts and open decisions. A preparation-only request stops before implementation. |
| Prepare a feature | Enforce [document QC gates](document-qc-gates.md) for the selected feature delta against accepted main inputs. Inspect existing contracts and implementation. Use design deltas where needed, then **sdd-specify**, **sdd-plan**, and **sdd-tasks** for the necessary FEATURE-SPEC, FEATURE-PLAN, and FEATURE-TASKS. Reuse established design and layout where sufficient. | Bounded feature requirements, delivery strategy, and executable tasks. Stop at preparation unless implementation is included in the request. |
| Implement a bounded range | Pass the owning TASKS or FEATURE-TASKS, requested IDs/count/milestone/phase, dependencies, and boundary to **sdd-implement**. It resolves the executable range and coordinates **sdd-tdd**, **sdd-docs**, **sdd-verify**, **sdd-report**, and active **sdd-forge** tracking. | Evidence-backed completed tasks, commits, pushes, and applicable issue closure. For main development, pause on an incomplete phase branch or explicitly integrate the verified full phase. For other workflows, integrate only the coherent authorized boundary. Verify/push applicable targets, then stop; retain branch state on a blocker. |
| Resume interrupted implementation | Pass orientation's identified pending task and evidence to **sdd-implement**. It pushes outstanding commits before task selection, tests, or edits, even on a clean tree; it finishes pending work before advancing. Use the established boundary; clarify it if unavailable. | Continuation of the bounded implementation workflow. No separate recovery protocol or automatic reset. |
| Steer at a checkpoint | Use **sdd-steer** for the human-defined focused amendment during partial implementation. An assessment request returns impact only; a command to implement authorizes direct changes to affected existing development documents, code, tests, and documentation. | Assessment, or a verified amendment branch explicitly merged into the paused implementation branch, merged-state verified and target pushed. Create no feature overlay and invoke no feature-document integration step. Stop; the human separately resumes implementation. |
| Integrate accepted feature documents | Pass the accepted sources and explicit target set to **sdd-integrate-feature**. TASKS and FEATURE-TASKS are independently selectable; transferring task ownership requires both lists in scope. Document-only integration does not imply task reconciliation. | Selected main documents incorporated, task relationships reconciled only within scope, source disposition, and external impacts. Stop without executing tasks. |
| Run a review/revision campaign | Use [review and revision](review-and-revision.md) for planned systematic review or prompt-driven focused review, stable findings, accepted revision planning, and authorized execution. Route concerns to focused owners. | Retained campaign plans/reports. Review stops before source changes unless revisions are authorized; implemented revisions finish with verified explicit merge/publication. |
| Review or maintain a selected scope | Route design review to **sdd-design**, behavior review to **sdd-specify**, strategy/layout review to **sdd-plan**, task-list review to **sdd-tasks**, selection-only requests to **sdd-implement**, test strategy or test maintenance to **sdd-tdd**, documentation to **sdd-docs**, and acceptance checks plus read-only milestone/phase implementation code review to **sdd-verify**. Use **sdd-conventions** for relevant criteria. | Findings, evidence, or explicitly requested maintenance. Review and verification do not authorize repairs or completion updates. Stop at the selected scope. |
| Synchronize hosted tracking | Use **sdd-forge** for the requested projection, association lookup, or issue reconciliation. Use available client authentication first and coordinate credential recovery through the credential protocol when needed; leave provider access checks and object mapping to its backend. | Repository and task-to-issue associations, eligible-phase object creation, verified issue/milestone closures, differences, and access blockers. Stop after the hosted operation. |

## Delivery strategy handoff

Preparation carries the accepted design/contracts into an early meaningful end-to-end MVP and small testable capability increments through **sdd-plan**, then derives their bounded executable work through **sdd-tasks**. Retain complete intended design and SPEC, justified prerequisite exceptions, preserved useful behavior, and relevant exit evidence. A scoped feature uses the earliest meaningful changed path rather than rebuilding the whole project.

Pass the selected range, owning capability/milestone outcomes, dependencies, verification obligations, and applicable human decision gates into implementation. At consequential checkpoints, return the demonstrated functionality and relevant usability/risk evidence for the human's continue/amend/simplify/stop decision. This does not authorize automatic steering, broaden the selected range, or require approval for routine work already authorized.

## Feature sequencing

- **Preparation:** Establish or reuse the convention's feature branch/package identity under [branch management](branch-management.md). Create its features-directory README linking the active root FEATURE sources; preserve another active package in the same worktree. Keep feature deltas distinguishable from the complete main documents. Creating a feature task list does not require immediate incorporation into TASKS.
- **Implementation:** An accepted FEATURE-TASKS can drive implementation while its authoritative feature documents remain active. Identify those sources explicitly in the handoff.
- **Document integration:** Incorporate accepted targets included in the request on the feature branch before final verification and Git merge. A complete feature implementation includes incorporation needed for a coherent final project; a preparation-only or narrow task request does not authorize unrelated incorporation. Do not infer acceptance from passing tests.
- **Archive:** After accepted final incorporation and task/evidence disposition, **sdd-integrate-feature** retains eligible sources under the package directory, repairs selected links, and marks historical snapshots. Partial/narrow integration retains needed active documents; verify archive ownership before final merge.
- **Git integration:** Merge the verified completed boundary into its established target by default with an explicit merge commit, verify the merged state, and publish the target. Preparation-only persists its documents on the feature branch and stops before implementation or full-feature merge.
- **Consistency:** If the selected work requires an unresolved contract or dependency decision, report it before the dependent mutation. Continue independent authorized work when sound.

## Cross-cutting operations

- **Reporting:** Use **sdd-report** throughout, or independently for an issue, commit message, PR description, or progress report. Drafting PR text does not create or merge a PR.
- **Hosted tracking:** Local workflows remain usable without hosting. Apply the shared backend lifecycle: activate/project only an eligible phase before its first task; coordinate committed milestone/phase review tasks and reports, task issue closure and then milestone closure; gate next-phase activation on verified predecessor integration/publication. Use phase activation for the transition. When tracking is active, coordinate task associations before commit composition and verified closure through **sdd-forge**; issue state never supplies completion evidence.
- **Authentication:** Attempt authorized pushes using existing shell authentication. Route access/credential failures to the coordinator's repository-token recovery protocol; preserve distinct Git and API access and the active backend's permission profile.
- **Persistence:** Implementation and steering own their commits and pushes. Coordinate persistence of other authorized repository edits through the shared protocol; hosted-only changes have no local commit by implication.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/coordination.md

SHA-256: `71228af38e0c333ae5ac5aa671d5df5370589dc131cca4ee336f28189fd46183`

```text
# Coordination protocol

## Establish scope and prerequisites

- **Request:** Capture the objective, inspection or mutation mode, target paths or documents, owning task list, selected boundary, and allowed external effects. Reuse session authorization and decisions.
- **Orientation:** Start with **sdd-orient**. Use its observed repository, applicable instructions, baseline, pending changes, tooling, and task evidence. Do not mistake an unchecked task or latest maintenance commit for a proven execution boundary.
- **Git:** Require an eligible worktree for repository mutations. Outside Git, continue discussion or inspection and report the mutation blocker; do not initialize a repository implicitly.
- **Pending work:** Establish ownership of dirty paths. Preserve unrelated staged and unstaged changes. Do not reset because the tree is dirty. Pass interrupted task implementation to **sdd-implement**, document incorporation to **sdd-integrate-feature**, and commanded amendment continuation to **sdd-steer**; if it lies outside the requested new scope, resolve that conflict before overlapping mutations.
- **Inputs:** Confirm the authoritative requirements, design, strategy, and layout needed by the selected stage. File presence alone does not establish acceptance or consistency.
- **Document readiness:** Use [document QC gates](document-qc-gates.md) before dependent PLAN/TASKS generation, implementation or hosted projection. Compare actual reviewed/governing state and coverage; route missing focused review within scope instead of trusting file presence or a Ready label.
- **Facilities:** Check availability of the selected skills and necessary tools. Report concrete missing capabilities. Use ordinary filesystem, Git, and available provider tools; require no particular client, hidden hooks, or implicit installation mechanism.

For branch workflows, use [branch management](branch-management.md) for setup and [Git workflows](git-workflows.md) for final integration. Preserve implementation's push-first prerequisite; a direct focused invocation uses the same protocol.

## Coordinate execution

1. Give each responsible skill the objective, scope, authoritative inputs, decisions, relevant task IDs, branch/HEAD, dirty-path ownership, permitted effects, required evidence, and stopping point. Keep credentials out of ordinary handoff text.
2. Let the skill perform its owned procedure. Collect its changed paths, observed evidence, findings, and remaining differences before the next dependent stage.
3. Refresh the material baseline when HEAD, instructions, project, target scope, or relevant pending changes change. Do not repeatedly run orientation or checks when the current evidence remains applicable.
4. Resolve missing human decisions and out-of-scope requirements without guessing or silently expanding work. Continue independent authorized work where possible. State the blocked operation and decision needed.
5. For verification failures, return repairs to the active **sdd-implement** or **sdd-steer** workflow. A standalone verification request returns findings; it does not start implementation. Documentation findings requiring governing-document changes are returned to the user before any authoring is coordinated.
6. Stop at the requested boundary. A checkpoint is not permission to select another milestone, start steering, incorporate unselected feature documents, or create hosted objects. Complete explicit integration/publication when its workflow gate is met; incomplete main phases push and pause even when the requested task subset is complete. A human-commanded steering amendment always returns control without resuming implementation.

## Persist repository changes

Use this procedure for document preparation, accepted integration, and standalone maintenance. Do not duplicate the commit workflows owned by **sdd-implement** or **sdd-steer**.

- **Policy:** Honor the user's commit and push instructions and repository policy, including standing session instructions. When no persistence policy is established, commit and push authorized finished changes to an established destination. Do not invent a remote branch or force-push.
- **Verification:** Inspect the actual diff and run checks appropriate to its effects: document consistency and links for authoring, relevant tests for test changes, or **sdd-verify** for acceptance campaigns. Verify heading spacing and project conventions. Do not manufacture task completion for document-only work.
- **Bootstrap:** Before the first SDD commit, apply [repository bootstrap](repository-bootstrap.md): package-derived root disclosure and usage notice plus README links travel with the first owned result. Reuse existing valid records; respect explicit path limits.
- **Staging:** Stage only owned changes; inspect the staged diff and exclude unrelated pre-existing staged paths from the commit. Preserve their index state. A normal commit includes all staged content; use a path-scoped commit only for wholly owned file contents, or isolate selected changes in a temporary index. Stop if ownership cannot be separated safely. Avoid broad staging or destructive cleanup.
- **Commit:** Use **sdd-report** to compose an evidence-backed message. Include stable task IDs and verified issue references when the change belongs to those tasks; preparation without assigned tasks does not invent IDs. Inspect commit contents and remaining staged and unstaged diffs; after a temporary-index commit, reconcile stale committed owned index entries while preserving unrelated staged content.
- **Push:** Assume existing shell authentication is usable; push the finished commits to the established destination and check that the remote contains them. For an access 403 or explicit credential failure, coordinate [shell recovery](credentials.md) and retry the affected push before reporting it as unresolved. Report a committed-but-unpushed result if access, destination, or divergence blocks persistence; retain local work. Resolve divergence without discarding changes or force-pushing.
- **State:** Distinguish committed, pushed, and hosted status. A successful local commit does not establish remote persistence or issue closure.

## Return results

Use **sdd-report** for the result format. Include the fulfilled objective and affected artifacts or task IDs, observed verification and gaps, commits and push status when applicable, hosted changes or pending reconciliation, unresolved decisions, and the boundary reached. Keep planned work distinct from implemented functionality. No extra workflow-state artifact is required: current documents, task evidence, Git, and applicable session decisions supply continuation context.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/document-qc-gates.md

SHA-256: `5f776622a41d2a9040b39c3800663532899d68bce10c204ce7564ed57a2c7f90`

```text
# Coordinate development-document QC gates

Load **sdd-conventions**' **Development-document QC** reference (`skills/sdd-conventions/references/development-document-qc.md`, bundled dependency) for canonical count/conformance/report/readiness rules. Artifact owners assess readiness; sdd-manage schedules reviews, routes corrections and enforces dependent-stage gates. **sdd-report**'s **Document QC reports** reference composes adjacent reports from their actual evidence.

## Stage handoff

| Completed input | Required owner assessment | Dependent operation |
| --- | --- | --- |
| SPEC / FEATURE-SPEC and applicable children | sdd-specify: accepted PROJECT/design conformance | PLAN / dependent feature planning |
| PLAN / FEATURE-PLAN with relevant layout | sdd-plan: SPEC conformance and phase/milestone decomposition | TASKS / dependent feature tasks |
| TASKS / FEATURE-TASKS and applicable children | sdd-tasks: PLAN conformance, scope and task hierarchy | Implementation or creation/projection of hosted task objects |

1. Establish the selected document/feature scope, accepted governing inputs, authorized effects and stopping point. Authoring includes its scoped QC correction/recheck and report; read-only review returns findings without silently correcting sources. Literal selected-path-only restrictions prevail; missing required report permission is a concrete scope blocker, not permission to widen paths.
2. At entry and each dependent transition, compare actual root/children/upstream state with current review evidence, finding dispositions, scope/coverage and readiness. Reuse demonstrably current equivalent reviews; explain materiality/equivalence from actual differences. A Ready label, file presence or a historical feature review is insufficient alone. Do not fabricate a review for an older project.
3. Obtain the focused missing assessment through the relevant owner within the already authorized scope. Creation/revision of an artifact includes review, authorized bounded corrections, recheck and report persistence before downstream progression. Use existing requirement/component IDs and grouped coverage; no new administrative milestones or task chain is needed for preparation QC.
4. Route missing design/behavior/strategy decisions upstream. Do not revise SPEC to excuse PLAN omissions or PLAN to accommodate accidental TASKS strategy. The owner may resolve routine choices already authorized; ask only for a genuinely missing consequential decision. Preserve read-only limits and unselected owners.
5. Have the owner produce the adjacent root report with current identities, coverage/count assessments, original findings, appended Revision N rechecks and Ready/Blocked evidence. Corrected artifacts and their report are one coherent preparation checkpoint under [coordination persistence](coordination.md#persist-repository-changes). Do not progress on a draft report, unpersisted required boundary or deferred confirmed issue. Honor explicit local-only publication limits; report any established dependent requirement for unavailable remote evidence separately.
6. For a blocked input, identify the finding, actual owner, needed correction/review scope and blocked dependent operation. Continue only independent authorized work. Explicit human exceptions name scope/consequences without relabeling Blocked as Ready or bypassing implementation acceptance.

## Amendments, scope and continuation

Material changes to design, behavior, strategy, hierarchy/dependencies or layout invalidate affected downstream review until rechecked. Recheck only impacted concerns; routine completion status/evidence updates alone need not invalidate unchanged conformance. Initial preparation and focused direct calls use the same gate. Main/feature task execution still pushes outstanding commits before other task work; readiness review follows that prerequisite and precedes new execution/phase projection.

sdd-integrate-feature and sdd-steer retain their accepted correction ownership. Coordinate owners' focused assessment of changed main/feature documents and their adjacent reports before dependent use. A SPEC-only incorporation does not authorize unselected TASKS/PLAN edits: report their invalidation and keep those downstream gates blocked until their separately authorized recheck. It can finish its coherent selected incorporation without claiming whole-project readiness.

Feature QC reports stay adjacent to their active roots and, when eligible/in scope, archived sources. Implementation reports retain their lifecycle phase/feature prefixes. Preserve scope, report/source identity, original findings and review history during moves; archive readiness is historical, not current main-document acceptance.

After interruption, inspect files, report source identities, pending corrections, index and commits. Finish the same correction/recheck/report/push without regenerating valid documents or duplicating Revision sections. Do not mark a gate Ready from a lost response, checkbox or commit subject. No new transaction journal is required.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/branch-management.md

SHA-256: `7f5fa93c685e8983efe72711f3ee6673dac6e9c6125406e23415a88e452dcb34`

```text
# Git branch management

Use this coordinator procedure for mutating branch setup, reuse, continuation, and authorized phase transitions. Apply **sdd-conventions**' **Workflow identity** rules; use [Git workflows](git-workflows.md) for explicit integration/publication. Local Git operations require no hosting backend. Execution/steering owners retain their commits and pushes; sdd-orient observes state without branch mutations.

## Establish context and identity

1. Use current orientation to identify eligible worktree, actual branch/HEAD, applicable instructions, pending-change ownership, authorized workflow/range, and accepted sources. Read-only review or selection creates no branch. Implementation pushes outstanding commits on the current established branch before task work or new branch setup; never create a branch to evade a push blocker.
2. Establish working branch, target, starting checkpoint, relevant HEADs and remote destinations. Main development identifies its actual main integration branch explicitly; revision/feature targets may be that branch or the active phase. Steering targets the paused implementation branch. A prefix or default-branch name proves neither target nor ownership.
3. Allocate or recover the convention's campaign identity for revision/steering/feature, or the owning PLAN/TASKS phase number for main implementation. Inspect reviews, features, phase-nested revisions and relevant remote state for allocation/collisions. Record the full baseline, actual working/target identities, scope, and active source links in the existing campaign/task/change record before dependent work. Preparation-only can reserve identity without authorizing implementation.
4. For revision/steering, ensure the workflow-specific revision directory/record matches the branch identity; steering uses the owning phase report directory's revisions prefix; a steering report can begin with objective/context and gain verification results later. For feature preparation, reserve its features directory with a concise README identifying full baseline, branch/target, scope, and active sources. Main documents remain in docs/dev. Do not fabricate optional review stages or a second registry.

## Create or reuse

- Reuse only when context, history, target and pending work fit the same scope. Preserve suitable legacy/in-flight names or explicit project/user overrides and their recorded association; no automatic migration.
- For new work, choose the workflow convention's branch name and validate it with `git check-ref-format --branch`. Inspect local/remote name collisions and worktree occupancy. An unrelated occupied name needs a distinct slug suffix without changing campaign identity; remote uncertainty is not proof the name is free.
- Create from the established target checkpoint before scoped edits. Use a separate worktree where unrelated dirty work or target availability requires it; preserve original staging/work and never implicitly stash/reset/clean. Do not check out one branch in two worktrees.
- An unborn/detached/conflicted state, missing usable checkpoint/target/remote, unresolved ownership or inability to establish identity blocks setup. Report the concrete decision/facility rather than guessing a different destination.
- Publish branch checkpoints through the active owner's ordinary Git push and verify remote containment; do not create the same remote ref through a duplicate API operation. This manager needs no sdd-forge branch capability or PR workflow.

## Main phase lifecycle

Apply [phase activation](phase-activation.md) before the phase's first task and every authorized next-phase transition. Hosting reads the complete plan but projects only the eligible phase. Require explicit review units and confirmed phase objects when tracking is active.

Select main-project work on the owning `phase/<number>-<slug>` branch. A bounded task or milestone request within an incomplete phase ends with verified commits/pushes and a paused phase branch, not a merge into main. Record completed range, remaining phase work, applicable evidence and current target context.

When all phase work, delivery and phase reviews/reports, applicable hosted milestone closures and exit evidence are complete, use the Git protocol for one explicit merge into the established main integration branch, verify the merged state, publish, and confirm containment. A checkbox or completed subset is insufficient. Failed exits or publication retain branch/merge state; do not create the next phase.

Only when the request authorizes further work, create the next phase branch from the updated verified/published main checkpoint and re-establish its scope. Split an authorized cross-phase range into sequential phase segments; each phase must meet its exit before the next branch starts. Do not execute extra tasks or perform an unrequested continuation to fill a phase. An explicit instruction to integrate a partial phase is a recorded override with its scope/evidence consequences, not the default.

Feature/revision integration into a phase updates that phase's accepted inputs and evidence; it does not complete the phase. Steering returns control after its amendment merge. Standalone revision/feature boundaries retain their own accepted scope and integration gates.

## Continuation

Recover identities and actual file paths from retained records and Git; names alone do not prove state. Distinguish incomplete phase work, pending archive/reconciliation, uncommitted merge, completed merge awaiting push, and an already integrated campaign. Resume the same authorized operation rather than allocate another identity or repeat an existing merge. Report ambiguous ownership/target and preserve valid work. Retain branches unless deletion is explicitly requested or covered by project policy.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md

SHA-256: `0f2db55e9bc50fe3f782c215884a52f8027e654367b8cf8bd6f8207215ca88df`

```text
# Scoped authorization for review and revision publication

Apply this policy with the actual human request, accepted campaign scope, established repository and working/target branches. sdd-manage supplies this authorization context to execution and platform review; the platform retains its permission and review controls.

## Authorized effects

For requested repository review/revision work, this policy authorizes the following effects within that request's accepted scope:

- Commit requested review records or verified revision results to the campaign's review/revision branch. A review-only request authorizes its requested records, not repairs to reviewed source.
- Push those commits to the established repository and campaign branch, including the report checkpoints prescribed by the review/revision workflow.
- Merge the verified completed review/revision branch into its established integration target, with the required explicit two-parent merge and merged-state checks, and push the target. A requested review stage may finish by integrating its records without implementing its proposed repairs. Source revisions require their own implementation authorization.

The human request and this policy establish scoped authorization for these effects; commits, pushes and merges are not independently classified as unauthorized solely because they publish requested work. Carry explicit human limits forward: preparation-only, pause, local-only, unmerged-branch, selected-path, destination or stopping-boundary instructions govern the actual eligible effects. Do not publish an unfinished or unrelated branch difference.

Establish identity and checks using [branch management](branch-management.md), [Git workflows](git-workflows.md) and [review/revision coordination](review-and-revision.md). This policy does not select a repository from a branch prefix, authorize unrelated destinations or widen a requested review into source implementation.

## Supply authorization after a rejection

1. Preserve the exact rejected operation and local state. Record the reviewer/tool's stated reason; inspect whether the operation was applied despite a lost response before retrying.
2. Assemble the authorization context below from observed facts. Cite this policy together with the actual human request and scope; the policy file alone is not evidence that an arbitrary operation was requested.
3. Supply that context through the platform/tool's supported authorization or review channel, or in the next operation request where that channel accepts context. Ask for assessment of the same bounded operation. Do not frame the request as an automatic exemption or an instruction to override platform review.
4. Retry only when the supplied authorization/new evidence resolves the rejection through the supported mechanism. Do not repeat an unchanged denied request, switch tools/transports/accounts to evade review, or assume that a policy citation granted platform approval.
5. If the platform still rejects the operation, or requires additional explicit authorization not available in the request, report that specific blocker and ask only for the missing authorization. Keep valid commits and pending publication/integration state; do not reimplement completed work.

| Authorization context | Evidence to supply |
| --- | --- |
| Human authorization | Actual command or applicable standing instruction; scope and explicit limits. |
| Policy | This file's path and applicable authorized effect. |
| Repository and destinations | Observed remote identity, review/revision branch and established merge target. |
| Exact effect | Commit/ref to push, or pinned source/target tips and intended two-parent integration. |
| Content scope | Owned changed paths and concise purpose; source repairs versus review records distinguished. |
| Verification | Actual checks/results, branch-difference eligibility and merge evidence where applicable. |
| Rejection | Stated reason, known successful/unknown effects, and how this context addresses the missing information. |

Keep credentials out of the context. Reuse existing campaign/report evidence rather than adding a separate mutable authorization registry. A failed authorization review is distinct from a Git credential failure; credential replacement cannot remedy it.

## Platform and workflow responsibilities

This is a scoped authorization policy, not a platform permission change. sdd-manage explains why the requested effect is authorized and supplies evidence; the execution owner performs approved Git operations; the platform decides whether its controls permit the operation. Do not claim approval from this file's existence or a locally successful check.

Report authorization, local completion, publication and integration as distinct facts. Read-only Git/provider inspection can establish identity and pending state without replaying a rejected write. Preserve working branches and completed evidence on a blocker, and resume the same authorized effect when its facility/approval is resolved.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-report/references/object-drafts.md

SHA-256: `f0c894eb233713f18cb48ac2a1f8ecea474c7891276f948443b8cc16462391fc`

```text
# Issue, commit, and PR drafts

Keep the same task identity across all outputs. Use the project-wide ID from its owning TASKS or FEATURE-TASKS entry; include a resolved issue reference only when **sdd-forge** supplies a unique repository and number. Match the requested object's time perspective: an issue describes intended work, while a commit or PR describes actual changes and available evidence.

## Task issue

Return `title` and `body` separately. Format the title as `[<task-id>] <task title>`, using the owning task list. Draft the body from the task outcome, reason and project context, expected scope and dependencies, objective acceptance and prescribed checks, and source document links. Add relevant kind-specific details. For example:

- **Performance:** Describe the problem with the current implementation, explain how the proposed approach may improve it, and identify the measurement plan and any established baseline. Do not present an expected speedup as an achieved result.
- **Security:** State the affected guarantee and risk without exposing exploit instructions or credentials.

**sdd-report** owns the title and body format. Preserve an exact task identity marker when one is supplied. Never invent host labels, milestone associations, issue URLs, or resolution state.

## Git commit

For a first SDD commit or adoption backfill, load **sdd-manage**'s [repository bootstrap](../../sdd-manage/references/repository-bootstrap.md). Confirm the commit owner has included or validly retained root disclosure/usage records and README links within scope. Return missing bootstrap evidence to that owner; drafting does not perform bootstrap or establish a committed result.

Draft a short imperative subject naming the actual change. For task-associated work, always include the owning task ID. For preparation or maintenance without an assigned task, do not invent an ID. Use a body when the reason, verification, migration implications, or multiple issue references need explanation. Base it on the inspected diff and checks, not merely the task brief.

Use `Refs owner/repo#123` when the commit advances an issue without completing it. Use `Fixes owner/repo#123`, `Resolves owner/repo#123`, or `Closes owner/repo#123` when the commit fully resolves that issue and the evidence supports completion. A commit may reference multiple issues, with a separate appropriate reference for each; omit issue references when no verified association exists. On GitHub, closing keywords may close an issue when the commit reaches the default branch. **sdd-forge** still reconciles issue closure after verified task completion, without waiting for that automation. If verification has not been run, say so in a proposed body rather than claiming it passed. The active implementation workflow makes and checks its commits; **sdd-manage** coordinates persistence for other authorized repository changes.

## Merge commit

Draft a subject identifying the actual feature, steering amendment, or selected range, such as `Merge phase 2 Archive support` or `Merge feature ZIP support`. A main milestone/task subset does not justify a merge draft while its phase remains incomplete. Return the subject and body separately. Include the working and target branches, starting checkpoint and verified parent tips, included task IDs where applicable, boundary and merged-state checks, material conflict resolutions, and limitations. Do not represent an amendment as completion of the next task. The coordinator performs the explicit two-parent merge; drafting the message does not authorize extra work or a hosted PR.

## Pull request

Draft a title and description only when requested; this skill does not create a PR. Scope the text to the actual branch diff and its included task IDs. Summarize **What**, **Why**, **Verification**, and **Result**; add the relevant fields from [change kinds](change-kinds.md). State the base branch and integration status only when known. List unrun checks, limitations, and remaining work explicitly rather than presenting partial work as complete.

A code health PR should explain the ownership or maintainability problem and the checks supporting behavior preservation. A performance PR should include baseline and current times, input size, environment, method, and whether the measured gain is meaningful. Do not imply that GitHub PR operations are available through **sdd-forge**.

## Examples

These show formatting for an issue title, commit message, and PR draft. Use actual task IDs, issue references, checks, and results for the current work.

### Issue title

```text
[T-012] Implement ZIP stream support
```

### Commit message

```text
Clarify filesystem utility ownership (T-041)

Move shared filesystem helpers into the module named by the project layout.
Update its documented responsibility; the focused unit suite passed.

Refs owner/repo#123
```

### Code health PR

```markdown
# 🧹 Clarify filesystem utility ownership

- 🎯 **What:** Renamed `common.py` to `fs.py` and updated its documented responsibility.
- 💡 **Why:** A focused module name makes ownership clear under the project's layout rules.
- ✅ **Verification:** Inspected layout references and passed the focused unit tests.
- ✨ **Result:** Filesystem utility ownership is explicit, with behavior preservation supported by the cited checks.
```

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-report/references/document-qc-reports.md

SHA-256: `fe09d71b27a70ef806898634c8bd7b32b12b0d425006e5b4c47a5b551e426e07`

```text
# Document QC review reports

Compose from the artifact owner's actual review/correction evidence under **sdd-conventions**' **Development-document QC** policy. This skill does not decide readiness, execute checks or authorize corrections. Use the owner's current Ready/Blocked conclusion with its supported scope and limits.

## Placement and identity

Place `SPEC-REVIEW-REPORT.md`, `PLAN-REVIEW-REPORT.md` or `TASKS-REVIEW-REPORT.md` beside the reviewed root; feature counterparts use `FEATURE-SPEC-REVIEW-REPORT.md`, `FEATURE-PLAN-REVIEW-REPORT.md` and `FEATURE-TASKS-REVIEW-REPORT.md` beside the selected feature roots. One report covers the root and applicable children. PLAN review covers relevant layout. These preparation reports are distinct from phase/milestone implementation reports and general campaign records. At feature archive retain selected QC reports beside archived sources and repair authorized links; historical feature readiness does not certify current main documents.

Identify artifact paths and exact reviewed/governing states: available full Git commit with file/blob identities, or content hashes for pending edits. A report need not contain its own future commit SHA. Use existing IDs/links and a compact grouped coverage table; no separate traceability database or row per SPEC sentence is required.

## Compact report structure

```markdown
# PLAN review report

## Current gate

State: Ready or Blocked, as established by the owner.
Reviewed scope/state: root, applicable children/layout and exact identities.
Governing inputs: accepted upstream roots/children and exact identities.
Checks/evidence: actual review methods and outcomes; limitations/exceptions.
Remaining blockers and affected downstream stage: explicit findings or none.

## Initial review

Record date/reviewer, original reviewed states, grouped conformance coverage,
count assessments and stable located findings with consequences and rechecks.

| Group | Delivery count | Excluded review units | Scope/count assessment and rationale |
| --- | --- | --- | --- |
| Actual phase or milestone ID | Observed number | IDs/count | Retained or revised boundary with evidence |

| Finding | Location / consequence | Correction owner / objective recheck | Current disposition |
| --- | --- | --- | --- |
| Stable review ID | Concrete evidence | Actual responsible owner | Open / resolved / rejected with evidence |

## Revision 1

Preserve the original finding IDs. Record actual corrected files/owners, why,
exact revised artifact and governing states, performed rechecks/results,
current dispositions, exceptions and remaining blockers.
```

Use equivalent concise prose where a table adds no clarity. Count tables apply to PLAN phases and TASKS delivery milestones; SPEC instead reports design/contract coverage. Label planned checks as planned, not performed. Do not fabricate a Revision section when no correction/recheck cycle occurred.

## Retained review and revisions

Append `Revision 1`, `Revision 2`, etc. for each correction/recheck cycle, including a later recheck after changed inputs; never erase original observations or earlier revised-state evidence. Update only the concise current gate/index to reflect the latest result. Explain retained equivalent evidence where changes do not affect its reviewed concern. Preserve finding IDs across cycles and avoid duplicate reports after interruption.

Ready requires current applicable coverage and no unresolved confirmed issue. A justified small/large group or rejected false positive is an assessment with reasoning; a knowingly deferred confirmed issue is Blocked. Explicit human exceptions keep their scope/consequences visible and do not relabel the review as passed. The implementation report's non-critical code TODO allowance does not clear document preparation gates.

Return the report, checked source identities, gate supplied by its owner, actual checks, limits and required corrections. The active authoring/integration/steering workflow persists corrected artifacts and report together under ordinary scoped Git rules.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-report/references/completion-reports.md

SHA-256: `1ed1bd98e8e78c0d22b049fa57843e87e4a740bd1415a7840b894493a7bffb46`

```text
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

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-tasks/references/progress-review.md

SHA-256: `32be8fbaa5e67e807d7c7f7be964c56ab7f65bd6398784606090fcdd9e40a912`

```text
# Progress review

TASKS and an active FEATURE-TASKS are human-readable status views of the complete hierarchy and scoped feature delta respectively. Git commits, verification results, and inspected artifacts provide the evidence behind them. Compare checked items in the applicable list with the present implementation and the task's acceptance evidence; do not infer completion from a checkbox, a commit message, or file presence alone. Review is read-only; report missing or conflicting evidence to the owning workflow.

## Completion evidence

Review existing claims against their accepted task or parent exit conditions and the implementation, verification, documentation, and Git evidence supplied by **sdd-implement**. It owns completion criteria and task or parent checkbox updates. **sdd-report** composes the resulting implementation summaries. Report missing evidence or a claimed scope broader than the evidence supports; this review does not perform completion updates.

Validate explicit review units and their report paths against the [backend object lifecycle](../../sdd-conventions/references/backend-object-lifecycle.md). Checked parents need review/report evidence as well as delivery-task exits; a feature parent cannot establish whole-project hosted closure. Report missing review tasks as an accepted-hierarchy amendment need, never silently insert them.

## Route findings

Pass task-list reconciliation, including feature-delta changes to task scope, dependencies, or parentage and FEATURE-TASKS incorporation into TASKS, to **sdd-integrate-feature**. Direct checkpoint amendments belong to human-commanded **sdd-steer**. Pass unfinished main implementation or completion-evidence gaps to **sdd-implement**. Report eligibility and dependency findings to **sdd-implement** before it selects further work.

## Distinguish preparation readiness

Use [conformance review](conformance-review.md) for task structure, PLAN alignment and preparation gates. Progress checks report missing/stale preparation evidence without automatically repairing documents. Ordinary status/evidence changes alone do not invalidate unchanged contract/decomposition review; changed scope, hierarchy, dependencies or upstream decisions require affected reassessment under the shared QC policy.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-tasks/references/conformance-review.md

SHA-256: `79e186c004f57193bf7a9ca8aaf7b6075d85fac240ae05a1ececa11ec7eea92e`

```text
# Task-list conformance and decomposition review

Use after TASKS/FEATURE-TASKS generation or material amendment, and for an explicit structure/conformance review. [Progress review](progress-review.md) instead assesses completion evidence; it cannot substitute for preparation QC. Apply **sdd-conventions**' **Development-document QC**, **Task hierarchy** and **Backend object lifecycle** references.

## Inputs and review

1. Identify selected owning list/children, exact state, accepted design/SPEC/PLAN/layout and current upstream review evidence. For a feature, review the delta against accepted main/feature sources without forcing unselected whole-project edits. A missing FEATURE-PLAN is acceptable only when sufficient accepted main strategy supplies its boundaries. Absent/stale required PLAN conformance blocks task derivation/use; coordinate the focused review rather than inventing a pass.
2. Map each planned delivery outcome and exit to sufficient executable work and trace acceptance to SPEC using existing IDs/links. Assess missing/duplicated scope, invented behavior, hidden strategy changes, feasible dependencies and implementation/test/documentation/failure/integration/packaging coverage. Preserve PLAN phase/milestone IDs and accepted boundaries.
3. Report delivery task counts for every delivery milestone and separately identify excluded dedicated review/report-only tasks. Apply shared 3–5 guidance and explicit 1–2/10+ assessments with rationale; inspect semantic size even for in-range groups. Do not count a task's own checks/docs as extra tasks, hide whole subsystems behind a single ID, or split into trivial edits to meet a number. Empty delivery groups require correction or accepted purpose. The mandatory one-task phase review milestone is excluded from this diagnostic, never from execution selection.
4. Check project-wide unique stable task IDs, exactly one executable owner, four-space checklist hierarchy, prerequisite feasibility, explicit final review/testing/report task per delivery milestone and final one-task phase review milestone. Review links and report paths against lifecycle policy. Checked status requires separate progress evidence; this review does not mark implementation complete.

## Corrections, evidence and gate

Authoring includes bounded initial task-list corrections, recheck and adjacent `TASKS-REVIEW-REPORT.md` or `FEATURE-TASKS-REVIEW-REPORT.md` through **sdd-report**'s **Document QC reports** format. The root report covers applicable children. Preserve original located findings and append Revision N cycles; count rationale is an assessment, not an automatic defect.

A task breakdown that exposes inadequate PLAN returns an amendment to sdd-plan, then rechecks affected inputs; do not silently change delivery strategy in TASKS. Necessary SPEC/design decisions return to their owners. Existing feature reconciliation belongs to sdd-integrate-feature; commanded checkpoint amendments belong to sdd-steer. Review-only returns findings without changing the governing list, checkboxes or code. A report is written only within authorized scope.

Correct all confirmed QC/conformance issues before implementation or hosted projection. Persist corrected list and report together through sdd-manage, then hand current Ready evidence to dependents. A known deferred issue or stale report remains Blocked; explicit human exceptions record scope/consequences without declaring a pass. Pure selection may identify candidate IDs but must report blocked execution eligibility. On interruption compare actual files, pending corrections, source identities and Git evidence before continuing the same review; preserve valid work and append rather than duplicate history.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-conventions/references/development-document-qc.md

SHA-256: `c108f60ddffee2665d759276b650a430fde1abad4361bafa20311b63f077429f`

```text
# Development-document quality and conformance

Apply these invariants through the artifact owner and coordinator. This reference defines shared criteria and readiness, not authorization to edit an artifact.

## Preparation gates

| Completed artifact | Required review | Gate before |
| --- | --- | --- |
| SPEC root and applicable children | Conformance to accepted PROJECT, ARCHITECTURE and DECOMPOSITION; coherent, complete and assessable contracts. | Dependent PLAN authoring. |
| PLAN root and applicable children, with layout where relevant | SPEC coverage/conformance, bounded incremental delivery, phase/milestone decomposition and feasible exits/dependencies. | Dependent TASKS generation. |
| TASKS or active FEATURE-TASKS | PLAN conformance, complete executable coverage, bounded task decomposition, dependencies, unique identity and review units; trace acceptance back to SPEC. | Dependent implementation or hosted projection. |

Creating/revising an artifact includes its QC review, bounded corrections within accepted scope, recheck and report persistence before dependent progression. Review-only requests remain read-only with respect to governing artifacts; report findings without silently correcting them. Writing a requested review report is distinct from editing the reviewed document. No stage authorizes code implementation by implication.

If a correction needs a new behavioral, architectural or delivery decision, the coordinator routes it to the governing owner/human and blocks dependent work. Do not rewrite SPEC to fit PLAN, or PLAN to fit an accidental task breakdown. A prerequisite decision can be resolved within existing authorization; do not request redundant approval for already accepted scope.

## Decomposition and count policy

Prefer approximately **3–5 delivery milestones per phase** and **3–5 delivery tasks per milestone** when the real work naturally supports that shape. These are planning heuristics, not quotas or a claim of universal optimality. Minimal useful increments, contracts, dependencies, integrated acceptance and maintainable scope determine the actual boundaries.

Count delivery milestones separately from the dedicated phase review milestone. Count delivery tasks separately from dedicated review/report-only tasks. Product implementation, integration, test, documentation and packaging work counts as delivery when it contributes to the capability; administrative/report-only work does not inflate the count. A delivery task's own testing/documentation remains part of that task. Counts must expose actual work, not hide oversized units behind labels.

| Delivery count | Required assessment |
| --- | --- |
| 1–2 | Explicitly review potential fragmentation or a boundary with too little independent value. Retain a small group when its narrow scope, cohesive outcome and dependency/risk/handoff purpose are clear. |
| 3–5 | Preferred starting range; still inspect actual scope and cohesion. A count in range cannot establish good decomposition. |
| 6–9 | Assess normal scope/cohesion and explain a material departure from the preferred range. Do not mechanically split an otherwise coherent group. |
| 10 or more | Explicitly review overloading, scope drift, weak boundaries and delayed integration. Split or narrow if evidence shows excessive scope; justify retention if the units genuinely form a bounded coherent outcome. |

Apply the same table to delivery milestones per phase during PLAN review, then to delivery tasks per milestone after TASKS generation. Report counts for each group, any excluded review units, triggered questions and the retained/revised boundary rationale. Empty delivery groups require correction or an accepted explicit purpose; the mandatory one-task phase review milestone is an intentional excluded review unit.

A single task implementing a subsystem is still oversized even when its milestone has only three tasks. Likewise, ten trivial file edits are not ten useful increments. Inspect behavioral contracts introduced, component/dependency breadth, prerequisite chains, failure/integration paths, verification effort and handoff overhead. Early meaningful end-to-end usefulness and timely regression checks remain required; do not defer coherent behavior until an enormous final milestone.

Do not add requirements, padding tasks, artificial milestones or phases to reach the preferred range. Do not merge independent outcomes solely to reduce counts. An occasional small phase is acceptable with a documented bounded scope; repeated tiny phases require assessing the larger delivery structure. Counts flag review questions; a finding needs a concrete consequence and evidence.

## Conformance review criteria

**SPEC against design:** compare structural ownership, interfaces, dependency direction and cross-component obligations with ARCHITECTURE/DECOMPOSITION; trace accepted project outcomes and non-goals into canonical behavioral contracts and objective acceptance. Assess missing/contradictory responsibilities, invented behavior, unsupported structural assumptions, error/resource/lifecycle contracts and parent-child coherence. Design may need correction rather than SPEC; resolve that conflict explicitly.

**PLAN against SPEC:** establish a delivery route for every significant accepted contract and end-to-end acceptance obligation. Assess omitted/duplicated scope, invented features, deferred obligations presented as complete, incompatible dependencies, feasible objective exits and the earliest useful end-to-end increment. Layout must support the design and planned integration. Review phase/milestone counts and semantic scope before TASKS derives executable work.

**TASKS against PLAN:** map each delivery outcome/exit to sufficient executable work, preserving phase/milestone IDs and boundaries. Assess gaps, duplication, new requirements, strategy changes hidden in tasks, excessive/trivial task scope, feasible dependency order, tests/docs/failure/integration coverage and evidence. Validate project-wide unique task IDs, one owning list, exact checklist form and mandatory milestone/phase review tasks. Review task counts without counting the dedicated review tasks toward the preferred delivery range. TASKS may reveal an inadequate PLAN; return that amendment to sdd-plan, then recheck, instead of silently changing strategy.

Use existing requirement/component IDs and local links for traceability. A compact grouped coverage table is sufficient when it demonstrates completeness; do not require a new traceability database, one row/task per SPEC sentence or duplicate contracts in the reports. Review both numerical shape and actual meaning.

## Review reports and correction records

Place the root review report beside the artifact being reviewed:

| Reviewed root | Adjacent report |
| --- | --- |
| `docs/dev/SPEC.md` | `docs/dev/SPEC-REVIEW-REPORT.md` |
| `docs/dev/PLAN.md` | `docs/dev/PLAN-REVIEW-REPORT.md` |
| `docs/dev/TASKS.md` | `docs/dev/TASKS-REVIEW-REPORT.md` |
| Active `FEATURE-SPEC.md`, `FEATURE-PLAN.md`, `FEATURE-TASKS.md` | `FEATURE-SPEC-REVIEW-REPORT.md`, `FEATURE-PLAN-REVIEW-REPORT.md`, `FEATURE-TASKS-REVIEW-REPORT.md` beside their respective roots. |

Adjacency governs these preparation QC reports, including reports beside active FEATURE documents in docs/dev. The existing phase/feature prefixes continue to govern implementation reports and feature package records; source revision must distinguish these categories explicitly.

A root report covers its applicable focused children; do not require a separate report per child. During feature archive, retain selected reports beside the corresponding archived feature sources and repair in-scope links. After accepted incorporation, reassess affected main-document conformance; a feature review is not proof that the complete main documents conform. General campaign records retain their standard reviews layout. These preparation reports are distinct from implementation milestone/phase reports defined by the backend lifecycle.

Keep each report concise: artifact identity and exact reviewed state, governing source identities, scope/criteria, coverage and counts, stable located findings with consequence and correction/recheck, current gate result and limits. Use `Ready` only after current applicable conformance and QC pass; otherwise `Blocked`, with explicit reasons. Counts and justified exceptions are assessment results, not findings automatically.

Append a **Revision 1**, **Revision 2**, etc. section for each correction/recheck cycle. Record original finding IDs, actual edits/owners, why, exact revised document state, checks/outcomes, disposition and remaining blockers. Preserve original observations and append evidence; update the concise current finding index and gate result without overwriting review history. Git records commits; no report needs to contain its own commit SHA or a parallel transaction log.

Correct every confirmed QC/conformance issue before dependent progression. Resolve false positives or retain an acceptable small/large group with explicit reasoning rather than manufacture a defect. A knowingly deferred unresolved confirmed issue cannot support `Ready`; an explicit human exception records its scope and consequences without relabeling the review as passed. The non-critical code TODO deferral policy for implementation reports does not automatically apply to these document preparation gates.

Persist corrected artifacts and report/recheck evidence together. On interruption, inspect actual files, source identities and commits; finish the pending correction/recheck/report/push within scope. Do not regenerate good documents or duplicate reports merely because a response was lost.

## Ownership and invalidation

| Owner | Responsibility |
| --- | --- |
| sdd-conventions | Shared QC/count/conformance invariants and report identity. |
| sdd-manage | Schedule gates, establish authorized scope, route corrections/upstream decisions, persist preparation boundaries and block dependent progression. |
| sdd-specify | SPEC/design conformance review and authorized SPEC corrections. |
| sdd-plan | PLAN/SPEC conformance, phase/milestone decomposition and layout review; authorized strategy/layout corrections. |
| sdd-tasks | TASKS/PLAN conformance, delivery task decomposition, hierarchy/dependency review and authorized initial task-list corrections. |
| sdd-report | Review report and appended revision-section composition from actual owner evidence; no independent readiness decision. |
| sdd-design | Accepted architectural/decomposition corrections where required; no automatic redesign by downstream owners. |
| sdd-integrate-feature / sdd-steer | Accepted feature incorporation or commanded checkpoint amendments retain their established correction ownership; trigger affected QC reassessment. |
| sdd-orient / sdd-implement | Observe current readiness/evidence; implementation consumes eligible reviewed inputs and does not redefine document policy or run unrequested corrections. |

Initial preparation QC needs no extra implementation milestones/tasks solely for administrative review. It is part of the authoring workflow. Milestone/phase implementation code review remains mandatory later and is owned as defined by the backend lifecycle.

Review readiness is tied to actual artifact and governing source state. Material amendments invalidate affected downstream assessments until rechecked; unchanged scope may retain supported evidence. Review the impacted dependency chain rather than rerunning every project audit after every edit. Reuse demonstrably current equivalent prior reviews for existing projects; absent or stale evidence requires the focused missing review, not a new fictional historical pass. Feature preparation reviews its selected delta and affected interfaces against accepted main inputs, without forcing a whole-project rewrite.

## Evidence currency during implementation

Identify reviewed root/children and governing inputs by available commit plus blob identities, or exact content hashes for pending edits. Assess material changes to requirements, design, delivery strategy, task scope, dependencies, hierarchy or physical ownership. Routine task completion checkbox/evidence updates do not invalidate an unchanged decomposition or contract assessment by themselves; establish and report equivalence of the reviewed concern against the actual diff. A changed scope or upstream guarantee requires affected review even when its report says Ready. Do not infer currency from a filename or status label alone.

A direct dependent-stage invocation follows the same gate as a coordinated request. Obtain the focused missing review within the already authorized scope; read-only assessment can return its result without persisting a report when writes are prohibited, but absent durable required evidence remains a progression blocker. An explicit human exception names its affected scope and consequences; it does not turn a Blocked report into Ready or supply missing implementation acceptance.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-integrate-feature/references/feature-incorporation.md

SHA-256: `52e311b66d7df21bea7f2c02463417d7219dabe844e2c98cafe03f0cb1aa7e30`

```text
# Feature incorporation

Treat each accepted feature document as a scoped delta and each main document as the complete intended description of its own concern. Identify which main nodes the selected delta changes and which unchanged nodes it references. Project instructions and accepted decisions govern; observed code or an unchecked task does not settle a design or behavioral conflict.

## Select and incorporate

1. Confirm the selected main target or targets and the corresponding accepted feature source. A feature may have no overlay for some levels. Permit a single document, such as SPEC alone, when its change can be expressed coherently there. Record affected but unselected dependents; do not expand the edit scope silently.
2. For PROJECT, integrate changes to purpose, users, scope, outcomes, or constraints into the brief. For ARCHITECTURE and DECOMPOSITION, integrate accepted block and component boundaries, dependencies, interfaces, and relevant rationale into the owning root and focused children. Preserve the difference between architectural structure and final behavioral contracts.
3. For SPEC, integrate final supported and unsupported behavior, errors, invariants, and objective acceptance into the owning root and children. For PLAN, integrate delivery strategy, phase and milestone definitions, dependencies, and exit checks. For layout, integrate changed physical ownership only where the accepted change requires it. Keep each concern in its main owner rather than copying it across documents.
4. When transferring tasks from FEATURE-TASKS into TASKS, require both lists in the selected edit scope. Move each owning entry into the complete hierarchy once, retiring its independently checked source entry in the same change while preserving project-wide IDs, dependencies, verified status, and durable evidence. If FEATURE-TASKS is outside scope, defer the transfer and report the required scope extension; TASKS-only reconciliation of existing main entries may still proceed. Reconcile parent placement and exit conditions against the accepted PLAN. A feature parent checkbox does not establish completion of its whole-project parent. Task-list creation and review belong to **sdd-tasks**; executable range selection, implementation, and completion updates belong to **sdd-implement**.
5. Read every changed main root and child as a coherent description of the intended end state. Remove superseded claims and editing-history language. Keep genuine backward compatibility or transition requirements as present obligations. Check parent-child links, affected cross-document contracts, and task references within the selected scope.

When a selected target depends on a still-unaccepted decision in another concern, stop that target and report the specific decision and owner. Continue independent selected targets only where their meaning remains sound. In particular, do not incorporate a task list against an unreconciled conflicting PLAN or SPEC.

## Task-list reconciliation

When TASKS or FEATURE-TASKS is selected, reconcile the accepted changes in its owning list; this need not incorporate the feature list into TASKS.

For an accepted feature delta, compare the intended final SPEC, design, PLAN, and layout with existing work, TASKS, and any active feature documents and FEATURE-TASKS. Revise affected tasks and dependency edges, remove obsolete uncompleted work, add necessary corrective work, and identify previously checked items whose acceptance has changed. Keep unaffected completed work and stable IDs. Revise an active feature list within its scope; revise main TASKS when the accepted end state changes its complete hierarchy. Do not leave a chronological amendment section or a list of discarded approaches in the main TASKS; Git retains that history. Preserve evidence for an implemented capability that was later removed in Git, while the current checklist describes only work required for the accepted end state.

When changed acceptance makes a checked task or parent claim stale:

- Record **Completion reassessment pending** beneath the affected owning entry, or in its existing linked evidence location, only when that location is in the edit scope. Identify the stable task or parent ID, changed acceptance and authoritative source, prior evidence whose scope no longer suffices, and required reassessment.
- Preserve the checkbox and previous evidence. The pending note makes the checked claim disputed; it is not current completion evidence. **sdd-implement** owns acceptance reassessment and checkbox correction. Direct checkpoint amendments retain **sdd-steer** ownership.
- Keep the note with the owning entry during task transfer. Preserve prior evidence as historical, and flag affected checked parent claims without inferring whole-project completion from feature results.
- If the owning list or evidence location is outside scope, report the deferred reassessment and needed edit scope without adding a note there or changing its status. Do not invoke implementation or change hosted state from the finding.

If the feature is withdrawn, preserve Git history and resolve the disposition of completed work before removing its task list. Task execution and completion verification belong to **sdd-implement**; reconciliation preserves evidence and the durable pending-reassessment notes for its review.

Apply the [backend object lifecycle](../../sdd-conventions/references/backend-object-lifecycle.md) when reconciling accepted review tasks, report links and parent evidence. Preserve milestone/phase review tasks and stable IDs during transfer; existing project-wide parents retain their full scope. Report warranted hosted reopening/reparenting to sdd-forge under authorized reconciliation, without performing it here. Future-phase feature work remains unprojected; scoped feature completion cannot close an unfinished project milestone.

Feature implementation reports remain under `docs/dev/features/<feature-id>/`, including after document incorporation/archive. Keep their provenance links from current owning entries; archiving feature sources does not relocate reports to the main phase tree.

## Scope and cleanup

Feature source documents remain active while other levels are integrated or work still depends on them. A selected SPEC-only incorporation does not archive the whole package, remove FEATURE-TASKS, or transfer unselected tasks. Preserve active sources and report deferred link/owner changes outside scope.

For a completed accepted feature, apply **sdd-conventions**' **Workflow identity** archive location. After selected final incorporation and task/evidence disposition, retain eligible sources in `docs/dev/features/<campaign>/` with their basenames rather than deleting them. Archive on the feature branch before final verification and Git integration; this skill owns document disposition, while sdd-manage owns the Git merge.

### Archive eligibility and procedure

1. Recover the package identity/full baseline and actual active sources from its navigation record and Git. Confirm completion and accepted incorporation scope; if completion verification or a necessary owner is unresolved, retain the active source and report the blocker.
2. Ensure accepted content is represented in the main owners, transferred tasks have one executable owner in TASKS, remaining work has a current authorized owner, and historical evidence remains findable. No active work may rely on a moved file as its sole authoritative source. FEATURE-TASKS remains active until its work/evidence disposition permits archival; document-only integration does not change it by implication.
3. Move only eligible selected sources, preserving basenames and any substantial child documents. Inspect for archive collisions rather than overwrite another record. Update in-scope links and evidence references; retain a source still required by unselected active links until those edits are authorized.
4. Update the package README with historical/archive status, source dispositions, current main owners/task references, and incorporation evidence. Mark archived task lists as historical snapshots, not executable owners. Archived checkboxes do not supply current task selection or completion; main owning entries preserve stable IDs and verified/historical evidence.
5. Recheck moved paths, relative links, cross-document consistency, unique task ownership, remaining active sources, and completion/publication reporting. Commit/push the coherent document checkpoint on the feature branch; coordinate final Git integration only when the authorized feature boundary is ready.

For a withdrawn feature, preserve historical evidence and resolve completed/remaining work disposition explicitly before archive/removal; withdrawal is not completed implementation. Report hosted identity/parentage impacts to sdd-forge when tracking is active, without mutating hosted objects here.

## Continue interrupted incorporation

- **Context:** Recover the selected target set, accepted feature sources, working/target branches, and starting checkpoint from the request, Git, and existing change evidence. An active feature campaign retains its working branch; a standalone integration uses a scoped branch under **sdd-manage**'s Git protocol. Ambiguous scope or dirty-path ownership blocks overlapping changes.
- **Partial state:** Compare actual selected roots, children, task lists, and links with the checkpoint and accepted delta. Identify completed amendments, unfinished reconciliation, partially moved archive paths, duplicate task IDs, conflicting executable owners, and stale acceptance. A changed SPEC or clean worktree is not proof that incorporation finished.
- **Resume:** Preserve valid incorporated content and historical evidence. Finish only selected owners, applying the ordinary unique-ownership, source-retention, and pending-reassessment rules. If task transfer is partially applied, inspect both entries and Git evidence before reconciling; require both lists in scope. Stop on unresolved identity or contract conflicts instead of creating a second executable task or deleting a guessed source entry.
- **Unselected owners:** A SPEC-only request leaves TASKS and FEATURE-TASKS untouched and reports their deferred consequences. Do not expand the request to repair all documents merely because the previous operation was interrupted.
- **Finish:** Check selected document consistency, links, task identity/ownership, and retained sources. Report coherent changes and unresolved dependencies to **sdd-manage** for commit/push and default explicit Git integration of the authorized boundary. Within a larger feature campaign, persist this document checkpoint on its branch and leave final merge to that campaign's boundary. Partial or conflicting incorporation is not a successful merge prerequisite.

Branch isolation protects the target from unpublished partial edits; it does not make individual working-branch edits transactional. No automatic rollback, reset, separate journal, or implementation invocation is required.

## Conformance after incorporation and archive

Material selected incorporation/reconciliation requires affected preparation QC under **sdd-manage**'s **Document QC gates**, using sdd-specify/sdd-plan/sdd-tasks assessment criteria while this workflow retains correction ownership. Persist selected corrected roots/children and their adjacent report/recheck evidence together within authorized scope. A feature review does not establish current full main-document conformance. Append Revision N cycles and retain original findings.

Do not expand a SPEC-only or literal selected-path request to amend unselected PLAN/TASKS or their reports. Report their affected invalidation and block dependent use until authorized reassessment; the coherent selected incorporation can finish without claiming whole-project readiness. Required selected-root QC whose report paths are explicitly forbidden is a scope conflict to resolve before claiming that preparation gate passed.

When selected feature sources become archive-eligible, move their associated QC reports with them, preserving adjacency/basenames, original reviewed identity/history and valid in-scope links. Retain a source/report pair if required link repairs or either move is outside scope. Preparation QC reports are distinct from milestone/phase implementation reports, which keep their established feature prefix. Recheck main-owner readiness independently; archived Ready is historical only.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-plan/references/review.md

SHA-256: `3500dd799e477807deee44e9e4a436626f22b8ce8bf91f1c7b8d3e1aa065c931`

```text
# Plan and layout review

For read-only review, inspect the relevant PLAN root and children, layout, accepted design and SPEC, active feature plan if any, and the current repository tree where placement matters. Check that phase and milestone exits are objective, dependencies and integration points are feasible, every significant contract has a delivery route, and physical ownership supports the logical boundaries. Report concrete gaps and conflicting authorities without editing governing documents.

Check that the earliest usable milestone is a minimal meaningful end-to-end slice, its inclusions/deferrals and acceptance are explicit, and each delaying prerequisite is justified. Check subsequent capability increments are behaviorally bounded, retain the working path, and include timely integration/regression evidence rather than postponing it to a final phase. A skeleton or mocked-only demonstration is insufficient by itself. At suitable milestones, check demonstrable functionality, relevant usability/risk evidence, and the consequential human decision being informed; distinguish technical exits from product/usefulness decisions.

Check that strategy belongs in PLAN, physical ownership in layout, behavior in SPEC, and executable units and status in TASKS or active FEATURE-TASKS. Check alignment with PROJECT, ARCHITECTURE, DECOMPOSITION, and SPEC. Review parent-child links and component-to-path routing in both directions, including tests, documentation, and integration. Read the main PLAN and layout nodes as standalone end-state descriptions without editing-history language; genuine compatibility and transition obligations may refer to an earlier released state.

Report concrete gaps and affected task-list dependencies. Direct corrections belong to [delivery plan](delivery-plan.md) or [physical layout](physical-layout.md); incorporation of accepted feature documents belongs to **sdd-integrate-feature**. A review does not authorize edits, task execution, or progression into another workflow.

## Required PLAN/SPEC QC gate

Apply **sdd-conventions**' **Development-document QC**. Establish current SPEC/design QC evidence for the accepted inputs; a material unresolved specification issue blocks dependent planning. Map every significant accepted contract and end-to-end obligation to a planned delivery route, including honest deferrals, failures, dependencies and objective exits. Identify omissions, duplication, invented features and scope drift. Verify that layout supports the accepted structure and planned integration; a layout-only review reports its affected PLAN implications without authorizing PLAN edits.

For each phase, report delivery milestone count separately from its final dedicated phase review milestone. Apply shared 3–5 guidance, explicit 1–2 fragmentation and 10+ overload/drift assessments, departure rationale and empty-group rules. Inspect semantic scope even for in-range groups: contract/component breadth, delayed usefulness, dependency chains, integration/testing effort and boundary overhead. Keep justified narrow phases; add no padding or quota-driven splits. Dedicated milestone review outcomes remain required even though excluded from delivery counts.

Authoring includes authorized bounded PLAN/layout correction, recheck and `PLAN-REVIEW-REPORT.md` adjacent to PLAN (FEATURE-PLAN counterpart beside its root); the report covers applicable children and relevant layout. Use sdd-report's **Document QC reports** format and append Revision N cycles. Route changed behavioral/design decisions upstream; never rewrite SPEC to fit PLAN. Persist the corrected strategy and review together before TASKS generation. Pure review does not amend strategy. Missing/stale evidence or confirmed unresolved issues blocks dependent generation; explicit exceptions remain recorded as exceptions, not Ready.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-orient/references/inspection-and-handoff.md

SHA-256: `1df6b1c7a972959a4b6fb5820ac2a8fbefe732b6abfdef1d52c319811777502f`

```text
# Inspection and handoff

Use this reference for read-only orientation. Collect enough evidence for the contemplated action; do not dump an entire monorepo into context.

## Project and authority

- Resolve the user-supplied path or current directory to a project root. In a monorepo, distinguish the governed subproject from the containing repository. When candidates are genuinely ambiguous, report them instead of choosing one silently.
- Read applicable root and more deeply scoped `AGENTS.md` files for anticipated paths. Follow their relevant references and project-designated instruction sources, including policies outside the project root when they apply.
- Identify contradictory or unreadable instructions and the exact affected action. Record rules for language, build, test, documentation, generated files, source ownership, and commit practices when relevant.
- Inspect `docs/dev/PROJECT.md` as the project brief. Determine the role of its actual contents. If it contains operating instructions, report them as applicable instructions and identify their scope and any conflict; document revision is a separate workflow.

## Git evidence

Use Git's inspection commands with optional writes suppressed. Plain `git status` can refresh index metadata even when file contents are unchanged. Apply `git --no-optional-locks` to each inspection command, or scope `GIT_OPTIONAL_LOCKS=0` to the inspection process; do not change repository or global configuration. For example, from the candidate project path:

```text
git --no-optional-locks rev-parse --is-inside-work-tree
git --no-optional-locks rev-parse --show-toplevel
git --no-optional-locks symbolic-ref --quiet --short HEAD
git --no-optional-locks rev-parse --verify HEAD
git --no-optional-locks status --porcelain=v1 --untracked-files=all
```

Distinguish a Git worktree from a bare repository, a Git directory outside the target project, or a path with no Git. Record branch or detached state; record an unborn HEAD explicitly. Note staged, unstaged, untracked, deleted, renamed, conflicted, and submodule changes where present. Scope status to the project and anticipated target paths without concealing relevant parent-level or shared files.

Do not assume dirty paths belong to the current task or the agent. Do not interpret clean status alone as proof that the intended work is finished or that documents agree. For the Git prerequisite to be met, the project must be inside a usable worktree; a missing HEAD, conflict, or ambiguous ownership is an additional blocker for ordinary mutation until a later workflow defines how to handle it.

For branch workflows, identify the working and target branches, starting checkpoint, remote destinations, branch occupancy in worktrees, and existing task/change evidence of the authorized boundary. Report in-progress merges, already merged commits awaiting publication, and unresolved target identity. Inspect Git ancestry and parent commits when relevant with optional writes suppressed; do not fetch, switch branches, create worktrees, or infer a target from a branch name alone.

## Project evidence

Look for present roots and referenced children; absence is a finding, not automatically a defect:

```text
docs/dev/PROJECT.md
docs/dev/ARCHITECTURE.md   docs/dev/architecture/
docs/dev/DECOMPOSITION.md  docs/dev/decomposition/
docs/dev/SPEC.md           docs/dev/spec/
docs/dev/PLAN.md           docs/dev/plan/
docs/dev/TASKS.md          docs/dev/tasks/
docs/dev/layout.md         docs/dev/layout/
docs/dev/FEATURE_ARCHITECTURE.md
docs/dev/FEATURE_DECOMPOSITION.md
docs/dev/FEATURE-SPEC.md  docs/dev/FEATURE-PLAN.md
docs/dev/FEATURE-TASKS.md
docs/dev/verification-map.json
```

Inspect relevant reviews/features package navigation for branch identity and source disposition. Archived feature documents and historical task snapshots under docs/dev/features are retained evidence, not active FEATURE-TASKS; discover active ownership from main TASKS and explicitly active root sources. Observe partially moved paths/links as unfinished incorporation, without repairing them. Inspect the workflow-specific report prefix and retained review/report commits, pending publication and issue/milestone reconciliation facts when available. Distinguish unfinished review, committed report awaiting push, closed milestone awaiting local parent persistence, and completed phase review awaiting integration. Unknown hosted effects remain unknown until provider readback; orientation observes and hands off rather than replaying writes.

Also identify project-specific equivalents and other execution evidence when present. Do not modify or restore such state during orientation. Feature documents describe an intended delta; FEATURE-TASKS holds only scoped feature work and is not the complete task baseline. Inspect it with TASKS when establishing active work and progress.

Inspect relevant source, tests, manifests, and declared commands for building, focused checks, integration checks, documentation checks, and packaging. Note unavailable tools without installing dependencies or executing commands with side effects. Use project instructions over guessed defaults.

## Task state at startup

When TASKS or an active FEATURE-TASKS exists, establish the implementation starting point:

1. Find the latest completed task identified by a task commit and inspect its committed checklist and result. Later maintenance, steering-amendment, or boundary-merge commits do not independently advance that task boundary. Trace completed task commits through merge parents rather than interpreting aggregate task IDs in a merge message as newly completed tasks. If no task has been committed, use the established preimplementation commit as the baseline.
   Inspect owning entries and linked evidence for **Completion reassessment pending** notes. Report the affected IDs, changed acceptance, authoritative sources, and historical evidence as disputed completion, even when the tree is clean and boxes remain checked. Do not change status or clear notes during orientation.
2. Compare the committed boundary with the owning working checklist and staged, unstaged, and untracked changes. If the last checked task is ahead of the last committed task, identify it as completed work awaiting commit; confirm that pending changes belong to it and existing completion evidence is present. Otherwise identify the current incomplete task from the selected execution order and changes since the boundary. Future unchecked tasks do not identify the interrupted task. If the tree is clean and the checklist agrees with the committed boundary, report no pending task changes.
3. Include the task ID, owning list, last task commit, pending paths and ownership, existing verification evidence, and remaining work or ambiguity in the handoff to **sdd-implement**. It owns verification, completion, commits, pushes, and issue-closure coordination. Orientation observes existing evidence; it does not repeat implementation or run verification.

Report ambiguous task identity, change ownership, or missing completion evidence without guessing. Git and the owning task list provide startup state; no separate transaction journal is required.

## Interrupted document operations

When changes belong to feature-document incorporation or a steering amendment, report that workflow separately from interrupted task execution. Inspect selected sources/owners and their checkpoint diff, existing scope evidence, unfinished reconciliation, and branch/merge state. Preserve task history and unresolved identities; do not assign a document-only operation to the next unchecked task. Route facts to **sdd-manage** and its active owner; orientation does not reconcile files or execute checks.

## Orientation report

Produce a concise human-readable handoff with these slots, using `none`, `unknown`, or `not inspected` distinctly:

```text
Target: project root; Git root; contemplated paths or workflow
Git: worktree eligibility; branch/detached/unborn; HEAD; relevant status and ownership; working/target branches, checkpoint, and merge/publication state
Instructions: applicable sources, scope, and conflicts
Documents: main roots and relevant children; active feature/change documents
Execution evidence: owning TASKS or FEATURE-TASKS; last committed task and commit; current task and status; pending changes; existing verification evidence; remaining work or ambiguity
Tooling: relevant declared commands and environment limitations
Readiness: read-only possible; repository mutation eligible or blocked; reasons
Handoff: scoped facts for the next skill; unknowns and checks to repeat
```

This report is an observation at a particular repository state, not a lasting certificate or permission to mutate. Attribute factual claims to paths or Git output when the distinction matters. Do not invent completion states from checkboxes, timestamps, or file presence alone. The orchestrator must recheck stale facts and retain responsibility for authorization, workflow selection, and final validation.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-specify/references/review.md

SHA-256: `60ef1b66449b4f40adf88f475fa4767cfd663d17ba4cd304236e8dfcb79500c9`

```text
# Specification review

For a review-only request, read the relevant SPEC root and children, accepted design, and any active change specification. Assess completeness, clarity, ownership, objective acceptance, and consistency without editing governing documents. State concrete findings and their consequences; do not demand invented detail where the project intentionally delegates a decision.

Check the canonical behavioral owner, relevant structural owner links, and affected consumers using [design traceability](system-specification.md#design-traceability). Ensure cross-component guarantees identify participating boundaries and design/contract conflicts are surfaced for accepted decisions. Recheck parent-child routing, public contracts, errors, formats, compatibility, and end-to-end acceptance. Compare with PROJECT, ARCHITECTURE, and DECOMPOSITION; report needed decisions to their owners. Identify impacts on PLAN, TASKS, any active FEATURE-TASKS, tests, and user documentation. A direct correction belongs to the owning SPEC node under [system specification](system-specification.md); incorporating an accepted feature delta into main documents belongs to **sdd-integrate-feature**.

## End-state language

Write the main SPEC and its children as direct descriptions of the complete intended system. Do not turn an incorporated change into an amendment or a story about prior versions. Replace transition wording such as “previously,” “formerly,” “now supports,” “newly added,” “was changed to,” “no longer,” and “this revision replaces” when it describes the document's editing history. For example, write “Encrypted archives are rejected” instead of “Encrypted archives are no longer supported.” Apply the same check to headings, rationale, acceptance conditions, and linked children.

An active feature specification may describe the baseline and proposed delta. A genuine compatibility contract may name earlier released versions or formats, but express their currently required treatment as a present guarantee. Historical steps belong in Git history, not in the main SPEC. This is an editorial check on meaning, not a ban on individual words that have a legitimate role in a requirement.

A review does not authorize document edits, code changes, or implementation of a newly specified capability.

## Required SPEC/design QC gate

Apply **sdd-conventions**' **Development-document QC** criteria. Review the selected SPEC root and applicable children against accepted PROJECT, ARCHITECTURE and DECOMPOSITION (feature deltas against their accepted main/feature inputs). Identify exact reviewed/governing states and group contract-to-design coverage using existing IDs/links. Check outcomes/non-goals, responsibility/interface/dependency consistency, unsupported structural assumptions, success/error/resource/lifecycle obligations, objective acceptance and parent-child coherence. Missing or contradictory significant obligations block dependent PLAN authoring.

When authoring or correction is authorized, fix bounded SPEC issues through its owning node and recheck. A needed design or behavioral decision goes to its actual owner; do not reshape design to make a deficient contract look consistent. Pure review leaves governing files untouched and returns findings; write a review report only when requested or included in authoring scope.

Use **sdd-report**'s **Document QC reports** reference to place `SPEC-REVIEW-REPORT.md` beside SPEC (or `FEATURE-SPEC-REVIEW-REPORT.md` beside FEATURE-SPEC). Cover children in that root report. Retain located original findings, append each Revision N correction/recheck, and report Ready only for the currently reviewed scope with all confirmed issues resolved. Persist corrected documents and report together through sdd-manage. Reuse current equivalent review evidence; report affected downstream invalidation. Do not proceed to PLAN merely because SPEC exists.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-specify/references/change-specification.md

SHA-256: `74ad9a214189fa094c48acfd6c1daacb4eef43fe64ea18946ff5e6628a3be94c`

```text
# Scoped change specification

Use `docs/dev/FEATURE-SPEC.md` when an additive, corrective, subtractive, or compatibility-sensitive change needs a reviewable behavioral delta before it is integrated into the complete system specification. A small unambiguous correction may instead revise the owning main SPEC node directly when that is the requested scope.

Define:

1. the change objective, affected users and existing SPEC nodes, and whether the work adds, alters, or removes behavior;
2. the final supported behavior and explicit unsupported boundaries or non-goals;
3. changed public and internal contracts, errors, data and persistent formats, compatibility, and transition requirements where material;
4. dependencies and effects on completed consumers, including a required rejection behavior when a capability is removed;
5. acceptance conditions for the changed behavior and affected cross-component guarantees;
6. unresolved decisions whose answer would alter the contract, without pretending they are settled.

Reference unaffected main SPEC nodes rather than copying them. If the change alters structural boundaries, align with applicable FEATURE_ARCHITECTURE or FEATURE_DECOMPOSITION decisions; those documents are needed only when their level actually changes. Treat implementation evidence as observed state, not automatic approval of a new requirement.

The feature document describes an intended delta while active. Say explicitly which main requirement it revises; if it conflicts without declaring a change, resolve the conflict before authoring further. It does not contain implementation tasks or chronological migration notes. Use **sdd-integrate-feature** to incorporate settled final behavior into the main SPEC when requested.

## Review the scoped delta

Apply [SPEC/design QC](review.md#required-specdesign-qc-gate) to the selected delta and affected interfaces against accepted main/feature sources. Produce the adjacent FEATURE-SPEC review report and resolve confirmed issues before dependent feature planning. Do not force a complete main-document rewrite or incorporate the delta implicitly. Absent feature design overlays can be replaced by demonstrably sufficient accepted main design.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-specify/references/system-specification.md

SHA-256: `4af4ac610c2e6b020c57182e486d55124142394f9ba341db0b81339404723afd`

```text
# Complete system specification

`docs/dev/SPEC.md` and its focused children define the complete intended current system. A reader should be able to understand required outcomes without conversation history, a change document, or implementation logs. For a new project, describe the system that is to be built from scratch; for an existing project, distinguish verified behavior from intended corrections and do not fill evidentiary gaps by guessing.

## Root

Keep `SPEC.md` compact but substantive. Include the relevant:

- purpose and intended outcomes, principal users and system context, scope and non-goals;
- terminology and guarantees used across components;
- short orientation to the architectural blocks and permitted interactions, linking to design documents for structural detail;
- system-wide public, cross-component, data, lifecycle, compatibility, and error contracts;
- mapping to focused child specifications, if any;
- objective end-to-end acceptance conditions, including important boundaries and failures.

PROJECT owns the fuller project brief; ARCHITECTURE and DECOMPOSITION own the structural rationale. Include only the structural facts needed to make behavior intelligible. Do not copy design documents into SPEC or reduce its root to a table of contents.

## Design traceability

SPEC defines the observable guarantees the selected structure must satisfy. Link relevant contracts to responsible components in DECOMPOSITION and, where consequential, their consumers and architectural constraints. Cross-component guarantees have a canonical behavioral owner with links to participating boundaries; do not repeat the contract in every component description or require one specification per component.

Design supplies responsibility, dependency, extension, and verification seams; SPEC settles precise success/failure behavior and acceptance. Feedback is bidirectional: a contract can reveal an inadequate structural boundary, and design analysis can reveal an unresolved behavioral obligation. Surface the conflict to its requirement or design owner and resolve the accepted decision before dependent work. Do not silently redesign in SPEC, invent a requirement to fit the structure, or introduce a separate mapping artifact solely for traceability.

## Focused children

When distinct contracts have substantial independent detail, place them under `docs/dev/spec/` with stable semantic names. Split by cohesive behavior, component contract, public interface, external protocol, or persistent representation, rather than implementation phase or arbitrary requirement codes. Define each child's scope and relationship in its parent. The child owns detailed requirements; the root retains only the broader system guarantee and route to the child.

At the appropriate owner, define required successful behavior, inputs and outputs, invariants, rejection and error semantics, boundary cases, state and lifecycle, resource ownership, data formats, compatibility, and nonfunctional guarantees when those materially affect correct use. Specify externally observable outcomes and constraints, not an internal algorithm unless the algorithm itself is part of the accepted contract.

## Acceptance and review

Write acceptance conditions that can be assessed objectively: meaningful success cases, failures, edge cases, and interactions. A test command or an implementation task is not a behavioral requirement. Avoid prescribing redundant tests at every layer; verification planning owns check selection and execution.

Confirm every accepted requirement has one canonical owner, all parent/child links resolve, contracts are mutually consistent, and important behavior can be checked. Label intentionally deferred decisions and their limits. A missing choice that would force SPEC to invent public behavior is a blocker, not a license to complete the prose by assumption.

Read the main SPEC and affected children as a standalone end-state contract. Remove wording that narrates what an earlier draft or implementation did; express accepted behavior directly. Apply the detailed editorial check in [review](review.md).

## Finish the preparation boundary

Authoring includes the required SPEC/design QC gate in [review](review.md). Correct in-scope issues, resolve consequential decisions with their owners, recheck and produce the adjacent root review report before dependent PLAN authoring. A draft specification or report is not Ready. Complete the requested specification boundary without automatically starting planning.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-implement/references/range-selection.md

SHA-256: `092f930702c80eccaee732c252c1c68bbfaeaa8be78386b5f688d1509274a5e9`

```text
# Range selection

Resolve a human request against TASKS and any active FEATURE-TASKS before implementation starts. For an explicit feature request, select from FEATURE-TASKS and check external prerequisites in TASKS; for an explicit main-project request, use TASKS. If both contain eligible work and an unqualified “next” has no clear active scope, report the ambiguity instead of mixing the lists or choosing silently. Read the relevant PLAN or FEATURE-PLAN exits, dependency notes, and the current Git and worktree evidence from orientation. A checked item in either list alone does not establish completion; review task evidence if status is disputed or stale, obtaining **sdd-tasks** progress review when needed, and route feature-delta reconciliation to **sdd-integrate-feature**; direct checkpoint amendments require a human command to **sdd-steer**. Resolve interrupted or ambiguous task state using the **sdd-orient** handoff before selecting new work.

Inspect **Completion reassessment pending** notes in owning entries or linked evidence. Treat affected checked tasks and parents as disputed, assess their current acceptance and dependency consequences, and include in-scope reassessment in the requested range rather than skipping it because every box is checked. Report an out-of-range reassessment as a scope conflict. Selection-only reports these facts without running checks, correcting status, or clearing notes.

1. Identify the applicable task list and requested unit: one named task, the next eligible task, the next N eligible tasks, a named milestone, the next milestone, a named phase, or the next phase. Count explicit milestone/phase review/report tasks as tasks too; do not skip them or append out-of-range review work. Count **tasks** only for “N tasks”; count phase or milestone units only when the request names that unit. Resolve “next” from verified completion and dependency order, not from the first unchecked box alone.
2. Expand the request to precise task IDs and enclosing milestone or phase. Use globally unique IDs for dependencies across lists; check prerequisites and identify any blocked or out-of-range dependency. Do not silently expand the authorized range; report the dependency and obtain its resolution through the appropriate workflow.
3. State the selected IDs, prerequisite evidence, expected end condition, and the stopping boundary. An implementation agent must stop at that boundary for human review, even if subsequent tasks are ready. If no eligible work remains, report why without inventing work.

A selection-only request is read-only and stops after reporting the range. It does not enter the push-first execution protocol. Selection within an implementation request follows startup pushing and interrupted-task handling. It does not mark tasks done, run checks, create a commit, or authorize the implementation workflow. A user may explicitly select a different valid order; document the dependency consequences instead of silently replacing their range.

## Phase branch segments

For main TASKS, identify the owning phase of each selected task and its full exit obligations. Execute a partial range on that phase branch and stop after persistence without integrating an unfinished phase. Split an authorized range spanning phases into sequential phase segments; complete/verify/publish each phase before starting the next branch. If the request excludes remaining work or evidence needed for the phase exit, report the blocker or pause rather than expanding the selected IDs. Selection-only identifies these boundaries without branch changes.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-plan/references/review.md

SHA-256: `3500dd799e477807deee44e9e4a436626f22b8ce8bf91f1c7b8d3e1aa065c931`

```text
# Plan and layout review

For read-only review, inspect the relevant PLAN root and children, layout, accepted design and SPEC, active feature plan if any, and the current repository tree where placement matters. Check that phase and milestone exits are objective, dependencies and integration points are feasible, every significant contract has a delivery route, and physical ownership supports the logical boundaries. Report concrete gaps and conflicting authorities without editing governing documents.

Check that the earliest usable milestone is a minimal meaningful end-to-end slice, its inclusions/deferrals and acceptance are explicit, and each delaying prerequisite is justified. Check subsequent capability increments are behaviorally bounded, retain the working path, and include timely integration/regression evidence rather than postponing it to a final phase. A skeleton or mocked-only demonstration is insufficient by itself. At suitable milestones, check demonstrable functionality, relevant usability/risk evidence, and the consequential human decision being informed; distinguish technical exits from product/usefulness decisions.

Check that strategy belongs in PLAN, physical ownership in layout, behavior in SPEC, and executable units and status in TASKS or active FEATURE-TASKS. Check alignment with PROJECT, ARCHITECTURE, DECOMPOSITION, and SPEC. Review parent-child links and component-to-path routing in both directions, including tests, documentation, and integration. Read the main PLAN and layout nodes as standalone end-state descriptions without editing-history language; genuine compatibility and transition obligations may refer to an earlier released state.

Report concrete gaps and affected task-list dependencies. Direct corrections belong to [delivery plan](delivery-plan.md) or [physical layout](physical-layout.md); incorporation of accepted feature documents belongs to **sdd-integrate-feature**. A review does not authorize edits, task execution, or progression into another workflow.

## Required PLAN/SPEC QC gate

Apply **sdd-conventions**' **Development-document QC**. Establish current SPEC/design QC evidence for the accepted inputs; a material unresolved specification issue blocks dependent planning. Map every significant accepted contract and end-to-end obligation to a planned delivery route, including honest deferrals, failures, dependencies and objective exits. Identify omissions, duplication, invented features and scope drift. Verify that layout supports the accepted structure and planned integration; a layout-only review reports its affected PLAN implications without authorizing PLAN edits.

For each phase, report delivery milestone count separately from its final dedicated phase review milestone. Apply shared 3–5 guidance, explicit 1–2 fragmentation and 10+ overload/drift assessments, departure rationale and empty-group rules. Inspect semantic scope even for in-range groups: contract/component breadth, delayed usefulness, dependency chains, integration/testing effort and boundary overhead. Keep justified narrow phases; add no padding or quota-driven splits. Dedicated milestone review outcomes remain required even though excluded from delivery counts.

Authoring includes authorized bounded PLAN/layout correction, recheck and `PLAN-REVIEW-REPORT.md` adjacent to PLAN (FEATURE-PLAN counterpart beside its root); the report covers applicable children and relevant layout. Use sdd-report's **Document QC reports** format and append Revision N cycles. Route changed behavioral/design decisions upstream; never rewrite SPEC to fit PLAN. Persist the corrected strategy and review together before TASKS generation. Pure review does not amend strategy. Missing/stale evidence or confirmed unresolved issues blocks dependent generation; explicit exceptions remain recorded as exceptions, not Ready.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-plan/references/delivery-plan.md

SHA-256: `b757fd076dc35d419a85c64fe7ea1e38c2fa78c493b5c2b19b094cf7f5b8416a`

```text
# Delivery plan

`docs/dev/PLAN.md` defines a coherent strategy to deliver the complete intended system. It describes phases and meaningful milestones, dependency order, integration approach, major risks and decision gates, and evidence required at phase and milestone exits. Keep it substantive enough that TASKS can derive bounded executable work without inventing delivery strategy. It is not a record of completed work.

## Establish the strategy

1. Map the accepted architecture and decomposition to the behavioral contracts and end-to-end acceptance in SPEC. Identify critical dependencies and the points where components must integrate.
2. Default to the simplest practical meaningful end-to-end MVP or prototype as the earliest usable milestone. State included and deferred capability/contract scope, observable usefulness, relevant acceptance, and minimum necessary dependencies. For an existing system, preserve its useful baseline and identify the earliest meaningful changed path. Justify prerequisites that delay this outcome, such as unavoidable infrastructure, characterization, compatibility/migration, or a risk probe; name their evidence and route to integrated behavior. A technical skeleton or mocked-only path does not by itself establish useful functionality.
3. Define phases around major delivery outcomes and milestones around reviewable, verifiable stopping points. For each, state scope, outputs or capabilities, prerequisites, and objective exit evidence. At suitable early and subsequent milestones, state what working capability can be demonstrated, what functional/usability feedback or risk evidence is needed, and which consequential human decision it informs: continue, amend, simplify, or stop. Do not require usability trials at every task or authorize automatic steering/stopping; routine progression already authorized by the request needs no additional approval. Include important failure and integration checks where they establish readiness, without prescribing a test case for every requirement.
4. Identify cross-cutting verification, documentation, packaging, and release work at the level required for the strategy. State risks, assumptions, unresolved decisions, and their gates without treating guesses as accepted requirements.
5. Check that every intended capability has a plausible delivery path and that the plan can be executed in bounded units later. Do not enumerate file edits, task IDs, commit transactions, or a per-test command sequence; TASKS owns that detail.

## Review boundaries

Apply the [backend object lifecycle](../../sdd-conventions/references/backend-object-lifecycle.md). Reserve one final phase review milestone with a single phase review/testing/report outcome. Every preceding delivery milestone includes its own final milestone review/testing/report outcome. Define code review, focused testing/regressions, blocker repair and committed report evidence as exits. The phase review starts after all delivery milestones complete/close; its own milestone closes afterward. PLAN owns these boundaries; TASKS assigns executable task IDs. Include final TODO aggregation when the last phase completes the full task list.

## Incremental growth

- **Bound behavior:** Evolve the usable path through the smallest meaningful capability increments that can be integrated, reviewed, and robustly checked. State affected contracts, dependencies, and acceptance; small file scope alone does not establish a small functional change.
- **Establish checks early:** Plan rigorous relevant end-to-end, regression, failure, and integration coverage alongside the initial slice and each increment. Preserve previously working behavior and resolve required failures before dependent functionality grows.
- **Respect ownership:** PLAN defines capability increments and verification dependencies; TASKS derives bounded work within them. **sdd-tdd** owns detailed testing strategy, **sdd-verify** assesses checks/evidence, and **sdd-implement** owns execution, repairs, and completion.
- **Retain full intent:** Main design and SPEC describe the complete intended system. MVP deferrals select implementation scope without silently relaxing applicable acceptance or deleting intended requirements. Required extensibility/load constraints guide staged realization; anticipated generalizations do not automatically become MVP prerequisites.

Choose an order that reduces integration uncertainty and makes failures easier to localize. Explain consequential interface, format, migration, and dependency choices; do not promise globally optimal delivery speed or guaranteed correctness from incremental development.

## Document organization

Keep the root compact but substantive: system delivery objective, strategic approach, phase and milestone map, key dependencies, integration and verification gates, and links to focused children. Put independently substantial phase or area detail under `docs/dev/plan/`, with stable semantic names and an explicit scope link from the root. Split by coherent delivery concern, not a file per task. A child refines its parent's strategy without duplicating or contradicting its guarantees.

For a scoped change, `docs/dev/FEATURE-PLAN.md` may define affected phases or milestones, dependency and rollout effects, compatibility or transition work, and exit evidence for the proposed delta. Use it when the change needs a reviewable delivery strategy; do not require it for every correction. Name the main plan decisions it affects, reference unchanged strategy instead of copying it, and use **sdd-integrate-feature** to incorporate accepted final strategy into the main PLAN when requested. Main PLAN and its children read as the intended complete delivery strategy, not a series of amendments. For an active feature workflow, FEATURE-PLAN supplies phase and milestone boundaries and exit checks to FEATURE-TASKS when a scoped delivery plan is needed. TASKS retains the complete project hierarchy until feature tasks are reconciled; existing parents keep their project-wide meaning.

The plan can mention paths only when a path is a fixed project constraint or required external artifact. Defer allocation of source and test paths to `layout.md`; let TASKS derive concrete edit scopes from both. When producing both artifacts, establish strategic boundaries first, assign physical ownership, then recheck that the proposed layout supports the planned increments and integration points.

## Preparation readiness

Before dependent planning, require current SPEC/design QC for the inputs; obtain focused missing assessment through sdd-manage within authorized scope. Finish authoring with the [PLAN/SPEC QC gate](review.md#required-planspec-qc-gate), including delivery counts, semantic scope, corrections/recheck and an adjacent report. TASKS derives only from current reviewed strategy/layout. Do not start TASKS merely because a plan draft is complete.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-design/references/architecture.md

SHA-256: `329327e9cadf2637289dcad8808faa0a31c7e386223accb91366b897ef64339b`

```text
# Architecture

Define the system's high-level arrangement and why it fits the project's purpose. Read accepted exploration decisions and relevant existing project evidence. Apply the shared **sdd-conventions** modularity checks to major boundaries. Use [decomposition](decomposition.md) when responsibility analysis reaches detailed components.

## Document ownership

- `docs/dev/PROJECT.md` is the concise brief: purpose, users, principal outcomes, scope and non-goals, constraints, and terms needed to orient a reader. It is not an operating-instructions file. If an existing copy contains instructions, preserve their authority and resolve its intended role before replacing content.
- `docs/dev/ARCHITECTURE.md` is a compact but substantive design entry point: a short orientation back to the brief; major blocks and their responsibilities; dependency direction and cross-block interactions; relevant external systems and data ownership; selected patterns, design principles, and consequential tradeoffs; system-wide architectural invariants; and a map of focused children when present.
- Focused children under `docs/dev/architecture/` may own a substantial architectural area. The root defines their scopes and system-wide relationships; each child adds detail within its area. Split for independent responsibility and navigability, not a fixed size or one child per task.

Keep project-specific links in ARCHITECTURE limited to useful navigation. Put detailed logical component responsibilities and collaboration in DECOMPOSITION, exact observable behavior and acceptance in SPEC, physical placement in layout, and delivery order in PLAN. Use the [document boundaries](../SKILL.md#document-boundaries) comparison to route shared interface, ownership, and invariant concerns by granularity. Record a design choice and its reason where that reason is needed to understand a durable constraint; avoid a chronological decision log in the current-state architecture.

## Initial and existing systems

For a new system, establish its intended blocks and dependency direction before expanding detailed components. For an existing system, inspect the relevant actual code and contracts; distinguish observed architecture from the intended change. Do not claim an inferred or proposed capability is already implemented. If the task is adoption of project-wide documents, describe the intended whole within the evidence available and surface gaps.

For a material architectural change, `docs/dev/FEATURE_ARCHITECTURE.md` may define the feature or revision's objective and scope, affected baseline blocks, proposed final arrangement, dependency or compatibility effects, and explicit non-goals. It is a scoped delta; unchanged architecture remains owned by the main document. Do not require this overlay for every feature or correction.

## Review

Check that every major responsibility has one owner, important interactions and dependencies are legible, architectural constraints support the desired outcomes, and remaining unknowns are explicit. Confirm PROJECT and ARCHITECTURE do not repeat one another and that any child scope is navigable from the root. Stop at architecture when the user requested only architecture; a sound architecture is not permission to author SPEC or start implementation.

Read PROJECT, the main ARCHITECTURE, and affected children as descriptions of the intended end state. Remove narration of earlier drafts or implementations, including “formerly,” “now,” or “replaces” when those words describe an editing transition. State the settled arrangement directly; keep genuine compatibility constraints as present design constraints. A feature overlay may describe its proposed delta until **sdd-integrate-feature** incorporates the accepted change.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-design/references/decomposition.md

SHA-256: `eac648372c44883068569a13a2715cb7d7b4d84e26f7c4de20478f93bb124abf`

```text
# Decomposition

Refine accepted architecture into understandable component responsibilities and collaboration. ARCHITECTURE owns the major arrangement and consequential rationale; DECOMPOSITION owns logical units within it. Use the [document boundaries](../SKILL.md#document-boundaries) comparison when routing overlapping structural concerns. Read only the relevant architecture root and children, existing code or contracts where applicable, and the shared **sdd-conventions** modularity reference. Revisit architecture when decomposition reveals a weak block boundary rather than hiding the conflict in detail.

## Document ownership

`docs/dev/DECOMPOSITION.md` is the compact entry point for the logical component model. Identify principal components within each architectural block, their responsibility and non-responsibility, provided and required interfaces at the level needed to assess the design, dependency direction, data or state ownership, lifecycle and failure boundaries when architectural, and relevant verification seams. Give each child document a precise scope and link to it from the root.

Focused children under `docs/dev/decomposition/` may detail a component or coherent area: subcomponents, collaboration, important invariants and design-level interface shape, and how it relates to its parent and peers. A parent defines relationships and shared constraints; a child owns detail. Split only when independent detail justifies it. Avoid duplicating the same normative interface in parent and child.

Interfaces here may be provisional enough to test the architecture for coherence. Link the relevant SPEC owners and consumers when established; a cross-component guarantee can span several structural units without being copied into each. Feed incompatible obligations back to the affected design or requirement owner for an accepted decision. Identify contract details that SPEC must settle; do not present undecided errors, formats, or behavior as final requirements. Do not turn component descriptions into a file inventory, implementation order, or task checklist.

## Existing systems and changes

Inspect actual component boundaries and dependents before proposing changes. `docs/dev/FEATURE_DECOMPOSITION.md` may describe only affected units, altered collaborations and interface boundaries, compatibility needs, and component impact for a scoped architectural revision. Reference unchanged main nodes rather than copying them. It may accompany FEATURE_ARCHITECTURE when both levels change; neither is obligatory for a change that does not affect its level.

Main architecture and decomposition describe the coherent intended system after accepted decisions are incorporated. Feature documents serve the proposed delta until **sdd-integrate-feature** incorporates the accepted change into the main documents. Do not leave both contradictory descriptions as current truth.

## Review

For each unit, answer what it does, how it is used, what it depends on, and how its boundary can be checked without inspecting its internals. Inspect dependency cycles and unclear ownership; prefer a focused contract or a genuine combined unit to artificial layers. Check that a later SPEC could define objective behavior for each affected boundary, and that planned implementation could proceed in localized, verifiable changes. Report unresolved design decisions rather than inventing final contracts.

Read the main DECOMPOSITION and affected children as the intended component model. Remove narration of prior drafts or implementations after incorporating a feature; describe each settled boundary and responsibility directly. A feature overlay may describe the proposed change while it is active.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-conventions/references/task-hierarchy.md

SHA-256: `675d67a8a7487c7876e084276638a966072d177f56376d3c156eec29c9b90a75`

```text
# Phase, milestone, and task hierarchy

Use one Phase → Milestone → Task hierarchy. Each task has exactly one parent milestone, and each milestone has exactly one parent phase. `docs/dev/TASKS.md` holds the complete intended hierarchy. An active `docs/dev/FEATURE-TASKS.md` may hold its feature's scoped delta, using the same three-level form and project-wide unique task IDs. Reused phase and milestone IDs and names match the main hierarchy; new groups follow the accepted feature plan. In either list, phase heading and checkbox agree. PLAN or active FEATURE-PLAN defines strategic outcomes and exit conditions, and the owning task list supplies host-facing names.

Keep IDs stable across both lists and feature reconciliation. A host projection uses the project-wide task ID to recognize an object and reconciles its name when the owning list changes. Resolve duplicate task IDs across lists, mismatched parent identities, phase headings and checkboxes, or ambiguous parentage before publishing. Task completion remains evidence-backed in its owning list; a host object's state is not completion authority.

## Delivery and decision boundaries

Phases express major delivery or risk outcomes; milestones expose meaningful integrated capabilities and suitable exit evidence; tasks supply bounded executable work within them. PLAN defines the early meaningful end-to-end MVP, subsequent small capability increments, and appropriate functional/usability decision gates. Module-sized tasks alone do not establish incremental functionality, and a task need not independently produce user-visible value.

At consequential milestones, identify the demonstration or feedback that informs a human decision to continue, amend, simplify, or stop. Keep these decisions with the human; the hierarchy does not authorize automatic steering, stopping, or task-list continuation. Stable identities, parentage, and completion evidence remain governed by the owning lists and execution workflow.

Apply [backend object lifecycle](backend-object-lifecycle.md) for mandatory delivery review tasks, the final single-task phase review milestone, completion gates and report placement. PLAN reserves those milestones/exits; TASKS derives their tasks.

## Hosted projection

When the selected backend supports issues, as GitHub does, create an associated issue for every task of the eligible phase in TASKS or the active FEATURE-TASKS being projected; never duplicate an issue for the same project task ID. Represent each phase with a phase label and create a host milestone for each SDD milestone when supported; use a milestone label only when a backend defines equivalent completion/reconciliation semantics; otherwise report milestone lifecycle unsupported. Assign each task issue its phase label and its parent milestone or milestone label when creating it. After the task is implemented, verified, committed, and reconciled in its owning task list, close its issue as completed. A feature parent checkbox does not establish completion of the whole-project phase or milestone.

The active backend owns object creation, lookup, and reconciliation. It may define equivalent host objects while preserving the phase → milestone → task relationships and issue lifecycle.

For the GitHub backend, use these names from the task's owning list:

| Host object | Title or name |
| --- | --- |
| Phase label | `sdd-phase-2-Archive-streams` |
| Milestone | `sdd-2.2-ZIP-support` |
| Task issue | `[T-012] Implement ZIP stream support` |

If a host has no native milestones, an equivalent milestone label may be named `sdd-milestone-2.2-ZIP-support`. Replace example IDs and words with the actual ID and name in the owning task list. For labels and milestone titles, trim the name and replace whitespace with hyphens while preserving meaningful case and acronyms; normalize other host-incompatible characters deterministically. The stable ID distinguishes objects even when their names change. Give labels brief descriptions of their phase or milestone scope; use the backend's available metadata for milestone outcomes and exit conditions.

```

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/plugin/skills/sdd-conventions/references/backend-object-lifecycle.md

SHA-256: `8729f0f62f649509080018ebf43aa2f5e7f710939ed182494460c23a0d9a0685`

```text
# Backend object lifecycle and review boundaries

Apply these shared invariants to PLAN/TASKS generation, bounded implementation, hosted reconciliation and interruption recovery. Local governing documents and verified Git/check evidence are authoritative; backend objects are projections. Hosting is optional. sdd-manage coordinates transitions; sdd-implement executes tasks and persists results; sdd-forge owns provider writes.

## Phase activation

Keep the complete intended hierarchy in local PLAN/TASKS. Create a phase's label, all its milestones and all its task issues only after its predecessor is complete and before its first task executes. First-phase activation has no predecessor. Completion includes the predecessor's reviews, required reports, all milestone closures when tracking is active, local exits and required target integration/publication. Starting the next phase also requires authorization within the selected range.

Preparation does not activate a phase. Projection reads the complete hierarchy to resolve identity/dependencies but writes only the eligible phase. Added work in an already active phase is projected before execution. Future-phase work remains unprojected, including feature deltas. When tracking is enabled, incomplete or unverified phase projection blocks the first task unless the human explicitly authorizes local-only continuation. Preserve existing future-phase objects as historical/pre-existing state; report them rather than deleting them to enforce timing retrospectively.

## Explicit review units

Each phase has one or more delivery milestones followed by a dedicated phase review milestone containing exactly one phase code review/testing/report task. Each delivery milestone ends with its own milestone code review/testing/report task, including the last delivery milestone. The final phase review milestone has no additional milestone review task.

PLAN owns these milestones and exits; sdd-tasks derives executable review tasks with stable IDs, prerequisites, scope and evidence. Review tasks count toward selected next-N ranges. The phase review depends on all **delivery** milestones being complete/closed, not its own still-open milestone. Accepted existing hierarchies require a scoped amendment; never insert or renumber tasks implicitly during execution.

## Completion ordering

1. Verify task acceptance, tests and documentation; reconcile its owning checklist/evidence; commit result and status together, push and verify containment. Then close its task issue with evidence when tracking is active. A task issue records work on its working branch; target integration is separate.
2. Execute a delivery milestone's final review task after preceding delivery tasks complete. Review the whole capability and relevant dependencies, test applicable exits/regressions, fix blockers and commit/push its report. Close this review task's issue like any other task.
3. Close/read back the delivery milestone only after every constituent issue, including the review issue, is closed and its review/report/exit evidence is established. Unexpected open or foreign issues and ambiguous ownership block closure; never close foreign issues to clear the gate.
4. After all delivery milestones close, execute the phase review task: review cross-milestone interactions, phase exits and remaining findings, run required checks, repair blockers, commit/push the phase report and close its issue. Then close/read back the final review milestone.
5. Reconcile local parent claims, verify the full phase and perform required explicit integration, merged-state verification and publication before activating an authorized next phase. A partial range pushes and pauses without inventing additional review work beyond its selected tasks.

Local-only execution applies the same review/report/exit gates without hosted closure. If an enabled backend cannot complete closure, keep local verified results and report hosted reconciliation pending; dependent phase review/advancement remains blocked. Independent tasks in an already activated phase may continue within scope when dependencies permit. A phase label has no close state on GitHub: retain its historical associations. Unsupported backend state transitions need an explicit backend procedure, not deletion or an invented equivalent.

## Review, repairs and deferral

sdd-verify owns read-only implementation code review and check evidence for milestone/phase boundaries, with focused specialists routed by sdd-manage as needed. sdd-implement owns repairs and completion; sdd-tdd designs/changes tests; sdd-docs maintains documentation; sdd-report presents evidence. Code review and testing are separate obligations. Passing tests without code review cannot complete a review task.

Fix bugs, critical code issues and every SPEC/PLAN violation before completing a review task. Missing or failing required evidence blocks completion. Route governing-contract or out-of-scope changes to their owner; do not disguise them as deferrable findings. Only non-critical code issues consistent with SPEC/PLAN may be postponed.

Keep required repairs and findings whose deferral eligibility is unestablished in Findings/Blockers, outside the deferred TODO section. Each report has a TODO section (`None` when empty). A deferred finding has a stable ID, location/evidence, impact/severity, deferral rationale showing contracts/exits remain satisfied, proposed solution options/tradeoffs and follow-up owner/scope. Phase reports carry unresolved milestone findings and add phase findings. The final implementation report aggregates unresolved/deferred milestone and phase TODOs without losing options or provenance; preserve resolution references for earlier findings. The last phase review task includes the final report when the full task list completes. Partial requests cannot claim full-project completion.

## Report locations

| Workflow / artifact | Path or prefix |
| --- | --- |
| Main/greenfield phase report | `docs/dev/reports/phases/<phase-id>/PHASE-REPORT.md` |
| Main/greenfield milestone report | `docs/dev/reports/phases/<phase-id>/<milestone-id>.md` |
| Main/greenfield final report | `docs/dev/reports/IMPLEMENTATION-REPORT.md` |
| Phase-checkpoint steering revision records | `docs/dev/reports/phases/<phase-id>/revisions/<revision-id>/` |
| Feature reports and records | `docs/dev/features/<feature-id>/` |

Use filesystem-safe stable IDs; link reports from owning review tasks. Steering retains applicable review/revision stage basenames including `REVISION-REPORT.md` within its phase-specific prefix, instead of the general reviews directory. General campaigns retain [review campaign](review-campaigns.md) storage. Feature milestone/phase reports remain under their feature prefix; qualify paths by phase ID when multiple phases would collide, and place the feature's final `IMPLEMENTATION-REPORT.md` at that prefix. Feature archive eligibility is separate from report placement. Preserve established historical paths unless an authorized migration includes them.

## Recovery and changed scope

On resume, inspect actual lists, reports, Git commits/pushes and hosted states. Finish the earliest unmet authorized transition, including older pending closures. Reuse exact managed identities after partial creation. For an uncertain issue/milestone write, read actual state and evidence before replay; incomplete or contradictory lookup leaves the outcome unknown. A report partly written needs missing review/check/repair work; a committed report needs its pending push, not repeated review. A closed milestone with uncommitted local parent status needs status reconciliation. A completed phase review with integration pending needs that existing integration finished before next-phase activation. Do not introduce a second progress registry or require a report to contain its own commit SHA.

Accepted steering/feature changes can invalidate task and parent acceptance. Preserve stable IDs, earlier reports and evidence; mark reassessment pending and reconcile authorized issue/milestone reopening when current acceptance fails. Retired work is not verified completion and must not be silently closed as completed. Feature transfer retains its original issue; a scoped feature parent cannot close a whole-project milestone while another owning list still contains unfinished work. Existing completed phases require a scoped accepted amendment and dependency reassessment, not silent replay or advancement.

```

Read correction: attempted sdd-plan/references/conformance-review.md in an earlier batched cat; stderr No such file or directory. Loaded the actual referenced sdd-plan/references/review.md instead. No authority inferred from the unavailable path.

## Owned document incorporation

Edit script (actual executed source):

```python
from pathlib import Path
import hashlib,sys
sys.path.insert(0,'/workspace/scratch')
from a022_acceptance_log import root,journal

def replace(path,old,new):
 p=root/path;s=p.read_text();assert old in s,(path,old);p.write_text(s.replace(old,new))
replace('docs/dev/SPEC.md','Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END.','Endpoints are nonempty sequences of Unicode decimal digits (Unicode category Nd), interpreted by each digit\'s decimal value in base10, inclusive and one-based; their numeric values must be positive and START <= END. ASCII and non-ASCII decimal digits may be mixed within or between endpoints, and leading zeros from any accepted decimal digit set are allowed.')
replace('docs/dev/SPEC.md','Reject signs, whitespace, Unicode digits, zero, reversed endpoints','Reject signs, whitespace, non-decimal numerals (including `²`), zero, reversed endpoints')
replace('docs/dev/SPEC.md','| same | 1:1 | 1 / 2 |','| same | 1:1 | 1 / 2 |\n| same | ١:٢ or １:２ or 1:٢ or ٠1:０２ | 2 / 3 |')
replace('docs/dev/SPEC.md','both option spellings/orders/formats, leading-zero endpoints, huge endpoints','both option spellings/orders/formats, all Unicode Nd digit sets and mixed ASCII/Unicode decimal endpoints, decimal-value ordering across digit sets, leading-zero endpoints, huge endpoints')
replace('docs/dev/SPEC.md','all rejection categories and mixed repeated spellings before acquisition','all rejection categories (including signs, spaces, `²`, Unicode zero-only and numerically reversed endpoints) and mixed repeated spellings before acquisition')
replace('docs/dev/ARCHITECTURE.md','positive ordered ASCII decimals','positive ordered Unicode decimal endpoints under S-8')
replace('docs/dev/DECOMPOSITION.md','one ordered positive ASCII range','one ordered positive Unicode decimal range under S-8')
replace('docs/dev/PLAN.md','unbounded decimals, text/JSON','unbounded Unicode decimal endpoints under S-8, text/JSON')
replace('docs/dev/PLAN.md','ASCII/leading-zero/huge decimal/rejected syntax','Unicode Nd/mixed ASCII-and-Unicode/leading-zero/huge decimal/rejected syntax')
replace('docs/dev/TASKS.md','T-018–T-022 range implementation/review is verified below','T-018–T-022 range implementation/review has historical evidence below; revised S-8 Unicode decimal acceptance requires the pending reassessments recorded with its owners')
replace('docs/dev/TASKS.md','positive ASCII inclusive endpoints','positive Unicode decimal (Nd) inclusive endpoints, including mixed digit sets and leading zeros,')
replace('docs/dev/TASKS.md','option orders, leading zeros and endpoints longer','option orders, Unicode Nd endpoints (`١:٢`, `１:２`), mixed ASCII/Unicode endpoints and leading zeros, numeric ordering across digit sets, signs/spaces/non-decimal numerals such as `²` rejected before acquisition, and endpoints longer')
p=root/'docs/dev/TASKS.md';s=p.read_text()
notes={
'T-019':'reassess command parsing/comparison and actual module text/JSON against all Unicode Nd digit sets, mixed endpoints, leading zeros, unbounded lengths and retained rejection/usage-before-input, full decode/BOM/EOF/resource rules. Prior evidence at 9ade315a9f6ded1fade6f457a504f5e07e58fba5 verifies ASCII and explicitly rejects Unicode examples; it cannot establish revised S-8.',
'T-020':'reassess public range syntax/examples and isolated extracted-source acceptance after T-019; existing README/module documentation and archive evidence at 749a89844249d3b1c5ebb04c459d7e66bcb3ed2e describe the ASCII-only grammar.',
'T-021':'reassess milestone 2.4 code review, regressions, documentation/distribution and all revised exits after T-019/T-020; existing report at 3f93cd40d90001ee7e4f54b36c764d1d5067b72e and features/002_ea97182/2.4.md verify the prior ASCII grammar.',
'T-022':'reassess feature cross-component review/final report after milestone 2.4; existing phase/implementation reports at d518cc23650018542e43d8fb5a63f44a4d283518 and features/002_ea97182/PHASE-REPORT.md verify the prior ASCII grammar.',
'Milestone 2.4':'reassess revised Unicode Nd/mixed-decimal range exits through T-019–T-021; its historical ASCII acceptance and features/002_ea97182/2.4.md do not establish current completion.',
'Milestone 2.5':'reassess revised Unicode Nd/mixed-decimal cross-component exits through T-022 after milestone 2.4; historical ASCII feature reports do not establish current completion.'}
lines=s.splitlines();new=[]
for line in lines:
 new.append(line)
 for key,detail in notes.items():
  if line.lstrip().startswith('- [x] '+key+' —'):
   indent=' '*(len(line)-len(line.lstrip())+4)
   new.append(indent+'Completion reassessment pending (2026-10-05): '+key+' acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. '+detail+' Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.')
s='\n'.join(new)+'\n'
s=s.replace('T-018–T-022 are verified completed on feature/002_ea97182-line-ranges.','T-018–T-022 have historical verified completion on feature/002_ea97182-line-ranges for the ASCII grammar. Current T-019–T-022 and milestone 2.4/2.5 claims are disputed by the owning Completion reassessment pending notes; T-018\'s source-independent seam acceptance is unchanged.')
s=s.replace('record evidence and TODO: None.','record historical evidence and TODO: None for the prior acceptance, without establishing revised Unicode decimal acceptance.')
s=s.replace('records current acceptance.','records historical ASCII acceptance.')
p.write_text(s)

states=['docs/dev/PROJECT.md','docs/dev/ARCHITECTURE.md','docs/dev/DECOMPOSITION.md','docs/dev/SPEC.md','docs/dev/PLAN.md','docs/dev/layout.md','docs/dev/TASKS.md']
identity='\n'.join('- `'+path+'`: SHA-256 `'+hashlib.sha256((root/path).read_bytes()).hexdigest()+'`.' for path in states)
scopes=[('SPEC',4,'sdd-specify','S-8 requires each endpoint character to be Nd and interprets decimal values, including mixed digit sets and leading zeros. New objective row covers Arabic-Indic, fullwidth and mixed digits; rejection specifies non-decimal ², zero and reversed numeric bounds. All S-1–S-7/API/decode/BOM/EOF/atomicity/option composition obligations remain. Design retains cli validation ownership with unchanged core/io seams; no structural redesign.'),('PLAN',4,'sdd-plan','S-8 maps to existing 2.4 range delivery and 2.5 scoped review, with Unicode Nd/mixed-digit/leading-zero/unbounded checks and retained whole-input/resource/distribution exits. Phase1 retains two cohesive delivery milestones (MVP/reliable distribution), excluding1.3; Phase2 retains three (2.1/2.2/2.4), excluding2.3/2.5 review. Small Phase1 group is justified by distinct useful MVP/reliability outcomes; no padding or new milestone. Layout unchanged and sufficient.'),('TASKS',5,'sdd-tasks','Existing T-019 is the sole parser/CLI acceptance owner; no new or duplicate task is created. T-020 docs/extraction, T-021 milestone review, T-022 feature review and parents2.4/2.5 have durable pending notes, preserving checked boxes and native task IDs/prior evidence. T-018 seam is unaffected; T-013–T-017/Phase2 remain incomplete. Delivery counts remain1.1:3,1.2:3,2.1:2,2.2:3,2.4:3, each excluding its final review task;1.3/2.3/2.5 are dedicated one-task reviews. Two-task2.1 is justified by rendering then docs/extraction; other bounded groups remain coherent. IDs1–22 stay unique, hierarchy/dependencies intact. Completion claims and archived feature snapshots cannot skip revised acceptance reassessment.')]
for name,rev,owner,coverage in scopes:
 path=root/f'docs/dev/{name}-REVIEW-REPORT.md';s=path.read_text();s=s.replace(f'Revision {rev-1} records current accepted owner identities, coverage and limits.',f'Revision {rev} records current accepted owner identities, coverage and limits.')
 text=f'''\n## Revision {rev} — Unicode decimal endpoint acceptance\n\nOwner assessment: {owner} under selected acceptance incorporation, 2026-10-05. Accepted request: expand named-file endpoint grammar to Unicode category Nd, including mixed digit sets and leading zeros; retain positivity, numeric ordering, strict full decoding, BOM/EOF rules, single option and usage-before-input. Baseline: `0e4741465c3e086d2ab95c5af73ca89371c16fac`; branch: `trial/a022-acceptance-change`. Publication is only to the authorized local bare trial branch; no live/hosted integration.\n\n{coverage}\n\nExact reviewed/governing states:\n\n{identity}\n'''
 for upstream in (['SPEC'] if name=='PLAN' else ['SPEC','PLAN'] if name=='TASKS' else []):
  up=f'docs/dev/{upstream}-REVIEW-REPORT.md';text+=f'\n- `{up}`: SHA-256 `'+hashlib.sha256((root/up).read_bytes()).hexdigest()+'`.\n'
 text+='''\nFinding A022-ACCEPTANCE: prior ASCII-only acceptance/evidence does not cover the accepted Unicode decimal grammar. Governing SPEC/design/PLAN/TASKS wording and adjacent current QC are reconciled; historical reports/snapshots remain unchanged. Document conformance finding resolved. Product acceptance reassessment remains pending with sdd-implement, not a deferred conformance finding or a verified feature.\n\nFull selected-root review checked canonical ownership, S-1–S-8 traceability, unchanged dependencies/non-goals, objective decimal-value acceptance, unique task ownership, hierarchy, local links, heading spacing and allowed-path/whitespace diff. Scoped document checks passed. No product suite, CLI acceptance invocation or implementation was performed. Gate: Ready for current document conformance only; changed delivered acceptance is not verified. Next executable work is T-019 acceptance reassessment/correction under a separately authorized sdd-implement range, followed by the affected T-020–T-022 review/evidence dispositions. Do not select unchecked T-013 from a checkbox scan while these claims remain disputed. Hosted state is retained and uninspected in this local trial.\n'''
 path.write_text(s+text)
with journal.open('a') as f:
 f.write('\n## Owned document incorporation\n\nEdit script (actual executed source):\n\n```python\n'+Path(__file__).read_text()+'\n```\n')
print('Reconciled 8 owned governing/QC documents; historical sources, production, tests unchanged.')

```

### Command ['git', '--no-optional-locks', 'diff', '--check']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--stat']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
 docs/dev/ARCHITECTURE.md        |  2 +-
 docs/dev/DECOMPOSITION.md       |  2 +-
 docs/dev/PLAN-REVIEW-REPORT.md  | 24 +++++++++++++++++++++++-
 docs/dev/PLAN.md                |  4 ++--
 docs/dev/SPEC-REVIEW-REPORT.md  | 22 +++++++++++++++++++++-
 docs/dev/SPEC.md                |  5 +++--
 docs/dev/TASKS-REVIEW-REPORT.md | 26 +++++++++++++++++++++++++-
 docs/dev/TASKS.md               | 16 +++++++++++-----
 8 files changed, 87 insertions(+), 14 deletions(-)

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--', 'docs/dev/SPEC.md', 'docs/dev/TASKS.md']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
diff --git a/docs/dev/SPEC.md b/docs/dev/SPEC.md
index b4e65c2..7186355 100644
--- a/docs/dev/SPEC.md
+++ b/docs/dev/SPEC.md
@@ -48,7 +48,7 @@ Public API/module documentation describes signatures, text/BOM rules, UTF-8 exce
 
 ### Invocation and validation
 
-Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.
+Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty sequences of Unicode decimal digits (Unicode category Nd), interpreted by each digit's decimal value in base10, inclusive and one-based; their numeric values must be positive and START <= END. ASCII and non-ASCII decimal digits may be mixed within or between endpoints, and leading zeros from any accepted decimal digit set are allowed. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, non-decimal numerals (including `²`), zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.
 
 ### Selection semantics
 
@@ -68,6 +68,7 @@ Normalization and selection operate on decoded strings independently of source a
 | --- | --- | --- |
 | `alpha beta\nbeta\nlast two` | 2:3 or 2:99 | 2 / 3 |
 | same | 1:1 | 1 / 2 |
+| same | ١:٢ or １:２ or 1:٢ or ٠1:０２ | 2 / 3 |
 | same | 4:99 | 0 / 0 |
 | `a\n\n` | 2:9 | 1 / 0 |
 | `a\r\nb c\rd\n` | 2:3 | 2 / 3 |
@@ -77,7 +78,7 @@ Normalization and selection operate on decoded strings independently of source a
 | `a\n\ufeff\n` | 2:2 | 1 / 1 |
 | `a\u2028b\nlast` | 1:1 | 1 / 2 |
 
-Acceptance includes both option spellings/orders/formats, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout.
+Acceptance includes both option spellings/orders/formats, all Unicode Nd digit sets and mixed ASCII/Unicode decimal endpoints, decimal-value ordering across digit sets, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories (including signs, spaces, `²`, Unicode zero-only and numerically reversed endpoints) and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout.
 
 The command adapter owns syntax, option composition and rendering; named-file acquisition owns complete decoding and handle closure; pure text processing owns normalization, selection and counting. Public facade exports remain unchanged.
 
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index fb849fb..2d0fb28 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,6 +1,6 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-012 are implemented and verified below; T-018–T-022 range implementation/review is verified below; remaining Phase 2 tasks retain their incomplete status. Range tasks are owned only here; feature snapshots are not executable lists. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Phase 2 is activated on phase/2-output-and-source-extensions; JSON milestone2.1 is selected, with stdin and final review incomplete. Range tasks T-018–T-022 have this list as their sole executable owner.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-012 are implemented and verified below; T-018–T-022 range implementation/review has historical evidence below; revised S-8 Unicode decimal acceptance requires the pending reassessments recorded with its owners; remaining Phase 2 tasks retain their incomplete status. Range tasks are owned only here; feature snapshots are not executable lists. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Phase 2 is activated on phase/2-output-and-source-extensions; JSON milestone2.1 is selected, with stdin and final review incomplete. Range tasks T-018–T-022 have this list as their sole executable owner.
 
 ## Hosted tracking
 
@@ -110,6 +110,7 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Evidence: phase code review, complete nonempty product suites, runnable docs, isolated extracted-source module checks, blocker repair and committed/pushed reports. Reports: docs/dev/reports/phases/2/PHASE-REPORT.md and docs/dev/reports/IMPLEMENTATION-REPORT.md. Aggregate unresolved admissible TODOs and solution/owner/provenance with resolution references; verify full-phase explicit integration, merged state and publication before claiming complete implementation.
 
     - [x] Milestone 2.4 — Named-file line ranges
+        Completion reassessment pending (2026-10-05): Milestone 2.4 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess revised Unicode Nd/mixed-decimal range exits through T-019–T-021; its historical ASCII acceptance and features/002_ea97182/2.4.md do not establish current completion. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
         - [x] T-018 — Establish normalized logical-line selection seam
             Depends on: T-012 and current main preparation gates.
             Scope: textstats/core.py, textstats/io.py and tests/unit semantic/acquisition checks; preserve public facade.
@@ -117,27 +118,32 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Evidence: pure supplied selection examples, empty/final segments/Unicode separators/interior and double BOM; whole-input API signatures/exports/silence/counts, close-on-success/failure and unchanged bytes. Strict decoding remains complete before any selection. Default CLI stays useful while no range command is exposed yet.
             Completion evidence (2026-10-05): focused selection RED ran 2 tests with 2 missing-seam assertion failures; GREEN independent unit19/integration11 passed, no skips. Supplied logical-line/BOM/Unicode/EOF rows preserve characters and terminators; whole-input facade/signature/silence/unchanged bytes and existing success/read/decode/close lifecycle regressions pass after private full-decode factoring. Default CLI unchanged. `git diff --check` passed. Issue #18 title/phase/milestone confirmed; protected metadata omits body marker, so prior projection marker verification in authorized request is retained rather than claimed freshly inspected.
         - [x] T-019 — Integrate validated named-file range text and JSON commands
+            Completion reassessment pending (2026-10-05): T-019 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess command parsing/comparison and actual module text/JSON against all Unicode Nd digit sets, mixed endpoints, leading zeros, unbounded lengths and retained rejection/usage-before-input, full decode/BOM/EOF/resource rules. Prior evidence at 9ade315a9f6ded1fade6f457a504f5e07e58fba5 verifies ASCII and explicitly rejects Unicode examples; it cannot establish revised S-8. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-018.
             Scope: textstats/cli.py and tests/unit/test_cli.py plus tests/integration module/file checks.
-            Outcome: --lines spellings validate positive ASCII inclusive endpoints before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (S-8).
-            Evidence: actual module supplied examples in text/JSON and both option orders, leading zeros and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
+            Outcome: --lines spellings validate positive Unicode decimal (Nd) inclusive endpoints, including mixed digit sets and leading zeros, before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (S-8).
+            Evidence: actual module supplied examples in text/JSON and both option orders, Unicode Nd endpoints (`١:٢`, `１:２`), mixed ASCII/Unicode endpoints and leading zeros, numeric ordering across digit sets, signs/spaces/non-decimal numerals such as `²` rejected before acquisition, and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
             Completion evidence (2026-10-05): actual module RED observed 73 unknown-option failures across 2 test methods; after parser/composition implementation GREEN independent unit21/integration13 passed, no skips. Both range spellings/text/JSON/orders, ASCII/leading-zero/5000-digit endpoints, malformed/repeated ranges before acquisition, complete bad UTF-8 after END, BOM/Unicode/CRLF/EOF rows, file preservation and owned-handle/expected errors verified. API stays whole-input; no stdin delivered. `git diff --check` passed. #19 exact title and opening/closing task markers verified through readonly connector; maintained closure pending adapter facility resolution.
         - [x] T-020 — Document ranges and verify extracted-source acceptance
+            Completion reassessment pending (2026-10-05): T-020 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess public range syntax/examples and isolated extracted-source acceptance after T-019; existing README/module documentation and archive evidence at 749a89844249d3b1c5ebb04c459d7e66bcb3ed2e describe the ASCII-only grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-019.
             Scope: README.md, docs/module.md, docs/api.md accuracy review and tests/integration/test_distribution.py; existing Makefile recipe.
             Outcome: runnable named-file range examples, syntax/repetition/status/complete-decode/BOM rules and explicit stdin boundary; public API docs retain whole-input contract (S-8/S-7).
             Evidence: execute public examples/help, run independent nonempty product suites, clean archive extraction and actual extracted python -m textstats for both spellings/formats/BOM policies and representative usage/read/decode failures. Remove checkout import leakage, assert extracted package identity and unchanged input. Workflow fixtures remain separate.
             Completion evidence (2026-10-05): README/module named-file range examples, full syntax/repetition/status/decode/BOM/EOF rules and explicit stdin boundary added; API reviewed whole-input unchanged. Existing delivered behavior characterized, no production edit or manufactured RED. Extended isolated archive test passed with extracted import identity, both spellings/text/JSON/BOM orders, dash file and usage/read/late-decode errors; bytes unchanged. Independent unit21/integration13 passed, no skips; public fenced Python/shell examples executed in temporary directories with expected statuses, build/test blocks separately covered by suites. Diff check passed. #20 exact title/markers verified; hosted reconciliation pending unknown preHTTP adapter failure.
-        Completion evidence (2026-10-05): T018–T021 implementation, separate code review, unit21/integration13, public examples/isolated source checks and all PLAN2.4 exits verified. [Range milestone report](features/002_ea97182/2.4.md) records current acceptance. Hosted report/issue/milestone transitions are separately observed after publication; Phase2 remains incomplete.
+        Completion evidence (2026-10-05): T018–T021 implementation, separate code review, unit21/integration13, public examples/isolated source checks and all PLAN2.4 exits verified. [Range milestone report](features/002_ea97182/2.4.md) records historical ASCII acceptance. Hosted report/issue/milestone transitions are separately observed after publication; Phase2 remains incomplete.
         - [x] T-021 — Review, test and report range milestone 2.4
+            Completion reassessment pending (2026-10-05): T-021 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess milestone 2.4 code review, regressions, documentation/distribution and all revised exits after T-019/T-020; existing report at 3f93cd40d90001ee7e4f54b36c764d1d5067b72e and features/002_ea97182/2.4.md verify the prior ASCII grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-018, T-019, T-020.
             Scope: all named-file range behavior, helper/acquisition/CLI composition, API compatibility, docs/distribution and prior acceptance.
             Evidence: separate code review and focused/regression checks against all2.4 exits, useful demonstrations, required blocker repairs, TODO provenance and committed/pushed report. Reconcile issues and close2.4 only after all constituent issues are verified complete when tracking is active.
             Report: docs/dev/features/002_ea97182/2.4.md.
             Completion evidence (2026-10-05): [milestone code review/testing report](features/002_ea97182/2.4.md), reviewed749a898 plus accepted owner/docstring-only changes; independent unit21/integration13 no skips, public examples/links/diff check pass. No in-scope finding/TODO. Governing-owner incorporation/QC Ready; issue#21 exact title/markers verified, closure follows commit/push.
     - [x] Milestone 2.5 — Range feature review
+        Completion reassessment pending (2026-10-05): Milestone 2.5 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess revised Unicode Nd/mixed-decimal cross-component exits through T-022 after milestone 2.4; historical ASCII feature reports do not establish current completion. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
         Completion evidence (2026-10-05): T022 cross-component review, independent unit21/integration13, examples/links/archive and main owner QC verify scoped PLAN2.5 exits; [feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) retain TODO: None. Hosting closure follows publication; main Phase2 remains incomplete.
         - [x] T-022 — Review, test and report the named-file range feature
+            Completion reassessment pending (2026-10-05): T-022 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess feature cross-component review/final report after milestone 2.4; existing phase/implementation reports at d518cc23650018542e43d8fb5a63f44a4d283518 and features/002_ea97182/PHASE-REPORT.md verify the prior ASCII grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: feature milestone2.4 complete/closed when tracking is active, including T-021.
             Scope: cross-component S-8 and retained named-file S-1–S-5/S-7; feature-only phase/final report, not main T-017 or stdin acceptance.
             Evidence: separate feature phase code review, nonempty suites, API/default/format/BOM/decode/lifecycle regressions, runnable docs and extracted-source checks, blocker repair and final feature TODO aggregation with provenance/resolution references. Separately authorized full implementation incorporates accepted selected feature docs and reconciles task ownership/QC before final target merge and merged-state verification/publication; main Phase2 remains unfinished. No incorporation/merge/implementation during preparation.
@@ -145,6 +151,6 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
 
 ## Range feature conclusion
 
-T-018–T-022 are verified completed on feature/002_ea97182-line-ranges. Governing owners and task ownership are reconciled; feature sources/adjacent QC are historical under [feature002_ea97182](features/002_ea97182/README.md). Fresh independent unit21/integration13, code review, public examples, links and diff checks establish named-file feature exits. [Feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) record evidence and TODO: None. 2.4/#7 closed with0open/4closed after report/status publication; 2.5/#8 closure follows T022 publication. Main Phase2, stdin2.2 and final2.3/T013–T017 remain unchecked; no Phase2→main integration is authorized here.
+T-018–T-022 have historical verified completion on feature/002_ea97182-line-ranges for the ASCII grammar. Current T-019–T-022 and milestone 2.4/2.5 claims are disputed by the owning Completion reassessment pending notes; T-018's source-independent seam acceptance is unchanged. Governing owners and task ownership are reconciled; feature sources/adjacent QC are historical under [feature002_ea97182](features/002_ea97182/README.md). Fresh independent unit21/integration13, code review, public examples, links and diff checks establish named-file feature exits. [Feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) record historical evidence and TODO: None for the prior acceptance, without establishing revised Unicode decimal acceptance. 2.4/#7 closed with0open/4closed after report/status publication; 2.5/#8 closure follows T022 publication. Main Phase2, stdin2.2 and final2.3/T013–T017 remain unchecked; no Phase2→main integration is authorized here.
 
 T-022 completion evidence (2026-10-05): reviewed full delivered production/test/docs/build boundaries separately from fresh unit21/integration13 (no skips), verified R1–R4/mainS8 and retained named-file/API/format/decode/BOM/resource/docs/distribution conditions. Sources and adjacent QC archived only after owner/task/evidence disposition; main owner QC rechecked, links/unique IDs/whitespace passed. No findings/TODO. #22 exact title/opening+closing markers verified; report/status push precedes issue/milestone closure and explicit feature integration.

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--name-only']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
docs/dev/ARCHITECTURE.md
docs/dev/DECOMPOSITION.md
docs/dev/PLAN-REVIEW-REPORT.md
docs/dev/PLAN.md
docs/dev/SPEC-REVIEW-REPORT.md
docs/dev/SPEC.md
docs/dev/TASKS-REVIEW-REPORT.md
docs/dev/TASKS.md

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--exit-code', '0e4741465c3e086d2ab95c5af73ca89371c16fac', '--', 'textstats-run-resources', 'textstats', 'tests', 'README.md', 'docs/module.md', 'docs/api.md', 'Makefile']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--check']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--', 'docs/dev/ARCHITECTURE.md', 'docs/dev/DECOMPOSITION.md', 'docs/dev/PLAN.md', 'docs/dev/SPEC.md', 'docs/dev/TASKS.md', 'docs/dev/SPEC-REVIEW-REPORT.md', 'docs/dev/PLAN-REVIEW-REPORT.md', 'docs/dev/TASKS-REVIEW-REPORT.md']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
diff --git a/docs/dev/ARCHITECTURE.md b/docs/dev/ARCHITECTURE.md
index c90c1f0..333c671 100644
--- a/docs/dev/ARCHITECTURE.md
+++ b/docs/dev/ARCHITECTURE.md
@@ -16,6 +16,6 @@ Decode complete bytes using strict UTF-8 before text processing. File reads pres
 
 ## Named-file range selection
 
-A CLI-only selection stage sits between complete decoding/BOM normalization and counting. It identifies only CRLF, CR and LF logical lines, preserves selected contents and terminators, and never applies BOM stripping again to a slice. Source-independent decoded-text processing supports named files and future stdin. Range syntax is validated before acquisition, including repetition and positive ordered ASCII decimals without an endpoint cap or interpreter conversion limit. Named-file acquisition exposes complete decoded text privately, while count_file retains its whole-input contract. The command selects normalized logical lines and counts the slice with BOM stripping disabled. Stdin acquisition remains a separate delivery; stdin ranges are unsupported.
+A CLI-only selection stage sits between complete decoding/BOM normalization and counting. It identifies only CRLF, CR and LF logical lines, preserves selected contents and terminators, and never applies BOM stripping again to a slice. Source-independent decoded-text processing supports named files and future stdin. Range syntax is validated before acquisition, including repetition and positive ordered Unicode decimal endpoints under S-8 without an endpoint cap or interpreter conversion limit. Named-file acquisition exposes complete decoded text privately, while count_file retains its whole-input contract. The command selects normalized logical lines and counts the slice with BOM stripping disabled. Stdin acquisition remains a separate delivery; stdin ranges are unsupported.
 
 See [DECOMPOSITION.md](DECOMPOSITION.md) for component seams and [SPEC.md](SPEC.md) for observable contracts.
diff --git a/docs/dev/DECOMPOSITION.md b/docs/dev/DECOMPOSITION.md
index 4f57915..b7d4e8c 100644
--- a/docs/dev/DECOMPOSITION.md
+++ b/docs/dev/DECOMPOSITION.md
@@ -16,6 +16,6 @@ The intended components refine [ARCHITECTURE.md](ARCHITECTURE.md). [SPEC.md](SPE
 
 `count_text` consumes caller text and owns only normalization/counting. `count_file` consumes a path and delegates after complete decoding. The command adapter delegates named-file acquisition and, at its later delivery boundary, reads borrowed stdin bytes until EOF. Read/decode failures propagate through the API; the CLI translates expected failures and produces no partial success output. The core cannot emit diagnostics.
 
-Text formatting and JSON rendering consume the same statistics. Option validation precedes any input acquisition. The internal range selector consumes already normalized text and passes retained contents/terminators to counting without a second BOM normalization. It has no source dependency or public export. The command adapter validates one ordered positive ASCII range before acquisition, composes format/BOM options and invokes source-independent selection after complete decoding and one BOM normalization. Stdin acquisition remains separately scheduled; stdin ranges are unsupported.
+Text formatting and JSON rendering consume the same statistics. Option validation precedes any input acquisition. The internal range selector consumes already normalized text and passes retained contents/terminators to counting without a second BOM normalization. It has no source dependency or public export. The command adapter validates one ordered positive Unicode decimal range under S-8 before acquisition, composes format/BOM options and invokes source-independent selection after complete decoding and one BOM normalization. Stdin acquisition remains separately scheduled; stdin ranges are unsupported.
 
 No extra abstraction layer or focused child document is needed for this bounded utility. Source allocation belongs to layout, and delivery order belongs to PLAN.
diff --git a/docs/dev/PLAN-REVIEW-REPORT.md b/docs/dev/PLAN-REVIEW-REPORT.md
index 1e37b42..642205e 100644
--- a/docs/dev/PLAN-REVIEW-REPORT.md
+++ b/docs/dev/PLAN-REVIEW-REPORT.md
@@ -2,7 +2,7 @@
 
 ## Current gate
 
-State: Ready for current PLAN.md conformance. Owner: sdd-plan, 2026-10-05. Revision 3 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
+State: Ready for current PLAN.md conformance. Owner: sdd-plan, 2026-10-05. Revision 4 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
 
 ## Retained original gate and identities (historical)
 
@@ -89,3 +89,25 @@ Exact current reviewed/governing SHA256:
 - `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`
 
 Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.
+
+## Revision 4 — Unicode decimal endpoint acceptance
+
+Owner assessment: sdd-plan under selected acceptance incorporation, 2026-10-05. Accepted request: expand named-file endpoint grammar to Unicode category Nd, including mixed digit sets and leading zeros; retain positivity, numeric ordering, strict full decoding, BOM/EOF rules, single option and usage-before-input. Baseline: `0e4741465c3e086d2ab95c5af73ca89371c16fac`; branch: `trial/a022-acceptance-change`. Publication is only to the authorized local bare trial branch; no live/hosted integration.
+
+S-8 maps to existing 2.4 range delivery and 2.5 scoped review, with Unicode Nd/mixed-digit/leading-zero/unbounded checks and retained whole-input/resource/distribution exits. Phase1 retains two cohesive delivery milestones (MVP/reliable distribution), excluding1.3; Phase2 retains three (2.1/2.2/2.4), excluding2.3/2.5 review. Small Phase1 group is justified by distinct useful MVP/reliability outcomes; no padding or new milestone. Layout unchanged and sufficient.
+
+Exact reviewed/governing states:
+
+- `docs/dev/PROJECT.md`: SHA-256 `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`.
+- `docs/dev/ARCHITECTURE.md`: SHA-256 `36d791fca787c60328cec8fa0742201a48ab5a6862ded6707c4c7ce3bd809505`.
+- `docs/dev/DECOMPOSITION.md`: SHA-256 `4f2faa1123b65e7c83909d3d4e5a6d310b4210809975ef9e5be013b25ed59a8c`.
+- `docs/dev/SPEC.md`: SHA-256 `9e58d8f5debc1ddb830fa63ed5860804df06954a38187ccb157200be7db1660b`.
+- `docs/dev/PLAN.md`: SHA-256 `a9b95ee565598935497fd0fbefd0fc19459b66c67443358544285d86b9fdea58`.
+- `docs/dev/layout.md`: SHA-256 `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`.
+- `docs/dev/TASKS.md`: SHA-256 `d00709492e31f9019a4da6fff98906940b05e2f6a91bca58cb14038c366193db`.
+
+- `docs/dev/SPEC-REVIEW-REPORT.md`: SHA-256 `1e1e340f2bd79d2aeff48ced35e317920bf38445cb9fa76f8c79ca1143e137ef`.
+
+Finding A022-ACCEPTANCE: prior ASCII-only acceptance/evidence does not cover the accepted Unicode decimal grammar. Governing SPEC/design/PLAN/TASKS wording and adjacent current QC are reconciled; historical reports/snapshots remain unchanged. Document conformance finding resolved. Product acceptance reassessment remains pending with sdd-implement, not a deferred conformance finding or a verified feature.
+
+Full selected-root review checked canonical ownership, S-1–S-8 traceability, unchanged dependencies/non-goals, objective decimal-value acceptance, unique task ownership, hierarchy, local links, heading spacing and allowed-path/whitespace diff. Scoped document checks passed. No product suite, CLI acceptance invocation or implementation was performed. Gate: Ready for current document conformance only; changed delivered acceptance is not verified. Next executable work is T-019 acceptance reassessment/correction under a separately authorized sdd-implement range, followed by the affected T-020–T-022 review/evidence dispositions. Do not select unchecked T-013 from a checkbox scan while these claims remain disputed. Hosted state is retained and uninspected in this local trial.
diff --git a/docs/dev/PLAN.md b/docs/dev/PLAN.md
index 99aab40..efa05a8 100644
--- a/docs/dev/PLAN.md
+++ b/docs/dev/PLAN.md
@@ -42,9 +42,9 @@ Dedicated single phase code review/testing/report outcome after both delivery mi
 
 Prerequisite: completed/published JSON milestone2.1/T-012 at the pinned paused baseline, current main SPEC/design QC and separately authorized implementation. No prerequisite on unfinished stdin or main final review; whole-input named-file text/JSON already works. Delivery retains the useful baseline while introducing a source-independent normalization/selection seam, then composing command validation/acquisition/rendering into a named-file slice. Pure helper work is a bounded prerequisite to the earliest usable changed CLI path, not a released skeleton.
 
-Scope: S-8 and retained S-1–S-5/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded decimals, text/JSON and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.
+Scope: S-8 and retained S-1–S-5/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded Unicode decimal endpoints under S-8, text/JSON and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.
 
-Exit: actual module invocation counts selected named-file lines in text/JSON with exact stdout/status/stderr; supplied examples, ASCII/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.
+Exit: actual module invocation counts selected named-file lines in text/JSON with exact stdout/status/stderr; supplied examples, Unicode Nd/mixed ASCII-and-Unicode/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.
 
 ### Milestone 2.5 — Range feature review
 
diff --git a/docs/dev/SPEC-REVIEW-REPORT.md b/docs/dev/SPEC-REVIEW-REPORT.md
index 785f00b..0873897 100644
--- a/docs/dev/SPEC-REVIEW-REPORT.md
+++ b/docs/dev/SPEC-REVIEW-REPORT.md
@@ -2,7 +2,7 @@
 
 ## Current gate
 
-State: Ready for current SPEC.md conformance. Owner: sdd-specify, 2026-10-05. Revision 3 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
+State: Ready for current SPEC.md conformance. Owner: sdd-specify, 2026-10-05. Revision 4 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
 
 ## Original reviewed identities
 
@@ -89,3 +89,23 @@ Exact current reviewed/governing SHA256:
 - `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`
 
 Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.
+
+## Revision 4 — Unicode decimal endpoint acceptance
+
+Owner assessment: sdd-specify under selected acceptance incorporation, 2026-10-05. Accepted request: expand named-file endpoint grammar to Unicode category Nd, including mixed digit sets and leading zeros; retain positivity, numeric ordering, strict full decoding, BOM/EOF rules, single option and usage-before-input. Baseline: `0e4741465c3e086d2ab95c5af73ca89371c16fac`; branch: `trial/a022-acceptance-change`. Publication is only to the authorized local bare trial branch; no live/hosted integration.
+
+S-8 requires each endpoint character to be Nd and interprets decimal values, including mixed digit sets and leading zeros. New objective row covers Arabic-Indic, fullwidth and mixed digits; rejection specifies non-decimal ², zero and reversed numeric bounds. All S-1–S-7/API/decode/BOM/EOF/atomicity/option composition obligations remain. Design retains cli validation ownership with unchanged core/io seams; no structural redesign.
+
+Exact reviewed/governing states:
+
+- `docs/dev/PROJECT.md`: SHA-256 `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`.
+- `docs/dev/ARCHITECTURE.md`: SHA-256 `36d791fca787c60328cec8fa0742201a48ab5a6862ded6707c4c7ce3bd809505`.
+- `docs/dev/DECOMPOSITION.md`: SHA-256 `4f2faa1123b65e7c83909d3d4e5a6d310b4210809975ef9e5be013b25ed59a8c`.
+- `docs/dev/SPEC.md`: SHA-256 `9e58d8f5debc1ddb830fa63ed5860804df06954a38187ccb157200be7db1660b`.
+- `docs/dev/PLAN.md`: SHA-256 `a9b95ee565598935497fd0fbefd0fc19459b66c67443358544285d86b9fdea58`.
+- `docs/dev/layout.md`: SHA-256 `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`.
+- `docs/dev/TASKS.md`: SHA-256 `d00709492e31f9019a4da6fff98906940b05e2f6a91bca58cb14038c366193db`.
+
+Finding A022-ACCEPTANCE: prior ASCII-only acceptance/evidence does not cover the accepted Unicode decimal grammar. Governing SPEC/design/PLAN/TASKS wording and adjacent current QC are reconciled; historical reports/snapshots remain unchanged. Document conformance finding resolved. Product acceptance reassessment remains pending with sdd-implement, not a deferred conformance finding or a verified feature.
+
+Full selected-root review checked canonical ownership, S-1–S-8 traceability, unchanged dependencies/non-goals, objective decimal-value acceptance, unique task ownership, hierarchy, local links, heading spacing and allowed-path/whitespace diff. Scoped document checks passed. No product suite, CLI acceptance invocation or implementation was performed. Gate: Ready for current document conformance only; changed delivered acceptance is not verified. Next executable work is T-019 acceptance reassessment/correction under a separately authorized sdd-implement range, followed by the affected T-020–T-022 review/evidence dispositions. Do not select unchecked T-013 from a checkbox scan while these claims remain disputed. Hosted state is retained and uninspected in this local trial.
diff --git a/docs/dev/SPEC.md b/docs/dev/SPEC.md
index b4e65c2..7186355 100644
--- a/docs/dev/SPEC.md
+++ b/docs/dev/SPEC.md
@@ -48,7 +48,7 @@ Public API/module documentation describes signatures, text/BOM rules, UTF-8 exce
 
 ### Invocation and validation
 
-Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.
+Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty sequences of Unicode decimal digits (Unicode category Nd), interpreted by each digit's decimal value in base10, inclusive and one-based; their numeric values must be positive and START <= END. ASCII and non-ASCII decimal digits may be mixed within or between endpoints, and leading zeros from any accepted decimal digit set are allowed. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, non-decimal numerals (including `²`), zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines, --json and --keep-bom compose in either order before the `--` separator.
 
 ### Selection semantics
 
@@ -68,6 +68,7 @@ Normalization and selection operate on decoded strings independently of source a
 | --- | --- | --- |
 | `alpha beta\nbeta\nlast two` | 2:3 or 2:99 | 2 / 3 |
 | same | 1:1 | 1 / 2 |
+| same | ١:٢ or １:２ or 1:٢ or ٠1:０２ | 2 / 3 |
 | same | 4:99 | 0 / 0 |
 | `a\n\n` | 2:9 | 1 / 0 |
 | `a\r\nb c\rd\n` | 2:3 | 2 / 3 |
@@ -77,7 +78,7 @@ Normalization and selection operate on decoded strings independently of source a
 | `a\n\ufeff\n` | 2:2 | 1 / 1 |
 | `a\u2028b\nlast` | 1:1 | 1 / 2 |
 
-Acceptance includes both option spellings/orders/formats, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout.
+Acceptance includes both option spellings/orders/formats, all Unicode Nd digit sets and mixed ASCII/Unicode decimal endpoints, decimal-value ordering across digit sets, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories (including signs, spaces, `²`, Unicode zero-only and numerically reversed endpoints) and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text/JSON, BOM policy and representative failures without importing the checkout.
 
 The command adapter owns syntax, option composition and rendering; named-file acquisition owns complete decoding and handle closure; pure text processing owns normalization, selection and counting. Public facade exports remain unchanged.
 
diff --git a/docs/dev/TASKS-REVIEW-REPORT.md b/docs/dev/TASKS-REVIEW-REPORT.md
index 3f0bab5..af9a75a 100644
--- a/docs/dev/TASKS-REVIEW-REPORT.md
+++ b/docs/dev/TASKS-REVIEW-REPORT.md
@@ -2,7 +2,7 @@
 
 ## Current gate
 
-State: Ready for current TASKS.md conformance. Owner: sdd-tasks, 2026-10-05. Revision 4 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
+State: Ready for current TASKS.md conformance. Owner: sdd-tasks, 2026-10-05. Revision 5 records current accepted owner identities, coverage and limits. Original gate observations are retained historical evidence. Implementation, hosted lifecycle and integration are separately assessed.
 
 ## Retained original gate and identities (historical)
 
@@ -103,3 +103,27 @@ Exact current reviewed/governing SHA256:
 - `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`
 
 Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.
+
+## Revision 5 — Unicode decimal endpoint acceptance
+
+Owner assessment: sdd-tasks under selected acceptance incorporation, 2026-10-05. Accepted request: expand named-file endpoint grammar to Unicode category Nd, including mixed digit sets and leading zeros; retain positivity, numeric ordering, strict full decoding, BOM/EOF rules, single option and usage-before-input. Baseline: `0e4741465c3e086d2ab95c5af73ca89371c16fac`; branch: `trial/a022-acceptance-change`. Publication is only to the authorized local bare trial branch; no live/hosted integration.
+
+Existing T-019 is the sole parser/CLI acceptance owner; no new or duplicate task is created. T-020 docs/extraction, T-021 milestone review, T-022 feature review and parents2.4/2.5 have durable pending notes, preserving checked boxes and native task IDs/prior evidence. T-018 seam is unaffected; T-013–T-017/Phase2 remain incomplete. Delivery counts remain1.1:3,1.2:3,2.1:2,2.2:3,2.4:3, each excluding its final review task;1.3/2.3/2.5 are dedicated one-task reviews. Two-task2.1 is justified by rendering then docs/extraction; other bounded groups remain coherent. IDs1–22 stay unique, hierarchy/dependencies intact. Completion claims and archived feature snapshots cannot skip revised acceptance reassessment.
+
+Exact reviewed/governing states:
+
+- `docs/dev/PROJECT.md`: SHA-256 `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`.
+- `docs/dev/ARCHITECTURE.md`: SHA-256 `36d791fca787c60328cec8fa0742201a48ab5a6862ded6707c4c7ce3bd809505`.
+- `docs/dev/DECOMPOSITION.md`: SHA-256 `4f2faa1123b65e7c83909d3d4e5a6d310b4210809975ef9e5be013b25ed59a8c`.
+- `docs/dev/SPEC.md`: SHA-256 `9e58d8f5debc1ddb830fa63ed5860804df06954a38187ccb157200be7db1660b`.
+- `docs/dev/PLAN.md`: SHA-256 `a9b95ee565598935497fd0fbefd0fc19459b66c67443358544285d86b9fdea58`.
+- `docs/dev/layout.md`: SHA-256 `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`.
+- `docs/dev/TASKS.md`: SHA-256 `d00709492e31f9019a4da6fff98906940b05e2f6a91bca58cb14038c366193db`.
+
+- `docs/dev/SPEC-REVIEW-REPORT.md`: SHA-256 `1e1e340f2bd79d2aeff48ced35e317920bf38445cb9fa76f8c79ca1143e137ef`.
+
+- `docs/dev/PLAN-REVIEW-REPORT.md`: SHA-256 `2132c2fd328d4b79d019bbda5b6f8500286c8db659c0338cbebdae59adc13ef3`.
+
+Finding A022-ACCEPTANCE: prior ASCII-only acceptance/evidence does not cover the accepted Unicode decimal grammar. Governing SPEC/design/PLAN/TASKS wording and adjacent current QC are reconciled; historical reports/snapshots remain unchanged. Document conformance finding resolved. Product acceptance reassessment remains pending with sdd-implement, not a deferred conformance finding or a verified feature.
+
+Full selected-root review checked canonical ownership, S-1–S-8 traceability, unchanged dependencies/non-goals, objective decimal-value acceptance, unique task ownership, hierarchy, local links, heading spacing and allowed-path/whitespace diff. Scoped document checks passed. No product suite, CLI acceptance invocation or implementation was performed. Gate: Ready for current document conformance only; changed delivered acceptance is not verified. Next executable work is T-019 acceptance reassessment/correction under a separately authorized sdd-implement range, followed by the affected T-020–T-022 review/evidence dispositions. Do not select unchecked T-013 from a checkbox scan while these claims remain disputed. Hosted state is retained and uninspected in this local trial.
diff --git a/docs/dev/TASKS.md b/docs/dev/TASKS.md
index fb849fb..2d0fb28 100644
--- a/docs/dev/TASKS.md
+++ b/docs/dev/TASKS.md
@@ -1,6 +1,6 @@
 # TextStats executable task hierarchy
 
-Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-012 are implemented and verified below; T-018–T-022 range implementation/review is verified below; remaining Phase 2 tasks retain their incomplete status. Range tasks are owned only here; feature snapshots are not executable lists. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Phase 2 is activated on phase/2-output-and-source-extensions; JSON milestone2.1 is selected, with stdin and final review incomplete. Range tasks T-018–T-022 have this list as their sole executable owner.
+Derived from reviewed [SPEC.md](SPEC.md), [PLAN.md](PLAN.md), [layout.md](layout.md) and [DECOMPOSITION.md](DECOMPOSITION.md). [TASKS-REVIEW-REPORT.md](TASKS-REVIEW-REPORT.md) records preparation readiness. T-001–T-012 are implemented and verified below; T-018–T-022 range implementation/review has historical evidence below; revised S-8 Unicode decimal acceptance requires the pending reassessments recorded with its owners; remaining Phase 2 tasks retain their incomplete status. Range tasks are owned only here; feature snapshots are not executable lists. Maintained GitHub tracking is enabled for this repository; Phase 1 is implemented, reviewed and closed in maintained tracking. Phase 2 is activated on phase/2-output-and-source-extensions; JSON milestone2.1 is selected, with stdin and final review incomplete. Range tasks T-018–T-022 have this list as their sole executable owner.
 
 ## Hosted tracking
 
@@ -110,6 +110,7 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Evidence: phase code review, complete nonempty product suites, runnable docs, isolated extracted-source module checks, blocker repair and committed/pushed reports. Reports: docs/dev/reports/phases/2/PHASE-REPORT.md and docs/dev/reports/IMPLEMENTATION-REPORT.md. Aggregate unresolved admissible TODOs and solution/owner/provenance with resolution references; verify full-phase explicit integration, merged state and publication before claiming complete implementation.
 
     - [x] Milestone 2.4 — Named-file line ranges
+        Completion reassessment pending (2026-10-05): Milestone 2.4 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess revised Unicode Nd/mixed-decimal range exits through T-019–T-021; its historical ASCII acceptance and features/002_ea97182/2.4.md do not establish current completion. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
         - [x] T-018 — Establish normalized logical-line selection seam
             Depends on: T-012 and current main preparation gates.
             Scope: textstats/core.py, textstats/io.py and tests/unit semantic/acquisition checks; preserve public facade.
@@ -117,27 +118,32 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
             Evidence: pure supplied selection examples, empty/final segments/Unicode separators/interior and double BOM; whole-input API signatures/exports/silence/counts, close-on-success/failure and unchanged bytes. Strict decoding remains complete before any selection. Default CLI stays useful while no range command is exposed yet.
             Completion evidence (2026-10-05): focused selection RED ran 2 tests with 2 missing-seam assertion failures; GREEN independent unit19/integration11 passed, no skips. Supplied logical-line/BOM/Unicode/EOF rows preserve characters and terminators; whole-input facade/signature/silence/unchanged bytes and existing success/read/decode/close lifecycle regressions pass after private full-decode factoring. Default CLI unchanged. `git diff --check` passed. Issue #18 title/phase/milestone confirmed; protected metadata omits body marker, so prior projection marker verification in authorized request is retained rather than claimed freshly inspected.
         - [x] T-019 — Integrate validated named-file range text and JSON commands
+            Completion reassessment pending (2026-10-05): T-019 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess command parsing/comparison and actual module text/JSON against all Unicode Nd digit sets, mixed endpoints, leading zeros, unbounded lengths and retained rejection/usage-before-input, full decode/BOM/EOF/resource rules. Prior evidence at 9ade315a9f6ded1fade6f457a504f5e07e58fba5 verifies ASCII and explicitly rejects Unicode examples; it cannot establish revised S-8. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-018.
             Scope: textstats/cli.py and tests/unit/test_cli.py plus tests/integration module/file checks.
-            Outcome: --lines spellings validate positive ASCII inclusive endpoints before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (S-8).
-            Evidence: actual module supplied examples in text/JSON and both option orders, leading zeros and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
+            Outcome: --lines spellings validate positive Unicode decimal (Nd) inclusive endpoints, including mixed digit sets and leading zeros, before input, reject malformed/missing/repeated ranges, and compose with --json/--keep-bom; render the same selected counts with exact statuses/streams and unchanged whole-input API (S-8).
+            Evidence: actual module supplied examples in text/JSON and both option orders, Unicode Nd endpoints (`١:٢`, `１:２`), mixed ASCII/Unicode endpoints and leading zeros, numeric ordering across digit sets, signs/spaces/non-decimal numerals such as `²` rejected before acquisition, and endpoints longer than the interpreter decimal conversion limit (valid huge START/END, beyond-EOF and reversed values), repeated ranges in separate/equal/mixed spellings, all invalid categories with instrumented no acquisition, empty/beyond-EOF/CRLF/CR/LF/Unicode/BOM files, invalid UTF-8 after END, retained errors/defaults/help/dash filenames/unchanged files. Demonstrate useful 2:3 and beyond-EOF results and rejecting invalid syntax. Run nonempty independent unit/integration regressions.
             Completion evidence (2026-10-05): actual module RED observed 73 unknown-option failures across 2 test methods; after parser/composition implementation GREEN independent unit21/integration13 passed, no skips. Both range spellings/text/JSON/orders, ASCII/leading-zero/5000-digit endpoints, malformed/repeated ranges before acquisition, complete bad UTF-8 after END, BOM/Unicode/CRLF/EOF rows, file preservation and owned-handle/expected errors verified. API stays whole-input; no stdin delivered. `git diff --check` passed. #19 exact title and opening/closing task markers verified through readonly connector; maintained closure pending adapter facility resolution.
         - [x] T-020 — Document ranges and verify extracted-source acceptance
+            Completion reassessment pending (2026-10-05): T-020 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess public range syntax/examples and isolated extracted-source acceptance after T-019; existing README/module documentation and archive evidence at 749a89844249d3b1c5ebb04c459d7e66bcb3ed2e describe the ASCII-only grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-019.
             Scope: README.md, docs/module.md, docs/api.md accuracy review and tests/integration/test_distribution.py; existing Makefile recipe.
             Outcome: runnable named-file range examples, syntax/repetition/status/complete-decode/BOM rules and explicit stdin boundary; public API docs retain whole-input contract (S-8/S-7).
             Evidence: execute public examples/help, run independent nonempty product suites, clean archive extraction and actual extracted python -m textstats for both spellings/formats/BOM policies and representative usage/read/decode failures. Remove checkout import leakage, assert extracted package identity and unchanged input. Workflow fixtures remain separate.
             Completion evidence (2026-10-05): README/module named-file range examples, full syntax/repetition/status/decode/BOM/EOF rules and explicit stdin boundary added; API reviewed whole-input unchanged. Existing delivered behavior characterized, no production edit or manufactured RED. Extended isolated archive test passed with extracted import identity, both spellings/text/JSON/BOM orders, dash file and usage/read/late-decode errors; bytes unchanged. Independent unit21/integration13 passed, no skips; public fenced Python/shell examples executed in temporary directories with expected statuses, build/test blocks separately covered by suites. Diff check passed. #20 exact title/markers verified; hosted reconciliation pending unknown preHTTP adapter failure.
-        Completion evidence (2026-10-05): T018–T021 implementation, separate code review, unit21/integration13, public examples/isolated source checks and all PLAN2.4 exits verified. [Range milestone report](features/002_ea97182/2.4.md) records current acceptance. Hosted report/issue/milestone transitions are separately observed after publication; Phase2 remains incomplete.
+        Completion evidence (2026-10-05): T018–T021 implementation, separate code review, unit21/integration13, public examples/isolated source checks and all PLAN2.4 exits verified. [Range milestone report](features/002_ea97182/2.4.md) records historical ASCII acceptance. Hosted report/issue/milestone transitions are separately observed after publication; Phase2 remains incomplete.
         - [x] T-021 — Review, test and report range milestone 2.4
+            Completion reassessment pending (2026-10-05): T-021 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess milestone 2.4 code review, regressions, documentation/distribution and all revised exits after T-019/T-020; existing report at 3f93cd40d90001ee7e4f54b36c764d1d5067b72e and features/002_ea97182/2.4.md verify the prior ASCII grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: T-018, T-019, T-020.
             Scope: all named-file range behavior, helper/acquisition/CLI composition, API compatibility, docs/distribution and prior acceptance.
             Evidence: separate code review and focused/regression checks against all2.4 exits, useful demonstrations, required blocker repairs, TODO provenance and committed/pushed report. Reconcile issues and close2.4 only after all constituent issues are verified complete when tracking is active.
             Report: docs/dev/features/002_ea97182/2.4.md.
             Completion evidence (2026-10-05): [milestone code review/testing report](features/002_ea97182/2.4.md), reviewed749a898 plus accepted owner/docstring-only changes; independent unit21/integration13 no skips, public examples/links/diff check pass. No in-scope finding/TODO. Governing-owner incorporation/QC Ready; issue#21 exact title/markers verified, closure follows commit/push.
     - [x] Milestone 2.5 — Range feature review
+        Completion reassessment pending (2026-10-05): Milestone 2.5 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess revised Unicode Nd/mixed-decimal cross-component exits through T-022 after milestone 2.4; historical ASCII feature reports do not establish current completion. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
         Completion evidence (2026-10-05): T022 cross-component review, independent unit21/integration13, examples/links/archive and main owner QC verify scoped PLAN2.5 exits; [feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) retain TODO: None. Hosting closure follows publication; main Phase2 remains incomplete.
         - [x] T-022 — Review, test and report the named-file range feature
+            Completion reassessment pending (2026-10-05): T-022 acceptance changed by the accepted Unicode decimal endpoint requirement in [SPEC.md S-8](SPEC.md#s-8-named-file-line-selection), carried into PLAN 2.4/2.5. reassess feature cross-component review/final report after milestone 2.4; existing phase/implementation reports at d518cc23650018542e43d8fb5a63f44a4d283518 and features/002_ea97182/PHASE-REPORT.md verify the prior ASCII grammar. Checkbox and earlier evidence are preserved as historical; sdd-implement owns reassessment and any completion correction. No implementation or hosted reopening occurred in this incorporation.
             Depends on: feature milestone2.4 complete/closed when tracking is active, including T-021.
             Scope: cross-component S-8 and retained named-file S-1–S-5/S-7; feature-only phase/final report, not main T-017 or stdin acceptance.
             Evidence: separate feature phase code review, nonempty suites, API/default/format/BOM/decode/lifecycle regressions, runnable docs and extracted-source checks, blocker repair and final feature TODO aggregation with provenance/resolution references. Separately authorized full implementation incorporates accepted selected feature docs and reconciles task ownership/QC before final target merge and merged-state verification/publication; main Phase2 remains unfinished. No incorporation/merge/implementation during preparation.
@@ -145,6 +151,6 @@ Phase 1 working branch: `phase/1-named-file-utility`; integration target: `main`
 
 ## Range feature conclusion
 
-T-018–T-022 are verified completed on feature/002_ea97182-line-ranges. Governing owners and task ownership are reconciled; feature sources/adjacent QC are historical under [feature002_ea97182](features/002_ea97182/README.md). Fresh independent unit21/integration13, code review, public examples, links and diff checks establish named-file feature exits. [Feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) record evidence and TODO: None. 2.4/#7 closed with0open/4closed after report/status publication; 2.5/#8 closure follows T022 publication. Main Phase2, stdin2.2 and final2.3/T013–T017 remain unchecked; no Phase2→main integration is authorized here.
+T-018–T-022 have historical verified completion on feature/002_ea97182-line-ranges for the ASCII grammar. Current T-019–T-022 and milestone 2.4/2.5 claims are disputed by the owning Completion reassessment pending notes; T-018's source-independent seam acceptance is unchanged. Governing owners and task ownership are reconciled; feature sources/adjacent QC are historical under [feature002_ea97182](features/002_ea97182/README.md). Fresh independent unit21/integration13, code review, public examples, links and diff checks establish named-file feature exits. [Feature phase report](features/002_ea97182/PHASE-REPORT.md) and [implementation report](features/002_ea97182/IMPLEMENTATION-REPORT.md) record historical evidence and TODO: None for the prior acceptance, without establishing revised Unicode decimal acceptance. 2.4/#7 closed with0open/4closed after report/status publication; 2.5/#8 closure follows T022 publication. Main Phase2, stdin2.2 and final2.3/T013–T017 remain unchecked; no Phase2→main integration is authorized here.
 
 T-022 completion evidence (2026-10-05): reviewed full delivered production/test/docs/build boundaries separately from fresh unit21/integration13 (no skips), verified R1–R4/mainS8 and retained named-file/API/format/decode/BOM/resource/docs/distribution conditions. Sources and adjacent QC archived only after owner/task/evidence disposition; main owner QC rechecked, links/unique IDs/whitespace passed. No findings/TODO. #22 exact title/opening+closing markers verified; report/status push precedes issue/milestone closure and explicit feature integration.

```

Exit: 0

## Scoped document checks

Actual check source:

```python
from pathlib import Path
import hashlib,re,sys,subprocess
sys.path.insert(0,'/workspace/scratch')
from a022_acceptance_log import root,run,journal
owned=['docs/dev/ARCHITECTURE.md','docs/dev/DECOMPOSITION.md','docs/dev/PLAN.md','docs/dev/SPEC.md','docs/dev/TASKS.md','docs/dev/SPEC-REVIEW-REPORT.md','docs/dev/PLAN-REVIEW-REPORT.md','docs/dev/TASKS-REVIEW-REPORT.md']
changed=run(['git','--no-optional-locks','diff','--name-only']).splitlines()
assert set(changed)==set(owned),(changed,owned)
tasks=(root/'docs/dev/TASKS.md').read_text()
old=subprocess.check_output(['git','--no-optional-locks','show','0e4741465c3e086d2ab95c5af73ca89371c16fac:docs/dev/TASKS.md'],cwd=root,text=True)
check=lambda s:re.findall(r'^\s*- \[[ x]\].*$',s,re.M)
assert check(tasks)==check(old),'checklist identity/status changed'
ids=re.findall(r'^        - \[[ x]\] (T-\d+) —',tasks,re.M)
assert len(ids)==22 and len(set(ids))==22
pending=re.findall(r'^\s*Completion reassessment pending[^\n]+',tasks,re.M)
assert len(pending)==6
for task in ['T-019','T-020','T-021','T-022','Milestone 2.4','Milestone 2.5']:
 assert any(': '+task+' acceptance changed' in note for note in pending),task
assert '- [ ] Phase 2' in tasks and '- [ ] T-013' in tasks
spec=(root/'docs/dev/SPEC.md').read_text()
assert all(x in spec for x in ['Unicode category Nd','١:٢','１:２','1:٢','٠1:０２','`²`','START <= END','There is no arbitrary endpoint bound or digit-count limit.'])
assert 'Reject signs, whitespace, Unicode digits' not in spec
for path in owned:
 text=(root/path).read_text();lines=text.splitlines()
 for i,line in enumerate(lines):
  if re.match(r'^#{1,6} ',line):
   assert i==0 or not lines[i-1].strip(),(path,i,'heading preceding')
   assert i+1==len(lines) or not lines[i+1].strip(),(path,i,'heading following')
 for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
  if '://' in target or target.startswith('#'):continue
  assert (root/path).parent.joinpath(target.split('#')[0]).exists(),(path,target)
for report in ['SPEC','PLAN','TASKS']:
 text=(root/f'docs/dev/{report}-REVIEW-REPORT.md').read_text()
 latest=text.rsplit('## Revision ',1)[1]
 for path,digest in re.findall(r'- `([^`]+)`: SHA-256 `([a-f0-9]{64})`',latest):
  assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,(report,path)
# Verify immutable package and all production/tests/public docs against baseline without executing product code.
run(['git','--no-optional-locks','diff','--exit-code','0e4741465c3e086d2ab95c5af73ca89371c16fac','--','textstats-run-resources','textstats','tests','README.md','docs/module.md','docs/api.md','Makefile'])
run(['git','--no-optional-locks','diff','--check'])
run(['git','--no-optional-locks','diff','--',*owned])
with journal.open('a') as f:
 f.write('\n## Scoped document checks\n\nActual check source:\n\n```python\n'+Path(__file__).read_text()+'\n```\n\nResult: PASS. Exactly eight owned document changes;22 unique stable task entries and identical complete checkbox lines;6 current pending reassessments; revised examples/Nd/rejection/unbounded requirements; all changed-file heading spacing/local links; current QC artifact/upstream hashes; production/tests/public docs/frozen resources unchanged; git diff --check passes. No product tests or implementation.\n')
 for path in owned:
  f.write('\nFinal owned '+str(root/path)+' SHA-256 `'+hashlib.sha256((root/path).read_bytes()).hexdigest()+'`.\n')
print('PASS: owned paths, exact status preservation, 22 unique task IDs, 6 pending notes, Nd acceptance, local links, spacing, current hashes, unchanged source/tests/frozen package, diff whitespace.')

```

Result: PASS. Exactly eight owned document changes;22 unique stable task entries and identical complete checkbox lines;6 current pending reassessments; revised examples/Nd/rejection/unbounded requirements; all changed-file heading spacing/local links; current QC artifact/upstream hashes; production/tests/public docs/frozen resources unchanged; git diff --check passes. No product tests or implementation.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/ARCHITECTURE.md SHA-256 `36d791fca787c60328cec8fa0742201a48ab5a6862ded6707c4c7ce3bd809505`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/DECOMPOSITION.md SHA-256 `4f2faa1123b65e7c83909d3d4e5a6d310b4210809975ef9e5be013b25ed59a8c`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/PLAN.md SHA-256 `a9b95ee565598935497fd0fbefd0fc19459b66c67443358544285d86b9fdea58`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/SPEC.md SHA-256 `9e58d8f5debc1ddb830fa63ed5860804df06954a38187ccb157200be7db1660b`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/TASKS.md SHA-256 `d00709492e31f9019a4da6fff98906940b05e2f6a91bca58cb14038c366193db`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/SPEC-REVIEW-REPORT.md SHA-256 `1e1e340f2bd79d2aeff48ced35e317920bf38445cb9fa76f8c79ca1143e137ef`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/PLAN-REVIEW-REPORT.md SHA-256 `2132c2fd328d4b79d019bbda5b6f8500286c8db659c0338cbebdae59adc13ef3`.

Final owned /workspace/scratch/textstats-acceptance-change-worktree-20261005/docs/dev/TASKS-REVIEW-REPORT.md SHA-256 `9c8b3ff302d556a3a9afbb6538438d1abe9daa29790287774ecfc38203718f26`.

### Command ['rg', '--files', 'textstats-run-resources', '-g', '!skills/**']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
textstats-run-resources/HARNESS-SOURCE.json
textstats-run-resources/PLUGIN-SOURCE.json
textstats-run-resources/SETUP.md
textstats-run-resources/plugin/skills/sdd-implement/SKILL.md
textstats-run-resources/plugin/skills/sdd-implement/references/completion-and-checkpoints.md
textstats-run-resources/plugin/skills/sdd-implement/references/range-selection.md
textstats-run-resources/plugin/skills/sdd-implement/references/task-execution.md
textstats-run-resources/plugin/skills/sdd-implement/references/startup-and-continuation.md
textstats-run-resources/plugin/skills/sdd-implement/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-implement/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-specify/SKILL.md
textstats-run-resources/plugin/skills/sdd-specify/references/system-specification.md
textstats-run-resources/plugin/skills/sdd-specify/references/change-specification.md
textstats-run-resources/plugin/skills/sdd-specify/references/review.md
textstats-run-resources/plugin/skills/sdd-specify/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-specify/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-forge/SKILL.md
textstats-run-resources/plugin/skills/sdd-forge/references/github.md
textstats-run-resources/plugin/skills/sdd-forge/references/github-milestone-lifecycle.md
textstats-run-resources/plugin/skills/sdd-forge/references/github-issue-lifecycle.md
textstats-run-resources/plugin/skills/sdd-forge/references/github-projection.md
textstats-run-resources/plugin/skills/sdd-forge/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-forge/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-orient/SKILL.md
textstats-run-resources/plugin/skills/sdd-orient/references/inspection-and-handoff.md
textstats-run-resources/plugin/skills/sdd-orient/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-orient/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-plan/SKILL.md
textstats-run-resources/plugin/skills/sdd-plan/references/delivery-plan.md
textstats-run-resources/plugin/skills/sdd-plan/references/review.md
textstats-run-resources/plugin/skills/sdd-plan/references/physical-layout.md
textstats-run-resources/plugin/skills/sdd-plan/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-plan/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-integrate-feature/SKILL.md
textstats-run-resources/plugin/skills/sdd-integrate-feature/references/feature-incorporation.md
textstats-run-resources/plugin/skills/sdd-integrate-feature/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-integrate-feature/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-docs/SKILL.md
textstats-run-resources/plugin/skills/sdd-docs/references/in-code-documentation.md
textstats-run-resources/plugin/skills/sdd-docs/references/standalone-documentation.md
textstats-run-resources/plugin/skills/sdd-docs/references/review-and-findings.md
textstats-run-resources/plugin/skills/sdd-docs/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-docs/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-tasks/SKILL.md
textstats-run-resources/plugin/skills/sdd-tasks/references/conformance-review.md
textstats-run-resources/plugin/skills/sdd-tasks/references/task-derivation.md
textstats-run-resources/plugin/skills/sdd-tasks/references/progress-review.md
textstats-run-resources/plugin/skills/sdd-tasks/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-verify/SKILL.md
textstats-run-resources/plugin/skills/sdd-tasks/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-report/SKILL.md
textstats-run-resources/plugin/skills/sdd-verify/references/boundary-review.md
textstats-run-resources/plugin/skills/sdd-verify/references/check-selection.md
textstats-run-resources/plugin/skills/sdd-verify/references/execution-and-evidence.md
textstats-run-resources/plugin/skills/sdd-verify/references/failure-assessment.md
textstats-run-resources/plugin/skills/sdd-report/references/completion-reports.md
textstats-run-resources/plugin/skills/sdd-report/references/change-kinds.md
textstats-run-resources/plugin/skills/sdd-report/references/document-qc-reports.md
textstats-run-resources/plugin/skills/sdd-report/references/campaign-artifacts.md
textstats-run-resources/plugin/skills/sdd-report/references/object-drafts.md
textstats-run-resources/plugin/skills/sdd-verify/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-report/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-verify/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-manage/SKILL.md
textstats-run-resources/plugin/skills/sdd-conventions/SKILL.md
textstats-run-resources/plugin/skills/sdd-report/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-conventions/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-conventions/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-tdd/SKILL.md
textstats-run-resources/plugin/skills/sdd-conventions/references/review-campaigns.md
textstats-run-resources/plugin/skills/sdd-conventions/references/task-hierarchy.md
textstats-run-resources/plugin/skills/sdd-conventions/references/design-heuristics.md
textstats-run-resources/plugin/skills/sdd-conventions/references/workflow-identity.md
textstats-run-resources/plugin/skills/sdd-conventions/references/modularity.md
textstats-run-resources/plugin/skills/sdd-conventions/references/hosting-tokens.md
textstats-run-resources/plugin/skills/sdd-conventions/references/development-document-qc.md
textstats-run-resources/plugin/skills/sdd-conventions/references/backend-object-lifecycle.md
textstats-run-resources/plugin/assets/logo.png
textstats-run-resources/plugin/assets/AI_DISCLOSURE.md
textstats-run-resources/plugin/assets/icon.svg
textstats-run-resources/plugin/assets/SDD-MANAGER.md
textstats-run-resources/plugin/skills/sdd-manage/references/git-workflows.md
textstats-run-resources/plugin/skills/sdd-manage/references/document-qc-gates.md
textstats-run-resources/plugin/skills/sdd-manage/references/coordination.md
textstats-run-resources/plugin/skills/sdd-manage/references/examples.md
textstats-run-resources/plugin/skills/sdd-manage/references/workflows.md
textstats-run-resources/plugin/skills/sdd-design/SKILL.md
textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md
textstats-run-resources/plugin/skills/sdd-manage/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-design/references/decomposition.md
textstats-run-resources/plugin/skills/sdd-manage/references/phase-activation.md
textstats-run-resources/plugin/skills/sdd-manage/references/review-and-revision.md
textstats-run-resources/plugin/skills/sdd-manage/references/credentials.md
textstats-run-resources/plugin/skills/sdd-manage/references/branch-management.md
textstats-run-resources/plugin/skills/sdd-manage/references/repository-bootstrap.md
textstats-run-resources/plugin/skills/sdd-tdd/LICENSE
textstats-run-resources/plugin/skills/sdd-tdd/references/test-first-cycle.md
textstats-run-resources/plugin/skills/sdd-tdd/references/upstream-provenance.md
textstats-run-resources/plugin/skills/sdd-tdd/references/testing-strategy.md
textstats-run-resources/plugin/skills/sdd-tdd/references/writing-good-tests.md
textstats-run-resources/plugin/skills/sdd-design/references/exploration.md
textstats-run-resources/plugin/skills/sdd-design/references/architecture.md
textstats-run-resources/plugin/skills/sdd-manage/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-tdd/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-design/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-tdd/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-design/assets/icon.svg
textstats-run-resources/plugin/skills/sdd-steer/SKILL.md
textstats-run-resources/plugin/skills/sdd-steer/references/objective-and-impact.md
textstats-run-resources/plugin/skills/sdd-steer/references/amendment-execution.md
textstats-run-resources/plugin/skills/sdd-steer/references/verification-and-stop.md
textstats-run-resources/plugin/skills/sdd-steer/agents/openai.yaml
textstats-run-resources/plugin/skills/sdd-steer/assets/icon.svg

```

Exit: 0

### Command ['rg', '-n', '019eb354cf0921ebd6056e6579763ac33d0baec2', 'textstats-run-resources']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
textstats-run-resources/SETUP.md:3:Pinned source: 019eb354cf0921ebd6056e6579763ac33d0baec2. Resources are coordinator infrastructure, not generated TextStats product implementation. Existing README retained. Product consumers use plugin/skills only; the harness is published on a separate evidence branch and is assessor/coordinator material.
textstats-run-resources/HARNESS-SOURCE.json:2:  "commit": "019eb354cf0921ebd6056e6579763ac33d0baec2",
textstats-run-resources/PLUGIN-SOURCE.json:3:  "commit": "019eb354cf0921ebd6056e6579763ac33d0baec2",
textstats-run-resources/PLUGIN-SOURCE.json:232:  "revision": "019eb354cf0921ebd6056e6579763ac33d0baec2",

```

Exit: 0

### Loaded /workspace/scratch/textstats-acceptance-change-worktree-20261005/textstats-run-resources/PLUGIN-SOURCE.json

SHA-256 `dc9a100b8eda35f908b0cbbb4b6dc4d4b449d07723bf9ae8d52868c773bacea2`

```json
{
  "changed_package_paths": [],
  "commit": "019eb354cf0921ebd6056e6579763ac33d0baec2",
  "fingerprint": "33d65ea05b3299f1c2348802f95d1767dbccd5f72f4537a8ced52eaa1608fafd",
  "manifest_path": "/workspace/scratch/textstats-live-20261004/textstats-run-resources/PLUGIN-SOURCE.json",
  "package_file_modes": {
    ".codex-plugin/plugin.json": "100644",
    "assets/AI_DISCLOSURE.md": "100644",
    "assets/SDD-MANAGER.md": "100644",
    "assets/icon.svg": "100644",
    "assets/logo.png": "100644",
    "skills/sdd-conventions/SKILL.md": "100644",
    "skills/sdd-conventions/agents/openai.yaml": "100644",
    "skills/sdd-conventions/assets/icon.svg": "100644",
    "skills/sdd-conventions/references/backend-object-lifecycle.md": "100644",
    "skills/sdd-conventions/references/design-heuristics.md": "100644",
    "skills/sdd-conventions/references/development-document-qc.md": "100644",
    "skills/sdd-conventions/references/hosting-tokens.md": "100644",
    "skills/sdd-conventions/references/modularity.md": "100644",
    "skills/sdd-conventions/references/review-campaigns.md": "100644",
    "skills/sdd-conventions/references/task-hierarchy.md": "100644",
    "skills/sdd-conventions/references/workflow-identity.md": "100644",
    "skills/sdd-design/SKILL.md": "100644",
    "skills/sdd-design/agents/openai.yaml": "100644",
    "skills/sdd-design/assets/icon.svg": "100644",
    "skills/sdd-design/references/architecture.md": "100644",
    "skills/sdd-design/references/decomposition.md": "100644",
    "skills/sdd-design/references/exploration.md": "100644",
    "skills/sdd-docs/SKILL.md": "100644",
    "skills/sdd-docs/agents/openai.yaml": "100644",
    "skills/sdd-docs/assets/icon.svg": "100644",
    "skills/sdd-docs/references/in-code-documentation.md": "100644",
    "skills/sdd-docs/references/review-and-findings.md": "100644",
    "skills/sdd-docs/references/standalone-documentation.md": "100644",
    "skills/sdd-forge/SKILL.md": "100644",
    "skills/sdd-forge/agents/openai.yaml": "100644",
    "skills/sdd-forge/assets/icon.svg": "100644",
    "skills/sdd-forge/references/github-issue-lifecycle.md": "100644",
    "skills/sdd-forge/references/github-milestone-lifecycle.md": "100644",
    "skills/sdd-forge/references/github-projection.md": "100644",
    "skills/sdd-forge/references/github.md": "100644",
    "skills/sdd-implement/SKILL.md": "100644",
    "skills/sdd-implement/agents/openai.yaml": "100644",
    "skills/sdd-implement/assets/icon.svg": "100644",
    "skills/sdd-implement/references/completion-and-checkpoints.md": "100644",
    "skills/sdd-implement/references/range-selection.md": "100644",
    "skills/sdd-implement/references/startup-and-continuation.md": "100644",
    "skills/sdd-implement/references/task-execution.md": "100644",
    "skills/sdd-integrate-feature/SKILL.md": "100644",
    "skills/sdd-integrate-feature/agents/openai.yaml": "100644",
    "skills/sdd-integrate-feature/assets/icon.svg": "100644",
    "skills/sdd-integrate-feature/references/feature-incorporation.md": "100644",
    "skills/sdd-manage/SKILL.md": "100644",
    "skills/sdd-manage/agents/openai.yaml": "100644",
    "skills/sdd-manage/assets/icon.svg": "100644",
    "skills/sdd-manage/references/branch-management.md": "100644",
    "skills/sdd-manage/references/coordination.md": "100644",
    "skills/sdd-manage/references/credentials.md": "100644",
    "skills/sdd-manage/references/document-qc-gates.md": "100644",
    "skills/sdd-manage/references/examples.md": "100644",
    "skills/sdd-manage/references/git-workflows.md": "100644",
    "skills/sdd-manage/references/phase-activation.md": "100644",
    "skills/sdd-manage/references/repository-bootstrap.md": "100644",
    "skills/sdd-manage/references/review-and-revision.md": "100644",
    "skills/sdd-manage/references/revision-authorization.md": "100644",
    "skills/sdd-manage/references/workflows.md": "100644",
    "skills/sdd-orient/SKILL.md": "100644",
    "skills/sdd-orient/agents/openai.yaml": "100644",
    "skills/sdd-orient/assets/icon.svg": "100644",
    "skills/sdd-orient/references/inspection-and-handoff.md": "100644",
    "skills/sdd-plan/SKILL.md": "100644",
    "skills/sdd-plan/agents/openai.yaml": "100644",
    "skills/sdd-plan/assets/icon.svg": "100644",
    "skills/sdd-plan/references/delivery-plan.md": "100644",
    "skills/sdd-plan/references/physical-layout.md": "100644",
    "skills/sdd-plan/references/review.md": "100644",
    "skills/sdd-report/SKILL.md": "100644",
    "skills/sdd-report/agents/openai.yaml": "100644",
    "skills/sdd-report/assets/icon.svg": "100644",
    "skills/sdd-report/references/campaign-artifacts.md": "100644",
    "skills/sdd-report/references/change-kinds.md": "100644",
    "skills/sdd-report/references/completion-reports.md": "100644",
    "skills/sdd-report/references/document-qc-reports.md": "100644",
    "skills/sdd-report/references/object-drafts.md": "100644",
    "skills/sdd-specify/SKILL.md": "100644",
    "skills/sdd-specify/agents/openai.yaml": "100644",
    "skills/sdd-specify/assets/icon.svg": "100644",
    "skills/sdd-specify/references/change-specification.md": "100644",
    "skills/sdd-specify/references/review.md": "100644",
    "skills/sdd-specify/references/system-specification.md": "100644",
    "skills/sdd-steer/SKILL.md": "100644",
    "skills/sdd-steer/agents/openai.yaml": "100644",
    "skills/sdd-steer/assets/icon.svg": "100644",
    "skills/sdd-steer/references/amendment-execution.md": "100644",
    "skills/sdd-steer/references/objective-and-impact.md": "100644",
    "skills/sdd-steer/references/verification-and-stop.md": "100644",
    "skills/sdd-tasks/SKILL.md": "100644",
    "skills/sdd-tasks/agents/openai.yaml": "100644",
    "skills/sdd-tasks/assets/icon.svg": "100644",
    "skills/sdd-tasks/references/conformance-review.md": "100644",
    "skills/sdd-tasks/references/progress-review.md": "100644",
    "skills/sdd-tasks/references/task-derivation.md": "100644",
    "skills/sdd-tdd/LICENSE": "100644",
    "skills/sdd-tdd/SKILL.md": "100644",
    "skills/sdd-tdd/agents/openai.yaml": "100644",
    "skills/sdd-tdd/assets/icon.svg": "100644",
    "skills/sdd-tdd/references/test-first-cycle.md": "100644",
    "skills/sdd-tdd/references/testing-strategy.md": "100644",
    "skills/sdd-tdd/references/upstream-provenance.md": "100644",
    "skills/sdd-tdd/references/writing-good-tests.md": "100644",
    "skills/sdd-verify/SKILL.md": "100644",
    "skills/sdd-verify/agents/openai.yaml": "100644",
    "skills/sdd-verify/assets/icon.svg": "100644",
    "skills/sdd-verify/references/boundary-review.md": "100644",
    "skills/sdd-verify/references/check-selection.md": "100644",
    "skills/sdd-verify/references/execution-and-evidence.md": "100644",
    "skills/sdd-verify/references/failure-assessment.md": "100644"
  },
  "package_hashes": {
    ".codex-plugin/plugin.json": "eeb08ba49f7c8d58c0af38057411475a89a6d4a1536b850230a716232b7083df",
    "assets/AI_DISCLOSURE.md": "09411dc61f4966efabe8e821f2270c768baf5b96f4fd4587eb5c05233de7ffea",
    "assets/SDD-MANAGER.md": "07947f37a7a69fdfe45331d51e46d21267297e9fc547c84448949e711469403b",
    "assets/icon.svg": "78e8e4a4c1225f96d4f2d6577736ecf431cdc8be09730e3cb063f3ed6436fb87",
    "assets/logo.png": "e4a01cfa8c3712ff7e4ab3bd65bd58687c3aaa6d55b6af486cd632edee7a6d45",
    "skills/sdd-conventions/SKILL.md": "f441da1bfc36aaedceec0cb18838dc5496ea70e198edfa1ba66027bcbc619f0a",
    "skills/sdd-conventions/agents/openai.yaml": "3afb66258ca9ee5f7e35b0986ac130e34a4a73c4d5c41b1c7de94e19133e4cea",
    "skills/sdd-conventions/assets/icon.svg": "5702cda32d79bc28857dedfe0f9811d382d8b2e4c46d1ac571d8114aabd279a4",
    "skills/sdd-conventions/references/backend-object-lifecycle.md": "8729f0f62f649509080018ebf43aa2f5e7f710939ed182494460c23a0d9a0685",
    "skills/sdd-conventions/references/design-heuristics.md": "b4ded8adbaa45a74858cff4dbed277936d52d31a91534ab303b6af018262a448",
    "skills/sdd-conventions/references/development-document-qc.md": "c108f60ddffee2665d759276b650a430fde1abad4361bafa20311b63f077429f",
    "skills/sdd-conventions/references/hosting-tokens.md": "54f2e5949ddeae7aafcb985092309676b42b358135d8fea29481fc8071336324",
    "skills/sdd-conventions/references/modularity.md": "98d41ef9fb16f373ca2fddfe2c048775a40165823dd503d4df58c18654b11283",
    "skills/sdd-conventions/references/review-campaigns.md": "88ca8f7012e2e6255b4f8b0f41a2bf68b9fd3f5b3b205f7c7f7eda91f003f0bc",
    "skills/sdd-conventions/references/task-hierarchy.md": "675d67a8a7487c7876e084276638a966072d177f56376d3c156eec29c9b90a75",
    "skills/sdd-conventions/references/workflow-identity.md": "7192602affb35813b9ec052e87d3614b15098b779a8e1c104b1f723e1f6f531a",
    "skills/sdd-design/SKILL.md": "bacf686f53b4f2e1a759624ddd70ae34cd6b55ed51c3dd5e1a6624eb0ea028aa",
    "skills/sdd-design/agents/openai.yaml": "102d11e8960f1f7af69bfcbacbe71defad289b9c368d11a610fb6b19e61dd3b6",
    "skills/sdd-design/assets/icon.svg": "98c55eb98b3e3702037698739b96fb550da2223bf733fb576650d0a4c5504864",
    "skills/sdd-design/references/architecture.md": "329327e9cadf2637289dcad8808faa0a31c7e386223accb91366b897ef64339b",
    "skills/sdd-design/references/decomposition.md": "eac648372c44883068569a13a2715cb7d7b4d84e26f7c4de20478f93bb124abf",
    "skills/sdd-design/references/exploration.md": "54d5b0262975a3a4981deb5717ca7cb0e87817cd54b2a51e10d6d6fa7eb1d209",
    "skills/sdd-docs/SKILL.md": "561a9f9935357e3cb82e3110868571632f3b3a01ad4ddebc654232086d33f659",
    "skills/sdd-docs/agents/openai.yaml": "9715602c3bdcd14d41e6e99e24edb32389499e0ec96b0aad5cdf4b30b187de15",
    "skills/sdd-docs/assets/icon.svg": "69e272ee97e9957387f8ca8b51bec3d3d176c33e6bf6b20d2bff5b3536f507e2",
    "skills/sdd-docs/references/in-code-documentation.md": "95312201830c2006a68661142cdbc2fcd313282f2b318a0bceee6ef854990d82",
    "skills/sdd-docs/references/review-and-findings.md": "2c678bfc1facfdb4ba0b470c96137454cd68fc3518c53227f9e9bd09a7bcb39a",
    "skills/sdd-docs/references/standalone-documentation.md": "82115d3d727ecde42593782cc161c8923299303fc1439eff3b4a14c8aab52cf4",
    "skills/sdd-forge/SKILL.md": "21cba41d7d64fc54206dc981fab665b16b7b868e4fe1c75769048a59b294b9b4",
    "skills/sdd-forge/agents/openai.yaml": "303dd1fd13c645d36bac324e76198629bb567a245a360955e447612487aa1ca3",
    "skills/sdd-forge/assets/icon.svg": "ca997d09da83d706126f43dc2ace19c00ee9036ae67dcce225e688a09d398d33",
    "skills/sdd-forge/references/github-issue-lifecycle.md": "73288c6f708bc36734fae4dff77c6a3dc44b4d804083b30d832441cf494ab896",
    "skills/sdd-forge/references/github-milestone-lifecycle.md": "879e7a70f56e50c9178cf0d8142d2bbbfb4710c686e3c25cae4e67e85f867fe0",
    "skills/sdd-forge/references/github-projection.md": "7124759c2c3aa98d909d62b64db302d76d65ed35701ec22d47cc6a20a38d17a8",
    "skills/sdd-forge/references/github.md": "a3aaa97b52374db1b21e8e0fc2a8b87d8462e8703cad1336008cf990bb0e9770",
    "skills/sdd-implement/SKILL.md": "ca32a423668d4749f0ec9c463f3ae597ba2e3def51eb3333912133f397e11df0",
    "skills/sdd-implement/agents/openai.yaml": "438f0f659f42428e943046f75e10eb5b21384802baf3ce8eb010b9598d00cb7b",
    "skills/sdd-implement/assets/icon.svg": "4fd314a8f182561a13fbf6fe062e4aee5fd0e0330dccd9943ec14aa5dab34c48",
    "skills/sdd-implement/references/completion-and-checkpoints.md": "9cb68ab3573e670f71134f1a42ae61c254d31493f28d45b4d141c637fb0d7ac6",
    "skills/sdd-implement/references/range-selection.md": "092f930702c80eccaee732c252c1c68bbfaeaa8be78386b5f688d1509274a5e9",
    "skills/sdd-implement/references/startup-and-continuation.md": "fe986a81b9e0344340754775675280b55c851873c9a7dfdfc8c3835fb8dce373",
    "skills/sdd-implement/references/task-execution.md": "0da734c6682c8088af89fb5da78474b78e65e3d7cf35deca83b2e86aace720b5",
    "skills/sdd-integrate-feature/SKILL.md": "62bbe9725faada9934eea8ce29a6ab0bc40462747a1e49243c2d48331ca05bc9",
    "skills/sdd-integrate-feature/agents/openai.yaml": "48018ed1de138598f6be61e916b701638234e2d0e570ed42d39760e0f4de8392",
    "skills/sdd-integrate-feature/assets/icon.svg": "9b68ea07e6b5916efa646ad8f639cb1872523bb40630043a317cc862440dc006",
    "skills/sdd-integrate-feature/references/feature-incorporation.md": "52e311b66d7df21bea7f2c02463417d7219dabe844e2c98cafe03f0cb1aa7e30",
    "skills/sdd-manage/SKILL.md": "b826b549817648a7ab0ce68f324b0d8158d4ede6b687e4034cb664306256cd3e",
    "skills/sdd-manage/agents/openai.yaml": "c3d318cf2a1074db8bc3c956109b12b1a3399c3835eded7bbac57f9ee7f5a778",
    "skills/sdd-manage/assets/icon.svg": "d263da0cf62afe30dec52294f51c33a0d522b25c44049224a2274037e8ace44d",
    "skills/sdd-manage/references/branch-management.md": "7f5fa93c685e8983efe72711f3ee6673dac6e9c6125406e23415a88e452dcb34",
    "skills/sdd-manage/references/coordination.md": "71228af38e0c333ae5ac5aa671d5df5370589dc131cca4ee336f28189fd46183",
    "skills/sdd-manage/references/credentials.md": "5d33060db46a9ddb1f0581944da960813bf9e548169bf73625d3e3d6a4c3a795",
    "skills/sdd-manage/references/document-qc-gates.md": "5f776622a41d2a9040b39c3800663532899d68bce10c204ce7564ed57a2c7f90",
    "skills/sdd-manage/references/examples.md": "96eebdfe90f270cff46bdd4f69d596fd439acbb7d4ea8633e91772a74b1e5acd",
    "skills/sdd-manage/references/git-workflows.md": "2f712ad70cbfc187f91517d9d9a8799340439996850d5557bfa5c61de4ad8ac7",
    "skills/sdd-manage/references/phase-activation.md": "fad5b5c71c8b58e19b94f61f494e31901d5d5a2cc262ab72944dca17e1891559",
    "skills/sdd-manage/references/repository-bootstrap.md": "01032399eb4422ac61a6b3934912ee8392f2b043a187459bd261dba6ddc4f7d5",
    "skills/sdd-manage/references/review-and-revision.md": "df7f820cb4decccbc1d077ce80ded8b745b1a10c2d813b7011fa8c0dc16d6114",
    "skills/sdd-manage/references/revision-authorization.md": "0f2db55e9bc50fe3f782c215884a52f8027e654367b8cf8bd6f8207215ca88df",
    "skills/sdd-manage/references/workflows.md": "8ca466b140717b3cd8a33ea5fb1b9aafa8aa4fd696c8bee2455ef3edcf1912c2",
    "skills/sdd-orient/SKILL.md": "91eeed3179358cb50e908a24ef83a2de9cc46dca7bf833509654b4bd04c66791",
    "skills/sdd-orient/agents/openai.yaml": "36dbb7990b7f504c1fa4b614651ad26431ab6af5a623be8250b780ce156667c9",
    "skills/sdd-orient/assets/icon.svg": "ef235e59b6a56e0d21629b3b6c1b2ca9cc97cd678d02bcb31b0e2f7bc11bf1f2",
    "skills/sdd-orient/references/inspection-and-handoff.md": "1df6b1c7a972959a4b6fb5820ac2a8fbefe732b6abfdef1d52c319811777502f",
    "skills/sdd-plan/SKILL.md": "816cc68dc8322ec0a9a1fb6c2bd1a1da648ed0447ca48037d0804e0e847ad2d3",
    "skills/sdd-plan/agents/openai.yaml": "8672b642e8c5ae2114cd839af1152435c7da485b4a25c3dd62d15c78d124ac98",
    "skills/sdd-plan/assets/icon.svg": "44568c513e736771f4dde159c1903c6da19a774474ce65aeb8992dd694706659",
    "skills/sdd-plan/references/delivery-plan.md": "b757fd076dc35d419a85c64fe7ea1e38c2fa78c493b5c2b19b094cf7f5b8416a",
    "skills/sdd-plan/references/physical-layout.md": "14f3ef1e83e8d810b6fd65857aa5b63edbe28ad24982ab639f31210d4e984dd5",
    "skills/sdd-plan/references/review.md": "3500dd799e477807deee44e9e4a436626f22b8ce8bf91f1c7b8d3e1aa065c931",
    "skills/sdd-report/SKILL.md": "481bec03eb256c70cabfc55ea7adca1626b940fa115e879f82e9de368a335a63",
    "skills/sdd-report/agents/openai.yaml": "bfe1a84a61bf154a5cb846d41b10d73e88a596044d21e6d1f151d1dc78ae221c",
    "skills/sdd-report/assets/icon.svg": "aca30e96cbe5d44d759da47cc1db33c87dce1d04bf77142feac8475eecbab074",
    "skills/sdd-report/references/campaign-artifacts.md": "e9ba5c14d03544c518b035f71c0725616e1a1dc28c004ba8e8b4d59aa5d87783",
    "skills/sdd-report/references/change-kinds.md": "51ebff15a54a17b885cf7835474334da7e285823a0113e9c56ebd5bff4769597",
    "skills/sdd-report/references/completion-reports.md": "1ed1bd98e8e78c0d22b049fa57843e87e4a740bd1415a7840b894493a7bffb46",
    "skills/sdd-report/references/document-qc-reports.md": "fe09d71b27a70ef806898634c8bd7b32b12b0d425006e5b4c47a5b551e426e07",
    "skills/sdd-report/references/object-drafts.md": "f0c894eb233713f18cb48ac2a1f8ecea474c7891276f948443b8cc16462391fc",
    "skills/sdd-specify/SKILL.md": "7b2fc98175350c9a5385e779cccaf93a7207ac429d4b3302b2c88b1dbd395fa9",
    "skills/sdd-specify/agents/openai.yaml": "c61e7eb38f097029d947314b441959b17aae2303440a52022cd386d78171e6b5",
    "skills/sdd-specify/assets/icon.svg": "ebeaf7c64a2fb958088765c46c48e8269625f03ddccefec9dc7b76ff7379f2ad",
    "skills/sdd-specify/references/change-specification.md": "74ad9a214189fa094c48acfd6c1daacb4eef43fe64ea18946ff5e6628a3be94c",
    "skills/sdd-specify/references/review.md": "60ef1b66449b4f40adf88f475fa4767cfd663d17ba4cd304236e8dfcb79500c9",
    "skills/sdd-specify/references/system-specification.md": "4af4ac610c2e6b020c57182e486d55124142394f9ba341db0b81339404723afd",
    "skills/sdd-steer/SKILL.md": "fcd5c2ea4a6eb877ceadadc7211e82f7d9abf1e76a4d8f1b381b369d9b286162",
    "skills/sdd-steer/agents/openai.yaml": "421038f108a077de64e16c95011ed4f6bff87d47e16c53894bbcc0dc581cc4ae",
    "skills/sdd-steer/assets/icon.svg": "b9d353ce223194b53f52a4853ed1cc9468718ed0ee57074b5988a309f54d14d1",
    "skills/sdd-steer/references/amendment-execution.md": "c185174fd72625f51a151bb6085140e9599f848e26f461d1131c87f2865d0cac",
    "skills/sdd-steer/references/objective-and-impact.md": "f1f57ab732b6c40c14260ab006377504bece4993bd7a80dac3d2adc53c9902ec",
    "skills/sdd-steer/references/verification-and-stop.md": "1905da31e42fc0ab565fe67fe789e43be426787710bf58e500dc11bf1b8e2b4a",
    "skills/sdd-tasks/SKILL.md": "c669a4c270f8c7ffedaff6cc456c0dbaf7a24020bb4830357f32d0e8883cc800",
    "skills/sdd-tasks/agents/openai.yaml": "60b43614f445a40f3d52d21869962189bdfe0252461317a6712a55d176797aa2",
    "skills/sdd-tasks/assets/icon.svg": "dad3203c0386ce1a697600ae82fc1e03f530111626192018df24dd7c5ac69eb0",
    "skills/sdd-tasks/references/conformance-review.md": "79e186c004f57193bf7a9ca8aaf7b6075d85fac240ae05a1ececa11ec7eea92e",
    "skills/sdd-tasks/references/progress-review.md": "32be8fbaa5e67e807d7c7f7be964c56ab7f65bd6398784606090fcdd9e40a912",
    "skills/sdd-tasks/references/task-derivation.md": "2d232e7e314dd2ccbe3eed3a16c0ec9e06ca56f5c5d3f58756fe902b95f56711",
    "skills/sdd-tdd/LICENSE": "a37e0e9697144819e1d965176ac4ae5bc3fa02d11e7812036bbcadf6dafe2400",
    "skills/sdd-tdd/SKILL.md": "adc0c2c0f7bc3cc7612dfc781ee8681289b1542aae8eba0bb6d99361a3a903ed",
    "skills/sdd-tdd/agents/openai.yaml": "f0049fe541cbffe331d4ccb9e903ed49bb96f1011cefecd1ced49fbd1bd19da4",
    "skills/sdd-tdd/assets/icon.svg": "37e86ed29c77f13846f9c315627c5e139d1348d7eed26eef2ff94354c334239f",
    "skills/sdd-tdd/references/test-first-cycle.md": "e8d797ba50e555d53500516e85f8b624f7ed11f5a7534e39220f2a74141e3d96",
    "skills/sdd-tdd/references/testing-strategy.md": "2ed2ba4a226e88a6dfd0dce41bc5f3f4f56942e28b7d032b5bb936c5ff268880",
    "skills/sdd-tdd/references/upstream-provenance.md": "668d85251c25027ac1494c9bb89367fa3c1885c23424e3987d02f7fd0b02ca33",
    "skills/sdd-tdd/references/writing-good-tests.md": "c5a555443dc5cf3b78312f9939bfbe53be7b04978f4f14f3350820ed5bc5b0d8",
    "skills/sdd-verify/SKILL.md": "fe02f63973521e86fa68a5fd775d01ab41fe7a797d26d8ae59dfa05bb25152ac",
    "skills/sdd-verify/agents/openai.yaml": "3176532ba151974e4f6186c589a9e8ba59247367629ace97788cf70e1bdfe40a",
    "skills/sdd-verify/assets/icon.svg": "60c4fbc478c5c5569c7db40ee7d2b90c061fb8e0b7a2274ec8757cbcadc6c837",
    "skills/sdd-verify/references/boundary-review.md": "53babcce80c31cefb2396f490332cdb3e0ca4e4472fdf3ba4eec189aa2f9ffc0",
    "skills/sdd-verify/references/check-selection.md": "27a9bcf8babe88b0d72956a2774e5e45a5cfd3316d009c955f450a2ef8fb1b34",
    "skills/sdd-verify/references/execution-and-evidence.md": "ad1dcdeca15cc67179f1923f74f044d4e6304dbf1195afff9f93dba885054a29",
    "skills/sdd-verify/references/failure-assessment.md": "0d1297f0b6d03dfd429c9d8e0d912c841801b8207141651aca1f1a90fe9a12c6"
  },
  "revision": "019eb354cf0921ebd6056e6579763ac33d0baec2",
  "snapshot_path": "/workspace/scratch/textstats-live-20261004/textstats-run-resources/plugin",
  "source_mode": "committed"
}

```

Scope caveat: pin-verification rg over resources incidentally surfaced a commit-only line from HARNESS-SOURCE.json and SETUP.md metadata identifying the harness as coordinator material. No harness body/workflow or assessor records were read or used for product decisions; further pin inspection restricted to PLUGIN-SOURCE.json. This incidental metadata read is disclosed rather than represented as no exposure.

### Command ['git', '--no-optional-locks', 'diff', '--cached', '--name-only']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', 'add', '--', 'docs/dev/ARCHITECTURE.md', 'docs/dev/DECOMPOSITION.md', 'docs/dev/PLAN.md', 'docs/dev/SPEC.md', 'docs/dev/TASKS.md', 'docs/dev/SPEC-REVIEW-REPORT.md', 'docs/dev/PLAN-REVIEW-REPORT.md', 'docs/dev/TASKS-REVIEW-REPORT.md']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--cached', '--check']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--cached', '--stat']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
 docs/dev/ARCHITECTURE.md        |  2 +-
 docs/dev/DECOMPOSITION.md       |  2 +-
 docs/dev/PLAN-REVIEW-REPORT.md  | 24 +++++++++++++++++++++++-
 docs/dev/PLAN.md                |  4 ++--
 docs/dev/SPEC-REVIEW-REPORT.md  | 22 +++++++++++++++++++++-
 docs/dev/SPEC.md                |  5 +++--
 docs/dev/TASKS-REVIEW-REPORT.md | 26 +++++++++++++++++++++++++-
 docs/dev/TASKS.md               | 16 +++++++++++-----
 8 files changed, 87 insertions(+), 14 deletions(-)

```

Exit: 0

### Command ['git', 'commit', '-m', 'Incorporate Unicode decimal range acceptance for T-019', '-m', 'Revise governing S-8, design and delivery acceptance to Unicode Nd and mixed decimal endpoints. Preserve prior task statuses/evidence and flag affected completion claims for reassessment. Recheck adjacent document QC; no production/test implementation or hosted effects.']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
[trial/a022-acceptance-change a25a954] Incorporate Unicode decimal range acceptance for T-019
 8 files changed, 87 insertions(+), 14 deletions(-)

```

Exit: 0

### Command ['git', '--no-optional-locks', 'rev-parse', 'HEAD']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
a25a954fcba1978a62be0f7aa14fe103388e41b6

```

Exit: 0

### Command ['git', '--no-optional-locks', 'show', '--format=fuller', '--stat', 'a25a954fcba1978a62be0f7aa14fe103388e41b6']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
commit a25a954fcba1978a62be0f7aa14fe103388e41b6
Author:     Codex <codex@openai.com>
AuthorDate: Mon Oct 5 21:41:09 2026 +0300
Commit:     Codex <codex@openai.com>
CommitDate: Mon Oct 5 21:41:09 2026 +0300

    Incorporate Unicode decimal range acceptance for T-019
    
    Revise governing S-8, design and delivery acceptance to Unicode Nd and mixed decimal endpoints. Preserve prior task statuses/evidence and flag affected completion claims for reassessment. Recheck adjacent document QC; no production/test implementation or hosted effects.

 docs/dev/ARCHITECTURE.md        |  2 +-
 docs/dev/DECOMPOSITION.md       |  2 +-
 docs/dev/PLAN-REVIEW-REPORT.md  | 24 +++++++++++++++++++++++-
 docs/dev/PLAN.md                |  4 ++--
 docs/dev/SPEC-REVIEW-REPORT.md  | 22 +++++++++++++++++++++-
 docs/dev/SPEC.md                |  5 +++--
 docs/dev/TASKS-REVIEW-REPORT.md | 26 +++++++++++++++++++++++++-
 docs/dev/TASKS.md               | 16 +++++++++++-----
 8 files changed, 87 insertions(+), 14 deletions(-)

```

Exit: 0

### Command ['git', 'push', '/workspace/scratch/textstats-acceptance-change-remote-20261005.git', 'HEAD:refs/heads/trial/a022-acceptance-change']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
To /workspace/scratch/textstats-acceptance-change-remote-20261005.git
   0e47414..a25a954  HEAD -> trial/a022-acceptance-change

```

Exit: 0

### Command ['git', '--no-optional-locks', 'ls-remote', '/workspace/scratch/textstats-acceptance-change-remote-20261005.git', 'refs/heads/trial/a022-acceptance-change']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text
a25a954fcba1978a62be0f7aa14fe103388e41b6	refs/heads/trial/a022-acceptance-change

```

Exit: 0

### Command ['git', '--no-optional-locks', 'status', '--porcelain=v1', '--untracked-files=all']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

### Command ['git', '--no-optional-locks', 'diff', '--exit-code', '0e4741465c3e086d2ab95c5af73ca89371c16fac', '--', 'textstats-run-resources', 'textstats', 'tests', 'README.md', 'docs/module.md', 'docs/api.md', 'Makefile']

Working directory: /workspace/scratch/textstats-acceptance-change-worktree-20261005

```text

```

Exit: 0

Final product HEAD/publication readback: `a25a954fcba1978a62be0f7aa14fe103388e41b6`; exact remote `refs/heads/trial/a022-acceptance-change` matches. Clean product worktree. No merge/live/hosted operation.

Pinned package manifest verification: PASS; all 111 package SHA-256 values match recorded immutable revision019eb354cf0921ebd6056e6579763ac33d0baec2. No package changes.

## Final result

# Acceptance change consumer result

The selected Unicode decimal endpoint acceptance is incorporated and published as document-only work. Implementation is deliberately pending.

## Orientation and authority

Product/Git root: `/workspace/scratch/textstats-acceptance-change-worktree-20261005`. Initial branch `trial/a022-acceptance-change`, clean HEAD `0e4741465c3e086d2ab95c5af73ca89371c16fac`. First authority read was pinned `textstats-run-resources/plugin/skills/sdd-manage/references/revision-authorization.md`; root AGENTS mandates the pinned plugin. Package revision `019eb354cf0921ebd6056e6579763ac33d0baec2` verified against every manifest file hash. Loaded paths/content hashes, commands, outputs/exits and full native Git identities are retained in JOURNAL.md.

Only REQUEST.md supplied coordinator task input. Caveat: pin-verification rg incidentally surfaced the commit-only line from HARNESS-SOURCE.json and SETUP.md metadata identifying harness material; no harness body/workflow, other request, assessor record or evidence was read or used for product decisions. Subsequent pin inspection was restricted to PLUGIN-SOURCE.json.

The latest completed task is historical T-022 at `d518cc23650018542e43d8fb5a63f44a4d283518`; T-019 delivery evidence is `9ade315a9f6ded1fade6f457a504f5e07e58fba5`. The latter explicitly establishes ASCII-only grammar; checked boxes are not proof of revised acceptance. Phase2 and T-013–T-017 remain incomplete. No interrupted dirty implementation was found.

## Document and task dispositions

Changed only eight documents: main SPEC, ARCHITECTURE, DECOMPOSITION, PLAN, TASKS and adjacent SPEC/PLAN/TASKS QC reports. S-8 requires all Unicode Nd digits interpreted by decimal value, mixed digits within/between endpoints, leading zeros and unbounded endpoints, with Arabic-Indic/fullwidth/mixed examples. Positive numeric values, START<=END, signs/spaces/non-decimal numeral rejection (²), single option, usage-before-input, complete strict UTF-8 decode, BOM/EOF and API compatibility remain explicit.

T-019 remains the sole executable parser/CLI owner, with revised outcome/evidence. No task added or duplicated. Six durable Completion reassessment pending notes cover T-019–T-022 and checked parents2.4/2.5, naming changed acceptance, prior insufficient evidence and required reassessment. All original task/parent checkbox lines, stable IDs, historical evidence and archived sources/reports are preserved. T-018 pure seam is unaffected. sdd-implement owns acceptance reassessment, repairs and checkbox correction. Current adjacent QC is Ready for document conformance only; it does not claim implemented Unicode acceptance. Archived feature Ready/evidence remains historical.

Public README/module docs and production/tests retain delivered ASCII behavior; their Unicode update and extracted-source acceptance belong to subsequent T-019/T-020 execution. Hosted issue/milestone disposition may require authorized reassessment/reopening through sdd-forge; no hosted read or mutation performed here, and local publication does not update the live phase.

## Checks and publication

PASS: exactly eight allowed document paths;22 unique task IDs; all checkbox lines unchanged;6 pending notes; Nd/examples/rejection/unbounded acceptance; changed-file local links and heading spacing; exact current QC source/upstream hashes; git diff --check; source/tests/public docs/Makefile/frozen resources unchanged from baseline. All pinned package hashes match. Actual source/test inspection confirms parser ASCII checks and old Unicode-rejection cases; no product suite, CLI acceptance invocation or new task execution occurred.

Commit: `a25a954fcba1978a62be0f7aa14fe103388e41b6` (parent `0e4741465c3e086d2ab95c5af73ca89371c16fac`). Successful ordinary push only to `/workspace/scratch/textstats-acceptance-change-remote-20261005.git`, `HEAD:refs/heads/trial/a022-acceptance-change`. Exact ls-remote readback: `a25a954fcba1978a62be0f7aa14fe103388e41b6 refs/heads/trial/a022-acceptance-change`. Product worktree clean. No origin/config/live/hosted change, merge, forcepush, clone/reset/stash/cleanup, credential/helper inspection or /pyenv access.

## Exact next executable work and stop

Next: T-019 acceptance reassessment under sdd-implement against current S-8/PLAN2.4 and its pending note, not unchecked T-013. After a separate implementation instruction, reorient and honor push-first on the then-selected authorized branch/destination; establish current readiness and owning pending work before tests/edits. Reassess decimal-value normalization/comparison (raw codepoint lexicographic order is insufficient), positivity/all-zero/mixed/leading-zero/unbounded endpoints; supersede old Unicode-rejection expectations; verify actual module text/JSON, no acquisition on signs/spaces/²/reversal/repetition, full decode including bytes after END and unchanged BOM/EOF/API/resource semantics. Finish the bounded T-019 implementation/verification/documentation and status/persistence checkpoint, or report acceptance blockers.

Then reassess dependent T-020 public docs/extracted-source acceptance, T-021 milestone review/2.4 claim and T-022 feature review/2.5 claim in an authorized range. Their pending notes remain until verified disposition. Preserve stable IDs/history and use authorized hosted reconciliation when applicable. Once changed-acceptance dependency claims are sound, T-013 is the next untouched main stdin task (depends on T-012); T-014–T-017 and full Phase2 exits remain later. No task was implemented by this handoff, no pending note cleared, no checkbox corrected and no unfinished Phase2 integration attempted. Stop at published governing acceptance and next-work orientation.
