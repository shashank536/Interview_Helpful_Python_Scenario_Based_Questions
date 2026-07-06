"""Create a function that returns the mean of all digits.

Examples
mean(42) ➞ 3

mean(12345) ➞ 3

mean(666) ➞ 6

Notes
•	The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=2).
•	The mean will always be an integer.
"""


def mean(number):
    num = str(number)
    total_is = 0
    for i in num:
        total_is += int(i)
    return total_is // len(num)


print(mean(42))  # 3
print(mean(12345))  # 3
print(mean(666))  # 6
