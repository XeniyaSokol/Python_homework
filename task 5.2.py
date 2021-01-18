# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('text_here.txt', 'r') as text_here:  # открываем файл на чтение
    row_count = sum(1 for _ in text_here)      # подсчет кол-ва строк в файле
    print(row_count)

with open('text_here.txt', 'r') as text_here:
    lines = text_here.readlines()              # читаем файл построчно
    for value in lines:                        # перебираем строки по индексу и значению
        word_count = len(value.split())
        print(word_count)
