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

## Input and options

Syntax: `python -m textstats [--keep-bom] INPUT`. Exactly one named UTF-8 file is required. `--` permits dash-prefixed filenames. `--keep-bom` retains all leading BOM characters; otherwise exactly one initial BOM is removed. CRLF/CR/LF lines and Unicode whitespace words follow the [API rules](api.md). Files stay unchanged. JSON output and stdin input are planned for Phase 2 and are not delivered in Phase 1.

## Output and status

Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout, and leaves stderr empty. Help exits 0. Missing, extra or unknown arguments exit 2, with useful stderr, empty stdout, no traceback and no file acquisition. Expected open/read/decode failures exit 1, identify INPUT on stderr, and produce no stdout or traceback. Strict complete UTF-8 decoding prevents partial success even when invalid bytes follow valid text. File handles opened by the API are owned and closed.

```sh
python -m textstats nonexistent.txt
# status 1; stderr identifies nonexistent.txt; stdout is empty
```

See the [README](../README.md) for test and distribution commands.
