kol = int(input('Сколько будет элементов в списке? '))
my_list = []
i = 0
# Заполнениение
while i < kol:
    s = input(f'Введите {i}-ый эл-нт списка: ')
    my_list.append(s)
    i += 1
print('Вот такой список', my_list)

# обработка
i = 0
while i + 1 < kol:
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print('После перестановки элементов ', my_list)
