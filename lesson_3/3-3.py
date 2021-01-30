def third_func(par1, par2, par3):
    """Возвращает сумму наибольших двух аргументов.

        Позиционные аргументы:
        par1 -- 1-й аргумент
        par2 -- 2-й аргумент
        par3 -- 3-й аргумент

        """
    if (par2 + par3) < (par1 + par2) > (par1 + par3):
        result = (par1 + par2)
    elif (par1 + par2) <= (par2 + par3) >= (par1 + par3):
        result = (par2 + par3)
    else:
        result = (par1 + par3)
    return result

while True:
    try:
        arg1 = int(input('Введите 1-й аргумент: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    else:
        break

while True:
    try:
        arg2 = int(input('Введите 2-й аргумент: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    else:
        break

while True:
    try:
        arg3 = int(input('Введите 3-й аргумент: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    else:
        break

print(f"Cумма наибольших двух аргументов равна: {third_func(par1=arg1, par2=arg2, par3=arg3)}")