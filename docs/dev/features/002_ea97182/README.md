# Named-file line ranges feature

Campaign: `002_ea97182`. Baseline: `ea97182d2d6a3984599238312a13e78d54d3221a`.
Working branch: `feature/002_ea97182-line-ranges`. Integration target: `phase/2-output-and-source-extensions` in pchemguy/Skill-Test-SDD-Manager-TextStats-20261004. Main remains `59debb649545125dd3aa00377ea115451b594271`.

Authorized delivery: implement named-file text/JSON selection, incorporate governing owners, project maintained tracking and integrate into the paused phase target after verification. Stop before stdin or later phase execution. T-012 is complete; T-013–T-017/stdin remain unfinished. Preserve their identities and current acceptance.

Active sources: [FEATURE-SPEC](../../FEATURE-SPEC.md), [FEATURE-PLAN](../../FEATURE-PLAN.md), [FEATURE-TASKS](../../FEATURE-TASKS.md). Adjacent QC reports govern dependent use. Sources remain active at root until separately accepted incorporation/archive.

## Design decision

Reuse [ARCHITECTURE](../../ARCHITECTURE.md) and [DECOMPOSITION](../../DECOMPOSITION.md): command validation → complete named-file byte decoding → one leading BOM normalization → pure logical-line selection → count_text with stripping disabled → existing text/JSON rendering. Whole-input APIs retain signatures/exports and lifecycle. Internal acquisition may share a private decode helper with count_file; selection and normalization have no file/stdin dependency. Counting a selected slice never removes an exposed interior BOM. No new abstraction layer, public range API, encoding or stdin delivery is needed. Existing layout places pure helpers in core, acquisition in io, validation/rendering in cli, product tests in unit/integration and workflow fixtures separately.

The selector recognizes only CRLF/CR/LF and preserves original contents/terminators; str.splitlines would violate the Unicode-separator contract. Endpoint parsing/comparison must accept arbitrarily long ASCII decimals without Python's configured integer-string conversion limit becoming a usage rejection (normalized decimal strings or incremental conversion are viable internal choices). Memory scales with complete input, as accepted by the main design.
