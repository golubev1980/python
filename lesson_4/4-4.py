rand_list = []
from random import randrange
num = 0

while num < 15:
    rand_el = randrange(10)
    rand_list.append(rand_el)
    num += 1

print(f"Исходный список: {rand_list}")

new_list = [elem for elem in rand_list if rand_list.count(elem) == 1]

print(f"Результат: {new_list}")

