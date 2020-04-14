# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open('textdz2.txt', 'r')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
lines = 0
words = 0
for line in open('textdz2.txt'):
    lines += 1
    words += len(line.split())  #Сколько слов в каждой строке не разобрался как подсчитать
print('Lines:', lines)
print('Words:', words)
my_file.close()