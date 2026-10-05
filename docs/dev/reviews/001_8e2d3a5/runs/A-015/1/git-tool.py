#!/usr/bin/env python
import os,sys
os.execv('/usr/local/bin/git',['/usr/local/bin/git','-c','remote.origin.url=/workspace/scratch/textstats-staged-remote-20261005.git','-c','core.hooksPath=/workspace/scratch/textstats-staged-tools-20261005/hooks',*sys.argv[1:]])
