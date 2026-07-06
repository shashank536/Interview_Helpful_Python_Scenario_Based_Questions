"""
Longest Word

#sentence = "Anirudh is learning Python programming every single day"

Take a sentence as input. Print the longest word in it."""


def longest_word(sentence):
    words = sentence.split()
    longestCount = 0
    longestWord = ""
    for i in words:
        if len(i) > longestCount:
            longestCount = len(i)
            longestWord = i
    print(longestWord)


longest_word("Anirudh is learning Python programming every single day")
