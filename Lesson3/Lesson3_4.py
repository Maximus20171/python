def my_func(x,y):
    x1=x
    for t in range(-1,y,-1):
        x=x1*x
    return 1/x

x = float(input('Введите Х '))
y = int(input('Введите отрицательну степень числа Х '))
if y<0:
    print(f'Х в степени {y} = ', (lambda x,y : x**y)(x,y))
    print(f'Х в степени {y} = ', my_func(x,y))
else:
    print('ВВЕДИТЕ ОТРИЦАТЕЛЬНУЮ СТЕПЕНЬ')