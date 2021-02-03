rand_list = []
from random import randrange
num = 0

while num < 15:
    rand_el = randrange(1000)
    rand_list.append(rand_el)
    num += 1

print(f"Исходный список: {rand_list}")

new_list = []
cnt = 0

for el in rand_list:
    if len(rand_list) == cnt + 1:
        break
    elif rand_list[cnt] < rand_list[cnt + 1]:
        el = rand_list[cnt + 1]
        new_list.append(el)
        cnt += 1
    elif rand_list[cnt] >= rand_list[cnt + 1]:
        cnt += 1

print(f"Результат: {new_list}")