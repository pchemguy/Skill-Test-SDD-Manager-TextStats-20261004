# TextStats project brief

TextStats is a small Python utility for people counting lines and words in UTF-8 files, and Python callers processing strings. Its public package is `textstats`, with the module CLI `python -m textstats`.

## Scope and constraints

Use Python 3.11+, the standard library and unittest. Deliver the named-file API/CLI first, then JSON output and byte-based stdin. Keep counting deterministic, API calls silent, input unchanged, diagnostics useful, and owned file resources closed. The complete behavioral contract is [SPEC.md](SPEC.md); structural responsibilities are in [ARCHITECTURE.md](ARCHITECTURE.md) and [DECOMPOSITION.md](DECOMPOSITION.md).

Provide importable immutable statistics, public API/module documentation, a runnable README, discoverable nonempty unit/integration tests, and an extracted-source distribution smoke check. Workflow fixture checks have their own test directory and cannot establish product acceptance.

## Boundaries

This preparation defines the design, specification, delivery plan, physical layout and executable tasks. It stops before production implementation and hosted tracking. The authorized preparation checkpoint is main at `8e2d3a57af36bc42d73f2118542a8f2608bab6ae` in pchemguy/Skill-Test-SDD-Manager-TextStats-20261004, published through origin/main. No phase is activated by preparation.

A separately requested line-range feature is outside the main delivery hierarchy. Its future constraints are recorded in design so that selection can share decoded-text semantics across named files and future stdin. No range API export or public API parameter is intended. Network services, GUI, encodings other than UTF-8, file mutation, plugins and performance guarantees for unbounded data are non-goals.

## Decisions

The preparation brief supplies the product requirements and phase/milestone identities. No material requirement decision remains open. Entire-input decoding is accepted: this keeps strict UTF-8 failures atomic and supports future selection after decoding. Memory use scales with input size; streaming optimization is outside the requested scope.
