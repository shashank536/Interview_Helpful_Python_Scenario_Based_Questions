"""Create a function that takes a string and returns a string with its letters in alphabetical order.
Examples
alphabet_soup("hello") ➞ "ehllo"

alphabet_soup("edabit") ➞ "abdeit"

alphabet_soup("hacker") ➞ "acehkr"

alphabet_soup("geek") ➞ "eegk"

alphabet_soup("javascript") ➞ "aacijprstv"
"""


def alphabet_soup(arr):
    char = list(arr)
    for i in range(len(char)):
        for j in range(len(char) - 1):
            if char[j] > char[j + 1]:
                char[j], char[j + 1] = char[j + 1], char[j]
    return "".join(char)


print(alphabet_soup("hello"))  # "ehllo"
print(alphabet_soup("edabit"))  # "abdeit"
print(alphabet_soup("hacker"))  # "acehkr"
print(alphabet_soup("geek"))  # "eegk"
print(alphabet_soup("javascript"))  # "aacijprstv"
