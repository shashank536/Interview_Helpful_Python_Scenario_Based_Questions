"""Question 1:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""
import math


def question1(num):
    C = 50.
    H = 30.
    result = []
    for i in num:
        q = math.sqrt((2 * C * i) / H)
        result.append(round(q))
    print(*result, sep=",")


num = list(map(int, input("Enter a Number: ").split(",")))
question1(num)
