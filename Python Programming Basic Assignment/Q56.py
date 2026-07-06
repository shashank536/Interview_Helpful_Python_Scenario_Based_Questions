"""Create a function that takes a list of numbers and return the number that's unique.

Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7

unique([0, 0, 0.77, 0, 0]) ➞ 0.77

unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0

Notes
Test cases will always have exactly one unique number while all others are the same.
"""


def unique(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key, value in count.items():
        if value == 1:
            return key


print(unique([3, 3, 3, 7, 3, 3]))  # 7
print(unique([0, 0, 0.77, 0, 0]))  # 0.77
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))  # 0
