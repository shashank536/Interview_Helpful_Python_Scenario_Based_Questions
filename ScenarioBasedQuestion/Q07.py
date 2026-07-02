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


def findFrequency(user_input):
    count = {}
    for i in user_input:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key in sorted(count):
        print(f"{key}:{count[key]}")


user_input = input("Enter a sentence: ").split()
findFrequency(user_input)
