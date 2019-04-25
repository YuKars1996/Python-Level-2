x = int(input('Сколько чисел будете вводить: '))
y = int(input('Какую цифру будем считать: '))
i = 0

for n in range(1, x + 1):
    number = int(input('Введи число: '))
    while number > 0:
        if number % 10 == y:
            i += 1
        number = number // 10
print(f'Цифра {y} вывелась {i} раз.')