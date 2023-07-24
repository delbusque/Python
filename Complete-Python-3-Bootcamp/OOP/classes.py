class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, num = 1):
        print(f'{self.name} is barking ... {num} times ! This {Dog.species} is a {self.breed} !')

my_dog = Dog('Huskie', 'Lucky', True)
your_dog = Dog(name='Buck', spots=False, breed='Shephard')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

print(your_dog.breed)
print(your_dog.name)
print(your_dog.spots)

print(my_dog.species)
print(your_dog.species)

my_dog.bark(3)