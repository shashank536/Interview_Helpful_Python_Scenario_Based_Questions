"""
INPUT - 658488
OUTPUT - ><>=<
"""

num = "658488"
result = ""
for i in range(len(num) - 1):
    if num[i] > num[i + 1]:
        result += ">"
    elif num[i] < num[i + 1]:
        result += "<"
    else:
        result += "="
print(result)
