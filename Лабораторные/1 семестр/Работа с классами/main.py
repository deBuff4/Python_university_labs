# Задание 1.
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

# Задание 2.

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