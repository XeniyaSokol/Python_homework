# 3.Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


salary = []
with open('staff.txt', 'r') as staff:
    text = staff.readlines()
    number_lines = len(text)
    for line in text:
        sal = int(line.split(' ')[1])
        salary.append(sal)
        if sal < 20000:
            print(line.split(' ')[0])
print(sum(salary)/number_lines)
