#!/usr/bin/python3
"""
This script reads from standard input and computes metrics
"""
import re
import signal
import sys


pat = (
    r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[[0-9]+-[0-9]+-[0-9]+ '
    r'[0-9]+:[0-9]+:[0-9]+\.[0-9]+\] "GET /projects/260 HTTP/1\.1" '
    r'([0-9]+) ([0-9]+)'
)

data = []
sum = 0

try:
    for line in sys.stdin:
        match = re.match(pat, line)
        if match:
            data.append(match.group(1))
            response_size = int(match.group(2))
            sum += response_size
        if len(data) % 10 == 0:
            print("File size: " + str(sum))
            data.sort()
            for code in set(data):
                print("{}: {}".format(code, data.count(code)))
except KeyboardInterrupt:
    print("File size: " + str(sum))
    data.sort()
    for code in set(data):
        print("{}: {}".format(code, data.count(code)))
