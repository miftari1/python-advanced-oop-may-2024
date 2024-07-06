class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        # If there is free space, registers an animal
        if Vet.space > 0:
            Vet.animals.append(animal_name)
            self.animals.append(animal_name)
            Vet.space -= 1
            return f'{animal_name} registered in the clinic'
        # If there is no free space
        return 'Not enough space'

    def unregister_animal(self, animal_name):
        # If the given name is in the clinic, it is removed
        if animal_name in self.animals:
            self.animals.remove(animal_name)
            Vet.animals.remove(animal_name)
            Vet.space += 1
            return f'{animal_name} unregistered successfully'
        # If not, output the corresponding message
        return f'{animal_name} not in the clinic'

    def info(self):
        number_animals = len(self.animals)
        return f'{self.name} has {number_animals} animals. {Vet.space} space left in clinic'

peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())