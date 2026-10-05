#!/usr/bin/env python
import os,sys
os.execv('/usr/local/bin/git',['/usr/local/bin/git','-c','core.hooksPath=/workspace/scratch/textstats-unpublished-tools-20261005/hooks',*sys.argv[1:]])
