"""The "Reverser" takes a string as input and returns that string in reverse order,
with the opposite case.

Examples
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
"""


def reverse(text):
    reversed_text = ""
    for i in text:
        if i.islower():
            reversed_text = i.upper() + reversed_text
        else:
            reversed_text = i.lower() + reversed_text
    return reversed_text


print(reverse("Hello World"))  # "DLROw OLLEh"
print(reverse("ReVeRsE"))  # "eSrEvEr"
print(reverse("Radar"))  # "RADAr"
