#!/usr/bin/python

import sys

hits = 0
ip = None

for line in sys.stdin:
    
    if not ip or ip != line:
        print "{0}\t{1}".format(ip, hits)
        hits = 0
        ip = line
    hits += 1

print "{0}\t{1}".format(ip, hits)
