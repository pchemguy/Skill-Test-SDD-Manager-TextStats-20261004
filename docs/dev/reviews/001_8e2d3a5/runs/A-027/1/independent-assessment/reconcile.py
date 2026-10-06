import pathlib,json,hashlib,subprocess,datetime
P=pathlib.Path('/workspace/scratch/textstats-live-evidence-20261004/docs/dev/reviews/001_8e2d3a5'); O=P/'runs/A-027/1/independent-assessment'; E=P.parents[3]; R=pathlib.Path('/workspace/scratch/textstats-live-20261004')
def sha(b):return hashlib.sha256(b).hexdigest()
def git(r,*a):
 x=subprocess.run(['git','-C',str(r),*a],capture_output=True);return {'args':list(a),'exit_code':x.returncode,'stdout':x.stdout.decode(),'stderr':x.stderr.decode()}
c=json.loads((P/'COVERAGE.json').read_text());head=git(E,'rev-parse','HEAD')['stdout'].strip();rows=[]
for k,v in c['cases'].items():
 for a in v['attempts']:
  rel=a.get('current_assessment',a.get('assessment')); row={'case_id':k,'attempt':a['attempt'],'coverage_status':a['status'],'selected_assessment':rel}
  if rel:
   f=P/rel;b=f.read_bytes();j=json.loads(b);remote=git(E,'show',head+':'+str(f.relative_to(E)));row.update(status=j.get('status'),agent_behavior_assessed=j.get('agent_behavior_assessed'),sha256=sha(b),published_bytes_equal=remote['exit_code']==0 and remote['stdout'].encode()==b,checkpoint_refs=j.get('checkpoint_refs'),initial_status=j.get('first_attempt_status',j.get('initial_outcome',a.get('initial_status'))),assisted=j.get('assisted',a.get('assisted',False)))
  rows.append(row)
s=json.loads((R/'textstats-run-resources/PLUGIN-SOURCE.json').read_text()); mismatches=[]
for path,h in s['package_hashes'].items():
 f=R/'textstats-run-resources/plugin'/path
 if not f.is_file() or sha(f.read_bytes())!=h:mismatches.append(path)
commands=[git(R,'show','-s','--format=%H%n%P%n%D','HEAD'),git(R,'status','--porcelain'),git(R,'diff','--exit-code'),git(R,'diff','--cached','--exit-code'),git(R,'ls-remote','origin','refs/heads/main','refs/heads/phase/2-output-and-source-extensions','refs/heads/revision/003_0e47414-remove-json'),git(E,'ls-remote','origin','refs/heads/revision/001_8e2d3a5-live-acceptance')]
out={'schema_version':1,'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'evidence_baseline':head,'selected_assessments':rows,'pin':{'commit':s['commit'],'fingerprint':s['fingerprint'],'file_count':len(s['package_hashes']),'mismatches':mismatches,'source_manifest_sha256':sha((R/'textstats-run-resources/PLUGIN-SOURCE.json').read_bytes()),'plugin_manifest_sha256':s['package_hashes']['.codex-plugin/plugin.json']},'commands':commands}
(O/'RECONCILIATION.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'selected':len(rows),'mismatches':mismatches,'unpublished':[r['selected_assessment'] for r in rows if r.get('published_bytes_equal') is False],'evidence_baseline':head}))
