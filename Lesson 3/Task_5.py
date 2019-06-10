from random import random

M = 10
Val_numbers = 5
a = []
for i in range(Val_numbers):
    b = []
    for j in range(M):
        n = int(random() * 300)
        b.append(n)
        print(f'{n}', end=' | ')
    a.append(b)
    print()

mx = -1
for j in range(M):
    mn = 200
    for i in range(Val_numbers):
        if a[i][j] < mn:
            mn = a[i][j]
    if mn > mx:
        mx = mn
print(f'Максимальное число среди минимальных: {mx}')