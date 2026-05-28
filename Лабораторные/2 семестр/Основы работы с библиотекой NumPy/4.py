### Прикол broadcasting в том, что с массивами n-размерности можно произвести любые математические действия, но при условии что последние размерности будут равны
import arrays

print(f"#------------------ Использование метода broadcasting ------------------#\n")

print(f"Массивы:\nf: {arrays.f}\ne:{arrays.e}")
broadcasting_summary = arrays.f + arrays.e
broadcasting_submit = arrays.e - arrays.f
print(f"Сумма: {broadcasting_summary}\nРазность: {broadcasting_submit}")

