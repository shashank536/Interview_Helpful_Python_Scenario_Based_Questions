# 1.Write a Python program to check if the given number is a Disarium Number?
# Input = 135
# logic = 1^1+2^2+5^3

# 2.Write a Python program to print all disarium numbers between 1 to 100?


def isdisarium(num):
    s = str(num)
    output = 0
    for i in range(len(s)):
        output = output + int(s[i]) ** (i + 1)
    return output == num


#
# for i in range(1, 101):
#     if isdisarium(i):
#         # print(i)


# 3.Write a Python program to check if the given number is Happy Number?
# 4.Write a Python program to print all happy numbers between 1 and 100?


def isHappyNumber(num):
    while True:
        output = 0
        for i in num:
            output = output + int(i) ** 2
        if output == 1:
            print("happy")
            break
        num = str(output)


for i in range(1, 101):
    if isHappyNumber(str(i)):
        print(i)
