# создаем список
my_list = []

# заполняем список данными
while True:
    elem = input('Введите элемент списка (0 - для окончания ввода): ')
    if elem == str(0):
        break
    else:
        my_list.append(elem)
        print('Текущий вид списка: ', my_list)

# определяем длину списка
len_list = len(my_list)

# определяем четность длины списка
parity_len = len_list % 2

# счетчик попыток цикла
number = 0

while number < (len_list - parity_len):
    my_list[number+1], my_list[number] = my_list[number], my_list[number+1]
    number +=2

# печать результатов
print(my_list)
