def delenue(a,b):
    try:
        result = round(a/b, 2)
    except ZeroDivisionError:
        result = 'Ошибка. Деление на 0'
    return result

a=float(input('Введите А '))
b=float(input('Введите Б '))
print('А / Б = ', delenue(a,b))
