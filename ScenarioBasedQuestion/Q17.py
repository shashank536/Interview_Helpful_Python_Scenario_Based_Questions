"""The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
Example:
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
"""


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


n = 1
result = [str(fib(i)) for i in range(n + 1)]
print(",".join(result))
