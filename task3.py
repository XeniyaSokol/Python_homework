#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input('введите число n'))
print (user_number)

sum_number = (user_number + 11*user_number + 111*user_number)

print ('Сумма: n+nn+nnn=', sum_number)






