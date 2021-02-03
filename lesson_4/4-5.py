from functools import reduce

def my_func (prev_el, el):
    return prev_el * el

generator = [elem for elem in range(100, 1001) if elem % 2 == 0]
print(f'Список четных чисел: {generator}')
print(f'Результат умножения элементов списка: {reduce(my_func, generator)}')