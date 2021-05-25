'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length) + 2*(self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*(self.radius**2)
    
    def circumference(self):
        return 2 * 3.14 * self.radius

rec1 = Rectangle(4, 2)
print(rec1.area())

circ1 = Circle(9)
print(circ1.circumference())