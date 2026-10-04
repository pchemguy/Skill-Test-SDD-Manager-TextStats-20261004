# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats counts lines and words in strings and named UTF-8 files on Python 3.11+, using only the standard library. Its immutable results and silent API are described in the [API guide](docs/api.md); options, errors and statuses are in the [module guide](docs/module.md). JSON and stdin remain planned Phase 2 capabilities. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).

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
