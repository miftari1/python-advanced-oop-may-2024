from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance: int):
        pass

    @abstractmethod
    def refuel(self, fuel: int):
        pass

    def drive_vehicle(self, distance: int, increase: float) -> None:
        needed_fuel = distance * (self.fuel_consumption + increase)
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel_vehicle(self, fuel: int, loss: float = 0) -> None:
        fuel_loss = fuel * loss
        self.fuel_quantity += (fuel - fuel_loss)


class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def drive(self, distance: int) -> None:
        self.drive_vehicle(distance, Car.CONSUMPTION_INCREASE)

    def refuel(self, fuel: int) -> None:
        self.refuel_vehicle(fuel)


class Truck(Vehicle):
    CONSUMPTION_INCREASE = 1.6
    FUEL_LOSS = 0.05

    def drive(self, distance: int):
        self.drive_vehicle(distance, Truck.CONSUMPTION_INCREASE)

    def refuel(self, fuel: int):
        self.refuel_vehicle(fuel, Truck.FUEL_LOSS)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
