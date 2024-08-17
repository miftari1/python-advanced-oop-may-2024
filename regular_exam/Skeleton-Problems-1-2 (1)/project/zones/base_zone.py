from abc import ABC, abstractmethod
from typing import List

from project.battleships.base_battleship import BaseBattleship


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: List[BaseBattleship] = []
        
    @property
    def code(self):
        return self._code
    
    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self._code = value

    def get_ships(self):
        return list(sorted(self.ships, key=lambda s: (s.hit_strength, -ord(s.name[0])), reverse=True))

    @abstractmethod
    def zone_info(self):
        pass
