from random import random

x = round(random() * 100)
i = 0
print('Угадай число с 10 попыток!')

while i < 10:
    answer = int(input('Введи число от 0 до 100: '))
    if answer > x:
        print('Много!')
    elif answer < x:
        print('Мало!')
    else:
        print(f'Ура! Это число {x}. Вы угадали с {i} попытки')
        break
    i += 1
else:
    print(f'Попытки кончились. Загаданное число: {x}')