my_list = [7, 5, 3, 3, 2]
c = int(input('Введите число '))
i=0
while i<len(my_list) and my_list[i]>=c:
    i+=1
my_list.insert(i, c)
print(my_list)