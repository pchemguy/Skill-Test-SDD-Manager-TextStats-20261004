# TextStats architecture

[PROJECT.md](PROJECT.md) defines purpose and boundaries. This describes intended design, not implemented behavior.

## Blocks and dependencies

A pure counting core owns statistics and text semantics. An acquisition adapter owns UTF-8 decoding and named-file resource lifecycle. A command adapter owns option validation, source choice, text output, diagnostics and process status. Public exports expose the core and named-file adapter; the module entry delegates to the command adapter. Dependencies flow command → acquisition/core and acquisition → core. The core never imports CLI, filesystem or process state.

All mutable state is per call. There is no persistent store or external service. Input belongs to the caller; the named-file adapter closes handles it opens, while the command adapter borrows stdin. Output is published only after successful complete acquisition and counting.

## Choices and invariants

A frozen value object plus functions gives a small public surface without an inheritance hierarchy. Separate acquisition from counting to keep Unicode and line semantics testable without filesystem or process fixtures. Standard-library argument parsing and text formatting are sufficient; no runtime third-party dependency is needed.

Decode complete bytes using strict UTF-8 before text processing. File reads preserve CR/LF terminators, avoiding universal-newline translation. Apply the BOM policy once at the boundary of text processing; the core operates on the resulting text. Keep formatting outside the counting core. These boundaries allow small integrated delivery increments while retaining a stable whole-input API.

## Named-file range selection

A CLI-only selection stage sits between complete decoding/BOM normalization and counting. It identifies only CRLF, CR and LF logical lines, preserves selected contents and terminators, and never applies BOM stripping again to a slice. Source-independent decoded-text processing supports named files and future stdin. Range syntax is validated before acquisition, including repetition and positive ordered ASCII decimals without an endpoint cap or interpreter conversion limit. Named-file acquisition exposes complete decoded text privately, while count_file retains its whole-input contract. The command selects normalized logical lines and counts the slice with BOM stripping disabled. Stdin acquisition remains a separate delivery; stdin ranges are unsupported.

See [DECOMPOSITION.md](DECOMPOSITION.md) for component seams and [SPEC.md](SPEC.md) for observable contracts.
