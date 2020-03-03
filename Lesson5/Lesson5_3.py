with open('my_file5_3.txt') as my_file:
    i = 0
    summa = 0
    for line in my_file:
        i += 1
        spisok = line.split()
        if float(spisok[1]) < 20000:
            print(spisok[0])
        summa += float(spisok[1])
    print('---------------------')
    print('Средная зарплата = ', round(summa / i, 2))
