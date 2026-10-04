# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats currently provides immutable `TextStats` values and pure `count_text` counting for Python 3.11+. The public `count_file(path, *, strip_bom=True)` API also counts named UTF-8 files without changing their bytes. Run `python -m textstats INPUT` for `lines=<N> words=<N>` output, `--keep-bom` to retain a leading BOM, or `--help` for syntax. Use `--` before a dash-prefixed filename. JSON, stdin, diagnostic hardening and release documentation are planned later. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
