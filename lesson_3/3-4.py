def my_func(x, y):
    """Возвращает результат возведения в степень отрицательного числа.

        Позиционные аргументы:
        x -- действительное положительное число
        y -- целое отрицательное число

        """
    result = 1
    while (y < 0):
        result *= 1/x
        y += 1

    return round(result, 4)

while True:
    try:
        num1 = abs(float(input('Введите действительное положительное число x: ')))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    try:
        num2 = int(input('Введите целое отрицательное число y: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    if num2 >= 0:
        print("Ошибка! Это число не является отрицательным, попробуйте снова.")
        continue
    else:
        break

print(my_func(x=num1, y=num2))
