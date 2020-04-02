# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

whole = 5
fractional = 1.2
line = 'First race'
leaflet = ['c', '4']
my_tuple = ('2', '8')
my_dict = {'name': 'Anna', 'surname': 'Federovna'}

my_list = [whole, fractional, line, leaflet, my_tuple, my_dict]
for i in my_list:
    print(f'{i} is {type(i)}')
