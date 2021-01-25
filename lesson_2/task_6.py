number = 1
goods_list = []

# заполняем список данными
while True:
    name = input('Введите название: ')
    price = input('Введите цену: ')
    quantity = input('Введите количество: ')
    unit = input('Введите единицу измерения: ')
    my_dict = {'название': name, 'цена': price, 'количество': quantity, 'eд': unit}
    my_tuple = (number, my_dict.copy())
    goods_list.append(my_tuple)
    elem = input('Для продолжения введите любое значение и нажмите Enter (0 - для окончания ввода): ')
    number += 1
    if elem == str(0):
        break

# печатаем структуру товаров
print(goods_list)

# здесь должна была быть моя аналитика... :-(


