# 6. Необходимо создать(не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


result = {}
with open('HW5.6.txt', 'r') as f:
    text = f.readlines()
    for line in text:
        name, lect_hours, pract_hours, lab_hours = line.split()

        temp = ''.join(e for e in lect_hours if e.isdigit())
        lect_hours_int = int(temp) if temp.isdigit() else 0

        temp = ''.join(e for e in pract_hours if e.isdigit())
        pract_hours_int = int(temp) if temp.isdigit() else 0

        temp = ''.join(e for e in lab_hours if e.isdigit())
        lab_hours_int = int(temp) if temp.isdigit() else 0

        all_hours = lect_hours_int + pract_hours_int + lab_hours_int
        result[name[:-1]] = all_hours

print(result)
