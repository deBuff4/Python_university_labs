# Задание 1:  Защита данных пользователя

#     1. Создайте класс UserAccount, который представляет аккаунт пользователя с атрибутами: имя пользователя (username), электронная почта (email) и приватный атрибут пароль (password).
#     2. Используйте конструктор __init__ для инициализации этих атрибутов.
#     3. Реализуйте метод set_password(new_password), который позволяет безопасно изменить пароль аккаунта.
#     4. Реализуйте метод check_password(password), который проверяет, соответствует ли введённый пароль текущему паролю аккаунта и возвращает True или False.
#     5. Создайте объект класса UserAccount, попробуйте изменить пароль и проверить его с помощью методов set_password и check_password.

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

# Задание 2: Полиморфизм и наследование

#     1. Определите базовый класс Vehicle с атрибутами: make (марка) и model (модель), а также методом get_info(), который возвращает информацию о транспортном средстве.
#     2. Создайте класс Car, наследующий от Vehicle, и добавьте в него атрибут fuel_type (тип топлива). Переопределите метод get_info() таким образом, чтобы он включал информацию о типе топлива.

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
