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

CLI `--lines` selection for named files or stdin does not change these whole-input API signatures or semantics. No range API is exported.
