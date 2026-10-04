"""Case evidence persistence only; no product workflows or grading decisions."""
import argparse,json,pathlib,shutil,subprocess,re
ROOT=pathlib.Path('/workspace/scratch/textstats-live-harness-20261004')
EVID=pathlib.Path('/workspace/scratch/textstats-live-evidence-20261004')
REC=EVID/'docs/dev/reviews/001_8e2d3a5'
PRODUCT=pathlib.Path('/workspace/scratch/textstats-live-20261004')
BRANCH='revision/001_8e2d3a5-live-acceptance'
def git(*args,cwd=EVID):
 return subprocess.check_output(['git',*args],cwd=cwd,text=True).strip()
def save(p,v):
 p.parent.mkdir(parents=True,exist_ok=True)
 p.write_text(json.dumps(v,indent=2)+'\n')
def publish(paths,message):
 for p in paths:
  pp=EVID/p
  for f in ([pp] if pp.is_file() else pp.rglob('*')):
   if f.is_file() and f.suffix in ('.md','.json','.py','.txt'):
    if re.search(r'github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{20,}',f.read_text(errors='replace')):
     raise SystemExit('Protected content detected; publication blocked')
 git('add','--',*paths)
 subprocess.run(['git','diff','--cached','--check'],cwd=EVID,check=True)
 subprocess.run(['git','commit','-m',message],cwd=EVID,check=True)
 subprocess.run(['git','push','origin',BRANCH],cwd=EVID,check=True)
 sha=git('rev-parse','HEAD')
 observed=git('ls-remote','origin','refs/heads/'+BRANCH).split()[0]
 if observed!=sha: raise SystemExit('Evidence remote readback mismatch')
 return sha
p=argparse.ArgumentParser();sub=p.add_subparsers(dest='action',required=True)
a=sub.add_parser('publish');a.add_argument('case');a.add_argument('--assessment',required=True);a.add_argument('--attempt',type=int,default=1)
a=sub.add_parser('render');a.add_argument('case');a.add_argument('--current',required=True)
a=sub.add_parser('dispatch');a.add_argument('case');a.add_argument('--attempt',type=int,default=1)
args=p.parse_args();case=args.case
catalog=json.loads((ROOT/'harness/cases/catalog.json').read_text())['cases'];entry=next(x for x in catalog if x['id']==case)
if args.action=='render':
 out=ROOT/'consumer-handoffs'/case;out.mkdir(parents=True,exist_ok=True)
 current=json.loads(pathlib.Path(args.current).read_text());checks=[]
 required=entry['checkpoint_bindings']['start']['from_case']
 if required:
  old=REC/'runs'/required/'1'/'ASSESSMENT.json';assessment=json.loads(old.read_text())
  evidence_sha=git('log','-1','--format=%H','--',str(old.relative_to(EVID)))
  checks.append({'case_id':required,'status':assessment['status'],'assessment_path':str(old),'checkpoint_refs':assessment['checkpoint_refs'],'local_checkout':str(PRODUCT),'remote':'origin','remote_ref':'refs/heads/'+assessment['checkpoint_refs']['product_branch'],'evidence_publication':{'status':'published','commit':evidence_sha,'path':str(old.relative_to(EVID)),'remote':'origin','ref':'refs/heads/'+BRANCH}})
 binding=out/'RESOLVED.json';save(binding,{'checkpoints':checks,'current':current})
 subprocess.run(['python',str(ROOT/'harness/cases/assessor/catalog_tools.py'),'render','--case',case,'--bindings',str(binding),'--output',str(out/'REQUEST.md')],check=True)
elif args.action=='dispatch':
 dest=REC/'runs'/case/str(args.attempt);dest.mkdir(parents=True,exist_ok=True)
 for f in (ROOT/'consumer-handoffs'/case).iterdir():
  if f.name!='RESULT.md' and f.is_file():shutil.copy2(f,dest/f.name)
 state=json.loads((REC/'RUN-STATE.json').read_text());state.update(phase=entry['phase'],case_id=case,attempt=args.attempt,role='consumer',last_completed_action='Verified prerequisites and prepared exact consumer handoff',next_action='Observe consumer completion/trigger then independent assessment',pending_operation={'kind':'task','status':'in_progress','description':case+' ordinary consumer request'})
 save(REC/'RUN-STATE.json',state)
 cov=json.loads((REC/'COVERAGE.json').read_text());cov['cases'][case]={'status':'Running','attempts':[{'attempt':args.attempt,'status':'Running','consumer':'fresh explicit-source context'}]};save(REC/'COVERAGE.json',cov)
 print(publish([str(dest.relative_to(EVID)),str((REC/'RUN-STATE.json').relative_to(EVID)),str((REC/'COVERAGE.json').relative_to(EVID))],f'Record {case} consumer dispatch'))
elif args.action=='publish':
 source=pathlib.Path(args.assessment);assessment=json.loads((source/'ASSESSMENT.json').read_text())
 assert assessment['case_id']==case and assessment['agent_behavior_assessed'] is True
 dest=REC/'runs'/case/str(args.attempt);dest.mkdir(parents=True,exist_ok=True)
 for f in source.iterdir():
  target=dest/f.name
  if target.exists():
   if f.is_file() and target.is_file() and f.read_bytes()==target.read_bytes():continue
   raise SystemExit('Occupied nonidentical attempt artifact '+f.name)
  if f.is_dir():shutil.copytree(f,target)
  else:shutil.copy2(f,target)
 result=ROOT/'consumer-handoffs'/case/'RESULT.md'
 if result.exists():shutil.copy2(result,dest/'CONSUMER-RESULT.md')
 state=json.loads((REC/'RUN-STATE.json').read_text());state.update(phase=entry['phase'],case_id=case,attempt=args.attempt,role='coordinator',last_completed_action=f'Independent {case} assessment: '+assessment['status'],next_action='Select next eligible catalog case within full authorized scope',pending_operation=None)
 state['checkpoint_refs']=assessment['checkpoint_refs']|{'evidence_branch':BRANCH,'remote':'origin','remote_ref':'refs/heads/'+assessment['checkpoint_refs']['product_branch']}
 save(REC/'RUN-STATE.json',state)
 cov=json.loads((REC/'COVERAGE.json').read_text());cov['cases'][case]={'status':assessment['status'],'attempts':[{'attempt':args.attempt,'status':assessment['status'],'assessment':str((dest/'ASSESSMENT.json').relative_to(REC))}]};save(REC/'COVERAGE.json',cov)
 (REC/'RESUME.md').write_text(f'# Live acceptance checkpoint\n\n{case} independently assessed {assessment["status"]}. Full authorized campaign remains active. Reconcile product, evidence and hosted state before selecting the next eligible case. Exact refs and next action: RUN-STATE.json; all case dispositions: COVERAGE.json. No source/package changes are authorized in this campaign.\n')
 report=REC/'DIAGNOSTIC-REPORT.md'
 with report.open('a') as f:f.write(f'\n## {case} — {assessment["status"]}\n\nIndependent evidence: [assessment](runs/{case}/{args.attempt}/ASSESSMENT.md). Original consumer result retained separately. Source remains pinned and unchanged; final causal findings/proposals await campaign assessment.\n')
 paths=[str(dest.relative_to(EVID))]+[str((REC/n).relative_to(EVID)) for n in ('RUN-STATE.json','COVERAGE.json','RESUME.md','DIAGNOSTIC-REPORT.md')]
 print(publish(paths,f'Retain independent {case} live acceptance assessment'))
