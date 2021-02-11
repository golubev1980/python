from abc import ABC, abstractmethod

class Clothing(ABC):

    result = 0

    def __init__(self, fabric):
        self.fabric = fabric

    @property
    @abstractmethod
    def amount_fabric(self):
        pass

    def __add__(self, other):
        Clothing.result = self.amount_fabric + other.amount_fabric
        return Costume(0)

    def __str__(self):
        return f'{Clothing.result}'

class Coat (Clothing):
    @property
    def amount_fabric(self):
        return round((self.fabric / 6.5) + 0.5)

class Costume (Clothing):
    @property
    def amount_fabric(self):
        return round((2 * self.fabric + 0.3) / 100)

coat_1 = Coat(50)
costume_1 = Costume(190)

print(f'Расход ткани для пальто 50 размера: {coat_1.amount_fabric}')
print(f'Расход ткани для костюма на рост 190: {costume_1.amount_fabric}')
print(f'Общий расход ткани: {coat_1 + costume_1}')