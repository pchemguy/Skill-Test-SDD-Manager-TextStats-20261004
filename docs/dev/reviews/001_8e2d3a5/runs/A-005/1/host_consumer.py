import sys,subprocess,json,pathlib,shlex
p=pathlib.Path(__file__).parent
label=sys.argv[1]; args=["python",".git/textstats-hosting-curl.py"]+sys.argv[2:]
r=subprocess.run(args,cwd="/workspace/scratch/textstats-live-20261004",text=True,capture_output=True)
try:
 d=json.loads(r.stdout)
 def clean(x):
  if isinstance(x,list): return [clean(v) for v in x]
  if isinstance(x,dict): return {k:clean(v) for k,v in x.items() if k in ("http_status","transport","result","number","title","state","state_reason","html_url","open_issues","closed_issues","milestone","message")}
  return x
 out=json.dumps(clean(d),indent=2)
except Exception: out="Non-JSON response; exit "+str(r.returncode)+"; response withheld"
(p/(label+".json")).write_text(out)
with (p/"consumer-command-journal.md").open("a") as f: f.write("\n## "+label+"\n\nStanding human GO and scoped read/write token grant authorize this maintained repository operation. Command: `"+shlex.join(args)+"`. Exit: "+str(r.returncode)+". Sanitized observed metadata: ["+label+".json]("+label+".json).\n")
print(out); print("EXIT",r.returncode)
