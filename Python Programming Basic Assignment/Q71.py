"""Write Anagram program"""


def anagram(text1, text2):
    if len(text1) == len(text2):
        if sorted(text1.lower()) == sorted(text2.lower()):
            return True
    return False


print(anagram("silent", "listen"))
print(anagram("shashank", "kumarddf"))
