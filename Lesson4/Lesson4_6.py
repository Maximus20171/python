from itertools import count, cycle

i = int(input('Введите число с которого все начнеться '))
for el in count(i):
    if el > 100:
        break
    else:
        print(el)


с = 0
for el in cycle(['А','Б','В','С']):
    if с > 15:
        break
    print(el)
    с += 1