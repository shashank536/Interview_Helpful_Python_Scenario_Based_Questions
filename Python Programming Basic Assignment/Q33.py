"""Create a function that takes a string and returns a string in which each character is repeated once.
Examples
double_char("String") ➞ "SSttrriinngg"

double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

double_char("1234!_ ") ➞ "11223344!!__  "
"""


def double_char(text):
    new_text = ""
    for i in text:
        doubleheader = i * 2
        new_text += doubleheader
    return new_text


print(double_char("String"))
print(double_char("Hello World!"))
print(double_char("1234!_ "))
