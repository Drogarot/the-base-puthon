# Программа запрашивает у пользователя строку чисел, разделенных
# пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и
# снова нажать Enter. Сумма вновь введенных чисел будет добавляться
# к уже подсчитанной сумме. Но если вместо числа вводится специальный
# символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


def my_func():
    sum_res = 0
    while True:
        if input('Выход - Q, \nНажмите Enter чтобы продолжить: ').upper() == 'Q':
            break
        else:
            number = input('Введите числа через пробел и подтвердите нажатием Enter: ').split()
        res = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                break
            else:
                res = res + int(number[i])
        sum_res = sum_res + res
        print(f'Сумма {sum_res}')
    print(f'Общая сумма введёных чисел {sum_res}')

my_func()
