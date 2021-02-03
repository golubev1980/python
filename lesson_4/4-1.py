def salary_func (a, b, c):
    return (int(a)*int(b))*22+int(c)

from sys import argv
script_name, prod, bid, prize = argv
print("Имя скрипта: ", script_name)
print("Производим расчет заработной платы сотрудника по нижеприведенным параметрам...")
print("Выработка в часах: ", prod)
print("Cтавка в час: ", bid)
print("Премия: ", prize)
print(f"Заработная плата сотрудника составляет: {salary_func(a=prod, b=bid, c=prize)}")