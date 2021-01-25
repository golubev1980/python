# создание и печать исходного набора
my_list = [7, 5, 3, 3, 2]
print('Начальный рейтинг: ', my_list)

# создаем интервал значений
min_val, max_val = 1, 9

while True:
    try:
        elem = int(input('Введите новый элемент рейтинга (числа от 1 до 9): '))
    except ValueError:
        print("Ошибка! Это не число, попробуйте снова.")
        continue
    if min_val <= elem <= max_val:
        my_list.append(elem)
        break
    else:
        print("Ошибка! Это число за пределами указанного диапазона")
        continue

# печать результатов
print('Текущий рейтинг: ', sorted(my_list, reverse=True))
