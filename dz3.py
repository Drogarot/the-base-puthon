# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg2 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Результат {my_func(int(input("arg1 ")), int(input("arg2 ")), int(input("arg3 ")))}')
