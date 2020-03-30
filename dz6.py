one_day = float(input('Какой ваш результат в первый день: '))
result = float(input('Чего вы хотите достичь: '))
day = 1
if one_day > result:
    print(day)
while one_day < result:
    one_day = one_day + one_day%10
    day += 1
print(day)