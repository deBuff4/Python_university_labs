# Задание 5.
# Создайте логические маски для массива NumPy и выполните фильтрацию элементов по заданному условию. Реализуйте аналогичную фильтрацию без использования NumPy.

import arrays

print(f"\n#------------------ Логические маски ------------------#\n")

mask = arrays.a > 4
print(mask)
print(arrays.a[mask])

print(f"\n#------------------ Логические маски без NumPy ------------------#\n")

mask = []

for i in arrays.c:
    if i < 4:
        mask.append(False)
    else: mask.append(True)

# print(mask)
filtered_massive = []
count = 0
for j in mask:
    if j:
        filtered_massive.append(arrays.c[count])
    else: continue
    count += 1

print(f"Массив: {arrays.c}\nУсловие: array > 4\nМаска: {mask}\nФильтрованный массив: {filtered_massive}")
