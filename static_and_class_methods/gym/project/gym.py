from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next((s for s in self.subscriptions if s.id == subscription_id), None)
        customer = next((c for c in self.customers if subscription.customer_id == c.id), None)
        trainer = next((t for t in self.trainers if subscription.trainer_id == t.id), None)
        plan = next((p for p in self.plans if subscription.exercise_id == p.id), None)
        equipment = next((e for e in self.equipment if plan.equipment_id == e.id), None)

        result = [f'{subscription}', f'{customer}', f'{trainer}', f'{equipment}', f'{plan}' ]
        return '\n'.join(result)
