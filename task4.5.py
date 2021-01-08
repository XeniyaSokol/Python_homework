#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). 
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def multiplication_reduce (prev_el,el):
    return prev_el * el
my_lst = [i for i in range(99,1001) if i % 2 == 0]
# проверка на малом кол-ве значений my_lst = [i for i in range(1,7) if i % 2 == 0]
print (reduce(multiplication_reduce, my_lst))
