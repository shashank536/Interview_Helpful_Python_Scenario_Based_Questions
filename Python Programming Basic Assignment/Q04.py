"""Question 4:
Write a program that accepts a sequence of
whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def remove_duplicate_and_sort(text):
    words = text.split()
    original_words = []
    for i in words:
        if i not in original_words:
            original_words.append(i)
    for i in range(len(original_words)):
        for j in range(len(original_words) - 1):
            if original_words[j] > original_words[j + 1]:
                original_words[j], original_words[j + 1] = (
                    original_words[j + 1],
                    original_words[j],
                )
    return " ".join(original_words)


print(
    remove_duplicate_and_sort(
        "hello world and practice makes perfect and hello world again"
    )
)
