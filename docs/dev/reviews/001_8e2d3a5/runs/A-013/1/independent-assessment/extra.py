import os,sys,json,subprocess,hashlib,re,io,contextlib,tarfile
from pathlib import Path
from unittest.mock import patch
sys.dont_write_bytecode=True
O=Path(__file__).parent;P=Path('/workspace/scratch/textstats-live-20261004');R=O.parent;E=O/'extracted'
def save(n,v):(O/n).write_text(json.dumps(v,indent=2)+'\n')
def g(*a):return subprocess.run(['git','--no-optional-locks',*a],cwd=P,capture_output=True,check=True).stdout
sys.path.insert(0,str(P))
from textstats.cli import main
from textstats import count_file
class Borrowed:
 def __init__(self,data=None,error=None): self.buffer=self;self.data=data;self.error=error;self.reads=0;self.closed=False
 def read(self):
  self.reads+=1
  if self.error:raise self.error
  return self.data
 def close(self):self.closed=True
rows=[]
for name,args,data,error,rc,out,reads in [('mixed',['--lines','2:3','-'],b'a\r\nb c\rd\n',None,0,'lines=2 words=3\n',1),('keep',['--lines=1:1','--keep-bom','-'],b'\xef\xbb\xbf',None,0,'lines=1 words=1\n',1),('read-error',['-'],None,OSError('independent read failure'),1,'',1),('decode-after',['--lines=1:1','-'],b'ok\n\xff',None,1,'',1),('invalid-before',['--lines=0:2','-'],None,OSError('must not read'),2,'',0),('json-before',['--json','-'],None,OSError('must not read'),2,'',0)]:
 b=Borrowed(data,error);stdout=io.StringIO();stderr=io.StringIO()
 with patch('sys.stdin',b),contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
  try:actual=main(args)
  except SystemExit as ex:actual=ex.code
 assert(actual,stdout.getvalue(),b.reads,b.closed)==(rc,out,reads,False),(name,actual,stdout.getvalue())
 if rc==1:assert 'stdin' in stderr.getvalue() and 'Traceback' not in stderr.getvalue()
 rows.append({'name':name,'status':actual,'stdout':stdout.getvalue(),'stderr':stderr.getvalue(),'reads':b.reads,'closed':b.closed,'passed':True})
for locale in ['C','C.UTF-8']:
 env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','PYTHONSTARTUP')};env.update(LC_ALL=locale,PYTHONUTF8='0',PYTHONCOERCECLOCALE='0',PYTHONDONTWRITEBYTECODE='1')
 r=subprocess.run([sys.executable,'-m','textstats','--lines=1:1','-'],cwd=P,env=env,input='café β\nlate'.encode(),capture_output=True)
 assert(r.returncode,r.stdout,r.stderr)==(0,b'lines=1 words=2\n',b'')
 rows.append({'locale':locale,'status':r.returncode,'stdout':r.stdout.decode(),'stderr':r.stderr.decode(),'passed':True})
save('INDEPENDENT-STDIN.json',rows)
# Invoke protected adapter read-only; retain no provider prose.
hosted=[]
for resource in ['milestones?state=all&per_page=100','issues?state=all&per_page=100']:
 r=subprocess.run([sys.executable,'.git/textstats-hosting-curl.py','GET',resource],cwd=P,capture_output=True,text=True)
 assert r.returncode==0,(resource,r.returncode)
 d=json.loads(r.stdout); entries=d.get('json',d.get('body',d.get('result',d))) if isinstance(d,dict) else d
 # Some adapter responses wrap the provider payload under data.
 if isinstance(entries,dict):
  for k in ['data','response']:
   if k in entries:entries=entries[k];break
 if isinstance(entries,str):entries=json.loads(entries)
 if not isinstance(entries,list):
  save('ADAPTER-SHAPE.json',{'keys':list(d) if isinstance(d,dict) else None});raise RuntimeError('unexpected adapter response shape')
 if resource.startswith('milestones'):
  items=[{k:x.get(k) for k in ['number','id','state','open_issues','closed_issues','closed_at']} for x in entries]
 else:
  items=[{'number':x['number'],'id':x['id'],'state':x['state'],'state_reason':x.get('state_reason'),'milestone':x.get('milestone',{}).get('number') if x.get('milestone') else None,'pr':bool(x.get('pull_request')),'markers':re.findall(r'<!-- /?sdd-forge:task-id=T-\d+ -->',x.get('body','')),'closed_at':x.get('closed_at')} for x in entries]
 hosted.append({'resource':resource,'exit_code':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'items':items})
save('LIVE-HOSTED.json',hosted)
qc=[];prep='40a1923'
for f in ['SPEC-REVIEW-REPORT.md','PLAN-REVIEW-REPORT.md','TASKS-REVIEW-REPORT.md']:
 t=(P/'docs/dev'/f).read_text();tail=t[t.rfind('## Revision '):];ids=[]
 for n,h in re.findall(r'^- ([A-Za-z-]+\.md): SHA256 `([0-9a-f]{64})`',tail,re.M):
  atprep=g('show',prep+':docs/dev/'+n);current=(P/'docs/dev'/n).read_bytes()
  ids.append({'path':n,'declared':h,'at_preparation':hashlib.sha256(atprep).hexdigest(),'matches_preparation':hashlib.sha256(atprep).hexdigest()==h,'current':hashlib.sha256(current).hexdigest(),'diff':g('diff',prep,'HEAD','--','docs/dev/'+n).decode() if current!=atprep else ''})
 qc.append({'report':f,'latest_revision':tail,'identities':ids,'finding_resolved':'Corrected and resolved' in tail})
save('QC-IDENTITIES.json',qc)
# Retain all original evidence by exact hashes, distinguish continuation and receipts.
ret=[]
for f in sorted(R.glob('*')):
 if f.is_file():
  b=f.read_bytes();ret.append({'path':f.name,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
save('CONSUMER-EVIDENCE-RETENTION.json',ret)
# Run public docs exactly against independently built extracted archive.
docs=[]
for f in ['README.md','docs/module.md','docs/api.md']:
 for n,(lang,block) in enumerate(re.findall(r'```(python|sh)\n(.*?)```',(P/f).read_text(),re.S),1):
  if 'unittest discover' in block:continue
  statuses=re.findall(r'# status (\d+)',block);status=int(statuses[-1]) if statuses else 0
  r=subprocess.run([sys.executable,'-c',block] if lang=='python' else ['bash','-c',block],cwd=E,env={**os.environ,'PYTHONPATH':str(E),'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
  expected=re.findall(r'# (lines=\d+ words=\d+)',block);actual=re.findall(r'^lines=\d+ words=\d+$',r.stdout,re.M)
  assert r.returncode==status and actual==expected,(f,n,r.returncode,r.stdout)
  docs.append({'source':f,'fence':n,'command':block,'expected_status':status,'expected_counts':expected,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'passed':True})
save('DOC-EXAMPLES.json',docs)
links=[]
for f in [P/'README.md',*sorted((P/'docs').rglob('*.md'))]:
 for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)',f.read_text()):
  if '://' not in target:links.append({'source':str(f.relative_to(P)),'target':target,'exists':(f.parent/target).exists()})
assert all(x['exists'] for x in links)
save('LOCAL-LINKS.json',links)
print(json.dumps({'stdin_checks':len(rows),'doc_fences':len(docs),'links':len(links),'qc_hashes_match':all(x['matches_preparation'] for q in qc for x in q['identities']),'hosted_resources':len(hosted)}))
