"""Create a function that validates whether three given integers form a Pythagorean triplet.
The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

Examples
is_triplet(3, 4, 5) ➞ True
# 3² + 4² = 25
# 5² = 25

is_triplet(13, 5, 12) ➞ True
# 5² + 12² = 169
# 13² = 169

is_triplet(1, 2, 3) ➞ False
# 1² + 2² = 5
# 3² = 9

Notes
Numbers may not be given in a sorted order.
"""


def is_triplet(a, b, c):
    numbers = [a, b, c]
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    firstAndSecond = numbers[0] ** 2 + numbers[1] ** 2
    Third = numbers[2] ** 2
    if firstAndSecond == Third:
        return True
    else:
        return False


print(is_triplet(3, 4, 5))  # True
print(is_triplet(13, 5, 12))  # True
print(is_triplet(1, 2, 3))  # False
