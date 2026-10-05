import subprocess,json,pathlib,hashlib,datetime,re,sys
root=pathlib.Path('/workspace/scratch/textstats-live-20261004'); out=pathlib.Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def cmd(a,cwd=root):
 p=subprocess.run(a,cwd=cwd,capture_output=True);return {'argv':a,'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()}
commands=[cmd(['git',*x]) for x in [['status','--porcelain=v2','--branch'],['log','-1','--format=%H %P %s'],['for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/remotes/origin'],['ls-files','--stage'],['diff','--binary'],['diff','--cached','--binary'],['ls-remote','origin','refs/heads/main','refs/heads/phase/2-output-and-source-extensions','refs/heads/feature/002_ea97182-line-ranges','refs/heads/revision/001_8e2d3a5-live-acceptance']]]
files=cmd(['git','ls-files','-z'])['stdout'].split('\0'); hashes={f:sha((root/f).read_bytes()) for f in files if f and (root/f).is_file()}
unknown={str(p.relative_to(root)):sha(p.read_bytes()) for p in (root/'-json-9l969okj').rglob('*') if p.is_file()}
owners={f:(root/f).read_text() for f in files if f and pathlib.Path(f).name in ['TASKS.md','FEATURE-TASKS.md']}
snap={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_id':'A-010','role':'independent-assessor','git':commands,'tracked_hashes':hashes,'unknown_fixture_hashes':unknown,'task_lists':owners,'consumer_frozen':True}
(out/'FINAL-OBSERVATION.json').write_text(json.dumps(snap,indent=2)+'\n')
previous=json.loads(pathlib.Path('/workspace/scratch/textstats-live-harness-20261004/assessments/A-009-1/PINNED-SOURCE.json').read_text())
checks=[{'path':v['path'],'expected':v['expected'],'actual':sha((root/'textstats-run-resources/plugin'/v['path']).read_bytes())} for v in previous['checks']]
(out/'FINAL-PINNED-SOURCE.json').write_text(json.dumps({'commit':previous['commit'],'checks':checks,'all_match':all(v['actual']==v['expected'] for v in checks)},indent=2)+'\n')
reads=[]
for endpoint in ['issues?state=all&per_page=100','milestones?state=all&per_page=100','labels?per_page=100']:
 a=['python',str(root/'.git/textstats-hosting-curl.py'),'GET',endpoint]; p=subprocess.run(a,capture_output=True)
 try:d=json.loads(p.stdout)
 except:raise RuntimeError('Non-JSON provider response retained only as hash')
 # adapter envelope may be API payload itself or result envelope
 print('provider structure',endpoint,type(d).__name__,list(d)[:10] if isinstance(d,dict) else len(d))
 def safe(v):
  if not isinstance(v,dict):return None
  r={k:v[k] for k in ['id','number','title','state','state_reason','html_url','name','full_name','default_branch','private','closed_at','created_at','updated_at','open_issues','closed_issues','color'] if k in v}
  if isinstance(v.get('milestone'),dict):r['milestone_number']=v['milestone']['number']
  if isinstance(v.get('labels'),list):r['labels']=[x.get('name') for x in v['labels']]
  return r
 payload=d.get('result',d.get('data',d)) if isinstance(d,dict) else d
 reads.append({'args':a,'returncode':p.returncode,'stdout_bytes':len(p.stdout),'stdout_sha256':sha(p.stdout),'stderr_bytes':len(p.stderr),'stderr_sha256':sha(p.stderr),'metadata':[safe(v) for v in payload] if isinstance(payload,list) else safe(payload),'safe_envelope':{k:d[k] for k in ['http_status','transport'] if isinstance(d,dict) and k in d}})
(out/'FINAL-PROVIDER-READBACK.json').write_text(json.dumps(reads,indent=2)+'\n')
print('snapshot complete',len(hashes),'tracked',len(checks),'pin checks',unknown)
