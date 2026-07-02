# 1.Write a Python Program to Add Two Matrices?
a = [[1, 2],
     [3, 4]]
b = [[5, 6],
     [7, 8]]


result = []
for i in range(len(a)):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j]+b[i][j])
    result.append(row)
print(result)


# 1.Write a Python Program to Add Two Matrices?

a = [[1,2,3,4],[5,6,7,8]]
b = [[1,2,3,4],[5,6,7,8]]

result = []
for i in range(len(a)):
    row = []
    for j in range(len(a[0])):
        row.append(a[i][j]+b[i][j])
    result.append(row)
print(result)

# 3.Write a Python Program to Transpose a Matrix?
matrix = [[1,2,3],
          [4,5,6]]

"""output: [[1,4],
            [2,5],
            [3,6]]"""

result = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    result.append(row)
print(result)


# 4.Write a Python Program to Sort Words in Alphabetic Order?

alpha = "python java c cpp html css"
new_order = alpha.split()
new_order.sort()
print(new_order)

# 5.Write a Python Program to Remove Punctuation From a String?
import string
text = "hello! world!!"
result = ""
for i in text:
    if i not in string.punctuation:
        result = result+i
print(result)



matrix = [[4,5,6,9],
          [7,8,9,9]]
result =[]
for i in range(len(matrix[0])): #4
    row =[]
    for j in range(len(matrix)): #2
        row.append(matrix[j][i])
    result.append(row)
print(result)















