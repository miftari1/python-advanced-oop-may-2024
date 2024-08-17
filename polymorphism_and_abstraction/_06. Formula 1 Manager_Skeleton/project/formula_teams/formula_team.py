from abc import ABC, abstractmethod
from typing import Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')
        self._budget = value

    @property
    @abstractmethod
    def team_info(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int):
        expenses, sponsors= self.team_info
        earned_money = 0
        for sponsor in sponsors.keys():
            for pos, prize in sponsors[sponsor].items():
                if race_pos <= pos:
                    earned_money += prize
                    break

        revenue = earned_money - expenses
        self.budget += revenue
        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
