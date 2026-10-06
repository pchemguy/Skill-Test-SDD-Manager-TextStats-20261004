import os, sys, json, hashlib, subprocess, re, shutil, io, contextlib
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parent
HERE=BASE/'checks-attempt2'
HERE.mkdir()
OLD=BASE.parent.parent/'independent-assessment'
ROOT=Path('/workspace/scratch/textstats-live-20261004')
HAR=Path('/workspace/scratch/textstats-live-harness-20261004/harness')
commands=[]
def run(argv,cwd=ROOT,env=None):
    p=subprocess.run(argv,cwd=cwd,env=env,capture_output=True,text=True,timeout=90)
    d=dict(argv=argv,cwd=str(cwd),returncode=p.returncode,stdout=p.stdout,stderr=p.stderr)
    commands.append(d); return d
def write(name,value): (HERE/name).write_text(json.dumps(value,indent=2)+'\n')
sha=lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
start=json.loads((OLD/'START.json').read_text())
tracked=run(['git','ls-files','-z'])['stdout'].split('\0')
inventory=run(['git','ls-files','-z','--cached','--others','--exclude-standard'])['stdout'].split('\0')
history=lambda p:any('archive' in part.lower() or part.lower() in {'.git','features','reviews','textstats-run-resources'} for part in p.parts[:-1])
candidates=[]
for p in sorted(ROOT.rglob('*.md')):
    rel=p.relative_to(ROOT)
    if p.name not in {'TASKS.md','FEATURE-TASKS.md'} or history(rel):continue
    ignored=run(['git','check-ignore','-v',str(rel)])
    candidates.append(dict(path=str(rel),tracked=str(rel) in tracked,in_git_inventory=str(rel) in inventory,ignore=ignored,sha256=sha(p)))
write('OWNERSHIP-CANDIDATE-AUDIT.json',dict(candidates=candidates,conclusion='Frozen rglob includes ignored generated dist/extracted/docs/dev/TASKS.md; Git inventory contains only main executable TASKS.md. Feature TASKS is historical and independently inspected.'))
assert len([c for c in candidates if c['in_git_inventory']])==1
assert any(not c['in_git_inventory'] and c['ignore']['returncode']==0 and c['path'].startswith('dist/') for c in candidates)
variant=OLD.parents[2]/'A-006/2/checker-variant/assess_git_owners.py'
assert sha(variant)=='10c4cce8ed9e275d0d36b207578ca8399104c818858d8364d490bb47020875c8'
write('VARIANT-AUDIT.json',dict(path=str(variant),sha256=sha(variant),original_core_sha256=sha(HAR/'scripts/core.py'),difference='Only candidate selection changes from filesystem rglob to git ls-files cached/others/exclude-standard; task parser, archive rules, deterministic contract and Git observation remain original. Original hash and exact source replacement guarded.'))
preserved={k:sha(ROOT/k) for k in start['pinned_source_sha256']}
assert preserved==start['pinned_source_sha256']
final=json.loads((OLD/'FINAL.json').read_text())
all_hashes={k:sha(ROOT/k) for k in final['tracked_sha256']}
assert all_hashes==final['tracked_sha256']
refs={name:run(['git','rev-parse',name])['stdout'].strip() for name in ['HEAD','main','HEAD^1','HEAD^2']}
assert refs=={'HEAD':'0e4741465c3e086d2ab95c5af73ca89371c16fac','main':'59debb649545125dd3aa00377ea115451b594271','HEAD^1':'ea97182d2d6a3984599238312a13e78d54d3221a','HEAD^2':'d518cc23650018542e43d8fb5a63f44a4d283518'}
assert all(sha(ROOT/k)==v for k,v in start['unrelated'].items())
write('SOURCE-REOBSERVATION.json',dict(refs=refs,status=run(['git','status','--porcelain=v1']),pinned_source_sha256=preserved,pinned_count=len(preserved),tracked_hashes_equal_prior_final=True,unrelated=start['unrelated']))
sys.path.insert(0,str(ROOT))
from textstats import cli, count_file, TextStats
import textstats.io as fileio
probes=[]
bad=[[],['x','y'],['--unknown','x'],['--lines','0:1','x'],['--lines','2:1','x'],['--lines','1:1','--lines','1:1','x'],['--lines','1:','x'],['--lines','١:2','x']]
for argv in bad:
    out,err=io.StringIO(),io.StringIO()
    with patch('builtins.open',side_effect=AssertionError('acquisition before validation')) as op, contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
        try: cli.main(argv)
        except SystemExit as e: status=e.code
    assert status==2 and op.call_count==0 and out.getvalue()=='' and err.getvalue()
    probes.append(dict(kind='usage-before-read',argv=argv,status=status,open_calls=op.call_count,stdout=out.getvalue(),stderr=err.getvalue()))
class Handle:
    def __init__(self,kind):self.kind=kind;self.closed=False;self.events=[]
    def __enter__(self):self.events.append('enter');return self
    def read(self):
        self.events.append('read')
        if self.kind=='read-error':raise OSError('independent read failure')
        return b'alpha\n\xff' if self.kind=='decode-error' else b'alpha beta\n'
    def __exit__(self,*args):self.closed=True;self.events.append('close');return False
for kind in ['success','read-error','decode-error']:
    handle=Handle(kind);out,err=io.StringIO(),io.StringIO();exception=None;result=None
    with patch('builtins.open',return_value=handle) as op,contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
        try:result=count_file('independent-owned.txt')
        except (OSError,UnicodeDecodeError) as e:exception=type(e).__name__
    assert handle.closed and handle.events==['enter','read','close'] and out.getvalue()==err.getvalue()==''
    assert (result==TextStats(1,2)) if kind=='success' else exception=={'read-error':'OSError','decode-error':'UnicodeDecodeError'}[kind]
    probes.append(dict(kind=kind,events=handle.events,closed=handle.closed,exception=exception,stdout=out.getvalue(),stderr=err.getvalue(),open_args=str(op.call_args)))
for kind in ['read-error','decode-error']:
    handle=Handle(kind);out,err=io.StringIO(),io.StringIO()
    with patch('builtins.open',return_value=handle),contextlib.redirect_stdout(out),contextlib.redirect_stderr(err): status=cli.main(['--json','--lines','1:1','independent-owned.txt'])
    assert status==1 and out.getvalue()=='' and 'independent-owned.txt' in err.getvalue() and 'Traceback' not in err.getvalue() and handle.closed
    probes.append(dict(kind='cli-'+kind,status=status,closed=handle.closed,stdout=out.getvalue(),stderr=err.getvalue()))
write('INDEPENDENT-ACQUISITION-PROBES.json',dict(status='Passed',probes=probes))
expected=json.loads((HAR/'cases/assessor/expected.json').read_text())
write('EXPECTED-SCHEMA.json',dict(keys=list(expected)))
distribution=json.loads((OLD/'EXTRACTED-distribution.json').read_text())['literals']['distribution']
exp=expected['literals']['distribution']
assert distribution==exp
contract=json.loads((HAR/'cases/assessor/A-010.json').read_text())
for key in ['ranges','ranges-json']:
    exp=next(c['expected'] for c in contract['checks'] if c.get('key')==key)
    assert json.loads((OLD/('EXTRACTED-'+key+'.json')).read_text())['literals'][key]==exp
distprov=json.loads((OLD/'DISTRIBUTION-PROVENANCE.json').read_text())
assert sha(Path(distprov['archive']))==distprov['sha256']
write('DISTRIBUTION-CONTRACT-ASSESSMENT.json',dict(status='Passed',expected_file=str(HAR/'cases/assessor/expected.json'),expected_sha256=sha(HAR/'cases/assessor/expected.json'),actual_evidence=str(OLD/'EXTRACTED-distribution.json'),actual=distribution,expected=exp,distribution_expected=expected['literals']['distribution'],archive_sha256=distprov['sha256'],ranges_and_ranges_json_equal_contract=True))
work=HERE/'documentation-workspace';work.mkdir()
for name in tracked:
    if name and not name.startswith('textstats-run-resources/'):
        dest=work/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,dest)
env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'};env.pop('PYTHONPATH',None)
docs=[]
for name in ['README.md','docs/api.md','docs/module.md']:
    cwd=work
    for index,(lang,code) in enumerate(re.findall(r'```(python|sh)\n(.*?)```', (ROOT/name).read_text(),re.S)):
        rows=[]
        if lang=='python':
            row=run([sys.executable,'-c',code],cwd,env);assert row['returncode']==0;rows.append(row)
        else:
            lines=code.splitlines()
            for n,line in enumerate(lines):
                if not line.strip() or line.startswith('#'):continue
                if line.startswith('cd '):cwd=cwd/line[3:];rows.append(dict(command=line,resolved_cwd=str(cwd)));continue
                row=run(['bash','-c',line],cwd,env);rows.append(row)
                comment=lines[n+1] if n+1<len(lines) and lines[n+1].startswith('#') else ''
                if '# status ' in comment:
                    status=int(re.search(r'status (\d)',comment).group(1));assert row['returncode']==status and row['stdout']=='' and row['stderr'] and 'Traceback' not in row['stderr']
                else:
                    assert row['returncode']==0
                    if comment:
                        literal=comment[2:]+'\n'
                        if literal.startswith('{'):assert json.loads(row['stdout'])==json.loads(literal)
                        else:assert row['stdout']==literal
                    if line.startswith('python -m textstats'):assert row['stderr']==''
        docs.append(dict(document=name,block=index,language=lang,code=code,commands=rows,status='Passed'))
write('PUBLIC-DOCUMENTATION-EXAMPLES.json',dict(status='Passed',documents=['README.md','docs/api.md','docs/module.md'],blocks=docs,workspace=str(work),note='Exact current public fenced examples executed in tracked-file copy to preserve unrelated samples and generated distribution in product. Bash blocks run linewise, preserving cd; literal comments independently compared; test suites nonempty passed.'))
write('COMMANDS.json',commands)
print(json.dumps(dict(status='Passed',probe_count=len(probes),doc_blocks=len(docs),refs=refs)))
