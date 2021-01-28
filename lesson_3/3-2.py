def second_func(**kwargs):
    """Функция принимает несколько параметров, описывающих данные пользователя:

        Именованные аргументы:
        name -- имя
        surname -- фамилия
        birthday -- год рождения
        city -- город проживания
        email -- адрес электронной почты
        phone -- телефон

        """
    return kwargs

print('Введите нижеуказанные данные пользователя...')
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birthday = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите адрес электронной почты: ')
phone = input('Введите телефон: ')

print(second_func(name=name, surname=surname, birthday=birthday, city=city, email=email, phone=phone))