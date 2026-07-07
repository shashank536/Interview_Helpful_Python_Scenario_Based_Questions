"""Create a function that reverses a boolean value and returns
the string "boolean expected" if another variable type is given.
Examples
reverse(True) ➞ False

reverse(False) ➞ True

reverse(0) ➞ "boolean expected"

reverse(None) ➞ "boolean expected"

"""


def reverse(boolean):
    if type(boolean) == bool:
        return not boolean
    else:
        raise ValueError("boolean expected")


print(reverse(True))
print(reverse(0))
