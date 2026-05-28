import numpy as np
import arrays
import time

print(f"\n#------------------ Количество занимаемой памяти ------------------#\n")

print(f"Тип данных int: {arrays.int_a.nbytes}")
print(f"Тип данных float: {arrays.float_a.nbytes}")

print(f"\n#------------------ Скорость выполнения инструкций ------------------#\n")


a = 20000000

python_list = list(range(a))

numpy_array = np.arange(a)
print(numpy_array)
start = time.time()
sum(python_list)
time_python = time.time() - start

start = time.time()
np.sum(numpy_array)
time_numpy = time.time() - start

print(f"Время выполнения инструкций с обычным массивом: {time_python}\nВремя выполнения инструкций с NumPy массивом: {time_numpy}")
print(f"Разница в скорости выполнения: {time_python // time_numpy}")

