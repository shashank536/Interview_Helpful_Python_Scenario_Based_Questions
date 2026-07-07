"""Question 6:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z] #small
2. At least 1 number between [0-9] #digit
1. At least 1 letter between [A-Z] #caps
3. At least 1 character from [$#@] #spcl char
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
"""


def passwordVerifierTool(user_password):
    upper = lower = digit = spcl_char = False
    if 6 <= len(user_password) <= 12:
        for i in password:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i.isdigit():
                digit = True
            if not i.isalnum():
                spcl_char = True
        return upper and lower and digit and spcl_char
    return False


user_input = input("Enter a List Of Password: ").split(",")
valid_pwd = []
for i in user_input:
    password = i.strip()
    if passwordVerifierTool(i):
        valid_pwd.append(i)
print(",".join(valid_pwd))
