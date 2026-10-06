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

Syntax: `python -m textstats [--keep-bom] [--lines START:END] INPUT`. Exactly one named UTF-8 file or `-` for binary stdin is required. `--` permits dash-prefixed filenames. `--keep-bom` retains all leading BOM characters; otherwise exactly one initial BOM is removed. CRLF/CR/LF lines and Unicode whitespace words follow the [API rules](api.md). Files stay unchanged. `--json` is an unknown option (status 2 before acquisition); a literal `--json` filename is accessible after `--`. INPUT `-` reads borrowed stdin bytes until EOF and decodes strict UTF-8 independently of locale; stdin stays open. `./-` names a literal file called `-`.

## Output and status

Success exits 0, writes exactly `lines=<N> words=<N>\n` to stdout, and leaves stderr empty. Help exits 0. Missing, extra or unknown arguments exit 2, with useful stderr, empty stdout, no traceback and no input acquisition. Expected open/read/decode failures exit 1, identify the named INPUT or stdin on stderr, and produce no stdout or traceback. Strict complete UTF-8 decoding prevents partial success even when invalid bytes follow valid text. File handles opened by the API are owned and closed; borrowed stdin is never closed.

```sh
python -m textstats nonexistent.txt
# status 1; stderr identifies nonexistent.txt; stdout is empty
```

See the [README](../README.md) for test and distribution commands.

## CLI line ranges

```sh
printf 'alpha beta\nbeta\nlast two' > ranges.txt
python -m textstats --lines 2:3 ranges.txt
# lines=2 words=3
python -m textstats --lines=2:3 ranges.txt
# lines=2 words=3
python -m textstats --lines 4:99 ranges.txt
# lines=0 words=0
python -m textstats --lines=2:1 ranges.txt
# status 2; empty stdout; useful stderr; no input acquisition
```

`--lines START:END` and `--lines=START:END` select inclusive one-based logical lines of a named file or stdin. Endpoints must be positive ASCII decimals with START <= END; leading zeros and arbitrarily long endpoints are accepted. Missing/open endpoints, signs, whitespace, Unicode digits, zero, reversed bounds, extra colons and repeated range options are usage errors (status 2) before input is read. Selection intersects available lines; beyond EOF may yield empty counts. Only CRLF, CR and LF terminate lines, and original contents/terminators are preserved.

The entire input is strictly decoded before selection, so bad UTF-8 after END still fails (status 1). Apply the default one-leading-BOM removal or `--keep-bom` once to complete text before line numbering. An interior BOM exposed at the selection start stays ordinary non-whitespace. `--lines` and `--keep-bom` compose in either order before `--`. Public APIs always count the whole input; they have no range parameter. Stdin uses the same range grammar, complete decoding, single BOM policy and preserved logical-line semantics.


## Binary stdin

Use `-` to count stdin bytes through EOF. UTF-8 decoding is strict and independent of the process locale. Stdin is borrowed and remains open; `./-` names a literal file called `-`. Range syntax and both BOM policies apply after complete decoding. Invalid ranges are rejected before reading; malformed UTF-8 after the selected END still fails with status 1, stderr identifying stdin and empty stdout.

```sh
printf 'alpha beta\ngamma\n' | python -m textstats -
# lines=2 words=3
printf 'alpha beta\nbeta\nlast two' | python -m textstats --lines 2:3 -
# lines=2 words=3
printf 'alpha beta\nbeta\nlast two' | python -m textstats --lines=2:3 -
# lines=2 words=3
printf '\357\273\277\n' | python -m textstats --keep-bom --lines=1:1 -
# lines=1 words=1
printf '\357\273\277\n' | python -m textstats --lines 1:1 --keep-bom -
# lines=1 words=1
```

```sh
printf 'valid\nlate\377' | python -m textstats --lines=1:1 -
# status 1; stderr identifies stdin; stdout is empty
```
