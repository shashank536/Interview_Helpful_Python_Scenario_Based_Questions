"""Define a class Person and its two child classes:
Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class."""


class Person:
    def __init__(self):
        pass

class Male(Person):
    def getGender(self):
        print(f"Gender is Male")

class Female(Person):
    def getGender(self):
        print(f"Gender is Female")

male = Male()
female = Female()
male.getGender()
female.getGender()
