# Named-file line ranges delivery plan

Active delta: [FEATURE-SPEC](FEATURE-SPEC.md), [package identity/design](features/002_ea97182/README.md). The reviewed specification is Ready. Preserve main [PLAN](PLAN.md) and [TASKS](TASKS.md): JSON2.1 is complete at T-012; stdin2.2 and main review2.3 remain incomplete. This feature reuses Phase2's identity with new feature-only milestone IDs2.4/2.5, allocated after existing2.1–2.3. Numerical order does not impose a stdin dependency. Feature progress measures only the delta and cannot complete Phase2.

## Phase 2 — Output and source extensions

### Milestone 2.4 — Named-file line ranges

Prerequisite: completed/published JSON milestone2.1/T-012 at the pinned paused baseline, current feature SPEC/design QC and separately authorized implementation. No prerequisite on unfinished stdin or main final review; whole-input named-file text/JSON already works. Delivery retains the useful baseline while introducing a source-independent normalization/selection seam, then composing command validation/acquisition/rendering into a named-file slice. Pure helper work is a bounded prerequisite to the earliest usable changed CLI path, not a released skeleton.

Scope: R-1–R-4 and retained S-1–S-5/S-7 at named-file boundary. Deliver grammar/repetition checks before input acquisition, complete decode before range selection, one BOM policy, preserved terminators, unbounded decimals, text/JSON and BOM option composition, EOF behavior and API/lifecycle compatibility. Checks accompany each behavioral increment. Complete user documentation and extracted-source acceptance before the milestone exit.

Exit: actual module invocation counts selected named-file lines in text/JSON with exact stdout/status/stderr; supplied examples, ASCII/leading-zero/huge decimal/rejected syntax, malformed bytes after END, BOM/EOF/terminator boundaries pass. Default CLI, whole-input API and file lifecycle/unchanged input regress successfully. Independent nonempty product suites and clean extracted-source range invocation pass; README/module examples run. Required final milestone code review, relevant testing, blocker repairs and committed/pushed report establish all exits. Demonstrate 2:3, beyond-EOF and a rejected range without acquisition; this informs the human's continue/amend/simplify/stop decision about syntax and usefulness.

### Milestone 2.5 — Range feature review

Dedicated single feature-scoped phase review/testing/report outcome after delivery milestone2.4 completes/closes when tracking is active. Exit: cross-component range/API/BOM/format/decode/lifecycle/docs/distribution acceptance, prior finding disposition, blocker repair and committed/pushed feature phase report. Aggregate feature TODOs and final feature implementation report. This is not main milestone2.3/T-017 or a whole-project Phase2 completion claim.

A full separately authorized feature implementation must incorporate accepted in-scope feature documents and reconcile task ownership before final feature merge into the established paused phase target; main stdin tasks retain incomplete state. Incorporation triggers affected main QC and rechecks changed review dependencies without renumbering T-017. Preparation stops on the published feature branch before implementation, incorporation/archive or merge.

## Layout and integration constraints

Reuse [layout](layout.md): core owns pure normalization/selection/counting; io owns complete named-file UTF-8 acquisition; cli owns validation, command composition, diagnostics and renderers. Private acquisition factoring may allow the command to obtain decoded text while count_file remains whole-input. The selected slice is counted with stripping disabled. Future stdin can call the same decoded-text seam; no borrowed source is acquired/delivered in this feature.

Pure/helper and parser/lifecycle checks belong under tests/unit; real file/module and isolated extraction checks under tests/integration. README/docs/module describe the feature; docs/api retains whole-input signatures. Existing Makefile archive includes updated package/docs with no workflow fixture substitution. Feature review reports reside under features/002_ea97182; preparation QC reports remain adjacent to active FEATURE roots. No new source home or main layout edit is required.

## Activation, risks and boundary

Preparation creates no label, milestone, issue or PR. If separately implemented while Phase2 remains active, project the added feature work in that active phase before first execution, preserving managed IDs and existing issue/milestone ownership. The feature delta must not close Phase2 or existing2.2/2.3.

Primary risks: argparse silently accepts repeats; unrestricted integer-string conversion hits interpreter limits; splitlines treats Unicode separators as terminators; range processing strips an interior BOM twice; slicing hides late bad UTF-8; helper factoring changes whole-input APIs/resources; distribution imports the checkout. Planned evidence explicitly addresses these risks. One delivery milestone plus mandatory feature review is intentionally small: the bounded named-file option has one coherent changed end-to-end outcome, and splitting text/JSON or validation into artificial release milestones delays usefulness. No unresolved delivery decision remains.
