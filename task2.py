#2. Пользователь вводит время в секундах. Переведите время в часы, 
#минуты и секунды и выведите в формате чч:мм:сс.Используйте форматирование строк.


time_user = int(input('введите время в секундах'))

time_mm = time_user // 60
time_hh = time_mm // 60
time_ss = time_user % 60

total_time = '{} : {} : {}'.format (time_hh, time_mm, time_ss)

print(type(total_time))
print (total_time)