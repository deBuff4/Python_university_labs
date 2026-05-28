import arrays

print(f"\n#------------------ Вычисления с использованием библиотеки NumPy ------------------#")

print("Операции со скалярами")
print(f"\nСумма: {arrays.a + 12.5}\nРазность: {arrays.a - 10}\nСреднее значение: {arrays.a.mean()}\nМинимальное: {arrays.a.min()}\n"
      f"Максимальное: {arrays.a.max()}\nСреднее отклонение: {arrays.a.std()} ")

print(f"\nОперации с массивами")
print(f"Сумма: {arrays.a + arrays.b}, Произведение: {arrays.a * arrays.b}")

print(f"\n#------------------ Вычисления без использования библиотеки NumPy ------------------#")

# Сумма

sum_number = 5
new_array = []
for i in range(len(arrays.c)):
    new_array = arrays.c[i] + 12.5
print(f"Сумма: {new_array}")

# Среднее значение
average = 0
for i in arrays.c:
    average += i
print(f"Среднее значение: {average/(len(arrays.c))}")

# Минимальное значение

minimal = arrays.c[0]

for i in arrays.c:
    if i < minimal:
        minimal = i
    else: continue

print(f"Минимальное значение: {minimal}")

# Максимальное значение

maximal = arrays.c[0]

for i in arrays.c:
    if i > maximal:
        maximal = i
    else: continue

print(f"Максимальное значение: {maximal}")

# Среднее отклонение

avg_arithmetics = 0
f = []
for i in arrays.c:
    avg_arithmetics += i
avg_arithmetics /= len(arrays.c)

for j in arrays.c:
    f.append((j - avg_arithmetics) ** 2)

summary = 0
for s in f:
    summary += s