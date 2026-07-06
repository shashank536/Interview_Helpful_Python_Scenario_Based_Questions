"""Create a function that takes a string and returns True or False,
depending on whether the characters are in order or not.

Examples
is_in_order("abc") ➞ True

is_in_order("edabit") ➞ False

is_in_order("123") ➞ True

is_in_order("xyzz") ➞ True

Notes:
You don't have to handle empty strings.
"""


def is_in_order(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


print(is_in_order("abc"))  # True
print(is_in_order("edabit"))  # False
print(is_in_order("123"))  # True
print(is_in_order("xyzz"))  # True
