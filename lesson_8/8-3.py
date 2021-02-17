class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

num_list = []

while True:

    number = input('Введите число: ')

    try:
        number = int(number)
    except ValueError:
        print("Вы ввели не число")
    except OwnErr as err:
        print(err)
    else:
        num_list.append(number)
    if number == ('stop') or number == ('STOP'):
        print(f'\nЗавершение программы...\n')
        break

print(f'Список введенных значений:\n{num_list}')