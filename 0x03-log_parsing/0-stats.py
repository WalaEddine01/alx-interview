#!/usr/bin/python3
"""
This script reads from standard input and computes metrics
"""
import re
import sys

# Define the regex pattern
pat = (
    r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ - \[[0-9]+-[0-9]+-[0-9]+ '
    r'[0-9]+:[0-9]+:[0-9]+\.[0-9]+\] "GET /projects/260 HTTP/1\.1" '
    r'([0-9]+) ([0-9]+)'
)

data = []
total_size = 0
count = 0

try:
    for line in sys.stdin:
        match = re.match(pat, line)
        if match:
            # Extract status code and file size
            status_code = match.group(1)
            file_size = int(match.group(2))
            # Update total size and count
            total_size += file_size
            count += 1
            # Append status code to data list
            data.append(status_code)

            # Print statistics after every 10 lines
            if count == 10:
                print("File size:", total_size)
                # Sort the data list
                data.sort()
                # Print status codes
                for code in ["200", "301", "400", "401", "403",
                             "404", "405", "500"]:
                    if code in data:
                        print("{}: {}".format(code, data.count(code)))
                # Reset count and clear data list
                count = 0
                data.clear()

except KeyboardInterrupt:
    # Handle KeyboardInterrupt gracefully
    pass

finally:
    # Print final statistics
    print("File size:", total_size)
    data.sort()
    for code in ["200", "301", "400", "401", "403", "404", "405", "500"]:
        if code in data:
            print("{}: {}".format(code, data.count(code)))
