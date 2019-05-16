# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

introductory = deque()
finite = deque()


numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13, 'E': 14, 'F': 15, 'G': 16,
           }

revert_numbers = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4':4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, '10': "A", '11': 'B', '12': 'C', '13': 'D',
            '14': 'E', '15': 'F', '16': 'G',
}


introductory.append(list(input('Введите первое число: ').upper()))
introductory.append(list(input('Введите второе число: ').upper()))

for element in introductory:
    ter = []
    for indElement in element:
        power = (numbers[indElement])
        length_ind = len(element) - element.index(indElement) - 1
        numso = power * (16 ** length_ind)
        ter.append(numso)
    finite.append(sum(ter))

print(f'Сумма равна: {sum(finite)}')

l = 1
for i in finite:
    l *= i
transfer = list(str(l))

for i in transfer:
    print(revert_numbers[i], end='')


