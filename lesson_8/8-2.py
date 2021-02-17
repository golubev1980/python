class OwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

divisible = input('Введите делимое: ')
divisor = input('Введите делитель: ')

try:
    divisible = int(divisible)
    divisor = int(divisor)
    if divisor == 0:
        raise OwnErr("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnErr as err:
    print(err)
else:
    print(f'Все хорошо. Результат: {round((divisible / divisor), 2)}')
