"""Render isolated product handoff only from an independently published predecessor."""
import json,pathlib,subprocess,sys
root=pathlib.Path('/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5')
case,previous,relative,publication,summaryfile=sys.argv[1:]
a=json.loads((root/relative).read_text());out=root/'runs'/case/'1';out.mkdir(parents=True,exist_ok=True)
b={'checkpoints':[{'case_id':previous,'status':a['status'],'assessment_path':str(pathlib.Path('../../..')/relative),'checkpoint_refs':a['checkpoint_refs'],'local_checkout':'/workspace/scratch/textstats-live-20261004','remote':'origin','remote_ref':'refs/heads/'+a['checkpoint_refs']['product_branch'],'evidence_publication':{'status':'published','commit':publication,'path':'docs/dev/reviews/001_8e2d3a5/'+relative,'remote':'origin','ref':'refs/heads/revision/001_8e2d3a5-live-acceptance'}}],'current':{'summary':pathlib.Path(summaryfile).read_text()}}
p=out/'BINDINGS.json'
if p.exists():raise SystemExit('Refuse overwrite')
p.write_text(json.dumps(b,indent=2)+'\n')
result=subprocess.run(['python','/workspace/scratch/textstats-live-harness-20261004/harness/cases/assessor/catalog_tools.py','render','--case',case,'--bindings',str(p),'--output',str(out/'REQUEST.md')],capture_output=True)
(out/'RENDER-RESULT.json').write_text(json.dumps({'argv':'catalog_tools render '+case,'returncode':result.returncode,'stdout':result.stdout.decode(),'stderr':result.stderr.decode()},indent=2)+'\n');print(result.stdout.decode());raise SystemExit(result.returncode)
