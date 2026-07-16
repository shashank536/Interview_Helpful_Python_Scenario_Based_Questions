"""
aaabb = True
ababa = False
"""


def check_order(s):
    seen_b = False
    for i in s:
        if i == "b":
            seen_b = True
        elif i == "a" and seen_b:
            return False
    return True


print(check_order("aaabb"))
print(check_order("ababa"))
