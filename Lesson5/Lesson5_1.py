my_file = open('my_file5_1.txt', 'w')
stroka = ' '
i = 0
while stroka != '':
    i += 1
    stroka = input(f'{i}-ая строка для записи в файл ')
    my_file.write(stroka + '\n')
my_file.close()
