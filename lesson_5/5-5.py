def str_to_num(str):
    str = str.strip()
    if str.isdigit():
        return int(str)

rand_list = []
from random import randrange
num = 0

while num < 15:
    rand_el = randrange(1000)
    rand_list.append(str(rand_el))
    num += 1

with open("text_5_mod.txt", "w", encoding="utf-8") as f_1:
    with open("text_5_mod.txt", "r", encoding="utf-8") as f_2:

        print(' '.join(rand_list), file=f_1)
        f_1.seek(0)

        line = f_2.readline()
        str_list = line.split(' ')

        num_list = []
        for i in str_list:
            n = str_to_num(i)
            if n is not None:
                num_list.append(str_to_num(i))

        print(f'Сумма чисел в файле text_5_mod.txt: {sum(num_list)}')
