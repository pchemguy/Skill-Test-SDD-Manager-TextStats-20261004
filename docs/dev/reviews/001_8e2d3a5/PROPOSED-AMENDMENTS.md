# Proposed TextStats acceptance amendments

## Purpose and status

Batch 1 repairs the acceptance harness prerequisites, interruption controls and grading that left seven cases blocked. It prioritizes important behavior that can reasonably be tested and separates complex facility-dependent scenarios into optional, non-blocking coverage. These are proposed changes to the plugin repository's `acceptance/textstats/` bundle, not TextStats counting-code changes.

This document is requested follow-up to the [final diagnostic report](DIAGNOSTIC-REPORT.md). The assessed source remains SDD Manager 0.14.3 at `019eb354cf0921ebd6056e6579763ac33d0baec2`. The completed campaign's published stop checkpoint is `93a3428e23f0a3ba93ff45693a3793db3a102c8e`; its result remains **20 Passed / seven Blocked**. Creating this proposal does not implement the amendments, rerun cases, or retroactively regrade independent assessments.

## Batch 1 policy: required behavior and optional extended scenarios

Grade independently executable checks independently. Do not let an unavailable advanced scenario erase a verified core result, become a product failure, or block unrelated required work. Equally, do not turn missing evidence into a pass.

Each case or variant must declare its purpose, whether it is required or optional, evidence class, prerequisites, and execution requirements before dispatch. Ordinary completion, prerequisite refusal, controlled fault handling, interrupted recovery and live provider recovery are different claims and must have distinct criteria and results.

| Classification | Result and reporting | Effect on campaign readiness |
| --- | --- | --- |
| Required core check, executed | Passed or Failed from observed behavior and independent evidence | A failure prevents required acceptance. |
| Required core check, unavailable | Blocked, with the exact prerequisite or harness defect and repair action | Required acceptance remains incomplete; no product defect inferred merely from unavailable setup. |
| Optional extended scenario, executed | Passed or Failed, with evidence class and findings | Report separately; it does not automatically block core acceptance. A reproduced defect that also violates a required contract must be escalated against that contract. |
| Optional extended scenario, unavailable or not selected | Not run, optional/non-blocking, with reason and full-execution requirements | Excluded from required acceptance counts; never reported as Passed or as a required failure. |

Show required totals and optional totals separately. State which profiles and environments were actually covered. A required-core pass does not establish full native, installed-client, live-provider or cross-machine acceptance. Optional cases must not become prerequisite gates for required cases. Do not downgrade a difficult ordinary core check merely to obtain a green result; optional status is for clearly identified advanced scope with justified facility requirements.

## Ordered amendment queue

All paths below are relative to `acceptance/textstats/` in the owning plugin repository. Stable A-014 through A-026 IDs remain; distinguish variants beneath them rather than renumbering historical cases. Proposed variant names below are design labels, not existing catalog entries.

| Action | Proposed amendment and affected owners | Objective recheck |
| --- | --- | --- |
| B1-001 | Add required/optional variant classification, evidence class and capability eligibility to `cases/catalog.json`, assessor contracts, configuration/checkpoint schemas where necessary, `cases/assessor/catalog_tools.py`, coordinator scripts and reporting. Update `OBJECTIVES.md`, `SETUP.md`, `EXECUTION.md`, `RECOVERY.md`, `DIAGNOSTICS.md` and role guidance consistently. | Validate every variant's metadata and dependency graph. Reject a required dependency on an unavailable optional variant. Demonstrate separate required and optional counts, including an unavailable optional scenario that leaves required readiness unchanged. |
| B1-002 — A-014 | Repair `cases/consumer/A-014.md`, its assessor guide/contract and catalog binding. Required cross-phase execution starts at an actual checkpoint with outside prerequisites complete; its selected scope permits required commits, pushes and integration. Keep the incomplete-prerequisite refusal as a separate required check. | Observe first-phase exits/review, explicit merge and publication before the next phase starts; stop at the selected range. Separately verify refusal without unauthorized prerequisite execution or mutation. |
| B1-003 — A-017 | Supply a deterministic, contract-valid acceptance failure at the starting checkpoint and an observed failure boundary. Update case setup, consumer request, assessor assets and interruption controls. Do not use an invalid assertion or arbitrary nonzero exit as the required product failure. | Independently establish why the starting implementation fails the valid contract. Observe the consumer encounter that failure, interrupt at the selected boundary, preserve state, and give a fresh consumer the continuation. Verify scoped repair, nonempty passing checks and publication; retain the original failure. |
| B1-004 — A-019 | Replace the incomplete A-005 milestone binding with a verified complete phase, such as the actual A-006 completion boundary or a separately established eligible boundary. Prepare controlled divergence in an isolated target while preserving the real source and target identities. Update the catalog dependency, renderer, requests and assessor expectations together. | Reject an incomplete-phase fixture in preflight. At the eligible boundary observe a real conflict or merged-state check failure, preserve pending state, then independently verify fresh recovery, two-parent merge, merged checks and exact target publication. |
| B1-005 — A-021 | Replace polling-dependent interception with a bounded control between actual selected transfer operations. The control belongs to the test fixture; it must not add mandatory journals or test hooks to ordinary product workflows. Update case setup, `cases/consumer/INTERRUPTIONS.md`, handoff controls and assessor evidence. | Capture a genuine state with at least one selected transfer completed and another pending, including actual owner/link/index evidence. Interrupt and resume in a fresh context; verify no lost or duplicate task ownership, correct links, preserved unrelated edits and coherent publication. |
| B1-006 — A-023 | Split ordinary uncertain-effect reconciliation from extended live-provider response-loss scenarios. Required core checks may use a disclosed controlled facility with independently observable effects; label their evidence accordingly. Actual GitHub write-applied/response-lost variants are optional and non-blocking when no suitable hosted setup is available. Update requests, contracts, catalog and publication criteria. | Core tests demonstrate readback before retry, reuse of an already-applied effect, bounded retry of an unapplied effect and no duplication. A separate optional live run must establish actual provider mutation, discarded response and independent provider readback; controlled tests never count as live acceptance. |
| B1-007 — A-024 | Split reasonably testable access classification and bounded handling from complex native credential/session failure and recovery. Required checks assess sanitized denial, rate-limit and unavailable-access handling. Native protected handoff, real expiry/revocation and fresh native recovery are optional/non-blocking extensions. See the detailed contract below. | Required checks pass independently of optional facility availability, with preserved state and no secret exposure. Missing native facilities produce an explicit optional Not run result, not an overall required Blocked result. |
| B1-008 — A-026 | Separate empty collection, genuine pre-existing baseline failure and verification-only preservation. Supply an isolated fixture with an independently reproduced assertion failure and no consumer repair authorization. Restrict local-only assessor helpers to local checks; remove implicit hosted reads from that mode. | Reject zero-test acceptance; show an actual nonempty failing baseline; verify accurate attribution and unchanged source/task/index state. Local assessment completes without hidden network reads. Passing ordinary baseline tests do not substitute for the failure variant. |

## A-024: required checks and optional native recovery

Retain A-024 as the parent identity, with independently graded core and extended variants. The current case couples classification and complex recovery; that coupling should be removed. If implementation review concludes its existing contract is entirely native recovery, classify that entire contract as optional/non-blocking and add a separately defined core classification variant. Do not mislabel the native contract as a core pass.

### Required core: access classification and bounded handling

Use separate actual consumer-visible controlled operations for permission denial, rate limiting and unavailable authenticated access. The fixture may inject sanitized faults through a documented adapter. The report must say that these are controlled faults, not actual provider denial or credential expiry.

Check that the consumer:

- Distinguishes access denial, rate limiting, transport failure and unavailable authentication from a product/test failure.
- Preserves valid work and identifies the exact pending operation and destination.
- Applies bounded retry/backoff or stops appropriately; a rate limit does not trigger credential replacement.
- Keeps Git publication recovery and API access recovery distinct.
- Uses an available supported protected mechanism when recovery is selected, without putting secret values into prompts, arguments, logs or reports.
- Resumes the same bounded operation after the controlled facility is restored, with independent readback where applicable and no duplicate effect.

Credential replacement is not necessary to prove classification, state preservation or bounded handling. Restoration of a controlled wrapper proves only that bounded continuation. Grade these checks from their own evidence rather than withholding their result because native protected handoff cannot be exercised.

### Optional extension: native credential/session recovery

Report this as **optional, non-blocking native authentication recovery**. Full execution requires a supported client/protected input facility, an isolated recoverable access configuration, a controlled genuine unavailable/expired/invalid credential condition, and independent same-destination observations before and after recovery. Where the contract specifically requires ignored/untracked credential reuse, demonstrate that eligibility through supported nonsecret evidence without reading or exporting the credential value.

Preserve the actual failure and use a separate fresh continuation when that is the scenario. Never invalidate ordinary campaign credentials simply to force a test. Do not substitute scripted error responses, wrapper restoration or token possession for demonstrated native recovery.

If facilities are missing, report: the precise unexecuted recovery behavior; the missing client/control; what was tested by the core variants; and what setup would enable the extension. Its status is optional Not run, with no reduction of required-core readiness. If it executes and fails, retain the failure and investigate its cause; optional classification does not conceal a confirmed contract defect.

## Other complex scenarios and capability reporting

A-023's optional live scenarios require a legitimately identified isolated hosted project/campaign, narrowly scoped operations and a mechanism that discards a response after the real write applies. A separate repository is one possible arrangement, not an automatic requirement; a separate campaign in the same repository is eligible only if its identity/object isolation is established. Do not reopen completed positive-campaign objects or create duplicate managed task identities as a substitute.

Keep safely reproducible local interruption/recovery behavior in required coverage. If a particular extension requires unavailable platform-native interruption, installed-client routing, hard filesystem isolation or another specialized facility, name that extension and its requirements explicitly and classify it separately before the run. A general environment limitation must not silently downgrade all checks in a case.

Preflight must establish the exact starting commit, actual dependency completion, legitimate integration boundary, permitted destination, required access and available trigger controls. Missing setup should produce a precise preparation diagnosis before consumer dispatch. It must not be presented as a product failure. Record successful eligibility separately from runtime acceptance.

Deterministic interruption controls must observe the selected action before holding it, retain the unfinished state, and support a fresh continuation. They must have sensitivity checks that reject a missing trigger or already-completed operation. Do not manufacture product completion records or alter the frozen plugin to inject a trigger.

## Implementation, regression and rerun boundary

Implement the proposals in a separate owning-source revision. Preserve this campaign's original inputs, assessments, frozen package and publication history. Record a new full source SHA and harness identity for any rerun; do not retrospectively mark the seven historical cases Passed or replace their grades with optional status.

First implement the classification/reporting and capability preflight, then repair the individual cases and deterministic controls. Run catalog/schema/renderer validation and meaningful sensitivity tests for unavailable optional scenarios, incorrect prerequisites, already-completed triggers, duplicate-effect recovery and local-only access. Changes to shared coordinator or grading behavior require targeted regressions of previously passing consumers or retained fixtures as appropriate; support tests alone do not demonstrate live plugin acceptance.

Rerun the affected required variants with fresh consumers and independent assessors. Execute optional extensions only when their declared facilities are available and selected. Publish required totals, optional executed totals, optional Not run totals, actual evidence classes and outstanding findings separately. Required acceptance may complete with optional coverage unavailable; the report must still state the narrower demonstrated scope.

This batch proposes no TextStats production-code changes. Existing [authorization amendments](runs/A-004/1/AUTHORIZATION-AMENDMENT-PROPOSAL.md) and their [supplement](AUTHORIZATION-AMENDMENT-SUPPLEMENT.md) remain separate proposals; they are not withdrawn or implemented by this document.
