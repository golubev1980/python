vir = int(input('Введите значение выручки фирмы: '))
izd = int(input('Введите значение издержек фирмы: '))

if vir > izd:
    print('Фирма имеет положительный финансовый результат')
    prib = vir - izd
    print('Прибыль составляет:', prib)
    rentab = prib / vir
    print('Рентабельность выручки составляет:', rentab)
    peoples = int(input('Введите численность сотрудников фирмы: '))
    prib_peoples = prib / peoples
    print('Прибыль фирмы в расчете на одного сотрудника:', prib_peoples)

elif vir < izd:
    print('Фирма имеет отрицательный финансовый результат')
    ubitok = izd - vir
    print('Убыток составляет: ', ubitok)

else:
    print('Выручка фирмы равна ее издержкам')