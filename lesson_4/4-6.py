from sys import argv
script_name, num = argv

from itertools import count, cycle

print("Имя скрипта: ", script_name)

count_list = []
cycle_list = []

counter_1 = 0
counter_2 = 0

for elem_1 in count(int(num)):
    if counter_1 > 10:
        break
    else:
        count_list.append(elem_1)
        counter_1 += 1

for elem_2 in cycle(count_list):
    if counter_2 > 10:
        break
    else:
        cycle_list.append(elem_2)
        counter_2 += 1

print(f'Результат работы count: {count_list}')
print(f'Результат работы cycle: {cycle_list}')