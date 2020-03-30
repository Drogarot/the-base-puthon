# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите любое положительное число: '))
while number < 0 or number > 99999999999999999999999:
    number = int(input('Введите любое положительное число: '))
max_number = number%10
number = number//10
while number > 0:
    if number%10 > max_number:
        max_number = number%10
    number = number//10
print(max_number, 'Наибольшая цифра в вашем введеном числе')
