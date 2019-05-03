import random

Val_numbers = 10
a = [random.randint(0, 100) for i in range(Val_numbers)]
print(a)

number = a[0]
max_value = 1

for x in range(Val_numbers - 1):
    value = 1
    for i in range(x + 1, Val_numbers):
        if a[x] == a[i]:
            value += 1
    if value > max_value:
        max_value = value
        number = a[x]
if max_value > 1:
    print(f'{max_value} раза встречается число {number}.')
else:
    print('На всех индексах уникальные числа')