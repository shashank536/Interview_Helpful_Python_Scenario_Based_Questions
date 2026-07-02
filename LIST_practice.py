# 1.Write a Python Program to find sum of array?
def sumofarray(num):
    sum = 0
    for i in num:
        sum = sum + i
    print(sum)


# sumofarray([1,2,3,4,5])


# 2.Write a Python Program to find largest element in an array?
def largestNum(num):
    largest = num[0]
    for i in num:
        if i > largest:
            largest = i
    print(largest)


# largestNum([1,2,3,4,55])

# 3.Write a Python Program for array rotation?


def rotateArray(num):
    a = num[:1]
    b = num[1:]
    x = num[:-1]
    y = num[-1:]
    print(b + a)
    print(y + x)


rotateArray([1, 2, 3, 4, 55])


# 4.Write a Python Program to Split the array and add the first part to the end?
# [1,2,3,4,5,6]-->[4,5,6,1,2,3]
def firstparttoend(num):
    mid = len(num) // 2
    a = num[:mid]
    b = num[mid:]
    print(b + a)


# firstparttoend([1,2,3,4,5,6,7,8,9])

# 5.Write a Python Program to check if given array is Monotonic?
# monotonic means for current value next value should be always greater [1,2,4,5]
# increasingno.


def monotonic(num):
    isIncreasing = True
    isDecreasing = True
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            isIncreasing = False
        if num[i] < num[i + 1]:
            isDecreasing = False
    if isIncreasing or isDecreasing:
        print("yes given value is monotonic")
    else:
        print("no its not monotonic")


# monotonic([1,2,3,4])
