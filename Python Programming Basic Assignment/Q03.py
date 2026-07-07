"""
Question 3:
Write a program that accepts a comma separated sequence of
words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
"""


def sorting(text):
    words = text.split(",")
    for i in range(len(words)):
        for j in range(len(words) - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]
    return ",".join(words)


print(sorting("without,hello,bag,world"))
