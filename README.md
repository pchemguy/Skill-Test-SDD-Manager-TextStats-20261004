# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats counts lines and words in strings and named UTF-8 files on Python 3.11+, using only the standard library. Its immutable results and silent API are described in the [API guide](docs/api.md); options, errors and statuses are in the [module guide](docs/module.md). Text output is available for named files; stdin remains planned for milestone 2.2. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).

## Quick start

Run from the source root:

```python
from textstats import TextStats, count_text
assert count_text("alpha beta\r\ngamma\r") == TextStats(2, 3)
```

```sh
printf 'alpha beta\ngamma\n' > sample.txt
python -m textstats sample.txt
# lines=2 words=3
python -m textstats --help
printf '\357\273\277\n' > bom.txt
python -m textstats bom.txt
# lines=1 words=0
python -m textstats --keep-bom bom.txt
# lines=1 words=1
printf 'alpha\n' > ./-sample.txt
python -m textstats -- -sample.txt
# lines=1 words=1
```

Empty input counts zero lines and words. Only CRLF, CR and LF terminate lines; a trailing terminator creates no extra line. Words follow Python Unicode whitespace splitting. By default exactly one initial BOM is removed. Input bytes stay unchanged, reads decode strict UTF-8, and owned file handles close. Complete-input processing uses memory proportional to input size.

Text output is exactly `lines=<N> words=<N>` plus newline. `--json` is an unknown option (status 2 before acquisition); a file literally named `--json` is accessible after `--`.

Success/help exit 0. Invalid arguments exit 2 before reading input. Expected file/read/decode failures exit 1 with an input-identifying diagnostic on stderr, no stdout or traceback. API errors propagate as OSError subclasses or UnicodeDecodeError.

## Product tests

Run the nonempty product suites independently:

```sh
python -m unittest discover -s tests/unit -t . -v
python -m unittest discover -s tests/integration -t . -v
```

Workflow fixtures under tests/workflows, when present, are separate from product acceptance.

## Source distribution

Build a standard-library source archive and extract it in an empty directory:

```sh
make dist
mkdir -p dist/extracted
python -m tarfile -e dist/textstats.tar.gz dist/extracted
cd dist/extracted
python -m textstats --help
```

The archive includes the package, public/development documentation and product tests. Generated dist output stays untracked. Integration discovery builds and extracts to a temporary directory, clears checkout import settings and verifies the extracted module's text/BOM/help/error behavior and import location. `make check` runs the two product suites independently.

## Named-file line ranges

```sh
printf 'alpha beta\nbeta\nlast two' > ranges.txt
python -m textstats --lines 2:3 ranges.txt
# lines=2 words=3
python -m textstats --lines=2:3 ranges.txt
# lines=2 words=3
python -m textstats --lines 4:99 ranges.txt
# lines=0 words=0
python -m textstats --lines=2:1 ranges.txt
# status 2; empty stdout; useful stderr; no file acquisition
```

`--lines START:END` and `--lines=START:END` select inclusive one-based logical lines of a named file. Endpoints must be positive ASCII decimals with START <= END; leading zeros and arbitrarily long endpoints are accepted. Missing/open endpoints, signs, whitespace, Unicode digits, zero, reversed bounds, extra colons and repeated range options are usage errors (status 2) before input is read. Selection intersects available lines; beyond EOF may yield empty counts. Only CRLF, CR and LF terminate lines, and original contents/terminators are preserved.

The entire file is strictly decoded before selection, so bad UTF-8 after END still fails (status 1). Apply the default one-leading-BOM removal or `--keep-bom` once to complete text before line numbering. An interior BOM exposed at the selection start stays ordinary non-whitespace. `--lines` and `--keep-bom` compose in either order before `--`. Public APIs always count the whole input; they have no range parameter. Stdin remains scheduled for milestone 2.2; stdin ranges are unsupported.
