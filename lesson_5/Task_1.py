# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Enterprises = namedtuple('Enterprises', 'name, all_sum')
N = int(input('Введите количество компаний: '))
arr = []
i = 0

while i < N:
    name = input('Введите назнание компании: ')
    first = input('Введите прибыль за 1 квартал: ')
    second = input('Введите прибыль за 2 квартал: ')
    thirty = input('Введите прибыль за 3 квартал: ')
    four = input('Введите прибыль за 4 квартал: ')
    all_sum = sum(list(map(int, [first, second, thirty, four])))
    company = Enterprises(name, all_sum)
    print(f'Средняя сумма компании {name}: {all_sum}')
    arr.append(company)
    i += 1

s = 0
for company in arr:
    s += int(company.all_sum)

average_profit = s/N
average_up = []
average_down = []

for company in arr:
    if company.all_sum < average_profit:
        average_down.append(company.name)
    elif company.all_sum == average_profit:
        print(f'Доход {company.name} равен среднему доходу компаний.')
    else:
        average_up.append(company.name)

print(f'Средний доход по компаниям : {int(average_profit)}')
print(f'Список компаний с доходом ниже среднего: {average_down}')
print(f'Список компаний с доходом выше среднего: {average_up}')


