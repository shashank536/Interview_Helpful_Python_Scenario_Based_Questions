"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
        # print("------------------")
        # print(j, end=" "),
        # print("&", end=" ")
    print()


# reversing the array


def reverse(num):
    result = []
    for i in range(len(num) - 1, -1, -1):
        result.append(num[i])
    print(result)


reverse([1, 2, 3, 4])
