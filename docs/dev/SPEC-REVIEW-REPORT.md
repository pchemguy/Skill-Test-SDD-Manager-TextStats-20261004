# SPEC review report

## Current gate

State: Ready for current text-only SPEC conformance. Owner: sdd-specify, 2026-10-05. Revision 4 records the removal amendment; historical evidence retained.

## Original reviewed identities

Reviewed and governing states:

- PROJECT.md: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- SPEC.md: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.

Checks: compared the accepted brief with every S-1 through S-7 contract and design ownership; inspected public signatures, result invariants, source/resource/error boundaries, format preservation, end-to-end acceptance and local document links. No confirmed issue or material open decision remains. PLAN authoring may proceed; implementation is not authorized.

## Initial review

| Contract group | Design and project coverage | Result |
| --- | --- | --- |
| S-1/S-2 value and text | Pure counting, immutable value and public facade | Complete CRLF/CR/LF, Unicode words and single-BOM behavior with objective examples |
| S-3 file failures/lifecycle | Named-file adapter, atomic complete UTF-8 decoding | API exceptions, silence, unchanged input and close ownership specified |
| S-4 CLI | Command adapter/module entry | Exact output, option errors, help, dash filenames and expected failures specified |
| S-5/S-6 extensions | Renderers and borrowed stdin adapter | JSON preservation and locale-independent binary stdin specified |
| S-7 product exits | Verification/distribution component | Public docs, runnable README, nonempty separated suites and extracted-source entry specified |

No findings. The future range contract is a source-independent design constraint, not an unrequested main delivery feature. Memory scaling is a documented scope tradeoff, not a claimed performance guarantee. No correction cycle occurred.

## Revision 1 — Selected named-file range incorporation

Scope: SPEC.md and this adjacent QC report only. Incorporation uses accepted FEATURE-SPEC R-1–R-4; all active feature sources and their reports remain in place. Existing review observations above are historical and retained.

Exact reviewed/governing states (SHA-256):

- SPEC.md: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`.
- FEATURE-SPEC.md: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`.
- PROJECT.md: `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- ARCHITECTURE.md: `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- DECOMPOSITION.md: `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.

| Contract group | Accepted coverage / current result |
| --- | --- |
| S-1–S-3 | Immutable value, silent whole-input APIs, exact text/BOM semantics, complete strict UTF-8 decode and resource ownership unchanged |
| S-4/S-5/S-8; R-1/R-3 | Command adapter owns one optional range, both spellings, unbounded positive ASCII decimals, repetition/invalid usage before acquisition, both renderers/BOM options, unchanged APIs/errors |
| S-2/S-3/S-8; R-2 | Acquisition fully decodes before pure source-independent normalization/selection; preserved CRLF/CR/LF, EOF and exposed interior BOM have objective contracts |
| S-6 | Borrowed binary stdin whole-input contract retained; named-file range acceptance makes no stdin range delivery claim |
| S-7/S-8; R-4 | All supplied examples and edge/failure cases, runnable docs/help, independent nonempty product suites and extracted-source range invocation required |

Assessment: accepted design already provides every structural owner/seam; PROJECT identifies ranges as separately requested rather than rejecting them. The selected request accepts their incorporation without moving them into the main delivery hierarchy. No design change or material unresolved behavioral decision is required. Read the full main root as a standalone intended contract, checked original S-1–S-7 preservation and R-1–R-4 coverage, format/error/lifecycle guarantees, absence of editing-history language, local links and objective acceptance. Removed the obsolete main range exclusion and integrated selection into S-4/S-5/S-7 plus canonical S-8. Editorial recheck removed implementation-stage language from the incorporated source prose. Whitespace, link, hash and selected-path checks passed; no product tests were run for this document-only checkpoint. No confirmed in-scope finding remains. SPEC gate: Ready.

Outside selected scope: main PLAN excludes range allocation and PLAN-REVIEW-REPORT reviews the old SPEC; main TASKS/TASKS-REVIEW-REPORT consequently cannot establish complete expanded-main conformance. Their affected gates require authorized PLAN/TASKS reconciliation and owner rechecks before dependent execution/projection. FEATURE-SPEC's own R-1–R-4 content is unchanged, but its recorded main SPEC identity and feature PLAN/TASKS upstream equivalence need reassessment before dependent use; those reports are retained historical evidence, not a fresh gate for this main incorporation. Feature tasks T-018–T-022 remain the sole executable range owners, unchecked; no transfer or duplicate entry was made. Main T-013–T-017 remain incomplete. Existing checked tasks and milestone/phase evidence are preserved for their historical whole-input/JSON boundaries; expanded S-4/S-5/S-7 or whole-project acceptance claims (notably T-004/T-008/T-009/T-012 and their parents) need scope-aware reassessment in their owning lists/evidence before reuse as complete current acceptance. Those locations are outside scope, so no pending note or checkbox change is made here.

The package README and feature PLAN/TASKS retain preparation-era incorporation boundary wording; their later continuation must account for this SPEC checkpoint and its QC without treating the entire package as incorporated. Active sources remain required by feature planning/tasks/links and unfinished implementation. Archival, task ownership transfer, hosted reparenting/projection and final feature-to-phase integration are deferred. This selected SPEC checkpoint may finish on the existing feature branch without claiming whole-project readiness or implementing ranges.

## Revision 2 — Accepted governing-owner incorporation recheck

Owner assessment: sdd-specify under sdd-integrate-feature correction ownership, 2026-10-05.

S-1–S-3 whole-input API/value/decode/lifecycle map to facade/core/io; S-4/S-5/S-8 option validation, named-file ranges and formatting map to cli plus source-independent core/io seam. S-6 remains later borrowed stdin without ranges. S-7 maps tests/docs/build. Accepted design/PROJECT incorporation resolves stale future-range exclusions without new contract or public API. Every objective row/error/BOM obligation remains owned and assessable. No focused children or confirmed unresolved finding.

Exact reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e143b7d27c5b097e4404c1a1c4d2e571dfe1229446e334e61de527afe4a9207e`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `a513c7c51ce1a1f125f1fb737537381dbcc907f328b58b1026cced7f7d9a1dde`
- `FEATURE-SPEC.md`: `e5c45a21e3fd9b8b9f507f5a82ac1e06f6c04c9c0673ce409a9a86bb04ccaeed`
- `FEATURE-PLAN.md`: `fca8d080af1594d7e6664692477d7afd97bd5b78af28139cb4d3126946ff223c`
- `FEATURE-TASKS.md`: `327ec8646733d7c40e19092d02b309c5ee98352ffadb3444df975f97c7018cd8`

Whitespace/local-link checks and complete selected-root consistency review passed. Original observations and identities retained above. Gate: Ready for current selected conformance; implementation/hosted closure/archive/merge remain separately assessed.

## Revision 3 — Final range incorporation and archive conformance

Selected complete main owner reassessment, 2026-10-05. Accepted contract/design scope unchanged; PLAN2.4 now refers to canonical S8/main QC, and TASKS references S8/main readiness with sole T018–T022 ownership. Historical feature sources and adjacent reports moved together into features/002_ea97182, with local links repaired; main roots are standalone intended descriptions. TASKS status/reassessment changes have implementation evidence in T021/T022 reports and do not alter task decomposition/dependencies. S1–S8 routes, delivery counts/rationale and boundary obligations from previous revisions remain applicable. Original findings/identities retained, no unresolved conformance finding. Main Phase2/stdin/final review remain incomplete.

Exact current reviewed/governing SHA256:

- `PROJECT.md`: `289e8cd7356ac224beb073a3edb352adb73d2c48d636e1ce5fbe1791bdbc4988`
- `ARCHITECTURE.md`: `4cf11af91266438fbc1baf69ca51d64400eb0f64ce82fc0b48e5ba61d720ca0a`
- `DECOMPOSITION.md`: `bdccc4d9365d2733a4f2f168dcd8a15d17b7f93ac4dece431e5e1cdd455e1e15`
- `SPEC.md`: `fc99b2e6314aeaffa1f1bbcb71df3cb64fe43dd1517664357b5cf4456659fc7d`
- `PLAN.md`: `e1aa667a8bea06ed9feb9211697a9d70ac3f75b688f1f877ee4d38443cd8c629`
- `layout.md`: `abab95bf824a28080034bdcca7737acdfe48e74f665521139a118918fa6bff32`
- `TASKS.md`: `88086b1fb8853d5357bc245fb56e5d089589a8b5b9dbcb353e08d30ddc3182de`

Full selected-root consistency, main/archive links, unique task ownership and whitespace checks passed. Gate: Ready for current main conformance; historical archived Ready does not govern dependent use. Feature implementation and published integration are assessed separately.

## Revision 4 — JSON removal focused owner recheck

Reviewed current roots directly against the selected human JSON-removal objective and retained counting/BOM/API/range/source boundaries. No focused children changed. Exact SHA256 identities:

- PROJECT.md: `23ad8f583e821004e74dfafe815c5be78cc1c0734790d95ef3e06c37c66d1527`
- ARCHITECTURE.md: `d956e2c505971def1b5a6463d478f10264601de8f72afe2cec45ee993012aeaa`
- DECOMPOSITION.md: `c378dcc1247436d0d67a80dcf49d6a781335674ba489dcd50da2086f8c98fd1c`
- SPEC.md: `2d0d904bc337c66919b45927ed0b784295ca67b190598d2e7bdf4bc9123fe8e3`
- PLAN.md: `58c03a18e862ffdd7bd7cd6cd6a5a89ae8194da5614ae95872580b1ef057703f`
- TASKS.md: `4731343bcbfe8d9992648df48fd6782ff0ec98a79a2703ffba336ed02e6cd45f`
- layout.md: `815e6a65252b15d4941cf1abff9b2c3e0119cb0a8d692689dd4dbe35c2c5929c`

S-1–S-3 map unchanged to facade/core/io; S-4/S-8 map text rendering and no-acquisition validation to cli plus decoded selection; reserved S-5 explicitly rejects --json while literal paths after -- remain valid. S-6 retains pending strict binary borrowed stdin, text/BOM and no stdin ranges; S-7 maps docs/tests/distribution. PROJECT/design agree, no serializer obligation remains. Complete retained objective rows/errors/lifecycle and dependency ownership inspected. No confirmed conformance finding; Ready for selected current conformance, not implementation acceptance.
