# Named-file line range specification

Active scoped delta for [feature002_ea97182](features/002_ea97182/README.md), based on completed JSON milestone2.1/T-012. Extend main [SPEC](SPEC.md) S-4/S-5/S-7; preserve S-1–S-3 and unaffected S-4/S-5 behavior. S-6/stdin remains later main delivery, with source-independent compatibility required by [architecture](ARCHITECTURE.md). Public API stays whole-input: no new export or range parameter.

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
