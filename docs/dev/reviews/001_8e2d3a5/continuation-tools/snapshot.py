"""Read-only Git-visible state capture, excluding ignored protected stores."""
import sys,json,subprocess,pathlib,hashlib,datetime,os,stat
root=pathlib.Path(sys.argv[1]);dest=pathlib.Path(sys.argv[2])
def cmd(*args):
 p=subprocess.run(['git','--no-optional-locks','-C',str(root),*args],capture_output=True,check=True)
 return p.stdout.decode()
paths=cmd('ls-files','-z','--cached','--others','--exclude-standard').split('\0');files={}
for n in sorted(set(paths)-{''}):
 p=root/n
 if not p.exists() and not p.is_symlink():files[n]={'missing':True};continue
 s=p.lstat();b=os.readlink(p).encode() if p.is_symlink() else p.read_bytes()
 files[n]={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'mode':stat.S_IMODE(s.st_mode),'symlink':p.is_symlink()}
d={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(root),'head':cmd('rev-parse','HEAD').strip(),'branch':cmd('symbolic-ref','--short','HEAD').strip(),'status':cmd('status','--porcelain=v1','--untracked-files=all'),'refs':cmd('for-each-ref','--format=%(refname) %(objectname)','refs/heads','refs/remotes/origin'),'index':cmd('ls-files','--stage'),'files':files,'ignored_paths_excluded':True}
dest.parent.mkdir(parents=True,exist_ok=True)
if dest.exists():raise SystemExit('Refuse overwrite')
dest.write_text(json.dumps(d,indent=2)+'\n');print(str(dest),len(files),'visible files',d['head'])
