#!/usr/bin/python

import sys

n_of_sales = 0
total_sales = 0

for line in sys.stdin:
    total_sales += float(line)
    n_of_sales += 1

print n_of_sales
print total_sales
