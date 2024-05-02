#!/usr/bin/python3

import re

text = r'38.153.152.64 - [2024-05-02 15:15:30.674796] "GET /projects/260 HTTP/1.1" 405 268'
pat = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[[0-9]+-[0-9]+-[0-9]+ [0-9]+:[0-9]+:[0-9]+\.[0-9]+\] "GET /projects/260 HTTP/1\.1" ([0-9]+) [0-9]+'
match = re.match(pat, text)
print("Status Code:", match.group(1))

