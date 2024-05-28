# class Vehicle:
#     def move(self):
#         print("Vehicle moved")
#
#
# class Car(Vehicle):
#     def move(self):
#         print("Car moved")
#
#
# class Boat(Vehicle):
#     def move(self):
#         print("Boat moved")
#
#
# class Plane(Vehicle):
#     def move(self):
#         print("Plane moved")
#
#
# car = Car()
# boat = Boat()
# plane = Plane()
#
#
# transport = [car, boat, plane]
# for tr in transport:
#     tr.move()


class Shape:
    def area(self):
        print("Area of Shape")


class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        s = (1 / 2) * self.a * self.h
        print(s)


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        s = (1 / 2) * self.a * self.b
        print(s)


class Cycle(Shape):
    def __init__(self, pi, d):
        self.pi = pi
        self.d = d

    def area(self):
        s = self.pi * self.d
        print(s)


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        s = self.a ** 2
        print(s)


triangle = Triangle(5, 10)
triangle.area()
rectangle = Rectangle(10, 3)
rectangle.area()
square = Square(10)
square.area()