"""Disclosed CHK-002 assessor-only variant; original helper remains unchanged."""
import hashlib
import importlib.util
import inspect
from pathlib import Path
import sys
sys.dont_write_bytecode = True
ORIGINAL = Path('/workspace/scratch/textstats-live-harness-20261004/harness/scripts/core.py')
EXPECTED_SHA256 = '72ddbe9d32d4655659582e23e4be9645ab7c3abf19209120fc9ab95608eddb80'
if hashlib.sha256(ORIGINAL.read_bytes()).hexdigest() != EXPECTED_SHA256:
    raise SystemExit('Original helper identity changed; stop variant execution.')
spec = importlib.util.spec_from_file_location('original_textstats_core', ORIGINAL)
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
before = inspect.getsource(core.ownership)
old = "    selected = sorted(p for p in root.rglob('*.md') if p.name in {'TASKS.md', 'FEATURE-TASKS.md'} and not task_history(p.relative_to(root)))"
new = """    result = subprocess.run(['git', '--no-optional-locks', '-C', str(root), 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], capture_output=True)
    if result.returncode != 0: raise Stop('unavailable_git_owner_inventory')
    names = {os.fsdecode(name) for name in result.stdout.split(b'\\0') if name}
    selected = sorted(root / name for name in names if Path(name).name in {'TASKS.md', 'FEATURE-TASKS.md'} and not task_history(Path(name)))"""
if before.count(old) != 1:
    raise SystemExit('Unexpected ownership implementation; stop variant execution.')
after = before.replace(old, new)
exec(compile(after, str(Path(__file__).resolve()), 'exec'), core.__dict__)
if __name__ == '__main__':
    raise SystemExit(core.main('assess'))
