with open("text_1.txt", "a") as f_1:

    str_list = ['\nstroka_1\n', 'stroka_2\n', 'stroka_3']
    f_1.writelines(str_list)

with open("text_1.txt", "r") as f_2:

    counter = 1

    while True:

        content = f_2.readline()
        len_str = len(content.split())

        if content == str(''):
            break
        else:
            print(f'Строка № {counter} состоит из {len_str} слов')
            counter += 1
            continue

print(f'Количество строк в файле: {counter - 1}')
