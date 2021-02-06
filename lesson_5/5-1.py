f_1 = open("text_1_mod.txt", 'w')

while True:
    string = input('Введите любую строку данных: ')
    f_1 = open("text_1_mod.txt", 'a')
    if string == str(''):
        f_1.close()
        break
    else:
        f_1.write(string)
        f_1.write('\n')
        continue
