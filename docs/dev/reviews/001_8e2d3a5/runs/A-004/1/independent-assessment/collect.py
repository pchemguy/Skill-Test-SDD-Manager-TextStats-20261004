import datetime, hashlib, json, pathlib, subprocess, sys
root=pathlib.Path('/workspace/scratch/textstats-live-20261004')
out=pathlib.Path(__file__).parent
def run(args,cwd=root):
    p=subprocess.run(args,cwd=cwd,capture_output=True,text=True)
    return {'argv':args,'cwd':str(cwd),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
records=[]
for args in [['git','status','--porcelain=v1'],['git','rev-parse','HEAD'],['git','branch','--show-current'],['git','rev-parse','main'],['git','show','--format=fuller','--stat','HEAD'],['git','diff','d009899e39790c39be32ae77e7fe8294bf60d04c','HEAD','--','docs/dev/TASKS.md','README.md'],['git','ls-remote','origin','refs/heads/main','refs/heads/phase/1-named-file-utility'],['git','diff','--check'],['git','ls-files','--stage'],['git','diff','--name-only','d009899e39790c39be32ae77e7fe8294bf60d04c','HEAD'],[sys.executable,'-B','-m','unittest','discover','-s','tests/unit','-t','.','-v'],[sys.executable,str(root/'.git/textstats-hosting-curl.py'),'GET','issues?state=all&per_page=100&page=1'],[sys.executable,str(root/'.git/textstats-hosting-curl.py'),'GET','milestones?state=all&per_page=100&page=1']]: records.append(run(args))
code='''import contextlib,dataclasses,io,json,textstats
vectors=[('',True,0,0),('a\\r\\nb\\r c\\n',True,3,3),('\\ufeff\\r\\n',True,1,0),('\\ufeff\\ufeff\\r\\n',True,1,1),('x\\u2029y\\u0085z',True,1,3),('\\r\\n\\r\\n',True,2,0),('\\n\\r',True,2,0),('a\\ufeffb',True,1,1),('\\ufeff a',False,1,2)]
stdout,stderr=io.StringIO(),io.StringIO(); rows=[]
with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
 for s,b,l,w in vectors:
  actual=textstats.count_text(s,strip_bom=b); assert (actual.lines,actual.words)==(l,w); rows.append({'text':s,'strip_bom':b,'expected':[l,w],'actual':[actual.lines,actual.words]})
 for bad in (-1,False,1.2,'2'):
  try: textstats.TextStats(bad,0)
  except (TypeError,ValueError): pass
  else: raise AssertionError('invalid count accepted')
 value=textstats.TextStats(0,0)
 try: value.lines=1
 except dataclasses.FrozenInstanceError: pass
 else: raise AssertionError('mutable')
assert not stdout.getvalue() and not stderr.getvalue()
print(json.dumps({'import_origin':textstats.__file__,'vectors':rows,'silence':True,'immutable':True,'invalid_counts_rejected':True}))
'''
records.append(run([sys.executable,'-B','-c',code]))
manifest=json.loads((root/'textstats-run-resources/PLUGIN-SOURCE.json').read_text()); hashes={p:hashlib.sha256((root/'textstats-run-resources/plugin'/p).read_bytes()).hexdigest() for p in manifest['package_hashes']}
verification={'source_commit':manifest['commit'],'file_count':len(hashes),'all_hashes_match':hashes==manifest['package_hashes'],'actual_hashes':hashes}
(out/'PINNED-PACKAGE-VERIFICATION.json').write_text(json.dumps(verification,indent=2)+'\n')
tracked=run(['git','ls-files']).get('stdout').splitlines()
file_hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in tracked if not p.startswith('textstats-run-resources/')}
(out/'SOURCE-HASHES.json').write_text(json.dumps(file_hashes,indent=2)+'\n')
for filename,data in [('INDEPENDENT-COMMANDS.json',{'assessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'commands':records})]: (out/filename).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'commands':len(records),'statuses':[r['returncode'] for r in records],'pinned_hashes_match':verification['all_hashes_match']}))
