my_dict={'one': 'один',
         'two': 'два',
         'three':'три',
         'four':'четыре',
         'five':'пять',
         'six':'шесть',
         }
with open('my_file5_4.txt') as my_file:
    with open('my_file5_4new.txt', 'w') as my_file1:
        for line in my_file:
            spisok = line.split()
            spisok[0] = my_dict.get(spisok[0].lower())
            print(f'{spisok[0].title()} - {spisok[2]}', file= my_file1)