# ввод исходных данных
line = (input("Введите строку: "))

# разбиение строки по разделителю
str_list = line.split(' ')


def str_to_num(str):
    str = str.strip()
    if '.' in str and str.replace('.', '').isdigit():
        return float(str)
    elif str.isdigit():
        return int(str)

num_list = []
for i in str_list:
    n = str_to_num(i)
    if n is not None:
        num_list.append(str_to_num(i))

print(num_list)
print(sum(num_list))

# # проверка на выход
# for el in mod_str:
#     if el == str('q'):
#         print('Завершение программы...')
#         break
#     else:
#         print(el)
