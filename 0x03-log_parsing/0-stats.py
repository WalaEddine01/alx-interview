#!/usr/bin/python3
"""
This script reads from standard input and computes metrics
"""
import re
import sys


pat = (
    r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[[0-9]+-[0-9]+-[0-9]+ '
    r'[0-9]+:[0-9]+:[0-9]+\.[0-9]+\] "GET /projects/260 HTTP/1\.1" '
    r'([0-9]+) ([0-9]+)'
)

data = []
data2 = ["200", "301", "400", "401", "403", "404", "405", "500"]
sum = 0
c = 0

try:
    for line in sys.stdin:
        Match = re.match(pat, line)
        if Match:
            if Match.group(1) in data2:
                data.append(Match.group(1))
            file_size = int(Match.group(2))
            sum += file_size
            c += 1
        if c == 10:
            c = 0
            print("File size: {}".format(sum))
            data.sort()
            for code in ["200", "301", "400", "401", "403",
                         "404", "405", "500"]:
                if code in data:
                    print("{}: {}".format(code, data.count(code)))
except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(sum))
    data.sort()
    for code in ["200", "301", "400", "401", "403",
                 "404", "405", "500"]:
        if code in data:
            print("{}: {}".format(code, data.count(code)))
