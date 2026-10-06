from pathlib import Path
import ast, hashlib, json, os, re, subprocess, sys, tarfile, tempfile
root=Path('/workspace/scratch/textstats-live-20261004')
env={k:v for k,v in os.environ.items() if k not in ('PYTHONPATH','PYTHONHOME','PYTHONSTARTUP')}
env.update(PYTHONNOUSERSITE='1', PYTHONDONTWRITEBYTECODE='1')
def run(args,cwd,**kw):
 r=subprocess.run(args,cwd=cwd,env=env,capture_output=True,text=True,**kw)
 print(json.dumps({'command':args,'cwd':str(cwd),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}))
 return r
with tempfile.TemporaryDirectory(prefix='textstats-continuation-') as temp:
 temp=Path(temp)
 r=run(['make','dist',f'DIST_DIR={temp / "build"}'],root); assert r.returncode==0
 extracted=temp/'extracted'; extracted.mkdir()
 with tarfile.open(temp/'build/textstats.tar.gz') as arc: arc.extractall(extracted,filter='data')
 r=run([sys.executable,'-c','import textstats; print(textstats.__file__)'],extracted)
 assert r.returncode==0 and Path(r.stdout.strip())==extracted/'textstats/__init__.py'
 total=0; skipped=0
 for file in ('README.md','docs/api.md','docs/module.md'):
  for number,(language,body) in enumerate(re.findall(r'```(python|sh)\n(.*?)```', (root/file).read_text(), re.S),1):
   if 'unittest discover' in body:
    skipped+=1; print(f'{file} fence {number}: suite fence independently covered'); continue
   total+=1; cwd=extracted
   if language=='python':
    r=run([sys.executable,'-c',body],cwd); assert r.returncode==0 and not r.stdout and not r.stderr
   else:
    lines=body.splitlines()
    for i,line in enumerate(lines):
     line=line.strip()
     if not line or line.startswith('#'): continue
     if line.startswith('cd '):
      cwd=cwd/line[3:]; assert cwd.is_dir(); continue
     r=run(['/bin/sh','-c',line],cwd)
     comment=lines[i+1].strip() if i+1<len(lines) else ''
     status=re.search(r'# status (\d+)',comment)
     expected=int(status[1]) if status else 0
     assert r.returncode==expected,(file,number,line,r.returncode,expected)
     if comment.startswith('# lines='): assert r.stdout==comment[2:]+'\n' and not r.stderr
     if status:
      assert not r.stdout and r.stderr and 'Traceback' not in r.stderr
      if 'stdin' in comment: assert 'stdin' in r.stderr
      if 'nonexistent.txt' in comment: assert 'nonexistent.txt' in r.stderr
   print(f'{file} fence {number}: passed')
 assert total==13 and skipped==1,(total,skipped)
 print(f'PUBLIC_EXAMPLES passed={total} suite_fences_independently_covered={skipped}')
links=0
for file in [root/'README.md',root/'AI_DISCLOSURE.md',root/'SDD-MANAGER.md',*root.glob('docs/**/*.md')]:
 for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)',file.read_text()):
  if '://' in target or target.startswith('#'):continue
  target=target.split('#')[0]
  assert (file.parent/target).exists(),(file,target)
  links+=1
print(f'LOCAL_LINKS checked={links} broken=0')
tasks=(root/'docs/dev/TASKS.md').read_text()
ids=re.findall(r'(?m)^\s*- \[x\] (T-\d{3}) —',tasks)
assert len(ids)==22 and len(set(ids))==22 and '[ ]' not in tasks and 'Completion reassessment pending' not in tasks
print('TASK_OWNERS unique=22 complete=22 unchecked=0 reassessment_pending=0')
for file in root.glob('textstats/*.py'): assert ast.get_docstring(ast.parse(file.read_text())),file
print('PRODUCTION_MODULE_DOCSTRINGS verified=5')
assert hashlib.sha256((root/'-json-9l969okj/sample.txt').read_bytes()).hexdigest()=='f1945cd6c19e56b3c1c78943ef5ec18116907a4ca1efc40a57d48ab1db7adfc5'
print('SAMPLE preserved')
for args in (['git','--no-optional-locks','diff','--check','HEAD^1','HEAD'],['git','--no-optional-locks','diff','--exit-code','HEAD^1','HEAD','--','AGENTS.md','textstats-run-resources'],['git','--no-optional-locks','diff','--exit-code','HEAD'],['git','--no-optional-locks','diff','--cached','--exit-code']):
 r=run(args,root); assert r.returncode==0
print('WHITESPACE_RESOURCE_AND_TRACKED_INDEX_PRESERVATION passed')
