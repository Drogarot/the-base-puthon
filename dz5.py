revenue = int(input('Введите сумму выручки: '))
costs = int(input('Введите сумму издержек: '))
if revenue > costs:
    profitability = revenue - costs
    rent = profitability / revenue
    print(f'Ваша фирма работает в прибыль на {profitability} ')
    worker = int(input('Сколько сотрудников в фирме: '))
    print(f'{profitability / worker} прибыль фирмы на одного сотрудника')
elif revenue < costs:
    print('Ваша фирма работает в убыток')
