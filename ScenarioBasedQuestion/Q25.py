""" Create a function that returns True if a given inequality expression is correct and False otherwise.
Examples
correct_signs("3 < 7 < 11") ➞ True

correct_signs("13 > 44 > 33 > 1") ➞ False

correct_signs("1 < 2 < 6 < 9 > 3") ➞ True
"""


def correct_signs(expression):
    data = expression.split()
    for i in range(1, len(data), 2):
        left = int(data[i - 1])
        operator = data[i]
        right = int(data[i + 1])
        if operator == "<":
            if left >= right:
                return False
        elif operator == ">":
            if left <= right:
                return False

    return True


print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 > 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))
