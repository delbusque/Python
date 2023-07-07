class Car:
    wheels = 4
    def __init__(self, model, fuel):
        self.model = model
        self.fuel = fuel

my_car = Car('Subaru', 'diesel')

print(my_car.wheels)
print(my_car.model)