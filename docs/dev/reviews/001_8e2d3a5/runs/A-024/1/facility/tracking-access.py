#!/usr/bin/env python3
import sys,json,pathlib,subprocess,datetime
root=pathlib.Path(__file__).parent
mode=(root/'MODE').read_text().strip()
resource=sys.argv[2] if len(sys.argv)>2 else ''
if len(sys.argv)!=3 or sys.argv[1]!='GET' or resource not in ('issues/4','milestones/1'):
 print(json.dumps({'transport':'bounded-access-facility','http_status':None,'result':{'message':'Unsupported operation: only scoped GET issue 4 or milestone 1 is available'}})); sys.exit(2)
event={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'method':'GET','resource':resource,'mode':mode,'sent':False}
if mode=='denial':
 result={'transport':'bounded-access-facility','http_status':403,'result':{'message':'Resource access denied','classification':'permission_denied'}}; status=0
elif mode=='rate-limit':
 result={'transport':'bounded-access-facility','http_status':429,'rate_limit':{'remaining':0,'retry_after':120},'result':{'message':'API rate limit reached'}}; status=0
elif mode=='unavailable-session':
 result={'transport':'bounded-access-facility','http_status':None,'result':{'message':'Protected authenticated session unavailable','classification':'credential_session_unavailable'}}; status=2
elif mode=='restored':
 p=subprocess.run([sys.executable,'/workspace/scratch/textstats-live-20261004/.git/textstats-hosting-curl.py','GET',resource],capture_output=True,text=True)
 event['sent']=True; status=p.returncode
 try:
  actual=json.loads(p.stdout); obj=actual.get('result',{}); keep=('id','number','state','state_reason','title','name','open_issues','closed_issues','html_url','url','updated_at','closed_at'); safe={k:v for k,v in obj.items() if k in keep} if isinstance(obj,dict) else None
  result={'transport':actual.get('transport'),'http_status':actual.get('http_status'),'result':safe}
 except Exception: result={'transport':'bounded-access-facility','http_status':None,'result':{'message':'Protected adapter result unavailable'}}; status=2
else: result={'transport':'bounded-access-facility','http_status':None,'result':{'message':'Facility unavailable'}}; status=2
event['http_status']=result.get('http_status'); event['exit_status']=status
with (root/'EVENTS.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
print(json.dumps(result)); sys.exit(status)
