# Skill-Test-SDD-Manager-TextStats-20261004

SDD Manager TextStats testing

Development uses [SDD Manager](SDD-MANAGER.md). See the [AI-assisted development disclosure](AI_DISCLOSURE.md).

TextStats currently provides immutable `TextStats` values and pure `count_text` counting for Python 3.11+. The public `count_file(path, *, strip_bom=True)` API also counts named UTF-8 files without changing their bytes. The module CLI is planned in the next task. See the [project brief](docs/dev/PROJECT.md) and [specification](docs/dev/SPEC.md).
