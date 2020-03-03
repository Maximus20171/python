import random
# Перезаписываем файл
my_file= open('my_file5_5.txt', 'w')
my_file.close()

# А теперь сама программа
with open('my_file5_5.txt', 'a') as my_file:
    summa=0
    for i in range(1,16):
        chislo=random.randint(0,20)
        summa+=chislo
        my_file.write(str(chislo)+ ' ')
    print('Сумма чисел записанных в файл = ', summa)