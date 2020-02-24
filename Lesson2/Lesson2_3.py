month = int(input('Введите месяц от 1 до 12 '))
my_list = ['зима', 'весна', 'лето', 'осень']
if month >= 1 and month <= 12:
    print('Решение для Cписка: ', end='')
    if month == 12 or month < 3:
        print(my_list[0])
    if month >= 3 and month < 6:
        print(my_list[1])
    if month >= 6 and month < 9:
        print(my_list[2])
    if month >= 9 and month < 12:
        print(my_list[3])

    my_dict = {1: 'Зима',
               2: 'Эима',
               3: 'Весна',
               4: 'Весна',
               5: 'Весна',
               6: 'Лето',
               7: 'Лето',
               8: 'Лето',
               9: 'Осень',
               10: 'Осень',
               11: 'Осень',
               12: 'Зима',
               }
    print("Решение для Словаря: ", my_dict[month])
