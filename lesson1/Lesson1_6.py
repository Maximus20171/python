a = float(input('Ввидите а '))
b = int(input('Введите b '))
if b > a:
    day = 1
    while a < b:
        print(f'{day}-й день: {a:.2f}')
        a += a * 0.1
        day += 1
    print(f'{day}-й день: {a:.2f}')
    print(f'На {day}-й день спротсмен достигнет результата - не менее {b} км')
else:
    print('Вы уже достигли этих рез-ов')
