print('Нужно ввести 3 числа поочереди.')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b > a:
    if a < c < b:
        print(f'Среднее число {c}')
    else:
        print(f'Среднее число {a}')
else:
    if c < b < a:
        print(f'Среднее число {b}')
    else:
        print(f'Среднее число {c}')