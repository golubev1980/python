import random

dimension_m = random.randrange(2, 5)

def matrix_gen():
    gen_m = []
    for gen_1 in range(dimension_m):
        gen_m.append([])
        for gen_2 in range(dimension_m):
            gen_m[gen_1].append(random.randrange(-100, 100))
    return gen_m


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(str, self.matrix))

    def __add__(self, other):
        summ_m = []
        for add_1 in range(len(self.matrix)):
            summ_m.append([])
            for add_2 in range(len(self.matrix[0])):
                summ_m[add_1].append(self.matrix[add_1][add_2] + other.matrix[add_1][add_2])
        return summ_m


m_1 = matrix_gen()
m_2 = matrix_gen()

matrix_1 = Matrix(m_1)
matrix_2 = Matrix(m_2)
matrix_3 = Matrix(matrix_1 + matrix_2)

print(f'\nМатрица 1:\n{str(matrix_1).replace(",", " ").replace("[", "").replace("]", "")}')
print(f'\nМатрица 2:\n{str(matrix_2).replace(",", " ").replace("[", "").replace("]", "")}')
print(f'\nМатрица 3:\n{str(matrix_3).replace(",", " ").replace("[", "").replace("]", "")}')
