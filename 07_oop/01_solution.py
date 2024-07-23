
class Car:
    total_car = 0

    def _init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fule_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fule_type():
        return "Electric Charge"
    
my_tesla = ElectricCar("Tesla", "Model 5", "85KWH")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))

print(isinstance(my_tesla.__brand))
print(isinstance(my_tesla.fule_type()))

my_car = Car("Tata", "Safari")
my_car.model = "City"
Car("Tata", "Nexon")

print(my_car.general_description())
print(my_car.model)

my_car1 = Car("Toyota", "Carolla")
print(my_car1.brand)
print(my_car1.model)
print(my_car1.full_name())

my_new_car = Car("BMW", "Mustang")
print(my_new_car.model)


class Battery:
    def battery_into(self):
        return "this is battery"
    

class Engine:
    def engine_into(self):
        return "this is engine"

class ElectricCar1(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCar1("Tesla", "Model S")
print(my_new_tesla.engine_into())
print(my_new_tesla.battery_into())