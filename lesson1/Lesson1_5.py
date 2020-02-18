revenue = float(input('Выручка '))
expenses = float(input('Затраты '))
if revenue > expenses:
    print('У компании прибыль')
    P_V = (revenue - expenses) / expenses
    print(f'Рентабельность =  {P_V:.2f}')
    person = int(input('Введите кол-во сотрудников: '))
    print('Прибыль фирмы на 1 сотрудника = %.2f' % ((revenue - expenses) / person))
elif revenue < expenses:
    print('У компании убыток')
elif revenue == expenses:
    print('уже не минус но еще не плюс')
