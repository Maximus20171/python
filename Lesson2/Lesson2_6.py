kol= int(input('Введите кол-во товара '))
my_list = []
my_tuple = ()
my_dict = {}
my_dict2 = {}
i =0
while i<kol:
    i+=1
    print(f'{i}-й товар:')
    my_dict['название'] = input("название ")
    my_dict['цена'] = int(input("цена "))
    my_dict['количество'] = int(input("количество "))
    my_dict['ед'] = input("ед ")
    print(my_dict)
    #my_dict2.update(i: my_dict)
    a=str(my_dict)
    print(a)
    my_dict2.update({i: a})
    print(my_dict2)
    #my_tuple += (i, a)
    #print(my_tuple)
    #my_list.append(my_tuple)
    #my_list.append(my_tuple[i])
    #my_list.append(i)
    #my_list.append(my_dict)
    #my_tuple=tuple(my_dict,)
    #my_tuple=tuple(str(my_list[i-0]+my_list[]))
print(my_list)
print(my_dict2.items())
