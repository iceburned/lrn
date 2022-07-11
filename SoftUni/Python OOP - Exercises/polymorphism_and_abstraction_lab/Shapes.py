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
        self.__radius = r

    def calculate_perimeter(self):
        return 2 * pi * self.__radius

    def calculate_area(self):
        return pi * self.__radius ** 2


class Rectangle(Shape):
    def __init__(self, h, w):
        self.__height = h
        self.__width = w

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__height + self.__width)


rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())