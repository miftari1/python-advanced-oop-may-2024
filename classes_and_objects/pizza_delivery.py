class PizzaDelivery:
    def __init__(self, name:str, price:float, ingredients:dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient not in self.ingredients.keys():
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        cost_ingredient = quantity * price_per_quantity
        self.price += cost_ingredient

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f'Pizza {self.name} already prepared, and we can\'t make any changes!'
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        elif quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'
        else:
            self.ingredients[ingredient] -= quantity
            cost_ingredient = quantity * price_per_quantity
            self.price -= cost_ingredient

    def make_order(self):
        self.ordered = True
        ingredients_list = []
        for k, v in self.ingredients.items():
            ingredients_list.append(f'{k}: {v}')
        return f'You\'ve ordered pizza {self.name} prepared with {", ".join(ingredients_list)} '\
               f'and the price will be {self.price}lv.'

    def ordered_message(self):
        print(f'Pizza {self.name} already prepared, and we can\'t make any changes!')


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))