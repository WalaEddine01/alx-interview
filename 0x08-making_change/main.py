#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 5], 11))  # Output: 3 (11 = 5 + 5 + 1)
print(makeChange([2], 3))  # Output: -1 (cannot form 3 with only coins of 2)
print(makeChange([1, 4, 5], 8))  # Output: 2 (8 = 4 + 4)
print(makeChange([1, 2, 5], 0))  # Output: 0 (total is 0, so 0 coins are needed)
print(makeChange([5], 3))  # Output: -1 (cannot form 3 with only coins of 5)
print(makeChange([1, 3, 4], 6))  # Output: 2 (6 = 3 + 3)
print(makeChange([1, 2, 5], 100))  # Output: 20 (100 = 5*20)
print(makeChange([7, 14], 49))  # Output: 7 (49 = 7*7)
print(makeChange([1, 5, 10, 25], 30))  # Output: 2 (30 = 25 + 5)
print(makeChange([3, 7, 8], 15))  # Output: 2 (15 = 7 + 8)
print(makeChange([1, 5, 10, 21], 63)) 