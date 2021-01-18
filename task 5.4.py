# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

number_dict = {'One ': 'один', 'Two ': 'два',
               'Three ': 'три', 'Four ': 'четыре'}
line_ru = []
with open('number_file.txt', 'r') as number:
    number_str = number.readlines()
    for line in number_str:
        word_en = line.split('—')[0]
        word_ru = (number_dict[word_en])
        line_ru.append(str(word_ru + ' - ' + line.split('—')[1]))
with open('new_number_file.txt', 'w') as number_ru:
    number_ru.writelines(line_ru)
