from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):
    def get_area(self):
        area = self.width * self.height

        return area


class AreaCalculator:

    def __init__(self, shapes: List[Shape]):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


class Triangle(Shape):
    def get_area(self):
        return (self.width * self.height) / 2


shapes = [Rectangle(1, 6), Triangle(2, 3)]

calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)