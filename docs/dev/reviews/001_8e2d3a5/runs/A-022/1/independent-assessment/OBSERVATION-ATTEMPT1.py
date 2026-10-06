import subprocess,json,hashlib,re,sys
from pathlib import Path
from datetime import datetime,timezone
E=Path(__file__).parent
P=Path('/workspace/scratch/textstats-acceptance-change-worktree-20261005')
H=Path('/workspace/scratch/textstats-live-harness-20261004/harness')
D='/workspace/scratch/textstats-acceptance-change-remote-20261005.git'
base='0e4741465c3e086d2ab95c5af73ca89371c16fac'
commands=[]
def run(argv,cwd=P):
 r=subprocess.run(argv,cwd=cwd,capture_output=True,text=True)
 commands.append({'argv':argv,'cwd':str(cwd),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 return r

def git(*args): return run(['git','--no-optional-locks',*args]).stdout.strip()
head=git('rev-parse','HEAD'); branch=git('branch','--show-current'); parents=git('show','-s','--format=%P','HEAD').split()
status=git('status','--porcelain=v1','--untracked-files=all')
remote=git('ls-remote',D,'refs/heads/'+branch)
paths=git('diff','--name-only',base,'HEAD').splitlines()
diff=git('diff',base,'HEAD','--','docs/dev')
rc=run(['git','--no-optional-locks','diff','--exit-code',base,'HEAD','--','textstats-run-resources','textstats','tests','README.md','docs/module.md','docs/api.md','Makefile']).returncode
whitespace=run(['git','--no-optional-locks','diff','--check',base,'HEAD']).returncode
livephase=git('rev-parse','refs/heads/phase/2-output-and-source-extensions')
old=git('show',base+':docs/dev/TASKS.md'); current=(P/'docs/dev/TASKS.md').read_text()
checkbox=lambda s:[l for l in s.splitlines() if re.search(r'\[[ x]\]',l)]
ids=re.findall(r'^\s*- \[[ x]\] T-(\d+)',current,re.M)
notes=[l.strip() for l in current.splitlines() if 'Completion reassessment pending (2026-10-05)' in l]
qc={}
for name in ['SPEC','PLAN','TASKS']:
 report=(P/f'docs/dev/{name}-REVIEW-REPORT.md').read_text(); latest=report[report.rfind('\n## Revision '):]
 pairs=re.findall(r'`(docs/dev/[^`]+)`:\s*SHA-256 `([0-9a-f]{64})`',latest)
 qc[name]={'identities':[{ 'path':n,'recorded':digest,'actual':hashlib.sha256((P/n).read_bytes()).hexdigest(),'matches':digest==hashlib.sha256((P/n).read_bytes()).hexdigest()} for n,digest in pairs], 'latest_revision':latest}
manifest=json.loads((P/'textstats-run-resources/PLUGIN-SOURCE.json').read_text())
print('manifest keys',list(manifest))
hashes=manifest.get('file_sha256',manifest.get('files',manifest.get('file_hashes',{})))
# Manifest uses hashes key in this frozen package.
if not hashes: hashes=manifest.get('sha256',{})
if not isinstance(hashes,dict) or not hashes: raise RuntimeError('manifest hash map not located')
pinchecks={n:hashlib.sha256((P/'textstats-run-resources/plugin'/n).read_bytes()).hexdigest()==sha for n,sha in hashes.items()}
refs={'product_branch':branch,'product_commit':head,'integration_branch':branch,'integration_commit':head,'merge_parents':parents,'remote':D,'remote_ref':'refs/heads/'+branch,'remote_commit':remote.split()[0]}
inputs={'schema_version':1,'test_repository':D,'local_checkout':str(P),'plugin_revision':'019eb354cf0921ebd6056e6579763ac33d0baec2','source_mode':'committed','scope':{'cases':['A-022']},'stop_after':None,'profile':'local-only'}
state={'schema_version':1,'run_id':'textstats-live-20261004','phase':'P1','case_id':'A-022','attempt':1,'role':'assessor','last_completed_action':'Independent changed-acceptance assessment','pending_operation':None,'next_action':'Coordinator publish sanitized assessment','checkpoint_refs':refs,'evidence_paths':['OBSERVATIONS.json']}
for name,value in [('INPUTS.json',inputs),('RUN-STATE.json',state)]: (E/name).write_text(json.dumps(value,indent=2)+'\n')
original=run(['python',str(H/'scripts/assess.py'),'--inputs',str(E/'INPUTS.json'),'--run-state',str(E/'RUN-STATE.json'),'--contract',str(H/'cases/assessor/A-022.json'),'--output',str(E/'ORIGINAL-DETERMINISTIC-ASSESSMENT.json')],H)
(E/'ORIGINAL-HELPER-RESULT.json').write_text(json.dumps(commands[-1],indent=2)+'\n')
if original.returncode==2 and 'repository_identity_mismatch' in original.stdout:
 adapter='/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-015/2/independent-assessment/local_url_assessment.py'
 adapted=run(['python',adapter,'--harness',str(H),'--inputs',str(E/'INPUTS.json'),'--run-state',str(E/'RUN-STATE.json'),'--contract',str(H/'cases/assessor/A-022.json'),'--output',str(E/'LOCAL-URL-DETERMINISTIC-ASSESSMENT.json')],H)
else: adapted=original
observations={'observed_at':datetime.now(timezone.utc).isoformat(),'checkpoint_refs':refs,'status_porcelain':status,'changed_paths':paths,'unchanged_protected_paths_exit':rc,'diff_check_exit':whitespace,'live_phase2_ref':livephase,'checkboxes_unchanged':checkbox(old)==checkbox(current),'task_ids':ids,'pending_notes':notes,'qc':qc,'pin_revision':manifest.get('revision'),'pin_hash_count':len(pinchecks),'pin_checks':pinchecks,'diff':diff,'consumer_journal':{'bytes':(E.parent/'JOURNAL.md').stat().st_size,'sha256':hashlib.sha256((E.parent/'JOURNAL.md').read_bytes()).hexdigest(),'native_command_sections':(E.parent/'JOURNAL.md').read_text().count('### Command'),'limit':'Journal is consumer-authored and includes replayed observations, not a full native session transcript.'},'deterministic_original_exit':original.returncode,'deterministic_adapter_exit':adapted.returncode}
(E/'OBSERVATIONS.json').write_text(json.dumps(observations,indent=2,ensure_ascii=False)+'\n')
(E/'INDEPENDENT-COMMANDS.json').write_text(json.dumps(commands,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:v for k,v in observations.items() if k not in ['diff','qc','pin_checks','pending_notes']},indent=2))
