kol= int(input('Введите кол-во товара '))
my_list= []
my_dict = {}
my_anakitics = {'название': [], 'цена': [], 'количество': [], 'eд': []}
i =0
while i<kol:
    i+=1
    print(f'{i}-й товар:')
    my_dict ={'название':input("название "), 'цена':int(input("цена ")), 'количество':int(input("количество ")), 'eд': input("ед ")}
    for f in my_anakitics.keys():
        my_anakitics[f].append(my_dict[f])
    my_list.append((i, my_dict))

for t in my_list:
    print(t)

c = input('по какому пункту сделать аналитику? (название/цена/количество/ед) ')
print(f'по ключу {c}: ', my_anakitics.get(c)) if my_anakitics.get(c) else print('Нет такого парраметра')

