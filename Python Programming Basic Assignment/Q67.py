"""Take a username as input. Strip any spaces from both sides and check if the
cleaned name starts with a letter (not a digit). Print "Valid" or "Invalid"."""


def validate(username):
    user = username.strip()
    if user[0].isdigit():
        return "invalid"
    return "Valid"


print(validate(" 1shashank"))
