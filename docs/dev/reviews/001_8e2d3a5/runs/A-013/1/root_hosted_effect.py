"""Primary acceptance evidence wrapper; invokes existing protected adapter privately."""
import sys, pathlib, subprocess, json, hashlib, datetime
method, resource, payload_arg, record_arg = sys.argv[1:]
record = pathlib.Path(record_arg)
if record.exists():
    raise SystemExit('Refuse overwrite of retained effect evidence')
args = ['python', '/workspace/scratch/textstats-live-20261004/.git/textstats-hosting-curl.py', method, resource]
payload = None if payload_arg == '-' else pathlib.Path(payload_arg)
if payload is not None:
    args.append(str(payload))
result = subprocess.run(args, capture_output=True)
data = {'at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'method': method, 'resource': resource, 'exit_code': result.returncode, 'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(), 'stderr_sha256': hashlib.sha256(result.stderr).hexdigest()}
if payload is not None:
    data.update(payload_path=str(payload), payload_sha256=hashlib.sha256(payload.read_bytes()).hexdigest(), payload_keys=sorted(json.loads(payload.read_text())))
try:
    response = json.loads(result.stdout)
except (ValueError, UnicodeDecodeError):
    data['response_json'] = False
else:
    data.update(response_json=True, transport=response.get('transport'), http_status=response.get('http_status'))
    for key in ['error', 'cause', 'message', 'action']:
        if response.get(key) is not None:
            data[key] = response[key]
    def safe(value):
        if not isinstance(value, dict):
            return {'result_type': type(value).__name__}
        row = {k: value[k] for k in ['id', 'number', 'title', 'state', 'state_reason', 'open_issues', 'closed_issues', 'url', 'html_url'] if k in value}
        if isinstance(value.get('milestone'), dict):
            row['milestone'] = {k: value['milestone'][k] for k in ['id', 'number', 'title', 'state'] if k in value['milestone']}
        if 'labels' in value:
            row['label_names'] = [x.get('name') for x in value['labels'] if isinstance(x, dict)]
        if payload is not None:
            authored = json.loads(payload.read_text())
            row['returned_owned_matches'] = {k: value[k] == v for k, v in authored.items() if k in value and k in ['title', 'body', 'description', 'state', 'state_reason']}
        return row
    value = response.get('result')
    data['result'] = [safe(x) for x in value] if isinstance(value, list) else safe(value)
record.parent.mkdir(parents=True, exist_ok=True)
tmp = record.with_suffix(record.suffix + '.tmp')
tmp.write_text(json.dumps(data, indent=2) + '\n')
tmp.replace(record)
print(json.dumps(data))
raise SystemExit(result.returncode or (0 if isinstance(data.get('http_status'), int) and 200 <= data['http_status'] < 300 else 1))
