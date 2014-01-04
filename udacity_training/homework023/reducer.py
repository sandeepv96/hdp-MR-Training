#!/usr/bin/python

import sys

hits = 0
current = None

winners_hits = 0
winner = None

for line in sys.stdin:

    if not current or current != line:
        current = line
    
    hits += 1

    if not winner or winners_hits < hits:
        winner, winners_hits = current, hits

print "{0}\t{1}".format(winner, winners_hits)
