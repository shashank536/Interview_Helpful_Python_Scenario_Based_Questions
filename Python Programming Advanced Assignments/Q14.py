"""print first non-repeated string
input = "automation"
output = u

approach:

"""


def non_repeated(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for k, v in count.items():
        if v == 1:
            return k


print(non_repeated("automation"))

sentence = "hello world"
words = sentence.split()
result = ""
for i in words:
    result += i[0].upper() + i[1:] + " "
print(result)
