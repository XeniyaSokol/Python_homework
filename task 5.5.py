# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


with open('number.txt', 'w') as number_file:
    number_file.write("1 3 9 81 27")
with open('number.txt', 'r') as number_file:
    numbers_str = number_file.readline().split(' ')
    numbers_int = [int(i) for i in numbers_str]

print(sum(numbers_int))
