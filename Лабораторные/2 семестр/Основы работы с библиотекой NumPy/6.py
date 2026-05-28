# Задание 6.
# Выполните сортировку массива и определите индекс максимального элемента с использованием функций NumPy.
# Реализуйте аналогичные операции с применением стандартных средств Python.

import arrays
import numpy as np

print(f"\n#------------------ Сортировка массива и нахождение максимального значения ------------------#\n")

sorted_massive_a = np.sort(arrays.a)
max_sorted_massive = np.argmax(sorted_massive_a)
print(sorted_massive_a)
print(f"Максимальное значение массива {arrays.a}: {sorted_massive_a[max_sorted_massive]}")

print(f"\n#------------------ Сортировка массива и нахождение максимального значения  без NumPy ------------------#\n")

max_value = arrays.c[0]

for i in arrays.c:
    if max_value <= i:
        max_value = i

print(f"Максимальное значение массива {arrays.c}: {max_value}")
