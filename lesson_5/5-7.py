def str_to_num(str):
    str = str.strip()
    if str.isdigit():
        return int(str)

import json

profit_dict = {}
average_dict = {}
profit_list = []

with open("text_7.txt", "r", encoding="utf-8") as f_1:

    while True:

        line = f_1.readline()
        str_list = line.split(' ')

        if not line:
            break

        org_name = str_list[0]

        money_list = []

        for i in str_list:
            n = str_to_num(i)
            if n is not None:
                money_list.append(str_to_num(i))

        profit = int(money_list[0]) - int(money_list[1])

        if profit > 0:
            profit_list.append(profit)
            profit_dict[org_name] = profit
        elif profit < 0:
            profit_dict[org_name] = profit

org_name = str('average_profit')
average = sum(profit_list) / len(profit_list)

average_dict[org_name] = average

profit_list.clear()
profit_list.append(profit_dict.copy())
profit_list.append(average_dict.copy())
print(f'Средняя прибыль по всем фирмам с положительным балансом: {average}')
print(profit_list)

with open("text_77.json", "w", encoding="utf-8") as write_f:
    json.dump(profit_list, write_f, ensure_ascii=False, indent=4)
