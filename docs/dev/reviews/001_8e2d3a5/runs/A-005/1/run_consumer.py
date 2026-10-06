import sys, subprocess, pathlib, datetime, shlex
p=pathlib.Path(__file__).parent
label=sys.argv[1]; args=sys.argv[2:]
r=subprocess.run(args,cwd="/workspace/scratch/textstats-live-20261004",text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(p/(label+".txt")).write_text(r.stdout)
with (p/"consumer-command-journal.md").open("a") as f:
 f.write("\n## "+label+"\n\nCommand: `"+shlex.join(args)+"`\n\nExit: "+str(r.returncode)+". Actual combined output: ["+label+".txt]("+label+".txt).\n")
print(r.stdout); print("EXIT",r.returncode)
