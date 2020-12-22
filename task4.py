#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
#Для решения используйте цикл while и арифметические операции.

user_number = int(input('Введите целое положительное число'))

count = len(str(user_number))
i = 0
max_number = 0

while i < count:
    i +=1
    digit = user_number % 10
    user_number = user_number // 10 
    if max_number < digit:
        max_number =digit

print(max_number)



