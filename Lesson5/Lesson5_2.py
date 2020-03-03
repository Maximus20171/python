with open('my_file5_2.txt') as my_file:
    i = 0
    for line in my_file:
        i += 1
        spisok = line.split()
        print(f'{i}-ой строке {len(spisok)} слов(а)')
    print('---------------------')
    print(f'Всего {i} строк')
