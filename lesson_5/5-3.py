def word_to_num(word):
    word = word.strip()
    if '.' in word and word.replace('.', '').isdigit():
        return float(word)

with open("text_3.txt", "r", encoding="utf-8") as f_1:

    counter = 0
    losers_list = []
    salary_list = []

    while True:

        counter += 1
        content = f_1.readline()
        word = content.split()

        for i in word:
            n = word_to_num(i)
            if n is not None:
                salary_list.append(word_to_num(i))

        if content == str(''):
            break
        elif float(word[1]) < 20000:
            losers_list.append(word[0])
        else:
            continue

    print(', '.join(losers_list), 'имеют зарплату менее 20 тыс.')
    print(f'Фонд оплаты труда составляет: {sum(salary_list)}')
    print(f'Средняя величина дохода сотрудника: {sum(salary_list) / (counter - 1)}')
