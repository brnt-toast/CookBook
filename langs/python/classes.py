from abc import ABC, abstractmethod

class CarInterface(ABC):
    @abstractmethod
    def drive(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(CarInterface): 
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model
        
    @property
    def full_name(self):
        return f'{self.brand} {self.model}'

    def drive(self):
        return f'{self.brand} {self.model} is driving'
    
    def stop(self):
        return f'{self.brand} {self.model} stopped'
    
class Battery:
	def __init__(self, capacity):
		self.capacity = capacity

class ElectricCar(Car, CarInterface):
    def __init__(self, brand, model, battery_capacity ):
        super().__init__(brand, model)
        self.battery= Battery(battery_capacity)
        
    def charge(self):
        return f'{self.brand} {self.model} is charging {self.battery.capacity} kWh capacity'
    
    def drive(self):
        return f"{self.brand} {self.model} is driving with electric power"

    def stop(self):
        return f"{self.brand} {self.model} stopped and parked"

car_1 = Car("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model S", 100)

print(electric_car.drive())
print(electric_car.charge())

print(car_1.brand)
print(car_1.model)
print(car_1.full_name)
print(car_1.drive())
