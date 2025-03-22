class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_year(self):
        return f"{self.year}"
    def get_model(self):
        return f"{self.model}"
    def get_make(self):
        return f"{self.make}"        

car1 = Car("Toyota", "Corolla", 2020)

print(car1.get_year())
print(car1.get_model())
print(car1.get_make())