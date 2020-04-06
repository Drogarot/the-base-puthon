# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных
# о пользователе одной строкой.

def user_data_func(name, surname, age, email, city, number_phone):
   print(name, surname, age, email, city, number_phone)


user_data_func(name='Ivan', surname='Vasilevich', age=30, email='mail.ru', city='Karpinsk', number_phone='8-800-3000-500')
