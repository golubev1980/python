my_dict = {}

with open("text_6.txt", "r", encoding="utf-8") as f_1:

    for line in f_1:
        line = line.replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('-', '0').split()

        title = line[0]
        hours = int(line[1]) + int(line[2]) + int(line[3])

        my_dict[title] = hours

print(my_dict)
