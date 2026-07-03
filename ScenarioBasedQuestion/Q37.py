"""Using list comprehensions, create a function that finds all even numbers from 1 to the given number.
Examples
find_even_nums(8) ➞ [2, 4, 6, 8]

find_even_nums(4) ➞ [2, 4]

find_even_nums(2) ➞ [2]

"""


def find_even_nums(num):
    even = [i for i in range(1, num + 1) if i % 2 == 0]
    print(even)


find_even_nums(8)
find_even_nums(4)
find_even_nums(2)
