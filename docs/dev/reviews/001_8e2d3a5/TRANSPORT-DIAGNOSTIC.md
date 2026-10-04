# API transport diagnosis and recovery

## Observations

On resume, the earlier repository-scoped Python/urllib REST command failed at the tool boundary with `Network access to https://api.github.com:443 was blocked by policy`. Git remote readback and the authenticated GitHub connector remained available. The connector lacked native repository-label and milestone creation/inventory methods.

The coordinator generalized that one observed failure into an assertion that direct API access was blocked for the session, placed the assertion in A-003's consumer handoff, and proposed browser fallback. That conclusion was too broad. At the user's explicit request to try curl, a credential-free repository GET returned HTTP200. A protected authenticated curl transport then read native milestones and labels with HTTP200: zero milestones and ten existing default labels. No objects were created by these probes.

## Effect on the run

A-003's first attempt stopped without hosted writes under the coordinator-supplied transport constraint and actual missing connector methods. It remains retained as Blocked; it is not evidence of a plugin defect. The user-directed client probe restored an available path without browser fallback. A separately recorded fresh consumer retry will execute the requested projection/reconciliation using existing connector tools and the scoped curl transport.

## Actions and safeguards

Created a generic dedicated-repository curl REST adapter under private Git administration storage. Existing token is passed to curl through stdin configuration; it is absent from command arguments, URLs and logs. Default curl configuration and redirects are disabled; JSON output is allowlisted and recognizable credential values withheld. No token was replaced or copied from the source repository. Tested native parent inventory only; pinned plugin/source unchanged. The adapter supplies transport, not workflow decisions or simulated acceptance.

## Diagnosis and proposal

The recorded Python-transport failure is real; its underlying cause is undiagnosed. The later curl success does not distinguish a Python-specific problem from a transient/runtime policy condition. The assertion that all direct API access was unavailable is withdrawn. Keep conclusions scoped to observed client, endpoint and time; where permitted, test a credential-free read through another available client before declaring a whole workflow unavailable. Retain failed probes and interventions. No SDD Manager source change has been made for this matter.

The run also retains a separate review correction: an assessor carried an intermediate draft finding into the completed-proposal assessment. The completed original RESULT already contained all nine issues and three milestones. Assessment Revision1 withdraws that stale finding; initial assessment history and later redundant validation remain preserved.
