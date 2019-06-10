number = [0] * 8

for x in range(2, 100):
    for y in range(2, 10):
        if x % y == 0:
            number[y - 2] += 1

i = 0
while i < len(number):
    print(i + 2, ' = ', number[i])
    i += 1