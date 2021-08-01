import math
import numpy as np


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be not empty!')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def plus(self, v):
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def dot(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalised()
            u2 = v.normalized()
            angle_in_radians = (u1.dot(u2)).acos

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return math.sqrt(sum(coordinates_squared))

    def normalised(self):
        try:
            magnitude = self.magnitude()
            magnitude1 = magnitude * 1/magnitude
            return magnitude1
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')



    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates


# v = Vector([-0.221, 7.437])
# print(v.magnitude())
#
# v = Vector([8.813, -1.331, -6.247])
# print(v.magnitude())
#
# v = Vector([5.581, -2.136])
# print(v.normalised())
#
# v = Vector([1.996, 3.108, -4.554])
# print(v.normalised())
v = Vector(np.array([[7.887], [-8.802]]))
w = Vector(np.array([[4.138], [6.776]]))
print((Vector))

