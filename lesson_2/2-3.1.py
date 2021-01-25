# создаем список
my_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень',
           'Осень', 'Осень', 'Зима']

# создаем интервал значений
min_val, max_val = 1, 12

# задаем начальное значение переменной
elem = 0

while True:
    try:
        elem = int(input('Введите месяц в виде целого числа от 1 до 12: '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    if min_val <= elem <= max_val:
        break
    else:
        print("Ошибка! Это число за пределами указанного диапазона")
        continue

# печатаем результат
print(f'Вы указали {elem}-й месяц. Время года {my_list[elem - 1]}')
