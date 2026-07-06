"""Given a string of numbers separated by a comma and space, return the product of the numbers.
Examples
multiply_nums("2, 3") ➞ 6

multiply_nums("1, 2, 3, 4") ➞ 24

multiply_nums("54, 75, 453, 0") ➞ 0

multiply_nums("10, -2") ➞ -20
"""


def multiply_nums(num):
    numbers = num.split(",")
    count = 1
    for i in numbers:
        count *= int(i)
    return count


print(multiply_nums("2, 3"))  # 6
print(multiply_nums("1, 2, 3, 4"))  # 24
print(multiply_nums("54, 75, 453, 0"))  # 0
print(multiply_nums("10, -2"))  # -20
