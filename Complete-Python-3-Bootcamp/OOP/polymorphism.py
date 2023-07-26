class Animal():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError('Subclass should implement speak abstract method')

class Dog(Animal):

    def speak(self):
        return f'{self.name} says Bauww'

class Cat(Animal):

    def speak(self):
        return f'{self.name} says Meoww'
    
zaks = Dog('Zaks')
pufi = Cat('Pufi')

def pet_speaks(pet):
    print(pet.speak())

pet_speaks(zaks)
pet_speaks(pufi)

zigo = Animal('Zigo')
zigo.speak()