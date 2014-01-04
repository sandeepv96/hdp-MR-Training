#!/usr/bin/python

# The logfile is in Common Log Format:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

import re
import sys

parts = [
    r'(?P<host>\S+)'	# host %h
    r'\S+',		# identity %I
    r'(?P<user>\S+)',	# user %u
    r'\[(?P<time>.+)\]',	# time %t
    r'"(?P<request>.+)"',	# request "%r"
    r'(?P<status>[0-9]+)',	# status %>s
    r'(?P<size>\S+)',	# size %b
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

for line in sys.stdin:
    data = line.split()
    if len(data) != 10:
        continue
    ip, id, user, datetime, timez, method, path, protocol, status, size = data
    print "{0}".format(path)
