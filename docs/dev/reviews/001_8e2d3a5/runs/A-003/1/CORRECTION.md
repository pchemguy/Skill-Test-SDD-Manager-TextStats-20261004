# A-003 recorded assisted correction

This is an assisted correction to the external reviewable proposal. It is not a case pass, retry of hosted writes, or evidence that erases the blocked original attempt. No hosted change has been executed. The lack of native milestone and repository label capabilities still blocks both requested hosted passes.

## Reported defect and observed entry state

Root's independent review reported an initial proposal defect: the multiline task-title regex greedily included the remaining Phase 1 TASKS through T-009 in the T-001 title, omitted substantive scope/acceptance, and failed to emit three native milestones or separate T-002–T-009 drafts. That failure occurred in the first draft generator and invalidated that draft's count claim.

At the start of this assisted correction, the existing RESULT.md actually contained nine proposed issue headings and three native milestone headings; it had previously been corrected in the originating turn. That observation is recorded separately from the reported original defect, rather than claiming the reported defective bytes were present at correction entry. RESULT.md was not edited in this assisted correction. Its entry and final SHA-256 are both `ab45359a34c6c56b95c8eceb6c6c4baa48725b397c251a516bed80065dfc2854`; byte equality was asserted against its complete entry bytes.

## Actual correction

Created `PROPOSED-HOSTED-CHANGES.corrected.md` separately from actual TASKS and PLAN sources, using a line-oriented parser with exact heading/checklist indentation and single-line task titles. Selected only owning Phase 1, retained exact stable task/milestone IDs, supplied native milestone outcome/prerequisite/exit descriptions and preserved each task's full scope, dependencies, evidence and required report path. Every object is explicitly proposed/unexecuted, with unresolved hosted numerical IDs. Parent associations are 1.1: T-001–T-004; 1.2: T-005–T-008; 1.3: T-009. No source or plugin amendment was needed.

## Actual validation and state

Python read back the written corrected proposal and ran these explicit assertions, all true:

- `one_phase_label`: `true`.
- `three_milestones`: `true`.
- `nine_issues`: `true`.
- `unique_task_ids`: `true`.
- `concise_single_line_titles`: `true`.
- `substantive_scope_dependency_acceptance`: `true`.
- `report_paths`: `true`.
- `balanced_exact_markers`: `true`.
- `correct_parent_mapping`: `true`.
- `original_result_byte_exact`: `true`.

Product checks used `git --no-optional-locks -C /workspace/scratch/textstats-live-20261004 status --porcelain=v1 --untracked-files=all` (empty, clean) and `rev-parse HEAD` (`4c275cc46fc0163c9e1e50871d3cc33c4c38567e`). No product file change, plugin change, hosted mutation, branch change, commit, push or merge was performed. No browser, credentials, assessor contracts or coordinator materials were consulted. Product tests remain unrun because this stops before implementation.

Corrected proposal SHA-256: `75a678c7877075b614d33005b7c2ef6e2849f566b9d4a5895749d0f06175e929`.

## Exact source identities

- `docs/dev/PROJECT.md`: SHA-256 `85f1c34aee621b56642cbf0ce61120da98ac27a01f690eb5e42ad3020709dc24`.
- `docs/dev/ARCHITECTURE.md`: SHA-256 `0237bf724eec1f18300d68024ca3afa4e96de753479b359655308afe5618cf6c`.
- `docs/dev/DECOMPOSITION.md`: SHA-256 `d9fa49ddb1e7a2548d7a9606482d3e5a2ca80346f52f11efb3252effe0e55a2d`.
- `docs/dev/SPEC.md`: SHA-256 `8cfd533f70463882dac3acf12930f17e22f5cd0d57266815fad02aae977c77eb`.
- `docs/dev/PLAN.md`: SHA-256 `8ff3ef53f126a79987490f28ad2f554842630c096c13f441111b55d796279bb8`.
- `docs/dev/layout.md`: SHA-256 `ffb4c1d632739889febf10515bf52e6db4596ce763ae5c4f7a66773e708a3e0d`.
- `docs/dev/TASKS.md`: SHA-256 `2e0af38698b5edf3911265da98815790143e2e5c1500b3bc04148ead2b9a8454`.
- `docs/dev/SPEC-REVIEW-REPORT.md`: SHA-256 `e4522d4a6d566d3dd6c7b208930547f152229ca3dd9a04028ce136a937a0df68`.
- `docs/dev/PLAN-REVIEW-REPORT.md`: SHA-256 `01f3041e8ccd688060ff51e0c7dd825475d44dfbcca73c31910bab038e231591`.
- `docs/dev/TASKS-REVIEW-REPORT.md`: SHA-256 `7a7e8f361bd18f4a6e5f580d87cc8f9757996be2fdbb214c44d59ca321404412`.
- `textstats-run-resources/plugin/skills/sdd-forge/SKILL.md`: SHA-256 `21cba41d7d64fc54206dc981fab665b16b7b868e4fe1c75769048a59b294b9b4`.
- `textstats-run-resources/plugin/skills/sdd-forge/references/github-projection.md`: SHA-256 `7124759c2c3aa98d909d62b64db302d76d65ed35701ec22d47cc6a20a38d17a8`.
- `textstats-run-resources/plugin/skills/sdd-conventions/references/task-hierarchy.md`: SHA-256 `675d67a8a7487c7876e084276638a966072d177f56376d3c156eec29c9b90a75`.
- `textstats-run-resources/plugin/skills/sdd-report/references/object-drafts.md`: SHA-256 `f0c894eb233713f18cb48ac2a1f8ecea474c7891276f948443b8cc16462391fc`.
