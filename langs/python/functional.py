from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model'])

def create_car(brand, model):
    return Car(brand, model)

def drive_car(car):
    return f'{car.brand} {car.model} is driving'

def stop_car(car):
    return f'{car.brand} {car.model} stopped'

car = create_car("Toyota", "Camery")
print(drive_car(car))
print(stop_car(car))