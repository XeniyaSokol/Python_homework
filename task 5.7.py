# 7. Создать(не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.


import json

profit = {}
avg_profit = {}
result = []
profit_sum = 0
above_zero_profit_count = 0
with open('firm.txt', 'r') as f:
    text = f.readlines()
    for line in text:
        name, ounership, earnings, costs = line.split()
        profit[name] = int(earnings) - int(costs)

for p in profit.values():
    if p > 0:
        profit_sum += p
        above_zero_profit_count += 1
avg_profit['average_profit'] = profit_sum/above_zero_profit_count

result.append(profit)
result.append(avg_profit)

with open('firm_result.txt', 'w') as f:
    json.dump(result, f)
