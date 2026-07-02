# 1.Write a Python program to find words which are greater than given length k?
# 2.Write a Python program for removing i-th character from a string?
# 3.Write a Python program to split and join a string?
def stringOperation():
    string = "i love bangalore"
    new_str = string.split()
    print(" ".join(new_str))

stringOperation()
# 4.Write a Python to check if a given string is binary string or not?
# 5.Write a Python program to find uncommon words from two Strings?
word1 = "I love Bangalore"
word2 = "I love Python"
s1 = word1.split()
s2 = word2.split()
for i in s1:
    if i not in s2:
        print(i)
for j in s2:
    if j not in s1:
        print(j)

# 6.Write a Python to find all duplicate characters in string?
input = "programming"
seen = []
duplicates = []
for i in input:
    if i not in seen:
        seen.append(i)
    else:
        duplicates.append(i)
# print(seen)
print(duplicates)

# 7.Write a Python Program to check if a string contains any special character?
