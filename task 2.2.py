# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

 l = list(input('enter the list'))
 i = 0

 while i < len(l) -1 :
     a = l[i]
     l[i] = l[i+1]
     l[i+1] = a
     i+=2
 print(l)