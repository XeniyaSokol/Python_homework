#1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
 #платы сотрудника. В расчете необходимо использовать формулу: 
 #(выработка в часах * ставка в час) + премия. 
 #Для выполнения расчета для конкретных значений необходимо запускать скрипт 
 #с параметрами.

from sys import argv 

a, hour, rate_hour, bonus = argv

print (a)
print (hour)
print (rate_hour)
print (bonus)

def salary (hour, rate_hour, bonus ) :
    res_salary = ((hour * rate_hour) + bonus)
    return res_salary
print (salary(int(hour), int(rate_hour), int(bonus)))

