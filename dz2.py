time_sec = int(input('Введите время в секундах: '))
hours = time_sec // 3600
residue = time_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f'Введёное вами время: {hours}:{minutes}:{sec}')