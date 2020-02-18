n = int(input('Введите целое положительное число '))
max = 0
if n > 0:
    while n > 0:
        ost = n % 10
        if ost > max:
            max = ost
        n = n // 10
    print('Максимальная цифр = ', max)
else:
    print("Число не соответсвует условию")
