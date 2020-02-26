def summa ():
    result_sum = 0
    k = None
    while k != '!':
        my_list = list(input('введите цифры через ПРОБЕЛ: ').split(' '))
        i = 0
        while i < len(my_list):
            if my_list[i] == '!':
                k = '!'
                break
            else:
                my_list[i] = int(my_list[i])
                result_sum += my_list[i]
                i += 1
        print('Текущая сумма =', result_sum)


summa()

