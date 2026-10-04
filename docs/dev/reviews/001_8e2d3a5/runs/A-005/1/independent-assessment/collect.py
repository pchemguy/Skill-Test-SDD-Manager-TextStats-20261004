import datetime,hashlib,json,pathlib,subprocess,sys
root=pathlib.Path('/workspace/scratch/textstats-live-20261004'); out=pathlib.Path(__file__).parent
def run(args):
 p=subprocess.run(args,cwd=root,capture_output=True,text=True); return dict(argv=args,cwd=str(root),returncode=p.returncode,stdout=p.stdout,stderr=p.stderr)
commands=[['git','status','--porcelain=v1'],['git','rev-parse','HEAD'],['git','branch','--show-current'],['git','rev-parse','main'],['git','log','-6','--format=%H %P %cI %s'],['git','ls-remote','origin','refs/heads/main','refs/heads/phase/1-named-file-utility'],['git','diff','--check'],['git','ls-files','--stage'],['git','diff','9b24dbd8bacbfcfa8e09c38e131baaecc3ba8f76','HEAD','--name-only'],['git','log','--format=%H %s','--name-status','9b24dbd8bacbfcfa8e09c38e131baaecc3ba8f76..HEAD'],[sys.executable,'-B','-m','unittest','discover','-s','tests/unit','-t','.','-v'],[sys.executable,'-B','-m','unittest','discover','-s','tests/integration','-t','.','-v']]
for resource in ['issues?state=all&per_page=100','milestones?state=all&per_page=100','milestones/1','issues?milestone=1&state=all&per_page=100']:
 commands.append([sys.executable,str(root/'.git/textstats-hosting-curl.py'),'GET',resource])
records=[run(c) for c in commands]
(out/'INDEPENDENT-COMMANDS.json').open('x').write(json.dumps(dict(assessed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),commands=records),indent=2)+'\n')
manifest=json.loads((root/'textstats-run-resources/PLUGIN-SOURCE.json').read_text())
hashes={p:hashlib.sha256((root/'textstats-run-resources/plugin'/p).read_bytes()).hexdigest() for p in manifest['package_hashes']}
(out/'PINNED-PACKAGE-VERIFICATION.json').open('x').write(json.dumps(dict(commit=manifest['commit'],actual_hashes=hashes,all_hashes_match=hashes==manifest['package_hashes']),indent=2)+'\n')
print(json.dumps(dict(statuses=[r['returncode'] for r in records],pin_equal=hashes==manifest['package_hashes'])))
