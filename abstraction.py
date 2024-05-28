from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return f" This is area of Rectangle {self.a * self.b}"

    def perimeter(self):
        return 2 * (self.a * self.b)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self): print(1 / 2 * (self.a * self.b))

    def perimeter(self): print(self.a + self.b + self.c)


class Circle:
    def __init__(self, p, r):
        self.p = p
        self.r = r

    def area(self):
        return self.p * (self.r ** 2)

    def perimeter(self):
        return 2 * (self.p * self.r)


r = Rectangle(5, 6)
# c = Circle(10, 2)
# o = Triangle(5, 2, 2)
print(r.area())
# print(r.perimeter())
# print(c.area())
# print(c.perimeter())
# print(o.area())
# print(o.area())
