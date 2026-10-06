"""Execute public code fences against isolated extracted product sources."""
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile

root = Path('/workspace/scratch/textstats-live-20261004')
environment = {key: value for key, value in os.environ.items()
               if key not in ('PYTHONPATH', 'PYTHONHOME', 'PYTHONSTARTUP')}
environment.update(PYTHONDONTWRITEBYTECODE='1', PYTHONNOUSERSITE='1')
executed = skipped = 0
with tempfile.TemporaryDirectory() as directory:
    temporary = Path(directory)
    build = temporary / 'build'
    run = subprocess.run(['make', 'dist', f'DIST_DIR={build}'], cwd=root,
                         env=environment, capture_output=True, text=True)
    assert run.returncode == 0, run.stderr
    extracted = temporary / 'extracted'
    extracted.mkdir()
    with tarfile.open(build / 'textstats.tar.gz') as source:
        source.extractall(extracted, filter='data')
    for relative in ['README.md', 'docs/module.md', 'docs/api.md']:
        path = root / relative
        text = path.read_text()
        for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', text):
            if '://' not in target:
                assert (path.parent / target).exists(), (relative, target)
        for index, (language, block) in enumerate(re.findall(r'```(python|sh)\n(.*?)```', text, re.S), 1):
            if 'unittest discover' in block:
                skipped += 1
                print(relative, index, 'suite block verified independently')
                continue
            statuses = re.findall(r'# status (\d+)', block)
            expected_status = int(statuses[-1]) if statuses else 0
            command = [sys.executable, '-c', block] if language == 'python' else ['bash', '-c', block]
            run = subprocess.run(command, cwd=extracted, env=environment,
                                 capture_output=True, text=True)
            assert run.returncode == expected_status, (relative, index, run.returncode, run.stderr)
            expected_counts = re.findall(r'# (lines=\d+ words=\d+)', block)
            observed_counts = re.findall(r'^lines=\d+ words=\d+$', run.stdout, re.M)
            assert observed_counts == expected_counts, (relative, index, observed_counts, expected_counts)
            if 'stderr identifies stdin' in block:
                assert 'stdin' in run.stderr and not run.stdout, (relative, index)
            if 'stderr identifies nonexistent.txt' in block:
                assert 'nonexistent.txt' in run.stderr and not run.stdout, (relative, index)
            print(relative, index, 'passed', 'status', expected_status)
            if run.stderr and expected_status == 0:
                print('observed successful-example stderr:', run.stderr.strip())
            executed += 1
print(f'{executed} public code fences passed; {skipped} suite fence independently covered; local links passed')
