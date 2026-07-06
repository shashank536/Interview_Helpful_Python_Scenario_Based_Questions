"""
Create a function that takes three integer arguments (a, b, c) and
returns the amount of integers which are of equal value.

Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0

Notes
Your function must return 0, 2 or 3.
"""


def equal(a, b, c):
    number = [a, b, c]
    count = {}
    for i in number:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    for value in count.values():
        if value == 3:
            return 3
        elif value == 2:
            return 2
    return 0


print(equal(3, 4, 3))  # 2
print(equal(1, 1, 1))  # 3
print(equal(3, 4, 1))  # 0
