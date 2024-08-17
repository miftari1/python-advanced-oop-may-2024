from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def animal_sound():
        pass


class Dog(Animal):
    @staticmethod
    def animal_sound():
        return 'woof-woof'


class Cat(Animal):
    @staticmethod
    def animal_sound():
        return 'meow'


class Snake(Animal):
    @staticmethod
    def animal_sound():
        return 'Ssssss'


animals = [Dog(), Cat(), Snake()]
for a in animals:
    print(a.animal_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]