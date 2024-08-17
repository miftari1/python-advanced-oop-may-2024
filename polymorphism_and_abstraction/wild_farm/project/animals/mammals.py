from typing import List, Type

from project.animals.animal import Mammal
from project.food import Food, Vegetable, Meat, Fruit


class Mouse(Mammal):
    @staticmethod
    def make_sound():
        return 'Squeak'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable, Fruit]

    @property
    def weight_gain(self):
        return 0.10

    def feed(self, food: Food):
        animal_type = self.__class__.__name__
        food_type = food.__class__.__name__

        if food_type != 'Vegetable' and food_type != 'Fruit':
            return f'{animal_type} does not eat {food_type}!'
        self.food_eaten += food.quantity
        self.weight += (self.weight_gain * food.quantity)

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return 'Woof!'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self):
        return 0.40

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return 'Meow'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Vegetable, Meat]

    @property
    def weight_gain(self):
        return 0.30

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gain(self):
        return 1.00

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'