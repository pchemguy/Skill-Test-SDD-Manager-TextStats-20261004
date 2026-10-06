"""Assessor-only explicit local URL observation adapter; shipped core unchanged.

Reproduces the executed in-memory core.repository replacement. The fixed
source hash guards the original helper implementation. Only repository
identity/discovery metadata is adapted; remote readback, Git observations,
ownership and all contract checks use original core functions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

EXPECTED_CORE_SHA256 = '72ddbe9d32d4655659582e23e4be9645ab7c3abf19209120fc9ab95608eddb80'


def assess(harness, inputs, state, contract, destination=None):
    core_path = harness / 'scripts/core.py'
    if hashlib.sha256(core_path.read_bytes()).hexdigest() != EXPECTED_CORE_SHA256:
        raise RuntimeError('Original core.py source guard failed')
    sys.path.insert(0, str(harness / 'scripts'))
    import core
    root = inputs['local_checkout']
    remote = destination or inputs['test_repository']
    read = core.remote_read(root, remote)
    repo = {
        'identity': remote,
        'local_checkout': root,
        'remote': remote,
        'remote_url': remote,
        'integration_branch': None,
        'remote_observation': read,
        'head': state['checkpoint_refs']['product_commit'],
        'existing_runs': [],
    }
    original_repository = core.repository
    try:
        core.repository = lambda inputs: repo
        return core.assessment(inputs, state, contract, None)
    finally:
        core.repository = original_repository


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--harness', required=True, type=Path)
    parser.add_argument('--inputs', required=True, type=Path)
    parser.add_argument('--run-state', required=True, type=Path)
    parser.add_argument('--contract', required=True, type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--observation-destination')
    args = parser.parse_args()
    if args.output.exists():
        raise RuntimeError('Refusing occupied output')
    result, code = assess(args.harness, json.loads(args.inputs.read_text()),
                          json.loads(args.run_state.read_text()), args.contract,
                          args.observation_destination)
    result['variant_disclosure'] = {
        'changed_function': 'core.repository (in memory only)',
        'original_core_sha256': EXPECTED_CORE_SHA256,
        'metadata': 'Explicit authorized local URL, checkout, actual remote_read result; no configured-remote identity lookup',
        'unchanged_checks': 'core.assessment/core.observe_git/core.ownership and original contract',
        'source_or_product_writes': False,
    }
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': result['status'], 'exit_code': code}))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
