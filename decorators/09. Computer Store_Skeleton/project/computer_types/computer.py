from abc import ABC, abstractmethod
from math import log, log2


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError('Manufacturer name cannot be empty.')
        self.__manufacturer = value
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError('Model name cannot be empty.')
        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def valid_ram(self):
        pass

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(f'{processor} is not compatible'
                             f' with {self.__str__()} {self.manufacturer} {self.model}!')
        if ram not in self.valid_ram:
            raise ValueError(f'{ram}GB RAM is not compatible'
                             f' with {self.__str__()} {self.manufacturer} {self.model}!')

        ram_price = int(log2(ram)) * 100
        processor_price = self.available_processors[processor]

        self.ram = ram
        self.processor = processor
        self.price += ram_price + processor_price

        return f'Created {self.__repr__()} for {self.price}$.'

    def __repr__(self):
        return f'{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM'
