"""
58697 - INPUT
[50000, 8000, 600, 90, 7] - OUTPUT

7*1 --10^1
9*10 -- 10^2
6*100 --10^3
8*1000 --10^4
5*10000 --10^5

length = 5


"""


def expand_number(num):
    result = []

    length = len(num)

    for i in range(length):  # 4
        digit = int(num[i])
        place = 10 ** (length - i - 1)
        result.append(digit * place)

    return result


print(expand_number("58697"))
