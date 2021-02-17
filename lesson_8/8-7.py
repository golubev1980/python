import random

class ComplexNumber:
    def __init__(self, cplx_1, cplx_2):
        self.cplx_1 = cplx_1
        self.cplx_2 = cplx_2

    def __str__(self):
        return f'{self.cplx_1}+{self.cplx_2}j' if self.cplx_2 >= 0 \
            else f'{self.cplx_1}{self.cplx_2}j'

    def __add__(self, other):
        cplx_1 = self.cplx_1 + other.cplx_1
        cplx_2 = self.cplx_2 + other.cplx_2
        return print(f'Сумма двух комплексных чисел: {cplx_1}+{cplx_2}j') if cplx_2 >= 0 \
            else print(f'Сумма двух комплексных чисел: {cplx_1}{cplx_2}j')

    def __mul__(self, other):
        cplx_1 = (self.cplx_1 * other.cplx_1) + ((self.cplx_2 * other.cplx_2) * -1)
        cplx_2 = (self.cplx_1 * other.cplx_2) + (self.cplx_2 * other.cplx_1)
        return print(f'Произведение двух комплексных чисел: {cplx_1}+{cplx_2}j') if cplx_2 >= 0 \
            else print(f'Произведение двух комплексных чисел: {cplx_1}{cplx_2}j')

a = random.randrange(-10, 10)
b = random.randrange(-10, 10)
c = random.randrange(-10, 10)
d = random.randrange(-10, 10)

complex_1 = ComplexNumber(a, b)
complex_2 = ComplexNumber(c, d)

print(f'Первое комплексное число: {complex_1}')
print(f'Второе комплексное число: {complex_2}')

sum_complex = complex_1 + complex_2
mul_complex = complex_1 * complex_2
