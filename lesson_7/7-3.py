import random

class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell - other.cell >= 0:
            return self.cell - other.cell
        else:
            return abs(self.cell - other.cell)

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        return round(self.cell // other.cell)

    def make_order(self, num):
        print(f'\nКоличество ячеек второй клетки: {self.cell}')
        print(f'Количество ячеек в ряду: {num}')
        if self.cell < num:
            print('#' * (self.cell % num))
        elif self.cell == num:
            print('#' * num)
        else:
            for el_1 in range(self.cell // num):
                print('#' * num)
            print('#' * (self.cell % num))

cell_1 = Cell(random.randrange(1, 20))
cell_2 = Cell(random.randrange(1, 20))

print(f'\nКоличество ячеек первой клетки: {cell_1}')
print(f'Количество ячеек второй клетки: {cell_2}')
print(f'Сумма ячеек двух клеток: {cell_1 + cell_2}')
print(f'Разность ячеек двух клеток: {cell_1 - cell_2}')
print(f'Произведение ячеек двух клеток: {cell_1 * cell_2}')
print(f'Частное ячеек двух клеток: {cell_1 // cell_2}')
cell_2.make_order(random.randrange(2, 6))
