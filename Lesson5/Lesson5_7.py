import json

fin_rez_plus = {}
fin_rez_minus = {}
fin_rez_medium = {}
my_list = []
with open('my_file5_7.txt') as my_file:
    i = 0
    summa = 0
    for line in my_file:
        spisok = line.split()
        fin_rez = int(spisok[2]) - int(spisok[3])
        print(fin_rez)
        if fin_rez > 0:
            i += 1
            summa += fin_rez
            fin_rez_plus.update({spisok[0]: fin_rez})
        else:
            fin_rez_minus.update({spisok[0]: fin_rez})
try:
    print(f'Средняя прибыль по зарабатывающим фирмам = {summa / i}')
    fin_rez_medium.update({'average_profit': summa / i})
    my_list.append(fin_rez_plus)
    my_list.append(fin_rez_medium)
    my_list.append(fin_rez_minus)
    with open('my_file5_7.json', 'w') as my_file1:
        json.dump(my_list, my_file1)
except ZeroDivisionError:
    print('Нет фирм отработавших в +')
