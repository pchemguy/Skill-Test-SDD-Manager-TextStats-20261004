import os,sys,json,subprocess,hashlib,tarfile,re,datetime
from pathlib import Path
sys.dont_write_bytecode=True
OUT=Path(__file__).parent
RUN=OUT.parent
PRODUCT=Path('/workspace/scratch/textstats-live-20261004')
HARNESS=Path('/workspace/scratch/textstats-live-harness-20261004/harness')
RECORDS=[]
def save(n,v): (OUT/n).write_text(json.dumps(v,indent=2)+'\n')
def call(args,cwd=PRODUCT):
 p=subprocess.run(list(map(str,args)),cwd=cwd,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'},capture_output=True,text=True)
 RECORDS.append({'args':list(map(str,args)),'cwd':str(cwd),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'completion':'complete'})
 save('COMMAND-RESULTS.json',RECORDS)
 return p
def git(*args): return call(['git','--no-optional-locks',*args]).stdout.strip()
head=git('rev-parse','HEAD'); branch=git('branch','--show-current'); parents=git('show','-s','--format=%P','HEAD').split()
remote=git('ls-remote','origin','refs/heads/phase/2-output-and-source-extensions','refs/heads/revision/003_0e47414-remove-json','refs/heads/main')
refs={'product_branch':branch,'product_commit':head,'integration_branch':branch,'integration_commit':head,'merge_parents':parents,'remote':'origin','remote_ref':'refs/heads/'+branch,'remote_commit':dict((b,a) for a,b in (x.split() for x in remote.splitlines()))['refs/heads/'+branch]}
save('LIVE-OBSERVATION.json',{'checkpoint_refs':refs,'remote_refs':remote,'status':git('status','--porcelain=v1'),'index':git('ls-files','--stage'),'untracked_sample_sha256':hashlib.sha256((PRODUCT/'-json-9l969okj/sample.txt').read_bytes()).hexdigest(),'journal_size':(RUN/'JOURNAL.md').stat().st_size,'journal_sha256':hashlib.sha256((RUN/'JOURNAL.md').read_bytes()).hexdigest(),'difference':git('diff','--name-status',parents[0],head),'merge_vs_second_parent':git('diff','--name-status',parents[1],head),'log':git('log','--format=%H %P %s',parents[0]+'..'+head)})
save('INPUTS.json',{'schema_version':1,'test_repository':str(PRODUCT),'local_checkout':str(PRODUCT),'profile':'full-github','scope':{'cases':['A-012']}})
save('RUN-STATE.json',{'schema_version':1,'run_id':'textstats-live-20261004','phase':'P3','case_id':'A-012','attempt':1,'role':'assessor','last_completed_action':'Independent reached-ref observation','pending_operation':None,'next_action':'Coordinator evidence publication','checkpoint_refs':refs,'evidence_paths':[]})
for suite in ['api','baseline','ranges','removal']:
 call([sys.executable,HARNESS/'cases/assessor/capture.py','--product-root',PRODUCT,'--suite',suite,'--output',OUT/(suite+'.json'),'--provenance',OUT/(suite+'-commands.json')])
literal={}
for suite in ['api','baseline','ranges','removal']: literal.update(json.loads((OUT/(suite+'.json')).read_text())['literals'])
save('LITERALS.json',{'schema_version':1,'literals':literal})
base=['--inputs',OUT/'INPUTS.json','--run-state',OUT/'RUN-STATE.json','--contract',HARNESS/'cases/assessor/A-012.json','--evidence',OUT/'LITERALS.json']
call([sys.executable,HARNESS/'scripts/assess.py',*base,'--output',OUT/'original-deterministic.json'])
variant=RUN.parents[1]/'A-006/2/checker-variant/assess_git_owners.py'
call([sys.executable,variant,*base,'--output',OUT/'variant-deterministic.json'])
call(['make','check'])
call(['git','diff','--check',parents[0],head])
call(['make','dist','DIST_DIR='+str(OUT/'distribution')])
archive=OUT/'distribution/textstats.tar.gz'; extract=OUT/'extracted';extract.mkdir()
with tarfile.open(archive) as t: t.extractall(extract,filter='data')
save('DISTRIBUTION-MANIFEST.json',{'archive':'distribution/textstats.tar.gz','sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'product_commit':head,'files':[{'path':str(p.relative_to(extract)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(extract.rglob('*')) if p.is_file()]})
call([sys.executable,HARNESS/'cases/assessor/capture.py','--product-root',extract,'--suite','distribution','--output',OUT/'distribution.json','--provenance',OUT/'distribution-commands.json'])
qc=[]
for report in ['SPEC-REVIEW-REPORT.md','PLAN-REVIEW-REPORT.md','TASKS-REVIEW-REPORT.md']:
 text=(PRODUCT/'docs/dev'/report).read_text(); tail=text[text.rfind('## Revision '):]
 matches=[]
 for line in tail.splitlines():
  values=re.findall(r'[0-9a-f]{64}',line)
  if values:
   pathmatch=re.search(r'`([^`]+)`',line)
   if pathmatch:
    path=PRODUCT/pathmatch.group(1)
    if path.exists():matches.append({'path':pathmatch.group(1),'expected':values[0],'actual':hashlib.sha256(path.read_bytes()).hexdigest()})
 qc.append({'report':report,'latest_revision':tail,'identity_matches':matches})
save('QC-IDENTITIES.json',qc)
print(json.dumps({'head':head,'parents':parents,'commands':len(RECORDS),'failed_commands':[{'args':x['args'],'returncode':x['returncode']} for x in RECORDS if x['returncode']]}))
