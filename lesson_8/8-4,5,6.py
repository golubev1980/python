class Storage:
    def __init__(self):
        self.storage_dict = {}

    def add(self, equipment):
        self.storage_dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name, pos):
        if self.storage_dict[name]:
            self.storage_dict.setdefault(name).pop(pos)

    def rebuild_print(self):
        storage.extract('Printer', 0)
        storage.extract('Printer', 0)
        storage.extract('Printer', 0)
        printer1 = Printer('Принтер HP', 'A4', 10000, hp_print_counter)
        storage.add(printer1)
        printer2 = Printer('Принтер Canon', 'A3', 30000, canon_print_counter)
        storage.add(printer2)
        printer3 = Printer('Принтер Xerox', 'A4', 8000, xerox_print_counter)
        storage.add(printer3)
        print(input_21)

    def rebuild_scan(self):
        storage.extract('Scaner', 0)
        storage.extract('Scaner', 0)
        storage.extract('Scaner', 0)
        scaner1 = Scaner('Сканер HP', 'A4', 5000, hp_scan_counter)
        storage.add(scaner1)
        scaner2 = Scaner('Сканер Canon', 'A3', 20000, canon_scan_counter)
        storage.add(scaner2)
        scaner3 = Scaner('Сканер Xerox', 'A4', 6000, xerox_scan_counter)
        storage.add(scaner3)
        print(input_21)

    def rebuild_copy(self):
        storage.extract('Xerox', 0)
        storage.extract('Xerox', 0)
        storage.extract('Xerox', 0)
        xerox1 = Scaner('Копир HP', 'A4', 7000, hp_copy_counter)
        storage.add(xerox1)
        xerox2 = Scaner('Копир Canon', 'A3', 50000, canon_copy_counter)
        storage.add(xerox2)
        xerox3 = Scaner('Копир Xerox', 'A4', 5000, xerox_copy_counter)
        storage.add(xerox3)
        print(input_21)


class Equipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.price} {self.quantity}'


class Printer(Equipment):
    def __init__(self, name, print_format, price, quantity):
        super().__init__(name, price, quantity)
        self.print_format = print_format

    def __repr__(self):
        return f'\nМодель: {self.name}' \
               f'\nФормат печати: {self.print_format}' \
               f'\nЦена: {self.price}' \
               f'\nКоличество: {self.quantity}'


class Scaner(Equipment):
    def __init__(self, name, scan_format, price, quantity):
        super().__init__(name, price, quantity)
        self.scan_format = scan_format

    def __repr__(self):
        return f'\nМодель: {self.name}' \
               f'\nФормат скана: {self.scan_format}' \
               f'\nЦена: {self.price}' \
               f'\nКоличество: {self.quantity}'


class Xerox(Equipment):
    def __init__(self, name, copy_format, price, quantity):
        super().__init__(name, price, quantity)
        self.copy_format = copy_format

    def __repr__(self):
        return f'\nМодель: {self.name}' \
               f'\nФормат копии: {self.copy_format}' \
               f'\nЦена: {self.price}' \
               f'\nКоличество: {self.quantity}'


class Menu():
    def __init__(self, quest, num_1, num_2, num_3, num_4, var_1, var_2, var_3, var_4):
        self.quest = quest
        self.num_1 = num_1
        self.num_2 = num_2
        self.num_3 = num_3
        self.num_4 = num_4
        self.var_1 = var_1
        self.var_2 = var_2
        self.var_3 = var_3
        self.var_4 = var_4

    def choice(self):

        while True:

            ans = input(f'\n{self.quest} ({self.num_1}-{self.var_1};'
                        f' {self.num_2}-{self.var_2};'
                        f' {self.num_3}-{self.var_3};'
                        f' {self.num_4}-{self.var_4}): ')

            try:
                ans = int(ans)
            except ValueError:
                print("Вы ввели значение вне предложенного диапазона")
                continue
            if ans != self.num_1 and ans != self.num_2 and ans != self.num_3 and ans != self.num_4:
                print("Вы ввели значение вне предложенного диапазона")
                continue
            elif ans == 0:
                print("Завершение работы...")
                break
            elif ans == 1:
                return self.num_1
            elif ans == 2:
                return self.num_2
            elif ans == 3:
                return self.num_3


# заполняем склад оргтехникой
storage = Storage()

# принтеры
hp_print_counter = 1
canon_print_counter = 1
xerox_print_counter = 1
printer1 = Printer('Принтер HP', 'A4', 10000, hp_print_counter)
storage.add(printer1)
printer2 = Printer('Принтер Canon', 'A3', 30000, canon_print_counter)
storage.add(printer2)
printer3 = Printer('Принтер Xerox', 'A4', 8000, xerox_print_counter)
storage.add(printer3)

# сканеры
hp_scan_counter = 1
canon_scan_counter = 1
xerox_scan_counter = 1
scaner1 = Scaner('Сканер HP', 'A4', 5000, hp_scan_counter)
storage.add(scaner1)
scaner2 = Scaner('Сканер Canon', 'A3', 20000, canon_scan_counter)
storage.add(scaner2)
scaner3 = Scaner('Сканер Xerox', 'A4', 6000, xerox_scan_counter)
storage.add(scaner3)

# копиры
hp_copy_counter = 1
canon_copy_counter = 1
xerox_copy_counter = 1
xerox1 = Xerox('Копир HP', 'A4', 7000, hp_copy_counter)
storage.add(xerox1)
xerox2 = Xerox('Копир Canon', 'A3', 50000, canon_copy_counter)
storage.add(xerox2)
xerox3 = Xerox('Копир Xerox', 'A4', 5000, xerox_copy_counter)
storage.add(xerox3)

while True:

    answer_1 = Menu('Выберите действие', 1, 2, 3, 0,
                    'Статистика по складу',
                    'Добавить оборудование на склад',
                    'Выдать со склада в подразделение компании',
                    'Завершение работы')

    input_1 = answer_1.choice()

    # статистика по складу
    if input_1 == 1:
        print(input_1)
        print(f'\nСтатистика по складу:\n{"*" * 20}')
        print('\nПринтеры:')
        for item in storage.storage_dict.setdefault('Printer'):
            print(f'{item}')
        print('\nСканеры:')
        for item in storage.storage_dict.setdefault('Scaner'):
            print(f'{item}')
        print('\nКопиры:')
        for item in storage.storage_dict.setdefault('Xerox'):
            print(f'{item}')
        continue

    # добавление оборудования на склад
    if input_1 == 2:
        print(input_1)
        answer_2 = Menu('Какое оборудование добавить на склад? ', 1, 2, 3, 0,
                        'Принтер', 'Сканер', 'Копир', 'Завершение работы')

        input_2 = answer_2.choice()

        if input_2 == 1:
            print(input_2)
            answer_21 = Menu('Выберите принтер: ', 1, 2, 3, 0,
                            'Принтер HP', 'Принтер Canon', 'Принтер Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_print_counter += 1
                storage.rebuild_print()
                print('Принтер добавлен...')
                continue
            elif input_21 == 2:
                canon_print_counter += 1
                storage.rebuild_print()
                print('Принтер добавлен...')
                continue
            elif input_21 == 3:
                xerox_print_counter += 1
                storage.rebuild_print()
                print('Принтер добавлен...')
                continue

        if input_2 == 2:
            print(input_2)
            answer_21 = Menu('Выберите сканер: ', 1, 2, 3, 0,
                             'Сканер HP', 'Сканер Canon', 'Сканер Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_scan_counter += 1
                storage.rebuild_scan()
                print('Сканер добавлен...')
                continue
            elif input_21 == 2:
                canon_scan_counter += 1
                storage.rebuild_scan()
                print('Сканер добавлен...')
                continue
            elif input_21 == 3:
                xerox_scan_counter += 1
                storage.rebuild_scan()
                print('Сканер добавлен...')
                continue

        if input_2 == 3:
            print(input_2)
            answer_21 = Menu('Выберите копир: ', 1, 2, 3, 0,
                             'Копир HP', 'Копир Canon', 'Копир Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_copy_counter += 1
                storage.rebuild_copy()
                print('Копир добавлен...')
                continue
            elif input_21 == 2:
                canon_copy_counter += 1
                storage.rebuild_copy()
                print('Копир добавлен...')
                continue
            elif input_21 == 3:
                xerox_copy_counter += 1
                storage.rebuild_copy()
                print('Копир добавлен...')
                continue

    # выдача со склада в подразделение компании
    if input_1 == 3:
        print(input_1)
        answer_2 = Menu('Какое оборудование выдать со склада? ', 1, 2, 3, 0,
                        'Принтер', 'Сканер', 'Копир', 'Завершение работы')

        input_2 = answer_2.choice()

        if input_2 == 1:
            print(input_2)
            answer_21 = Menu('Выберите принтер: ', 1, 2, 3, 0,
                             'Принтер HP', 'Принтер Canon', 'Принтер Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_print_counter -= 1
                if hp_print_counter < 0:
                    hp_print_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_print()
                    print('Принтер выдан...')
                    continue
            elif input_21 == 2:
                canon_print_counter -= 1
                if canon_print_counter < 0:
                    canon_print_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_print()
                    print('Принтер выдан...')
                    continue
            elif input_21 == 3:
                xerox_print_counter -= 1
                if xerox_print_counter < 0:
                    xerox_print_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_print()
                    print('Принтер выдан...')
                    continue

        if input_2 == 2:
            print(input_2)
            answer_21 = Menu('Выберите сканер: ', 1, 2, 3, 0,
                             'Сканер HP', 'Сканер Canon', 'Сканер Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_scan_counter -= 1
                if hp_scan_counter < 0:
                    hp_scan_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_scan()
                    print('Сканер выдан...')
                    continue
            elif input_21 == 2:
                canon_scan_counter -= 1
                if canon_scan_counter < 0:
                    canon_scan_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_scan()
                    print('Сканер выдан...')
                    continue
            elif input_21 == 3:
                xerox_scan_counter -= 1
                if xerox_scan_counter < 0:
                    xerox_scan_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_scan()
                    print('Сканер выдан...')
                    continue

        if input_2 == 3:
            print(input_2)
            answer_21 = Menu('Выберите копир: ', 1, 2, 3, 0,
                             'Копир HP', 'Копир Canon', 'Копир Xerox', 'Завершение работы')

            input_21 = answer_21.choice()

            if input_21 == 1:
                hp_copy_counter -= 1
                if hp_copy_counter < 0:
                    hp_copy_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_copy()
                    print('Копир выдан...')
                    continue
            elif input_21 == 2:
                canon_copy_counter -= 1
                if canon_copy_counter < 0:
                    canon_copy_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_copy()
                    print('Копир выдан...')
                    continue
            elif input_21 == 3:
                xerox_copy_counter -= 1
                if xerox_copy_counter < 0:
                    xerox_copy_counter = 0
                    print('На складе не осталось оборудования этого типа. Попробуйте выбрать другое.')
                    continue
                else:
                    storage.rebuild_copy()
                    print('Копир выдан...')
                    continue
    break
