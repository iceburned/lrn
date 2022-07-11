from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def calculate_perimeter(self):
        return 2 * pi * self.radius

    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())