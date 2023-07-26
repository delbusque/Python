class Animal():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass should implement speak abstract method')

class Dog(Animal):

    def speak(self):
        return f'{self.name} says Bauww'
    
    def __str__(self):
        return f'A dog with name {self.name}'

class Cat(Animal):

    def speak(self):
        return f'{self.name} says Meoww'
    
zaks = Dog('Zaks')
pufi = Cat('Pufi')

print(zaks)

def pet_speaks(pet):
    print(pet.speak())

pet_speaks(zaks)
pet_speaks(pufi)

zigo = Animal('Zigo')
zigo.speak()