"""Please write a binary search function which searches an item in a sorted list.
 The function should return the index of element to be searched in the list."""


def binarySearch(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1


print(binarySearch([10, 22, 35, 47, 50, 68, 75, 81, 99], 99))
