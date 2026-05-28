# Задание 4.
# Продемонстрируйте механизм broadcasting при выполнении арифметических операций между массивами различной формы,
# а также между массивом и скаляром. Объясните, почему реализация аналогичных операций без NumPy требует использования вложенных циклов и приводит к усложнению кода.

import arrays

print(f"#------------------ Использование метода broadcasting ------------------#\n")

print(f"Массивы:\nf: {arrays.f}\ne:{arrays.e}")
broadcasting_summary = arrays.f + arrays.e
broadcasting_submit = arrays.e - arrays.f
print(f"Сумма: {broadcasting_summary}\nРазность: {broadcasting_submit}")

