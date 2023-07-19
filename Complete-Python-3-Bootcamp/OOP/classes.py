class Dog():
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog('Huskie', 'Lucky', True)
your_dog = Dog(name='Buck', spots=False, breed='Shephard')

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

print(your_dog.breed)
print(your_dog.name)
print(your_dog.spots)