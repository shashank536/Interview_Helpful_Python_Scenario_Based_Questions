"""
Reverse Word Order

Take a sentence as input. Reverse the order of words (not the characters in
each word). Example: "Python is fun" -> "fun is Python".
"""


def reverseWord(text):
    return " ".join(text.split()[::-1])


print(reverseWord("Python is fun"))
print(reverseWord("I love Bengaluru"))
