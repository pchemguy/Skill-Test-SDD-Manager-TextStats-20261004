#!/usr/bin/env python
import os,sys
os.execv('/usr/local/bin/git',['/usr/local/bin/git','-c','core.hooksPath=/workspace/scratch/textstats-staged-tools-20261005/hooks',*sys.argv[1:]])
