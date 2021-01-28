def first_func(par1, par2):
    """Возвращает частное от деления.

        Позиционные аргументы:
        par1 -- делимое
        par2 -- делитель

        """
    return par1/par2

while True:
    try:
        divisible = float(input('Введите делимое: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    try:
        divisor = float(input('Введите делитель: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    try:
        print(f"Частное от деления указанных чисел равно: {round(first_func(par1=divisible, par2=divisor), 4)}")
    except ZeroDivisionError:
        print("Ошибка! Произошло деление на ноль.")
        continue
    else:
        break