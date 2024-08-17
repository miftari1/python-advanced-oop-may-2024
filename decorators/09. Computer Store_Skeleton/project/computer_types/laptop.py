from math import log2

from project.computer_types.computer import Computer


class Laptop(Computer):
    @property
    def available_processors(self):
        return {'AMD Ryzen 9 5950X': 900,
                'Intel Core i9-11900H': 1050,
                'Apple M1 Pro': 1200
                }

    @property
    def valid_ram(self):
        return [2 ** n for n in range(1, int(log2(64)) + 1)]

    def __str__(self):
        return 'laptop'
