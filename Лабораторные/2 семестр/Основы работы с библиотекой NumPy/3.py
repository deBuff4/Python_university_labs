import arrays
import numpy as np

print(f"\n#------------------ Вычисления с использованием библиотеки NumPy ------------------#\n")

print(f"Массив : {arrays.b}")

print(f"Сложение по столбцам: {np.sum(arrays.b, axis=0)}")
print(f"Сложение по строкам: {np.sum(arrays.b, axis=1)}")
print(f"Произведение по столбцам: {np.prod(arrays.b, axis=0)}")
print(f"Произведение по строкам: {np.prod(arrays.b, axis=1)}")
print(f"Среднее арифметическое по столбцам: {np.mean(arrays.b, axis=0)}")
print(f"Среднее арифметическое по строкам: {np.mean(arrays.b, axis=1)}")

### Без библиотеки NumPy

print(f"\n#------------------ Вычисления без использования библиотеки NumPy ------------------#\n")

print(f"Массив: {arrays.d}")

# Сложение по строке

summary_array = []
for i in range(len(arrays.d[:])):
    summary = 0
    for j in range(len(arrays.d[0][:])):
    #    print (f"i = {i}, j = {j}")
        summary = summary + arrays.d[i][j]
    summary_array.append(summary)
print(f"Сумма по строке: {summary_array}")



