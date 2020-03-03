# функция уберающая со строки все лишнее и получающая число
def chislo(s):
    ch = ''
    for i in s:
        if i != '(' and i != '-':
            ch += i
        else:
            break
    if ch == '':
        ch = '0'
    return int(ch)


my_dict = {}
with open('my_file5_6.txt') as my_file:
    for line in my_file:
        spisok = line.split()  # Формируем список
        for i in spisok[1:]:
            spisok[spisok.index(i)] = chislo(i)  # Форматируем цифры. Убираем лишнее
        my_dict.update({spisok[0]: sum([spisok[1], spisok[2], spisok[3]])})  # Заполняем словарь
print(my_dict)
