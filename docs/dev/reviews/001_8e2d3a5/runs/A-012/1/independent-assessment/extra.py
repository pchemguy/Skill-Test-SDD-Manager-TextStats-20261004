import json,re,subprocess,sys,hashlib,os
from pathlib import Path
O=Path(__file__).parent;P=Path('/workspace/scratch/textstats-live-20261004');E=O/'extracted'
def g(*a):return subprocess.run(['git','-C',str(P),*a],capture_output=True,check=True).stdout
prep='b7a4a7e47f512e541b670d0c6f02b2bd5746afc2'
qc=[]
for name in ['SPEC-REVIEW-REPORT','PLAN-REVIEW-REPORT','TASKS-REVIEW-REPORT']:
 t=(P/'docs/dev'/f'{name}.md').read_text();tail=t[t.rfind('## Revision '):];matches=[]
 for n,h in re.findall(r'^- ([A-Za-z-]+\.md): `([0-9a-f]{64})`',tail,re.M):
  b=g('show',prep+':docs/dev/'+n)
  matches.append({'path':'docs/dev/'+n,'declared_sha256':h,'preparation_sha256':hashlib.sha256(b).hexdigest(),'matches_preparation':hashlib.sha256(b).hexdigest()==h,'current_sha256':hashlib.sha256((P/'docs/dev'/n).read_bytes()).hexdigest()})
 old=g('show','0e47414:docs/dev/'+name+'.md').decode();body=t[t.find('## '):t.rfind('## Revision ')]
 qc.append({'report':name,'identities':matches,'history_retained':old[old.find('## '):].strip() in body.strip()})
(O/'QC-IDENTITIES.json').write_text(json.dumps(qc,indent=2)+'\n')
docs=[]
for f in ['README.md','docs/module.md','docs/api.md']:
 t=(P/f).read_text()
 for i,(lang,code) in enumerate(re.findall(r'```(python|sh)\n(.*?)\n```',t,re.S)):
  if 'unittest discover' in code or 'make dist' in code:continue
  commands=[code] if lang=='python' else [l for l in code.splitlines() if l and not l.startswith('#')]
  for k,c in enumerate(commands):
   r=subprocess.run([sys.executable,'-c',c] if lang=='python' else ['bash','-c',c],cwd=E,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPATH':str(E)},capture_output=True,text=True)
   expected=2 if '--lines=2:1' in c else 1 if 'nonexistent.txt' in c else 0
   docs.append({'source':f,'block':i,'command':c,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'expected_status':expected,'status_matches':r.returncode==expected})
(O/'DOC-EXAMPLES.json').write_text(json.dumps(docs,indent=2)+'\n')
tasks=(P/'docs/dev/TASKS.md').read_text();ids=re.findall(r'^\s*- \[([ x])\] (T-\d+) — (.*)$',tasks,re.M)
retained={n: g('diff','0e47414','HEAD','--',n)==b'' for n in ['textstats/core.py','textstats/io.py','textstats/__init__.py','docs/api.md','docs/dev/features','docs/dev/reports/phases/2/2.1.md']}
pending=[{'id':n,'checked':s=='x'} for s,n,_ in ids if n in ['T-013','T-014','T-015','T-016','T-017']]
links=[]
for f in ['README.md','docs/module.md','docs/api.md','docs/dev/SPEC.md','docs/dev/PLAN.md','docs/dev/TASKS.md']:
 for target in re.findall(r'\]\(([^)]+)\)',(P/f).read_text()):
  if not re.match(r'https?://|#',target):links.append({'source':f,'target':target,'exists':(P/f).parent.joinpath(target.split('#')[0]).exists()})
(O/'SEMANTIC-OBSERVATIONS.json').write_text(json.dumps({'unchanged_retained_sources':retained,'task_ids_unique':len(ids)==len({x[1] for x in ids}),'pending_tasks':pending,'json_historical_heading': 'Milestone 2.1 — Retired historical JSON output' in tasks,'public_local_links':links},indent=2)+'\n')
print(json.dumps({'qc_match':all(m['matches_preparation'] for q in qc for m in q['identities']),'qc_history': [q['history_retained'] for q in qc],'docs_commands':len(docs),'docs_failed':[r for r in docs if not r['status_matches']],'pending':pending,'retained':retained}))
