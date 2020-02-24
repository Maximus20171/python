words = input('введите несколько слов через ПРОБЕЛ ')
my_words = words.split(' ')
for ind, s in enumerate(my_words, 1):
    print(ind, s[:10])
