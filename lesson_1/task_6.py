print('Спортсмен занимается ежедневными пробежками...')

day_1 = int(input('Введите километраж спортсмена в первый день, км: '))
day_n = int(input('Введите целевой километраж спортсмена, км: '))
day_counter = 1

print('Результаты:')
print(day_counter, 'день: ' "%.2f" % (day_1), 'км')

while day_1 < day_n:
    day_1 = day_1 + (day_1*0.1)
    day_counter +=1
    print(day_counter, 'день: ' "%.2f" % (day_1), 'км')

print('Ответ: На', day_counter, 'день спортсмен достиг результата не менее', day_n, 'км')