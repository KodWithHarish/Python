# polymorphism
class Shape:
    width = 0
    height = 0

    def area(self):
        print('parent area class')


class Rectangle(Shape):
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area(self):
        print('area of rectangle',self.height * self.width)

class Triangle(Shape):
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area(self):
        print('area of triangle',(self.height * self.width)/2)

rectangle = Rectangle(20,40)
rectangle.area()

triangle = Triangle(10,20)
triangle.area()