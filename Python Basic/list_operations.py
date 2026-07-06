# 1.	Write a Python program to find sum of elements in list?


def sumoflist():
    user = list(map(int, input("Enter a List: ")))
    sum = 0
    for i in user:
        sum = sum + i
    print(sum)


# sumoflist()

# 2.Write a Python program to  Multiply all numbers in the list?


def multiplyList():
    user = list(map(int, input("Enter a List: ")))
    sum = user[0]
    for i in user:
        sum *= i
    print(sum)


# multiplyList()


# 3.	Write a Python program to find smallest number in a list?


def smallestNoInList():
    user = list(map(int, input("Enter a List: ")))
    smallest = user[0]
    for i in user:
        if i < smallest:
            smallest = i
    print(smallest)


# smallestNoInList()


# 4.	Write a Python program to find largest number in a list?
def findLargest():
    # user = list(map(int, input("Enter a list: ")))
    user = [9, 4, 3, 10]
    largest = user[0]
    for i in user:
        if i > largest:
            largest = i
    print(largest)


# findLargest()


# 5.	Write a Python program to find second largest number in a list?
def seclargest():
    user = [3, 4, 5, 10, 55, 54]
    largest = smallest = user[0]
    for i in user:
        if i > largest:
            smallest = largest
            largest = i
        elif i > smallest and i != largest:
            smallest = i
    print(smallest)


seclargest()


# 6.Write a Python program to find N largest elements from a list?


def findNthLargest(n):
    arr = [10, 4, 20, 15, 8]
    for i in range(n):
        largest = max(arr)
        arr.remove(largest)
    print(max(arr))


findNthLargest(2)


# 9.Write a Python program to Remove empty List from List?
arr = [
    1,
    [],
    2,
    [],
    3,
    [],
    4,
    [],
]
result = []
for i in arr:
    if i != []:
        result.append(i)
print(result)

# 10.	Write a Python program to Cloning or Copying a list?
arr = [1, 2, 3]
arr1 = arr.copy()
print(arr1)


# 11.Write a Python program to Count occurrences of an element in a list?


def occurance(arr):
    occur = {}
    for i in arr:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    print(occur)


occurance([1, 2, 3, 4, 1, 2, 3])
