# Для простоты доступа к массивам из разных .py файлов был создан модуль arrays.py

import arrays

# Задание 1.md.
# Информация о массивах

print(f"Размерность массива {arrays.a} - {arrays.a.ndim}\nФорма массива {arrays.b} - {arrays.b.shape}\nТип данных массива {arrays.a} - {arrays.a.dtype}")

# Доступ к элементам массива

print(f"Индексация: {arrays.a[2]}\nСрезы: {arrays.b[:2, 2:]}")

