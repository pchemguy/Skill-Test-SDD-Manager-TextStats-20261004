# TextStats component decomposition

The intended components refine [ARCHITECTURE.md](ARCHITECTURE.md). [SPEC.md](SPEC.md) owns normative public behavior.

| Component | Responsibility and collaborators | State / verification seam |
| --- | --- | --- |
| Statistics value | Immutable nonnegative integer lines/words; consumed by public callers and renderers | Frozen per-result data; construction and mutation checks |
| Text processing | One leading BOM policy, CR/LF line counting, Unicode whitespace word counting; returns statistics | Pure per-call text; table-driven unit checks |
| Named-file acquisition | Read bytes unchanged, strict UTF-8 decode, close its file handle, call text processing | Context-managed owned handle; real temporary-file and error checks |
| Public facade | Export TextStats, count_text, count_file directly from textstats | Import check and signature checks; no process side effects |
| Command adapter | Validate options, acquire the selected source, count, render once, map errors to diagnostics/status | Arguments and borrowed streams; subprocess checks for actual module entry |
| Module entry | Delegate process invocation to command adapter | Extracted-package module invocation |
| Product verification/distribution | Discoverable unit/integration suites, source archive with package/docs, extracted-source smoke check | Isolated temporary extraction; independent suite counts |

## Collaboration and ownership

`count_text` consumes caller text and owns only normalization/counting. `count_file` consumes a path and delegates after complete decoding. The command adapter delegates named-file acquisition and, at its later delivery boundary, reads borrowed stdin bytes until EOF. Read/decode failures propagate through the API; the CLI translates expected failures and produces no partial success output. The core cannot emit diagnostics.

Text formatting and JSON rendering consume the same statistics. Option validation precedes any input acquisition. The future range selector consumes already normalized text and passes retained contents/terminators to counting without a second BOM normalization. It has no source dependency or public export. The command adapter remains responsible for future range parsing and composing options; stdin acquisition remains separately scheduled.

No extra abstraction layer or focused child document is needed for this bounded utility. Source allocation belongs to layout, and delivery order belongs to PLAN.
