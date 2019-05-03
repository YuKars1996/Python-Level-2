from random import random

Val_numbers = 10
a = []
for i in range(Val_numbers):
    a.append(int(random() * 100))
    print("%3d" % a[i], end='')
print()

if a[0] > a[1]:
    min_n_1 = 0
    min_n_2 = 1
else:
    min_n_1 = 1
    min_n_2 = 0

for i in range(2, Val_numbers):
    if a[i] < a[min_n_1]:
        b = min_n_1
        min_n_1 = i
        if a[b] < a[min_n_2]:
            min_n_2 = b
    elif a[i] < a[min_n_2]:
        min_n_2 = i

print(f'Первое наименьшее число стоит на индексе [{(min_n_1 + 1)}] : {(a[min_n_1])}')
print(f'Второе наименьшее число стоит на индексе [{(min_n_2 + 1)}] : {(a[min_n_2])}')