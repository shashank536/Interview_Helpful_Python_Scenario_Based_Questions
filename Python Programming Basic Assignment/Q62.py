"""
Write a function that converts a dictionary into a list of keys-values tuples. D-L(tuples,tuples)

Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]

Notes
Return the elements in the list in alphabetical order.
"""


def dict_to_list(num):
    convert_to_list = list(num.items())
    for i in range(len(convert_to_list)):
        for j in range(len(convert_to_list) - 1):
            if convert_to_list[j] > convert_to_list[j + 1]:
                convert_to_list[j], convert_to_list[j + 1] = (
                    convert_to_list[j + 1],
                    convert_to_list[j],
                )
    return convert_to_list


print(dict_to_list({"D": 1, "B": 2, "C": 3}))  # [("B", 2), ("C", 3), ("D", 1)]
print(
    dict_to_list({"likes": 2, "dislikes": 3, "followers": 10})
)  # [("dislikes", 3), ("followers", 10), ("likes", 2)]
