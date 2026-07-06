"""
Write a function that takes a list and a number as arguments.
Add the number to the end of the list, then remove the first element of the list.
The function should then return the updated list.
Examples
next_in_line([5, 6, 7, 8, 9], 1) ➞ [6, 7, 8, 9, 1]

next_in_line([7, 6, 3, 23, 17], 10) ➞ [6, 3, 23, 17, 10]

next_in_line([1, 10, 20, 42 ], 6) ➞ [10, 20, 42, 6]

next_in_line([], 6) ➞ "No list has been selected"

"""

# def next_in_line(arr, element):
#     if len(arr) == 0:
#         print("No list has been selected")
#     arr.pop(0)
#     arr.append(element)
#     print(arr)


def next_in_line(arr, element):
    if len(arr) == 0:
        return "No list has been selected"

    new_list = []
    for i in range(1, len(arr)):
        new_list.append(arr[i])
    new_list.append(element)
    return new_list


print(next_in_line([5, 6, 7, 8, 9], 1))  # [6, 7, 8, 9, 1]
print(next_in_line([7, 6, 3, 23, 17], 10))  # [6, 3, 23, 17, 10]
print(next_in_line([1, 10, 20, 42], 6))  # [10, 20, 42, 6]
print(next_in_line([], 6))  # "No list has been selected"
