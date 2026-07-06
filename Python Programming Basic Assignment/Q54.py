"""
Create a function that sorts a list and removes all duplicate items from it.

Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]

setify([4, 4, 4, 4]) ➞ [4]

setify([5, 7, 8, 9, 10, 15]) ➞ [5, 7, 8, 9, 10, 15]

setify([3, 3, 3, 2, 1]) ➞ [1, 2, 3]
"""


def setify(arr):
    seen = []
    for i in arr:
        if i not in seen:
            seen.append(i)
    for i in range(len(seen)):
        for j in range(len(seen) - 1):
            if seen[j] > seen[j + 1]:
                seen[j], seen[j + 1] = seen[j + 1], seen[j]
    return seen


print(setify([1, 3, 3, 5, 5]))  # [1, 3, 5]
print(setify([4, 4, 4, 4]))  # [4]
print(setify([5, 7, 8, 9, 10, 15]))  # [5, 7, 8, 9, 10, 15]
print(setify([3, 3, 3, 2, 1]))  # [1, 2, 3]
