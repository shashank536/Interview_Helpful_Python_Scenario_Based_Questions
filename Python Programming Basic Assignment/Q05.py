"""Question 5:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def countLettersAndDigits(user_input):
    Letters = 0
    Digits = 0
    for i in user_input:
        if i.isalpha():
            Letters += 1
        if i.isdigit():
            Digits += 1
    print(f"Letters {(Letters)}")
    print(f"Digits {(Digits)}")


user_input = input("Enter a Sentence: ")
countLettersAndDigits(user_input)
