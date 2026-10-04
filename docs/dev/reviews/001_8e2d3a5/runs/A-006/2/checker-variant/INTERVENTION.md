# CHK-002 disclosed checker variant

Original helper SHA256: 72ddbe9d32d4655659582e23e4be9645ab7c3abf19209120fc9ab95608eddb80

Root cause: default ownership discovery recursively includes ignored generated distribution copies. Variant replaces only candidate inventory with Git tracked plus nonignored untracked paths. Explicit additive documents, path/symlink protections, parser, malformed/empty/duplicate refusal and every other assessment check stay unchanged. Original helper and failed results retained. Product/pinned-package bytes unchanged. Variant stops on original identity or exact function mismatch. Regression fixtures are disposable local Git inventories, with no clone, remote/provider operation or product mutation. They establish checker sensitivity only, not live acceptance. Independent assessor must verify candidate completeness and use actual captures for final case assessment.
