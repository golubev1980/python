# исходная строка
# ('nice авп ъghj jапро hjjпаро вапрghgh cool')

def int_func(word):
    latin_char = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_char) else False

words = input('Введите строку из слов, разделенных пробелом: ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')