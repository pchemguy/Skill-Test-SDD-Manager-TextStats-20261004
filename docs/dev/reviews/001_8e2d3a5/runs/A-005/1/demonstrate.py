import pathlib,subprocess,sys,tempfile
from textstats import count_file
with tempfile.TemporaryDirectory(prefix="-demo-",dir=".") as d:
 for name,data,args in [("normal.txt",b"alpha beta\r\ngamma\r",[]),("bom.txt","\ufeff\n".encode(),[]),("bom-kept.txt","\ufeff\n".encode(),["--keep-bom"])]:
  path=pathlib.Path(d)/name; path.write_bytes(data)
  command=[sys.executable,"-m","textstats",*args,"--",str(path)]
  r=subprocess.run(command,capture_output=True,text=True)
  print("Named-file demo:",name,"dash-prefixed relative filename; options",args)
  print("CLI",r.returncode,repr(r.stdout),repr(r.stderr))
  print("API",count_file(path,strip_bom=not bool(args)))
  assert r.returncode==0 and not r.stderr and path.read_bytes()==data
