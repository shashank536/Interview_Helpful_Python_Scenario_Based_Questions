"""
A group of friends have decided to start a secret society.
The name will be the first letter of each of their names,
sorted in alphabetical order.
Create a function that takes in a list of names and returns the name of the secret society.

Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"

society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"

society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
"""


def society_name(arr):
    initials = []
    for i in arr:
        initials.append(i[0])
    # initials.sort()
    # print("".join(after_sorting))
    for i in range(len(initials)):
        for j in range(len(initials) - 1):
            if initials[j] > initials[j + 1]:
                initials[j], initials[j + 1] = initials[j + 1], initials[j]
    return "".join(initials)


print(society_name(["Adam", "Sarah", "Malcolm"]))  # AMS
print(society_name(["Harry", "Newt", "Luna", "Cho"]))  # CHLN
print(
    society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
)  # CJMPRR
