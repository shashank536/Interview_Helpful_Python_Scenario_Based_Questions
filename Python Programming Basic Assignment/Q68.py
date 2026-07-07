"""Word Lengths (Homework)

Take a sentence as input. Print each word's length next to it.
Example: Python (6) is (2) great (5).
"""


def wordLengths(sentence):
    count = sentence.split()
    for i in count:
        print(f"{i} ({len(i)})", end=" ")


wordLengths("Anirudh is learning Python programming every single day")
