"""Question 1:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1"""


def frequency(text):
    words = text.split()
    for i in range(len(words)):
        for j in range(len(words) - 1):
            if (words[j]) > (words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]
    count = {}
    for i in words:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in count:
        print(f"{i}:{count[i]}")


frequency(
    "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
)
