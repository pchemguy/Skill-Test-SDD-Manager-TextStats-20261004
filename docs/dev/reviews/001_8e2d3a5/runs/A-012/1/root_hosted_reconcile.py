"""Authorized primary execution of exact authored managed projection payloads; safe observations only."""
import pathlib,subprocess,json,hashlib,time,datetime
r=pathlib.Path(__file__).parent;log=r/'ROOT-HOSTED-RECONCILIATION.json';ops=[]
for n in [14,15,16,17,19,20,21,22]:ops.append(('PATCH',f'issues/{n}',f'issue-{n}-payload.json',{'title','body'}))
for n in [4,5,6,7,8]:ops.append(('PATCH',f'milestones/{n}',f'milestone-{n}-payload.json',{'title','description'}))
for n in [10,11,12]:ops.append(('POST',f'issues/{n}/comments',f'issue-{n}-comment-payload.json',{'body'}))
if log.exists():raise SystemExit('Refuse replay/overwrite; exact readback before retry')
rows=[]
def save():
 p=log.with_suffix('.tmp');p.write_text(json.dumps({'started_at':start,'operations':rows,'provider_bodies_descriptions_withheld':True,'review_reassessment_owner':'primary execution with retained actual human campaign authority'},indent=2)+'\n');p.replace(log)
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
for method,endpoint,filename,keys in ops:
 payload=r/filename;d=json.loads(payload.read_text());assert set(d)==keys
 a=['python','/workspace/scratch/textstats-live-20261004/.git/textstats-hosting-curl.py',method,endpoint,str(payload)];p=subprocess.run(a,capture_output=True)
 try:reply=json.loads(p.stdout)
 except:reply={}
 q=reply.get('result',{});safe={k:q[k] for k in ['id','number','title','state','state_reason','html_url','open_issues','closed_issues'] if isinstance(q,dict) and k in q};row={'method':method,'endpoint':endpoint,'payload_file':filename,'payload_sha256':hashlib.sha256(payload.read_bytes()).hexdigest(),'returncode':p.returncode,'http_status':reply.get('http_status'),'metadata':safe,'safe_error':{k:reply[k] for k in ['error','cause','message','action'] if k in reply and isinstance(reply[k],str)},'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()};rows.append(row);save();print(json.dumps(row),flush=True)
 if p.returncode!=0 or reply.get('http_status')!=(201 if method=='POST' else 200):raise SystemExit('Affected effect uncertain/failed; stopped remaining writes; exact readback required before any retry')
 time.sleep(1)
print('Exact authored reconciliation operations completed; separate live readback still required.',flush=True)
