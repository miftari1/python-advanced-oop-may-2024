from abc import ABC, abstractmethod
from typing import List, Type

from project.food import Food


class Animal(ABC):
    def __init__(self, name: str, weight: float, food_eaten: int=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def allowed_food(self) -> List[Type[Food]]:
        return [Food]

    @property
    @abstractmethod
    def weight_gain(self):
        pass

    def feed(self, food: Food):
        if type(food) not in self.allowed_food:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.food_eaten += food.quantity
        self.weight += (self.weight_gain * food.quantity)


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @abstractmethod
    def __repr__(self):
        pass


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @abstractmethod
    def __repr__(self):
        pass


