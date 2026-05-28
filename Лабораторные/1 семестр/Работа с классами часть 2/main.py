# РАБОТАЕТ!!!
print("Задание 1. ")

class UserAccount:

    def __init__(self, username='', email='', password=None):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, password):
        self.__password = password

    def check_password(self,password):
        return self.__password == password

user1 = UserAccount()
user1.set_password(12)
print(user1.check_password(12))

print("Задание 2.")

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        self.fuel_type = fuel_type
        super().__init__(make, model)

    def get_info(self):
        return super().get_info() + " Fuel Type: " + self.fuel_type + "."

vehicle1 = Vehicle("Audi", "A5")
car1 = Car("Mazda", "RX8", "Gas")
print(vehicle1.get_info())
print(car1.get_info())
