x = int(input("Введите число: "))
evenNumbers = oddNumbers = 0

while x > 0:
    if x % 2 == 0:
        evenNumbers += 1
    else:
        oddNumbers += 1
    x = x // 10
print(f"Четных - {evenNumbers}, нечетных - {oddNumbers}")
