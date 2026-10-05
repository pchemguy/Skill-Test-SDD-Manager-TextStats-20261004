# A-010 completed continuation

T-018–T-022 are fully implemented, verified, committed, published and integrated into paused Phase 2. Named-file `--lines START:END` / `--lines=START:END` now supports text/JSON selection with ordered positive ASCII endpoints of arbitrary length, validation before acquisition, complete strict UTF-8 decode, exactly one complete-input BOM policy and preserved logical-line contents/terminators. Public APIs remain whole-input; stdin is not delivered.

| Task | Published commit |
| --- | --- |
| T-018 | `905d7a851124235db27f4f5a553ee39729957a44` |
| T-019 | `9ade315a9f6ded1fade6f457a504f5e07e58fba5` |
| T-020 | `749a89844249d3b1c5ebb04c459d7e66bcb3ed2e` |
| T-021 | `3f93cd40d90001ee7e4f54b36c764d1d5067b72e` |
| T-022 | `d518cc23650018542e43d8fb5a63f44a4d283518` |

On Python 3.12.14, independent unit discovery passes 21 tests and integration discovery passes 13 tests, without skips. The same suites pass on the prospective merged state (unit 0.053s; integration 11.032s). Pure helper RED observed two missing-seam failures; actual command RED observed 73 unknown-option failures before relevant production changes. Documentation/extraction tests characterize already delivered behavior without manufacturing RED. Verification covers both range spellings/formats/options/orders, all supplied logical-line/BOM/Unicode/EOF rows, huge endpoints/leading zeros, malformed/repeated syntax before acquisition, bad UTF-8 after END, whole-input API/signatures/silence/resources/files/default CLI regressions, runnable public examples and isolated extracted package identity/range/BOM/error behavior. Links, 22 unique executable task IDs, archived source disposition, whitespace and preserved paused statuses pass. Python 3.11 execution is not claimed. Separate milestone and feature code reviews found no defects or deferred TODOs.

Main PROJECT/ARCHITECTURE/DECOMPOSITION/SPEC/PLAN/layout/TASKS and affected preparation QC are reconciled. TASKS owns every executable entry exactly once. Accepted feature sources and their adjacent QC are historically archived under `docs/dev/features/002_ea97182/`; milestone/phase/implementation reports remain there. Current affected historical named-file/JSON acceptance reassessment is resolved against scoped regression evidence. No whole-project completion is inferred.

Issues #18–#22 are closed with completed reason after verified publication. Milestone #7 (2.4) is closed with 0 open / 4 closed; #8 (2.5) is closed with 0 open / 1 closed. Final readback confirms unfinished #5/#6 remain open with 4/1 issues. Evidence comments are #18:5995267730, #19:5995378177, #20:5995384077, #21:5995434213, #22:5995630245. No duplicate comment was created.

Explicit two-parent merge **`0e4741465c3e086d2ab95c5af73ca89371c16fac`** is published to `phase/2-output-and-source-extensions`. Parents are paused target `ea97182d2d6a3984599238312a13e78d54d3221a` and verified feature `d518cc23650018542e43d8fb5a63f44a4d283518`. No conflicts occurred; merged and committed tree equals the verified feature tree. Separate live readback confirms both feature and target exact tips. Main remains `59debb649545125dd3aa00377ea115451b594271`.

The original final feature-push automatic approval rejection is retained in JOURNAL.md: it cited an unverified GitHub destination and missing explicit repository/data-disclosure authorization. Parent supplied actual human “Full workflows must include pushes” and current “Resume”, established destination, exact owned commit/checks and the prior rejection through supported same-Git authorization reassessment. Publication then succeeded; no bypass or unchanged denied retry occurred. Initial issue #18 closure had an unknown preHTTP failure; assisted same-adapter recovery and consumer readback confirmed closure. Later #19 read transport failure was resolved by readonly connector readback. A #22 comment transport failure was read back as absent before one bounded same-adapter retry; it succeeded without duplication. Obsolete session8325 cancellation returned unknown process ID, with no replay. No unresolved blocker remains.

Tracked worktree/index are clean. Unrelated `-json-9l969okj/sample.txt` remains untracked, excluded and unchanged with SHA256 `f1945cd6c19e56b3c1c78943ef5ec18116907a4ca1efc40a57d48ab1db7adfc5`. Pinned workflow resources remain unchanged. Credentials and protected helper source were neither inspected nor modified. Actual loaded pinned skill hashes and nonsecret command/result details are in JOURNAL.md.

Stopped after verified published feature integration into paused Phase 2. Phase 2/T-013–T-017/stdin remain incomplete; no Phase 2-to-main integration or remaining implementation was started.
