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

`python -m textstats [--keep-bom] [--lines START:END] INPUT` accepts exactly one input; `--` permits dash-prefixed filenames. --keep-bom corresponds to strip_bom=False. Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout and leaves stderr empty. Help exits 0. Missing/extra input or unknown options exit 2 with useful stderr, empty stdout, no traceback and no input acquisition. Named-file input/read/decode failures exit 1, identify the input usefully on stderr, leave stdout empty and emit no traceback. CLI input remains unchanged. Optional named-file selection follows S-8; without --lines, count the whole input. The command adapter owns validation, rendering, diagnostics and status; the module entry exposes invocation.

## S-5 Retired JSON identity

S-5 is reserved and retired; JSON output is outside supported scope. `--json` is an unknown option: status 2, empty stdout, useful stderr and no acquisition, including composition with --keep-bom or --lines. A file literally named `--json` remains accessible after `--`. S-6–S-8 keep their identities.

## S-6 Standard input

INPUT `-` selects stdin at its later milestone. Read bytes until EOF, decode UTF-8 strictly independent of locale, and never close borrowed stdin. Empty stdin gives (0,0). Read/decode failures exit 1 with stderr identifying stdin, empty stdout and no traceback. Text output and both BOM policies apply to whole-input stdin; --lines with INPUT - is unsupported. Named-file behavior remains available; `./-` addresses a named file literally called `-`.

## S-7 Documentation, tests and distribution

Public API/module documentation describes signatures, text/BOM rules, UTF-8 exceptions and lifecycle. The README provides runnable API/CLI examples, help, statuses, supported Python, unittest commands and delivered output/source options, including runnable named-file range examples, both option spellings, validation/status rules, complete decoding and single BOM normalization. Discoverable nonempty product tests live under tests/unit/ and tests/integration/; workflow fixture checks live separately under tests/workflows/ and cannot substitute for product checks. A source distribution contains an importable package and relevant documentation. A distribution check extracts it to an isolated directory and invokes that extracted source package with `python -m textstats`, establishing counts and CLI behavior without importing the working checkout. Named-file range distribution acceptance covers text, BOM policy and representative usage/read/decode failures. Test/distribution ownership is described in DECOMPOSITION.

## S-8 Named-file line selection

### Invocation and validation

Named-file CLI accepts one optional `--lines START:END` or `--lines=START:END`. Endpoints are nonempty positive ASCII decimal sequences, interpreted in base10 with leading zeros allowed, inclusive and one-based; START <= END. There is no arbitrary endpoint bound or digit-count limit. Reject signs, whitespace, Unicode digits, zero, reversed endpoints, open endpoints, extra colons, missing values and repeated --lines options (including mixed spellings). Invalid usage exits2, useful stderr, empty stdout, no traceback, before opening or reading input. Without --lines retain whole-input behavior. Existing help/status/one-input/unknown-option/-- dash-filename behavior remains. --lines and --keep-bom compose in either order before the `--` separator.

### Selection semantics

Decode the entire named file as strict UTF-8 before selection; malformed bytes after END still fail. Apply the existing BOM policy exactly once to the complete decoded text before numbering. Default removes one leading U+FEFF, --keep-bom removes none. Number logical lines using only CRLF, lone CR and LF terminators; every terminator contributes one line, and a nonempty final unterminated segment contributes one. A trailing terminator adds no phantom line; empty normalized text has zero. Other Unicode separators remain contents.

Select the available intersection with inclusive START:END, preserving all selected characters and original terminators. Beyond EOF selects available lines or empty text. Count selected text under S-2 without BOM stripping again: an interior BOM exposed at the start of the selection remains ordinary non-whitespace. Unicode words use str.split semantics.

### Results and compatibility

Success text is exactly `lines=<N> words=<N>\n`, status0, empty stderr. Empty selection gives (0,0). Named-file read/decode errors retain status1, identifying stderr, empty stdout and no traceback; opened handles close, files remain unchanged. Public count_text/count_file remain silent whole-input calls with unchanged exports/signatures, exceptions and BOM policy. Without --lines, CLI output and error behavior satisfy S-4.

Normalization and selection operate on decoded strings independently of source acquisition, preserving compatibility with the borrowed-stdin adapter. Selection acceptance is named-file text only; stdin ranges and a public range API are unsupported.

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

Acceptance includes both option spellings and BOM option orders, leading-zero endpoints, huge endpoints beyond interpreter decimal conversion limits, all rejection categories and mixed repeated spellings before acquisition, invalid UTF-8 beyond END, interior BOM, CRLF/CR/LF, empty/beyond-EOF, unchanged files and owned-handle closure. API remains whole-input for files whose CLI range differs. Discoverable nonempty unit/integration suites remain separate from workflow checks. README/module help/docs show runnable named-file examples, syntax, statuses, complete decode/BOM rules and the exact delivered boundary. Isolated extracted-source module invocation demonstrates ranges/text, BOM policy and representative failures without importing the checkout.

The command adapter owns syntax, option composition and rendering; named-file acquisition owns complete decoding and handle closure; pure text processing owns normalization, selection and counting. Public facade exports remain unchanged.

## Acceptance boundaries

Phase 1 milestone 1.1 demonstrates useful named-file counting, public API and module CLI with S-1/S-2/S-3 success and S-4 success/help/option handling. Milestone 1.2 establishes all S-3/S-4 failure/resource contracts and S-7 documentation/distribution exits. Milestone 2.1 is a retired historical JSON boundary; milestone 2.2 demonstrates S-6 and updated S-7 exits, with all prior acceptance retained. Evidence includes exact stdout/status/stderr checks, path/BOM/terminator cases, complete decoding and unchanged input. Neither passing a workflow fixture nor a zero-test discovery is product acceptance.

Named-file line-selection acceptance establishes S-8 and the affected S-4/S-7 obligations, retaining S-1–S-3 and whole-input behavior. It covers every selection example and rejection category above through actual named-file module invocation, text output, unchanged input and resource/error checks. It makes no stdin range claim and does not establish whole-project phase completion.
