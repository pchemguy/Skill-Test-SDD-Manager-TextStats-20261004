import subprocess,json,pathlib,hashlib,tarfile,os,datetime
O=pathlib.Path(__file__).parent
R=pathlib.Path('/workspace/scratch/textstats-live-20261004')
H=pathlib.Path('/workspace/scratch/textstats-live-harness-20261004/harness')
logs=[]
def run(args,cwd=R):
 p=subprocess.run(args,cwd=cwd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
 logs.append({'command':args,'cwd':str(cwd),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
 (O/'commands.json').write_text(json.dumps(logs,indent=2)+'\n')
 return p
for suite in ['baseline','json']:
 run(['python',str(H/'scripts/capture.py'),'--product-root',str(R),'--suite',suite,'--output',str(O/f'actual-{suite}.json'),'--provenance',str(O/f'provenance-{suite}.json')])
for directory in ['tests/unit','tests/integration']:
 run(['python','-m','unittest','discover','-s',directory,'-t','.','-v'])
run(['git','diff','--check'])
run(['make','dist','DIST_DIR='+str(O/'build')])
archive=O/'build/textstats.tar.gz';ext=O/'extracted';ext.mkdir()
with tarfile.open(archive) as t:t.extractall(ext,filter='data')
(O/'archive.json').write_text(json.dumps({'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'archive':str(archive),'extract_root':str(ext)},indent=2)+'\n')
for suite in ['baseline','json','distribution']:
 run(['python',str(H/'scripts/capture.py'),'--product-root',str(ext),'--suite',suite,'--output',str(O/f'actual-extracted-{suite}.json'),'--provenance',str(O/f'provenance-extracted-{suite}.json')])
run(['python','-m','textstats','-'],cwd=ext)
run(['python','-m','textstats','--json','-'],cwd=ext)
head=run(['git','rev-parse','HEAD']).stdout.strip();branch=run(['git','symbolic-ref','--short','HEAD']).stdout.strip()
run(['git','status','--porcelain=v1']);run(['git','ls-remote','origin','refs/heads/main','refs/heads/'+branch])
state={'schema_version':1,'run_id':'001_8e2d3a5','phase':'P3','case_id':'A-007','attempt':1,'role':'assessor','last_completed_action':'Independent JSON milestone observation','pending_operation':None,'next_action':'Coordinator publishes assessment before dependent work','checkpoint_refs':{'product_branch':branch,'product_commit':head,'integration_branch':'main','integration_commit':'59debb649545125dd3aa00377ea115451b594271','remote':'origin','remote_ref':'refs/heads/'+branch,'remote_commit':head},'evidence_paths':['commands.json']}
(O/'RUN-STATE.json').write_text(json.dumps(state,indent=2)+'\n')
inp=json.loads(pathlib.Path('/workspace/scratch/textstats-live-harness-20261004/INPUTS.json').read_text());inp['local_checkout']=str(R);(O/'INPUTS.json').write_text(json.dumps(inp,indent=2)+'\n')
e={'schema_version':1,'literals':{}}
for suite in ['baseline','json']:e['literals'].update(json.loads((O/f'actual-{suite}.json').read_text())['literals'])
(O/'actual-combined.json').write_text(json.dumps(e,indent=2)+'\n')
common=['--inputs',str(O/'INPUTS.json'),'--run-state',str(O/'RUN-STATE.json'),'--contract',str(H/'cases/assessor/A-007.json'),'--evidence',str(O/'actual-combined.json')]
run(['python',str(H/'scripts/assess.py'),*common,'--output',str(O/'original-deterministic.json')])
run(['python','/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5/runs/A-006/2/checker-variant/assess_git_owners.py',*common,'--output',str(O/'variant-deterministic.json')])
