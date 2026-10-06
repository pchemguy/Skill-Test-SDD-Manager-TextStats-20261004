import pathlib,subprocess,hashlib,stat,json,datetime,os
r=pathlib.Path('/workspace/scratch/textstats-preservation-worktree-20261004');o=pathlib.Path(__file__).parent
base=pathlib.Path('/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5')
def g(*a):return subprocess.check_output(['git','--no-optional-locks','-C',str(r),*a]).decode()
d={'time':datetime.datetime.now(datetime.timezone.utc).isoformat(),'head':g('rev-parse','HEAD').strip(),'parents':g('rev-list','--parents','-n','1','HEAD').strip().split()[1:],'branch':g('branch','--show-current').strip(),'main':g('rev-parse','refs/heads/main').strip(),'status':g('status','--porcelain'),'paths':g('diff-tree','--no-commit-id','--name-only','-r','HEAD').splitlines(),'sentinels':{}}
for p in ('notes/local-retained.txt','notes/untracked-retained.txt'):
 b=(r/p).read_bytes();d['sentinels'][p]={'sha256':hashlib.sha256(b).hexdigest(),'mode':stat.S_IMODE((r/p).stat().st_mode),'index':g('ls-files','--stage','--',p)}
b=subprocess.check_output(['git','-C',str(r),'show',':notes/local-retained.txt']);d['sentinels']['notes/local-retained.txt']['staged_sha256']=hashlib.sha256(b).hexdigest()
mid=json.loads((o/'mid-execution-observation.json').read_text());d['preserved_exactly']=mid['sentinels']==d['sentinels'];d['main_preserved']=mid['main']==d['main'];d['owned_index_delta']=g('diff','--cached','--name-only');d['owned_worktree_delta']=g('diff','--name-only');d['checked_tasks']=[x.strip() for x in (r/'docs/dev/TASKS.md').read_text().splitlines() if '- [x]' in x]
manifest=json.loads((r/'textstats-run-resources/PLUGIN-SOURCE.json').read_text());d['plugin_pin']={'commit':manifest['commit'],'files':len(manifest['package_hashes']),'mismatches':[]}
for p,h in manifest['package_hashes'].items():
 b=(r/'textstats-run-resources/plugin'/p).read_bytes(); original=subprocess.check_output(['git','-C','/workspace/scratch/6420baa7afea','show',manifest['commit']+':'+p])
 if hashlib.sha256(b).hexdigest()!=h or b!=original:d['plugin_pin']['mismatches'].append(p)
(o/'frozen-observation.json').write_text(json.dumps(d,indent=2)+'\n')
(o/'task-commit.diff').write_text(g('show','--format=fuller','--stat','--patch','HEAD'))
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
p=subprocess.run(['python','-m','unittest','discover','-s','tests/unit','-t','.','-v'],cwd=r,env=env,capture_output=True);(o/'independent-unit.txt').write_bytes(p.stdout+p.stderr);print('unit exit',p.returncode)
# Independent literal boundary vectors; no product-driven expectations.
code='''from textstats import TextStats,count_text
from contextlib import redirect_stdout,redirect_stderr
from io import StringIO
from dataclasses import FrozenInstanceError
cases=[('',True,(0,0)),('a\\r\\n\\r\\nb',True,(3,2)),('\\r\\n\\n\\r',True,(3,0)),('x\\u2028y\\u2029z',True,(1,3)),('\\ufeff\\ufeff\\r\\n',True,(1,1)),('\\ufeff',False,(1,1)),('a\\x00b',True,(1,1)),('a\\u00a0b\\t c',True,(1,3))]
o,e=StringIO(),StringIO()
with redirect_stdout(o),redirect_stderr(e):
 for text,strip,want in cases:
  got=count_text(text,strip_bom=strip); assert (got.lines,got.words)==want,(text,got,want)
 for args in [(-1,0),(0,-1)]:
  try:TextStats(*args)
  except ValueError:pass
  else:raise AssertionError(args)
 try:TextStats(1,2).words=3
 except FrozenInstanceError:pass
 else:raise AssertionError('mutable')
assert o.getvalue()==e.getvalue()==''
print('PASS: 8 independent literal vectors, negatives, frozen value, silence')
'''
p2=subprocess.run(['python','-c',code],cwd=r,env=env,capture_output=True);(o/'independent-literals.txt').write_bytes(p2.stdout+p2.stderr);print('literal exit',p2.returncode)
i=json.loads((base/'INPUTS.json').read_text());i.update(local_checkout=str(r),profile='local-only',scope={'cases':['A-020']});(o/'helper-inputs.json').write_text(json.dumps(i,indent=2)+'\n')
s=json.loads((base/'RUN-STATE.json').read_text());s.update(case_id='A-020',attempt=1,role='assessor');s['checkpoint_refs'].update(product_branch=d['branch'],product_commit=d['head']);(o/'helper-state.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps(d,indent=2))
