from abc import ABC, abstractmethod


class BasePeak(ABC):
    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @abstractmethod
    def get_recommended_gear(self):
        pass

    @abstractmethod
    def calculate_difficulty_level(self):
        pass
