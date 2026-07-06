"""Hamming distance is the number of characters that differ between two strings.
To illustrate:
String1: "abcbba"
String2: "abcbda"

Hamming Distance: 1 - "b" vs. "d" is the only difference.
Create a function that computes the hamming distance between two strings.
Examples
hamming_distance("abcde", "bcdef") ➞ 5

hamming_distance("abcde", "abcde") ➞ 0

hamming_distance("strong", "strung") ➞ 1
"""


def hamming_distance(text1, text2):
    if len(text1) != len(text2):
        raise ValueError(
            "Cannot count the distance between 2 text as length of text must be same"
        )
    count = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            count += 1
    return count


# alternate
"""for t1,t2 in zip(text1,text2):
        if t1!=t2:
            count+=1"""


print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
