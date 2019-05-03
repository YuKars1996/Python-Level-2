import random

a = [random.randint(0, 100) for i in range(20)]
print(a)

arr = []

for i in range(20):
    if a[i] % 2 == 0:
        arr.append(i)

print(f'Индексы четных элементов:  {arr}')