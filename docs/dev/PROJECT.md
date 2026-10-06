# TextStats project brief

TextStats is a small Python utility for people counting lines and words in UTF-8 files, and Python callers processing strings. Its public package is `textstats`, with the module CLI `python -m textstats`.

## Scope and constraints

Use Python 3.11+, the standard library and unittest. Deliver the named-file API/CLI first, then byte-based stdin. Keep counting deterministic, API calls silent, input unchanged, diagnostics useful, and owned file resources closed. The complete behavioral contract is [SPEC.md](SPEC.md); structural responsibilities are in [ARCHITECTURE.md](ARCHITECTURE.md) and [DECOMPOSITION.md](DECOMPOSITION.md).

Provide importable immutable statistics, public API/module documentation, a runnable README, discoverable nonempty unit/integration tests, and an extracted-source distribution smoke check. Workflow fixture checks have their own test directory and cannot establish product acceptance.

## Boundaries

Named-file line ranges are part of the delivery hierarchy alongside later byte-based stdin. Range selection is a named-file CLI option; public APIs count whole input and expose no range parameter or additional export. Source-independent decoded-text selection shares semantics with future source acquisition. Stdin line ranges are unsupported. Network services, GUI, encodings other than UTF-8, file mutation, plugins and performance guarantees for unbounded data are non-goals.

## Decisions

The preparation brief supplies the product requirements and phase/milestone identities. No material requirement decision remains open. Entire-input decoding is accepted: this keeps strict UTF-8 failures atomic and supports future selection after decoding. Memory use scales with input size; streaming optimization is outside the requested scope.
