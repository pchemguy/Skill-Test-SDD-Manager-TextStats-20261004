#!/usr/bin/env python
import json,os,time,sys
from pathlib import Path
p=Path('/workspace/scratch/textstats-staged-tools-20261005')
(p/'COMMIT-WAITING.json').write_text(json.dumps({'pid':os.getpid(),'cwd':os.getcwd(),'created_at':time.time()}))
for _ in range(900):
 if (p/'RELEASE').exists():sys.exit(0)
 time.sleep(1)
print('Local commit facility unavailable',file=sys.stderr)
sys.exit(1)
