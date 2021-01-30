num = 0
stop = 0

def str_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)

while stop != 1:

    line = (input('Введите строку (q - для выхода): '))

    str_list = line.split(' ')

    num_list = []
    for i in str_list:
        n = str_to_num(i)
        if n is not None:
            num_list.append(str_to_num(i))

    num = num + sum(num_list)

    print(f'Сумма введенных чисел: {sum(num_list)}')
    print(f'Общая сумма: {num}')

    for stop in str_list:
        if stop == ('q') or stop == ('Q'):
            print('Завершение программы...')
            stop = 1
            break