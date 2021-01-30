def int_func(txt):
    return txt.capitalize()

while True:

    str = input('Введите слово: ')

    if str.islower() is True:
        print(int_func(txt=str))
        break
    else:
        continue