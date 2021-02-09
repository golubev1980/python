import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if is_police is False:
            print(f'Машина: {self.color} {self.name}')
        else:
            print(f'Полицейская машина: {self.color} {self.name}')

    def go(self):
        return print(f'{self.color} {self.name} поехал')

    def stop(self):
        return print(f'{self.color} {self.name} остановился')

    def turn(self, direction):
        self.turn = direction
        if direction >= 50:
            return print(f'{self.color} {self.name} повернул направо')
        else:
            return print(f'{self.color} {self.name} повернул налево')

    def show_speed(self):
        return print(f'Скорость машины {self.color} {self.name} составляет {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return print(f'{self.color} {self.name} превысил скорость! Скорость машины составляет {self.speed} км/ч')
        else:
            return print(f'Скорость машины {self.color} {self.name} составляет {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return print(f'{self.color} {self.name} превысил скорость! Скорость машины составляет {self.speed} км/ч')
        else:
            return print(f'Скорость машины {self.color} {self.name} составляет {self.speed} км/ч')


class PoliceCar(Car):
    pass


print()
car_1 = Car(random.randrange(10, 120), 'Белый', 'Фольксваген', False)
car_1.go()
car_1.show_speed()
car_1.turn(random.randrange(1, 101))
car_1.stop()

print()
towncar_1 = TownCar(random.randrange(10, 90), 'Черный', 'БМВ', False)
towncar_1.go()
towncar_1.show_speed()
towncar_1.turn(random.randrange(1, 101))
towncar_1.stop()

print()
workcar_1 = WorkCar(random.randrange(10, 70), 'Синий', 'Трактор', False)
workcar_1.go()
workcar_1.show_speed()
workcar_1.turn(random.randrange(1, 101))
workcar_1.stop()

print()
sportcar_1 = SportCar(random.randrange(100, 150), 'Фиолетовый', 'Ламборгини', False)
sportcar_1.go()
sportcar_1.show_speed()
sportcar_1.turn(random.randrange(1, 101))
sportcar_1.stop()

print()
policecar_1 = PoliceCar(random.randrange(10, 150), 'Черный', 'Джип Гранд Чероки', True)
policecar_1.go()
policecar_1.show_speed()
policecar_1.turn(random.randrange(1, 101))
policecar_1.stop()
