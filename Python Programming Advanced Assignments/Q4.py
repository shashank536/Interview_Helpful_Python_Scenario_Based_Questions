"""
Write a function that takes a number and returns True if it's a prime; False otherwise.
The number can be 2^64-1 (2 to the power of 63, not XOR).
With the standard technique it would be O(2^64-1),
which is much too large for the 10 second time limit.

Examples

prime(7) ➞ True

prime(56963) ➞ True

prime(5151512515524) ➞ False
"""

import math


def isprime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


print(isprime(7))  # True
print(isprime(56963))  # True
print(isprime(5151512515524))  # False
