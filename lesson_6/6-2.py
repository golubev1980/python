class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        return f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {int((self._length * self._width * 25 * 5) / 1000)} тонн'

r_1 = Road(5000, 20)
print(r_1.asphalt())
