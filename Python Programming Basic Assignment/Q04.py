"""Question 4:
Write a program that accepts a sequence of
whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
"""


def question4(input_value):
    new_list = []
    for i in input_value:
        if i not in new_list:
            new_list.append(i)
    sorted_names = sorted(new_list)
    return " ".join(sorted_names)


input_value = input("Enter a words with white space:").split()
result = question4(input_value)
print(result)
