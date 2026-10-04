# TextStats specification

The intended product serves Python callers and CLI users as defined in [PROJECT.md](PROJECT.md). Component owners are in [DECOMPOSITION.md](DECOMPOSITION.md); acquisition and counting depend only on the standard library. These contracts cover the complete main product, with delivery boundaries in PLAN. The separately requested range feature is excluded from main acceptance.

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

`python -m textstats [--keep-bom] INPUT` accepts exactly one input; `--` permits dash-prefixed filenames. --keep-bom corresponds to strip_bom=False. Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout and leaves stderr empty. Help exits 0. Missing/extra input or unknown options exit 2 with useful stderr, empty stdout, no traceback and no input acquisition. Named-file input/read/decode failures exit 1, identify the input usefully on stderr, leave stdout empty and emit no traceback. CLI input remains unchanged. The command adapter owns validation, rendering, diagnostics and status; the module entry exposes invocation.

## S-5 JSON

`--json` emits exactly one JSON object plus newline on success. Its only keys are lines and words, with integer values equal to default text counts. Key order and spacing are unrestricted. Text output remains the default, and BOM/source/error behavior is retained. Compose --json with --keep-bom in either order. Rendering belongs to the command adapter.

## S-6 Standard input

INPUT `-` selects stdin at its later milestone. Read bytes until EOF, decode UTF-8 strictly independent of locale, and never close borrowed stdin. Empty stdin gives (0,0). Read/decode failures exit 1 with stderr identifying stdin, empty stdout and no traceback. Both output modes and BOM policies apply. Named-file behavior remains available; `./-` addresses a named file literally called `-`.

## S-7 Documentation, tests and distribution

Public API/module documentation describes signatures, text/BOM rules, UTF-8 exceptions and lifecycle. The README provides runnable API/CLI examples, help, statuses, supported Python, unittest commands and delivered output/source options. Discoverable nonempty product tests live under tests/unit/ and tests/integration/; workflow fixture checks live separately under tests/workflows/ and cannot substitute for product checks. A source distribution contains an importable package and relevant documentation. A distribution check extracts it to an isolated directory and invokes that extracted source package with `python -m textstats`, establishing counts and CLI behavior without importing the working checkout. Test/distribution ownership is described in DECOMPOSITION.

## Acceptance boundaries

Phase 1 milestone 1.1 demonstrates useful named-file counting, public API and module CLI with S-1/S-2/S-3 success and S-4 success/help/option handling. Milestone 1.2 establishes all S-3/S-4 failure/resource contracts and S-7 documentation/distribution exits. Phase 2 milestone 2.1 demonstrates S-5 while retaining phase 1 behavior; milestone 2.2 demonstrates S-6 and updated S-7 exits, with all prior acceptance retained. Evidence includes exact stdout/status/stderr checks, path/BOM/terminator cases, complete decoding and unchanged input. Neither passing a workflow fixture nor a zero-test discovery is product acceptance.
