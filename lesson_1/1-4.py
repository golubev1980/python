number = int(input('Введите любое целое положительное число: '))

while number <= 0:
    print('Число должно быть положительным и отличным от нуля!')
    number = int(input('Введите любое целое положительное число: '))

print('Вы ввели число:', number)
result = 0

while number > 0:
    number_r = number % 10
    number = number // 10
    if result < number_r:
        result = number_r

print('Самая большая цифра в числе это:', result)