from math import factorial

def fact(n):
    for el in range(1, n+1):
        yield factorial(el)

n = int(input('Введите число: '))

counter = 0
for el in fact(n):
    counter += 1
    print(f'Факториал числа {counter} равен: {el}')