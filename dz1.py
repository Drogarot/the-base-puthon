# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv

name, time, salary, premium = argv

try:
    time = float(time)
    salary = float(salary)
    premium = float(premium)
    res = time * salary + premium
    print(f'Заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
