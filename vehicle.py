import time

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"Starting the engine of {self.make} {self.model} ({self.year})...")
        time.sleep(2)
        print("Mesin Menyala!\n")


class Car(Vehicle):
    def start_engine(self):
        print(f"Menyalakan Mesin Mobil: {self.make} {self.model} ({self.year})...")
        time.sleep(2)
        print("Vroom! Mesin Mobil Menyala!\n")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"Menyalakan Mesin Motor: {self.make} {self.model} ({self.year})...")
        time.sleep(2)
        print("Vroom! Mesin Motor Menyala!\n")


# Membuat objek Car
car = Car("Toyota", "Camry", 2022)
car.start_engine()

# Membuat objek Motorcycle
motorcycle = Motorcycle("Honda", "CBR500R", 2021)
motorcycle.start_engine()
