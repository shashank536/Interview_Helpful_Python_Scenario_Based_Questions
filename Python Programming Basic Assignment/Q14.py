"""Define a class named Shape and its subclass Square.
The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
formula area = length*length"""


class Shape:
    def area(self):
        print(f"Area = {0}")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(f"Area = {self.length * self.length}")


obj = Shape()
obj.area()
obj1 = Square(10)
obj1.area()
