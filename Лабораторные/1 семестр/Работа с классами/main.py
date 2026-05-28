# Задание 1. Базовый класс и методы

#    1. Определите класс Book, который имеет три атрибута: title (название), author (автор), и year (год издания).
#    2. Добавьте метод get_info(), который возвращает информацию о книге в формате: "Название книги: [title], Автор: [author], Год издания: [year]".

class  Book:
    title = None
    author = None
    year = None

    def get_info(self):
        print(f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}')

book1 = Book()
book1.title = "Мастер и Маргарита"
book1.author = "Михаил Булгаков"
book1.year = 1967

book1.get_info()

# Задание 2.Работа с конструктором

#    1. Определите класс Circle для представления круга.
#    2. Используйте конструктор __init__ для инициализации радиуса круга (radius).
#    3. Добавьте метод get_radius(), который возвращает значение радиуса.
#    4. Добавьте метод set_radius(new_radius), который позволяет изменить радиус круга.
#    5. Создайте объект класса Circle, измените его радиус и выведите новый радиус на экран

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

print("Задание 2.")
radius1 = Circle(15)
print("Радиус: ", radius1.get_radius())
radius1.set_radius(33)
print("Новый радиус: ", radius1.get_radius())
