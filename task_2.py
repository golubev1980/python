input_seconds = int(input('Введите любое число секунд: '))
print('Вы ввели значение', input_seconds, 'секунд')

hours = input_seconds // 3600
minutes = (input_seconds - hours * 3600) // 60
seconds = input_seconds % 60

print(f'В формате чч:мм:сс это будет равно: {hours}:{minutes}:{seconds}')