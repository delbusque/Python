class Animal():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
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
    
    def __len__(self):
        return self.age
          
    def __del__(self):
        return 'An annimal was deleted'
    
zaks = Dog('Zaks', 5)
pufi = Cat('Pufi', 2)

print(str(zaks))
print(len(pufi))

def pet_speaks(pet):
    print(pet.speak())

pet_speaks(zaks)
pet_speaks(pufi)

del(pufi)
pufii = Cat('Puffi', 22)