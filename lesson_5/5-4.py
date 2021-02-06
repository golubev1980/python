from translate import Translator

translator = Translator(from_lang="en", to_lang="ru")

with open("text_4.txt", "r", encoding="utf-8") as f_1:
    with open("text_4_mod.txt", "w", encoding="utf-8") as f_2:

        while True:

            line = f_1.readline().split()

            if not line:
                break

            trans_line = translator.translate(line[0])

            line.pop(0)
            line.insert(0, trans_line)

            new_file_line = ' '.join(line)
            print(new_file_line, file=f_2)
