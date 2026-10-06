# Protected transport interface clarification

During resumed startup the consumer tried RESOURCE values with a leading slash and full repository prefix. Both were rejected by the adapter before HTTP with AssertionError. The coordinator supplied the observed interface from the retained successful A-003 command journal: repository-relative RESOURCE with no leading slash (for example issues?state=all&per_page=100&page=1); writes take an existing nonsecret body JSON filename. Full issue bodies are read through the connector because this adapter omits them. This is an adapter handoff clarification, not a tested-source or product requirement change.

The platform rejected a redundant initial push. Read-only remote reconciliation established no outstanding startup publication; no retry or alternate transport was needed for that operation. New completion publication remains subject to platform review and existing scoped human authorization.
