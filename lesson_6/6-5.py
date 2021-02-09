class Stationery:

    def __init__(self, title):
        self.title = title
        print(title)

    def draw(self):
        return print('Запуск отрисовки...')


class Pen(Stationery):

    def draw(self):
        return print('Отрисовка ручкой...')


class Pencil(Stationery):

    def draw(self):
        return print('Отрисовка карандашом...')

class Handle(Stationery):

    def draw(self):
        return print('Отрисовка маркером...')


print()
draw_1 = Stationery('Канцтовары')
draw_1.draw()

print()
pen_1 = Pen('Ручка')
pen_1.draw()

print()
pencil_1 = Pencil('Карандаш')
pencil_1.draw()

print()
handle_1 = Handle('Маркер')
handle_1.draw()
