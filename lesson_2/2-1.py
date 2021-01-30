# создаем список
my_list = ["text"]

# заполняем список разными типами данных
my_list.extend([456, 45.3, 234, 32.1])
my_list.insert(0, True)
my_list.insert(4, False)
my_list.append(None)

# печатаем список
print('Имеется следующий список:', my_list)

# определяем длину списка
len_list = len(my_list)

# задаем число, равное стартовой позиции списка
number = 0

# цикл для проверки и печати типов элементов списка
while number < len_list:
    print(number, '-й элемент списка типа', type(my_list[number]))
    number += 1
