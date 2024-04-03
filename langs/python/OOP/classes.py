class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model

    def drive(self):
            return f'{self.brand} {self.model} is driving'

car_1 = Car("Toyota", "Camry")

print(car_1.brand)
print(car_1.model)
