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
| docs/module.md | Module CLI text output, option/source semantics and statuses |
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
