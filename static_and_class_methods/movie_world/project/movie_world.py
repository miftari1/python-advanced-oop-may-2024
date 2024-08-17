from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if self.customer_capacity() > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None :
        if self.dvd_capacity() > len(self.dvds):
            self.dvds.append(dvd)

    def find_customer_by_id(self, c_id):
        customer = next((c for c in self.customers if c_id == c.id), None)
        return customer

    def find_dvd_by_id(self, d_id):
        dvd = next((d for d in self.dvds if d_id == d.id), None)
        return dvd

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)
            return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer_by_id(customer_id)
        dvd = self.find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        else:
            return f'{customer.name} does not have that DVD'

    def __repr__(self):
        info = []
        for customer in self.customers:
            info.append(f'{customer}')

        for dvd in self.dvds:
            info.append(f'{dvd}')

        return '\n'.join(info)


