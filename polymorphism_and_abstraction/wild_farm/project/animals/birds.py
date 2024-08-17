from typing import List, Type

from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self):
        return 0.25

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Hen(Bird):
    @staticmethod
    def make_sound():
        return 'Cluck'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_gain(self):
        return 0.35

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'
