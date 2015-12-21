#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Write current time to a specific file.
"""

import os
import sys
from datetime import datetime

TIME_FILE = "time.txt"


now = datetime.now()
if not os.path.exists(TIME_FILE):
    print "first run"
    f = open(TIME_FILE, 'w')
    f.write("%s\n" % now.strftime("%Y-%m-%d %X"))
    print "write %s to %s" % (now, TIME_FILE)
    f.close()
    sys.exit(0)


f = open(TIME_FILE, 'r')
old_time = datetime.strptime(f.read().strip(), "%Y-%m-%d %X")
f.close()

if old_time.date() == now.date():
    print "skip write"
else:
    f = open(TIME_FILE, 'w')
    f.write("%s\n" % now.strftime("%Y-%m-%d %X"))
    print "write %s to %s" % (now, TIME_FILE)
    f.close()
