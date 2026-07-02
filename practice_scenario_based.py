# Write a Python program to do arithmetical operations addition and division.?

# def addOrDivision(a,b):
#     add = a+b
#     div = a/b
#     return add, div
#
# add, div = addOrDivision(1,2)
# print(add)
# print(div)

# 3.	Write a Python program to find the area of a triangle?
# formula 1/2*(b*h)

# def findAreaOfTriangle(b,h):
#     return (1/2)*b*h
#
# print(findAreaOfTriangle(2,3))

# 4.	Write a Python program to swap two variables?

# def swapVariable(a, b):
#     print(f"before swapping a = {a}, b = {b}")
#     a, b = b, a
#     print(f"after swapping a = {a}, b = {b}")
#     return a, b
#
# swapVariable(1,2)


# 5.	Write a Python program to generate a random number?
# import random
#
#
# def generateRandomNo(a, b):
#     return random.randint(a, b)
#
# print(generateRandomNo(1,100))

# 1.	Write a Python program to convert kilometers to miles?
# Formula :  Miles = 0.62*km

# def convertKmToMiles(km):
#     miles = 0.62*km
#     print(f"{km} kilometers is {miles} miles")
#
# convertKmToMiles(100)


# 2.	Write a Python program to convert Celsius to Fahrenheit?
# Formula : F = (c*9/5)+32
# def convertCelToFar(celsi):
#     f = (celsi*9/5)+32
#     print(f"{celsi} Celsius is {f} Fahrenheit")
#
# convertCelToFar(25)

# 3.	Write a Python program to display calendar?

# import calendar
#
# caalendar = calendar.calendar(2026)
# print(caalendar)

# 1.	Write a Python program to solve quadratic equation?


# 5.Write a Python program to swap two variables without temp variable?

# 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
# def checkNos():
#     while True:
#         try:
#             number = int(input("Enter a Number: "))
#             if number > 0:
#                 print(f"{number} is positive no.")
#             elif number < 0:
#                 print(f"{number} is -ve no.")
#             else:
#                 print(f"Given value is {number}")
#             break
#         except ValueError:
#             print(f"Applicable to number only. Pls enter number again")
# checkNos()

# 2.	Write a Python Program to Check if a Number is Odd or Even?

# def OddOrEven():
#     even = []
#     odd = []
#     for i in range(10):
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     return even, odd
# print(OddOrEven())

# 3.	Write a Python Program to Check Leap Year?

# 4.	Write a Python Program to Check Prime Number?
#
# def isPrime(num):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1
#     if count == 2:
#         return True
#     return False
#
#
# def oneToTenThousand():
#     for i in range(10):
#         if isPrime(i):
#             print(i, end=" ")
# oneToTenThousand()

# 1.	Write a Python Program to Find the Factorial of a Number?

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(3))

# 2.	Write a Python Program to Display the multiplication Table?
# 2 -user input
# 1-10

# def multiplicationTableOfAny(num):
#     print(f"Multiplication Table of {num} is")
#     for i in range(1,11):
#         table = num * i
#         print(f"{num}x{i} = {table}")
# multiplicationTableOfAny(2)


# 3.	Write a Python Program to Print the Fibonacci sequence?
# a = 0
# b = 1
# for i in range(10):
#     print(a, end=" ")
#     a,b = b, a+b

# 6.	Write a Python Program to Find the Sum of Natural Numbers?
#numbers in list
# def sumofno(num:list):
#     sum = 0
#     for i in num:
#         sum = sum+i
#     print(sum)
# sumofno([1,2,3,4,5])


# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
#2 inputs from user
#assign to variable
#user should not enter any letters
#throw exception and ask to re-enter no only

def calculator():
    while True:
        user_select = int(input("Pls select below operation : \n1.Addition, \n2.Subtraction, \n3.Multiplication, \n4.division:\nselect: "))
        try:
            if 1<= user_select <=4:
                num1 = int(input("Enter First Number: "))
                num2 = int(input("Enter Second Number: "))
                if user_select == 1:
                    total = num1+num2
                    print(f"Addition of 2 Numbers {num1} + {num2} is = {total}")
                elif user_select == 2:
                    total = num1-num2
                    print(f"Subtraction of 2 Numbers {num1} - {num2} is = {total}")
                elif user_select == 3:
                    total = num1*num2
                    print(f"Multiplication of 2 Numbers {num1} * {num2} is = {total}")
                elif user_select == 4:
                    if num2 == 0:
                        print("cannot divide by 0")
                    else:
                        total = num1/num2
                        print(f"division of 2 Numbers {num1} / {num2} is = {total}")
                break
            else:
                print("Pls select number between 1 to 4")
        except ValueError:
            print("Pls select only numbers")

calculator()

















