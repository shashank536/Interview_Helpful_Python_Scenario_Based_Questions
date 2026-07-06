"""
Write a function, that replaces all vowels in a string with a specified vowel.

Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"

Notes
All words will be lowercase. Y is not considered a vowel.
"""


def vow_replace(word, element):
    replace = ""
    for i in word:
        if i in "aeiouAEIOU":
            replace += element
        else:
            replace += i
    return replace


print(vow_replace("apples and bananas", "u"))  # "upplus und bununus"
print(vow_replace("cheese casserole", "o"))  # "chooso cossorolo"
print(vow_replace("stuffed jalapeno poppers", "e"))  # "steffed jelepene peppers"
