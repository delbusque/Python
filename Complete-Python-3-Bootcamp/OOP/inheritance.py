class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')
    def eat(self):
        print('Animal is eating')

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    def who_am_i(self):
        print('I am a dog')
    
    def bark(self):
        print('Bauww')

my_dog = Dog()
my_dog.who_am_i()
my_dog.bark()
