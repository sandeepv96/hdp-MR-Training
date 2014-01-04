#!/usr/bin/python

import sys

hits = 0
hitted = None

for line in sys.stdin:
    
    if not hitted or hitted != line:
        print "{0}\t{1}".format(hitted, hits)
        hits = 0
        hitted = line
    hits += 1

print "{0}\t{1}".format(hitted, hits)
